---
title: Tool Invocation
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
# Tool Invocation

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool Invocation

In the XpertAI workflow system, the **Tool Node** invokes external capabilities and services, supporting data processing, system integration, and MCP tool invocation. It seamlessly integrates complex logic and third-party system capabilities into automated workflows.

## Tool Types Overview

Tool nodes support three access methods:

* **Built-in Tools**: Provided by XpertAI, ready to use, some require authorization before first use.
* **Custom Tools**: Users can import via standard interfaces (e.g., OpenAPI/Swagger/OData) or manually configure for enterprise systems or proprietary services.
* **MCP Tools**: Highly customizable for complex business logic or asynchronous tasks, using existing modules or custom development.

> ✅ All tools can be created and managed in the “XpertAI → Workspace → Tools” menu.

## Tool Node Parameter Configuration

Configure tool selection and parameters in the **Properties Panel**:

1. **Add Tool Node**\
   Insert a “Tool” node in the workflow canvas.

2. **Select Tool Set and Tool**\
   In the properties panel, choose:
   * **Tool Set** (created tool set)
   * **Tool** (specific tool within the set)

3. **Configure Input Parameter Variables**\
   Tools require input parameters (e.g., user ID, keywords, time range). Use workflow state variables, such as:

   ```text theme={null}
   User input → ${human.input}
   Current time → ${sys.datetime}
   Previous node output → ${<node_name>.result}
   ```

   * Check parameter format via “Copy Parameter Example.”
   * Use `{{variable}}` syntax for references.

4. **Output Handling (Optional)**\
   Tool results are available as variables for downstream nodes (e.g., `${<tool_name>.text}`). Map specific fields as needed.

## Advanced Feature: Error Handling

To ensure workflow stability, tool nodes support **error handling configuration**:

* Enable the “Error Handling” toggle to create an exception branch (Catch).
* Add fallback nodes in the exception branch, such as:
  * Send error alerts
  * Return default data
  * Log and terminate the workflow

This prevents workflow interruptions due to third-party service failures.

## Application Examples

* Use custom tools to fetch order info from ERP systems.
* Use MCP tools to sync data to a data platform.

## Tips

* Ensure tools are created and tested before use.
* Use workflow variables for input parameters to enhance generality and reusability.
* Enable error handling for critical calls to ensure workflow robustness.


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
