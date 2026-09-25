---
title: Palantir 官方文档 · ontology-sdk-react-applications · 故障排除
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk-react-applications/troubleshooting/
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

# 故障排除

本页面包含在开发OSDK React应用程序时可能遇到的错误的故障排除提示。如果您有其他问题或无法通过本指南解决您的问题，请[报告问题](/docs/foundry/getting-started/issues/#report-an-issue)给Palantir客服支持。

## 工作区错误

如果在Palantir平台内工作，您将使用运行在Palantir代码工作区基础设施上的VS Code工作区。更多故障排除信息可以在以下文档中找到：

* [VS Code工作区故障排除](/docs/foundry/vs-code/troubleshooting/)
* [代码工作区故障排除](/docs/foundry/code-workspaces/troubleshooting/)

## npm故障排除步骤

如果您在运行npm命令时遇到问题，请尝试以下故障排除步骤：

* 删除锁定文件（`package-lock.json`）和依赖文件夹（`node_modules/`），然后重新运行出错的命令。
* 暂停并恢复工作区。

### `NPM MODULE_NOT_FOUND`错误：添加新依赖

代码库要求显式声明您的依赖。

默认情况下，我们添加以下npm库：

* 常见的OSDK依赖：`foundry-sdk-asset-bundle`，`osdk-templates-bundle`
* [npmjs.com ↗](https://www.npmjs.com/) 镜像：`external-npm-npmjs`
* 您的OSDK： `SDK Artifacts Repository - <rid>`

![代码库中的"Libraries"设置页面。](../../foundry-docs/ontology-sdk-react-applications/media/code-repositories-libraries-page.png)

如果您尝试添加一个在任何支持库中不存在的软件包，`npm install <package>`命令可能会失败。例如，如果您尝试安装的软件包是私有的，您必须确保它作为库Artifact存在。查看我们的[Artifacts文档](/docs/foundry/code-repositories/artifact-repositories-overview/)以获取更多信息。

示例错误：

![一个"Module not found" npm错误。](../../foundry-docs/ontology-sdk-react-applications/media/npm-module-not-found-error.png)

:::callout{theme="neutral"}
当VS Code工作区内无法访问**npmjs.com**时，npm将发出错误`code E401 Incorrect or missing password`。
:::
