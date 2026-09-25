#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kb_search.py —— 知识库检索器（所有 profile 共用的「外挂知识储备」入口）

目标：**高效 + 鲁棒 + 可自证**。
- 高效：预建索引（_index/kb_index.json）；**新鲜度检查 O(1)**（脏标记 + 30 分钟时间窗），
       索引内的词表缓存免去每次解析 YAML；重建才走全量（约 10-15s，写入侧已自动打脏标记）。
- 鲁棒：纯 Python 遍历（中文路径/NUL 安全）；frontmatter 坏掉不崩；`.git`/`_backup`/`参考存档`/`_index` 默认排除。
- 自证：`--selftest` 造正/负样本 + 索引新鲜度断言，退出码 0 才算可用。

检索管线（与《KB 检索行为》一致）：
  Pass1 关键词匹配（_keywords.yaml 的 aliases → 规范名）
  Pass2 语义扩展（related，方向：具体→抽象）
  Pass3 分层搜索（Wiki → Draft → Raw，同名去重保留最高层）
  兜底  全文 AND 匹配（全部查询词都出现才命中）

用法：
  python3 kb_search.py "定价策略"                  # 默认 Wiki + Draft
  python3 kb_search.py "Palantir" --raw            # 含素材层
  python3 kb_search.py "outcome" --all --limit 15  # 含存档层
  python3 kb_search.py "本体" --json               # 机器可读
  python3 kb_search.py --rebuild | --check | --stats | --selftest | --mark-dirty
"""
from __future__ import annotations
import argparse, json, os, re, sys, time, io, unicodedata
from concurrent.futures import ThreadPoolExecutor

KB = os.environ.get("KB_ROOT", "/mnt/d/Hermes-KnowledgeBase")
INDEX_DIR = os.path.join(KB, "_index")
INDEX_PATH = os.path.join(INDEX_DIR, "kb_index.json")
DIRTY = os.path.join(INDEX_DIR, ".dirty")
MISS_LOG = os.path.join(INDEX_DIR, "miss_log.jsonl")
KEYWORDS = os.path.join(KB, "_keywords.yaml")
SYNONYMS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synonyms.yaml")
LAYERS = [("03-Wiki", "wiki"), ("02-Draft", "draft"), ("01-Raw", "raw")]
SKIP_DIRS = {".git", "_backup", "_index", "参考存档", ".obsidian", "__pycache__", ".archive"}
MAX_AGE_S = 1800
BODY_CAP = 5000

# ---------- 基础 ----------
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").lower()
    return re.sub(r"""[\s\-_·・（）()\[\]【】:：/、,，.。;；"'“”‘’]+""", "", s)

def read_text(p: str) -> str:
    try:
        return open(p, encoding="utf-8", errors="ignore").read()
    except Exception:
        return ""

def split_frontmatter(txt: str):
    if not txt.startswith("---"):
        return {}, txt
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", txt, re.S)
    if not m:
        return {}, txt
    raw, body = m.group(1), txt[m.end():]
    try:
        import yaml
        fm = yaml.safe_load(raw) or {}
        return (fm if isinstance(fm, dict) else {}), body
    except Exception:
        fm = {}
        for k in ("title", "source", "evidence"):
            mm = re.search(rf"^{k}:\s*(.+)$", raw, re.M)
            if mm:
                fm[k] = mm.group(1).strip().strip('"\'')
        return fm, body

def load_vocab_yaml():
    alias2canon, related = {}, {}
    try:
        import yaml
        d = yaml.safe_load(read_text(KEYWORDS)) or {}
    except Exception:
        return alias2canon, related
    for canon, meta in (d or {}).items():
        if not isinstance(meta, dict):
            continue
        alias2canon[norm(canon)] = canon
        for a in (meta.get("aliases") or []):
            alias2canon[norm(str(a))] = canon
        if meta.get("related"):
            related[canon] = [str(x) for x in meta["related"]]
    return alias2canon, related

