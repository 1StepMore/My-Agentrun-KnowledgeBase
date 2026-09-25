---
title: MCP Tools
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
# MCP Tools

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# MCP Tools

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)

> MCP is an open protocol that standardizes how applications provide context to large language models (LLMs). Think of MCP as the USB-C port for AI applications. Just as USB-C provides a standardized way to connect various peripherals and accessories to your devices, MCP offers a standardized way for AI models to connect to different data sources and tools.

## Why Choose MCP?

MCP helps you build agents and complex workflows on top of large language models (LLMs). LLMs often need to integrate with data and tools, and MCP provides:

* A growing list of pre-built integrations that your LLM can directly access
* Flexibility to switch between LLM providers and vendors
* Best practices for securing data within your infrastructure

## How to Create?

In the Digital Expert workspace, select the MCP tool type and click the card to create a new MCP toolset.

As shown in the image below, fill in the required fields such as the name, enter the MCP service configuration into fields like commands and parameters, and click "Connect" to attempt loading the tool list with the current configuration.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/create-mcp-toolset.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=ab37da7ce39ec92671e0d9a01303d472" alt="Create MCP Toolset" width="2414" height="1360" data-path="public/img/ai/xpert/create-mcp-toolset.png" />

<Warning>
  **Security Warning**\
  In open-source code versions, MCP tools run using "commands" will trigger a security prompt: "Commands" are executed directly on the backend server, which may pose security risks. Upgrading to the **Pro** version ensures that "command" tools are securely run in a sandbox container.
</Warning>

After loading the MCP toolset’s tool list, users can enable or disable individual tools. You can also set "**Default Disabled Tools**," meaning tools not explicitly enabled will be turned off by default.

## Examples

* **Sequential Thinking**: An MCP server implementation that provides tools for dynamic and reflective problem-solving through a structured thinking process.

  ```json theme={null}
  {
    "mcpServers": {
      "sequential-thinking": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-sequential-thinking"
        ]
      }
    }
  }
  ```

* **Playwright**: A Model Context Protocol (MCP) server using Playwright to provide browser automation capabilities. This server enables large language models (LLMs) to interact with web pages through structured accessibility snapshots, without requiring screenshots or visually optimized models.

  ```json theme={null}
  {
    "mcpServers": {
      "playwright": {
        "transport": "stdio",
        "command": "npx",
        "args": [
          "-y",
          "@playwright/mcp@latest",
          "--headless"
        ]
      }
    }
  }
  ```

* **Blender**: BlenderMCP connects Blender to Claude AI via the Model Context Protocol (MCP), allowing Claude to directly interact with and control Blender. This integration supports prompt-based 3D modeling, scene creation, and manipulation.

  ```json theme={null}
  {
    "mcpServers": {
      "blender": {
        "command": "uvx",
        "args": [
          "blender-mcp"
        ]
      }
    }
  }
  ```

