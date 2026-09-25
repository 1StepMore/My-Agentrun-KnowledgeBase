---
title: Embedding WebApp
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
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/embed-webpage.md
---
# Embedding WebApp

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedding WebApp

This guide explains how to embed our chatbot into your website or application. By doing so, you can provide instant support and enhance the user experience for your audience.

To embed the chatbot, follow these steps:

* Open the Digital Expert Console and navigate to the Monitoring page. In the WebApp card section of the Monitoring page, you'll find the configuration for embedding the application.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-monitor-public-webapp.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=fc6d81d528ef0077ce84fad9c3d481a5" alt="Embedded Webapp" width="2886" height="920" data-path="public/img/ai/xpert-monitor-public-webapp.png" />

* Use the **Preview** button to open a new browser tab and preview how the embedded application will look.

```html theme={null}
<iframe
  src="https://app.xpertai.cn/x/call-center-chatbot"
  style="width: 100%; height: 100%; min-height: 700px"
  frameborder="0"
  allow="microphone">
</iframe>
```

<div className="w-full flex justify-center mb-8">
  <iframe src="https://app.xpertai.cn/x/call-center-chatbot" width="600" height="500" class="mx-auto shadow-lg rounded-sm border border-solid border-gray-300" />
</div>

* Click the **Embed** button to open a dialog box, choose the embedding method, and copy the code to your website or application.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-embedded-button.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=5944a78625b7037cbbba822a4ce6ec63" alt="Embedded Webapp Button" width="1138" height="1353" data-path="public/img/ai/xpert-embedded-button.png" />

* Use the **Settings** button to open a dialog box and configure the application's access permissions:
  * **Public**: Accessible to everyone, including anonymous users.
  * **Private**: Accessible only to users with accounts; anonymous users are restricted.
