> # ⛔ 本文档已作废（2026-09-19）
>
> **状态：ABANDONED — 不再执行。**
>
> **作废理由（用户拍板 2026-09-19）**：
> 1. 本文档与同日的另一份设计冲突（`_kb-expansion-plan.md` 提 04-Compendium+05-Experience；`_kb-experience-layer-design.md` 提 04-Experience）——**同一层级两个编号，无法并存**
> 2. 两份均长期停在"待拍板/未实施"，**从未进入执行**
> 3. 用户裁决：**不再推进新层**；**行业知识也不入知识库**
>
> **本文档保留仅供追溯。请勿依据其内容执行任何操作。**
>
> 现行状态以 `_kb-reform-design.md` §九「执行记录」为准。

---

# KnowledgeBase 补强总企划：04-Compendium + 05-Experience + 溯源补强

> 状态：企划草案（待拍板）
> 日期：2026-09-06
> 决策人：renanzai
> 关联文档：`_kb-reform-design.md`（关键词/管道整改）、`_kb-experience-layer-design.md`（经验层初版设计）

---

## 0. 一句话总览

在现有 KB 三层（Raw 原料 → Draft 半成品 → Wiki 成品）之上，**新增两个并列的第 4/5 层**，并补上**层间溯源记录**，让 KB 从「外部知识素材库」升级为「知识 + 经验双轴系统」。

```
01-Raw ──→ 02-Draft ──→ 03-Wiki ──→ 04-Compendium   （外部知识：原料→成品→合辑）
                                        │
05-Experience  ←────────────────────────┘（内部经验：决策/案例/复盘，独立写入）
```

---

## 1. 新层命名与定位

| 层 | 命名 | 定位 | 内容形态 | 晋升来源 |
|---|---|---|---|---|
| **04** | `04-Compendium` | 多篇同主题 Wiki 的**合辑精编**（canonical 权威版） | 合并后的长文/专题 | 03-Wiki 多篇同主题晋升 |
| **05** | `05-Experience` | 内部**经验资产**（跨 profile 共享） | decision/case/practice 档案 | 直接写入（不设 Raw/Draft 中间层） |

**命名理由**：
- `Compendium` = "concise but complete collection of a subject"，精确表达「同主题多篇的精编合辑」；与 Raw/Draft/Wiki 同气质（短英文名词）
- `Experience` = 经验档案，明确是「做过的事」不是「学到的知识」
- 04/05 是**并列**关系不是递进关系——Compendium 是外部知识加工链的延伸，Experience 是独立轴

---

## 2. 三层旧体系 + 两个新层 = 完整知识阶梯

```
【外部知识轴】              加工深度        例子
01-Raw   原料（未加工）     低             单篇 B 站视频字幕
02-Draft 半成品（清洗整合）  中             单主题多篇素材合成一篇
03-Wiki  成品（审核通过）    高             Loop-Engineering 单篇
04-Compendium 合辑（权威精编） 最高         Skill 编写完全指南（5篇wiki合成）

【内部经验轴】              来源            例子
05-Experience 经验档案       实践沉淀        AMD vs Dahl 选型决策
```

---

## 3. 04-Compendium 详细设计

### 3.1 晋升规则（什么时候 03 → 04）

**触发条件（满足其一即考虑晋升）**：

| # | 条件 | 例子 |
|---|---|---|
| 1 | 同主题 Wiki ≥ 3 篇，内容有重叠/互补 | Skill 主题 5 篇 |
| 2 | 用户明确要求「把这几篇合成一篇」 | — |
| 3 | 该主题成为工作高频引用对象 | Loop Engineering（content 产线天天用） |

**晋升流程（合成 → 校对 → 晋升）**：
1. **选材**：同一 `_keywords` 词下收集全部 03-Wiki 篇目
2. **合成**：合并去重、保留各自精华、统一结构 → 生成 Compendium 草稿
3. **校对**：用户过目，确认结构/取舍（这是人工 gate，不自动）
4. **落位**：写入 `04-Compendium/<主题>/`，原 Wiki 篇目保留（不删，靠 `derived_to` 指向合辑）
5. **标记**：原 Wiki 篇目 frontmatter 加 `state.derived_to: 04-Compendium/<主题>/xxx.md`

**Compendium 文件命名**：`04-Compendium/<主题>/<主题>-compendium.md`（或直接 `<主题>.md`，待定）

### 3.2 Compendium 内部结构
```
04-Compendium/
├── skill-writing/          # 主题目录（与 _keywords 词对应）
│   └── skill-writing-compendium.md
├── loop-engineering/
│   └── loop-engineering-compendium.md
└── semantic-layer/
    └── semantic-layer-compendium.md
```

### 3.3 首批候选合辑（前面盘点已识别）

| 主题群 | 涉及文件数 | 合并产物 |
|---|---|---|
| Skill 编写 | 5 篇（Wiki）+ Draft 若干 | Skill 编写完全指南 |
| Loop Engineering | 5 个文件（散在 Bilibili/ + 根目录） | Loop Engineering 专题 |
| 语义层 | 3 篇 | 语义层方法论合辑 |
| Harness | 3 篇 | Harness 工程合辑 |
| HTML 做视频 | 3 篇 | HTML 生成视频合辑 |

