---
title: Browser-use Tools
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
# Browser-use Tools

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser-use Tools

<Tip>
  **PRO**

  This feature is supported in the **Professional Edition**.
</Tip>

**Browser-use** is a browser automation task execution tool designed for Xpert agents. It encapsulates integration capabilities with the [browser-use](https://github.com/browser-use/browser-use) open-source framework, allowing large model Agents to call real browsers in sandbox environments to complete specified web page operation tasks automatically.

This tool is suitable for task scenarios that require automatically accessing websites, extracting information, filling forms, clicking buttons, etc., through browsers, providing browser operation extension capabilities for large models with general execution capabilities.

## Features

* ✅ Supports automatic browser operations through naturally described `task` tasks
* ✅ Supports custom large model and API integration configuration
* ✅ Seamless integration with `browser-use` open-source framework
* ✅ Automatically tracks and records execution process (history, recording, Trace)
* ✅ Supports multi-step tasks combined with Agent reasoning flow
* ✅ Supports runtime parameter configuration, such as whether to enable recording, whether to enable vision models, etc.
* ✅ Supports use in Agentic Workflow

## Usage Instructions

### Tool Parameter Configuration

* Specify browser task (provided by LLM)
* Configure LLM model
* Browser execution parameters (whether to record, whether to use vision model, timeout, etc.)

### Communication with browser-use in Sandbox

The tool establishes an SSE stream through `EventSource`, communicates with the Sandbox service, and initiates browser task streaming execution to `/operator/stream`.

### Real-time Event Reception

During task execution, the tool will listen and parse event messages sent back by browser-use:

* Thoughts for each execution step (`thoughts`)
* Current page URL
* Whether errors occurred (`errors`)
* Whether completed (messages containing `done`)

Parsed intermediate events will be distributed in real-time to the frontend or debugging interface for displaying execution status.

### Final Result Return

When the task completes (detecting `done`), the tool will extract the `final_result` field from events as the execution result.

## Return Value

Returns a string result, which is a summary or operation result description after the large model Agent executes the task.

## Advanced Configuration

| Configuration Item | Description                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------- |
| `copilotModel`     | Currently used LLM model and its Provider information                                     |
| `llm_temperature`  | Controls the temperature of large model sampling (default 0.5)                            |
| `enable_recording` | Whether to enable browser recording function (enabled by default)                         |
| `max_steps`        | Maximum number of steps for browser task execution (default 100)                          |
| `use_vision`       | Whether to enable vision recognition capabilities (such as page screenshot understanding) |
| `timeout`          | Task timeout time                                                                         |

***

## Application Scenario Examples

* Search for specified content on web pages and summarize (such as news, stock prices, reports)
* Complete multi-step interactions on complex websites (such as querying information and exporting)
* Simulate real human web page operation processes in large Agent systems

## Notes

* This tool depends on the backend `browser-use` runtime environment (i.e., Sandbox), ensure it is accessible and started normally.
* Tool return results depend on the correctness of browser task execution and model understanding accuracy.
* Currently defaults to running browsers in `headless` mode.
* The tool is designed for large models, so `task` expressions should clearly describe intent in natural language.

## Related Links

* [browser-use GitHub Repository](https://github.com/browser-use/browser-use)


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
