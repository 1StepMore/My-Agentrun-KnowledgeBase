---
title: 'Agentic BI: Agent Team for End-to-End Data Analysis'
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
# Agentic BI: Agent Team for End-to-End Data Analysis

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Agentic BI: Agent Team for End-to-End Data Analysis

In traditional BI tools, data analysis means repeatedly building models, dragging charts, and manually interpreting results—a typical *human-driven* process. But in **Xpert Agentic BI**, everything is led by AI agents: they understand your language, grasp business indicators, spot trends, and automatically execute the entire analysis task.

## 💡 What Is Agentic BI?

**Agentic BI** (Agent-Driven Business Intelligence) is a new BI paradigm for the AI era. It embeds **AI agents** into the full data analysis lifecycle, enabling the system to understand, plan, and act—achieving true automation and intelligent decision support.

In traditional BI, users must manually model, configure reports, write formulas, and interpret charts. In Agentic BI:

* 🧠 **AI agents become the core analysts**: Just describe your business problem in natural language, and the agent understands your intent, constructs the analysis path, and executes it.
* 🔧 **Agents can call toolsets**: such as semantic modeling tools, indicator management tools, etc., to automate querying, calculation, interpretation, and recommendations.
* 🔁 **Analysis is no longer a one-time result**: it becomes a continuous dialogue, supporting follow-ups, refinement, and iterative thinking—realizing human-machine collaborative analysis.

## 🔧 Overview of Currently Available Features

| Module                                                          | Function Summary                                                                                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [**Semantic Modeling Toolset**](/docs/ai/tool/bi/modeling)      | Builds the semantic layer for indicator analysis: domains, subdomains, facts, dimensions, and their relationships              |
| [**Indicator Management Toolset**](/docs/ai/tool/bi/indicators) | Defines and manages business indicators: supports multi-level indicator breakdowns, formula configuration, source traceability |
| [**ChatBI Toolset**](/docs/ai/tool/chatbi/)                     | Natural language conversational analysis: supports multi-turn Q\&A, context tracking, intelligent suggestions                  |
| ❌ Dashboard Toolset (Coming Soon)                               | Used to create interactive charts and dashboards, not yet available                                                            |
| ❌ Data Governance Toolset (Coming Soon)                         | For field quality, indicator consistency, permission governance, not yet available                                             |

***

## 🚀 Quick Start: 3 Steps to Activate Agentic BI

### Step 1: Create a Digital Expert Workspace

Go to any [Digital Expert interface](/docs/ai/xpert/) and click “Create Workspace.” This space will host your semantic models, indicator system, business data, and agent conversation context—it’s the core container of Agentic BI.

### Step 2: Instantiate Toolsets

Within the workspace, click “Add Toolset” and choose from the available ones:

* **Semantic Model Toolset**: Define business entities, dimensions, measures, etc.
* **Indicator Management Toolset**: Build and maintain key business indicators, define definitions, statistical rules, and business domains.

### Step 3: Create an Agent and Bind Toolsets

Click “Add Agent,” choose a Digital Expert template (like “Financial Analyst” or “Market Insight Assistant”), and bind it to your configured toolsets.

Once published, your Agentic BI agent is ready to go and can:

* 📊 Create semantic models via conversation
* 📌 Define and refine indicators via natural language
* 📈 Analyze business using models and indicators
* 🧠 Perform multi-turn reasoning and generate suggestions

## 🔍 Live Demo: What Can Agentic BI Do?

Here are some example natural language interactions:

**Modeling:**

> "Create a semantic model for sales orders with fields: customer, product, sale date, and sale amount."

**Indicators:**

> "Add a indicator called 'Monthly YoY Growth Rate' to calculate the sales amount year-over-year percentage change."

**Analysis:**

> "Show me the sales trend for East China by product line over the past 3 months, displayed monthly."

**Planning:**

> "We're preparing a gross margin analysis—please draft a indicator evaluation and analysis path."

## 🤝 Multi-Agent Collaboration: Role-Based Analysis

Add multiple digital experts (agents) to a project for role-based collaborative analysis:

* **Market Strategy Assistant** → User data analysis and segmentation
* **Sales Forecast Expert** → Trend prediction and planning recommendations
* **Financial Analyst** → Cost structure optimization and P\&L analysis

