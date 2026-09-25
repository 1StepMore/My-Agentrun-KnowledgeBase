---
title: Document Source Authorization
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
# Document Source Authorization

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Document Source Authorization

XpertAI supports connecting to various external document sources. To ensure data security and access control, the system provides a flexible authorization mechanism, allowing knowledge pipelines to securely access and import data.
In XpertAI, document source authorization can be achieved through **system integration** or **default environment variables**, supporting multiple authorization methods including **API Key** and **OAuth**.

***

## Overview of Document Source Authorization Mechanisms

The XpertAI authorization system consists of two parts:

1. **Default Environment Variable Authorization**\
   During system deployment or in the workspace environment, various API Keys can be preset via environment variables. The knowledge pipeline will automatically use these credentials for authorization at runtime, without manual binding.

2. **System Integration Authorization**\
   XpertAI provides a unified system integration entry point where administrators or developers can configure API Key or OAuth (in development) authorization information for external services.\
   System integration supports multiple authentication modes, including enterprise API Key, OAuth Client, and, in the future, service accounts and signed tokens.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/xpertai/public/en/img/ai/pipeline/pipeline-plugin-system-integration.png" alt="pipeline integrations" />

***

## Data Source Authorization Entry Points

In XpertAI, you can configure data source authorization in the following two ways:

### Method 1: Through the Knowledge Pipeline Orchestration Interface

Enter the knowledge pipeline orchestration interface and add the required data source node.\
Click **Bind** in the right panel, and the system will automatically detect whether the data source has valid authorization:

* If system integration or environment variables are configured, it will connect automatically;
* If no authorization information is found, you will be prompted to go to the system integration page for authorization.

***

### Method 2: Through the System Settings Interface

Click the settings icon in the lower left corner and select **System Integration** to enter the system integration configuration page.\
Select the system you want to authorize, click **Configure**, and you can add or update authorization credentials for that system.

***

## Supported Data Sources and Authorization Methods

| Data Source | Default Env Variable | API Key | OAuth |
| ----------- | -------------------- | ------- | ----- |
| Firecrawl   | ✅                    | ✅       |       |
| Lark Docs   | ✅                    | ✅       | ✅     |

> More third-party data sources (such as OneDrive, Notion, Google Drive) will be supported in future versions.

***

## Authorization Methods Explained

### 1. API Key Authorization

API Key is the most common authorization method, suitable for integrated services that require direct calls to external APIs.\
Users can generate API Keys on the corresponding service platform and configure them in two ways:

* **Method A: Environment Variable Authorization**\
  Write the API Key into the system environment variable (e.g., `LARK_APP_ID`, `LARK_APP_SECRET`). The pipeline will automatically detect and use it at runtime.

* **Method B: System Integration Configuration**\
  Go to **System Settings → System Integration**, select the corresponding system, and click **Add API Key**.\
  Enter the key and click **Save**. The authorization information will be securely encrypted and stored, and the status will show as **Connected**.

***

### 2. OAuth Authorization (In Development)

OAuth is a standardized authorization protocol suitable for scenarios where users need to access cloud documents or enterprise resources via login.\
XpertAI supports two OAuth authorization modes:

#### Mode A: Default Client (Built-in)

For the SaaS version of XpertAI, some mainstream data sources (such as Lark Docs) have official built-in OAuth client configurations.\
Users only need to click authorize and confirm the permission scope to complete authorization in one click.

#### Mode B: Custom Client

For self-hosted deployments or data sources without built-in configurations, you can register and obtain OAuth Client parameters (`Client ID` and `Client Secret`) on the third-party platform.\
Then, fill in and save these on the **System Settings → System Integration → Add OAuth** page to complete authorization.


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
