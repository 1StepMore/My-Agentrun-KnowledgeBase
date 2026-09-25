---
title: Palantir 官方文档 · platform-security-management · 从“传播查看要求”设置迁移并禁用
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-management/disabling-propagate-view-requirements/
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

# 从“传播查看要求”设置迁移并禁用

:::callout{theme="warning" title="终止"}
自2023年6月起，大多数客户将禁用使用“传播查看要求”安全设置。强烈建议仍在使用已弃用的“传播查看要求”功能的客户遵循以下指南，以[项目](/docs/foundry/security/projects-and-roles/)和[权限标记](/docs/foundry/security/markings/)取代这种用法，以提高安全性可读性和管理。
:::

## 概述

当在项目上启用“传播查看要求”设置时，项目中的每个数据集都要求用户具有访问权限，以查看其下游数据集，无论它们位于此项目内还是不同的项目中。

我们建议禁用“传播查看要求”设置，并在必要时用权限标记替代。与“传播查看要求”设置不同，权限标记更清晰地定义了查看底层数据所需的要求。如果只有一些数据集包含敏感数据，请考虑为这些特定数据集添加适当的权限标记。如果整个项目都是敏感的，请在项目级别添加权限标记。

以下是迁移离开“传播查看要求”设置的步骤概要：

1. 在[升级助手](/docs/foundry/upgrade-assistant/overview/)应用中开始，并选择需要迁移的项目。
2. 考虑您的迁移选项，并决定哪种方法最适合您的情况。
3. 执行迁移。
4. 在项目上禁用“传播查看要求”。
5. 返回升级助手，确认不再有与此项目对应的待处理操作。

## 迁移步骤

### 1. 升级助手

进入Foundry中的升级助手应用，选择启用了“传播查看要求”的特定项目以开始迁移过程。

![upgrade-assistant](../../foundry-docs/platform-security-management/media/upgrade-assistant-pvr.png)

### 2. 选择如何迁移所选项目

有几种不同的方法可以从使用“传播查看要求”设置中迁移。您选择的方法取决于数据的敏感性、平台上已有的项目和权限标记，以及企业的安全架构。以下是迁移选项和帮助您决定下一步的问题清单。由于您的决定可能对隐私有重大影响，我们强烈建议阅读所有提供的选项。

#### 分类敏感数据

首先，确定项目是否包含敏感数据。背景很重要；某些数据是否被视为敏感取决于相关的隐私法规和贵组织的标准。

在Palantir中，敏感数据被定义为任何被广泛分类和/或需要额外安全的数据。一些法律正式指定特定数据元素为敏感（例如，[欧盟的一般数据保护条例](https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en)），而其他数据由数据所有者或无论法律地位如何的普遍认可决定（如社会安全号码）。数据是否被分类为敏感通常取决于数据的类型或分类（例如，个人可识别信息（PII）），工作流程的类型（如那些仅限于特定目的的工作流程），或可能触发受限访问控制的任何内容（包括敏感的企业信息）。

如上所述，常见的敏感数据示例之一是个人可识别信息（PII），其中包括直接标识符和其他可用于重新识别或识别个人的信息。

