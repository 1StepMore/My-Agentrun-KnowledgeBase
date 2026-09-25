---
title: Palantir 官方文档汇编 · 数据与血缘
source: Palantir 官方文档（一手来源，中文机翻版，逐篇 URL 见 sources_note）
keywords:
- Palantir
- Foundry
- data-pipeline
- semantic-layer
sources:
- AI落地/Palantir/知识层/palantir-zh-data-lineage.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-build-datasets.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-build-timeline.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-check-permissions.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-dataset-preview-logic.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-elements-reference.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-explore-artifacts.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-explore-lineage.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-faq.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-find-column.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-manage-schedules.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-navigation.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-node-coloring.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-overview.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-save-share-graph.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-see-impact-marking-changes.md
- AI落地/Palantir/知识层/palantir-zh-data-lineage-stale-datasets.md
state:
  phase: draft
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23 02:25:43+08:00
  time_wiki: '2026-09-23T10:40:21+08:00'
related:
- '[[企业语义层建模-从数据仓库到数字孪生]]'
- '[[LLM驱动语义层构建的五种方法论]]'
wiki_ref: 03-Wiki/AI落地/_MOC-AI落地.md
---

> **本汇编性质**：Palantir 官方文档原文（17 篇）按主题合并，逐节保留原始 URL。
> 官方标注中文页为 **未经人工验证的机器翻译**；权威表述以英文原版为准（`/docs/foundry/...` 去掉 `zh`）。
> 本汇编**不做改写**，仅去除站点导航与重复声明——可逐节回溯官方原文。
> 汇编时间：2026-09-23T02:25:43+08:00

---

## [data-lineage] data-lineage

> **原文取证**：本汇编据官方**中文机翻**整理；引用原句请用英文原文层 `01-Raw/AI落地/Palantir-EN/知识层/`（126 篇 E1 原文，2026-09-23 抓取）。

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage.md`

# 概述

**数据沿袭**是一个交互式工具，帮助全面查看数据如何在Foundry平台中流动。

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

---

## [data-lineage] 搭建数据集

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/build-datasets/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-build-datasets.md`

# 搭建数据集

您可以使用数据沿袭图查看管道中的哪些数据集已过期，然后使用搭建助手直接从数据沿袭开始搭建。

从数据沿袭触发的搭建始终适用于图中配置的分支（包括回退分支）。

以下是一些常见的搭建工作流程：

