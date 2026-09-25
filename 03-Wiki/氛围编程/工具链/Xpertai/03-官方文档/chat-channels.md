---
title: Chat Channels
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/chat-channels.md
---
# Chat Channels

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
