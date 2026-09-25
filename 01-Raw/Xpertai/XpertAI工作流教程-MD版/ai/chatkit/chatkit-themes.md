---
title: Themes and Customization
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
# Themes and Customization

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Themes and Customization

<Info>
  Configure colors, fonts, density, and component variants.
</Info>

After finishing the [ChatKit quickstart](/docs/ai/chatkit/), you can change themes and customize the embed. Use light or dark themes, set accent colors, control density and radius, and align ChatKit with your product’s visual style.

## Overview

You usually customize the theme by passing an options object. If you embedded ChatKit using the [ChatKit quickstart](/docs/ai/chatkit/), you can use the React syntax below.

* React: pass options to `useChatKit({...})`

## Explore customization options

Visit [ChatKit Studio](https://chatkit.studio/playground) to see the live implementation and interaction builder. If you prefer to learn by tinkering, these resources are a great starting point.

## Change the theme

Match your product look by specifying colors, fonts, and more. The example below switches to dark mode, updates colors, tweaks radius and density, and sets the font.

See more theme options in the [ChatKit type definitions](https://github.com/xpert-ai/chatkit-js/tree/main/packages/chatkit):

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    theme: {
        colorScheme: "dark",
        color: { 
            accent: { 
                primary: "#2D8CFF", 
                level: 2 
            }
        },
        radius: "round", 
        density: "compact",
        typography: { fontFamily: "'Inter', sans-serif" },
    },
};
```

## Customize start screen text

Adjust the input placeholder to guide users on what to ask or how to begin.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    composer: {
        placeholder: "Ask anything about your data…",
    },
    startScreen: {
        greeting: "Welcome to FeedbackBot!",
    },
};
```

## Offer sample prompts for new conversations

Provide prompts at the start of a session to steer users toward helpful actions.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    startScreen: {
        greeting: "What can I help you build today?",
        prompts: [
            { 
                name: "Check on the status of a ticket", 
                prompt: "Can you help me check on the status of a ticket?", 
                icon: "search"
            },
            { 
                name: "Create Ticket", 
                prompt: "Can you help me create a new support ticket?", 
                icon: "write"
            },
        ],
    },
};
```

## Add custom buttons to the top bar

Use custom top-bar buttons for navigation, context, or integration-specific actions.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    header: {
        customButtonLeft: {
            icon: "settings-cog",
            onClick: () => openProfileSettings(),
        },
        customButtonRight: {
            icon: "home",
            onClick: () => openHomePage(),
        },
    },
};
```

## Enable file attachments (in development)

Attachments are off by default. To enable them, configure the attachment options. Unless you use a custom backend, you must choose the hosted upload strategy. For other strategies with a custom backend, see the Python SDK docs.

You can also control the number, size, and type of files users can upload.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    composer: {
        attachments: {
            uploadStrategy: { type: 'hosted' },
            maxSize: 20 * 1024 * 1024, // 每个文件 20MB
            maxCount: 3,
            accept: { "application/pdf": [".pdf"], "image/*": [".png", ".jpg"] },
        },
    },
}
```

## Enable @-mentions for entity chips (in development)

Let users @-mention custom entities to add richer context and interactions.

* Use `onTagSearch` to return entities for the query.
* Use `onClick` to handle entity click events.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    entities: {
        async onTagSearch(query) {
            return [
                { 
                    id: "user_123", 
                    title: "Zhang san", 
                    group: "People", 
                    interactive: true, 
                },
                { 
                    id: "doc_123", 
                    title: "Quarterly Plan", 
                    group: "Documents", 
                    interactive: true, 
                },
            ]
        },
        onClick: (entity) => {
            navigateToEntity(entity.id);
        },
    },
};
```

## Customize entity chip previews (in development)

Use widgets to customize how entity chips appear on hover. Show cards, document summaries, or images for rich previews.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    entities: {
        async onTagSearch() { /* ... */ },
        onRequestPreview: async (entity) => ({
            preview: {
                type: "Card",
                children: [
                    { type: "Text", value: `Profile: ${entity.title}` },
                    { type: "Text", value: "Role: Developer" },
                ],
            },
        }),
    },
};
```

## Add custom composer tools (in development)

Let users trigger specific app actions from the composer toolbar. The selected tool is sent as the preferred tool to the model.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    composer: {
        tools: [
            {
                id: 'add-note',
                label: 'Add Note',
                icon: 'write',
                pinned: true,
            },
        ],
    },
};
```

## Toggle UI regions and features

Disable major UI regions and features if you plan to implement your own top bar or other options. You can also turn off history if it does not fit your scenario (for example, a support-style chatbot).

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    history: { enabled: false },
    header: { enabled: false },
};
```

## Override locale

If your app enforces a single language, override the default locale. By default, the locale follows the browser setting.

```typescript theme={null}
const options: Partial<ChatKitOptions> = {
    locale: 'zh-Hans',
};
```


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
