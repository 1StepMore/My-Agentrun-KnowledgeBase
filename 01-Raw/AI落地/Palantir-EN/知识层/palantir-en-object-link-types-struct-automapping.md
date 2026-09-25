---
title: Palantir 官方文档（英文原版）· Automapping struct properties
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/struct-automapping/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/struct-automapping/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-struct-automapping.md`

# Automapping struct properties

Automapping allows users to map all columns automatically rather than manually.

## Automap struct types in Ontology Manager

If the object has already been created, users can automap all columns by using the **Automap all** feature.

1. In Ontology Manager, enter the **Properties** tab and select the desired property.
2. Under the **Column mapping** tab, select the desired column.

<img src="./media/automap-struct-oma.png" alt="The 'Column mapping' tab and the 'Automap all' button." width="500" />

3. Select **Automap all**.

## Automap struct types in Pipeline Builder

If the object has not yet been created, automapping can be done on initial object creation with the object type creation wizard.

1. In your Pipeline Builder pipeline, open the relevant dataset and select the **All Actions** dropdown in the top right.

<img src="./media/automap-struct-pipelinebuilder.png" alt="The All actions dropdown in the dataset detail page." width="500" />

2. Select **Create object type** to create a new object.

<img src="./media/automap-struct-properties.png" alt="The Properties tab in the 'Create a new object' dialog." width="500" />

3. Under **Properties**, add the desired properties to be mapped.
4. Select **Next** and complete the remaining steps to create an automapped object type.
