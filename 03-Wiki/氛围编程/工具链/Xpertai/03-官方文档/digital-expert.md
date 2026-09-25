---
keywords:
- XpertAI
- AI-Agent
title: 🧑🏼‍🚀 Xpert
state:
  phase: wiki
  time_raw: '2026-07-01T12:47:59'
  time_draft: '2026-07-01T12:47:59'
  time_wiki: '2026-07-01T12:47:59'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/digital-expert.md
related:
- '[[multi-agent-architecture]]'
- '[[agent]]'
- '[[knowledgebase]]'
source: 历史文件，来源见 sources
evidence: E1
---

# 🧑🏼‍🚀 Xpert

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 🧑🏼‍🚀 Xpert

## What is Xpert?

Xpert is a system that uses large language models as its foundation to simulate human social behaviors by combining intelligent agents. It applies the best practices of human society to AI agent behavior, enhancing and standardizing AI's capability to serve real-world scenarios effectively.

Xpert is categorized into two types: **Agent** and **Copilot**:

* **Agent Xpert**: These are expert agents designed to coordinate multiple agents working together to accomplish tasks. They simulate organizational structures found in human societies, maximizing the use of available human resources (via toolsets) and experiences (through organizational strategies) to better serve humanity.

* **Copilot Xpert**: These are expert assistant agents that use large language models to collaborate with humans in utilizing tools to complete tasks. This represents a best practice in human-machine collaboration.

## Where to Build Xpert?

Xpert and its related toolsets are developed within a workspace. This workspace organizes Xperts, toolsets, and access permissions, allowing workspace members to collaboratively edit and use the resources within it.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-workspace.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=60d44a781249f440fa67faf93af8d52d" alt="Xpert workspace" width="3024" height="1714" data-path="public/img/ai/xpert-workspace.png" />

## How to Orchestrate Xpert Agents?

Once an Agent Xpert is created, you can orchestrate agents on the **Agents** page in Xpert Studio. The orchestration process mirrors hierarchical structures in human society: higher-level agents plan, divide, and assign tasks to lower-level agents. The lower-level agents solve problems using toolsets or knowledge bases and report back to their higher-level agents, who integrate the results to make further decisions.

Agent operation follows this principle, and the orchestration adheres to the same methodology.

Each agent node can have unique toolsets and knowledge bases based on its responsibilities and may utilize different capabilities of large language models.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-studio.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=8c81c5cf9d96324c0acc1e55fd118bec" alt="Xpert studio" width="1814" height="1028" data-path="public/img/ai/xpert-studio.png" />

## How to Use Tools?

The use of tools marks a significant milestone in human evolution, and large language models that can utilize tools are a key step toward achieving AGI (Artificial General Intelligence).

To enable an agent to use tools:

1. **Authorize the tools**: This includes configuring authorization for built-in tools or creating custom toolsets via APIs.
2. **Assign toolsets to agents**: After authorization, the toolset instances can be added to agent nodes for use.

Additionally, if an Xpert agent needs to access an enterprise's proprietary systems, custom toolsets can be configured for this purpose.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-toolset-builtin-auth.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=91e0712e436b23002df3085cab7d4391" alt="Xpert toolset" width="1512" height="857" data-path="public/img/ai/xpert-toolset-builtin-auth.png" />

## How to Retrieve Knowledge Bases?

The [🎓Knowledge Base](../knowledge/) is the core support for AI agents. It provides background knowledge and domain-specific data, enabling agents to:

* Better understand user intent
* Solve problems effectively
* Optimize decision-making
* Enhance contextual comprehension
* Reduce generation bias

Dynamic updates to the knowledge base ensure that agents are always equipped with the latest information, significantly improving dialogue accuracy and intelligence.

To use a knowledge base, add it to Xpert Studio and link the knowledge base node to an agent node. The agent will then have access to the information within this knowledge base.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-agent-run-with-kb.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=05433bd52a69dbcdf92595c697a915aa" alt="Xpert with knowledgebase" width="3024" height="1710" data-path="public/img/ai/xpert-agent-run-with-kb.png" />

## What is Copilot?

**Copilot Xpert** helps users quickly operate interface functions, improving their expertise and work efficiency.

To set up a Copilot Xpert:

1. Create a Copilot Xpert in Xpert Studio.
2. Upload knowledge examples related to the expert's role. These examples are stored in a vector database, allowing the Copilot to retrieve relevant answers based on user queries.

Once created, the Copilot Xpert can be selected as a business role in the Copilot. During execution, the Copilot retrieves example answers based on commands and roles to operate interface functions more accurately.

For example, Xpert **Financial BP** can retrieve answers and create dimension objects based on the command `/dimension`.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert-copilot-example-testing.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=c2c6fc6af0a92e66d1881ce13dcb72fd" alt="Xpert Copilot" width="1512" height="857" data-path="public/img/ai/xpert-copilot-example-testing.png" />

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/copilot-command-dimension-result.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=05d4e6dff64c37b5e98762ccc186f1dd" alt="Copilot command" width="3024" height="1714" data-path="public/img/ai/copilot-command-dimension-result.png" />

## Connect to different chat channels with triggers

For details on how a Digital Expert connects to different conversation channels through triggers, see:

* [Connect to different chat channels with triggers](./chat-channels/)
