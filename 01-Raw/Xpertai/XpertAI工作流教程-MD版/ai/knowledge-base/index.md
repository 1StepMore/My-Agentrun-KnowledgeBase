---
title: Introduction
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
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
# Introduction

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

In AI conversational knowledge retrieval, the core functionalities of the knowledge base typically include document text embedding, Chunk retrieval, query optimization, and real-time updates. Below are common functionalities, with a focus on document text embedding and Chunk retrieval:

## Funtions

### 1. **Document Text Embedding**

* **Text Vectorization**: Using deep learning models (such as BERT, OpenAI Embeddings) to embed text into high-dimensional vectors, enabling similarity matching through vector retrieval. This forms the foundation for fast retrieval in the knowledge base and is suitable for various text types, such as documents, web pages, FAQs, etc.
* **Multilingual Support**: For texts in different languages, the corresponding embedding models are used to ensure the accuracy of multilingual retrieval.
* **Data Preprocessing**: Cleaning, tokenizing, and denoising the text in documents to generate high-quality vectors for embedding.
* **Context-Aware Embedding**: Ensuring that the embedding model can recognize the context within the text to enhance the accuracy of responses in conversations.

### 2. **Chunk Retrieval**

* **Document Chunking**: Breaking large documents into smaller chunks to improve retrieval accuracy and efficiency. Each Chunk typically consists of a few sentences or a paragraph, ensuring the system finds the most relevant specific information during retrieval rather than the entire document.
* **Embedding and Indexing Chunks**: Generating independent vectors for each Chunk and storing them in a vector database for indexing. This allows the system to quickly find the Chunks most similar to the user's query during retrieval.
  <img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/rag_indexing.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=2ddfab0b1b1e89f3ab49dfb39bb89465" alt="Rag indexing" width="2583" height="1299" data-path="public/img/ai/rag_indexing.png" />

### 3. **Query Optimization**

* **Semantic Retrieval**: Using semantic search technology to convert user queries into vectors that are then matched for similarity with the embedded knowledge base content. Compared to traditional keyword retrieval, semantic retrieval better understands user intent.
* **Fuzzy Matching**: Even if a query does not match the wording in a document exactly, the system can still return relevant results based on vector similarity.
* **Search Result Reordering**: (todo) Reordering returned results to ensure the most relevant answers appear first. This is typically based on vector similarity scores or other user interaction data (such as click-through rates).
  <img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/rag_retrieval_generation.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=1856793b7194498cd0ef9cf14b715f24" alt="Rag retrieval" width="2532" height="1299" data-path="public/img/ai/rag_retrieval_generation.png" />

### 4. **Document Update and Management**

* **Real-Time Updates**: Supports dynamic updates to the knowledge base, ensuring the latest information can be retrieved promptly. An automated document upload and embedding update process ensures the knowledge base content is always up to date.
* **Document Type Support**: The knowledge base typically supports various document formats, including PDF, Word, Markdown, plain text, etc., ensuring knowledge can be imported from different document sources.
* **Metadata Management**: (todo) Adding metadata (such as creation time, document type, author, etc.) to documents and Chunks, allowing the system to perform more precise retrieval based on metadata.

### 5. **Knowledge Base Q\&A**

* **Document-Based QA System**: Using retrieved text Chunks, combined with models like GPT, to generate direct answers to user questions. This method usually provides fact-based, accurate responses.
* **Step-by-Step Q\&A and Context Tracking**: The system can retain context in continuous conversations, providing more coherent responses and adjusting retrieval results based on previous dialogues.

### 6. **Extension and Integration**

* **External Data Source Integration**: The knowledge base can be integrated with external data sources (such as databases, APIs) to provide dynamic data query support.
* **Vector Database**: (todo) Utilizing vector databases like FAISS, Milvus, Pinecone, which can effectively manage and retrieve large-scale embedded data.

:::warning 🚧
In Development
:::

These functionalities will help make the knowledge retrieval module in Xpert AI more efficient and intelligent, especially in scenarios involving large amounts of documents and text. When designing the knowledge base retrieval system, you can optimize the speed and accuracy of Chunk retrieval by choosing the appropriate embedding models and vector databases.

## Detailed Settings for the Knowledge Base

Below are the detailed configurations for the knowledge base settings:

