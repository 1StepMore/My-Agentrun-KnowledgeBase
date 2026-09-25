---
title: Palantir 官方文档（英文原版）· Data Lineage
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/overview/
evidence: E1
lang: en
domain: AI落地
keywords:
- Palantir
- Foundry
- ontology-construction
- semantic-layer
state:
  phase: raw
  time_raw: '2026-09-23T06:47:11+08:00'
  time_draft: null
  time_wiki: null
related: null
compile: false
compile_note: 原文取证层：知识内容已由中文版汇编为 Draft（3 篇），本层用于引用英文原句，不重复编译
---

> 溯源：Palantir 官方英文原文（E1）。中文版为官方机翻（准确性未验证），本文件为**取证优先的原文**。抓取 2026-09-23T06:47:11+08:00。
> 原始地址：https://palantir.com/docs/foundry/data-lineage/overview/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-overview.md`

# Data Lineage

**Data Lineage** is an interactive tool that facilitates a holistic view of how data flows through the Foundry platform.

![Data Lineage flow animation](/docs/resources/foundry/data-lineage/data-lineage-flow.gif)

With Data Lineage, you can:

* Easily find and discover datasets
  * Search to find datasets using Project, table, and column names
  * Click through Foundry Projects to browse data
* Explore [pipelines](/docs/foundry/data-integration/data-pipeline/) through a powerful interface
  * Expand or hide ancestors and descendants of datasets
  * View attributes of a group of tables at once
  * Visualize your pipeline through coloring (e.g. color out-of-date tables)
  * Drill into details about your data such as its schema, when it was last built, and the code that generated the data itself
* Collaborate with teammates
  * Create pipeline snapshots to share with other users
