---
title: Document Transformer
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
# Document Transformer

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Document Transformer

**Document Transformer** is one of the core nodes in the XpertAI [Knowledge Pipeline](/docs/ai/knowledge/pipeline/), responsible for intelligently parsing, extracting, and structurally transforming raw document data via [plugins](/docs/plugin/). It can automatically process unstructured content from various data sources (such as PDFs, Word documents, web pages, images, audio, etc.) into standardized document objects that are understandable by the knowledge base, providing clear and consistent input for subsequent chunking, embedding, and retrieval.

In the knowledge pipeline, the main goals of the Document Transformer node are:

* Convert documents of different formats into unified, structured knowledge documents;
* Perform **semantic parsing, OCR recognition, text extraction, and metadata enhancement**;
* Use plugin strategies to adaptively handle various file types and sources;
* Support both test mode (preview) and production mode (official release) transformation workflows;

***

## How It Works

When the knowledge pipeline reaches the document transformation node, the system will automatically:

1. **Read the document data output from upstream nodes** (such as file upload nodes, web crawler nodes, or external integrated data sources);
2. Select the appropriate **Document Processing Strategy (Transformer Strategy)** based on the document transformation [plugins](/docs/plugin/) configured in the knowledge base;
3. Execute the transformation logic according to node configuration, including:

   * Text extraction
   * Optical Character Recognition (OCR)
   * Image content recognition and description generation (VLM / multimodal processing)
   * Format normalization (Markdown, JSON, HTML, etc.)
   * Metadata generation and cleansing
4. Write the transformation results back to the knowledge base, generating a document version with the status **"Transformed"**;
5. If the transformation fails, automatically record the error status and information for tracking and recovery in the pipeline.

***

## Use Cases

The Document Transformer node has broad application value in enterprise knowledge management and intelligent document processing scenarios:

* **OCR Scenarios**: Automatically recognize text from scanned PDFs, image reports, and scanned paper documents;
* **Structure Extraction**: Extract main content, titles, tables, and other key elements from Word, PPT, and HTML pages;
* **Rich Media Processing**: Recognize and transcribe images, charts, or formulas in documents for semantic search;
* **Web and Knowledge Source Synchronization**: Perform structured synchronization of web pages and online documents (such as Feishu Docs, Notion, etc.);
* **Content Cleansing and Enhancement**: Perform regex cleansing, semantic annotation, named entity recognition, etc., on text;
* **Data Archiving**: Form standardized, traceable knowledge assets in the knowledge base for RAG retrieval or multi-agent Q\&A.

***

## Node Features

| Feature            | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| **Node Type**      | Processor (Processing Node)                                              |
| **Node Name**      | Document Transformer                                                     |
| **Input**          | Raw document objects output from upstream nodes                          |
| **Output**         | Transformed document objects (structured docs + metadata + chunks)       |
| **Status Update**  | Automatically updates document status to `TRANSFORMED` or `ERROR`        |
| **Test Mode**      | Supports conversion debugging in preview mode (no DB write)              |
| **Error Handling** | Automatically captures conversion errors and writes to task logs         |
| **Compatibility**  | Supports multiple plugin strategies (text, image, web, rich media, etc.) |

***

## Plugin Mechanism

The power of the Document Transformer node lies in its **plugin-based architecture**.
XpertAI provides an open document transformation plugin interface (`DocumentTransformerStrategy`), allowing both official and community developers to implement the following types of plugins:

* 📄 **General Text Transformation Plugins**: Handle common documents such as PDF, DOCX, TXT, etc.;
* 🌐 **Web Parsing Plugins**: Structure web content into knowledge documents;
* 🧠 **Multimodal Recognition Plugins**: Use vision-language models (such as GPT-4V, PaddleOCR, MinerU) to understand images and charts;
* 🧩 **Enterprise Integration Plugins**: Connect to platforms like Feishu Docs, Notion, SharePoint, Confluence, etc.;
* ⚙️ **Custom Script Plugins**: User-written logic for content cleansing, format conversion, field extraction.

Before plugin execution, authorization verification is performed based on node context and system environment variables, including:

* API Key authorization;
* OAuth application authorization;
* Temporary file directory (`tempDir`) isolation;
* File system and external integration permission control (e.g., access to cloud drives, remote document libraries, etc.).

This open mechanism allows the Document Transformer node to flexibly expand and quickly adapt to different enterprise data scenarios.

***

## Operation Modes & Stages

The Document Transformer node supports two operation modes:

| Mode                | Description                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Test Mode**       | Executes during pipeline debugging, does not save results, for preview only.                                       |
| **Production Mode** | Executes during official knowledge base updates, results are persisted to the database for indexing and retrieval. |

The execution path is the same in both stages, differing only in:

* **Whether to write to the knowledge base table structure;**
* **Whether to trigger indexing and task status updates;**
* **Whether to generate persistent chunk data for AI retrieval.**

***

## Transformation Results & Downstream Integration

After transformation, the node outputs standardized knowledge document objects:

* Each document contains structured `metadata` information;
* Includes `chunks` processed for vector indexing and semantic retrieval;
* Status is `TRANSFORMED`;
* Also outputs an `Error` channel to capture exceptions.

Downstream nodes (such as **Chunker**, **Embedder**, **Recall Tester**, etc.) can directly use these outputs for subsequent processes.

***

## Summary

The **Document Transformer node** is the "intelligent content processing center" of the XpertAI Knowledge Pipeline.
Through its plugin mechanism and automated management, it transforms complex and diverse raw files into structured, standardized, and retrievable knowledge documents, serving as a key bridge between enterprise data sources and the AI knowledge base.

Whether building an enterprise knowledge base, training proprietary large models, or providing semantic context for digital experts,
the Document Transformer node is a crucial part of **turning unstructured data into usable knowledge assets**.


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
