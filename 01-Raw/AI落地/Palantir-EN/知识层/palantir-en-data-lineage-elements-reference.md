---
title: Palantir 官方文档（英文原版）· Graph elements reference
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/elements-reference/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/elements-reference/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-elements-reference.md`

# Graph elements reference

## Node types

| Node                                        | Type | Description |
| --- | --- | --- |
![Data Source](/docs/resources/foundry/data-lineage/data-lineage-node-data-source.png) | **Data source** | This is the name of the data source as it appears in [Data Connection](/docs/foundry/data-connection/overview/). [Learn more about the different source types.](/docs/foundry/data-integration/source-type-overview/)
![Dataset node](/docs/resources/foundry/data-lineage/data-lineage-node-dataset.png) | **Dataset**  |  Foundry datasets and the lineage between them. The color of the dataset node depends on [user selection](/docs/foundry/data-lineage/node-coloring/). Dashed border indicates unstructured datasets.
![Object type node](/docs/resources/foundry/data-lineage/data-lineage-node-object-type.png) | **Object type**  | Ontology [object types](/docs/foundry/object-link-types/object-types-overview/). The icon and color of the node depend on the definition of each object type. When clicking on the “link” icon next to the object type name, Data Lineage shows the relations between this object type and other object types.
![Artifact node](/docs/resources/foundry/data-lineage/data-lineage-node-artifact.png) | **Artifact** | Data Lineage exposes different Foundry artifacts like: [Contour](/docs/foundry/contour/overview/) analyses, [Reports](/docs/foundry/reports/overview/), etc. The color of the node depends on the artifact type, which is indicated at the top of the node.

## Node indicators

Node indicators appear on top of dataset nodes and provide additional information about the resource.

| Indicator | Type | Description |
| --- | --- | --- |
![Issues icon](/docs/resources/foundry/data-lineage/data-lineage-icon-issues-reported.png)  | **Open issues** | This indicator signals there are currently open issues associated with the node on the graph. Hovering over this signal indicates the number of open issues.
![Linked object icon](/docs/resources/foundry/data-lineage/data-lineage-icon-linked-objects.png) | **Defines an object type** | This indicator appears on datasets that are used to define Ontology object types. Hovering over the right arrow allows you to expose those linked object types. [Learn more about object types.](/docs/foundry/object-link-types/object-types-overview/)
![Syncs icon](/docs/resources/foundry/data-lineage/data-lineage-icon-syncs.png) | **Syncs** | Datasets with this indicator on them have syncs to other databases or systems. You can view these syncs by selecting the node and opening the Properties panel, or by opening the “Details” tab in Dataset Preview (right click on the node and click on **Open**).
![Trashed icon](/docs/resources/foundry/data-lineage/data-lineage-icon-trashed.png) | **Trashed** | This indicator appears on nodes representing deleted datasets or artifacts. Deleted nodes are also partially faded with their name crossed out.
