---
title: Connecting to external knowledge bases
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
# Connecting to external knowledge bases

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting to external knowledge bases

The XpertAI Agent Platform supports connecting to external knowledge bases, expanding the knowledge boundaries of agents through system integration. This feature allows your agent to directly access and utilize specialized information stored in external knowledge bases without the need for repeated uploads or data migration, ensuring data consistency while enhancing the accuracy and professionalism of the agent's responses.

This article will provide a detailed guide on how to configure and use the external knowledge base feature on the XpertAI platform.

## Preparation

Before starting the configuration, ensure you have the following information ready:

1. **External Knowledge Base API Endpoint**: This is the URL address XpertAI uses to access your knowledge base, typically provided by your knowledge base service provider.
2. **Authentication Key (if required)**: If your knowledge base requires an API Key, AK/SK, or other forms of authentication, obtain it in advance.
3. **Knowledge Base Identifier (ID or Name)**: If your external knowledge base system manages multiple bases, you need to specify the ID or name of the specific knowledge base to connect.

<Info>
  Currently supported knowledge base providers include: **RAGFlow**, **Dify**, and **FastGPT**.
</Info>

## Configuration Steps

Below are the detailed steps to connect an external knowledge base on the XpertAI platform.

### Step 1: Access the System Integration Page

1. Log in to the XpertAI Settings module.
2. In the left navigation bar, locate and click "**Integrations**."
3. On the "Integrations" page, select the provider type related to the knowledge base.
4. Enter the base address and authorization information, then click Create.

### Step 2: Add an External Knowledge Base Connection

Navigate to the "Knowledge Base" page in the workspace: Click to connect an external knowledge base, fill in the basic information, and select a knowledge base integration connection.

### Step 3: Advanced Settings (Optional)

The XpertAI platform provides advanced retrieval parameter configurations to optimize recall performance:

* **Top K**: Sets the number of the most relevant text segments returned per retrieval. Increasing this value may return more relevant information but could also introduce more irrelevant data. The default is typically 3–5.
* **Score Threshold**: Sets the relevance score threshold; only text segments with scores above this value will be returned. Increasing this value can make results more precise but may reduce the number of results. The default is typically 0.5.

You can adjust these parameters based on subsequent test results.

### Step 4: Save and Test the Connection

1. After filling in all necessary information, click the "**Connect**" button.
2. If the configuration is correct, the system will display a connection success message.
3. It is strongly recommended to use the "**Test Recall**" function. Enter a test question or keyword to verify whether XpertAI can correctly retrieve relevant text segments from your external knowledge base.

## Applying the External Knowledge Base in Agents

Once the connection is successful, you can use this external knowledge base when creating or editing an agent.

## Troubleshooting

| Issue                        | Possible Cause                              | Solution                                                                                                  |
| ---------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| No results from test recall  | Incorrect API endpoint or knowledge base ID | Verify the endpoint URL and knowledge base ID are correct.                                                |
| Authentication failure       | Invalid or expired API Key                  | Check and update the API Key.                                                                             |
| Irrelevant retrieval results | Improper retrieval parameter settings       | Adjust Top K and Score Threshold; check the document quality and indexing settings of the knowledge base. |
| Connection timeout           | Network issues or firewall restrictions     | Check network connectivity and ensure XpertAI services can access your knowledge base’s API address.      |

## Conclusion

By connecting to an external knowledge base, the XpertAI Agent Platform can deeply integrate into your enterprise’s knowledge ecosystem, fully leveraging the value of existing knowledge assets to build smarter and more professional AI applications. If you encounter any issues during the configuration process, please feel free to contact our technical support team.


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
