---
title: Scheduled Tasks
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
# Scheduled Tasks

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Tasks

**Scheduled Task Toolkit** is a task management feature designed for intelligent agents, enabling them to help users schedule and execute timed tasks efficiently.

1. **Support for Multi-Agent Collaboration Architecture**\
   Users can freely build a collaborative multi-agent architecture on the XpertAI platform. Agents seamlessly cooperate through the Task Toolkit to execute complex tasks. Each task can be completed by a single agent or collaboratively by multiple agents based on user needs.

2. **Flexible Task Customization**\
   The Task Toolkit allows users to create one-time or recurring tasks tailored to specific needs. Tasks can include reminders, data reports, workflow triggers, and more. Through the platform, users can refine task execution logic and set detailed trigger conditions.

3. **Multi-Channel Notification Support**\
   After task completion, notifications can be sent through familiar communication tools like Lark, email, or other integrated platforms, ensuring users receive task results or important reminders promptly.

4. **Deep Integration with the Platform**\
   The Task Toolkit is a key part of the XpertAI platform's ecosystem. Combined with other tools like ChatBI, ChatDB, and Search, users can integrate AI data analysis, knowledge retrieval, and more into tasks, making the agent's capabilities smarter and more powerful.

:::warning Trial Account Limitations

* **Task Limit**: Trial accounts can create up to **10 tasks**.
* **Task Execution Limit**: Each task can be executed up to **10 times**, meeting the basic task scheduling needs of trial users.
  :::

## Tools

The Scheduled Task Toolkit includes three tools:

* **Create Task**: Create a one-time or recurring scheduled task.
  * `name`: Task name.
  * `schedule`: Time schedule.
  * `xpertId`: ID of the digital expert responsible for the task.
  * `agentKey`: Primary key of the agent, specifying the agent in the expert team to execute the task.
  * `prompt`: Task instructions, guiding the agent on how to execute the task.
* **List Tasks**: List all tasks assigned to a digital expert.
* **Delete Task**: Delete a specific scheduled task.

## Suggested Prompts

Here are some example prompts for using the Scheduled Task Toolkit effectively:

```text theme={null}
Use the `*_task` tool to schedule **tasks** to do later. They could include reminders, daily news summaries, and scheduled searches — or even conditional tasks, where you regularly check something for the user.

-- Remove or change the agents key --
Set `agentKey` parameter to 'task-to-email' or 'task-to-feishu'.
- `task-to-email` can send email.
- `task-to-feishu` can send feishu message.
-- End --

To create a task, provide a **name** **prompt** and **schedule**
**name** should be short, imperative, and start with a verb. DO NOT include the date or time requested.

**prompt** should be a summary of the user's request but DO NOT include any time scheduling info.
    - For simple reminders, use "Tell me to..."
    - For requests that require a search, use "Search for..."
    - For conditional requests, include something like "...and notify me if so."

**schedule** must be given in cron job format.
    - If the user does not specify a time, make a best guess.
    - Prefer the RRULE: property whenever possible.
    - DO NOT specify SUMMARY and DO NOT specify DTEND properties in the VEVENT.
    - For conditional tasks, choose a sensible frequency for your recurring schedule. (Weekly is usually good, but for time-sensitive things use a more frequent schedule.)

If you want to delete a task, please first query the task list and select the task to delete.

Please answer in {{sys_language}} language.
```


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
