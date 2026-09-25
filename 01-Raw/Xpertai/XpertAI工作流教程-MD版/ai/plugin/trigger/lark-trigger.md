---
title: Lark Trigger
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
# Lark Trigger

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Lark Trigger

`Lark Trigger` connects Lark message events to the Digital Expert workflow, enabling the trigger chain of “send a message in Lark, execute the Digital Expert in Xpert”.

## Applicable scenarios

* Triggering a Digital Expert by @mentioning a bot in Lark group chats or direct chats
* Using enterprise IM as a unified entry for Digital Experts
* Mapping external message events into workflow inputs

## Key configuration

Core configuration of Lark Trigger includes:

* `enabled`: whether the trigger is enabled
* `integrationId`: Lark integration instance ID (required)

Validation before publish checks:

1. Whether a valid Lark integration is selected.
2. Whether the current integration is already bound to another Digital Expert (to avoid conflicts).

## Runtime mechanism

1. **Publish phase**: Write the `integrationId -> xpertId` binding and register in-memory callbacks.
2. **Message arrival phase**: Locate the bound Digital Expert by `integrationId`.
3. **When callback is available**: Build the handoff message directly and advance the current flow.
4. **When callback is unavailable (for example, after restart)**: Enter the persistent dispatch queue to guarantee no message loss.

## Startup recovery strategy

Lark Trigger uses `bootstrap.mode = skip`:

* It does not replay `publish` at startup.
* It relies on persistent bindings and external message events to resume processing.

This approach is suitable for triggers continuously driven by external events and avoids duplicate registration.

## Related features

* Trigger node overview: [Workflow Trigger](../../workflow/trigger/)
* Multi-channel access for Digital Expert: [Digital Expert](../../digital-expert/digital-expert/)
* Lark plugin and integration background: [Lark Plugin Docs](../lark/)
* Source code: [xpert-plugins / lark integration](https://github.com/xpert-ai/xpert-plugins/tree/main/xpertai/integrations/lark)


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