Agents share the same semantic model and indicator system, achieving true context synchronization and multi-perspective collaboration.

***

## 🧩 Use Case Examples

| Business Scenario          | How Agentic BI Helps                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Sales Forecasting          | Uses indicators like “Order Growth Rate” and “Projected Sales” to auto-generate trend graphs and textual explanations                      |
| Budget Tracking            | Defines semantic models by project domain and performs traceable analysis of budget indicators                                             |
| Regional Comparison        | Automatically identifies indicator differences between regions and generates visualizations and insights                                   |
| Business Anomaly Detection | Detects abnormal fluctuations in key indicators, traces back to dimensions/fields/raw data to assist problem diagnosis and decision-making |

***

## ✅ Why Choose Agentic BI?

| Capability               | Traditional BI Tools     | Xpert Agentic BI                                                        |
| ------------------------ | ------------------------ | ----------------------------------------------------------------------- |
| Data Modeling            | Manual, repetitive setup | Visual semantic modeling, structured indicator system                   |
| Natural Language Q\&A    | Not supported            | Built-in semantic understanding maps questions to indicators/dimensions |
| Analysis Execution       | Manual charts & reports  | Agents generate insights and recommendations automatically              |
| Multi-Role Collaboration | Not supported            | Multiple agents can share context and collaborate with role delegation  |
| Logic Reusability        | Not available            | indicators and models are reusable and cross-project applicable         |

### 🔍 Agentic BI vs ChatBI (Text2SQL)

| Comparison Dimension         | **ChatBI (Text2SQL)**                                  | **Agentic BI**                                                                         |
| ---------------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| 🎯 **Core Capability**       | Translates natural language to SQL and returns results | Agent-centric: understands context, models, indicators, analysis paths                 |
| 🧠 **Agent Role**            | No agent concept, just a query engine                  | Agents are central: they reason, model, manage, and plan                               |
| 🛠 **Underlying Basis**      | Depends on existing DB/table structure                 | Semantic models build a business layer independent of tables                           |
| 📊 **Indicator Management**  | None; indicators must be described in queries          | Built-in indicator tools with reuse, traceability, version control                     |
| 🔁 **Context Understanding** | Single-turn Q\&A only                                  | Multi-turn deep conversation with reasoning and follow-ups                             |
| 🧩 **Analysis Chain**        | Executes SQL and returns raw result                    | Generates analysis plans, executes step-by-step with insights                          |
| 👥 **Multi-Agent Collab**    | Not supported                                          | Multiple agents collaborate, share context, divide tasks                               |
| 🧱 **Extensibility**         | Limited to SQL and visualization                       | Extensible with various toolchains (semantic models, indicators, visualizations, etc.) |
| 👨‍💼 **Target Users**       | Light/medium users, for self-service BI                | Complex, intelligent decision chains driven by business + data                         |

***

#### ✅ Example

**ChatBI** Question:

> “Query monthly sales for 2024.”
> 👉 Executes SQL and shows table/chart. No background understanding or indicator explanation.

**Agentic BI** Question:

> “How is our sales trend this year? Which product line contributed most?”
> 👉 Agent uses the semantic model to identify “sales,” applies indicator definitions, understands “trend” as time-series analysis, and supports follow-up questions like “which channel had more impact.” Fully contextual and explainable.

***

### 🧠 One-Sentence Summary of the Core Difference:

* **ChatBI is an enhanced query tool**—translating natural language into SQL.
* **Agentic BI is an intelligent analysis assistant**—it understands your question, builds analysis paths, invokes tools, explains results, offers suggestions, and even drives the next step.

***

## 🔜 What’s Coming Next?

We’re developing the following features—stay tuned:

* **Dashboard Toolset**: For drag-and-drop chart configuration and result presentation
* **Data Governance Toolset**: For consistency checks, field quality tracking, and permission control

## 🔗 Further Reading

* [Xpert Project Feature Overview](/docs/ai/chat/project/)
* [How to Build Your First Digital Expert](/docs/ai/xpert/)
* [About MCP Toolchain and Advanced Analytics](/docs/ai/tool/)


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
