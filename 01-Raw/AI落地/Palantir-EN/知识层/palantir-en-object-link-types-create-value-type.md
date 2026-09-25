---
title: Palantir 官方文档（英文原版）· Create a value type
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/create-value-type/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/create-value-type/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-create-value-type.md`

# Create a value type

Follow the steps below to create a value type to use across your platform [space](/docs/foundry/security/orgs-and-spaces/#spaces).

1. Navigate to the **Value Types Manager** application from the platform sidebar.
2. From the top left corner, use the dropdown menu to select the space in which you would like to create a value type.
3. Select **Create New Value Type** from the upper right corner.
4. Provide a clear name, description, and unique API name for your value type.

<img src="./media/value-type-create-metadata.png" alt="Value type metadata creation" width="500" />

5. Choose a [base type](/docs/foundry/object-link-types/base-types/) for your value type.
6. (Optional) Define a constraint for your value type. Validation methods include regular expressions for `String` types, enumerated values, ranges, and other methods depending on the base type.
   For a full list of constraints supported by base type, review our [value type constraints](/docs/foundry/object-link-types/value-type-constraints/) documentation.
   When you define a constraint, configure the **Failure validation message** that appears when a value does not satisfy the constraint.

<img src="./media/value-type-create-constraint.png" alt="Value type constraint creation" width="500" />

7. (Optional but recommended) Provide an example preview value for your value type.

<img src="./media/value-type-create-preview.png" alt="Value type preview creation" width="500" />

8. Save your value type.
