---
title: Palantir 官方文档（英文原版）· Edit-only properties
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/edit-only-properties/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/edit-only-properties/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-edit-only-properties.md`

# Edit-only properties

Edit-only properties allow you to define Ontology properties that are not directly mapped to a column in the backing dataset of the object type.
This is particularly useful for situations where you may want to store additional information alongside your object types without modifying the underlying dataset.

:::callout{theme="neutral"}
To populate all property values through user edits, consider [creating an object type without a backing datasource](/docs/foundry/object-link-types/create-object-type/#create-an-object-type-without-a-backing-datasource).
:::

## Summary of edit-only properties

When working with edit-only properties, keep the following in mind:

* **No mapping to a column in the backing dataset:** Edit-only properties are not required to be mapped to a specific column in the backing dataset. This allows you to easily create new properties before the backing column exists, or create properties that will only be edited through the ontology.
* **Permissioned to one of the datasets backing the object type:** To ensure data consistency and security, edit-only properties must be permissioned to one of the datasets backing the object type.
* **Available only in Object Storage v2:** Edit-only properties are a feature that is exclusively available for object types leveraging Object Storage v2.

### Creating edit-only properties

1. Navigate to the **Ontology Manager**.
2. Choose the object type to which you want to add an edit-only property.
3. Select **Create Property** and fill in the required details, including the property name, type, and description.
4. Under the **Data** section, toggle on the **Edit-only property** toggle and choose a dataset to permission to (if you have more than one dataset backing the object type).
5. **Save** your changes to create the edit-only property.

<img src="./media/edit_only_property.png" alt="Edit-only property" width="300" />

### Mapping edit-only properties to dataset columns

If you later decide to add a column to your backing dataset that corresponds to a property that is currently edit-only, you can easily map that property to the new column.

1. Navigate to the **Ontology Manager**.
2. Choose the object type with the edit-only property you want to map.
3. Select the edit-only property to open its details.
4. Under the **Data** section, untoggle the edit-only property and choose a column from one of the backing datasets.
5. **Save** your changes.
