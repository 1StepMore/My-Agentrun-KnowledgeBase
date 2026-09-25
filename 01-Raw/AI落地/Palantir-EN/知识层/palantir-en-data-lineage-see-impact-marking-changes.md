---
title: Palantir 官方文档（英文原版）· See the impact of Marking changes
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/see-impact-marking-changes/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/see-impact-marking-changes/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-see-impact-marking-changes.md`

# See the impact of Marking changes

You can use Data Lineage to evaluate how changes to dataset Markings can impact derived datasets. This can be useful when [removing Markings](/docs/foundry/building-pipelines/remove-markings/).

:::callout{theme="warning" title="Simulation does not account for unfinalized changes"}
Marking simulation relies on the most recent dataset builds and does not account for changes that are not yet finalized. Confirm that you are working with the most up-to-date version of your data.
:::

## Access simulation mode

1. Open the **Access information** side panel.
2. Toggle on **Simulate access requirements**.
3. Select any dataset on the graph.
4. Click **Edit markings**.

![Access information side panel](/docs/resources/foundry/data-lineage/marking-simulation-helper-sidebar.png)

## Simulate Marking changes

![Simulate marking changes](/docs/resources/foundry/data-lineage/marking-simulation-apply.png)

To simulate Marking application, search for the Marking you want to apply, check the box next to the Marking, and then select the **Simulate changes** button.

Markings that are already applied on a dataset will appear as selected. To simulate Marking removal, uncheck the box next to the Marking and click **Simulate changes**.

:::callout{theme="neutral"}
You can only remove Markings that were applied directly on the dataset. Removal of Markings that were inherited through a dataset's lineage or from the parent Project cannot be simulated.
:::

## Analyze the simulated graph

![Analyze the simulated graph](/docs/resources/foundry/data-lineage/marking-simulation-analyze.png)

When in simulation mode, the graph coloring will indicate the datasets affected by the Marking changes. The graph colors are labeled in the interface and can represent the following dataset statuses:

* **Simulate changes applied** appears on the datasets to which you applied changes.
* **Access affected** appears on datasets for which the Markings before and after the change will be different.
* **Access unaffected** appears on datasets for which the Markings before and after the change will remain the same.
* **No visible transactions** appears on datasets that have not been built yet, or where you do not have permission to see transactions.

By selecting any of the datasets, the **Access information** side panel will show the simulated access requirements. You can toggle simulation mode on and off to view differences without losing any of the simulation changes.

## Tips for understanding changes

Before making changes, we suggest consulting the [Markings documentation](/docs/foundry/security/markings/) to learn more about the impact of Markings on users.

When simulating Markings, consider the following:

* Datasets can [stop propagating Markings *via code*](/docs/foundry/building-pipelines/remove-inherited-markings/). <br><img src="./media/marking-simulation-stop-propagating.png" alt="Permissions coloring showing stop propagating Markings" width="400" />
  * In the **Permissions** coloring, nodes on the Data Lineage graph that stop propagating Markings show that data access was *modified via code*. This message will also appear in the **Access information** section of the node properties side panel.
  * In the Code Helper, you can check the code for a dataset to see if it stops propagating Markings by using the term `stop_propagating`.
* Datasets can have Markings propagated to them from *other inputs*; expand the dataset inputs by clicking on the left arrow in the dataset node.
* Markings can be applied on the *parent Project or folder*; Markings will have a folder icon on their left when simulation mode is not enabled, and will show a folder icon in the Marking simulation menu when simulation mode is enabled.