---

## 4. 05-Experience 详细设计

### 4.1 定位重申
存**内部经验**：决策（decision）、案例复盘（case）、实践总结（practice）。
与 04 的本质区别：04 是「学到的外部知识精编」，05 是「做出来的内部经验」。

### 4.2 内部结构
```
05-Experience/
├── decision/    # 决策档案：AMD vs Dahl、Dahl 退役、某选题放弃
├── case/        # 案例复盘：AutoMedia 某期翻车、某次调研失误
├── practice/    # 实践总结：M2.7 适用边界、Dahl 批处理技巧
└── _index.md    # 索引（可选）
```

### 4.3 写入触发
- **主动沉淀**：完成任务（调研/选型/复盘）后，若结论有复用价值 → default 写入
- **被动查询**：新任务开工前，若涉及既往主题 → 先检索 05-Experience
- **跨 profile**：content/code 的经验由各自 profile 写，或经 handoff 转 default 代写

### 4.4 档案模板（5 段式）
```yaml
---
title: AMD vs Dahl 免费通道选型
kind: decision
date: 2026-09-05
keywords: [llm-providers, fallback, dahl, amd]
profiles: [default, content, code]
---
# 背景 → 候选方案 → 实测数据 → 结论与理由 → 后续注意
```

---

## 5. 溯源补强设计（贯穿全链）

### 5.1 问题回顾
多篇 Raw 合成 Draft、多篇 Draft 合成 Wiki、多篇 Wiki 合成 Compendium——**每步都缺血缘记录**，导致「文件数落差」被误判为「内容丢失」。

### 5.2 字段规范
| 层 | 加字段 | 指向 |
|---|---|---|
| Draft | `state.sources` | 合成它的 Raw 们 |
| Wiki | `state.sources` | 合成它的 Draft 们 |
| Compendium | `state.sources` | 合成它的 Wiki 们 |
| Wiki（被合入 Compendium） | `state.derived_to` | 它晋升成的 Compendium |

```yaml
state:
  phase: wiki
  time_raw: '...'
  sources:            # 上溯：由谁合成
    - 02-Draft/Loop-Engineering.md
  derived_to:         # 下溯：晋升成谁（被 Compendium 吸收时）
    - 04-Compendium/loop-engineering/loop-engineering-compendium.md
```

### 5.3 血缘追溯逻辑
```
Compendium → sources → Wiki → sources → Draft → sources → Raw
「这篇合辑的原始素材」→ 三步反查全部
「某主题全部素材」→ Raw 侧按 _keywords 匹配 + Draft/Wiki/Compendium 的 sources 校验
```

### 5.4 历史欠账补法
- **04/05 是新的**，从第一篇文章起就带字段（无欠账）
- **02-Draft + 03-Wiki 现存 ~200 篇**：人工补不值 → **Dahl M2.7 批处理**（低智能、容错、断点续跑）
  - 试点 3-5 篇看质量 → 通过则全量

---

## 6. 与既有设施的关系

| 设施 | 关系 |
|---|---|
| `_keywords.yaml` | 新增 `compendium`、`experience` 状态词；04/05 文件 keywords 纳入受控表 |
| `kb-organization` skill | 更新：盘点范围加 04/05；审计规则加溯源字段检查 |
| `ingest-raw-to-draft` 等 | 不受影响（仍管 01→02） |
| context-sync | 04 晋升/05 写入时可选记一条事件 |
| 三 profile memory | 各加一行 L1 指针（指向 05-Experience + 04-Compendium 检索规则） |

---

## 7. 落地顺序

| 步骤 | 内容 | 依赖 |
|---|---|---|
| 1 | 建 `04-Compendium/` `05-Experience/` 目录骨架 + README | 无 |
| 2 | 溯源字段规范写入 kb-organization skill | 无 |
| 3 | 试做 1 篇 Compendium（Skill 主题 5 篇合成，人工校对） | 1 |
| 4 | 试写 1 篇 Experience（AMD vs Dahl 决策档案） | 1 |
| 5 | _keywords 加词 + 三 profile 加 L1 指针（需授权跨 profile） | 2 |
| 6 | Dahl M2.7 批量补 Draft/Wiki sources（试点→全量） | 2 |
| 7 | 观察 2 周 → 评估是否扩产 | 3-6 |

---

## 8. 待拍板清单

| # | 决策项 | 我的推荐 |
|---|---|---|
| 1 | 04 命名 `Compendium` | ✅ 或改 |
| 2 | 05 命名 `Experience` | ✅ 或改 |
| 3 | 首批 Compendium 试点选哪个主题 | Skill（最典型） |
| 4 | 原 Wiki 篇目被合入后**保留还是归档** | 保留（靠 derived_to 指向，不删） |
| 5 | 05 档案 5 段式模板 | ✅ 或改 |
| 6 | 历史溯源用 Dahl M2.7 补 | ✅ 或改 |
| 7 | 落地顺序按 7 步走 | ✅ 或改 |
