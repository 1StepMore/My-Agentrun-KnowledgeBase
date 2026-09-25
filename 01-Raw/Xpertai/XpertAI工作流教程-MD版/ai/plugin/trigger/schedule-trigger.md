---
title: Schedule Trigger
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:53:35'
  time_wiki: '2026-09-23T00:50:32'
source_url: AI生成
source_type: article
source_platform: xpertai
author: XpertAI
fetch_date: '2026-05-08'
priority: 3
language: zh
notes: XpertAI官方文档
author_id: ''
publish_date: ''
---
# Schedule Trigger

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Schedule Trigger

`Schedule Trigger` automatically triggers the Digital Expert workflow based on a time schedule, which is suitable for unattended periodic tasks.

## Applicable scenarios

* Generating daily reports, weekly reports, or inspection reports on schedule
* Syncing external data on schedule and triggering downstream analysis
* Running batch processing during off-peak hours

## Key configuration

Core configuration of Schedule Trigger includes:

* `enabled`: whether enabled
* `cron`: Cron expression (required)
* `task`: default task text injected into the workflow (required)

Before publish, the workflow validates that `cron` is provided; if missing, validation fails.

## Runtime mechanism

1. **Publish phase**:
   * Delete the old task with the same name first (to prevent duplicate registration).
   * Create and start a new task based on `cron`.
2. **Trigger execution phase**:
   * When the scheduled task fires, inject `task` text into the workflow.
   * Let downstream Agent/tool/knowledge nodes continue processing.
3. **Stop phase**:
   * Stop and remove the corresponding Cron task to release scheduler resources.

## Startup recovery strategy

Schedule Trigger uses `bootstrap.mode = replay_publish`:

* After a system restart, it replays publish logic to restore scheduled tasks automatically.
* This fits trigger scenarios that need to continue running after restart.

## Related features

* Trigger node overview: [Workflow Trigger](../../workflow/trigger/)
* Multi-channel access for Digital Expert: [Digital Expert](../../digital-expert/digital-expert/)
* Trigger plugin overview: [Trigger Plugin](./)


## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

## 关联问题

- 这个概念和其他知识有什么联系？
- 这个观点和我的已有认知是否冲突？

---

## 抓取备注

- 抓取时间：2026-05-08
- 抓取工具：手动导入
- 质量评分：
