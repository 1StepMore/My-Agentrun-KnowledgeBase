---
title: Agent Middleware
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
# Agent Middleware

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Middleware

## Overview

Control and customize agent execution at every step.

Middleware provides a more fine-grained way to control the internal operations of agents. Middleware is suitable for the following scenarios:

* Track agent behavior through logging, analytics, and debugging.
* Transform prompts, tool selection, and output formats.
* Add retry, fallback, and early termination logic.
* Apply rate limiting, guardrails, and PII detection.

## Agent Loop

The core agent loop involves calling the model, having the model choose which tools to execute, and then ending when no more tools need to be called:

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/core_agent_loop.avif?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=28f76e9cf0f026757990c1f70915c1ba" alt="Core agent loop diagram" width="300" height="268" data-path="public/img/ai/xpert/core_agent_loop.avif" />

Middleware exposes hooks before and after each step:

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/middleware_final.avif?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=aac1bfb54ecd02ff52e293e6e60814c7" alt="Middleware flow diagram" width="500" height="560" data-path="public/img/ai/xpert/middleware_final.avif" />

## Middleware Nodes

In XpertAI, agent nodes support attaching multiple middleware to an Agent in a visual way. Users can manage the order and configuration of middleware in a unified manner in the right panel, achieving the same pluggable Middleware architecture as LangChain.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/agent-middleware-nodes.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=8383939aabe351cd01ada3468b3676bb" alt="Middleware node config" width="2410" height="1618" data-path="public/img/ai/xpert/agent-middleware-nodes.png" />

Each middleware has its own independent configuration panel, where you can adjust its execution parameters and behavior, forming a visual, configurable, and extensible agent execution pipeline.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/middleware-node-config.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=dbcd182086fd29603746e650376d7fd8" alt="Middleware node config" width="2404" height="1616" data-path="public/img/ai/xpert/middleware-node-config.png" />

Click the graph button to open the digital expert agent, and you can see the execution order and relationship between middleware and agents:

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/agent-middleware-graph.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=80e6a0932c29823ac941029e31a1d5a5" alt="Middleware graph" width="2400" height="1116" data-path="public/img/ai/xpert/agent-middleware-graph.png" />


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
