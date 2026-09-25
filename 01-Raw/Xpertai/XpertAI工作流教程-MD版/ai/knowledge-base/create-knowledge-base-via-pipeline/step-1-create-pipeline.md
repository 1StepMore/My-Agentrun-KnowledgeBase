---
title: 'Step 1: Create a Knowledge Pipeline'
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
# Step 1: Create a Knowledge Pipeline

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Step 1: Create a Knowledge Pipeline

Click **Knowledge Base** in the top menu of your workspace, then click **Create Knowledge Base via Pipeline** on the left. You can create a knowledge pipeline in the following three ways.

### Method 1: Build from Scratch

Click **Blank Knowledge Pipeline** to start building a custom knowledge pipeline from scratch.
If you need to customize processing strategies based on your data characteristics and business needs, it is recommended to start with a blank pipeline.

### Method 2: Create via Template

XpertAI provides pipeline templates. The template cards include the knowledge base name and a brief description.

Built-in pipelines are preset pipeline templates optimized for common document data structures. You can choose the appropriate processing method according to different document types and usage scenarios. Click **Install** to start using.

**Template Types**

| Template Name                       | Segmentation Structure | Indexing Method | Retrieval Settings | Description                                                                                                              |
| ----------------------------------- | ---------------------- | --------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| General Mode                        | General Mode           | Vector          | Vector Search      | Splits document content into smaller paragraph blocks (general blocks) for direct query matching and retrieval.          |
| Detailed PDF with Images and Tables | General Mode           | Vector          | Vector Search      | Designed for complex file formats like PDF, DOCX, and PPTX. Converts them to Markdown for better information processing. |

### Method 3: Import a Knowledge Pipeline

After configuring the knowledge pipeline, you can save and export it to share with others. Knowledge base users can import pipelines to quickly reuse existing ones and modify them for different scenarios or requirements.
Similar to Digital Expert DSL, knowledge pipelines use the same YAML format standard to define processing flows and configurations within the knowledge base.

A knowledge pipeline includes the following:

| Name                          | Includes                                                                            |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| Data Sources                  | File upload, websites, online documents, and drives                                 |
| Data Processing Flow          | Document extraction, content chunking, image understanding, and cleaning strategies |
| Knowledge Base Storage Config | Indexing, retrieval settings, and storage parameters                                |
| Node Connections              | Connections and processing order between nodes                                      |
| User Input Forms              | Custom trigger parameter input fields (if configured)                               |


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