def load_synonyms():
    """查询侧语义映射（手写、可评审、免依赖）。返回 {norm(键): [值...]}
    优先读索引内缓存（免 YAML 解析）；索引缺失时回退文件。"""
    try:
        m = json.load(open(INDEX_PATH, encoding="utf-8"))["meta"]
        if m.get("synonyms"):
            return {k: list(v) for k, v in m["synonyms"].items()}
    except Exception:
        pass
    try:
        import yaml
        d = yaml.safe_load(read_text(SYNONYMS)) or {}
        out = {}
        for k, v in (d.get("maps") or {}).items():
            out[norm(str(k))] = [str(x) for x in (v or [])]
        return out
    except Exception:
        return {}


def load_vocab():
    """优先读索引内缓存（免 YAML 解析），回退到 _keywords.yaml。"""
    try:
        m = json.load(open(INDEX_PATH, encoding="utf-8"))["meta"]
        if m.get("alias2canon") is not None:
            return m.get("alias2canon", {}), {k: list(v) for k, v in (m.get("related") or {}).items()}
    except Exception:
        pass
    return load_vocab_yaml()

# ---------- 索引 ----------
def iter_md(include_archive=False):
    for root_layer, layer in LAYERS:
        base = os.path.join(KB, root_layer)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            if not include_archive and "参考存档" in dirpath:
                continue
            for fn in filenames:
                if fn.endswith((".md", ".markdown")):
                    yield os.path.join(dirpath, fn), layer

def _entry(path, layer):
    txt = read_text(path)
    fm, body = split_frontmatter(txt)
    title = str(fm.get("title") or "").strip()
    if not title:
        m = re.search(r"^#\s+(.+)$", body, re.M)
        title = m.group(1).strip() if m else os.path.basename(path)[:-3]
    kws = fm.get("keywords") or []
    if isinstance(kws, str):
        kws = [k.strip() for k in kws.split(",")]
    flat = re.sub(r"\s+", " ", body)
    snip = flat[:600]
    bd = flat[:BODY_CAP] if layer in ("wiki", "draft") else ""
    heads = [h.strip() for h in re.findall(r"^#{2,4}\s+(.+)$", body, re.M)][:40]
    kws = [str(k) for k in kws]
    return {
        "p": os.path.relpath(path, KB), "layer": layer, "title": title,
        "kw": kws, "ev": str(fm.get("evidence") or ""), "heads": heads,
        "snip": snip, "body": bd,
        # 预归一化字段（查询时不再做正则，实测把查询从 ~1.9s 降到 <0.4s）
        "nt": norm(title), "nk": [norm(k) for k in kws],
        "nh": norm(" ".join(heads)), "ns": norm(snip), "nb": norm(bd),
        "mt": int(os.path.getmtime(path)), "sz": os.path.getsize(path),
    }

def build_index(include_archive=False, verbose=True, workers=8):
    t0 = time.time()
    pairs = list(iter_md(include_archive))
    entries, errors = [], []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(lambda pl: _safe_entry(*pl), pairs):
            if isinstance(res, Exception):
                errors.append(str(res)[:120])
            else:
                entries.append(res)
    a2c, rel = load_vocab_yaml()
    try:
        syn = load_synonyms()
    except Exception:
        syn = {}
    os.makedirs(INDEX_DIR, exist_ok=True)
    meta = {"built": int(time.time()), "kb": KB, "entries": len(entries),
            "archive_included": bool(include_archive), "errors": len(errors),
            "alias2canon": a2c, "related": rel, "synonyms": syn}
    tmp = INDEX_PATH + ".tmp"
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "items": entries}, f, ensure_ascii=False)
    os.replace(tmp, INDEX_PATH)
    try:
        if os.path.exists(DIRTY):
            os.remove(DIRTY)
    except OSError:
        pass
    if verbose:
        print(f"✅ 索引已建：{len(entries)} 条 → {INDEX_PATH}（{time.time()-t0:.1f}s，错误 {len(errors)}）")
        for e in errors[:5]:
            print(f"   ⚠️  {e}")
    return meta

