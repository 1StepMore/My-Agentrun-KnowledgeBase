---
title: Palantir 官方文档（英文原版）· Manage schedules
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/manage-schedules/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/manage-schedules/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-manage-schedules.md`

# Manage schedules

Data Lineage allows you to easily manage build schedules within your lineage graph. In the right sidebar, select **Manage schedules** to open the schedule details pane.

![Manage schedules in Data Lineage](/docs/resources/foundry/data-lineage/manage-schedules.png)

You will see the schedules related to selected datasets in your graph. Click on a schedule to see more details:

![Manage schedules details in Data Lineage sidebar](/docs/resources/foundry/data-lineage/manage-schedule-details.png)

* **Latest run:** The status of the latest run of the schedule.
* **Last update:** A timestamp of when the last update took place and the user who made changes
* **Target datasets:** A list of downstream datasets included in the build schedule.
* **When to build:** Displays the build schedule trigger determined when creating the build schedule. For example, a build schedule can be set to run **when specific datasets update.**
* **Build scope:** Defines the Project or user datasets included in the build and the permissions used to run the build.

Learn more about scheduling builds in the [**Building pipelines**](/docs/foundry/building-pipelines/scheduling-overview/) documentation.
