---
title: Recursion Limit
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
- Xpertai/XpertAI工作流教程-MD版/ai/troubleshooting/errors/recursion-limit.md
---
# Recursion Limit

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Recursion Limit

When using the Xpert AI platform for agent invocation or task orchestration, you may encounter an error message like:

```
Before reaching the stopping condition, the recursion limit of 20 has been hit. You can increase this limit by configuring the "Recursion Limit" in the Agent Settings of the Digital Expert Studio.
```

Or a similar error stack message, indicating that the recursion depth has exceeded the system’s preset limit. This guide will help you understand why this limit exists and provide best practices and troubleshooting tips.

***

### ❓ Why is a Recursion Limit Needed?

The Xpert AI platform supports collaboration among multiple agents, enabling **multi-turn processing**, **conditional logic**, and **context passing**. These features may lead to nested invocations, such as:

* Agent A delegates part of a task to Agent B, which then delegates to Agent C, and so on
* A failed task triggers a rollback or retry mechanism
* An agent re-invokes itself to optimize inference based on output results

Without a recursion limit, misconfigured logic or infinite loops can cause:

* Excessive token consumption
* Severe response delays
* System instability

To ensure system performance and stability, the platform enforces a maximum recursion limit.

***

### ✅ Best Practices

1. **Clarify the Task Flow**: Ensure that the task call paths are **convergent**, not infinite loops.
2. **Implement Exit Mechanisms**: Define stop conditions in agent logic—e.g., max rounds reached, goal achieved, confidence no longer improving.
3. **Avoid Unnecessary Nesting**: Minimize deep call chains. Prefer flat, modular agent designs with clear responsibilities.
4. **Configure Limits Wisely**: In certain modes (e.g., developer mode), recursion limits can be manually increased. Set conservatively.

***

### 🔍 How to Troubleshoot `recursion_limit` Errors

Follow these steps:

#### 1. **Check Invocation Logs**

* Log into the Xpert AI Console
* Navigate to the agent execution logs
* Locate the faulty task and inspect the message chain

#### 2. **Identify Recursion Paths**

* Review model capabilities used by the agent
* Check for circular invocation patterns, such as A → B → A → B → …

#### 3. **Check Condition Logic**

* Verify whether stop conditions like `if complete` are functioning
* Ensure conditional checks prevent redundant inferences

#### 4. **Fix and Test**

* Modify the agent prompt or logic to avoid infinite loops
* Monitor task logs to confirm if the recursion limit is still being triggered

#### 5. **Temporarily Increase the Limit (Not Recommended for Production)**

* In development or testing environments, advanced settings allow you to raise the `recursion_limit`
* Always monitor logs and revert to a safe value once the issue is resolved

***

### 📌 Example Scenarios and Optimization Tips

| Scenario                                | Issue               | Optimization Tip                                       |
| --------------------------------------- | ------------------- | ------------------------------------------------------ |
| Agent keeps rewriting the same response | No stop condition   | Set a max rewrite round limit (e.g., 3)                |
| Multiple subtasks depend on each other  | Circular dependency | Designate one master agent to control task dispatching |
| Retry logic lacks a cap                 | Infinite retries    | Add a max retry counter                                |

***

### 📞 Need Help?

If you're still unable to identify the issue, feel free to contact our technical support team. We’re here to assist with a step-by-step inspection of the agent behavior chain to ensure stable platform operation.
