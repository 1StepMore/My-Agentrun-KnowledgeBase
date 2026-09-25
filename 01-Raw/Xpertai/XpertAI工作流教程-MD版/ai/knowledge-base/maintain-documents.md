---
title: Maintaining Documents
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
# Maintaining Documents

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Maintaining Documents

**Knowledge Base Documents** refer to various types of textual information resources stored in the system. These can be files in formats such as PDF, Word, or Text, or web page content, providing efficient query and learning materials for intelligent agents. The document management function is one of the core components of the knowledge base, enabling users to upload, categorize, retrieve, and manage document content, ensuring the system can quickly and accurately extract relevant information from a large volume of documents.

## Managing Documents

In the knowledge base document management list, users can conveniently perform a series of operations on documents, including adding, converting to embeddings, deleting, and configuring chunking settings:

1. **Adding Documents**: Users can upload documents in various formats to the system, supporting multiple document types (e.g., PDF, Word, Text, etc.).

2. **Converting to Embedded Documents**: To improve retrieval efficiency, users can convert document content into embeddings. Through this process, the information in the document is transformed into vector form, allowing the system to perform semantic searches and relevance matching more effectively.

3. **Deleting Documents**: Users can delete documents that are no longer needed to keep the knowledge base organized. The deletion takes effect immediately, removing the document content from the system.

4. **Document Chunking Settings**: Users can individually configure chunking methods for documents, splitting them into smaller segments for easier management and querying. This chunking setup enhances the system’s processing speed and accuracy, especially during large-scale information retrieval.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/kb/documents.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=28f0346ff1db466ed5af0236f8bb9b0f" alt="Documents" width="3024" height="1714" data-path="public/img/ai/kb/documents.png" />

### Adding Documents

The XpertAI knowledge base provides a document upload function, allowing users to upload documents in two ways:

1. **Uploading Local Files**: Users can directly upload local files. Supported formats include TXT, Markdown, PDF, HTML, XLSX, PPTX, CSV, and other common formats. Each file size is limited to no more than 15MB.

2. **Web Scraping**: Users can also choose to upload documents by scraping text from web pages. This is useful for extracting information from websites to further enrich the knowledge base.

#### Files

After uploading files, users can click to preview the document content. For files with large amounts of data, only the beginning portion is previewed. Before creating a document from uploaded files, users can still delete unnecessary ones.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/kb/upload-file.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=9c2550e492695921de889d2e526b68c5" alt="Upload Documents" width="3024" height="1714" data-path="public/img/ai/kb/upload-file.png" />

#### Web Pages

Scraping online web pages supports two tools: Playwright and Firecrawl.

* Playwright scrapes web content through a local server.
* Firecrawl scrapes web content via an integrated connection with the Firecrawl provider.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/kb/web-scrape.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=33f7411367288ef94970a93a1f75876a" alt="Web Scrape" width="2070" height="1351" data-path="public/img/ai/kb/web-scrape.png" />

* **Playwright Operation Steps**:\
  Enter the full URL of the target web page in the input box (e.g., [https://xpertai.cn/](https://xpertai.cn/)), and click "Load" to view the web scraping results below. Click "Preview" to see the web content. Click "Next" to configure it the same way as local documents, then save and process.

* **Firecrawl Operation Steps**:\
  Unlike Playwright, you first need to configure an **integration connection**.\
  **Steps to Configure Integration Connection**:\
  In the settings page at the bottom left corner, find the integration link and add a new Firecrawl integration connection. First, customize a name. You’ll also need an API Key—click "Get an API Key" on the page to jump to the Firecrawl website, register, obtain your API Key, then copy and fill it in.\
  **Web Scraping Steps**:\
  After configuring the integration connection, go to the scraping page interface, select the configured connection, enter the URL, and choose the scraping mode and maximum subpages. Click "Load" to scrape the web content. Then click "Next" and "Save" to create a new document.

#### Chunking Settings

* **Delimiter**: Users can specify a custom delimiter to split text into smaller chunks. The default delimiter is automatically recognized based on the text structure, but users can adjust it as needed.
* **Chunk Size**: Users can set the number of characters per chunk (default is 1000 characters). The chunk size determines the length of each text segment, affecting retrieval precision and efficiency.
* **Chunk Overlap**: Users can set the number of overlapping characters between adjacent chunks (default is 100 characters). Overlap helps maintain contextual continuity and reduces information fragmentation.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/kb/chunk-options.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=833f7a248793a5ef9eade9505ccc3a52" alt="Chunk options" width="1888" height="1032" data-path="public/img/ai/kb/chunk-options.png" />

Before chunking, XpertAI provides powerful text preprocessing features to ensure the input content is clean and structured. Users can enable the following options:

* **Replace Consecutive Spaces, Line Breaks, and Tabs**: Remove redundant whitespace characters to standardize the text format.

* **Remove All URLs and Email Addresses**: Protect privacy and keep content concise, ideal for documents requiring noise reduction.

* **Preview Function**: Using the "Preview Chunk" button, users can view the chunked text in real-time. The preview window displays the character count and content of each chunk, helping users verify if the settings meet their needs.

* **Example**: The preview might show results like “Chunk-0 - 956 characters” or “Chunk-1 - 988 characters,” allowing users to adjust parameters based on the actual content.

#### Best Practices

* **Chunk Size Recommendation**: For complex documents, set a larger "Chunk Size" (e.g., 1000-2000 characters) to preserve context; for short queries, smaller chunks (e.g., 500 characters) may be more suitable.
* **Overlap Setting**: Keep "Chunk Overlap" between 50-150 characters to balance contextual continuity and performance.
* **Preprocessing Optimization**: If a document contains significant formatting noise (e.g., excessive line breaks or URLs), enable preprocessing rules to improve chunking quality.

## Managing Chunks

* **Chunk Viewing and Status Management**: Each chunk is presented in a concise card or list item format, including features like chunk number and character count, content preview, enable/disable status, and editing options.
* **Editing Chunks**
* **Adding New Chunks**
* **Search and Filtering**

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/kb/manage-chunks.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=03f1a6db9c3c0ef65e7180e9c2a98e47" alt="Manage chunks" width="2562" height="1352" data-path="public/img/ai/kb/manage-chunks.png" />

## How to Use the Knowledge Base

On the agent page, create a new digital expert, add a knowledge base, and connect them. This allows the digital expert to retrieve content from the knowledge base.\
After establishing the connection, you can test it by clicking "Preview" and sending a question. From the conversation log, you can see that the AI’s response invokes the Knowledge Retriever to fetch text from the knowledge base. Once the content is retrieved, it’s passed to the large language model (LLM).\
The large language model then answers the user based on the retrieved content.


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
