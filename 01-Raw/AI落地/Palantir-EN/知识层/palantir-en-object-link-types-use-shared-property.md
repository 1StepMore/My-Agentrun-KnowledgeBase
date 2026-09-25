---
title: Palantir 官方文档（英文原版）· Use shared properties on object types
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/use-shared-property/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/use-shared-property/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-use-shared-property.md`

# Use shared properties on object types

To update a property on an object type to a shared property, complete the following steps:

1. Navigate to the object type in the Ontology Manager.
2. Select the property on the panel that you want to update, then scroll down to the **Shared Property** section of the configuration.

<img src="./media/convert-shared-property.png" alt="Using a shared property" width="500" />

3. Use the dropdown menu to select an existing shared property to use, or convert the property to a new shared property with the [shared property creation](/docs/foundry/object-link-types/create-shared-property/) modal.

The property will then display as a shared property. To persist the use of the shared property to the Ontology, select **Save** in the upper right.

* When using a shared property on an object, the property ID and API name of the object-specific property will remain unchanged so as to not break existing downstream workflows that leverage them.
* While associated with a shared property, direct edits to property metadata that is inherited from the shared property will be disabled. You can still add, delete, or edit type classes. When the property is loaded, the resulting set of type classes will be a union of those from the property and its associated shared property.
* If the shared property you use has different [render hint](/docs/foundry/object-link-types/metadata-render-hints/) configuration values than the selected property, using the shared property will override the configuration values of the selected property. Make sure your shared property is configured with the proper render hints for your use case.

### Detach a shared property from an object

To detach a property from a shared property, use the same property panel on an object type in the Ontology Manager and select **Detach**.

<img src="./media/detach-shared-property.png" alt="Detach a shared property" width="500" />

Doing so will remove the association between the property and the shared property.
