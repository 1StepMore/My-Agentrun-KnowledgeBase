---
title: Palantir 官方文档 · data-lineage · 查看权限标记更改的影响
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/data-lineage/see-impact-marking-changes/
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

# 查看权限标记更改的影响

您可以使用数据沿袭来评估对数据集权限标记的更改如何影响派生数据集。这在[移除权限标记](/docs/foundry/building-pipelines/remove-markings/)时非常有用。

:::callout{theme="warning" title="警告"}
权限标记模拟依赖于最近的数据集搭建，并且不考虑尚未最终确定的更改。请确认您正在使用的是最新版本的数据。
:::

## 访问模拟模式

1. 打开**访问信息**侧边栏。
2. 开启**模拟访问要求**。
3. 在图表上选择任何数据集。
4. 点击**编辑权限标记**。

![访问信息侧边栏](../../foundry-docs/data-lineage/media/marking-simulation-helper-sidebar.png)

## 模拟权限标记更改

![模拟权限标记更改](../../foundry-docs/data-lineage/media/marking-simulation-apply.png)

要模拟权限标记的应用，请搜索您要应用的权限标记，勾选权限标记旁边的框，然后选择**模拟更改**按钮。

已经应用于数据集的权限标记将显示为已选中。要模拟移除权限标记，请取消选中权限标记旁边的框并点击**模拟更改**。

:::callout{theme="neutral"}
您只能移除直接应用于数据集的权限标记。无法模拟通过数据集沿袭或从父项目继承的权限标记的移除。
:::

## 分析模拟图表

![分析模拟图表](../../foundry-docs/data-lineage/media/marking-simulation-analyze.png)

在模拟模式下，图表的颜色将指示受权限标记更改影响的数据集。界面中标注了图表颜色，可以表示以下数据集状态：

* **模拟更改应用**显示在您应用更改的数据集上。
* **访问受影响**显示在更改前后权限标记不同的数据集上。
* **访问不受影响**显示在更改前后权限标记相同的数据集上。
* **没有可见的事务**显示在尚未搭建的数据集或您无权限查看事务的数据集上。

选择任何数据集时，**访问信息**侧边栏将显示模拟的访问要求。您可以切换模拟模式的开关来查看差异，而不会丢失任何模拟更改。

## 理解更改的提示

在进行更改之前，我们建议查阅[权限标记文档](/docs/foundry/security/markings/)以了解权限标记对用户的影响。

在模拟权限标记时，考虑以下几点：

* 数据集可以[通过代码停止传播权限标记](/docs/foundry/building-pipelines/remove-inherited-markings/)。 <br><img src="../../foundry-docs/data-lineage/media/marking-simulation-stop-propagating.png" alt="显示停止传播权限标记的权限颜色" width="400" />
  * 在**权限**颜色中，数据沿袭图上的节点显示停止传播权限标记，表示数据访问被*通过代码修改*。此消息也将显示在节点属性侧边栏的**访问信息**部分。
  * 在代码助手中，您可以检查数据集的代码，看看它是否通过使用术语`stop_propagating`来停止传播权限标记。
* 数据集可以从*其他输入*中继承权限标记；通过点击数据集节点左侧的箭头展开数据集输入。
* 权限标记可以应用于*父项目或文件夹*；当未启用模拟模式时，权限标记的左侧将显示文件夹图标，当启用模拟模式时，权限标记模拟菜单中将显示文件夹图标。
