---
title: Recall Test
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
# Recall Test

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Recall Test

The **XpertAI Knowledge Base** comes with a powerful **recall testing feature** that simulates real user query scenarios. By entering keywords or questions, you can evaluate the recall quality of the knowledge base.
The system automatically retrieves indexed content chunks and sorts them by similarity score. Generally, the higher the match between the question and the content chunk, the closer the AI model's answer will be to the original document's meaning, reflecting better "knowledge recall" performance.

You can freely switch between different retrieval methods and parameter configurations to intuitively assess the relevance and coverage of recall results.
XpertAI's knowledge base uses a **unified chunk tree structure**, so all tests are based on parent-child hierarchical semantic recall logic.

***

## General Testing Mode

Enter common user questions or keywords in the **source text input box** and click the **Test** button to view the matched content chunks in the **Recall Results Area** on the right.

* Each content chunk displays a similarity score in the upper right corner, indicating how well it matches the question.
* Higher scores mean stronger semantic relevance between the chunk and the question.
* Click a content chunk to view its details and source in the document.

Document source information is shown below each recall result, helping you judge whether the chunking is reasonable and the semantic boundaries are clear.

***

## Parent-Child Structure Testing Mode

XpertAI's knowledge base uses a **tree-structured chunking** approach. When recalling a child chunk, its parent context is also brought in to provide the AI model with more complete semantic information.

During testing:

* After the user enters a question, the system first matches the most relevant child chunk;
* Then it automatically traces back to its parent chunk, integrating the context for display;
* The match score is shown in the upper right corner to measure how well the hit segment matches the question.

Clicking the source in the recall result lets you view the original content directly.
On the details page, the left side shows the parent chunk information, and the right side shows the matched child chunk. The system may hit multiple child nodes, each with its own match score, making it easy for developers to analyze chunking rationality and recall performance.

***

## Query Records and Application Calls

In the **Records** panel, you can view the history of recall test queries.
If the knowledge base is linked to a digital expert or other AI application, queries triggered within the application will also be displayed here, making it easy to track recall logs and effectiveness in one place.

***

## Adjusting Text Retrieval Methods

Click the **retrieval configuration icon** in the upper right corner of the input box to switch the retrieval method and parameters for the current knowledge base.
The modified settings only apply to the current recall test, allowing developers to compare the effects of different retrieval strategies.
To make global changes, go to **"Knowledge Base Settings > Retrieval Settings"** to save.

***

## Recommended Steps for Recall Testing

1. **Prepare a test set**: Design a set of test questions covering common user scenarios to ensure diversity.
2. **Choose a retrieval strategy**: Select the appropriate retrieval mode based on content characteristics and application scenarios (e.g., Q\&A, multilingual corpus, etc.).
3. **Tune parameters**: Adjust the number of recalls (TopK) and similarity threshold (Score) to balance recall relevance and completeness.

***

## Explanation of TopK and Score Parameters

* **TopK**: The maximum number of content chunks to recall, sorted by similarity score in descending order.

  * Smaller values: More concise recall, but may miss some relevant segments.
  * Larger values: More comprehensive recall, but may include less relevant segments, affecting final answer quality.

* **Score (Recall Threshold)**: Sets the minimum similarity score allowed for recall.

  * Lower values: Looser recall, including more low-relevance content.
  * Higher values: Stricter recall, retaining only highly relevant segments, but may miss marginal information.

By dynamically adjusting these two parameters, you can quickly find the best retrieval configuration for the specific content and business semantics of your knowledge base.

***

✅ **Summary**

Recall testing in XpertAI is not only a key tool for verifying knowledge base quality, but also an important means to optimize the knowledge pipeline and improve AI answer accuracy.
With recall logs, parent-child hierarchical structure, and retrieval parameter tuning, teams can iteratively improve knowledge base quality in a visual and verifiable way, making every answer closer to real business semantics.


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
