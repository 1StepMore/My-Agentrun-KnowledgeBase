---
title: Palantir 官方文档（英文原版）· Unsupported types in OSDK
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/ontology-sdk/unsupported-types/
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
> 原始地址：https://palantir.com/docs/foundry/ontology-sdk/unsupported-types/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-ontology-sdk-unsupported-types.md`

# Unsupported types in OSDK

The OSDK generates client-side code for TypeScript, Python, and Java packages; this code represents object types, action types, and functions from the Ontology. Not all data types are currently available in the OSDK; this page lists data types that are not yet supported.

## Object types: Unsupported property types

If you use an object type with a property of a type which is listed below, the code generator will skip that property and log the error.

### Typescript SDK

The following Typescript SDK property types are unsupported:

* `Cipher`
* `Marking`
* `Vectors`

### Python SDK

The following Python SDK property types are unsupported:

* `Cipher`
* `Marking`
* `Media`
* `Struct`, except for [beta struct property support in Python functions](/docs/foundry/functions/python-ontology-edits/#edit-struct-properties)
* `Vector`

### Java SDK

The following Java SDK property types are unsupported:

* `TimeSeries`
* `Cipher`
* `Vector`

## Action types: Unsupported parameter types

If you use an action type with a parameter of a type mentioned below, the code generator will be unable to create your package. To resolve this, you must remove that action type from the SDK application until support is added for that type.

### TypeScript SDK

The following TypeScript SDK parameter types are unsupported:

* `InterfaceObjectSet`
* `MarkingList`

### Python SDK

The following Python SDK parameter types are unsupported:

* `ObjectSet`

## Action types: Unsupported webhook types

Action types with [webhooks that use OAuth 2.0 for authentication](/docs/foundry/data-connection/webhooks-reference/#oauth-20-with-webhooks) are not supported. This is because users would be unable to use these action types through the SDK application without first authorizing the outbound application through Foundry (for instance, by first calling the action in a Workshop application).

## Functions: Unsupported input parameter types and output types

If you use a function with an input or an output of a type which is listed below, the code generator will fail to generate your package. To resolve this, you must remove that function from the SDK application until such support is added.

### Typescript SDK

#### Function output types

The following Typescript SDK function output types are unsupported:

* `Principal`
* `User`
* `Notification`
* `OntologyEdit`
* `ClassificationMarking`

### Python SDK

#### Function input parameter types

The following Python SDK function input types are unsupported:

* `ObjectSet`
* `AnonymousCustomType`
* `CustomType`
* `GeoShape`
* `Group`
* `MandatoryMarking`
* `ModelGraph`
* `Notification`
* `OntologyEdit`
* `Principal`
* `Range`
* `StringFunctionDateType_ThreeDimensionalAggregation`
* `TimeSeries`
* `TwoDimensionalAggregation`
* `User`

#### Function output types

The following Python SDK function output types are unsupported:

* `ObjectSet`
* `AnonymousCustomType`
* `CustomType`
* `GeoShape`
* `Group`
* `MandatoryMarking`
* `ModelGraph`
* `Notification`
* `OntologyEdit`
* `Principal`
* `Range`
* `StringFunctionDateType_ThreeDimensionalAggregation`
* `TimeSeries`
* `TwoDimensionalAggregation`
* `User`

### Java SDK

#### Function input parameter types

The following Java SDK function input types are unsupported:

* `AnonymousCustomType`
* `ClassificationMarking`
* `CustomType`
* `GeoShape`
* `Group`
* `MandatoryMarking`
* `ModelGraph`
* `Notification`
* `OntologyEdit`
* `Principal`
* `Range`
* `StringFunctionDateType_ThreeDimensionalAggregation`
* `TimeSeries`
* `TwoDimensionalAggregation`
* `User`

#### Function output types

The following Java SDK function output types are unsupported:

* `AnonymousCustomType`
* `ClassificationMarking`
* `CustomType`
* `GeoShape`
* `Group`
* `MandatoryMarking`
* `ModelGraph`
* `Notification`
* `OntologyEdit`
* `Principal`
* `Range`
* `StringFunctionDateType_ThreeDimensionalAggregation`
* `TimeSeries`
* `TwoDimensionalAggregation`
* `User`

## OpenAPI Specification

You can [export an OpenAPI specification from Developer Console](/docs/foundry/ontology-sdk/generate-osdk-for-other-languages/). OpenAPI supports the `any` type, so you can still use the specification even if some types are unsupported. However, you will need to define the format for those parameters manually.

The following types do not have first-class support in the OpenAPI specification and will be rendered as `any`:

* `Struct`
* `Vector`
