---
title: Palantir 官方文档（英文原版）· Edit a struct property type
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/edit-struct-type/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/edit-struct-type/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-edit-struct-type.md`

# Edit a struct property type

1. In Ontology Manager, open the **Object types** tab in the left sidebar and select an existing object type.
2. In the object type details page, open the **Properties** tab in the left sidebar, and select the relevant struct property type from the **Properties** table.
3. In the **Property editor** panel, scroll to the **Struct fields** section and select the struct field you would like to edit. The number of edits made will appear on the top right of the Ontology Manager interface.

<img src="./media/Edit-struct.png" alt="Struct fields in the 'Property editor' panel." width="500" />

4. Make the necessary edits in the **Edit struct field** dialog, and select **Confirm**.

<img src="./media/confirm-struct-edit.png" alt="The 'Edit struct field' dialog." width="500" />

:::callout{theme="neutral"}
Changing a struct field's API name will result in a new struct field RID being generated. This will override the existing index, similar to the behavior of changing the property ID of a property type. Any applications that reference the updated struct field will need to be updated as well.
:::
