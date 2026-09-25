---
title: Feishu (Lark)
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
- Xpertai/XpertAI工作流教程-MD版/ai/toolset/feishu.md
---
# Feishu (Lark)

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Feishu (Lark)

The following toolkits are available for integrating with Feishu (Lark) features:

* [**Feishu Messages**](#feishu-messages): Send Feishu (Markdown) messages to Feishu groups or users.
* **Feishu Tasks**: Manage Feishu tasks. (In development)
* **Feishu Wiki**: Manage Feishu wiki documents. (In development)
* **Feishu Calendar**: Manage events in the Feishu calendar. (In development)

## Feishu Messages

The **Feishu Messages Toolkit** allows you to send messages to specific Feishu groups or users via system-integrated connections.

**Configuration**:

* **Feishu Integration**: Select an established integration connection between your system and Feishu.
* **Chat Group**: Choose a group where a Feishu bot is present; messages will be sent there.
* **User**: Select a user to receive the message.

<Tip>
  **Permissions**

  Enable one of the following permissions to access the contact directory:\
  \[im:chat:readonly, im:chat, im:chat.group\_info:readonly, im:chat:read]

  Enable one of the following permissions to send messages:\
  \[im:message:send, im:message, im:message:send\_as\_bot]
</Tip>
