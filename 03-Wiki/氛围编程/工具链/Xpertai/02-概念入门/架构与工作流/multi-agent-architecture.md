---
keywords:
- XpertAI
- Multi-Agent
title: Multi-Agent Architectures
state:
  phase: wiki
  time_raw: '2026-07-01T12:47:59'
  time_draft: '2026-07-01T12:47:59'
  time_wiki: '2026-07-01T12:47:59'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/multi-agent-architecture.md
related:
- '[[B01-多智能体架构蜂群模式与监督模式]]'
- '[[workflow-and-agent]]'
- '[[swarm-architecture]]'
- '[[Supervisor Architecture]]'
- '[[digital-expert-swarm-architecture]]'
- '[[Supervisor Architecture]]'
notes: 本页含 swarm-architecture / supervised-architecture 的**摘要级**补充；完整官方文档见 [[digital-expert-swarm-architecture]]、[[Supervisor Architecture]]
source: 历史文件，来源见 sources
evidence: E1
---

# Multi-Agent Architectures

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-Agent Architectures

**Agent systems** leverage large language models (LLMs) to determine application control flow. However, as system complexity increases, managing and scaling these systems can become challenging. For instance, you may encounter the following issues:

* **Tool selection complexity**: The abundance of tools available to agents makes it inefficient to determine which tool to invoke next.
* **Context management difficulties**: A single agent may struggle to handle complex contextual information effectively.
* **Specialization requirements**: The system may require expertise in various specialized domains, such as planning, research, or mathematics.

To address these challenges, applications can be decomposed into smaller, independent agents and integrated into a **multi-agent system**. These individual agents can range from simple setups with just a single prompt and an LLM call to advanced architectures like ReAct agents.

Key advantages of adopting a multi-agent system include:

* **Modularity**: Breaking functionalities into independent agents simplifies development, testing, and maintenance, enhancing system flexibility.
* **Specialization**: Creating domain-specific expert agents improves overall system performance and efficiency.
* **Controllability**: Communication between agents can be explicitly managed without relying on implicit mechanisms like function calls.

Multi-agent systems empower businesses to address complex scenarios, enhance scalability, and achieve specialized capabilities, thereby better supporting business objectives.

## Multi-Agent Architectures

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/multi-agent-architectures.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=97af731b7d24f9e7cea2248f9ea7ca18" alt="Set as sensitive" width="1492" height="1226" data-path="public/img/ai/multi-agent-architectures.png" />

In a multi-agent system, agents can be connected and coordinated in various ways, with the choice of architecture depending on business needs and application scenarios. Common multi-agent architecture patterns include:

1. **Network Architecture**
   * Each agent can communicate with all other agents.
   * Any agent can autonomously determine the target agent to invoke next.
   * Suitable for decentralized, high-flexibility scenarios.

2. **Supervisor Architecture**
   * Each agent communicates only with a **supervisor agent**.
   * The supervisor agent makes decisions and determines the next agent to invoke.
   * Ideal for centralized management and clear decision-making logic.

3. **Hierarchical Architecture**
   * Builds on the supervisor architecture by introducing **multi-level supervisor agents**, creating a hierarchy.
   * Supports complex control flows and modular management for multi-level business logic.

4. **Custom Multi-Agent Workflows**
   * Each agent communicates only with specific subsets of other agents.
   * Some workflows are deterministic, while some agents autonomously decide their next targets.
   * Highly flexible, suitable for specific logic or complex business rules.

By selecting the appropriate architecture, multi-agent systems can optimize coordination efficiency and execution performance, addressing the demands of complex business scenarios while improving scalability and reliability.

## Digital Expert Systems

Our **digital expert system** employs a **hierarchical architecture**, creating an efficient and scalable multi-agent system. Each digital expert within this system is itself a hierarchical multi-agent system. Here are the core reasons we chose this architecture:

### 1. **Adaptability to Complex Business Needs**

The hierarchical architecture introduces multi-level supervisor agents to handle multi-layered logic requirements in complex business scenarios. Each level focuses on specific tasks, with higher-level supervisors coordinating the overall system, enabling flexible handling of task decomposition, resource allocation, and workflow management.

### 2. **Enhanced Modularity and Maintainability**

The system is divided into clear hierarchical levels, with well-defined functions and responsibilities. This modular design simplifies development, testing, and maintenance, supporting rapid iteration and feature expansion.

### 3. **Improved Decision Efficiency and Control**

By incorporating supervisor agents and multi-level control, the system coordinates agent behavior across levels, reducing unnecessary communication and redundant decisions. This boosts decision efficiency and ensures system actions align with global objectives.

