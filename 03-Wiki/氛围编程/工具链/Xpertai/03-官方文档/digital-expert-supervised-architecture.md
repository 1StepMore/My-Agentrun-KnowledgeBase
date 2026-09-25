---
title: Supervisor Architecture
keywords:
- XpertAI
- AI-Agent
- documentation
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/supervised-architecture.md
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
