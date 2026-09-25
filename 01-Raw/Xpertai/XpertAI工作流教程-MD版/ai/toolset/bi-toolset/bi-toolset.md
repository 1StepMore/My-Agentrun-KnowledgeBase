---
title: BI Toolsets
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
# BI Toolsets

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# BI Toolsets

The Xpert Data Analytics Toolset provides a suite of tools for business intelligence analysis, seamlessly integrated with the Xpert Data Analytics Platform.

## How to Configure the Model for Analysis?

To analyze models on the data analytics platform using the ChatBI Toolset, authorize the relevant model(s) for the toolset. As shown below, select the model to analyze in the Chat Models attribute, in addition to name and description attributes, then save the authorization to enable three tools and save.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/builtin-tool-chatbi-auth.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=7740e30c03c8a6991a076d35e8c52b06" alt="ChatBI Toolset authorization" width="1341" height="857" data-path="public/img/ai/builtin-tool-chatbi-auth.png" />

## Why Are There No Chat Models Available?

The Chat Models list must be created in the Chat BI system configuration page of the Xpert Data Analytics Platform. Select a semantic model and one of its model entities, provide the entity description and details, then create successfully.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/chatbi-model.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=9777d301e79c771aa477ee02b8be1b4e" alt="ChatBI Toolset authorization" width="1078" height="852" data-path="public/img/ai/chatbi-model.png" />

For detailed information on semantic models, see [Semantic Models](/docs/models/).

## How to Use the ChatBI Toolset?

In Xpert Studio, when orchestrating an agent, right-click to add the toolset, locate the authorized ChatBI Toolset, and add it to the Studio panel. Connect the agent node to the toolset node, enabling the agent to use the ChatBI Toolset to answer data analysis-related questions.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/chatbi-toolset-usein-xpert.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=4e3e4776446ae614c7969965d0e26b0f" alt="ChatBI Toolset use" width="1744" height="1025" data-path="public/img/ai/chatbi-toolset-usein-xpert.png" />

## Final Usage

In the final user conversation interface, Xpert expert users can ask analysis questions related to the data model. Xpert will query model information as needed and provide answers using graphical components.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/chatbi-toolset-in-chat-xpert.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=d8f8e8d2a1565698b3e6f39d7887745e" alt="ChatBI Toolset use in chat" width="1294" height="857" data-path="public/img/ai/chatbi-toolset-in-chat-xpert.png" />

## ChatDB Toolset

The ChatDB Toolset includes tools for direct database interaction, converting natural language into SQL to query the database for answers. The usage process is similar to ChatBI.


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
