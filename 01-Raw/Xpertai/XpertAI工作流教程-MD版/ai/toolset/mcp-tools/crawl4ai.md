---
title: Crawl4AI
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
# Crawl4AI

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Crawl4AI

[Crawl4AI](https://docs.crawl4ai.com/): Open-source LLM-friendly web crawler and scraping tool.

## Configuring a Crawl4AI MCP Tool Instance

On the XpertAI platform, you can directly configure the built-in Crawl4AI MCP service as an **SSE-type MCP tool instance** for use by agents and workflows.

<Info>
  You can also find Crawl4AI in the MCP tool template marketplace and create it with one click.
</Info>

Configuration steps are as follows:

* **Configuration Example**
  When adding an MCP tool on the XpertAI platform, configure it as:

  ```yaml theme={null}
  type: sse
  url: "http://crawl4ai:11235/mcp/sse"
  name: crawl4ai
  ```

* **Usage**
  Once configured, agents or workflows can directly call the capabilities provided by the `crawl4ai` MCP tool (e.g., `md`, `html`, `screenshot`, `pdf`, `crawl`, `ask`, etc.) during orchestration.

## Use Cases

### Use Case 1: Automated Web Content Collection Agent ("Summary Bot")

**Objective**: Enable users to submit a webpage link through an intelligent agent to automatically retrieve a Markdown text summary of the page.

#### Key Steps

1. User inputs a link → The agent triggers the MCP's `md` tool to convert the target webpage into Markdown text.
2. The agent receives and displays the summary, and can further extract key content based on user needs.

#### Summary Illustration

```text theme={null}
User: Please summarize the main content of https://example.com.
Agent → Calls MCP tool `md` to retrieve content in Markdown format
Agent → Returns the summary to the user
```

### Use Case 2: Multimedia Content Capture and Analysis Workflow ("Report Generator")

**Objective**: After a user inputs a target URL, the agent automatically captures a webpage screenshot and PDF, and generates a final report on the XpertAI platform.

#### Implementation Steps

1. User inputs a link → The agent sequentially calls:
   * `screenshot`: Generates a webpage screenshot
   * `pdf`: Exports the webpage as a PDF
   * Optional: `ask` or `html` → Extracts structured text content
2. The agent compiles the screenshot, PDF, and text into a shareable report.

#### Workflow Illustration

```text theme={null}
User: Please capture the https://example.com page and generate a report.
→ Agent calls MCP:
   1⃣ Calls `screenshot` to obtain a page screenshot
   2⃣ Calls `pdf` to obtain a page PDF
   3⃣ Optional: Calls `ask`/`html` to retrieve structured text or Markdown

Agent: Below are the page screenshot and PDF file, with the extracted summary as follows... (displays content)
```

## Cross-Scenario Common Configuration Notes

* **MCP Tool List**

  | Tool Name    | Function Description                           |
  | ------------ | ---------------------------------------------- |
  | `md`         | Generates page content in Markdown             |
  | `html`       | Extracts preprocessed HTML                     |
  | `screenshot` | Captures a full-page screenshot (PNG)          |
  | `pdf`        | Exports the page as a PDF document             |
  | `execute_js` | Executes custom JavaScript in the page context |
  | `crawl`      | Crawls multiple URLs                           |
  | `ask`        | Queries the indexed library context            |

* For more tool parameters and usage, visit:

  [https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support](https://docs.crawl4ai.com/core/docker-deployment/#mcp-model-context-protocol-support)


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
