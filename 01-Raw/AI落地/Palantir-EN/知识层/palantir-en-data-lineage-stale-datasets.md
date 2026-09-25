---
title: Palantir 官方文档（英文原版）· Understand out-of-date datasets
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/stale-datasets/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/stale-datasets/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-stale-datasets.md`

# Understand out-of-date datasets

There are a few reasons why your dataset may not be up to date. Common scenarios to explore are:

* Is my dataset build failing?
* Is there an upstream dataset that has not built and is not up to date?
* Have we received up-to-date data from the source?

You can easily answer these questions by using Data Lineage.

* First, verify the status of each of the resources in your pipeline by opening up the dataset of interest in Data Lineage and right-clicking on the node.

![Expand selected node](/docs/resources/foundry/data-lineage/expand-node-data-lineage.png)

* Then, select **Expand node**. You can see all of the ancestor nodes for that dataset by clicking the double left arrow above **Expand parents**.

![Expand parents after expanding node](/docs/resources/foundry/data-lineage/parent-node.png)

* Next, select the **Build status** option in the **Node color options** dropdown in the top right of Data Lineage to see the build status of every resource in your pipeline. This view of your pipeline will make it much easier to diagnose stale datasets.

![Choose build status node color](/docs/resources/foundry/data-lineage/node-color-build-status.png)
