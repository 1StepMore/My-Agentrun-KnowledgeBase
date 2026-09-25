---
title: DingTalk
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
# DingTalk

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# DingTalk

With DingTalk integration, Xpert can receive messages from DingTalk private chats and group chats, then send expert responses back to DingTalk.

## Capability Overview

Current `@xpert-ai/plugin-dingtalk` capabilities:

* Receive DingTalk events via HTTP callback
* Handle private chat messages
* Handle group messages when users mention the bot (`@bot`)
* Send text/Markdown/card notifications via middleware
* Update sent messages via middleware
* Recall OTO (human-bot) messages via middleware

Current limitations:

* **HTTP callback only** (no Stream mode)
* In groups, only `@bot` messages are processed
* Recall currently applies to OTO messages only
* Group list APIs are not stable across tenants; do not rely on automatic group discovery

## Prerequisites

Before setup, prepare:

1. A DingTalk enterprise account with app management permission
2. An internal enterprise app with robot capability enabled
3. A public Xpert service URL
4. Callback security values (`callbackToken`, `callbackAesKey`)

## Required Permissions

To read users (for user selector or `dingtalk_list_users`), you must grant:

* `qyapi_get_department_member` (department member read permission)

Without this permission, DingTalk APIs return insufficient permission errors (for example `60011`).

## Create DingTalk Integration in Xpert

Go to **Settings -> System Integrations** and create a provider of type DingTalk.

### Required fields

| Field                  | Description                         |
| ---------------------- | ----------------------------------- |
| `Client ID (AppKey)`   | DingTalk AppKey (same as Client ID) |
| `Client Secret`        | DingTalk app secret                 |
| `Enable HTTP Callback` | Must be enabled in current version  |
| `Callback Token`       | Signature verification token        |
| `Callback AES Key`     | Used to decrypt callback payload    |

### Recommended fields

| Field                | Description                                        |
| -------------------- | -------------------------------------------------- |
| `Robot Code`         | Needed for proactive send/update/recall operations |
| `Xpert`              | Fallback target when trigger binding is not hit    |
| `Preferred Language` | `zh-Hans` or `en`                                  |

:::tip
`Client ID` and DingTalk `AppKey` are the same value.
:::

## Configure DingTalk Callback

After saving integration, you can get callback info from system integration test:

```text theme={null}
POST /api/dingtalk/webhook/:integrationId
```

Example:

```text theme={null}
https://<your-domain>/api/dingtalk/webhook/<integrationId>
```

Recommended DingTalk console setup:

1. Use this public callback URL in event/callback settings.
2. Keep DingTalk token/aes\_key consistent with Xpert integration config.
3. Use HTTP push mode.

## Build an Auto-Reply Bot (MyCoder Scenario)

1. Create and validate a DingTalk integration in Xpert.
2. Add **DingTalk Trigger** to target expert workflow and select that integration.
3. Publish the expert.
4. Add the application bot to target group.
5. Send `@bot` message in the group for verification.

Routing priority after publish:

1. Existing conversation binding
2. DingTalk trigger binding (`integrationId -> xpertId`)
3. Integration-level fallback `xpertId`

## DingTalk Notify Middleware

Common tools:

* `dingtalk_send_text_notification`
* `dingtalk_send_rich_notification`
* `dingtalk_update_message`
* `dingtalk_recall_message`
* `dingtalk_list_users`

`dingtalk_send_rich_notification` supports:

* `markdown`
* `interactive`
* `template`

### Recipient Configuration

Middleware resolves target by `recipient_type + recipient_id`.

Common `recipient_type` values:

* `user_id`
* `open_id`
* `chat_id`

Best practices:

* For user notifications, prefer stable user identifiers (`open_id` or mapped `user_id`).
* For group notifications, use `chat_id` (`openConversationId`).
* `recipient_id` can use runtime variable (for example `{{state.dingtalkRecipientId}}`).

## References

* [DingTalk Open Platform](https://open.dingtalk.com/document/dingstart)
* [Robot Development Overview](https://open.dingtalk.com/document/development/development-robot-overview)
* [Robot Sends Group Message](https://open.dingtalk.com/document/development/the-robot-sends-a-group-message)
* [Robot Sends Interactive Card](https://open.dingtalk.com/document/development/robots-send-interactive-cards)


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
