---
title: Palantir 官方文档（英文原版）· Use value types
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/use-value-type/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/use-value-type/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-use-value-type.md`

# Use value types

Once you have [created a value type](/docs/foundry/object-link-types/create-value-type/), you can use it as a data type or reusable constraint across Foundry. Supported use cases include:

* Assigning a value type to an object type property.
* Assigning a value type to a shared property.
* Assigning a value type to a Pipeline Builder pipeline property as a logical type using the `logical type cast` expression and selecting the value type on the property when you write to the objects target.
* Constraining the values accepted by an action parameter.

## Assign a value type to a property

To assign a value type to a property, select the value type from the dropdown menu during property configuration.

<img src="./media/value-type-use.png" alt="A value type is selected during property configuration." width="500" />

:::callout{theme="warning"}
If you apply a value type to an object property that contains property values that fail validation, that object type will fail to index. You can view such index failures in the object type health status in Ontology Manager, where you can correct your data or update your value type to fix the issue.
:::

## Constrain an action parameter with a value type

Use a value type constraint to apply reusable validation rules to an action parameter:

1. In Ontology Manager, open the action type and select the **Parameters** tab.
2. Select the parameter that you want to constrain.
3. In the **Constraints** card, select **Value type** as the constraint type.
4. Select a value type.
5. Save your changes.

The value type selector only displays value types whose [base type](/docs/foundry/object-link-types/base-types/) is compatible with the parameter type. Value type constraints are available for `String`, `Integer`, `Long`, `Double`, `Decimal`, `Date`, and `Timestamp` parameters, including list parameters of these types. For a list parameter, select an `Array` value type to constrain the list as a whole. To apply the same constraint to each item in the list, select a compatible non-array value type. Value type constraints cannot be applied to struct parameters or their fields. You can [configure other supported constraints on individual struct parameter fields](/docs/foundry/action-types/actions-on-structs/#constraints-on-struct-parameter-fields).

During action validation and submission, the parameter value must satisfy the selected value type constraint. If validation fails, the action cannot be submitted and displays the value type's **Failure validation message**. Non-breaking updates to the value type automatically propagate to the action type. Learn more about [value type versions](/docs/foundry/object-link-types/value-types-versions/).
