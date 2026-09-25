---
title: Release Version
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
# Release Version

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Release Version

Xpert Agents allow users to easily release new versions to meet the needs of continuous optimization and expansion.

* **Version Iteration Management**: Supports adjusting the features or logic of existing agents based on user needs and releasing updates through versioning.
* **Draft and Publish Separation**: Before releasing a new version, users can test and adjust the agent in draft mode to ensure stability and functional accuracy.
* **Version Release Logs**: Records changes made in each release, making it easy to trace and understand the context of version updates.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/publish.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=377b78585fcd7b5c4727469ac2d6d341" alt="Publish new version" width="1508" height="854" data-path="public/img/ai/publish.png" />

## Version Management Features

Version management features are designed to ensure the transparent and controllable evolution of Xpert Agents and help users efficiently manage multiple versions.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/publish-version.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=27568cd552cc884936a2624a6f9a8d71" alt="Publish new version" width="2130" height="1347" data-path="public/img/ai/xpert/publish-version.png" />

* **View Version History**: Users can view all historical versions of the agent, including release dates and version numbers.
* **Version Rollback**: If a new version encounters issues, users can quickly revert to an older version, ensuring business continuity and stability.
* **Multi-environment Support**: Supports managing multiple versions across different environments, such as testing and production environments (coming soon).

## Publish to Third-party Platforms

The Xpert AI platform supports publishing Xpert Agents to multiple major third-party platforms such as Feishu Bots, WeChat, DingTalk, etc. By integrating with these platforms, users can extend their intelligent assistants and automated tasks into everyday enterprise communication and workflows, enhancing work efficiency and user experience.

Xpert AI provides a graphical configuration interface that allows users to quickly configure their agents for target platforms by simply providing the necessary API keys and authentication information. The system will automatically handle connections to each platform.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/publish-3-platforms.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=97bdef2402009ab95c44afa78e9bcc7a" alt="Publish to third-party platforms" width="1512" height="855" data-path="public/img/ai/publish-3-platforms.png" />

Xpert Agent is optimized for the characteristics of different platforms, such as supporting rich media messages and button interactions in WeChat and DingTalk, while taking advantage of Feishu's stronger bot features for integration and diversified interactions.

### Publish to Feishu Bot

To publish to Feishu, you need to create an enterprise self-built application and configure the following conditions:

<Tip>
  **Prerequisites**

  * **Add bot capabilities**
  * **Send events to the developer server**
  * Add event `im.message.receive_v1`
  * **Send callbacks to the developer server**
  * Add callback `card.action.trigger`
  * Enable permissions `im:message.p2p_msg:readonly`, `im:message.group_at_msg:readonly`, `im:message`, `im:message:send_as_bot`
</Tip>

**Developer server** uses the `Webhook URL` generated during deployment.


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
