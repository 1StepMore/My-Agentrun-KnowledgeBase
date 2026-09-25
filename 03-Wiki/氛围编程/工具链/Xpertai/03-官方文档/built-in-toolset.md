---
title: Built-in Toolsets
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/toolset/built-in-toolset.md
---
# Built-in Toolsets

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in Toolsets

The built-in tools provide out-of-the-box functionality. You can directly use the first-party built-in tools offered by the Xpert ecosystem.

## How to Configure Built-in Tools?

Simply select a built-in toolset in the workspace, add the necessary authorization information, and enable the tools you need. Once configured, they can be used within the AI agent. Users can also click the test button to manually test the tools.

<figure className="Large">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/xpertai/img/ai/xpert-toolset-builtin-auth.png" alt="Builtin Toolset authorization" className="rounded-xl shadow-md" />

  <figcaption>Built-in Toolset Authorization</figcaption>
</figure>

The current built-in toolsets include the following:

| Tool Name         | Description                                                           | Status         |
| ----------------- | --------------------------------------------------------------------- | -------------- |
| **TavilySearch**  | A tool focused on domain-specific information retrieval.              | Enabled        |
| **DuckDuckGo**    | A privacy-friendly search engine supporting web searches.             | In Development |
| **Wikipedia**     | Access to Wikipedia for rich encyclopedia information.                | In Development |
| **SearchApi**     | A general search API integrating multiple search services.            | In Development |
| **ExaSearch**     | Offers integration and comparison of various search engines.          | In Development |
| **SearxngSearch** | An open-source meta-search engine supporting multiple search queries. | In Development |
| **BingSearch**    | Bing search engine supporting online queries.                         | In Development |

## Data Analysis Platform Toolset

In addition to commonly used toolsets, Xpert also provides analysis toolsets seamlessly integrated with its data analysis platform:

| Tool Name  | Description                                                                         | Status  |
| ---------- | ----------------------------------------------------------------------------------- | ------- |
| **ChatBI** | A ChatBI toolset for conversational analysis and presentation with semantic models. | Enabled |
| **ChatDB** | A ChatDB toolset for conversational data analysis directly with database tables.    | Enabled |

For more details, see [Data Analysis Toolset](../data/).
