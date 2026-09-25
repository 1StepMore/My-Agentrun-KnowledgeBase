---
title: Palantir 官方文档 · platform-security-management · 管理项目约束
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-management/manage-project-constraints/
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

# 管理项目约束

要在项目上添加约束，您必须在项目中拥有`Owner`角色，并在所有作为项目约束添加的权限标记上添加“应用权限标记”权限。如果添加或修改项目约束会导致项目中的现有文件违反您尝试添加的约束，您将无法添加或修改项目约束。

要管理约束，请导航到右侧访问面板中的权限标记部分。

![项目约束 - 概述](../../foundry-docs/platform-security-management/media/pmc-1.png)

## 项目约束违规

在应用项目约束后，如果某个违规的权限标记在上游某处被添加并被项目中的数据集继承，则数据集仍可能违反项目约束。这会通过警告显示在违反的数据显示集上。如果数据集违反了项目约束，则在解决违规问题之前无法搭建。

![项目中的数据集标有违规警告。](../../foundry-docs/platform-security-management/media/pmc-violation.png)

可以通过以下操作解决项目约束违规：

* 将此继承的权限标记添加为允许的项目约束。
* 从必要的变换中移除引入新权限标记的输入。
* 移除继承的上游权限标记。了解如何在我们的文档中[移除权限标记](/docs/foundry/building-pipelines/remove-markings/)。
