---
title: Client Tools
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
# Client Tools

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Client Tools

<Info>
  Learn how to define tools that let the agent operate client-side capabilities.
</Info>

Client tools route **model-initiated tool calls to the frontend UI for execution** and return results back to the model to continue reasoning. Use them for reading frontend state, handling user interaction, or leveraging browser capabilities.

<img src="https://mintcdn.com/xpertai/s0VVkPNi8D_ZpOIf/public/img/ai/chatkit/client-tool-middleware.png?fit=max&auto=format&n=s0VVkPNi8D_ZpOIf&q=85&s=1ba25bbdcf0b5a1bf4dd206f9330ab5a" alt="Client tool middleware" width="1660" height="1524" data-path="public/img/ai/chatkit/client-tool-middleware.png" />

## Workflow

1. **Configure the Client Tool on the server**

* Use the **Client Tool middleware** in the workflow
* Define `Tool Name / Description / Arguments Schema`

2. **Model triggers a tool call**

* The LLM calls the specified Client Tool based on context

3. **Frontend receives and executes**

* ChatKit sends the call to the frontend via `onClientTool`
* The frontend runs the real logic (UI or local state)

4. **Return the result**

* The frontend returns the tool result
* ChatKit passes the result back to the model to continue generation

***

## Server configuration essentials

**Tool Name**

* Unique identifier, for example `get_current_station`
* Must exactly match the `name` in frontend code

**Arguments Schema**

The schema must follow the [JSON Schema spec](https://json-schema.org/learn/getting-started-step-by-step):

```json theme={null}
{
  "type": "object",
  "properties": {}
}
```

***

## Frontend (React) integration

Register `onClientTool` in `useChatKit`:

```ts theme={null}
const handleClientTool = async ({ name, tool_call_id, id }) => {
  if (name === 'get_current_station') {
    return {
      tool_call_id: tool_call_id || id,
      name,
      status: 'success',
      content: JSON.stringify({ /* tool result */ }),
    };
  }
};
```

```ts theme={null}
useChatKit({
  ...
  onClientTool: handleClientTool,
});
```

***

## Return payload format

* `tool_call_id`: required
* `status`: `success` or `error`
* `content`: string (JSON recommended)

```json theme={null}
{
  "nodes": [...],
}
```

***

## Best practices

* Keep tool names identical between server and frontend
* Use `useRef` to read the latest UI state and avoid stale closures
* Keep `content` concise; avoid large payloads
* For failures, return `status: "error"`

***

Client tools let ChatKit safely and controllably integrate with frontend state and user interactions—a key capability for **HITL (Human-in-the-loop)** and **UI-aware agents**.


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
