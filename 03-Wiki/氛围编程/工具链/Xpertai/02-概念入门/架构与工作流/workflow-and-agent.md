---
keywords:
- XpertAI
- workflow
- Multi-Agent
title: Workflows and Agents
state:
  phase: wiki
  time_raw: '2026-07-01T12:47:59'
  time_draft: '2026-07-01T12:47:59'
  time_wiki: '2026-07-01T12:47:59'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/tutorial/workflow-and-agent.md
related:
- '[[multi-agent-architecture]]'
- '[[agent]]'
- '[[B01-多智能体架构蜂群模式与监督模式]]'
source: 历史文件，来源见 sources
evidence: E1
---

# Workflows and Agents

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Workflows and Agents

This guide reviews common patterns in agent systems. It may be helpful to distinguish between "workflow" and "agent" when describing these systems. Anthropic provides a good explanation of one way to think about this distinction:

> A workflow is a system that orchestrates large language models (LLMs) and tools through predefined code paths. An agent, on the other hand, is a system where the LLM dynamically directs its own process and tool usage, maintaining control over how the task is completed.

You can use any chat model that supports structured output and tool calls. Below, we show how to implement common agent system patterns on the Xpert AI platform.

## Building Block: Augmented LLM

LLMs have enhanced capabilities that support building workflows and agents. These include structured output and tool calls, as shown in this image from the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/effective-agents-augmented-llm.webp?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=0d06c7e69ebcb4dd6dda8027e7027818" alt="The augmented LLM" width="2401" height="1000" data-path="public/img/ai/workflow/effective-agents-augmented-llm.webp" />

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/xpert-augmented-llm.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=8a401f426fd15dda71d8c779c9037c0b" alt="Augmented LLM node" width="1182" height="978" data-path="public/img/ai/workflow/xpert-augmented-llm.png" />

## Prompt Chaining

In a prompt chain, each LLM call processes the output from the previous call.

As mentioned in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> A prompt chain breaks a task into a series of steps, where each LLM call processes the output of the previous one. You can add program checks at any intermediate step (see the "gate" in the image below) to ensure the process stays on track.
>
> When to use this workflow: This workflow is ideal for tasks that can be easily and clearly broken down into fixed sub-tasks. The main goal is to exchange higher accuracy for slightly higher latency by simplifying each LLM call.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/effective-agents-prompt-chaining.webp?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=8b39b6769c5584d6f713512a09232725" alt="Prompt chaining" width="2401" height="1000" data-path="public/img/ai/workflow/effective-agents-prompt-chaining.webp" />

On the Xpert AI platform, the prompt chain is implemented using agent nodes, routing, and responses. Note that if the routing executes the prompt chain to the final agent node, the stream output of the last agent can be returned to the user. If the route exits, the specified variable or content is returned to the user via the response node.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/xpert-prompt-chaining.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=1406c2c8468fb9cd6ee3bea526d25e65" alt="Prompt chaining" width="2176" height="688" data-path="public/img/ai/workflow/xpert-prompt-chaining.png" />