### 4. **Support for Specialization and Collaboration**

In the hierarchical architecture, each level can specialize in specific domains or tasks—for example, one level might handle data processing while another focuses on business logic optimization. Collaboration across levels enhances overall system performance and ensures domain-specific expertise.

### 5. **Scalability to Meet Business Growth**

As business requirements evolve, the hierarchical architecture can easily scale horizontally or vertically by adding or adjusting supervisor agents, meeting diverse future needs.

Our choice of a hierarchical architecture reflects our deep understanding of complex business scenarios and organizational requirements. This architecture enables our digital expert system to effectively solve complex problems, offering flexibility, stability, and scalability in real-world applications, ultimately driving greater value for businesses.

* [https://langchain-ai.github.io/langgraphjs/concepts/multi\_agent/](https://langchain-ai.github.io/langgraphjs/concepts/multi_agent/)

---

## Swarm Architecture（补充）

# Swarm

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

---

## Supervisor Architecture（补充）

# Supervisor Architecture

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Supervisor Architecture

The core of the Supervisor architecture is a single supervisor that interacts with users and manages multiple specialized worker agents. These worker agents each have their own strengths, focusing on specific types of tasks. The supervisor acts like a conductor, receiving user requests, analyzing their needs, and assigning tasks to the appropriate specialized agents. Once the tasks are completed, the supervisor gathers the results from these agents, consolidates the information, and delivers the final answer to the user.

To illustrate with a simple example: suppose you want to know the total number of employees across several companies in a given year. The supervisor would first assign the task of "finding employee data for each company" to a research expert. After the data is collected, it would then assign the task of "calculating the total" to a math expert, before finally combining the results and responding to you. This division of labor allows complex problems to be broken down and resolved efficiently.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/supervisor-agents.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=b9c34d4b11a7d81ef2fd952a73065387" alt="Supervisor Agent Architecture" width="1712" height="1320" data-path="public/img/ai/xpert/supervisor-agents.png" />

<Info>
  Compare with [Swarm Architecture](/docs/ai/xpert/swarm/)
</Info>

## Detailed Workflow

The workflow of the Supervisor architecture is clear and structured. Using the earlier example:

1. **Task Reception**: After the user poses a question, the supervisor first receives and interprets the request.
2. **Task Assignment**: The supervisor decides which specialized agent to assign the task to based on its nature. For instance, if data collection is involved, it selects the research expert.
3. **Specialized Processing**: The research expert uses its capabilities (e.g., search tools) to gather the required information and returns the results to the supervisor.
4. **Further Collaboration**: After reviewing the results, if calculations are needed, the supervisor hands the data to the math expert. The math expert computes the total and returns it.
5. **Result Integration**: The supervisor collects the outputs from all agents, organizes them into a final answer, and delivers it to the user.

Throughout this process, the supervisor maintains overall control, ensuring tasks progress step-by-step, while each agent focuses on its area of expertise.

## Core Concepts: Agents and Handoffs

The Supervisor architecture relies on two key concepts:

* **Agents**: Each agent is an independent work unit with specific capabilities. They can range from simple data processors to more complex task executors. The supervisor itself is a special type of agent, responsible for coordination and decision-making.
* **Handoffs**: This is the mechanism for transferring control within the system. When the supervisor switches tasks between agents, it performs a handoff and decides what information to pass along. For example, it might choose to share only the final result or include the full processing history. This flexibility makes the system both efficient and controllable.

## Advantages and Scalability of the Architecture

The Supervisor architecture’s strengths lie in its modularity and collaboration. Each agent focuses on a single task, reducing system complexity, while the supervisor’s coordination ensures result accuracy. Moreover, this architecture is scalable: you can create multi-level agent hierarchies. For instance, multiple teams could each have their own supervisor for internal coordination, while a top-level supervisor oversees all teams, forming a more intricate collaborative network.

## Conclusion

The Supervisor architecture offers an elegant and efficient solution for designing multi-agent systems. Through clear role division and flexible handoff mechanisms, it breaks down complex tasks into manageable parts, ultimately providing users with concise and accurate answers. Whether you’re a tech enthusiast or a developer, this architecture is worth exploring. Hopefully, it inspires further thought and experimentation with multi-agent systems!

* Reference template: [Supervisor](https://app.xpertai.cn/explore?search=Supervisor).
* [LangGraph Multi-Agent Supervisor](https://github.com/langchain-ai/langgraphjs/tree/main/libs/langgraph-supervisor)
