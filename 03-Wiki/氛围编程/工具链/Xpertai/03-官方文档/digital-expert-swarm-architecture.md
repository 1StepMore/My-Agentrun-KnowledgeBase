---
title: Swarm
keywords:
- XpertAI
- AI-Agent
- documentation
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/swarm-architecture.md
state:
  phase: wiki
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
related: []
source: 历史文件，来源见 sources
evidence: E1
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Swarm

Create a clustered multi-agent system. **Swarm** is a multi-agent architecture where agents dynamically hand over control to one another based on their respective expertise. The system remembers which agent was last active, ensuring that subsequent interactions continue with that agent.

<Tip>
  **Core Concept of Swarm Mode**

  Agents can pass requests to each other and share state (memory).
</Tip>

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/swarm-agents.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=6dc29b34226f6a8f21d0a201882b5a34" alt="Swarm Agents" width="2910" height="1620" data-path="public/img/ai/xpert/swarm-agents.png" />

<Info>
  Comparison [Supervisor Architecture](/docs/ai/xpert/supervisor/)
</Info>

## How to Orchestrate

To implement the swarm mode in XpertAI digital expert agents, simply add call connections from sub-agents to the main agent to switch to swarm mode, while the Supervisor working mode remains available.

* The large model selected must have tool-calling capabilities.

## Prompt Design

When setting prompts for a combination of agents in swarm mode, pay attention to the following points:

* The prompt should clearly specify which tasks are handed over to which agent.
* The prompt should indicate that control can only be transferred to one agent at a time, avoiding simultaneous transfers to multiple agents.

## Conversation

In the user conversation interface, you can directly interact with the entire digital expert system. The main agent will first receive the user’s message, process it, or pass it to other agent members within the swarm, and so on. The roles of agent members within the swarm are equal (in contrast to the Supervisor mode, where sub-agents must return processed messages to the Supervisor agent, which then decides the next step in the conversation or whether it can end).

<img src="https://mintcdn.com/xpertai/ZGpPZkKu2RpKGlB0/public/img/ai/xpert/swarm-chat.png?fit=max&auto=format&n=ZGpPZkKu2RpKGlB0&q=85&s=0b861af627ac7e89e4f39a3075d3c47f" alt="Conversational Swarm Agents" width="2870" height="1600" data-path="public/img/ai/xpert/swarm-chat.png" />

* Reference template [Customer Support Swarm](https://app.xpertai.cn/explore?search=Customer%20Support%20Swarm).
* [LangGraph Multi-Agent Swarm](https://github.com/langchain-ai/langgraph-swarm-py)
