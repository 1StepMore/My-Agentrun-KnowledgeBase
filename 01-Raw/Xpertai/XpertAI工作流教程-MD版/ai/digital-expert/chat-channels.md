---
title: Chat Channels
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
# Chat Channels

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Channels

This page explains how a Digital Expert can connect to different conversation channels through triggers while reusing the same agent workflow capabilities.

## Supported conversation channels

Besides being used directly in the in-platform chat interface, a Digital Expert can enter the same workflow through different Trigger channels:

* **In-platform chat channel (Chat Trigger)**: The flow is triggered when users submit questions in the platform chat window.
* **[Scheduled channel (Schedule Trigger)](../plugin/trigger/schedule-trigger/)**: The system triggers the Digital Expert on a Cron schedule for fixed tasks (such as daily summaries or inspection reminders).
* **[Lark channel (Lark Trigger)](../plugin/trigger/lark-trigger/)**: Users send messages in Lark, and the Lark trigger routes them to the corresponding Digital Expert.

## Integration principles

All three channels share the same Digital Expert configuration:

* Agent orchestration
* Toolset and tool authorization
* Knowledge base and retrieval logic

The differences are mainly in trigger timing and input source, not in the core workflow execution.

## Related docs

* Trigger node overview: [Workflow Trigger](../workflow/trigger/)
* Trigger plugin implementation (Lark / Schedule): [Plugin Trigger](../plugin/trigger/)
* Main Digital Expert doc: [Digital Expert](./digital-expert/)
* Toolset guide: [Toolset](../toolset/)
* Knowledge base guide: [Knowledge Base](../knowledge-base/)


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