def _safe_entry(path, layer):
    try:
        return _entry(path, layer)
    except Exception as e:
        return e

def log_miss(q, layers):
    """漏召回沉淀：每次 0 命中记一条（供 kb_eval --triage 复盘、固化为例题）。
    只记查询本身，不记上下文；同查询去重、上限 500 条。"""
    try:
        os.makedirs(INDEX_DIR, exist_ok=True)
        rows = []
        if os.path.exists(MISS_LOG):
            for line in read_text(MISS_LOG).splitlines()[-500:]:
                try:
                    rows.append(json.loads(line))
                except Exception:
                    pass
        if any(r.get("q") == q for r in rows[-50:]):
            return
        rows.append({"ts": time.strftime("%Y-%m-%d %H:%M:%S"), "q": q, "layers": "/".join(layers)})
        with io.open(MISS_LOG, "w", encoding="utf-8") as f:
            for r in rows[-500:]:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    except Exception:
        pass


def mark_dirty():
    try:
        os.makedirs(INDEX_DIR, exist_ok=True)
        open(DIRTY, "w").write(str(int(time.time())))
    except OSError:
        pass

def index_fresh(include_archive=False, strict=False, max_age_s=MAX_AGE_S):
    """默认 O(1)：脏标记 + 时间窗。strict=True 才全遍历（--check / selftest 用）。"""
    if not os.path.exists(INDEX_PATH):
        return False
    try:
        meta = json.load(open(INDEX_PATH, encoding="utf-8"))["meta"]
    except Exception:
        return False
    if meta.get("archive_included") != bool(include_archive):
        return False
    if os.path.exists(DIRTY):
        return False
    if not strict:
        return (time.time() - meta.get("built", 0)) <= max_age_s
    built = meta.get("built", 0)
    for layer in ("03-Wiki", "02-Draft", "01-Raw"):
        base = os.path.join(KB, layer)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            if "参考存档" in dirpath:
                continue
            try:
                if os.path.getmtime(dirpath) > built + 1:
                    return False
            except OSError:
                pass
            for fn in filenames:
                if fn.endswith((".md", ".markdown")):
                    try:
                        if os.path.getmtime(os.path.join(dirpath, fn)) > built + 1:
                            return False
                    except OSError:
                        pass
    return True

def load_index(include_archive=False, auto_build=True, verbose=False, no_check=False):
    if no_check and os.path.exists(INDEX_PATH):
        return json.load(open(INDEX_PATH, encoding="utf-8"))["items"]
    if not index_fresh(include_archive):
        if not auto_build:
            raise SystemExit("❌ 索引缺失或过期，请先 --rebuild")
        build_index(include_archive, verbose=verbose)
    return json.load(open(INDEX_PATH, encoding="utf-8"))["items"]

# ---------- 检索 ----------
def tokens(q: str):
    parts = [p for p in re.split(r"[\s,，、;；]+", (q or "").strip()) if p]
    if q.strip() and norm(q) not in [norm(p) for p in parts]:
        parts.append(q.strip())
    return parts

def bigrams(qs: str):
    qn = norm(qs)
    if len(qn) < 3:
        return set()
    return {qn[i:i + 2] for i in range(len(qn) - 1)
            if re.match(r"[\u4e00-\u9fff]", qn[i]) and re.match(r"[\u4e00-\u9fff]", qn[i + 1])}

_ALIAS_CACHE = {}

def _aliases_sorted(alias2canon):
    key = id(alias2canon)
    if key not in _ALIAS_CACHE:
        _ALIAS_CACHE[key] = sorted(alias2canon.keys(), key=len, reverse=True)
    return _ALIAS_CACHE[key]