在这里，您应识别限制访问项目中的数据应限制访问从中派生的任何下游数据集、对象或资源的情况。如果项目中的数据没有PII属性，您可以跳到[在项目上禁用“传播查看要求”设置](#4-disable-propagate-view-requirements-on-the-project)。

如果项目中存在数据敏感性，请对其进行分类。例如：“此项目中的数据集X、Y和Z包含PII，而此项目中的数据集A、B和C包含财务信息”。

#### 验证是否对敏感数据应用了权限标记

[权限标记](/docs/foundry/platform-security-management/manage-markings/#use-markings)是Foundry中的一种安全控制，用于定义限制用户可见性和操作的资格标准。

与“传播查看要求”设置相似，[权限标记](/docs/foundry/security/markings/)是一种安全原语，会传播到下游数据集和资源。在考虑是否可以安全地关闭此项目的“传播查看要求”设置时，我们建议检查此项目中的敏感数据是否已被适当的权限标记保护。如果是这种情况，可能适合关闭“传播查看要求”。

使用[数据沿袭](/docs/foundry/security/checking-permissions/#data-lineage)应用程序验证数据集上的权限标记。首先，将项目中的一个或多个数据集添加到图中。然后，选择**权限**节点着色选项。受权限标记保护的资源旁边会在图上显示盾牌图标。选择一个节点，然后在右侧边栏中选择**访问信息**以展开有关该节点上的权限标记的详细信息。

例如，如果您确定启用了“传播查看要求”设置的项目仅包含一个敏感数据类别（PII），并且PII权限标记已应用于项目中每个相关数据集（无论是直接应用还是通过数据依赖关系或文件层次结构继承），那么“传播查看要求”设置可能是多余的，可以安全地[为项目禁用](#4-disable-propagate-view-requirements-on-the-project)。

#### 确定数据敏感性是否在上游或此项目内引入

如果项目包含敏感数据，并且该数据尚未被[权限标记](/docs/foundry/security/markings/)保护，那么我们建议在禁用“传播查看要求”设置之前应用权限标记，以确保下游数据持续受到安全控制的传播保护。

然而，项目不一定是对数据应用权限标记的正确位置。

##### 示例

在下面的示例中，项目中一个启用了“传播查看要求”设置的敏感数据集没有应用权限标记。然而，该敏感数据集实际上是从上游数据集派生的。

![The sensitive data comes from an upstream dataset, as shown in the Data Lineage graph.](../../foundry-docs/platform-security-management/media/pvr-migration-example-data-lineage.png)

**方法1（错误）：** 如果您直接对项目中的敏感数据应用权限标记，上游数据将不会被正确标记；这会影响安全性可读性。

![A Marking was applied directly to the sensitive data in the Project.](../../foundry-docs/platform-security-management/media/pvr-migration-marking-applied-downstream.png)

**方法2（推荐）：** 如果您改为对\_上游\_数据应用权限标记，那么权限标记将自动传播到此项目中的数据；两个数据集都将被正确标记。

![A Marking was applied to the upstream dataset and propagated to the downstream sensitive data.](../../foundry-docs/platform-security-management/media/pvr-migration-marking-applied-upstream.png)

如果您的项目中的任何敏感数据应受权限标记保护，我们建议尽可能在上游保护这些数据，以确保敏感数据在平台中的任何地方都能得到一致保护。请确保采取适当的上游操作，然后再返回您的项目并继续迁移。

#### 适当时重用现有权限标记

如果您的项目是某些敏感数据的起源（最上游位置），并且数据未受到权限标记保护，那么项目可能是对数据应用权限标记作为“传播查看要求”设置替代的正确位置。对于每个敏感数据类别，[验证平台上是否已存在](#verify-if-markings-are-applied-to-sensitive-data)正确表示此数据的权限标记。

从数据治理的角度来看，如果数据是PII，并且平台上已有PII权限标记，我们建议应用现有权限标记，而不是创建第二个PII权限标记；这确保用户授权可以在单个地方进行管理。

记录您计划重用的权限标记的决定，然后[继续迁移](#3-complete-migration)。

#### 创建新的权限标记

如果项目中敏感数据类型没有合适的权限标记，请考虑创建新的权限标记。这只有在以下情况成立时才有必要：

* 项目中的数据是独特的，没有现有的权限标记可以使用。
* 数据源于项目；如果不是，则应将权限标记应用于派生数据的上游数据集。

记录您的决定并按照以下部分中的步骤完成迁移。

### 3. 完成迁移

以下部分描述了在讨论的选项下如何完成迁移。

#### 禁用“传播查看要求”

无需操作。继续[4. 在项目上禁用“传播查看要求”](#4-disable-propagate-view-requirements-on-the-project)。

#### 应用现有权限标记

将项目中某个特定类别的敏感数据集（例如，包含PII的数据集）访问权限的所有用户添加为现有权限标记（PII）的成员。这确保在迁移后不会有人失去对项目的访问权限。注意，一旦用户被添加为现有权限标记的成员，他们可能会看到在整个平台中应用了该权限标记的任何数据。

在应用现有权限标记之前，请查看[应用权限标记](/docs/foundry/platform-security-management/manage-markings/#apply-markings)的步骤。考虑应用权限标记的下游影响，并可能锁定其他下游用户。

准备就绪后，将权限标记应用于需要它的资源集。如果项目中只有一个敏感数据类别且所有数据都属于该类别，则将权限标记应用于项目本身。否则，直接应用权限标记到敏感数据集或它们的父文件夹（如果它们位于同一位置）。

#### 创建新的权限标记

首先，[创建新的权限标记](/docs/foundry/platform-security-management/manage-markings/#create-markings)。然后，将应有权访问其描述的数据的所有用户和/或组添加为此新权限标记的成员。这确保在迁移后不会有人失去访问权限。

在尝试应用任何权限标记之前，请查看[应用权限标记的步骤](/docs/foundry/platform-security-management/manage-markings/#apply-markings)。

### 4. 在项目上禁用“传播查看要求”

在为项目中的多种敏感数据类型[完成迁移](#3-complete-migration)后，确保从项目视图右侧面板的**设置**选项卡中禁用“传播查看要求”设置。

:::callout{theme="warning"}
禁用后，您将无法重新启用“传播查看要求”设置。
:::

![Disable the Propagate view requirements setting for a Project.](../../foundry-docs/platform-security-management/media/disable_pvr.png)

### 5. 确认操作完成

返回升级助手，确认不再有与此项目对应的待处理操作。
