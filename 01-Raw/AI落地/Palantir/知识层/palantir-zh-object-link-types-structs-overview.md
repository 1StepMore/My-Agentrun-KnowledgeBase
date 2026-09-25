---
title: Palantir 官方文档 · 对象与链接类型 · structs-overview
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/object-link-types/structs-overview/
lang: zh
keywords:
- Palantir
- Foundry
- ontology-construction
- semantic-layer
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:23:28+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# 概述

:::callout{theme="neutral" title="Struct 可用性"}
Struct 属性类型目前正在开发中，将于2024年9月普遍可用。
:::

**Struct** 是一种Ontology [基础类型](/docs/foundry/object-link-types/type-reference/#base-types)，允许用户创建具有多个字段的基于模式的属性。Struct 属性从 struct 类型数据集列创建。Struct 属性字段可以具有不同的数据源，只要在Ontology中定义之前将属性转换为单个 struct 类型列即可。

许多常见的 Object 属性可以建模为 struct。例如，具有 `First Name` 和 `Last Name` 字段的 `Full Name` 属性，或包含 `Street`、`City`、`Postal Code` 和 `Country` 字段的 `Address` 属性。

## Struct 配置

以下是 struct 属性约束和允许配置的列表：

* Struct 的深度为1，不能嵌套。
* Struct 必须至少有1个字段，最多可包含10个字段。
* 目前仅支持以下字段类型：
  * `BOOLEAN`
  * `BYTE`
  * `SHORT`
  * `INTEGER`
  * `LONG`
  * `FLOAT`
  * `DOUBLE`
  * `DECIMAL`
  * `STRING`
  * `BINARY`
  * `DATE`
  * `TIMESTAMP`
  * `GEOHASH`

## 当前支持水平

随着对 struct 属性类型支持的扩展，其可用性将在 Palantir 平台上有所不同。

Struct 目前在以下应用程序和服务中受到支持：

* **[Ontology Manager](/docs/foundry/ontology-manager/overview/)：** 定义和编辑 struct。
* **[Workshop](/docs/foundry/workshop/overview/)：** 对 struct 的基本渲染支持。
* **[Marketplace](/docs/foundry/marketplace/overview/)：** 打包和安装 struct 属性。

Struct 目前在以下服务中尚不支持：

* **[Object Explorer](/docs/foundry/object-explorer/search-objects/)：** 目前不支持通过 struct 属性值搜索 Object。
* **[Functions](/docs/foundry/functions/overview/)：** Functions 中不支持使用 struct 属性。
* **[Actions](/docs/foundry/action-types/overview/)：** Actions 中不支持使用 struct 属性。
* **[Ontology SDK](/docs/foundry/ontology-sdk/overview/)：** Ontology SDK 应用程序中不支持使用 struct 属性。

Struct 将不支持 Object Storage v1 (Phonograph)。
