---
title: Palantir 官方文档（英文原版）· Generate OSDK for other languages
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/ontology-sdk/generate-osdk-for-other-languages/
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
> 原始地址：https://palantir.com/docs/foundry/ontology-sdk/generate-osdk-for-other-languages/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-ontology-sdk-generate-osdk-for-other-languages.md`

# Generate OSDK for other languages

The Developer Console has built-in Java, Python, and TypeScript support for code generation using both pip and Conda but is not limited to these languages. Developer Console also supports exporting APIs in the industry-standard [OpenAPI format ↗](https://www.openapis.org/). You can use open source code generators to generate a client based on the downloaded OpenAPI spec in almost any language.

## Export an OpenAPI spec

Navigate to the **Application API** page in the Developer Console application and open the **SDK generation** tab. Then, choose **Other languages** and select **Export as OpenAPI**.

![export OpenAPI spec](/docs/resources/foundry/ontology-sdk/osdk-generate-other-language.png)

:::callout{theme="warning"}
As the exported file will include the name and the description of the resources included in the Developer Console application, ensure these fields do not contain sensitive information.
:::

## Generate clients and server in other languages

Once the OpenAPI file has been exported, you can generate a client and server using an open source generator. A list of OpenAPI generators can be found on the [OpenAPI generator web site ↗](https://openapi-generator.tech/docs/generators).
