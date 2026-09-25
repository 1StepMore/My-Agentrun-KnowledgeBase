---
title: Widgets
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
# Widgets

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Widgets

<Tip>
  **PRO** This feature is available in the **Pro** plan.
</Tip>

<Info>
  Learn how to design widgets for your chat experience.
</Info>

Widgets are the containers and components provided by ChatKit. Use prebuilts, tweak templates, or design your own to fully customize ChatKit in your product.

<img src="https://mintcdn.com/xpertai/s0VVkPNi8D_ZpOIf/public/img/ai/chatkit/a2ui_gallery_examples.png?fit=max&auto=format&n=s0VVkPNi8D_ZpOIf&q=85&s=52f405def2655e69adda736e146892f0" alt="ChatKit widgets" width="1662" height="927" data-path="public/img/ai/chatkit/a2ui_gallery_examples.png" />

## Quickly design widgets

Use the widget builder in [A2UI Widget Builder](https://go.copilotkit.ai/A2UI-widget-builder) to experiment with card layouts and list rows, and preview components. Once you like the design, copy the generated JSON into your integration and serve it from the backend.

## Widget middleware

With middleware, the model can return ChatKit widgets via tool calls or structured outputs for the frontend to render. Use middleware to dynamically change widget content, style, or behavior based on user context or preferences.

<img src="https://mintcdn.com/xpertai/s0VVkPNi8D_ZpOIf/public/img/ai/chatkit/chatkit-widgets-middleware.png?fit=max&auto=format&n=s0VVkPNi8D_ZpOIf&q=85&s=2a55ec2064e4234726b0d3eaa10bb559" alt="ChatKit widgets middleware" width="1810" height="1538" data-path="public/img/ai/chatkit/chatkit-widgets-middleware.png" />

ChatKit widgets can surface context, shortcuts, and interactive cards directly in the conversation. When a user clicks a widget button, your app receives a custom action payload so your backend can respond.

## Handle actions on the server

Widget actions let users trigger logic from the UI. Bind actions to widget node events (such as button clicks) and handle them on the server or client integration.

Use the `widgets.onAction` callback (or the equivalent React hook) to capture widget events. Forward the action payload to your backend for processing.

```typescript theme={null}
chatkit.setOptions({
    widgets: {
        async onAction(action, item) {
            await fetch('/api/widget-action', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action, itemId: item.id }),
            });
        },
    },
});
```

## Wrap-up

ChatKit widgets give your chat app rich display and interaction options. By combining prebuilts, custom designs, middleware, and action handling, you can create highly personalized and dynamic user experiences.

Learn more about the [A2UI spec](https://a2ui.org/).


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
