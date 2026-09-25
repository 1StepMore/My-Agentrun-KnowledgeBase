---
title: Palantir 官方文档 · data-lineage · 管理计划
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/data-lineage/manage-schedules/
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

# 管理计划

数据沿袭允许您轻松管理沿袭图中的搭建计划。在右侧边栏中，选择**管理计划**以打开计划详情窗格。

![在数据沿袭中管理计划](../../foundry-docs/data-lineage/media/manage-schedules.png)

您将看到与图中选定数据集相关的计划。点击某个计划以查看更多详情：

![在数据沿袭侧边栏中管理计划详情](../../foundry-docs/data-lineage/media/manage-schedule-details.png)

* **最新运行：** 计划最新一次运行的状态。
* **最后更新：** 最后一次更新的时间戳以及进行更改的用户
* **目标数据集：** 搭建计划中包含的下游数据集列表。
* **搭建时机：** 显示创建搭建计划时确定的搭建计划触发器。例如，可以将搭建计划设置为在**特定数据集更新时**运行。
* **搭建范围：** 定义搭建中包含的项目或用户数据集及运行搭建所使用的权限。

在[**搭建管道**](/docs/foundry/building-pipelines/scheduling-overview/)文档中了解更多关于计划搭建的信息。
