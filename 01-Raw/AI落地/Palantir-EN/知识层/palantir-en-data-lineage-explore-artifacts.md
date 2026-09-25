---
title: Palantir 官方文档（英文原版）· Explore artifacts and ontology entities
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/explore-artifacts/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/explore-artifacts/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-explore-artifacts.md`

# Explore artifacts and ontology entities

You can find Foundry artifacts and ontology entities related to your datasets in Data Lineage. The Data Lineage interface allows you to navigate directly to these resources and see how they fit in your ontology.

## Find related artifacts

In your data lineage graph, select a dataset. Then, select **Related items** in the right sidebar to expand the **Related artifacts** panel. The **Related items** icon will show a badge with the number of artifacts related to the selected dataset. In the artifacts panel, you can see a list of related resources throughout Foundry, including Contour visualizations and Slate applications.

![Find related dataset artifacts](/docs/resources/foundry/data-lineage/related-artifacts.png)

Click on the node icon next to a resource to zoom in on the related dataset, or click the resource to open it in the corresponding application in a new tab. You can filter the list of related artifacts to include different item types and sort the list by oldest, newest, name, path, or last modified.

## Find ontology entities

Find object types defined by datasets in your lineage graph by selecting the dataset and opening the **View node properties** panel in the right sidebar.

![View node properties in Data Lineage](/docs/resources/foundry/data-lineage/view-node-properties.png)

In the **About** tab, you will see any object types that were created with the selected dataset. Click the **Settings** icon next to the object type to view its configuration in a new Ontology manager tab.

![View ontology entities in Data Lineage](/docs/resources/foundry/data-lineage/ontology-entity.png)

You can also add object types to your data lineage with the **Search Foundry** tool in the right sidebar. Use a basic or advanced search to find an object type and select it from the list to add it to your graph. You can then view link types related to the object type and use the graph to visualize connections between your datasets and the newly added object type.

![View object type and dataset connection](/docs/resources/foundry/data-lineage/object-type-dataset-flow.gif)

[Learn more about creating an Ontology.](/docs/foundry/ontology/overview/)