def search(q, items, alias2canon, related, limit=8, layers=("wiki", "draft"), raw_archive=False, synonyms=None):
    synonyms = synonyms if synonyms is not None else load_synonyms()
    toks = tokens(q)
    if not toks:
        return [], {"canon": [], "expanded": [], "fallback": False}
    canon = {alias2canon[norm(t)] for t in toks if norm(t) in alias2canon}
    # 别名子串扫描：查询是自然语句时（"合同里出问题谁来担责"），词表别名可能不是独立 token，
    # 而是**嵌在句子里** → 扫一遍。长别名优先（避免短别名噪声）；这是对"同义改写 0 命中"的廉价修法。
    qn_full = norm(q)
    for a_norm in _aliases_sorted(alias2canon):
        if len(a_norm) >= 2 and a_norm in qn_full:
            canon.add(alias2canon[a_norm])
    expanded = set()
    for c in canon:
        expanded.update(related.get(c, []))
    ntoks = [norm(t) for t in toks if norm(t)]
    # 抑制判据只看**分词后的部分**（不含拼起来的整串查询）：
    # 反例（已修）："客户 续费" 两个词各 2 字，拼起来 4 字，若按整串算 maxlen 会误杀两者 → 0 命中
    parts_n = [norm(x) for x in re.split(r"[\s,，、;；]+", (q or "").strip()) if norm(x)]
    maxpart = max((len(x) for x in parts_n), default=0)
    long_tokens = [t for t in ntoks if len(t) >= 3]
    canon_n = {norm(c) for c in canon}
    exp_n = {norm(e) for e in expanded}
    nq = norm(q)
    qbi = bigrams(q) if " " not in q.strip() else set()
    # 查询侧语义映射：查整个查询串里是否出现映射键（含"客户为什么不续费了"这类整句）
    syn_terms = set()
    for k_norm, vals in (synonyms or {}).items():
        if k_norm and k_norm in nq:
            syn_terms.update(vals)
    syn_n = {norm(t) for t in syn_terms}

    def layer_ok(l):
        return (l in layers) or (raw_archive and l == "raw")

    results = []
    for it in items:
        if not layer_ok(it["layer"]):
            continue
        score, why = 0, []
        direct_hit = False
        t_norm = it.get("nt") or norm(it["title"])
        snip = it.get("ns") or norm(it["snip"])
        full = it.get("nb") if "nb" in it else norm(it.get("body") or "")
        heads = it.get("nh") or norm(" ".join(it["heads"]))
        kws = it.get("nk") or [norm(k) for k in it["kw"]]
        if nq and len(nq) >= 3:
            if nq in t_norm:
                score += 90; why.append("标题含整串查询")
            elif nq in snip or (full and nq in full):
                score += 40; why.append("正文含整串查询")
        for nt in ntoks:
            if len(nt) < 2 and long_tokens:
                continue
            # 只抑制 ASCII 短噪声（"ai"/"e"/"p" 之类）；中文 2 字词（获客/客户/合同）是有效查询词，不能杀
            if len(nt) < 3 and re.match(r"^[a-z0-9]+$", nt) and any(len(x) >= 4 for x in parts_n):
                continue
            w = max(1, min(len(nt), 10))
            if nt in t_norm:
                score += w * 8; why.append("标题命中"); direct_hit = True
            if any(nt == k for k in kws):
                score += w * 7; why.append("关键词精确命中"); direct_hit = True
            elif any(nt in k for k in kws):
                score += w * 4; why.append("关键词命中")
            if nt in heads:
                score += w * 2; why.append("小标题命中"); direct_hit = True
            if nt in snip:
                score += w; why.append("正文命中"); direct_hit = True
            elif full and nt in full:
                score += w; why.append("全文命中"); direct_hit = True
        if qbi:
            tb = {b for b in qbi if (b in t_norm or b in heads or any(b in k for k in kws))}
            cov = len(tb) / max(1, len(qbi))
            if len(tb) >= 2 and cov >= 0.6:
                score += len(tb) * 10; why.append(f"分词命中×{len(tb)}({cov:.0%})")
        for c in canon_n:
            if any(c in k for k in kws):
                score += 18; why.append("规范词命中")
        for e in exp_n:
            if any(e in k for k in kws) or e in t_norm:
                score += 10; why.append("相关词命中")
        # 同义词（查询侧映射）：权重低于词面，命中关键词最有价值
        syn_hit = 0
        for sy in syn_n:
            if any(sy == k or sy in k for k in kws):
                syn_hit += 12; why.append("同义映射→关键词")
            elif sy in t_norm or sy in heads:
                syn_hit += 6; why.append("同义映射→标题/小标题")
            # 正文命中同义词：**必须在"该文档已直接命中查询词"的前提下**才计分。
            # 否则英文同义词（churn/retention）散落在无关文档正文里，会靠 wiki+10 被抬到首位
            # （实测："客户为什么不续费了" 曾被 XpertAI enhanced-features 抢占头条）。
            elif direct_hit and (sy in snip or (full and sy in full)):
                syn_hit += 6; why.append("同义映射→正文(已直命中)")
        score += syn_hit
        if score <= 0:
            continue
        score += {"wiki": 10, "draft": 5, "raw": 0}.get(it["layer"], 0)
        # 索引页（MOC/_INDEX）是"地图"不是"内容"：除非用户就是要导航，否则降权，
        # 避免它靠"什么词都沾一点"稳居第一（实测：报价单/客户不续费/验收条款 都被 MOC 顶到首位）
        base_name = os.path.basename(it["p"])
        if base_name.startswith(("_MOC", "_INDEX", "_index")):
            nav = ("地图", "索引", "总览", "有哪些", "目录", "moc", "index", "导航")
            if not any(norm(k) in nq for k in nav):
                score -= 12
        results.append((score, it, " · ".join(dict.fromkeys(why))))

    best = {}
    for s, it, why in sorted(results, key=lambda x: -x[0]):
        key = norm(os.path.basename(it["p"])[:40]) or it["p"]
        order = {"wiki": 3, "draft": 2, "raw": 1}
        if key not in best or order[it["layer"]] > order[best[key][1]["layer"]]:
            best[key] = (s, it, why)
    out = sorted(best.values(), key=lambda x: -x[0])[:limit]
    fb = False
    if not out:
        fb = True
        # 兜底：自然语句 → 取查询的中文 bigram，丢弃"到处都有"的高频词对（IDF），
        # 按命中稀有词对的个数排序。反例（已修）："客户为什么不续费了" 原兜底要求整串全出现 → 0 命中。
        cand = bigrams(q) or set()
        if cand:
            n_items = max(1, len(items))
            df = {}
            pool = [(it, (it.get("nt", "") + it.get("ns", "") + (it.get("nb") or ""))) for it in items if layer_ok(it["layer"])]
            for b in cand:
                df[b] = sum(1 for _, body in pool if b in body)
            rare = {b for b in cand if 0 < df.get(b, 0) <= max(3, int(n_items * 0.04))}
            if rare:
                scored = []
                for it, body in pool:
                    m = sum(1 for b in rare if b in body)
                    # 门槛：稀有 bigram ≥3 命中；或 覆盖查询 bigram ≥60% 且 ≥2
                    cov = m / max(1, len(cand))
                    if m >= 3 or (m >= 2 and cov >= 0.6):
                        scored.append((m, it))
                scored.sort(key=lambda x: (-x[0], x[1]["layer"] != "wiki"))
                for m, it in scored[:limit * 2]:
                    out.append((m, it, f"稀有大gram兜底×{m}"))
        if not out:
            parts = [t for t in ntoks if len(t) >= 3] or [nq]
            for it in items:
                if not layer_ok(it["layer"]):
                    continue
                body = (it.get("ns") or norm(it["snip"])) + (it.get("nb") or "")
                if body and all(p in body for p in parts):
                    out.append((2, it, "全文兜底（全部词命中）"))
        out = out[:limit]
    return out, {"canon": sorted(canon), "expanded": sorted(expanded - canon), "fallback": fb}

