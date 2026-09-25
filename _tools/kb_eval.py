#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kb_eval.py —— 检索质量评估集 + 漏召回沉淀机制（防回归 / 越用越准）

三道防线：
  1. 内置用例（CASES）：A 词面 / B 自然语句 / C 关键词 / E code 场景 / F content 路由
  2. 负样本（NEGATIVES）：库里没有的主题必须 0 命中
  3. **真实漏召回沉淀**：`kb_search.py` 每遇 0 命中会写 `_index/miss_log.jsonl`；
     用 `--triage` 看未处理项，用 `--add` 把它固化成用例（就进 `_tools/eval_cases.yaml`）

用法：
  python3 kb_eval.py                    # 全量评估，不达标 exit 1
  python3 kb_eval.py --show             # 打印失败项 + 命中路径
  python3 kb_eval.py --triage           # 看真实使用中的未命中记录（待固化成用例）
  python3 kb_eval.py --add "查询" --expect "路径特征" --group B     # 固化一条用例
  python3 kb_eval.py --add "查询" --route "brand-assets" --group F  # 固化一条路由用例
"""
import argparse, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kb_search as K  # noqa: E402

KB = K.KB
EXTRA = os.path.join(HERE, "eval_cases.yaml")
MISS_LOG = os.path.join(KB, "_index", "miss_log.jsonl")

# (组, 查询, 期望命中路径特征[任一], 备注)
CASES = [
    # --- A 词面直接（基线，应 100%）---
    ("A", "按结果计费", ["术语表-AI服务商业化", "定价与计费"], "受控词别名"),
    ("A", "本体建模", ["本体建模"], "方法论条目"),
    ("A", "上下文工程", ["上下文工程"], "方法论条目"),
    ("A", "Skill 设计", ["Skill 与工具设计", "Skill设计"], "含 ASCII 词"),
    ("A", "AI 定价阶梯", ["定价与计费", "术语表-AI服务商业化"], "短词+长词（防 AI 噪声）"),
    ("A", "验收条款", ["合同与风险"], "合同组"),
    ("A", "Palantir", ["术语表-AI落地", "本体论"], "纯英文专名"),
    ("A", "单位经济", ["单位经济"], "汇编标题"),
    # --- B 自然语句 / 同义改写（靠 synonyms.yaml 补）---
    ("B", "客户为什么不续费了", ["单位经济", "流失"], "续费≈流失"),
    ("B", "怎么跟客户要钱，分几次收", ["定价与计费", "合同与风险"], "要钱≈计费/收款"),
    ("B", "合同里出问题谁来担责", ["合同与风险"], "担责≈责任/赔偿"),
    ("B", "怎么找到第一批客户", ["获客"], "找客户≈获客"),
    ("B", "怎么判断一个活儿该不该接", ["合同与风险", "单位经济"], "接活≈服务范围/单位经济"),
    ("B", "模型厂商降价对我们报价的影响", ["定价与计费", "单位经济"], "降价≈成本/定价"),
    ("B", "AI 干活的成果归谁", ["合同与风险"], "成果归谁≈IP 归属"),
    # --- C 关键词式（agent 常用）---
    ("C", "定价 计费 模型", ["定价与计费"], "三词同现"),
    ("C", "合同 责任 上限", ["合同与风险"], "两词+专名"),
    ("C", "获客 第一批客户", ["获客"], "2字词+4字词（防误杀）"),
    ("C", "客户 续费", ["单位经济", "流失"], "两词均 2 字（曾误杀）"),
    ("C", "成果 归属 IP", ["合同与风险"], "中英混"),
    ("C", "降价 报价", ["定价与计费", "交付与价值"], "宽期望"),
    # --- E code profile 场景（技术/英文/工具名：纯词面应保持高水位）---
    ("E", "harness 长任务", ["Harness与长任务"], "code 主场景"),
    ("E", "MCP 工具 注册", ["工具规模", "xpertai", "MCP"], "code 主场景"),
    ("E", "评测 噪声", ["评测"], "code 主场景"),
    ("E", "沙箱 隔离", ["沙箱隔离"], "code 主场景"),
    ("E", "opencode 使用", ["opencode"], "工具指南"),
    ("E", "测试驱动 方法论", ["TDD", "BDD", "测试驱动"], "方法论"),
    ("E", "多智能体 编排", ["多智能体"], "方法论"),
    # --- F content profile 场景（品牌/平台/内容运营：**按设计不在 KB**，
    #     期望的是"正确路由到别的层"，而不是 KB 命中 —— 给最近垃圾 = 失败）---
    ("F", "品牌人设 规范", "brand-assets", "应路由到品牌资产层"),
    ("F", "小红书规则 限流", "brand-assets", "平台规则不在 KB"),
    ("F", "封面图 prompt 库", "brand-assets", "品牌资产层"),
    ("F", "报价单 在哪", "01-Projects", "项目私有"),
    ("F", "这个客户是谁", "entities", "实体层"),
]

NEGATIVES = ["蛋白质折叠预测", "供应链金融 区块链", "量子纠缠 退相干", "大棚蔬菜病虫害防治"]

GATE = {"A": 1.00, "C": 0.50, "E": 0.80, "F": 0.80, "ALL": 0.45}


def load_cases():
    cases = list(CASES)
    if os.path.exists(EXTRA):
        try:
            import yaml
            d = yaml.safe_load(K.read_text(EXTRA)) or {}
            for c in (d.get("cases") or []):
                g = c.get("group", "B")
                if c.get("route"):
                    cases.append((g, c["query"], c["route"], c.get("note", "真实漏召回沉淀")))
                else:
                    cases.append((g, c["query"], c.get("expect") or [], c.get("note", "")))
        except Exception as e:
            print(f"⚠️  eval_cases.yaml 读取失败：{e}")
    return cases


def append_case(q, expect, route, group, note):
    import yaml
    d = {"cases": []}
    if os.path.exists(EXTRA):
        d = yaml.safe_load(K.read_text(EXTRA)) or {"cases": []}
        d.setdefault("cases", [])
    entry = {"query": q, "group": group, "note": note or "真实漏召回沉淀", "added": time.strftime("%Y-%m-%d")}
    if route:
        entry["route"] = route
    else:
        entry["expect"] = expect
    d["cases"].append(entry)
    with open(EXTRA, "w", encoding="utf-8") as f:
        yaml.safe_dump(d, f, allow_unicode=True, sort_keys=False)
    print(f"✅ 已固化用例：{q}（组 {group}）→ {EXTRA}")


def triage(n=40):
    if not os.path.exists(MISS_LOG):
        print("（还没有漏召回记录——kb_search 每次 0 命中会自动记一条）")
        return
    rows = []
    for line in K.read_text(MISS_LOG).splitlines()[-400:]:
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
    seen, uniq = set(), []
    for r in reversed(rows):
        q = r.get("q", "")
        if q and q not in seen:
            seen.add(q)
            uniq.append(r)
    print(f"未命中的真实查询（最近 {len(uniq)} 条，去重）：")
    for r in uniq[:n]:
        print(f"  · [{r.get('ts','')[:16]}] {r['q']}   层级={r.get('layers','')}")
    print("\n固化方法：python3 kb_eval.py --add \"<查询>\" --expect \"<路径特征>\" --group B")
    print('（若其实是「库外知识」，用 --route brand-assets / 01-Projects / entities）')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", action="store_true", help="打印失败项与命中路径")
    ap.add_argument("--triage", action="store_true", help="查看真实漏召回记录")
    ap.add_argument("--add", metavar="QUERY", help="把一条真实查询固化为用例")
    ap.add_argument("--expect", action="append", default=[], help="期望命中路径特征（可多次）")
    ap.add_argument("--route", help="期望路由目标（品牌/项目/实体层）")
    ap.add_argument("--group", default="B", help="用例分组 A/B/C/E/F")
    ap.add_argument("--note", default="", help="备注")
    a = ap.parse_args()
    if a.triage:
        triage(); return 0
    if a.add:
        append_case(a.add, a.expect, a.route, a.group, a.note); return 0

    items = K.load_index()
    a2c, rel = K.load_vocab()
    cases = load_cases()
    stat, rows = {}, []
    for grp, q, exp, note in cases:
        hits, meta = K.search(q, items, a2c, rel, limit=8)
        paths = [h[1]["p"] for h in hits]
        if isinstance(exp, str):     # 路由型用例
            hint = K.route_hint(q)
            ok5 = exp in (hint or "")
            r1 = r3 = r5 = ok5
        else:
            def hit(k):
                return any(any(e in p for e in exp) for p in paths[:k])
            r1, r3, r5 = hit(1), hit(3), hit(5)
        rows.append((grp, q, note, r1, r3, r5, paths))
        s = stat.setdefault(grp, [0, 0, 0, 0])
        s[0] += r1; s[1] += r3; s[2] += r5; s[3] += 1

    print(f"{'组':2s} {'查询':26s} {'r@1':4s} {'r@3':4s} {'r@5':4s} 备注")
    for grp, q, note, r1, r3, r5, paths in rows:
        m = lambda b: "✅" if b else "❌"
        print(f"{grp:2s} {q:26s} {m(r1):4s} {m(r3):4s} {m(r5):4s} {note}")
        if a.show and not r5:
            print(f"     命中：{paths[:3] if paths else '（无）'}")
    print()
    total = [0, 0, 0, 0]
    ok = True
    for grp in sorted(stat):
        r1, r3, r5, n = stat[grp]
        print(f"  {grp} 组：r@1 {r1}/{n}  r@3 {r3}/{n}  r@5 {r5}/{n}")
        for i in range(4):
            total[i] += stat[grp][i]
        if grp in GATE:
            rate = r5 / n
            good = rate >= GATE[grp]
            ok &= good
            print(f"       门槛 r@5 ≥ {GATE[grp]:.2f}：{rate:.2f} {'✅' if good else '❌'}")
    print(f"  合计：r@1 {total[0]}/{total[3]}  r@3 {total[1]}/{total[3]}  r@5 {total[2]}/{total[3]}")
    print()
    neg_bad = []
    for q in NEGATIVES:
        hits, _ = K.search(q, items, a2c, rel, limit=3)
        if hits:
            neg_bad.append(q)
        print(f"  {'✅' if not hits else '❌'} 负样本：「{q}」→ {len(hits)} 命中（应为 0）")
    ok &= not neg_bad
    allrate = total[2] / total[3]
    good = allrate >= GATE["ALL"]
    ok &= good
    print(f"  门槛 ALL r@5 ≥ {GATE['ALL']:.2f}：{allrate:.2f} {'✅' if good else '❌'}")
    print("✅ 评估通过" if ok else "❌ 评估未达标（检索质量回退）")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
