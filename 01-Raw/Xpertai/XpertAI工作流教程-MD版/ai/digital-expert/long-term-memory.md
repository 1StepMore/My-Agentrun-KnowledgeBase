---
title: Long-Term Memory
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
# Long-Term Memory

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Long-Term Memory

## What is Memory?

AI memory refers to the ability to process, store, and effectively recall past interactions. This allows intelligent systems to learn from feedback and adapt to user preferences. Memory can be categorized into two types: short-term memory and long-term memory.

* **Short-Term Memory** (memory within the scope of a session thread): The system can access short-term memory within a single session thread. This memory is managed as part of the agent's state and is persisted in a database through a checkpoint mechanism, allowing sessions to be resumed at any time. Short-term memory updates during process execution or after step completion and is read at the start of each step.

* **Long-Term Memory** (memory shared across threads): Long-term memory applies across multiple session threads and can be accessed in any thread at any time. It is not restricted to a single thread ID but can be stored and retrieved using custom namespaces. Xpert AI provides storage functionality to save and retrieve this long-term memory.

Currently, most AI applications are like "goldfish," unable to retain information between conversations. This short-sightedness is not only inefficient but also limits the capabilities of AI.

## Cross-thread Memory

Cross-session memory enables AI agents to store and retrieve information across different conversation threads. This allows the agent to retain context, user preferences, and historical information across multiple interactions, delivering smarter and more personalized experiences.

## Configuring Long-Term Memory

This configuration controls how information is extracted from conversations and stored in long-term memory.

**Memory Types** include *User Profiles*, *Q\&A*, and *Custom*.

### User Profile

* **Interval (seconds)**: Sets the delay in seconds before extracting information after a conversation ends. The default is 10 seconds, meaning the system will create a background task for information extraction 10 seconds after the user and Xpert stop interacting.
* **Prompt**: Guides the system on how to extract information from conversations. If no prompt is provided, the system uses a default one.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/feature-long-term-memory.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=c01b988245186a76054780421623f9eb" alt="Config Long-term memory" width="1088" height="616" data-path="public/img/ai/feature-long-term-memory.png" />

### Q\&A

In **Q\&A** mode, summarized memories are created by extracting questions and answers when the user likes a response.

### Custom Memory

**Custom** memory allows users to define their own rules for extracting information.

:::warning 🚧\
Under Development\
:::

## Managing Memory

The management page serves as a centralized interface for managing and maintaining Xpert memory data.

* **Score**: Represents the degree of similarity during semantic searches (0–1).
* **Creator**: Indicates the owner of the memory.
* **Value**: Stores the memory content in JSON format.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-long-term-memory.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=53444e3ecf07857e08ca34cc63002263" alt="Manage xpert memory" width="3024" height="1718" data-path="public/img/ai/xpert-long-term-memory.png" />

On this page, users can delete individual memories or clear all memories for a specific expert.

**Semantic Search Testing** allows users to test the retrieval of memories related to specific queries.


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
