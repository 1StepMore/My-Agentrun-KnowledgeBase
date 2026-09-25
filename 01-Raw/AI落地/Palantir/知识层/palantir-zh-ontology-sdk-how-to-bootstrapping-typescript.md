---
title: Palantir 官方文档 · ontology-sdk · 引导一个新的 Ontology SDK TypeScript 应用程序
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-typescript/
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

# 引导一个新的 Ontology SDK TypeScript 应用程序

本页面将引导您使用 `@osdk/create-app` CLI 工具在流行的 JavaScript 框架之上创建前端应用程序的过程。

如果您想为现有应用程序添加 Ontology SDK 支持，请查看我们的文档[如何将 Ontology SDK 添加到现有应用程序](/docs/foundry/ontology-sdk/how-to-add-to-existing-typescript/)。

## 1: 先决条件

### 创建一个 Developer Console 应用程序

请按照[创建一个新的 Developer Console 应用程序](/docs/foundry/ontology-sdk/create-a-new-osdk/)页面中列出的步骤操作。

### 设置您的词元

在本地环境中导出您的词元。以下是使用示例个人访问词元的示例，但您可以在 Developer Console 中生成一个更长时间有效的词元。此词元不应被检入源代码控制，因为它是您的个人访问词元。

```bash
# 将FOUNDRY_TOKEN环境变量设置为你从入门页面获取的令牌
export FOUNDRY_TOKEN=<YOUR-TOKEN-FROM-GETTING-STARTED-PAGE>
```

### 检查 Node 版本

TypeScript SDK 需要 Node 18 或更高版本才能工作。要检查您正在使用的 Node 版本，请输入以下命令：

```bash
node --version
# 输出 Node.js 的版本号
```

## 2. 快速开始使用 `@osdk/create-app`

### 创建您的前端应用程序

运行提供的命令，并按照交互式提示自定义您的项目，包括项目名称和框架选择。在 **入门** 页面上，您会找到特定于应用程序的信息，这些信息将预先填入命令中。以下是此代码的示例，其中 `< >` 内是您的具体详细信息将被填入的占位符：

```bash
npm create @osdk/app@latest -- \
    --application <RID OF YOUR DEVELOPER CONSOLE APPLICATION> \ # 开发者控制台应用程序的 RID
    --foundryUrl <YOUR FOUNDRY URL> \ # Foundry 的 URL
    --applicationUrl <SUBDOMAIN OF YOUR FOUNDRY URL USED FOR HOSTING> \ # 用于托管的 Foundry URL 的子域名
    --clientId <YOUR CLIENT ID> \ # 您的客户端 ID
    --osdkPackage <YOUR PACKAGE NAME> \ # 您的包名
    --osdkRegistryUrl <YOUR PACKAGE HOSTING URL> \ # 您的包托管 URL
    --corsProxy false # 禁用 CORS 代理
```

此命令用于创建一个新的 OSDK 应用程序，您需要提供一些必需的信息，例如应用程序的 RID、Foundry 的 URL、客户端 ID 等。

:::callout{theme="neutral"}
在开发者控制台的 **API Documentation** 部分的 **Getting Started** 页面或 **Overview** 页面可以找到预填充了所有这些参数的命令。
:::

### 开发前端应用程序

现在，您的项目文件已经根据您输入的项目名称生成在一个目录中。可以通过运行以下命令启动本地开发服务器：

```bash
cd <project-directory> # 进入项目目录
npm install # 安装项目依赖
npm run dev # 运行开发服务器
```
