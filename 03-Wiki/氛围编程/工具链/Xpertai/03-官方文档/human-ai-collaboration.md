---
title: Human in the loop
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
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/human-ai-collaboration.md
---
# Human in the loop

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Human in the loop

Human-machine collaboration (or "human-in-the-loop") enhances agent functionality through several common user interaction patterns:

* **Approval**: Actions requiring user confirmation, interrupting before invoking the node.
* **Editing**: Actions requiring user input, interrupting before invoking the tool.

## Configuring Sensitive Agents and Tools

By designating sub-agents or tools as sensitive, the primary agent will be interrupted before invoking these sensitive nodes. At this point, the system presents a confirmation and parameter editing window, allowing users to review and modify the parameters about to be used. The primary agent will proceed with the invocation only after the user confirms and approves. This mechanism ensures user involvement and control at critical nodes, enhancing the system's safety and flexibility.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/human-in-the-loop-sensitive.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=062279f0a1e08cf3856f6a30a401da0c" alt="Set as sensitive" width="2444" height="1614" data-path="public/img/ai/human-in-the-loop-sensitive.png" />

After users review or edit the parameter values, the agent will proceed with invoking the sub-agent or tool using the updated parameters.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/human-in-the-loop-approval.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=7ba0af0eafbb3433b629aac581fe74ff" alt="Interrupt sensitive nodes" width="2446" height="1608" data-path="public/img/ai/human-in-the-loop-approval.png" />

## Implementation Principles

The interruption of sensitive nodes in human-machine collaboration is implemented through the Breakpoints feature in **langgraph.js**. Breakpoints allow the setting of pause points at specific nodes. When the agent reaches these nodes, the system halts execution and triggers the user interaction interface. This mechanism ensures user participation at critical points, enabling users to review, edit, or confirm parameters during execution.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/human-in-the-loop-edit-toolcall.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=fef203ee76d27d49061874e9dca82df5" alt="Edit parameters of tool calls" width="1991" height="1456" data-path="public/img/ai/human-in-the-loop-edit-toolcall.png" />
