---
title: Palantir 官方文档 · data-lineage · 查看搭建时间线
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/data-lineage/build-timeline/
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

# 查看搭建时间线

在数据沿袭中使用 **搭建时间线** 工具查看数据集的搭建历史。

在数据沿袭中，点击窗口左下角的 **搭建时间线**。此操作会展开查看面板，显示在您选择的时间段内发生的搭建的甘特图。您可以选择想要在时间线中查看的天数或小时数，范围从一小时到十天。您还可以选择按颜色显示搭建，基于日程安排或任务状态。

![在数据沿袭中查看搭建时间线](../../foundry-docs/data-lineage/media/build-timeline.png)

要查看特定数据集的搭建时间线，请在图表中选择数据集。使用 **拖动选择模式** 工具或按住 `Ctrl / Command` 键同时点击选择多个数据集。

要查看搭建时间线中任务的详细信息，请点击甘特图中的任务。您将看到关于任务状态、起始时间和结束时间及持续时间的信息。

![在搭建时间线中查看任务详细信息](../../foundry-docs/data-lineage/media/job-details-window.png)

通过点击任务信息窗口中的链接查看更多关于搭建、任务和日程安排的详细信息。
