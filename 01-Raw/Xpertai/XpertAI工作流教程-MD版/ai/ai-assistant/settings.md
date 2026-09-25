---
title: Settings
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
# Settings

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Settings

Here is the basic configuration for the AI assistant in the Xpert AI system:

| Configuration Item    | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| **AI Model Provider** | Supported AI providers, such as OpenAI, Azure OpenAI, etc.        |
| **Default Model**     | The default AI model selected for handling general tasks.         |
| **Token Limit/User**  | The initial token usage limit per account, controlling API usage. |

This table provides a concise overview of the AI assistant's basic settings, enabling users to quickly understand and configure them.

## AI Providers

The Xpert platform supports mainstream AI model providers.

<img src="https://mintcdn.com/xpertai/0avAZsO6pri8DJS6/public/img/copilot/copilot-ai-providers.png?fit=max&auto=format&n=0avAZsO6pri8DJS6&q=85&s=24b342af7149c2f7b987f30b988e2cf7" alt="AI Providers" width="1698" height="1535" data-path="public/img/copilot/copilot-ai-providers.png" />

### Supported Model Providers

Xpert AI supports a wide range of AI providers to enhance flexibility and task-handling capabilities:

| AI Provider    | Official Website                                                           |
| -------------- | -------------------------------------------------------------------------- |
| OpenAI         | [https://openai.com](https://openai.com)                                   |
| Azure OpenAI   | [https://azure.microsoft.com](https://azure.microsoft.com)                 |
| Ollama         | [https://ollama.com](https://ollama.com)                                   |
| DeepSeek       | [https://deepseek.com](https://deepseek.com)                               |
| Anthropic      | [https://anthropic.com](https://anthropic.com)                             |
| Alibaba Tongyi | [https://bailian.console.aliyun.com/](https://bailian.console.aliyun.com/) |
| Zhipu AI       | [https://zhipu.ai](https://zhipu.ai)                                       |
| Together AI    | [https://together.ai](https://together.ai)                                 |
| Moonshot AI    | [https://moonshot.ai](https://moonshot.ai)                                 |
| Groq AI        | [https://groq.com](https://groq.com)                                       |
| Mistral AI     | [https://mistral.ai](https://mistral.ai)                                   |
| Cohere AI      | [https://cohere.ai](https://cohere.ai)                                     |

<Info>
  **No specific order**\
  [Add more providers](https://github.com/xpert-ai/xpert/tree/main/packages/server-ai/src/ai-model/model_providers)
</Info>

The multi-provider support in Xpert AI allows it to adapt to various business scenarios and dynamically select the best model to handle specific tasks.

## AI Copilot Roles

The AI Copilot in the Xpert AI system is divided into three roles, each responsible for different tasks. More roles may be added in the future for other purposes.

1. **Primary**: The main inference copilot, responsible for core task reasoning and generating solutions. It is primarily used for solving complex user problems and engaging in deep conversations.
2. **Secondary**: Acts as a support role in user interactions, providing background information, quick answers, or suggestions to enhance the efficiency of conversations.
3. **Embedding**: Focused on vectorizing files and text for semantic search and deep information retrieval, especially useful for large-scale document processing and analysis.


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
