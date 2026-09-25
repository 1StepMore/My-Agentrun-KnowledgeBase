---
title: Iterating
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
- Xpertai/XpertAI工作流教程-MD版/ai/workflow/iterating.md
---
# Iterating

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Iterating

**Iterating** node is a core component designed for loop processing scenarios, capable of automating the handling of structured data (**arrays/objects**). By flexibly configuring sub-agents or workflows, combined with parallel processing and intelligent error-handling mechanisms, it significantly enhances the execution efficiency of complex tasks.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/workflow/iterating-node.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=178a98fca9877fbfef4da5692428b20e" alt="Iterating node" width="1816" height="1102" data-path="public/img/ai/workflow/iterating-node.png" />

## Core Functionality Breakdown

### 1. Data Structure Support

| Data Type  | Processing Method                                                | Output Format                                |
| ---------- | ---------------------------------------------------------------- | -------------------------------------------- |
| **Array**  | Iterates through each element (in index order or random order)   | New array (collection of processed elements) |
| **Object** | Iterates through each key-value pair (property-level processing) | New object (restructured key-value pairs)    |

### 2. Processing Modes

| Mode           | Execution Method                                            | Applicable Scenarios                                            |
| -------------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| **Sequential** | Executes in sequence                                        | Tasks with strong data dependencies or resource-sensitive tasks |
| **Parallel**   | Multi-threaded concurrency (configurable concurrency level) | I/O-intensive tasks or independent element processing tasks     |

### 3. Error Handling Strategies

| Strategy                  | Behavior Description                                             | Data Integrity Assurance                   |
| ------------------------- | ---------------------------------------------------------------- | ------------------------------------------ |
| **Abort on Error**        | Stops the process immediately and throws an exception            | High requirement for full data consistency |
| **Ignore Errors**         | Skips errored items, retains original data                       | Allows partial failure, logs errors        |
| **Remove Failed Results** | Automatically filters out failed items, outputs valid result set | Prioritizes result usability               |

## Best Practice Guide

### Mode Selection Recommendations

* Prioritize **Parallel Processing** when:
  * Element processing logic has no state dependencies
  * External APIs/services have high availability
  * There are explicit concurrency limits (e.g., database connection pools)

* Use **Sequential Processing** when:
  * Processing order must be maintained (e.g., time-series data)
  * Involves transactional operations (e.g., database writes)
  * The process consumes significant computational resources

### Error Strategy Decision Tree

```plaintext theme={null}
                   Start
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
  Allow partial failure?       Must be 100% successful
         │                       │
   ┌─────┴─────┐             ┌────┴───┐
   ▼           ▼             ▼        ▼
Retain original data  Only need valid results  Select "Abort on Error"
   │           │
Select "Ignore Errors"  Select "Remove Failed Results"
```

By leveraging the iterative node effectively, users can build integrated solutions ranging from simple data cleaning to complex business process automation.
