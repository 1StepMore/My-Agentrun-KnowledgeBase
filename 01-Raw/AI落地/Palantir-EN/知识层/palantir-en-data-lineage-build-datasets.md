---
title: Palantir 官方文档（英文原版）· Build datasets
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/build-datasets/
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
  time_raw: '2026-09-23T06:46:51+08:00'
  time_draft: null
  time_wiki: null
related: null
compile: false
compile_note: 原文取证层：知识内容已由中文版汇编为 Draft（3 篇），本层用于引用英文原句，不重复编译
---

> 溯源：Palantir 官方英文原文（E1）。中文版为官方机翻（准确性未验证），本文件为**取证优先的原文**。抓取 2026-09-23T06:46:51+08:00。
> 原始地址：https://palantir.com/docs/foundry/data-lineage/build-datasets/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-build-datasets.md`

# Build datasets

You can use the Data Lineage graph to see which datasets in your pipeline are out of date, and then use the Builds helper to start builds directly from Data Lineage.

:::callout{theme="neutral"}
Builds triggered from Data Lineage always apply to the branches (including fallback branches) configured in the graph.
:::

The following are a few common build workflows:

* [Build all ancestors](#build-all-ancestors)
* [All transforms in between selected datasets](#all-transforms-in-between-selected-datasets)
* [Selected dataset(s) only](#selected-datasets)

## Build All Ancestors

This strategy builds the selected datasets and all ancestor datasets, to ensure that the selected datasets become completely up to date.

:::callout{theme="neutral"}
By default, this builds only ancestors that are out of date, but you can choose to force a re-build of up-to-date datasets. Forcing a re-build can be expensive in terms of build time and resources.
:::

1. Add datasets to the graph or open a saved snapshot.
2. Select the dataset that you want to build.
3. In the Builds helper, choose **All ancestor datasets**, then click **Next**.

:::callout{theme="neutral"}
Clicking **Next** will *not* trigger any builds yet. You will simply see a preview of the datasets to be built. To change which datasets are included, click **Cancel** on the build preview and change the nodes you have selected; you cannot change your selection from the build preview screen.
:::

![build helper](/docs/resources/foundry/data-lineage/data-lineage-build-helper.png)

4. If you want to force a re-build of up-to date datasets, click **Force build** on up-to-date datasets.
5. After examining the list of datasets to be built, click **Run build** to trigger the builds.

![build-all-ancestors](/docs/resources/foundry/data-lineage/data-lineage-build-all-ancestors.png)

## All transforms in between selected datasets

This strategy lets you bind your builds to a subset of your pipeline. A common use case for this strategy can occur when new raw data regularly lands in your pipeline and there is a particular dataset that you want to update to reflect the new data, but you do not want to build *all* out-of-date ancestors. You can then use Data Lineage to determine which other datasets need to be built to bring your dataset of interest more up to date.

1. Add the dataset you ultimately want to build to the graph.
2. Add any raw datasets to the graph (or any upstream dataset)
3. Select all nodes.
4. In the Builds helper, choose the **All transforms in between selected dataset(s)** strategy, then click **Next**.

:::callout{theme="neutral"}
Clicking **Next** will *not* trigger any builds yet. You will simply see a preview of the datasets to be built based on the nodes you have selected. You can now see exactly what needs to be built to update your dataset of interest. You may not want to build *all* datasets – maybe there is a very large derived dataset that should only build once a day – so click **Add all to graph** at the bottom of the list.
:::

## Selected Datasets

This strategy allows you to pick individual datasets that you want to build. If there are dependencies between the datasets, builds would be executed in the right order to assure descendants are built after their ancestors were built.

After examining the final list of datasets to be built, click **Run** build to trigger the builds.

If you want to change the datasets you are building, you must click **Cancel** on the current build preview, change the nodes you have selected, then enter a new preview. You cannot change your build selection from the build preview screen.
