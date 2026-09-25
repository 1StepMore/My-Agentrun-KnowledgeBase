---
title: DingTalk Trigger
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
# DingTalk Trigger

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# DingTalk Trigger

DingTalk Trigger binds one DingTalk integration to one Xpert, so callback events are routed to the correct expert reliably.

## Why DingTalk Trigger Is Needed

A DingTalk integration only handles connectivity and callback ingestion.

To decide which Xpert should process an incoming message, the trigger creates a binding:

```text theme={null}
integrationId -> xpertId
```

## Configuration

Current DingTalk Trigger fields:

* `Enabled`
* `DingTalk Integration` (required)

:::tip
Changes take effect only after the expert is published again.
:::

## Activation Flow

1. Create DingTalk integration
2. Add DingTalk Trigger in workflow
3. Select target DingTalk integration
4. Publish expert
5. Platform persists trigger binding
6. New messages from this integration route to the current expert

## Routing Priority

DingTalk routing priority:

1. Existing conversation binding
2. Trigger binding
3. Integration fallback `xpertId`

If all are missing, the message has no target expert.

## Binding Tables

DingTalk plugin uses two persistent bindings:

1. `plugin_dingtalk_trigger_binding`
2. `plugin_dingtalk_conversation_binding`

Meanings:

* `trigger_binding`: default expert ownership for one integration
* `conversation_binding`: conversation continuity for one DingTalk conversation user key

## Constraints

* One `integrationId` can bind to only one `xpertId`
* In group chats, only `@bot` messages trigger processing
* Stopping trigger or taking expert offline clears relevant bindings

## FAQ

### Trigger configured but not effective

Re-publish the expert.

### Private chat works, group chat does not

Check bot membership in the group and confirm the message mentions `@bot`.

### Why did routing not switch to new expert immediately

Existing conversation binding has higher priority; end current conversation before testing new routing.


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
