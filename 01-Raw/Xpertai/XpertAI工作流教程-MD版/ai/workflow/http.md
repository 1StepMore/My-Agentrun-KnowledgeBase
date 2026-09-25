---
title: HTTP Request
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
# HTTP Request

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# HTTP Request

The **HTTP Request** node is a key component in the XpertAI platform's agent workflow, enabling flexible external API calls within agent processes to facilitate data interaction, automated triggers, and complex system integrations.

## 📌 Feature Overview

The HTTP Request node supports initiating standard web requests (e.g., GET, POST) in workflows, allowing seamless integration with any service supporting the HTTP protocol. Whether fetching data, submitting forms, or triggering third-party system commands, this node handles it effortlessly.

## 🔧 Configuration Details

After dragging an HTTP Request node into the workflow, you can configure it in the right panel as follows:

### 1. Request Method and URL (API)

* **Method Type**: Supports common HTTP methods like `GET`, `POST`, `PUT`, `DELETE`, etc.
* **Request URL**: Enter the full API address, e.g., `https://api.example.com/data`.

### 2. Headers

Add multiple header key-value pairs to pass information like authentication tokens or content types.

* **Name**: Header name, e.g., `Authorization`.
* **Value**: Header value, e.g., `Bearer {{access_token}}`.

### 3. Params (Query Parameters)

Set URL parameters, ideal for GET requests or appending query strings.

* **Key**: Parameter name.
* **Value**: Parameter value (supports dynamic variables).

### 4. Body (Request Body)

Used for requests like POST or PUT that include a body.

* Supported formats:
  * `x-www-form-urlencoded`
  * `JSON`
  * `RAW`
* Enter specific fields or bind variables for dynamic data.

### 5. Timeout Settings

Fine-tune settings for network conditions or slow API responses:

* **Connection Timeout**: Time limit for establishing a connection (seconds).
* **Read Timeout**: Time limit for reading data (seconds).
* **Write Timeout**: Time limit for sending data (seconds).

### 6. Output Variables

The HTTP Request node outputs three default session variables:

* `body`: Response body.
* `status_code`: Response status code.
* `headers`: Response headers.

### 7. Error Handling

Refer to [Error Handling](/docs/ai/workflow/error-handling/).

## ✅ Usage Example

For instance, to automatically call a weather API in a node, configure as follows:

* Method: GET
* URL: [https://api.weatherapi.com/v1/current.json](https://api.weatherapi.com/v1/current.json)
* Params:
  * `key`: `{{weather_api_key}}`
  * `q`: `{{user_location}}`
* No request body required
* Timeout: Use default or customize as needed

## 🚀 Use Cases

* Call internal enterprise systems or third-party APIs.
* Enable data synchronization or notification pushes.
* Integrate with tools like CRM, ERP, WeChat Work, or Slack.
* Expand agent capabilities for more powerful automation logic.


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