# 未命中路由表：**KB 只放通用可公开知识**；下列内容按设计在别的层 → 说清去哪找，别让调用方乱猜
ROUTES = [
    # 顺序 = 优先级：越具体的意图放越前（"客户是谁"要进实体层，不能落到项目私有）
    (["是谁", "这个人", "某人", "负责人", "简介", "同一个人", "履历"], "实体层 → /mnt/d/Hermes-Workspace/00-Records/entities/（人/公司/项目卡）"),
    (["品牌", "人设", "persona", "定位", "slogan", "封面", "视觉", "账号"], "品牌资产层 → /mnt/d/Hermes-Workspace/00-Records/brand-assets/（brand / accounts）"),
    (["平台规则", "小红书规则", "公众号规则", "抖音规则", "限流", "封号", "违规"], "品牌资产层 → 00-Records/brand-assets/platforms/（平台规则不进 KB）"),
    (["合作方", "报价单", "项目现状", "合同原件", "交付件", "客户档案"], "项目私有 → /mnt/d/Hermes-Workspace/01-Projects/<项目>/（私有信息不进 KB）"),
    (["本机", "我的配置", "cron", "端口", "进程", "环境变量"], "本机状态 → 用 terminal 直接查，不属于知识库"),
    (["AI味", "AI 味", "去AI", "去 AI", "人味", "翻译腔", "Chinglish", "读起来像机器"], "content profile 技能 → humanize / slop-scan / english-quality-gate（内容质检工具，不在 KB）"),
    (["账号", "密码", "token", "key", "凭据", "密钥"], "凭据 → 各 profile 的 .env / keystore，**永不进 KB**"),
]


