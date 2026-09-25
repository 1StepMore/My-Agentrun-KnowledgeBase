---
title: Actions
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
- Xpertai/XpertAI工作流教程-MD版/ai/chatkit/chatkit-actions.md
---
# Actions

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Actions

<Warning>In development</Warning>

<Info>
  Trigger backend actions based on user interactions in chat.
</Info>

Actions let the ChatKit SDK frontend trigger streaming responses before a user submits a message and can also trigger side effects outside ChatKit.

## Trigger actions

### Respond to widget interactions

Attach an `ActionConfig` to supported widget nodes to fire actions. For example, react to a button click: when the user clicks the button, the action payload is sent to your server, where you can update widgets, run reasoning, or stream new thread entries.
