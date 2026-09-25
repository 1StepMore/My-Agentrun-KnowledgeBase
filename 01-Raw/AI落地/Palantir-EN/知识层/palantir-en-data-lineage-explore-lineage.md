---
title: Palantir 官方文档（英文原版）· Explore data lineage
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/explore-lineage/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/explore-lineage/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-explore-lineage.md`

# Explore data lineage

Data lineage helps you understand how your data came to be. There are various ways to explore data pipelines in the Data Lineage app. Consider one common path:

1. Using the **Search** helper, find your resource (for example, a dataset or an object type) and add it to the graph.

2. Click on the left arrow of the node to expose the direct parents of the resource.

![Expand parents](/docs/resources/foundry/data-lineage/data-lineage-see-parents.png)

3. To expand your graph, select the next resource on the graph and click the **Expand** button in the graph tools.

4. Click on the chevron button to define the number of levels to expose. Click the double-chevron to expand all the way to the raw data (or all the way to the final descendants).

:::callout{theme="neutral"}
Adding too many nodes simultaneously may affect the graph's performance and usability. Keep a manageable number of nodes by checking the node count in the **Expand** tool.
:::

![Expand All](/docs/resources/foundry/data-lineage/data-lineage-expand-all.png)

:::callout{theme="success"}
You can find the relation between two nodes on the graph by selecting the **Expand** button and adding all nodes in between the resources or all common ancestors/descendants.
:::

5. Get more information on one of the datasets by selecting the dataset and using the bottom panel to display a preview of the data.

6. Click on **Code** to view how the dataset was created.

![Dataset code preview](/docs/resources/foundry/data-lineage/data-lineage-dataset-code.png)

7. Click on **View in code workbook** or **View in repository** to see the original code and make changes as needed (subject to permissions).

:::callout{theme="neutral"}
Some options may be unavailable for some datasets depending on the type of resource. For example, **Code** is only available for Code Workbook or Code Repositories. For Fusion sheet syncs with no code to show, you may have the option to view the source sheet and make your changes there (if you have appropriate permissions).
:::
