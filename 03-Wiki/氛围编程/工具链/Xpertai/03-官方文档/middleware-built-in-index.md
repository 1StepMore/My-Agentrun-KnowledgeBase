---
title: Built-in Middleware
keywords:
- XpertAI
- AI-Agent
- documentation
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/middleware/built-in/index.md
state:
  phase: wiki
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
related: []
source: 历史文件，来源见 sources
evidence: E1
---

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
