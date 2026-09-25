---
title: Trigger
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
# Trigger

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger

Trigger nodes are special nodes responsible for executing workflows in response to specific conditions.

**Trigger nodes** are activated when the current workflow is updated or activated, or when a digital expert instance is started or restarted. You can use trigger nodes to notify when these events occur.

## The role of triggers in workflows

Triggers determine "who" sends input into the Digital Expert workflow and "when" it happens. A single Digital Expert can bind different types of triggers to cover different business entry points.

Typical entry points include:

* **Chat Trigger**: User input from the in-platform chat interface.
* **[Lark Trigger](../plugin/trigger/lark-trigger/)**: Input from Lark message events.
* **[Schedule Trigger](../plugin/trigger/schedule-trigger/)**: System input from Cron-based scheduled tasks.

After receiving input, triggers inject data into workflow state, and then downstream nodes (Agent, tool invocation, knowledge retrieval, etc.) continue processing.

## Trigger lifecycle

Triggers typically include three phases:

1. **validate**: Check whether trigger configuration is complete and valid.
2. **publish**: Register trigger capabilities when publishing or activating a workflow (such as registering callbacks or creating scheduled jobs).
3. **stop**: Release resources when disabling a workflow (such as deleting scheduled jobs or unbinding external integrations).

Recovery strategy after system restart may vary by trigger type:

* **replay\_publish**: Replay publish logic to restore trigger capability automatically.
* **skip**: Skip auto-recovery and continue through runtime events or external systems.

## Chat Trigger Node

When building AI workflows for chatbots and other chat interfaces, use the chat trigger node.

### Node Parameters

A list of parameters for defining a pre-input form for the digital expert conversation interface, allowing users to enter necessary information before starting the conversation.

## Related docs

* How a Digital Expert connects to different conversation channels via triggers: [Chat Channels](../digital-expert/chat-channels/)
* Trigger plugin implementation details (including Lark and Schedule): [Plugin Trigger](../plugin/trigger/)


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
