---
title: Palantir 官方文档（英文原版）· Preview and logic
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/dataset-preview-logic/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/dataset-preview-logic/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-dataset-preview-logic.md`

# Preview and logic

The Data Lineage interface allows you to view previews of selected datasets or media sets, as well as examine the associated code to understand the logic behind the dataset or media set.

## Preview

To see a preview of a dataset or media set, select it in your data lineage graph, then choose the **Preview** tab in the bottom left of the interface.

### Media set

When the media set preview expands, you can view the contents of your media set. [Learn more about media sets.](/docs/foundry/data-integration/media-sets/)

Example of PDF preview:

![Media Set PDF Preview](/docs/resources/foundry/data-lineage/dl-pdf-preview.png)

Example of audio preview:

![Media Set Audio Preview](/docs/resources/foundry/data-lineage/dl-audio-preview.png)

### Dataset

When the dataset preview expands, you can scroll through the first 300 rows of the selected dataset. You can also search for specific columns using the **Search columns...** field to the right of the preview window. The preview of your dataset will look different depending on the type of data within your dataset.

![View dataset preview](/docs/resources/foundry/data-lineage/dataset-preview.png)

## Logic

Select the **Code** tab to view the code logic of the selected dataset or media set. From the **Code** view, you can make quick edits, search for items, or open the code in the repository or other application used to derive the data.

![View dataset code](/docs/resources/foundry/data-lineage/dataset-code.png)

:::callout{theme="neutral"}
Uploaded and writeback datasets do not have associated code to view in Data Lineage.
:::
