---
title: 'Step 1: Create a Knowledge Pipeline'
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/knowledge-base/create-knowledge-base-via-pipeline/step-1-create-pipeline.md
---
# Step 1: Create a Knowledge Pipeline

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
