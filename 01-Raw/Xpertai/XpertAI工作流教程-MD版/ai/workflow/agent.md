---
title: Agent
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
# Agent

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent

In the Xpert AI platform, the **Agent Node** is a highly autonomous and flexible component responsible for performing specific tasks and coordinating various sub-tasks, tools, knowledge bases, or external experts.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/workflow/agent.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=63e5717fc9a4baf2a918427fdd067b10" alt="agent node" width="2426" height="1612" data-path="public/img/ai/workflow/agent.png" />

## Core Features

### Sub-Agent and Tool Invocation

* **Automatic Sub-Agent Selection**: The Agent can automatically select the appropriate sub-agent (Sub-Agents) based on the input needs and task type to handle the task. A sub-agent is an execution module for specific tasks, which helps achieve complex functionality.
* **Tool Support**: The Agent can use different tools (Tools) to assist with task execution, such as performing calculations, querying databases, or sending messages.

### Knowledge Base and External Digital Experts

* **Knowledge Base Access**: The Agent can query an internal knowledge base for background information, rules, or decision support, enhancing task accuracy and intelligence.
* **External Expert Support**: When tasks involve specific domains or external resources, the Agent can call on external experts (External Experts) or API services to get the latest information or technical support.

### Intelligent Decision Making and Automation

* **Task Automation**: The Agent makes intelligent decisions based on task requirements and available data, automatically choosing the best processing method, reducing manual intervention.
* **Parallel Task Execution**: Supports the parallel execution of multiple tasks to improve efficiency and response speed.

### Self-Optimization and Adaptability

* **Learning and Optimization**: The Agent node continuously optimizes its behavior through real-time feedback and historical data, improving task processing efficiency and accuracy.
* **Flexible Adaptation**: The Agent can flexibly adjust its task processing methods to adapt to different business scenarios, based on environmental changes and user needs.

## Parameters

The **custom parameters** feature of the Agent allows users to define multiple parameters for the Agent, with specific parameter values passed during invocation to flexibly adjust the Agent's behavior.

### Main Features

1. **Define Parameters**: Users create custom parameters for the Agent, such as strings, integers, etc., to specify different inputs required for the task.
2. **Dynamic Filling**: The caller passes parameter values based on their needs, affecting the logic and results of task execution.
3. **Subsequent Use**: The passed parameter values can be used as prompts or variables during task execution, ensuring the Agent generates personalized responses.
4. **Default Values and Validation**: If parameters are not provided, the Agent uses default values and performs parameter validation to ensure correctness.

### Use Cases

* **Task Management**: Dynamically adjust execution based on task priority and time.
* **Notification System**: Determine the notification method and recipient based on the passed parameters.
* **Report Generation**: Generate customized reports based on date ranges and types.

## Node Properties

* **Sensitive**: Sets the node as sensitive, causing the process to pause before this node is executed, awaiting manual confirmation before continuing. See [Human-in-the-Loop](/docs/ai/xpert/human-in-the-loop).
* **End Point**: Sets the node as the endpoint, indicating the end of the process. Once this node completes execution, the flow ends and returns to the caller. See [Execution Endpoint](../terminal/).
* **Disable Output**: Disables the output of this Agent node to the user dialog box.
* **Parallel Tool Invocation**: Allows the Agent node to invoke multiple tools in parallel, improving task execution efficiency (only supported by some LLMs, such as OpenAI).

## Message History

When the message history feature is enabled, the Agent node uses the data from the message history during execution to better understand the user's intent and context, improving task accuracy and intelligence.

If message history is not enabled, users can add custom "human" messages to simulate user input, helping the Agent node perform tasks.

## Structured Output

Users can define structured output for the Agent node to return task execution results in a specific format for easier processing and analysis. Structured output only works when the Agent node does not use sub-agents, tools, or knowledge base calls, and not all models support structured output.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/structured-output.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=79f23bcebe2cf9dfbacb088211b2142c" alt="Structured output" width="1832" height="1570" data-path="public/img/ai/workflow/structured-output.png" />

## Write to Memory

Customize the writing of the Agent node's output to memory ([session variables](/docs/ai/workflow/variables/)) for use in subsequent flow nodes.


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
