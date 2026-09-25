---
title: Agent Tool
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
# Agent Tool

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Tool

The **Agent Tool Node** in the XpertAI platform's Workflow serves as a **callable tool for an Agent**, executing a predefined **sub-workflow** to accomplish specific tasks when triggered.

Compared to the **Task Handover** node’s **single-task transfer** mode, the **Agent Tool Node** can, upon invocation:

* Execute multi-step, complex sub-workflows
* Invoke multiple functional nodes
* Branch or loop based on task results

This makes it highly suitable for scenarios requiring **multi-step processing or complex logic orchestration**.

***

## **How It Works**

1. **Tool Registration and Invocation**

   * The Agent Tool Node can be registered as an “available tool” by any higher-level Agent.
   * The higher-level Agent can actively call this tool node to perform specific tasks during task processing.

2. **Connecting Sub-Workflows**

   * The Agent Tool Node can connect to a single subsequent node or multiple nodes to form a **complete sub-workflow**.
   * Sub-workflows can include:

     * Data processing nodes
     * Computation and analysis nodes
     * External API calls
     * File/database operations
     * Interactions with other agents

3. **Task Context Passing**

   * When called, the Agent Tool Node receives contextual information (task content, variables, history, etc.) from the upstream Agent.
   * All nodes within the sub-workflow can access and utilize this contextual information.

4. **Task Completion and Result Return**

   * After the sub-workflow is executed, the Agent Tool Node returns the processing results to the calling Agent or passes them to subsequent nodes in the main workflow (if the tool is an endpoint).

***

## **Configuration Details**

After adding an **Agent Tool Node** in the Workflow editor, the following configurations are available:

| Configuration Item         | Description                                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Node Name**              | Custom display name for the node in the workflow                                                         |
| **Node Description**       | Custom description for the node in the workflow                                                          |
| **Tool Name**              | Name of the tool for reference during Agent invocation                                                   |
| **Tool Description**       | Functional description for reference during Agent invocation                                             |
| **Input Parameters**       | Define variables and data that can be passed during invocation                                           |
| **Sub-Workflow Structure** | Configure connected sub-nodes and their execution logic                                                  |
| **Endpoint**               | Specify if the tool is an endpoint; if so, the Agent response ends or proceeds to subsequent Agent nodes |

***

## **Use Case Examples**

### **1. Data Processing and Analysis Tool**

* Main Agent receives a task to “generate a market analysis report.”
* Calls the Agent Tool Node to execute a sub-workflow:

  1. Data Collection Node → Retrieve raw data
  2. Data Cleaning Node → Remove outliers
  3. Visualization Generation Node → Output charts

### **2. Automated Content Generation Tool**

* Main Agent is responsible for planning a marketing campaign.
* Calls the Agent Tool Node to execute:

  1. Copywriting Node → Generate initial draft
  2. Language Polishing Node → Refine expression
  3. Image Generation Node → Provide accompanying visuals

### **3. Business Approval Sub-Workflow**

* Main Agent receives a “leave request” task.
* Calls the Agent Tool Node to execute:

  1. Check leave balance
  2. Send approval request
  3. Notify applicant of approval result

***

## **Advantages**

* **Highly Scalable**: Supports sub-workflows of any complexity
* **Multi-Function Integration**: Can call external APIs, databases, and other tools
* **Context Integrity**: Ensures tasks in the sub-workflow align with the main workflow’s information
* **Reusability**: A single Agent Tool Node can be invoked by multiple different Agents

***

## **Best Practices**

1. When designing an Agent Tool Node, clearly define functional goals to avoid overly scattered logic.
2. Use reusable functional nodes in sub-workflows to facilitate cross-scenario invocation.


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