* More at [MCP.so](https://mcp.so/)

## Transport Protocols

MCP (Model Context Protocol) has two primary communication modes: Standard Input/Output (stdio) command mode and HTTP Server-Sent Events (SSE) mode.

### Standard Input/Output Mode

This is the standard input/output communication mode, running the server as a local process and interacting via standard input (stdin) and standard output (stdout). It’s suitable for development and testing scenarios, requiring no network connection.

### HTTP SSE Mode

This is the remote communication mode, where the client connects to the server’s HTTP endpoint, receiving real-time events via SSE and sending commands via HTTP POST. It’s ideal for applications requiring remote access and real-time data streaming.

### Mode Comparison

The table below summarizes the differences between the two modes to help understand their use cases and characteristics:

| **Feature**       | **Standard Input/Output Mode**         | **HTTP SSE Mode**                             |
| ----------------- | -------------------------------------- | --------------------------------------------- |
| **Communication** | Local stdin/stdout                     | HTTP POST (commands) + SSE (events)           |
| **Use Case**      | Local development, testing             | Remote access, real-time data streaming       |
| **Network Needs** | Local server network                   | Connects to other servers via network         |
| **Real-Time**     | Synchronous, suitable for blocking ops | Asynchronous, supports real-time event push   |
| **Security**      | Local ops, lower network risks         | Requires network authentication/authorization |
| **Example Tools** | Quarkus MCP stdio extension            | Supergateway, Cloudflare remote deployment    |

## Code MCP Tools

Code MCP tools offer a more flexible approach, allowing users to write backend logic code for MCP tools directly online and run it using the MCP protocol. This enables developers to call external APIs, perform logic processing, and more without deploying servers or building full projects, greatly enhancing the scalability and efficiency of MCP tools.

When creating an MCP tool, select the “Code” type to access the online editor page. The editor supports Python syntax (with JavaScript support planned) and provides basic templates for quick starts.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/mcp-code-type.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=f1fe571f108cb7d6c86b2435946d72de" alt="MCP Code Tool" width="2412" height="1362" data-path="public/img/ai/xpert/mcp-code-type.png" />

### Development Experience

Code MCP tools are essentially custom-implemented MCP server code, hosted and run by the system in a sandbox container, automatically exposing MCP-compliant interfaces. You can focus on writing business logic, including but not limited to:

* Calling third-party APIs, such as weather queries, stock market data, or translation services
* Interfacing with internal enterprise systems like ERP or CRM
* Implementing data processing logic, such as format conversion, filtering, or aggregation
* Converting structured inputs to natural language outputs, or vice versa

### Debugging and Testing

* The editor includes a testing panel to simulate parameter calls, enabling real-time debugging of tool logic.
* All runtime environments are isolated sandbox containers, ensuring secure execution.

### Multi-Tool Support

A single code MCP tool can register multiple MCP tools using multiple `@mcp.tool()` decorators. The system automatically recognizes and generates a tool list for model invocation.

## MCP Tools Marketplace

The MCP Tools Marketplace offers a rich set of tool integration modules, enabling users to quickly extend model perception and action capabilities without writing complex code. With one-click installation, you can add various MCP tools to your agent’s toolset, instantly enabling external data retrieval, third-party service calls, and data processing.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/mcp-marketplace.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=34ce859ddcd686bec122e89dff52567f" alt="MCP Marketplace" width="2820" height="1602" data-path="public/img/ai/xpert/mcp-marketplace.png" />

### Diverse Tool Categories for Various Scenarios

The MCP Tools Marketplace supports multiple tool types, covering the following typical use cases:

* **Agent Support**: Tools like `Sequential Thinking` provide structured reasoning chains, supporting multi-step reasoning and task planning for agents.
* **System Tools**: Tools like `Memory Server` offer runtime data caching and context state management, supporting continuous conversation memory for AI systems.
* **Browser Operations**: Tools like `Playwright MCP` support browser automation for tasks like web scraping and login operations.
* **Map Services**: Tools like `Baidu Map` and `AMap` are MCP-compatible, supporting coordinate resolution and route planning.
* **Utility Tools**: Tools like `Time MCP Server` support timezone conversion, `Fetch` enables web content retrieval and conversion, and `Firecrawl` supports advanced crawling.
* **Document Processing**: Tools like `Perplexity` enable document Q\&A and search engine access, while `GitHub MCP` supports repository searches and code reading.
* **Dify Tool Integration**: Includes `Dify Knowledgebase`, `Dify Workflow`, `Dify Chatflow`, and more, offering seamless integration with the Dify platform.

### Diverse Tool Formats: SSE, Stdio, and Code

Each MCP tool supports the following formats:

* **SSE**: Configures existing SSE interface MCP tool services.
* **Studio Tools (STUDIO)**: Uploaded, hosted, and registered by developers in the official MCP service, ready for direct user installation.
* **Code Tools (CODE)**: Custom-created by developers within the platform using online code, offering greater flexibility for enterprise-specific tools.

### Quick Activation and Search

* Filter tools quickly by category (e.g., Agent, Workflow, Utils, Analysis).
* Support for keyword search and tag navigation to locate tools efficiently.
* Tool pages display details like call frequency, developer, supported tags, and parameters for easy selection.

***

The MCP Tools Marketplace ensures that AI agent capabilities are no longer limited to the model itself but can connect to business systems, data services, and the real world through a rich tool ecosystem. In the future, it will support more community and enterprise developers to join the ecosystem, further enriching the toolset and enhancing the practical effectiveness of AI agents.


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
