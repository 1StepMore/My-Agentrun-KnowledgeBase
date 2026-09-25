---
title: Built-in Middleware
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
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
# Built-in Middleware

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in Middleware

Built-in middleware for common proxy use cases

XpertAI provides built-in middleware for common use cases. Each middleware is production-tested and can be configured according to your specific needs.

## Model Provider Agnostic Middleware

The following middleware works with any LLM provider:

| Middleware                                                    | Description                                                                                     |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [Context Compression](#context-compression)                   | Automatically summarizes conversation history when approaching session limit.                   |
| [Sensitive Filter Middleware](./sensitive-filter)             | Filters sensitive input/output content using rule-based or LLM policies.                        |
| [Agent Behavior Monitor Middleware](./agent-behavior-monitor) | Detects prompt injection, risky instructions, high-frequency tool calls, and repeated failures. |

### Context Compression

Automatically summarizes conversation history when approaching token limits, preserving recent messages while compressing older context. The summarization feature is suitable for the following scenarios:

* Long conversations that exceed the context window.
* Multi-turn dialogues with extensive history.
* Applications that need to retain full conversation context.


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
