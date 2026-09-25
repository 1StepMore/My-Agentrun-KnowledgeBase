---
title: Palantir 官方文档（英文原版）· Value type constraints
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/value-type-constraints/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/value-type-constraints/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-value-type-constraints.md`

# Value type constraints

Each value type may optionally define a constraint to enforce data validation. You can configure these constraints when [creating a new value type](/docs/foundry/object-link-types/create-value-type/) in the **Value Type Manager** application. The available value type constraints, along with what base types they can be applied to, are below:

* **Enum (one of):** A constraint representing a static set of allowed values.
  * **Valid base types:** String, Boolean, Decimal, Double, Float, Integer, or Short.
  * For String properties, the enum values may optionally be case-sensitive or case-insensitive.
* **Range:** A minimum value, maximum value, or range of allowed values.
  * **Valid base types:** Decimal, Double, Float, Integer, Short, Date, Timestamp, String, or Array.
  * For String properties, the length of the string is constrained.
  * For Array properties, the size of the array is constrained.

Additionally, the following property types have additional type-specific constraints available:

* **String:**
  * **Regex:** A regex pattern that the string must match. The regex validation may optionally pass when matching only a substring of the property value.
  * **RID:** The string must be a valid rid.
  * **UUID:** The string must be a valid UUID.
* **Array:**
  * **Uniqueness:** All elements of the array must be unique.
  * **Nested:** A value type constraint can be applied to the elements of the array. For example, a regex constraint could be applied to every string in an array.
* **Struct:**
  * **Element constraints:** A mapping between a struct field identifier and a value type reference, where the struct field identifier indicates the struct component to which the referenced value type should be applied.
