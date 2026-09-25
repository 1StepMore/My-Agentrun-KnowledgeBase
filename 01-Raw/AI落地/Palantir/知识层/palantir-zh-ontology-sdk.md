---
title: Palantir 官方文档 · ontology-sdk · Ontology SDK
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:24:14+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# Ontology SDK

Ontology软件开发工具包（SDK）允许您直接从开发环境访问Ontology的全部功能。您可以通过Developer Console生成Ontology SDK，这是一个用于创建和管理应用程序的新门户，使用Palantir API。Ontology SDK支持TypeScript的NPM（Node包管理器）包，Python的Pip或Conda，Java的Maven，以及任何其他语言的OpenAPI规范。

将Foundry作为您的后端，您可以利用Ontology强大的高规模查询能力和Foundry数据输出，以及细粒度的治理控制，加速安全开发能够为您的组织提供动力的应用程序的过程。

![Demo应用程序设置页面](../../foundry-docs/ontology-sdk/media/osdk-demo-app.png)

## Ontology SDK的优势

Ontology SDK的构建旨在提供几个主要优势：

* **加速开发：** 使用Ontology SDK，您可以快速开始开发由Foundry Ontology支持的应用程序。通过使Ontology API的访问更为便利，Ontology SDK允许您以最少的代码读取和写入Ontology。
* **强类型安全：** 为Ontology SDK生成的函数和类型仅基于与您相关的Ontology子集。从您的Ontology生成类型和函数，使您能够直接在编辑器中查询和探索您的Ontology。
* **集中化维护：** 由于Ontology在Foundry中集中构建和管理，您可以专注于应用程序搭建，减少构建数据基础所需的典型维护负担。
* **安全设计：** Ontology SDK使用的词元仅限于您希望应用程序访问的本体实体，此外还有用户对数据的权限。

此外，前端开发的TypeScript绑定为开发者快速在Foundry之上搭建React应用程序提供了便利的方法。

![显示应用程序SDK概览的开发者控制台界面](../../foundry-docs/ontology-sdk/media/osdk-overview.png)

生成的代码使用关于您的Ontology的元数据，包括属性名称和描述。您可以直接在编辑器中查看此元数据。

## Developer Console

Developer Console是用于创建Ontology SDK应用程序和OAuth客户端的平台（以前在[控制面板](/docs/foundry/platform-security-third-party/third-party-apps-overview/)中称为第三方应用程序）。要访问Developer Console，请打开[应用程序门户](/docs/foundry/app-building/curating-apps/)并搜索`developer console`。

![访问开发者控制台](../../foundry-docs/ontology-sdk/media/developer-console-landing.png)

:::callout{theme="neutral"}
您可能需要[在控制面板中启用Developer Console](/docs/foundry/administration/configure-workspaces/#foundry-suite)。如需更多帮助，请联系您的Palantir代表。
:::
