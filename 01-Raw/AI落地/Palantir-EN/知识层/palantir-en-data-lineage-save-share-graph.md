---
title: Palantir 官方文档（英文原版）· Save and share a graph
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/save-share-graph/
evidence: E1
lang: en
domain: AI落地
keywords:
- Palantir
- Foundry
- ontology-construction
- semantic-layer
state:
  phase: raw
  time_raw: '2026-09-23T06:47:11+08:00'
  time_draft: null
  time_wiki: null
related: null
compile: false
compile_note: 原文取证层：知识内容已由中文版汇编为 Draft（3 篇），本层用于引用英文原句，不重复编译
---

> 溯源：Palantir 官方英文原文（E1）。中文版为官方机翻（准确性未验证），本文件为**取证优先的原文**。抓取 2026-09-23T06:47:11+08:00。
> 原始地址：https://palantir.com/docs/foundry/data-lineage/save-share-graph/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-save-share-graph.md`

# Save and share a graph

Data Lineage allows you to easily save your graph and share it with other users. You can find multiple ways to save and share by selecting the **Actions** tab in the upper right of the application and selecting a method from the dropdown menu.

![Save and share actions in Data Lineage](/docs/resources/foundry/data-lineage/data-lineage-save-and-share.png)

## Save a graph

Select the following options in the **Actions** dropdown menu to save your Data Lineage graph:

* **Save:** Save your Data Lineage graph to where it currently lives in your files or Project.
* **Save as...:** Choose a name for your lineage graph and save it to a new location in your file system.

![Save as lineage graph window](/docs/resources/foundry/data-lineage/save-data-lineage-window.png)

You can also open a previously saved graph with the following option:

* **Open graph:** Choose to open a different saved graph to which you have access, or open the **Clipboard** tab to enter the resource identifier (RID) of a dataset, schedule, graph, or path.

![Open new graph Clipboard option](/docs/resources/foundry/data-lineage/open-graph-clipboard.png)

:::callout{theme="neutral"}
Your branch choice is saved with your saved graph. If you load a graph with a different branch configuration than you currently have, you will be asked if you would like to switch branches to the saved branch configuration.
:::

![Switch branches alert to open new graph](/docs/resources/foundry/data-lineage/switch-branches-alert-open-graph.png)

## Share a graph

You can share a graph with other users using the options below:

* **Get quick share link:** Generate a shareable link that provides read-only access to your graph. This option is only available for users belonging to the same Organization. To share a graph across Organizations, ensure the graph is saved in [a shared Project accessible to both Organizations](/docs/foundry/security/cross-organization-collaboration/#create-a-shared-project).
* **Export graph to SVG:** Generate and download a static image of your lineage graph in .svg format.

You can also select **Share** in the upper right of the application to open the sidebar and view **Roles** details. From here, you can turn on link sharing or give a user or group access to your graph.

![View Roles details in Data Lineage sidebar](/docs/resources/foundry/data-lineage/roles-details-data-lineage.png)