| Configuration Item        | Description                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Avatar**                | The identifying icon for the knowledge base, usually a logo or representative image.                                                    |
| **Name**                  | The name of the knowledge base, used to identify and differentiate between different knowledge bases.                                   |
| **Description**           | A brief description of the knowledge base, summarizing its content and purpose.                                                         |
| **Language**              | The primary language used in the knowledge base, such as Chinese, English, etc.                                                         |
| **Permissions**           | Access permission settings for the knowledge base, options include: <br /> - *Private* <br /> - *Within Organization* <br /> - *Public* |
| **Intelligent Assistant** | The intelligent assistant providing text embedding capabilities, specifying the AI provider used.                                       |
| **Embedding Model**       | The AI model used for text embedding, depending on the chosen intelligent assistant (i.e., AI provider).                                |
| **Embedding Batch Size**  | The number of text embeddings processed at once, affecting processing efficiency and performance.                                       |
| **Chunk Size**            | The size of each Chunk when dividing documents, typically by sentence or paragraph.                                                     |
| **Chunk Overlap**         | Specifies the overlapping part between adjacent Chunks to maintain context coherence.                                                   |
| **Similarity Threshold**  | When retrieving text blocks, filter results based on a similarity threshold to determine which Chunks to return.                        |

## Documents

Here is a detailed introduction to document and parsing functionalities, including document upload, document parsing, and related operation configurations:

### 1. Uploading Documents

Users can upload various formats of documents to the knowledge base. Supported document types include:

* **Markdown**: Used for lightweight markup language documents, easy to read and edit.
* **PDF**: Suitable for preserving formatted documents, ideal for long articles and reports.
* **EPUB**: An e-book format that supports reading on various devices.
* **DOCX**: Microsoft Word documents, widely used for text editing and formatting.

### 2. Document Parsing

Uploaded documents need to be parsed to extract their content and store it in the knowledge base. The parsing process can be configured as follows:

| Configuration Item | Description                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Chunk Size**     | Size setting for each text chunk (number of words or sentences) used to split document content into smaller pieces for retrieval. |
| **Chunk Overlap**  | Defines the overlap in words between adjacent text chunks, ensuring contextual coherence and avoiding information loss.           |
| **Delimiter**      | Defines how to separate chunks in the document, such as by paragraph, newline characters, or specific characters.                 |

### 3. Start Parsing

Once the configuration is complete, users can start the parsing process. The parsing task will run on the server-side, and the system will execute the following steps:

* **Read Document**: Load the uploaded document and perform format parsing.
* **Extract Content**: Based on the configured chunk size, chunk overlap, and delimiter, split the document content into multiple text chunks.
* **Generate Embeddings**: Call the AI model to generate vector embeddings for each text chunk for subsequent retrieval and query use.

### 4. Re-parse or Delete Documents

* **Re-parse**: Users can choose to re-parse a document at any time to update its configuration or content. This will re-execute the parsing process and replace old document chunks.
* **Delete Document**: Users can delete documents no longer needed, and the system will automatically delete all associated document chunks. This ensures the knowledge base content remains clean and accurate.

## Retrieval Testing

The retrieval testing feature is used to validate the effectiveness and accuracy of the knowledge base retrieval, ensuring the system can effectively retrieve relevant information from the knowledge base. Below are detailed parameter introductions for this feature:

| Parameter                | Description                                                                                                                                                                                                 |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Similarity Threshold** | Set a minimum similarity value, only retrieval results with similarity above this value will be returned.                                                                                                   |
| **Top N**                | Specify the number of results to return; the system will sort results based on similarity from high to low and return the top N most relevant results.                                                      |
| **Input**                | User-input query text to trigger the retrieval feature. The system will analyze this input and calculate its similarity with the content in the knowledge base to find relevant text blocks or information. |

### Function Flow:

1. **Input**: The user enters a query in the input box.
2. **Similarity Calculation**: The system vectorizes the user's input text and calculates similarity with all text blocks in the knowledge base.
3. **Filtering**: Based on the set similarity threshold, filter out text blocks with similarity below the threshold.
4. **Sorting**: Sort the remaining text blocks by similarity and return the most relevant results.
5. **Return Results**: The system returns the specified number of retrieval results based on the "Top N" setting.


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
