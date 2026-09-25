---
title: Palantir 官方文档 · 对象与链接类型 · shared-property-overview
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/object-link-types/shared-property-overview/
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

:::callout{theme="warning" title="测试版功能"}
共享属性并非在所有Foundry注册中都可用。请联系您的Foundry代表以获取更多信息。
:::

**共享属性**是可以在您的Ontology中用于多个[Object类型](/docs/foundry/object-link-types/object-types-overview/)的[属性](/docs/foundry/object-link-types/properties-overview/)。共享属性允许在Object类型之间进行一致性的数据建模，并集中管理属性元数据。尽管属性元数据在Objects之间共享，但底层的Object数据并不共享。

例如，在Ontology管理器中，您可能有`Employee`和`Contractor` Object类型，它们都有属性`start date`。通过创建一个`start date`共享属性并将其用于这两种Object类型，您可以使用一致的属性来建模数据，并在一个地方更新`start date`元数据，而不是在每个Object类型上进行更新。

共享属性可以[直接创建](/docs/foundry/object-link-types/create-shared-property/)，或者现有的Object类型属性可以转换为共享属性。添加到您的Ontology后，共享属性可以在Object类型上[使用](/docs/foundry/object-link-types/use-shared-property/)，作为Ontology化数据的一部分，并以类似于常规属性的方式[编辑](/docs/foundry/object-link-types/edit-shared-property/)。

Objects上的共享属性在其名称旁边标有一个地球图标。

<img src="../../foundry-docs/object-link-types/media/shared-property-menu-option.png" alt="Ontology管理器中的共享属性页面" width="800" />
