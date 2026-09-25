---
title: Code Execution
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
# Code Execution

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Code Execution

The **Code Node** in XpertAI workflows supports running Python (in development) or Node.js code, enabling developers to efficiently perform data transformations. This node is suitable for various scenarios such as arithmetic calculations, JSON processing, and text transformations, making your workflows more flexible.

With the **Code Node**, developers can embed custom Python (in development) or JavaScript scripts to manipulate variables beyond the capabilities of preset nodes. You can freely configure input and output variables and write the corresponding execution logic.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/workflow-code.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=67f11239e094b02b7fa2ce56bfca21ec" alt="Code Node" width="1498" height="1522" data-path="public/img/ai/workflow/workflow-code.png" />

## Configuration Guide

If the **Code Node** needs to use variables from other nodes, you must define variable names in the **input variables** section and reference them in your code. For detailed variable management, refer to [Session Variables](/docs/ai/workflow/variables/).

## Advanced Features

### 1. Error Retry Mechanism

In certain exceptional cases, re-executing the **Code Node** may resolve the issue. By enabling the **error retry** feature, the system will automatically retry execution based on predefined strategies to enhance workflow stability.

* **Maximum retry attempts**: 10
* **Maximum retry interval**: 5s

You can adjust these parameters according to business needs to optimize the retry strategy.

### 2. Exception Handling

Errors may occur during code execution. To prevent a single node failure from disrupting the entire workflow, you can enable **exception handling** in the **Code Node** and configure appropriate response strategies.

#### Configuration Steps:

1. Enable the **"Exception Handling"** option in the **Code Node**.
2. Select an appropriate exception handling strategy and configure it accordingly.

For more exception handling strategies, refer to [Exception Handling](/docs/ai/workflow/error-handling/).


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
