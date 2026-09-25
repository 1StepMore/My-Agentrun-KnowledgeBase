---
title: Palantir 官方文档 · ontology-sdk · 为其他语言生成 OSDK
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/generate-osdk-for-other-languages/
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

# 为其他语言生成 OSDK

OSDK 开发者控制台内置了 TypeScript 和 Python 的支持，可以通过 pip 和 Conda 进行代码生成，但不限于这些语言。开发者控制台还支持以行业标准 [OpenAPI 格式 ↗](https://www.openapis.org/) 导出 API。您可以使用开源代码生成器基于下载的 OpenAPI 规范生成几乎任何语言的客户端。

## 导出 OpenAPI 规范

导航至开发者控制台应用程序中的 **Application API** 页面并打开 **SDK 生成** 选项卡。然后，选择 **Other languages** 并选择 **Export as OpenAPI**。

![export OpenAPI spec](../../foundry-docs/ontology-sdk/media/osdk-generate-other-language.png)

:::callout{theme="warning"}
由于导出的文件将包含开发者控制台应用程序中包含的资源的名称和描述，请确保这些字段不包含敏感信息。
:::

## 在其他语言中生成客户端和服务器

一旦 OpenAPI 文件被导出，您可以使用开源生成器生成客户端和服务器。OpenAPI 生成器的列表可以在 [OpenAPI 生成器网站 ↗](https://openapi-generator.tech/docs/generators) 上找到。
