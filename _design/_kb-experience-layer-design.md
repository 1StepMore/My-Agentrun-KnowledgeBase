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

# KB 第二系统设计提案：经验资产层 + 溯源补强

> 状态：设计提案（未实施）
> 日期：2026-09-06
> 决策人：renanzai（拍板项见文末清单）

---

## 0. 背景与问题（本次暴露的两个真实缺陷）

**缺陷 A — 溯源缺失导致误判**
- 现状：01-Raw 700 md / 02-Draft 37 md / 03-Wiki 161 md
- 误判：看到 Raw 远多于 Draft，会以为「大量内容丢失未消化」
- 真相：多篇 Raw 合成 1 篇 Draft（如 Loop-Engineering 主题至少 4 篇 Raw 素材），但 **frontmatter 无任何字段记录血缘** → 无法区分「丢失」与「已合成」

**缺陷 B — 中期经验无处安放**
- memory（每 profile，2200 字符）：只装高频事实碎片
- skills：只装可复用流程，不装案例/决策
- session_search：全文检索对话，费力
- context-sync.log：一行式事件，7 天滚动，无细节
- **空白带：结构化「案例/决策/复盘」档案**——调研结论、方案取舍、翻车复盘，做完就散，下次从零开始

**目标定位一句话**：
> KB 复用现有检索基建（_keywords/frontmatter/三层检索），新增第二个用途——**经验资产层**：存放低频高价值的内部实践档案（决策/案例/复盘），跨 session、跨 profile 可检索复用。素材管线（Raw/Draft/Wiki）与外挂经验层**分离设计，互不污染**。

---

## 1. 决策点 1：溯源字段规范（补缺陷 A）

### 1.1 在现有 frontmatter 加字段（不新建系统）

Draft 层：
```yaml
state:
  phase: draft
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
  sources:                    # 新增：本篇由哪些 Raw/前置文件合成（相对路径）
    - 01-Raw/Bilibili/Loop-Engineering实操指南.md
    - 01-Raw/Bilibili/循环工程-Loop-Engineering.md
```

Wiki 层：
```yaml
state:
  phase: wiki
  sources:                    # 新增：本篇由哪个 Draft 晋升而来（相对路径）
    - 02-Draft/Loop-Engineering.md
```

Raw 层：**不改**（素材保留即可，不维护「被谁消费」反向指针，避免双向维护成本）。

### 1.2 血缘追溯逻辑（单向向上，够用）
```
Wiki → sources → Draft → sources → Raw
「这篇 Wiki 的原始素材是什么」→ 两步反查
「某主题全部素材」→ 从 Raw 侧按 _keywords 匹配，再对 Draft 的 sources 校验
```

### 1.3 历史欠账怎么补？（37 个 draft + 161 个 wiki）
- 人工逐篇补：工作量 ~200 篇，不值得
- **Dahl M2.7 批处理补**（正好用上免费 token 的「低智能任务」定位）：
  - 输入：Draft 全文 + 01-Raw 文件清单
  - 任务：判断该 Draft 由哪些 Raw 合成（按主题相似度）
  - 输出：候选 sources → 人工确认后写入 frontmatter
- 精度要求不高（溯源是辅助索引，错 1-2 条无伤大雅），M2.7 足够

---

## 2. 决策点 2：经验资产层目录位置

### 候选方案对比

| 方案 | 位置 | 优点 | 缺点 |
|---|---|---|---|
| **A. KB 内新顶层** | `Hermes-KnowledgeBase/04-Experience/` | 复用 _keywords/检索；与素材同库 | 概念上混「外部知识」与「内部经验」（可接受） |
| **B. Hermes 全局** | `~/.hermes/shared/` | 天然跨 profile | 无检索基建；.hermes 是配置目录非知识库 |
| **C. Workspace** | `Hermes-Workspace/` | 与 handoff/ 协作基建相邻 | 偏「工作产物」非「知识资产」；无检索 |

### 我的推荐：A（KB 内 04-Experience/），理由
1. 检索基建现成（_keywords.yaml 加词即可纳入检索）
2. 你已明确「知识库闲置很久」——给现有基建找第二用途正是本意
3. 隔离规则清晰：**01/02/03 走三层提炼管线；04 直接写入、不设 Raw/Draft 中间层、不参与提炼**

