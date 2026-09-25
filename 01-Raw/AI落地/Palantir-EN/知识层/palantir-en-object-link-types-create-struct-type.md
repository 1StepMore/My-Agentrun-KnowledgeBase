---
title: Palantir 官方文档（英文原版）· Create a struct property type
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/create-struct-type/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/create-struct-type/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-create-struct-type.md`

# Create a struct property type

Create and configure a new struct property from the **Object types** page in Ontology Manager. For more information about struct properties, see the [overview](/docs/foundry/object-link-types/structs-overview/).

1. In Ontology Manager, open the **Object types** tab in the left sidebar and select an existing object type.
2. In the object type details page, open the **Properties** tab in the left sidebar, and select the **Create property** button on the top right of the **Properties** table.

<img src="./media/create-struct-from-ontology-manager.png" alt="The object type Properties table and 'Property editor' panel."  width="500" />

3. In the **Property editor** panel, add a name and description, and select **Struct** from the **Base type** dropdown menu.

<img src="./media/name-struct-from-ontology-manager.png" alt="The Base type dropdown with 'Struct' selected." width="500" />

4. Scroll down to the **Data** section and select a **Backing column** from the dropdown.

<img src="./media/backing-column-struct-ontology-manager.png" alt="Choose a backing column in the Data section of the Property editor." width="500" />

5. In the **Struct fields** section, select **Add field**, then **New field**.

<img src="./media/struct-field-ontology-manager.png" alt="Sample struct fields in a struct property type." width="500" />

6. Name the new struct field and optionally add a description.
7. Lastly, map a column from a datasource to the new struct field.
