---
title: Palantir 官方文档 · 入门 · 快速搜索
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/getting-started/quicksearch/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:23:28+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# 快速搜索

快速搜索是Palantir平台中一个用于快速、轻松搜索、导航和发现的工具。可以从左侧边栏的**搜索**图标访问快速搜索，或使用`Cmd+J`（macOS）或`Ctrl+J`（Windows）。快速搜索有两种视图模式：

1. **跳转模式：** 提供个性化的简短结果列表，以便用户直接导航到主要类型的可用内容：平台应用程序、自定义应用程序、对象、数据集和其他资源。
2. **完整结果视图：** 旨在帮助用户查找内容和发现平台中存在的内容。用户可以使用高级筛选器搜索Palantir应用程序、对象、数据集和其他文件，并找到最相关的结果以及丰富的元数据。

## 跳转模式

* **易于访问：** 要打开快速搜索，在导航侧栏中选择**搜索...**，或使用快捷键`Cmd+J`（macOS）或`Ctrl+J`（Windows）。
* **以导航为中心：** 初始对话框和下拉菜单以导航为导向。开始输入以接收建议。使用键盘跳转到平台中的任何页面。
* **仅搜索标题：** 跳转模式仅在应用程序、资源和对象的标题中搜索。要搜索其他字段和元数据，请使用完整结果模式。
* **单击即可获得完整结果：** 从对话框和下拉菜单中，按`Enter/Return`或通过**应用程序**、**对象**、**数据集**或**文件**筛选以进入高级搜索模式。
* **个性化结果：** 快速搜索中的结果根据您最近访问或收藏的资源进行个性化。

![快速搜索最近搜索](/docs/resources/foundry/getting-started/quicksearch-recents.png)

![快速搜索下拉菜单](/docs/resources/foundry/getting-started/quicksearch-dropdown.png)

## 完整结果视图

* **以发现为中心：** 设计用于搜索和发现，用户可以比较多个搜索结果以找到对他们最有用的资源。
* **搜索多个字段：** 搜索描述、列名、文件路径等。此外，可按创建者、标签、项目、文件夹等进行筛选。
* **标签：** 界面包括一个顶级结果标签和四个可筛选的标签：**应用程序**、**对象**、**数据集**或**文件**。
* **元数据：** 用户可以查看每个结果的信息，以评估该资源是否与他们相关。按关键字高亮搜索、文件路径、查看次数、最后更新时间、关键安全元数据等。
* **排序：** 结果基于一个包含文本匹配和其他提升参数的算法进行排序。
* **筛选器：** 提供筛选器用于高级搜索。此外，通过从初始搜索下拉菜单中选择筛选标签，用户可以执行复杂的筛选搜索（例如，“我创建的项目X下的所有报告”）。
* **权限：** 快速搜索遵循平台中的所有现有权限。具有`发现`权限的内容将打开一个`请求访问`消息。用户将看不到他们无权访问的内容。

![快速搜索顶级标签](/docs/resources/foundry/getting-started/quicksearch-top-tab.png)

![快速搜索结果](/docs/resources/foundry/getting-started/quicksearch-results.png)

:::callout{theme="warning"}
快速搜索**不会**在平台中的所有对象实例中进行搜索。快速搜索仅限于搜索250个对象类型的实例，优先级为`活动`对象类型的`重要`，然后是`正常`，然后是`实验`状态（不搜索已弃用和隐藏的对象类型）。如果用户找不到他们正在寻找的内容，他们会被提示尝试在[Object Explorer](/docs/foundry/object-explorer/search-objects/)中搜索，在那里他们可以将搜索调整为仅特定组的对象类型，甚至是特定的对象类型。
:::

### 筛选器

您可以通过快速搜索中的筛选器快速找到平台中所需的资源和数据。通过选择**应用程序**、**对象**、**数据集**或**文件**结果类型来筛选您的搜索结果。您甚至可以通过在文件路径、标签或项目中搜索来进一步筛选。一旦应用筛选器，搜索结果视图将仅显示您选择的结果类型。

例如，我们想要搜索在我们的注册中关于“汽车”的资源。

#### 应用程序

要搜索通过Palantir应用程序搭建接口制作的模块、工作区或其他应用程序，您可以按**应用程序**进行筛选。

在我们的“汽车”搜索示例中，我们可以看到三个Workshop模块、一个Carbon工作区和一个Slate文档，这些都被正确识别为在Palantir中构建的应用程序。

![按应用程序筛选的“汽车”搜索结果。](/docs/resources/foundry/getting-started/quicksearch-apps.png)

#### 对象

要仅查看基于Ontology对象类型的结果，请按**对象**进行筛选。在此搜索结果视图中，您可以从与搜索词匹配的对象类型中进行选择，选择编辑或查看对象类型的谱系，并进一步深入到单个对象。

当搜索“汽车”时，我们看到几个对象类型和对象结果，并且可以进一步筛选到选定的对象类型，如`Award`或`Auto Parts`。

![按对象筛选的“汽车”搜索结果。](/docs/resources/foundry/getting-started/quicksearch-objects.png)

#### 数据集

当按**数据集**筛选时，结果视图将显示平台中与数据集名称或列名称中的搜索词匹配的可用数据集列表。

使用相同的“汽车”示例，我们可以看到包含匹配术语的数据集和列名称的38个数据集列表。

![按数据集筛选的“汽车”搜索结果。](/docs/resources/foundry/getting-started/quicksearch-datasets.png)

#### 文件

在快速搜索中使用**文件**标签快速找到添加到或在平台中创建的单个资源文件。使用左侧面板中的筛选器专门搜索某些文件或资源类型。

当我们搜索“汽车”时，我们收到几种不同的文件结果，包括文件夹、图表、图像和Modeling Objective。

![按文件筛选的“汽车”搜索结果。](/docs/resources/foundry/getting-started/quicksearch-files.png)

## 高级搜索

高级搜索提供了一种超出快速搜索范围的更全面的搜索体验。当您不知道所需资源的名称或元数据时，这可能很有用。通过选择快速搜索右上角的“展开”图标进入高级搜索。

![进入高级搜索](/docs/resources/foundry/getting-started/advanced-search-button.png)

与快速搜索类似，高级搜索提供了一个**顶级**结果标签和其他按类别筛选结果的标签：**应用程序**、**数据集**和**文件**。要查询特定对象，您可以通过选择右上角的**Object explorer**从高级搜索导航到Object Explorer。

完整的高级搜索查询被捕获在一个有状态的URL中。您可以通过从浏览器中复制URL并发送给同事来分享感兴趣的查询。结果可能因用户之间的[资源访问控制](/docs/foundry/security/securing-a-data-foundation/)而异。

![高级搜索](/docs/resources/foundry/getting-started/advanced-search.png)

### AIP驱动的推荐 \[测试版]

:::callout{theme="warning"}
AIP驱动的搜索推荐是一个[实验](/docs/foundry/platform-overview/development-life-cycle/#experimental)功能，并非在所有地方都可用。对于早期采用请求，请联系您的Palantir代表。
:::

除了顶级结果外，高级搜索还提供AIP驱动的推荐，可以解析完整句子、语义查询并推荐下一步。这些建议会在**顶级**标签中以紫色框加载。

![高级搜索](/docs/resources/foundry/getting-started/aip-search.png)
