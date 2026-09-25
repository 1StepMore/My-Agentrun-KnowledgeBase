---
title: Human in the loop
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
# Human in the loop

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

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
