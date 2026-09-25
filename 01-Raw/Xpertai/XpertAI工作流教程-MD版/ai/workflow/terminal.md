---
title: Execution Endpoint
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
# Execution Endpoint

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

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
