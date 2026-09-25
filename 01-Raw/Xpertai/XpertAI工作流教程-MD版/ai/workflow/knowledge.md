---
title: Knowledge Retrieval
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
# Knowledge Retrieval

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Knowledge Retrieval

The **Knowledge Retrieval** node is a core capability in the XpertAI agent workflow, providing highly relevant information support for user queries. It automatically retrieves content snippets semantically related to the query from a pre-built knowledge base, serving as contextual input for downstream agents to understand, analyze, and generate responses.

## Main Capabilities

| Function                          | Description                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 🔍 Semantic Matching              | Automatically identifies the core intent of user input and retrieves the most semantically relevant knowledge snippets    |
| 📂 Content Support                | Supports retrieval of structured and unstructured document content, such as policy documents, FAQs, product manuals, etc. |
| 🎯 Precise Recall                 | Supports recall of multiple relevant content items, enabling comprehensive judgment by downstream nodes                   |
| 🔄 Composability                  | Can be flexibly combined with any language model node (e.g., reasoning models) to form complex task flows                 |
| 🔗 Multi-Knowledge Source Support | Configurable to access multiple knowledge bases for cross-business or multi-domain information retrieval                  |

## Usage

### 1. Input Parameters

The Knowledge Retrieval node accepts input from upstream nodes, typically a user's natural language question or a standardized query processed by an agent.

```json theme={null}
{
  "question": "What are the company's rules for compensatory leave?"
}
```

### 2. Output Structure

The Knowledge Retrieval node returns a list of documents in the format of Langchain's `Document` object. Each document contains two parts:

* `page_content`: The actual retrieved text content
* `metadata`: Metadata related to the content (e.g., source, document name, segment index, etc.)

\*\* 📄 Output Example \*\*:

```json theme={null}
[
  {
    "pageContent": "According to company policy, employees may apply for compensatory leave within 5 working days after overtime.",
    "id": "123",
    "metadata": {
      "source": "HR_Employee_Policy_v3.pdf",
      "section": "Compensatory Leave Policy",
      "page": 12
    }
  },
  {
    "pageContent": "Compensatory leave applications require approval from the direct supervisor and must not exceed the actual overtime hours.",
    "id": "456",
    "metadata": {
      "source": "HR_Employee_Policy_v3.pdf",
      "section": "Compensatory Leave Policy",
      "page": 12
    }
  }
]
```

This structure facilitates downstream language model nodes (e.g., Deepseek R1) to use the raw content and contextual information for high-quality question answering, summarization, or logical reasoning.

## Typical Use Cases

* **Enterprise Internal Q\&A Assistant**: For policies, IT support, expense reimbursement processes, etc.
* **Customer Service Intelligent Assistant**: Product feature explanations, troubleshooting guides
* **Project Knowledge Support**: Helps team members quickly understand background information or past experiences
* **Legal/Compliance Consulting Bot**: Extracts explanatory content from regulatory documents

## Recommended Companion Nodes

The Knowledge Retrieval node is typically used with the following nodes to form a complete agent task chain:

| Companion Node                              | Role                                                                                                     |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| 🎯 Reasoning Model Node (e.g., Deepseek R1) | Performs deep understanding and logical judgment on retrieved content to generate professional responses |
| 🧠 Prompt Generation Node                   | Rewrites user input to improve retrieval accuracy                                                        |
| 📝 Formatting Node                          | Enhances output readability and clarity                                                                  |
| 🚀 Output Node                              | Sends results to user interfaces, such as Feishu or web chat windows                                     |

## Notes

* Ensure the relevant knowledge base is populated and available
* For multilingual content, pre-configure support for the corresponding language in the knowledge base
* The amount of retrieved content can be customized in node settings (e.g., return top 3 or top 5 results)

***

## Conclusion

<Tip>
  The **Knowledge Retrieval** node serves as a bridge between "user questions" and "intelligent answers."
</Tip>

It not only provides factual evidence but also offers reliable semantic support for the agent's understanding and expression. In the XpertAI workflow, Knowledge Retrieval enhances your agent's contextual awareness and business expertise.

For more details on building and maintaining a knowledge base, refer to [Knowledge Base Management](/docs/ai/knowledge/).


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