### 04-Experience/ 内部结构（建议，可改）
```
04-Experience/
├── decision/    # 决策档案（如 amd-vs-dahl-fallback.md）
├── case/        # 案例复盘（选题成败/事故复盘）
├── practice/    # 实践总结（非流程类经验，如「M2.7 适用边界」）
└── _index.md    # 可选：手动索引（或用 _keywords 检索替代）
```

每篇档案 frontmatter 示例：
```yaml
---
title: AMD vs Dahl 免费通道选型
kind: decision
date: 2026-09-05
keywords: [llm-providers, fallback, dahl, amd]
profiles: [default, content, code]   # 相关 profile 标记（供消费机制用）
summary: 一页内看懂结论的摘要（3-5 行）
---
```

**档案正文规范**（轻量，5 段式）：
`背景 → 候选方案 → 实测数据 → 结论与理由 → 后续注意`

---

## 3. 决策点 3：Profile 消费机制（怎么让三 profile 知道并去读）

**核心问题**：文件放在 D 盘共享位置 ≠ content/code agent 会自动读。Hermes 各 profile memory 物理隔离，需显式机制。

### 机制组合（推荐三层）

**L1 — 指针入 memory**：三 profile 的 MEMORY.md 各加一行（约 40 字符）：
```
跨profile经验资产: /mnt/d/Hermes-KnowledgeBase/04-Experience/ (决策/案例/复盘, 新调研/方案前先查)
```
成本极低，保证每个 profile 每 session 都「知道这地方存在」。

**L2 — 消费触发 skill**：default 建 `experience-archive` skill（写 + 查规范）：
- **写入侧**：完成任务（调研/选型/复盘）时，若结论有复用价值 → 按 5 段式写 04-Experience
- **查询侧**：新任务开工前，若涉及既往主题 → 先检索 04-Experience 避免重复踩坑
- code/content profile 各自装一份轻量「查询版」（或 symlink 同一源文件）

**L3 — 主动推送（跨 profile 通知）**：
- default 写完一篇经验档案 → 走现有 handoff/ 或 bot-chat 通知相关 profile（frontmatter 的 `profiles` 字段决定通知谁）
- 可选升级：cron 周报汇总 04-Experience 新增（复用 self-packaging 思路）

### 明确不做的（防过度设计）
- ❌ 不做跨 profile 共享 memory（Hermes 不支持且没必要，指针够用）
- ❌ 不做自动消化（档案是给人/AI 按需读的，不是喂给谁的）
- ❌ 不要求所有档案三 profile 都读（按 `profiles` 字段定向）

---

## 4. 落地顺序建议

| 步骤 | 内容 | 耗时 |
|---|---|---|
| 1 | 建 04-Experience/ 目录 + decision/ 首篇样例（拿 AMD vs Dahl 开刀） | 15 分钟 |
| 2 | 溯源字段规范写入 kb-organization skill + _keywords 加 `experience` 类词 | 15 分钟 |
| 3 | 三 profile MEMORY.md 加 L1 指针（需授权跨 profile 改） | 5 分钟 |
| 4 | Dahl M2.7 批处理补 draft 的 sources（试点 3-5 篇看质量） | 后台跑 |
| 5 | 跑两周后评估：是否建 L2 skill / 是否加 L3 周报 | 观察 |

---

## 5. 待你拍板清单

| # | 决策项 | 选项 |
|---|---|---|
| 1 | 溯源字段方案 | A 接受（frontmatter 加 sources，Raw 不改）/ B 要改 / C 不做 |
| 2 | 经验层位置 | A 04-Experience/（推荐）/ B ~/.hermes/shared/ / C Workspace / D 其他 |
| 3 | 04-Experience 内部分类 | A decision/case/practice（推荐）/ B 按 profile 分 / C 不分直接平铺 |
| 4 | 消费机制 | A 三层全上 / B 只做 L1 指针 / C 只做 L1+L2 skill / D 先只做 default 试点 |
| 5 | 历史溯源补欠账 | A 用 Dahl M2.7 补（推荐）/ B 人工关键篇补 / C 暂不补 |
| 6 | 首篇样例 | A AMD vs Dahl 选型（推荐）/ B 其他 |
