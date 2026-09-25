---
title: Execution Endpoint
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
- Xpertai/XpertAI工作流教程-MD版/ai/workflow/terminal.md
---
# Execution Endpoint

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Execution Endpoint

In Xpert Agents, the `END` node is a special node used to represent the termination point of a graph. When the execution flow reaches the `END` node, it signifies that the execution of the graph is complete, and the process will stop.

When defining the orchestration structure of an Xpert agent, you can use an `END` agent or tool node to explicitly specify the end of the process.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/terminal-agent.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=86c52435568648e692c67f736b17ec99" alt="End agent" width="1511" height="855" data-path="public/img/ai/terminal-agent.png" />

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/terminal-tool.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=1f6543cd8b58a47fb1143a69ca868d28" alt="End tool" width="1511" height="854" data-path="public/img/ai/terminal-tool.png" />

<Tip>
  It is important to ensure that the logic of the graph is correctly designed to avoid unexpected loops or continued execution after reaching the `END` node.
</Tip>
