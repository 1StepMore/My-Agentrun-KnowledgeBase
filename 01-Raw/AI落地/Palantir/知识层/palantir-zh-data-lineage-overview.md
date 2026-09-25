---
title: Palantir 官方文档 · data-lineage · overview
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/data-lineage/overview/
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

# 概述

**数据沿袭**是一个交互式工具，帮助全面查看数据如何在Foundry平台中流动。

![Data Lineage流动动画](../../foundry-docs/data-lineage/media/data-lineage-flow.gif)

使用数据沿袭，您可以：

* 轻松查找和发现数据集
  * 使用项目、表和列名称搜索数据集
  * 点击浏览Foundry项目中的数据
* 通过强大的界面探索[管道](/docs/foundry/data-integration/data-pipeline/)
  * 展开或隐藏数据集的祖先和后代
  * 同时查看一组表的属性
  * 通过着色可视化您的管道（例如，对过期的表进行着色）
  * 深入了解您的数据细节，例如其架构、最后构建时间以及生成数据的代码
* 与队友协作
  * 创建管道快照与其他用户共享