def route_hint(q):
    nq = norm(q)
    for keys, where in ROUTES:
        if any(norm(k) in nq for k in keys):
            return where
    return ""


def render(q, hits, meta, as_json=False):
    if as_json:
        print(json.dumps({"query": q, "meta": meta,
                          "hits": [{"score": s, "layer": it["layer"], "path": it["p"],
                                    "title": it["title"], "keywords": it["kw"],
                                    "evidence": it["ev"], "why": why} for s, it, why in hits]},
                         ensure_ascii=False, indent=1))
        return
    print(f"🔍 查询：{q}")
    if meta["canon"]:
        line = f"   规范词：{', '.join(meta['canon'])}"
        if meta["expanded"]:
            line += f" ｜ 语义扩展：{', '.join(meta['expanded'])}"
        print(line)
    if meta["fallback"]:
        print("   （关键词 0 命中 → 走全文兜底）")
    if not hits:
        print("   ❌ 无结果。可试：换同义词 / --raw / --all / 或该知识尚未入库")
        return
    hint = route_hint(q)
    if hint:
        print(f"\n   ⚠️  这个问题可能**不在 KB 范围内**（KB 只放通用可公开知识）")
        print(f"   🧭 应该去：{hint}")
    for i, (s, it, why) in enumerate(hits, 1):
        print(f"\n{i}. [{it['layer']}] {it['title']}   (score {s})")
        print(f"   📍 {it['p']}")
        if it["kw"]:
            print(f"   🏷️  {' · '.join(it['kw'][:8])}")
        if it["ev"]:
            print(f"   🧾 证据：{it['ev']}")
        print(f"   ✅ {why}")
        print(f"   📋 {it['snip'][:160]}…")