Reference Template: [Workflow Prompt Chaining](https://app.xpertai.cn/explore?search=Workflow%20Prompt%20Chaining).

## Parallelization

With parallelization, large language models can handle a task simultaneously:

> Large language models can sometimes handle a task simultaneously and aggregate their outputs programmatically. This workflow, called parallelization, comes in two key variants: segmentation (breaking a task into independent sub-tasks that run in parallel) and voting (running the same task multiple times to get diverse outputs).
>
> When to use this workflow: Parallelization is effective when sub-tasks can be processed in parallel to improve speed, or when multiple perspectives or attempts are needed to achieve more confident results. For complex tasks that involve multiple considerations, large language models often perform better when each consideration is handled by a separate model call, allowing for focused attention on each specific aspect.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/effective-agents-parallelization.webp?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=aff8f7b415af8547d19f21a418f49b8d" alt="Parallelization" width="2401" height="1000" data-path="public/img/ai/workflow/effective-agents-parallelization.webp" />

On the Xpert AI platform, you can implement parallelized agent workflows by directly adding multiple agent nodes as subsequent nodes. In addition to agent nodes supporting parallel subsequent points, **iteration** nodes also support parallelized subsequent nodes.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/xpert-parallelization.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=d80fcc3cb69fb2eef4b0682cc58e9307" alt="Parallelization agents" width="2068" height="1064" data-path="public/img/ai/workflow/xpert-parallelization.png" />

Reference Template: [Workflow Parallelization](https://app.xpertai.cn/explore?search=Workflow%20Parallelization).

## Routing

Routing classifies inputs and guides them to subsequent tasks. As mentioned in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> Routing classifies inputs and directs them to specialized subsequent tasks. This workflow allows for focus separation and the construction of more specialized prompts. Without it, optimizing for one type of input might impair performance for others.
>
> When to use this workflow: Routing is suitable for complex tasks where there are clearly different categories that should be handled separately, and classification can be accurately performed by a large language model or more traditional classification models/algorithms.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/effective-agents-routing.webp?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=0a010366faf60f812f4a0ac4e4fcd6f3" alt="Routing" width="2401" height="1000" data-path="public/img/ai/workflow/effective-agents-routing.webp" />

On the Xpert AI platform, the routing workflow can be implemented using [**conditional branches**](/docs/ai/workflow/if-else) by adding multiple conditions and assigning subsequent nodes to each condition.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/xpert-routing.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=637ace780c70a6fcefa29c01c7edd452" alt="Routing agents" width="2126" height="1238" data-path="public/img/ai/workflow/xpert-routing.png" />

Reference Template: [Workflow Routing](https://app.xpertai.cn/explore?search=Workflow%20Routing).

## Orchestrator-Worker

In the **orchestrator-worker** pattern, a coordinator breaks down tasks and delegates each sub-task to workers. As mentioned in the [Anthropic blog](https://www.anthropic.com/research/building-effective-agents):

> In an orchestrator-worker workflow, a central large language model dynamically breaks down a task, delegates it to worker large language models, and integrates their results.
>
> When to use this workflow: This workflow is ideal for complex tasks where the required sub-tasks cannot be predicted (e.g., in coding, the number of files that need changes and the nature of each change likely depend on the task). While similar to parallelization in topology, the key distinction lies in its flexibility—the sub-tasks are not predefined but are decided by the coordinator based on the specific input.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/effective-agents-orchestrator-worker.webp?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=18b2af9ae083f58ea5475da2244c2730" alt="Orchestrator-Worker" width="2401" height="1000" data-path="public/img/ai/workflow/effective-agents-orchestrator-worker.webp" />

On the Xpert AI platform, you can implement the orchestrator-worker agent workflow using [**iteration**](/docs/ai/workflow/iterating) logic nodes. The iteration node can process each element of an array by calling a sub-agent workflow, executing sequentially or concurrently (with a limit set) for each sub-task. After all elements are processed, the result array is returned, and subsequent nodes are executed.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/xpert-orchestrator-worker.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=3935d8116488f6f8d9de57b25d89cea4" alt="Orchestrator-Worker agents" width="1948" height="972" data-path="public/img/ai/workflow/xpert-orchestrator-worker.png" />

Reference Template: [Workflow Orchestrator-Worker](https://app.xpertai.cn/explore?search=Workflow%20Orchestrator-Worker).

## Evaluator-Optimizer

In an evaluator-optimizer workflow, one large language model (LLM) generates a response, and another provides evaluation and feedback in a loop:

> In the evaluator-optimizer workflow, one large language model (LLM) generates a response, while another provides evaluation and feedback in a loop.
>
> When to use this workflow: This workflow is especially effective when we have clear evaluation criteria, and iterative optimization provides measurable value. Two key indicators for using this process are: first, when human feedback significantly improves the LLM's responses; and second, when the LLM can provide such feedback. This is similar to the iterative writing process that human writers go through when refining a document.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/effective-agents-evaluator-optimizer.webp?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=6ee5277420a33741d96fc7aae5c9112d" alt="Evaluator-optimizer" width="2401" height="1000" data-path="public/img/ai/workflow/effective-agents-evaluator-optimizer.webp" />

On the Xpert AI platform, you can implement the evaluator-optimizer agent workflow by using the agent's [structured output](/docs/ai/workflow/agent#structured-output) along with [routing](/docs/ai/workflow/if-else) logic.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/xpert-evaluator-optimizer.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=253be03840661007716fd978b4d226b1" alt="Evaluator-optimizer" width="2688" height="508" data-path="public/img/ai/workflow/xpert-evaluator-optimizer.png" />

Reference Template: [Workflow Evaluator-Optimizer](https://app.xpertai.cn/explore?search=Workflow%20Evaluator-Optimizer).

## Conclusion

Success in the field of large language models is not about building the most complex system, but about building the right system for your needs. Start with simple prompts, optimize them through thorough evaluation, and only add multi-step agent systems when simpler solutions are insufficient.

When implementing agents, we try to follow three core principles:

* Keep the agent design simple.
* Prioritize transparency by clearly showing the agent’s planned steps.
* Carefully design your agent toolset through thorough documentation and testing.