* [搭建所有上级](#build-all-ancestors)
* [所选数据集之间的所有变换](#all-transforms-in-between-selected-datasets)
* [仅所选数据集](#selected-datasets)

## 搭建所有上级

此策略搭建选定的数据集和所有上级数据集，以确保选定的数据集完全更新。

默认情况下，这仅搭建过期的上级，但您可以选择强制重新搭建已更新的数据集。强制重新搭建在搭建时间和资源方面可能会很昂贵。

1. 将数据集添加到图中或打开已保存的快照。
2. 选择您要搭建的数据集。
3. 在搭建助手中，选择**所有上级数据集**，然后点击**下一步**。

点击**下一步**尚未触发任何搭建。您将仅看到要搭建的数据集的预览。

4. 如果您想强制重新搭建已更新的数据集，请点击**强制搭建**已更新的数据集。
5. 在检查要搭建的数据集列表后，点击**运行搭建**以触发搭建。

如果您决定不想搭建*所有*过期的上级，您必须在当前搭建预览中点击**取消**，然后更改您选择的节点。您无法从搭建预览屏幕更改选择。

## 所选数据集之间的所有变换

此策略允许您将搭建绑定到管道的一个子集。此策略的一个常见应用案例是在新的原始数据定期进入您的管道时，您希望更新特定数据集以反映新数据，但不想搭建*所有*过期的上级。您可以使用数据沿袭来确定哪些其他数据集需要搭建，以使您感兴趣的数据集更接近最新。

1. 将您最终想要搭建的数据集添加到图中。
2. 将任何原始数据集（或任何上游数据集）添加到图中。
3. 选择所有节点。
4. 在搭建助手中，选择**所选数据集之间的所有变换**策略，然后点击**下一步**。

点击**下一步**尚未触发任何搭建。您将仅看到基于您选择的节点要搭建的数据集的预览。您现在可以准确看到需要搭建哪些内容以更新您感兴趣的数据集。您可能不想搭建*所有*数据集——也许有一个非常大的派生数据集应该每天只搭建一次——所以请在列表底部点击**全部添加到图中**。

## 仅所选数据集

此策略允许您选择要搭建的单个数据集。如果数据集之间存在依赖关系，搭建将按正确的顺序执行，以确保子集在其上级搭建后被搭建。

如果您想更改要搭建的数据集，您必须在当前搭建预览中点击**取消**，更改您选择的节点，然后进入新的预览。您无法从搭建预览屏幕更改搭建选择。

在检查要搭建的最终数据集列表后，点击**运行**搭建以触发搭建。

---

## [data-lineage] 查看搭建时间线

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/build-timeline/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-build-timeline.md`

# 查看搭建时间线

在数据沿袭中使用 **搭建时间线** 工具查看数据集的搭建历史。

在数据沿袭中，点击窗口左下角的 **搭建时间线**。此操作会展开查看面板，显示在您选择的时间段内发生的搭建的甘特图。您可以选择想要在时间线中查看的天数或小时数，范围从一小时到十天。您还可以选择按颜色显示搭建，基于日程安排或任务状态。

要查看特定数据集的搭建时间线，请在图表中选择数据集。使用 **拖动选择模式** 工具或按住 `Ctrl / Command` 键同时点击选择多个数据集。

要查看搭建时间线中任务的详细信息，请点击甘特图中的任务。您将看到关于任务状态、起始时间和结束时间及持续时间的信息。

通过点击任务信息窗口中的链接查看更多关于搭建、任务和日程安排的详细信息。

---

## [data-lineage] 检查资源权限

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/check-permissions/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-check-permissions.md`

# 检查资源权限

您可以使用数据沿袭通过"权限"着色选项检查用户查看数据集或制品的权限。为此，请首先在图中添加节点。您可以使用侧面板上的搜索助手来完成此操作。

然后展开图以查看通向您的资源的沿袭（阅读更多关于[探索沿袭](/docs/foundry/data-lineage/explore-lineage/)的信息）。

完成此操作后，使用**节点颜色选项**下拉菜单选择**权限**配色方案。

从**以...查看**下拉菜单中选择用户的姓名。这样您就可以看到用户对图中每个节点的权限。

您可以按两种权限类型进行着色：

* [数据集中的数据访问](#data-access-in-datasets)
* [资源访问](#resource-access)

### 数据集中的数据访问

使用此选项来排查权限问题。请记住，用户的数据访问受数据沿袭影响（参见[平台安全性](/docs/foundry/security/checking-permissions/)）。通过根据用户对数据的访问权限为节点着色，您可以轻松查看可能限制用户访问数据的上游数据集。

请注意，此选项仅适用于数据集节点。

### 资源访问

这将使您可以看到为选定用户在选定资源上设置的[角色](/docs/foundry/security/projects-and-roles/)（例如编辑者、只读等）。

使用此选项查看用户对您的制品的访问级别。

角色与数据沿袭的对应关系与数据访问不同。例如，用户在轮廓分析中为"编辑者"并不保证他们有权限查看分析所依赖的数据。在与用户共享资源时，确保他们可以访问基础数据。

---

## [data-lineage] 预览和逻辑

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/dataset-preview-logic/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-dataset-preview-logic.md`

# 预览和逻辑

数据沿袭界面允许您查看所选数据集或媒体集的预览，并检查相关代码以理解数据集或媒体集背后的逻辑。

## 预览

要查看数据集或媒体集的预览，请在您的数据沿袭图中选择它，然后在界面左下角选择 **预览** 选项卡。

### 媒体集

当媒体集预览展开时，您可以查看媒体集的内容。[了解更多关于媒体集的信息。](/docs/foundry/data-integration/media-sets/).

PDF预览示例：

音频预览示例：

### 数据集

当数据集预览展开时，您可以滚动浏览所选数据集的前300行。您还可以使用预览窗口右侧的 **搜索列...** 字段搜索特定列。根据数据集中数据的类型，数据集的预览将有所不同。

## 逻辑

选择 **代码** 选项卡以查看所选数据集或媒体集的代码逻辑。在 **代码** 视图中，您可以快速编辑、搜索项目，或在用于推导数据的代码库或其他应用程序中打开代码。

上传和数据输出数据集在数据沿袭中没有可查看的相关代码。

---

## [data-lineage] 图元素参考

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/elements-reference/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-elements-reference.md`

# 图元素参考

## 节点类型

| 节点                                        | 类型 | 描述 |
| --- | --- | --- |
![数据集节点](../../foundry-docs/data-lineage/media/data-lineage-node-dataset.png) | **数据集** | Foundry数据集及其之间的沿袭。数据集节点的颜色取决于[用户选择](/docs/foundry/data-lineage/node-coloring/)。虚线边框表示非结构化数据集。
![Object类型节点](../../foundry-docs/data-lineage/media/data-lineage-node-object-type.png) | **Object类型** | Ontology [Object类型](/docs/foundry/object-link-types/object-types-overview/)。节点的图标和颜色取决于每种Object类型的定义。当点击Object类型名称旁边的“链接”图标时，数据沿袭显示此Object类型与其他Object类型之间的关系。
![工件节点](../../foundry-docs/data-lineage/media/data-lineage-node-artifact.png) | **工件** | 数据沿袭展示不同的Foundry工件，如：[Contour](/docs/foundry/contour/overview/)分析，[报告](/docs/foundry/reports/overview/)等。节点的颜色取决于工件类型，工件类型在节点顶部标示。

## 节点指示器

节点指示器出现在数据集节点的顶部，并提供有关资源的附加信息。

| 指示器 | 类型 | 描述 |
| --- | --- | --- |
![问题图标](../../foundry-docs/data-lineage/media/data-lineage-icon-issues-reported.png)  | **打开的问题** | 此指示器表示图中与节点相关的当前打开的问题。悬停在此信号上会显示打开问题的数量。
![同步图标](../../foundry-docs/data-lineage/media/data-lineage-icon-syncs.png) | **同步** | 带有此指示器的数据集与其他数据库或系统同步。您可以通过选择节点并打开属性面板，或在数据集预览中打开“详细信息”选项卡（右键单击节点并点击**打开**）来查看这些同步。
![回收站图标](../../foundry-docs/data-lineage/media/data-lineage-icon-trashed.png) | **回收站** | 此指示器出现在表示已删除数据集或工件的节点上。删除的节点也会被局部淡化，并且它们的名称被划掉。

---

## [data-lineage] 探索工件和Ontology实体

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/explore-artifacts/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-explore-artifacts.md`

# 探索工件和Ontology实体

您可以在数据沿袭中找到与您的数据集相关的Foundry工件和Ontology实体。数据沿袭界面允许您直接导航到这些资源，并查看它们如何融入您的Ontology。

## 查找相关工件

在您的数据沿袭图中，选择一个数据集。然后，在右侧边栏中选择**相关项**以展开**相关工件**面板。**相关项**图标将显示一个徽章，其中包含与所选数据集相关的工件数量。在工件面板中，您可以看到整个Foundry中相关资源的列表，包括Contour可视化和Slate应用程序。

单击资源旁边的节点图标以放大相关数据集，或单击资源以在新标签中打开相应应用程序。您可以筛选相关工件的列表以包含不同的项目类型，并按最旧、最新、名称、路径或最后修改时间排序列表。

## 查找Ontology实体

通过选择数据集并在右侧边栏中打开**查看节点属性**面板，在您的沿袭图中查找由数据集定义的Object类型。

在**关于**选项卡中，您将看到使用所选数据集创建的任何Object类型。单击Object类型旁边的**设置**图标以在新的Ontology管理器标签中查看其配置。

您还可以使用右侧边栏中的**搜索Foundry**工具将Object类型添加到您的数据沿袭中。使用基本或高级搜索查找Object类型，并从列表中选择它以将其添加到您的图表中。然后，您可以查看与Object类型相关的链接类型，并使用图表可视化您的数据集与新添加的Object类型之间的连接。

[了解有关创建Ontology的更多信息。](/docs/foundry/ontology/overview/)

---

## [data-lineage] 探索数据沿袭

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/explore-lineage/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-explore-lineage.md`

# 探索数据沿袭

数据沿袭帮助您了解数据的来源。在数据沿袭应用中，有多种方式可以探索数据管道。考虑一种常见的路径：

1. 使用**搜索**助手，找到您的资源（例如，数据集或Object类型）并将其添加到图中。

2. 点击节点的左箭头以显示资源的直接父级。

3. 若要扩展您的图形，请在图中选择下一个资源并点击图形工具中的**展开**按钮。

4. 点击折角按钮以定义要显示的层级数。点击双折角以扩展到原始数据（或扩展到最终的后代）。

同时添加过多节点可能会影响图形的性能和可用性。通过检查**展开**工具中的节点计数保持一个可管理的节点数量。

通过选择**展开**按钮并添加资源之间的所有节点或所有共同的祖先/后代，可以在图中找到两个节点之间的关系。

5. 通过选择数据集并使用底部面板显示数据预览，获取有关某个数据集的更多信息。

6. 点击**代码**以查看数据集的创建方式。

7. 点击**在代码工作簿中查看**或**在存储库中查看**以查看原始代码并根据需要进行更改（需符合权限）。

根据资源类型，某些选项可能对某些数据集不可用。例如，**代码**仅适用于代码工作簿或代码存储库。对于没有代码显示的Fusion表同步，您可能有查看源表并在那里进行更改的选项（如果您拥有适当的权限）。

---

## [data-lineage] 数据沿袭问题

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/faq/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-faq.md`

# 数据沿袭问题

以下是一些关于数据沿袭的常见问题。

如需了解一般信息，请查看我们的[数据沿袭文档](/docs/foundry/data-lineage/overview/)。

* [如何查看我的Object类型在数据沿袭中的支持和数据输出数据集？](#how-can-i-see-the-backing-and-writeback-datasets-for-my-object-type-in-data-lineage)
* [我的管道中有哪些数据集也具有特定列？](#what-datasets-in-my-pipeline-also-have-a-specific-column)
* [谁是最后一个修改此管道上资源的人？](#who-was-the-last-person-to-modify-a-resource-on-this-pipeline)
* [如何找到我的哪些数据集有未完成的事务？](#how-can-i-find-which-of-my-datasets-have-open-transactions)
* [管道中大多数数据集存储在哪里？](#where-are-most-of-the-datasets-used-in-the-pipeline-stored)
* [如何分享我未保存的数据沿袭图？](#how-can-i-share-my-unsaved-data-lineage-graph)
* [为什么我的数据集不是最新的？](#why-is-my-dataset-is-not-up-to-date)

***

## 如何查看我的Object类型在数据沿袭中的支持和数据输出数据集？

* 首先，通过在右侧面板（带有放大镜图标的标签）中搜索，将您的Object添加到数据沿袭图中。选择**Object类型**以筛选您的搜索，然后输入您想查看支持和数据输出数据集的Object名称。

* 接下来，选择您的Object类型左侧的箭头以显示其上级。如果您的Object类型是只读的，这将产生一个上级节点；如果您的Object类型启用了数据输出，则将产生两个上级节点。确保在**节点颜色选项**下拉菜单中选择了**资源类型**，以便根据右上角的图例查看您的数据输出数据集颜色。支持架构数据集的颜色取决于所使用的变换类型。

* 您的Object类型的支持和数据输出数据集在右上角也会有一个小地球图标。

[返回顶部](#data-lineage-questions)

***

## 我的管道中有哪些数据集也具有特定列？

1. 首先，确保您管道中所有所需的数据集已添加到数据沿袭图中。
2. 接下来，使用画布左上角工具切换中的**选择**模式选择所需的数据集。
3. 然后，从右侧面板打开**选择属性直方图**。在名为**常见列**的部分下，您将看到在您的选择中按列名称的最常见列。

选择其中一列将突出显示在您的选择中包含此列的数据集。

[返回顶部](#data-lineage-questions)

***

## 谁是最后一个修改此管道上资源的人？

* 首先，确保您管道中所有感兴趣的数据集已添加到数据沿袭图中。
* 接下来，使用屏幕左上角工具切换中的选择模式选择数据集。然后，从右侧面板打开**选择属性直方图**。
* 在**最后修改**部分下，您将看到最后修改您选择的数据集的用户。选择用户名将突出显示该用户在图中最后修改的数据集。

[返回顶部](#data-lineage-questions)

***

## 如何找到我的哪些数据集有未完成的事务？

在右上角的下拉菜单中，选择**搭建状态**。现在，您应该能够看到是否有任何数据集当前正在运行。任何这样的数据集都有一个未完成的事务。

[返回顶部](#data-lineage-questions)

***

## 管道中大多数数据集存储在哪里？

* 首先，确保您管道中所有感兴趣的数据集已添加到数据沿袭图中。
* 接下来，使用屏幕左上角工具切换中的**选择**模式选择所有感兴趣的数据集。然后，从右侧面板打开**选择属性直方图**。
* 在名为**常见文件夹路径**的部分下，您将看到您选择中资源的最常见文件夹路径。

选择一条黄金路径将突出显示图中此路径上的资源。悬停在文件夹路径上将显示完整路径。

您可以在**选择属性直方图**面板中选择多个属性，这样图将突出显示满足您选择的所有资源。

[返回顶部](#data-lineage-questions)

***

## 如何分享我未保存的数据沿袭图？

要分享您未保存的数据沿袭图，请选择保存附近右上角的箭头。到那里后，您可以看到一个快速分享链接。

[返回顶部](#data-lineage-questions)

***

## 为什么我的数据集不是最新的？

您的数据集可能不是最新的有几个原因。

请考虑以下原因可能导致您的数据集不是最新的：

* 您的数据集搭建是否失败？
* 是否有上游数据集尚未搭建且不是最新的？
* 您是否从源接收到最新的数据？

您可以在数据沿袭中轻松回答这些问题：

1. 首先，通过在数据沿袭中打开感兴趣的数据集并右键单击节点来验证管道中每个资源的状态。

2. 然后，选择**展开节点...**。您可以通过选择\*\*展开父节点...\*\*上方的双左箭头查看该数据集的所有上级节点。

3. 接下来，在右上角的**节点颜色选项**下拉菜单中选择**搭建状态**选项，以查看管道中每个资源的搭建状态。此视图将使您更容易诊断过时的数据集。

[返回顶部](#data-lineage-questions)

---

## [data-lineage] 查找具有指定列的数据集

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/find-column/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-find-column.md`

# 查找具有指定列的数据集

您可以在您的数据沿袭图中轻松搜索特定数据集列：

* 首先，确保您已将管道中所有感兴趣的数据集添加到您的沿袭图中。

* 接下来，使用应用程序左上角工具切换中的**拖拽选择模式**选择所有感兴趣的数据集。您也可以按住 `Ctrl / Command` 一次选择多个节点，或使用 `Ctrl / Command + A` 选择所有节点。

* 然后，从数据沿袭侧边栏中选择**查看选择属性的直方图**。

* 在**常见列**部分，您可以看到选择中按名称排列的最常见列。

* 点击其中一个列以突出显示选择中包含该列的数据集。

---

## [data-lineage] 管理计划

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/manage-schedules/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-manage-schedules.md`

# 管理计划

数据沿袭允许您轻松管理沿袭图中的搭建计划。在右侧边栏中，选择**管理计划**以打开计划详情窗格。

您将看到与图中选定数据集相关的计划。点击某个计划以查看更多详情：

* **最新运行：** 计划最新一次运行的状态。
* **最后更新：** 最后一次更新的时间戳以及进行更改的用户
* **目标数据集：** 搭建计划中包含的下游数据集列表。
* **搭建时机：** 显示创建搭建计划时确定的搭建计划触发器。例如，可以将搭建计划设置为在**特定数据集更新时**运行。
* **搭建范围：** 定义搭建中包含的项目或用户数据集及运行搭建所使用的权限。

在[**搭建管道**](/docs/foundry/building-pipelines/scheduling-overview/)文档中了解更多关于计划搭建的信息。

---

## [data-lineage] 导航

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/navigation/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-navigation.md`

# 导航

为了充分利用数据沿袭应用程序，您需要了解如何导航图表、使用工具以及配置分支和图表属性。以下编号部分对应于下方截图上的编号：

1. [沿袭图表](#lineage-graph)
2. [分支设置](#branch-settings)
3. [侧边面板](#side-panel)
   * [搜索和浏览](#search-and-browse)
   * [属性和直方图](#properties-and-histogram)
   * [管理搭建](#manage-builds)
   * [管理计划](#manage-schedules)
   * [相关工件](#related-artifacts)
4. [节点详情面板](#node-details)
5. [图表工具](#graph-tools)
6. [保存图表](#save-graph)

## 沿袭图表

图表是您的工作区，用于在探索数据管道时安排和操作节点。

在图表中添加节点后，可以通过单击节点两侧的箭头或使用[图表工具](#graph-tools)中的**展开**选项来添加相关资源。

默认情况下，节点按自动设计排列，但您可以通过单击并拖动手动重新排列节点。要重新启用自动设计，请在[图表工具](#graph-tools)中选择**设计所有节点**选项。

在默认的**平移模式**下，点击并拖动以在图表中移动。要使用光标选择多个节点，请在[图表工具](#graph-tools)中切换到**拖动选择**模式或按住`Shift`键同时点击并拖动。您可以通过点击选择一个节点，或者通过`Ctrl/Cmd` + 点击选择多个节点。

## 分支设置

从列表中选择一个分支以探索该分支中的数据管道。图表和其他辅助工具将基于所选分支显示信息。如果某个资源不存在该分支，将使用列出的回退分支（按列表中的顺序）。

要了解有关分支的更多信息，请参阅[分支文档](/docs/foundry/data-integration/branching/)。

## 侧边面板

### 搜索和浏览

使用搜索助手找到 Foundry 资源并将其添加到图表中。使用自由文本搜索或浏览树以查找资源。通过点击资源添加它，或者使用视图底部的按钮添加所有搜索结果（包括或排除子文件夹的内容）。使用**高级**选项卡为搜索添加筛选并排序结果。

在查看包含子文件夹的文件夹时，可以递归地将所有子文件夹中的\_所有\_表格添加到图表中。一次添加过多节点可能会影响图表的性能。

### 属性和直方图

当您在图表中选择一个节点时，属性助手会显示资源的详细信息。根据您选择的资源类型，属性助手会在**操作**菜单下显示可用的 Foundry 应用程序以及其他链接和操作（报告问题、添加描述等）。

当您在图表中选择多个节点时，您将看到直方图助手。助手显示常见属性及其值，以及每个值在图表中出现的次数。点击值时，会突出显示匹配的节点。如果您想深入查看这些资源，请点击**更新选择**。

<img src="../../foundry-docs/data-lineage/media/data-lineage-histogram.png" alt="查看直方图" width="400" />

使用直方图中的**复制名称**按钮复制所有当前选定资源的名称。全名（包括路径）会以逗号分隔的列表形式复制到剪贴板。

### 管理搭建

搭建助手为您提供三种搭建策略：

* 仅搭建选定的数据集
* 搭建选定数据集之间的所有数据集
* 搭建选定的数据集及其所有祖先

[了解更多关于管理搭建的信息。](/docs/foundry/data-lineage/build-datasets/)

### 管理计划

计划助手允许您设置和编辑图表中选定资源的搭建计划。
[了解更多关于搭建计划的信息。](/docs/foundry/building-pipelines/scheduling-overview/)

在数据沿袭中查看和创建计划时，这些计划适用于图表中配置的分支（包括回退分支）。

### 相关工件

相关工件助手显示与图表中选定节点直接链接的工件。已删除和自动保存的文件将从列表中排除，除非另有选择。您还可以通过将鼠标悬停在图表中每个节点的右箭头上来访问相同的相关工件列表。

## 节点详情

点击一个节点以查看更多详情：

* **预览：** 选定数据集中的数据样本。
* **历史：** 数据集更改历史概览。概览包括日志、文件、元数据、架构和任务规范的选项卡。
* **代码：** 如果使用代码生成数据集，这里会显示
* **数据健康：** 选定数据集上设置的所有[健康检查](/docs/foundry/data-health/overview/)。
* **搭建时间线：** 选定数据集实际搭建时间的甘特图。

## 图表工具

图表工具提供了一组图表探索、导航和自定义功能：

* [节点着色](#node-coloring)
* [设计](#layout)
* [展开](#expand)
* [查找](#find)
* [选择](#selection)

### 节点着色

您可以按多个属性和指标为沿袭图中的节点着色。节点着色通常用于传达沿袭结构、排除故障、监控管道健康状况和管理搭建。您还可以创建自己的自定义着色，并根据分配的颜色排列图表。

[阅读更多关于节点着色选项的信息。](/docs/foundry/data-lineage/node-coloring/)

您可以在图表中按颜色组排列节点，位于**设计**下。

### 设计

设计按钮为图表中的节点提供各种排列选项。
**设计所有节点**为图表中的所有节点应用自动设计。当您在图表中选择多个节点时，您可以应用其他设计（垂直、层次结构、按级别等）。

您可以在沿袭图中使用各种有用的键盘快捷键。在应用程序右上角的**键盘快捷键**按钮下查看完整列表。

### 展开

使用**展开**工具揭示图表中节点的祖先和后代。[了解更多关于探索数据沿袭的信息。](/docs/foundry/data-lineage/explore-lineage/)

### 查找

使用**查找**在图表中搜索节点。您可以搜索节点名称或数据集中的列名称。

### 选择

**选择**工具允许您轻松选择图表中的节点：

* **全选：** 选择图表中当前所有节点。
* **反选：** 取消选择当前选定的所有节点，并选择图表中的其他节点。
* **选择子节点：** 将当前选定节点的所有直接子节点添加到您的选择中
* **选择父节点：** 将当前选定节点的所有直接父节点添加到您的选择中。

## 保存图表

您可以通过以下方式保存和分享您的沿袭图表给其他 Foundry 用户：

* **保存/打开：** 保存您的数据沿袭图表，并通过点击**打开图表**重新打开它。
* **获取快速分享链接：** 生成一个可共享的链接，提供对图表的只读访问。
* **以SVG格式导出图表：** 生成沿袭图表的静态图像。

您的分支选择将与您保存的图表一起保存。如果您加载的图表与当前配置的分支不同，系统会询问您是否要切换到保存的分支配置。

---

## [data-lineage] 节点着色

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/node-coloring/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-node-coloring.md`

# 节点着色

有几种内置选项可以为图形节点着色，以便为您提供有关管道的更多信息：

| 着色选项 | 描述 |
|--- |--- |
| **无颜色** | 将完全移除颜色 |
| **自定义颜色** | 允许您通过点击**颜色**按钮选择节点并为其指派颜色 |
| **数据目录** | 节点将根据其所在的数据目录集合进行着色。如果节点属于多个集合，则会被着色为“属于多个集合” |
| **文件夹** | 按资源所在文件夹的名称为节点着色 |
| **问题** | 按指派给它们的Foundry问题数量为节点着色。此选项还允许您通过问题标签进行筛选。 |
| **权限** | 按用户对数据或资源的访问级别为节点着色。如果您有权访问图中的资源，此视图还允许您选择任何Foundry用户并查看其权限。 |
| **项目** | 根据它们所在的Foundry项目为节点着色。 |
| **存储库** | 根据创建它们的代码存储库为节点着色。您可以按存储库名称或其类型（例如代码存储库、代码工作簿）为节点着色。 |
| **资源类型** | 此视图按资源类型为节点着色。资源类型主要指资源的创建方式（例如，Contour、代码工作簿、Fusion电子表格同步、上传等）。 |
| **构建状态** | 指示图中每个数据集的当前构建状态。如果节点被分组，将显示更严重的状态。 |
| **数据健康** | 指示资源健康检查的状态，并能够筛选仅监控的健康检查。如果节点被分组，组的颜色将指示该组最严重的健康检查状态。 |
| **过时** | 此选项将指示数据或逻辑是否相对于数据集祖先过时。 <br> **与父级过时** 意味着资源的直接父级已更新，而资源本身尚未相应更新。<br>**与祖先过时** 意味着资源与其直接父级是最新的，但上游有一个资源更为更新。此选项允许您筛选两种类型的更新：数据和逻辑。<br>**数据过时** 意味着数据在祖先中更新，而资源尚未在构建中获取更新。<br> **逻辑过时** 意味着任务规格更改了。 |
| **计划计数** | 指示设置在数据集上的构建计划数量，并可选择筛选出暂停的计划。 |
| **同步状态** | 如果数据集上设置了同步，此选项将指示同步的状态 |
| **上次构建时间** | 指示自上次成功构建数据集以来的时间。 |
| **构建持续时间** | 根据每个资源最近一次成功构建，指示近似的构建持续时间 |
| **文件** | 根据文件相关指标为图中的节点着色：平均文件大小、文件数量和数据集大小 |
| **行数** | 按每个数据集的行数为节点着色。如果行数不存在，可以在数据集详细信息助手或Foundry中的数据集视图（数据集应用程序）中计算。 |
| **Spark使用情况** | 按给定时间段内的执行器运行/CPU时间为每个节点着色 |
| **用户查看次数** | 按用户查看次数为节点着色 |
| **分支** | 指示图中每个节点的当前查看分支。 |
| **代码状态** | 指示此节点/数据集的代码状态。<br>**CI运行中** 意味着CI检查目前正在此节点上运行。<br>**CI失败** 意味着CI检查在此节点上出错。<br>**过时** 意味着节点的代码已过时。<br>**不可用** 意味着节点/数据集不是stemma后端或用户缺少权限。 |
| **存储** | 指示数据存储位置。将为**Foundry**，除非您使用[虚拟表](/docs/foundry/data-integration/virtual-tables/)。 |
| **计算\[实验性]** | 指示变换是否使用外部计算运行。对于所有客户，直到进一步推出，将为**Foundry**。 |
| **事务类型** | 指示每个节点的事务类型：追加或快照 |

---

## [data-lineage] overview

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-overview.md`

# 概述

**数据沿袭**是一个交互式工具，帮助全面查看数据如何在Foundry平台中流动。

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

---

## [data-lineage] 保存和分享图表

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/save-share-graph/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-save-share-graph.md`

# 保存和分享图表

数据沿袭允许您轻松保存和分享您的图表给其他用户。您可以通过点击应用程序右上角的**操作**选项卡，并从下拉菜单中选择一种方法，找到多种保存和分享的方式。

* \*\*保存：\*\*将您的数据沿袭图表保存到当前文件或项目所在的位置。
* \*\*另存为...：\*\*为您的沿袭图表选择一个名称，并将其保存到文件系统的新位置。

* **打开图表：**选择打开您有权限访问的不同已保存图表，或打开**剪贴板**选项卡以输入数据集、计划、图表或路径的资源标识符（RID）。

您的分支选择会与您保存的图表一起保存。如果您加载的图表与您当前的分支配置不同，系统将询问您是否要切换到保存的分支配置。

* \*\*获取快速分享链接：\*\*生成一个可分享的链接，提供对您的图表的只读访问。
* \*\*以SVG格式导出图表：\*\*生成并下载您的沿袭图表的静态图像，以.svg格式保存。

您还可以点击应用程序右上角的**分享**按钮以打开侧边栏并查看**角色**详细信息。在这里，您可以打开链接分享或给予某个用户或群组访问您图表的权限。

---

## [data-lineage] 查看权限标记更改的影响

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/see-impact-marking-changes/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-see-impact-marking-changes.md`

# 查看权限标记更改的影响

您可以使用数据沿袭来评估对数据集权限标记的更改如何影响派生数据集。这在[移除权限标记](/docs/foundry/building-pipelines/remove-markings/)时非常有用。

权限标记模拟依赖于最近的数据集搭建，并且不考虑尚未最终确定的更改。请确认您正在使用的是最新版本的数据。

## 访问模拟模式

1. 打开**访问信息**侧边栏。
2. 开启**模拟访问要求**。
3. 在图表上选择任何数据集。
4. 点击**编辑权限标记**。

## 模拟权限标记更改

要模拟权限标记的应用，请搜索您要应用的权限标记，勾选权限标记旁边的框，然后选择**模拟更改**按钮。

已经应用于数据集的权限标记将显示为已选中。要模拟移除权限标记，请取消选中权限标记旁边的框并点击**模拟更改**。

您只能移除直接应用于数据集的权限标记。无法模拟通过数据集沿袭或从父项目继承的权限标记的移除。

## 分析模拟图表

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

---

## [data-lineage] 了解过时的数据集

- 官方原文：https://palantir.com/docs/zh/foundry/data-lineage/stale-datasets/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-data-lineage-stale-datasets.md`

# 了解过时的数据集

您的数据集可能未更新的原因有几个。常见的场景包括：

* 我的数据集搭建是否失败？
* 是否有上游数据集未搭建且未更新？
* 我们是否从源接收到最新数据？

您可以通过使用数据沿袭轻松解答这些问题。

* 首先，通过在数据沿袭中打开感兴趣的数据集并右键单击节点，验证管道中每个资源的状态。

* 然后，选择**展开节点**。您可以通过点击**展开父节点**上方的双左箭头来查看该数据集的所有祖先节点。

* 接下来，在数据沿袭右上角的**节点颜色选项**下拉菜单中选择**搭建状态**选项，以查看管道中每个资源的搭建状态。此视图将使诊断过时的数据集变得更加容易。

## 英文原文对照索引

> 中文版是官方**机翻**（准确性未验证）；引用原句请用英文原文层。本节列全 17 篇的来源与原文路径对照。

| 中文来源文件 | 英文原文 |
|:---|:---|
| `palantir-zh-data-lineage.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage.md` |
| `palantir-zh-data-lineage-build-datasets.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-build-datasets.md` |
| `palantir-zh-data-lineage-build-timeline.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-build-timeline.md` |
| `palantir-zh-data-lineage-check-permissions.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-check-permissions.md` |
| `palantir-zh-data-lineage-dataset-preview-logic.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-dataset-preview-logic.md` |
| `palantir-zh-data-lineage-elements-reference.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-elements-reference.md` |
| `palantir-zh-data-lineage-explore-artifacts.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-explore-artifacts.md` |
| `palantir-zh-data-lineage-explore-lineage.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-explore-lineage.md` |
| `palantir-zh-data-lineage-faq.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-faq.md` |
| `palantir-zh-data-lineage-find-column.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-find-column.md` |
| `palantir-zh-data-lineage-manage-schedules.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-manage-schedules.md` |
| `palantir-zh-data-lineage-navigation.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-navigation.md` |
| `palantir-zh-data-lineage-node-coloring.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-node-coloring.md` |
| `palantir-zh-data-lineage-overview.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-overview.md` |
| `palantir-zh-data-lineage-save-share-graph.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-save-share-graph.md` |
| `palantir-zh-data-lineage-see-impact-marking-changes.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-see-impact-marking-changes.md` |
| `palantir-zh-data-lineage-stale-datasets.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-data-lineage-stale-datasets.md` |