# ---------- 自检 ----------
def selftest():
    ok = True
    items = load_index(auto_build=not index_fresh())
    a2c, rel = load_vocab()
    print(f"索引：{len(items)} 条")
    pos = [("定价策略", "定价与计费"), ("AI 定价阶梯", "商业化"), ("Palantir", "Palantir"),
           ("本体", "本体"), ("合同", "合同"), ("术语表", "术语表"), ("合同验收", "合同")]
    for q, expect in pos:
        hits, _ = search(q, items, a2c, rel, limit=5)
        good = bool(hits) and any(expect.lower() in (h[1]["title"] + h[1]["p"]).lower() for h in hits)
        print(f"  {'✅' if good else '❌'} 正向：「{q}」→ {len(hits)} 命中" + (f"（首位：{hits[0][1]['title'][:38]}）" if hits else ""))
        ok &= good
    # 负样本用**现实的不存在主题**（库里确实没有的知识领域）。
    # 注：不用"乱码里夹真词"的对抗样本——那种样本的词对本身是真词，命中不算 precision 缺陷。
    for neg in ("蛋白质折叠预测", "供应链金融 区块链", "量子纠缠 退相干"):
        hits, _ = search(neg, items, a2c, rel, limit=3)
        print(f"  {'✅' if len(hits)==0 else '❌'} 负向：「{neg}」→ {len(hits)} 命中（应为 0）")
        ok &= (len(hits) == 0)
    fresh = index_fresh(strict=True)
    print(f"  {'✅' if fresh else '❌'} 索引新鲜度（严格全遍历）：{'最新' if fresh else '已过期'}")
    ok &= fresh
    print(("✅ 自检通过" if ok else "❌ 自检失败"))
    return 0 if ok else 1

def main():
    ap = argparse.ArgumentParser(description="知识库检索器")
    ap.add_argument("query", nargs="*")
    ap.add_argument("--raw", action="store_true", help="含 01-Raw 素材层")
    ap.add_argument("--all", action="store_true", help="含 Raw + 参考存档")
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--brief", action="store_true", help="精简输出：只给 层级/标题/路径（已定位时省 token，实测 2173→541 tok）")
    ap.add_argument("--build-index", action="store_true")
    ap.add_argument("--rebuild", action="store_true", help="强制重建索引")
    ap.add_argument("--check", action="store_true", help="严格新鲜度检查（全遍历，慢）")
    ap.add_argument("--no-check", action="store_true", help="跳过新鲜度检查（最快）")
    ap.add_argument("--mark-dirty", action="store_true", help="标记索引需重建（写入侧用）")
    ap.add_argument("--stats", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.mark_dirty:
        mark_dirty(); print("✅ 已标记索引需重建"); return 0
    if a.build_index or a.rebuild:
        build_index(include_archive=a.all); return 0
    if a.selftest:
        return selftest()
    if a.stats:
        items = load_index(a.all, no_check=a.no_check)
        from collections import Counter
        meta = json.load(open(INDEX_PATH, encoding="utf-8"))["meta"]
        c = Counter(i["layer"] for i in items)
        print(f"KB={KB}\n索引 {len(items)} 条：" + " ｜ ".join(f"{k} {v}" for k, v in c.items()))
        print(f"构建时间：{time.strftime('%Y-%m-%d %H:%M', time.localtime(meta['built']))}"
              f" ｜ 体积 {os.path.getsize(INDEX_PATH)//1024} KB ｜ 脏标记 {'有' if os.path.exists(DIRTY) else '无'}")
        return 0
    q = " ".join(a.query).strip()
    if not q:
        ap.print_help(); return 1
    layers = ("wiki", "draft", "raw") if (a.raw or a.all) else ("wiki", "draft")
    if a.check:
        print(f"[严格检查] 索引{'最新' if index_fresh(a.all, strict=True) else '已过期（本次会重建）'}")
    items = load_index(a.all, no_check=a.no_check)
    a2c, rel = load_vocab()
    hits, meta = search(q, items, a2c, rel, limit=a.limit, layers=layers, raw_archive=(a.raw or a.all))
    if a.brief:
        for i, (sc, it, why) in enumerate(hits, 1):
            print(f"{i}. [{it['layer']}] {it['title']}  —  {it['p']}")
        if not hits:
            print(f"❌ 「{q}」无结果" + (f" ｜ 🧭 {route_hint(q)}" if route_hint(q) else ""))
        return 0
    if not hits:
        log_miss(q, layers)
    render(q, hits, meta, as_json=a.json)
    return 0

if __name__ == "__main__":
    sys.exit(main())
