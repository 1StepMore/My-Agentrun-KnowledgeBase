---
title: Variable Assigner
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
# Variable Assigner

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Variable Assigner

In the XpertAI workflow system, the **Variable Assigner Node** assigns values to writable variables, enabling information recording, state updates, and context maintenance. It’s a core component for user preference memory, session state management, and process data transfer. This node writes existing variable values to persistent variables.

## Configuration Process

Below is a typical "memory write" scenario for variable assigner configuration:

### 1. Define Session Variable Structure

Define a session variable named `memories`:

* Type: `array[object]`
* Purpose: Record facts, preferences, and historical data from user input.

### 2. Check for New Information

After user input, use a **Conditional Node** with LLM reasoning:

* If new information is detected, take the upper branch.
* If no new information, take the lower branch and generate a response using existing memories.

### 3. Extract New Information

In the upper branch, add an **LLM Node** to extract user input into structured facts, e.g.:

```json theme={null}
{
  "fact": "User likes black coffee",
  "time": "2025-06-29"
}
```

### 4. Variable Assigner/Memory Write

Use the **Variable Assigner Node** to append LLM output to the `memories` array:

* Operation: Select variable type as `array`, operation as `append`.
* Content: Extract object from LLM output using variable reference (e.g., `{llm.result}`).
* If LLM output is a string, convert to standard object structure before writing.

### 5. Read Memory in Subsequent Nodes

In subsequent **LLM Nodes**, concatenate `memories` content into a string for context input, e.g.:

```text theme={null}
Historical Information:
1. User likes black coffee.
2. User often checks order status in the morning.
```

Insert into the system prompt for personalized response capability.

## Summary

The Variable Assigner Node enables flexible data writing, forming the foundation for stateful, personalized, multi-turn dialogue experiences. Combined with conditional nodes, LLM nodes, and memory mechanisms, it builds smarter business processes and user interactions.


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
