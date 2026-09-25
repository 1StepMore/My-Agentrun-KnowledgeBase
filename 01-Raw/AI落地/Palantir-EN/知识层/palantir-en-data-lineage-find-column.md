---
title: Palantir 官方文档（英文原版）· Find datasets with a given column
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/find-column/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/find-column/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-find-column.md`

# Find datasets with a given column

You can easily search for specific dataset columns within your Data Lineage graph:

* First, ensure you added all datasets of interest in your pipeline to your lineage graph.

* Next, select all datasets of interest by using **Drag select mode** in the Tools toggle in the upper left hand corner of the app. You can also hold down `Ctrl / Command` to select multiple nodes at once, or use `Ctrl / Command + A` to select all nodes. <br><br>
  ![Select datasets with Select mode](/docs/resources/foundry/data-lineage/select-mode.png) <br><br>

* Then, select **View histogram of selection properties** from the Data Lineage sidebar. <br><br>
  ![View histogram of selection properties](/docs/resources/foundry/data-lineage/view-histogram.png) <br><br>

* Under the **Frequent Columns** section, you can see the most frequent columns by name in your selection.

* Click one of the columns to highlight the datasets in your selection that contain this column. <br><br>
  ![View frequent columns in histogram](/docs/resources/foundry/data-lineage/column-search-dataset.png) <br><br>
