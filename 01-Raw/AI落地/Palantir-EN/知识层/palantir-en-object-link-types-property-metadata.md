---
title: Palantir 官方文档（英文原版）· Metadata reference
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/property-metadata/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/property-metadata/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-property-metadata.md`

# Metadata reference

A property is represented in the Ontology by the following metadata:

* **ID:** A unique identifier of the property, primarily used to reference the property when configuring an application. For example, `start-date` may be the ID of the start date property.
* **Display name:** The name shown to anyone accessing property values for this property in user applications. For example, the display name for the `start date` property may be `Start date`.
* **Description:** Explanatory text about the property that anyone can read in user applications. For example, the description of the `start date` property may be `The day the employee began new hire training`.
* **RID:** An automatically generated unique identifier for every resource in Foundry. A property’s RID will be referenced in error messages across the platform.
* **Status:** A signal to users and other Ontology builders about where in the development process the property stands. It can be `active`, `experimental`, or `deprecated`. By default, the `start date` property will have status `experimental`. Read more about [statuses](/docs/foundry/object-link-types/metadata-statuses/).
* **API name:** The name used when referring to the property programmatically in code. For example, the API name of the `start date` property may be `startDate`. Read more about [API names (TSv1)](/docs/foundry/functions/api-objects-links/).
* **Keys:** An indication of whether the property is the object type’s title key or primary key.
  * The **title key** is the property that acts as a display name for objects of this type. For example, setting the `full name` property as the title key of the `Employee` object type will use the values of that property, such as the notional employees “Melissa Chang” and “Diego Rodriguez” as the display names for each respective `Employee` object.
  * The **primary key** is the property that acts as a unique identifier for each instance of an object type, meaning that each row in the backing datasources must have a different value for this property. For example, the value of the `employee number` property may be used to identify “Melissa Chang” as a unique employee within the organization.
* **Base type:** Indicates the type of values for this property and determines the set of operations available in user applications. For example, the `start date` property will have base type `date`. User applications will allow you to configure a timeline widget with this property.
* **Value formatting:** Depending on the base type of the property, numeric formatting, date and time formatting, user ID and resource ID formatting are available to apply to the property, transforming its raw values into more readable versions in user applications. Read more about [value formatting](/docs/foundry/object-link-types/value-formatting/).
* **Conditional formatting:** Rules set on a property that dictate how that property value will render (e.g coloring, alignment, etc.) in user facing applications. For example, you may set a rule on the `full name` property that colors its values green if the value of the `start date` property was less than 2 weeks ago, in order to indicate a new hire in user applications. Read more about [conditional formatting](/docs/foundry/object-link-types/conditional-formatting/).
* **Type classes:** Additional metadata that are interpreted by user applications. Read more about [type classes](/docs/foundry/object-link-types/metadata-typeclasses/).
* **Render hints:** Indications to user applications about how to render the property that may be different than most properties of the same base type. Many render hints can be used to impact the performance of reindexes of the object type the property is defined on. For example, if you do not expect any users to search or sort on the `start date` property in user applications, you can deselect the `searchable` and `sortable` render hints and improve the reindex performance of the `Employee` object type. Read more about [render hints](/docs/foundry/object-link-types/metadata-render-hints/).
* **Visibility:** An indication to user applications for how prominently to display the property. A `prominent` property will lead applications to show this property first to users. A `hidden` property will not appear in user applications. By default, the `start date` property will have visibility `normal`.

[Learn more about creating and configuring properties in the Ontology and about validation requirements for property metadata.](/docs/foundry/object-link-types/create-object-type/)

## Property base types with limited support

Some property base types have limited support. These types are indicated with the `Limited support` tag which is visible in the property base type picker.

* `byte`:
  * Properties of this type cannot be used within action types.
* `float`:
  * Properties of this type cannot be used within action types.
* `short`:
  * Properties of this type cannot be used within action types.
* `vector`:
  * Vectors can only be queried by [KNN (TSv1)](/docs/foundry/functions/api-object-sets/#k-nearest-neighbors-knn).
  * The max vector dimension is 2048.

For more information on the limitations of property base types in action types, see [the documentation on supported property types](/docs/foundry/action-types/scale-property-limits/#supported-property-types).
