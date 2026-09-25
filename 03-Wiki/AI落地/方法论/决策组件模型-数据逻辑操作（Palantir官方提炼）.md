---
title: "决策组件模型：数据·逻辑·操作（Palantir 官方提炼）"
source: "Palantir 官方文档 Platform overview · Decision components（E1 英文原文）"
evidence: E1
domain: AI落地
keywords: [Palantir, Foundry, AIP, semantic-layer, ontology-construction]
state:
  phase: wiki
  time_raw: "2026-09-23T00:00:00Z"
  time_draft: "2026-09-23T00:00:00Z"
  time_wiki: "2026-09-23T09:00:00+08:00"
related:
  - "[[_MOC-AI落地]]"
  - "[[术语表-AI落地]]"
  - "[[本体建模方法论（Palantir官方提炼）]]"
---

# 决策组件模型：数据 · 逻辑 · 操作（Palantir 官方提炼）

> **L3 方法条目**。来源 **E1 官方英文原文** `platform-overview`（含 `Decision components` 一节）。组织与中文表述为**我们的提炼**；引用原句请用英文原文层（`01-Raw/AI落地/Palantir-EN/`）。

## 一句话（官方原句，适合直接对客）

> **"The Ontology is designed to represent the *decisions* in an enterprise, not simply the data."**
> 本体是为了表达企业里的**决策**，而不只是数据。
> 而**"每一个决策都可以拆成：数据（data）、逻辑（logic）、操作（actions）"**。

## 二、三件套各自的官方定义（这是对客讲清价值的最短路径）

| 组件 | 官方的提问式定义 | 落地含义 |
|:---|:---|:---|
| **Data（数据）** | "What are the **relevant facts or truth** about the world and our operations that form the **context** for this decision?" | 决策所需的**事实与真值**——即"上下文" |
| **Logic（逻辑）** | "What organizational or business **rules act as guardrails**? What are the **probabilities** of certain outcomes under different assumptions? **What have we done in previous, similar situations** and what have the outcomes been? What are the inputs from our **forecasting and optimization models**?" | 业务规则的护栏 + 假设下的概率 + **历史相似情形的结果** + 预测/优化模型的输入 |
| **Actions（操作）** | "What are the '**kinetics**' or **effects** of this decision — how does the decision **manifest in the world**? **How do we reduce or collapse the steps between taking a decision and affecting an outcome in a production setting?**" | 决策在**现实中产生的效果**；关键是**压缩"做决策"到"生产环境产生结果"之间的步骤** |

> 🔑 **最后那句是整套价值主张的核心**：AI 落地的收益不在"多一个模型"，而在**把决策到结果的链路压短**——这正好对应官方另一篇的"决策捕获"（决策变成数据 → 反馈闭环）。

## 三、官方给的平台能力全景（八块，可当交付范围清单）

`Data connectivity & integration` · `Model connectivity & development` · **`Ontology building`** · `Use case development` · `Analytics` · `Product delivery` · `Security & governance` · `Management & enablement`

> 官方强调：**"关键的差异化因素是围绕 Ontology 的软件架构"**，而不是某一块能力本身。并且本体提供与既有企业系统的**深度双向互操作性（deep, two-way interoperability）**。

## 四、为什么要这样切（官方逻辑链）

1. 任何组织都在解决同一个问题：**如何在内外条件持续变化中，尽可能实时地做出最好的决策**。
2. 这类决策过程的复杂度，**反映在本体上**——本体自动把**相关的数据、逻辑与操作组件**整合进一个**AI 可访问的现代计算环境**。
3. 于是可以**快速开发运营型应用**，并让 AI 与操作者"**组队**"（AI teaming patterns）——把操作人员、分析师、领域专家的能力放大。

## 五、用法（E3）——这套框架最适合做**需求访谈与方案骨架**

- **对客访谈**：不要一上来问"你想用 AI 做什么"，而是逐项问——
  - 数据：**做这个决策，你需要哪些事实？现在从哪来、准不准、多快？**
  - 逻辑：**你们的规则护栏是什么？历史上类似情况怎么处理、结果如何？有没有预测/优化模型？**
  - 操作：**决策做完，现实里要发生什么？现在从决策到生效要几步、多久？**
- **方案设计**：把访谈结果直接映射成八块平台能力，**逐块标注"现状 / 缺口 / 谁来做"**（这是可交付的骨架）。
- **价值论证**：把"决策到结果的链路压缩了多少"作为**收益度量**，而不是"上了几个模型"。

## 六、与本库实践的对应（E3）

| 官方组件 | 我们的对应物 |
|:---|:---|
| Data | 本库"原始材料无损保留"（Raw 层）→ 决策上下文可回溯 |
| Logic | 门禁/红线条例/验收判据（**规则作为护栏**）；历史失败样本 |
| Actions | "交付前可执行校验 + 落地到真实产物"（压缩决策到结果的步骤）|
| 决策捕获/反馈闭环 | 我们的"发现缺陷立刻变成检查项"（把一次决策变成长期资产）|

相关条目：[[本体建模方法论（Palantir官方提炼）]] · [[术语表-AI落地]] · [[AI落地行业地图（认知基座）]]

## 七、实操清单

- [ ] 面对一个需求，我**拆得出数据/逻辑/操作三件套**吗？
- [ ] "逻辑"这块我有没有漏掉**历史相似情形的结果**与**预测/优化模型**？
- [ ] 我能不能说出**"决策 → 结果"当前有几步、要多久**？（说不出 → 价值论证没有基线）
- [ ] 方案里能不能逐块对应八项平台能力？
- [ ] 我讲的是"上了 AI"，还是"**决策链路缩短了多少**"？

## 待补

- [ ] 官方的 `distilling functional requirements`（用例开发一节）→ 补成"需求蒸馏"方法条目
- [ ] 八项能力各自在**客户侧的真实交付物**清单
- [ ] 与行业地图（T1-T8）的**映射表**（哪些行业的三件套最清晰）
