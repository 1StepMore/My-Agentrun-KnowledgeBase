---
title: Palantir 官方文档 · data-lineage · 预览和逻辑
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/data-lineage/dataset-preview-logic/
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

# 预览和逻辑

数据沿袭界面允许您查看所选数据集或媒体集的预览，并检查相关代码以理解数据集或媒体集背后的逻辑。

## 预览

要查看数据集或媒体集的预览，请在您的数据沿袭图中选择它，然后在界面左下角选择 **预览** 选项卡。

### 媒体集

当媒体集预览展开时，您可以查看媒体集的内容。[了解更多关于媒体集的信息。](/docs/foundry/data-integration/media-sets/).

PDF预览示例：

![媒体集PDF预览](../../foundry-docs/data-lineage/media/dl-pdf-preview.png)

音频预览示例：

![媒体集音频预览](../../foundry-docs/data-lineage/media/dl-audio-preview.png)

### 数据集

当数据集预览展开时，您可以滚动浏览所选数据集的前300行。您还可以使用预览窗口右侧的 **搜索列...** 字段搜索特定列。根据数据集中数据的类型，数据集的预览将有所不同。

![查看数据集预览](../../foundry-docs/data-lineage/media/dataset-preview.png)

## 逻辑

选择 **代码** 选项卡以查看所选数据集或媒体集的代码逻辑。在 **代码** 视图中，您可以快速编辑、搜索项目，或在用于推导数据的代码库或其他应用程序中打开代码。

![查看数据集代码](../../foundry-docs/data-lineage/media/dataset-code.png)

:::callout
上传和数据输出数据集在数据沿袭中没有可查看的相关代码。
:::
