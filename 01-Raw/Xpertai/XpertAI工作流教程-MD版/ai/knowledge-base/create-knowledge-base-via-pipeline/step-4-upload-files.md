---
title: 'Step 4: Upload Files'
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
# Step 4: Upload Files

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Step 4: Upload Files

After you have finished configuring, debugging, and successfully publishing your knowledge pipeline, you can upload files by navigating to the document list page:

## Upload Process

### 1. Select Data Source

Choose an upload method from the data source types configured in the pipeline.
Currently, XpertAI supports the following data sources:

* **Local file upload** (pdf, docx, txt, markdown, etc.)
* **Remote file systems** (such as S3, FTP, etc.)
* **Online drives** (in development)
* **Online documents** (such as Feishu Docs)
* **Web crawling** (such as Firecrawl and other plugins)

You can also find more data source support in the [XpertAI Plugin Marketplace](https://app.xpertai.cn/settings/plugins).

<Tip>
  **Tip**:

  Even if you have configured a knowledge pipeline for your knowledge base, you can still use the **basic configuration mode** to upload files directly, without processing them through the pipeline.
  This allows your knowledge base to support both automated processing and flexible manual additions or quick testing scenarios.
</Tip>

***

### 2. Fill in File Processing Parameters and Input Variables

If user input fields were defined during pipeline configuration, you will need to fill in the corresponding parameters and variables when uploading files.
After completing the form, you can click **Preview Segmentation** to view how the document will be chunked.
Once confirmed, click **Save and Process** to start creating and processing the knowledge base document.

***

### 3. Document Processing and Progress Tracking

After the file upload is complete, the system will automatically start the document processing workflow.
You can monitor the processing progress of each file in real time. Once embedding is complete, click **Go to Document** to enter the knowledge base page.

***

### 4. View File List

After entering the knowledge base document interface, you can view:

* The number of uploaded files
* The processing status and progress of each file
* Whether embedding is complete and the file is available

On this page, you can also reprocess, delete, or append files to documents, making it easy to maintain the latest content in your knowledge base.


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
