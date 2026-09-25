---
title: Palantir 官方文档 · data-lineage · 探索数据沿袭
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/data-lineage/explore-lineage/
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

# 探索数据沿袭

数据沿袭帮助您了解数据的来源。在数据沿袭应用中，有多种方式可以探索数据管道。考虑一种常见的路径：

1. 使用**搜索**助手，找到您的资源（例如，数据集或Object类型）并将其添加到图中。

2. 点击节点的左箭头以显示资源的直接父级。

![展开父级](../../foundry-docs/data-lineage/media/data-lineage-see-parents.png)

3. 若要扩展您的图形，请在图中选择下一个资源并点击图形工具中的**展开**按钮。

4. 点击折角按钮以定义要显示的层级数。点击双折角以扩展到原始数据（或扩展到最终的后代）。

:::callout
同时添加过多节点可能会影响图形的性能和可用性。通过检查**展开**工具中的节点计数保持一个可管理的节点数量。
:::

![全部展开](../../foundry-docs/data-lineage/media/data-lineage-expand-all.png)

:::callout{theme="success"}
通过选择**展开**按钮并添加资源之间的所有节点或所有共同的祖先/后代，可以在图中找到两个节点之间的关系。
:::

5. 通过选择数据集并使用底部面板显示数据预览，获取有关某个数据集的更多信息。

6. 点击**代码**以查看数据集的创建方式。

![数据集代码预览](../../foundry-docs/data-lineage/media/data-lineage-dataset-code.png)

7. 点击**在代码工作簿中查看**或**在存储库中查看**以查看原始代码并根据需要进行更改（需符合权限）。

:::callout
根据资源类型，某些选项可能对某些数据集不可用。例如，**代码**仅适用于代码工作簿或代码存储库。对于没有代码显示的Fusion表同步，您可能有查看源表并在那里进行更改的选项（如果您拥有适当的权限）。
:::
