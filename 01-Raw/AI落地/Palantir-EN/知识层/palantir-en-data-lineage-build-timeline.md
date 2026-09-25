---
title: Palantir 官方文档（英文原版）· View build timeline
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/build-timeline/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/build-timeline/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-build-timeline.md`

# View build timeline

Use the **Build timeline** tool in Data Lineage to view the build history of your datasets.

In Data Lineage, click on **Build timeline** in the bottom left of your window. This action expands the view panel to display a Gantt chart of builds that took place during the period of time of your choice. You can select the number of days or hours you would like to view in your timeline, ranging from one hour to ten days. You can also choose to display the builds by color based on schedule or job status.

![View build timeline in Data Lineage](/docs/resources/foundry/data-lineage/build-timeline.png)

To view the build timeline of a specific dataset, select the dataset on your graph. Select multiple datasets with the **Drag select mode** tool or by holding `Ctrl / Command ` while clicking.

To view details of a job in the build timeline, click on the job in the Gantt chart. You will see information about the job status, start and end time, and duration.

![View job details in build timeline](/docs/resources/foundry/data-lineage/job-details-window.png)

See more details about the build, job, and schedule by clicking on the links within the job information window.
