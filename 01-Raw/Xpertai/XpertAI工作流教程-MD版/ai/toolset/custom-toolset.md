---
title: Custom Toolsets
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
# Custom Toolsets

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Toolsets

A **Custom Toolset** is a collection of tools created and configured by users to meet their specific needs, designed to extend the system's functionality and flexibility. With custom toolsets, users can integrate various services and data sources to address specific business requirements.

Custom toolsets support multiple protocols, including:

* **OpenAPI Protocol**: OpenAPI is a standardized format for describing RESTful APIs. By supporting OpenAPI, custom toolsets can easily integrate with REST-based services, providing standardized interface definitions and interaction methods.

* **OData Protocol**: OData is an open protocol for accessing and querying data. Custom toolsets that support OData can interact with various data sources, offering flexible data query and operation capabilities.

## Custom OpenAPI Toolset

The custom OpenAPI toolset allows users to create toolsets by providing a URL or manually entering a Swagger OpenAPI specification. The system automatically parses the specification, identifying API paths and parameters, simplifying the integration process.

Users only need to provide the URL of the OpenAPI specification or directly input the content in the interface. The system then generates the corresponding interface definitions, enabling users to quickly build and configure custom toolsets.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/custom-toolset-openapi.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=c4ae518d5d3f674eb4d8d4cdf908d5c3" alt="Custom Toolset OpenAPI" width="1882" height="1540" data-path="public/img/ai/custom-toolset-openapi.png" />

## Custom OData Toolset

The custom OData toolset allows users to create toolsets by providing the URL of an OData service or manually entering OData metadata. The system automatically parses the metadata to identify entity sets and generates the corresponding CRUD (Create, Read, Update, Delete) interface definitions, streamlining the integration process.

Users can simply provide the OData service URL or directly input the metadata content in the interface. The system will generate the necessary interface definitions, helping users quickly build and configure custom toolsets.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/custom-toolset-odata.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=9e0674354573cdf54eec7b27467d8745" alt="Custom Toolset OData" width="1766" height="1536" data-path="public/img/ai/custom-toolset-odata.png" />

## Authorization Methods

Custom API toolsets support the following authorization methods:

1. **None**: No authorization required to access the API. This method is suitable for public API interfaces that users can call without providing credentials.

2. **Basic**: Basic authorization using a username and password. Users must include a Base64-encoded combination of the username and password in the request header for authentication.

3. **API Key**: Authorization using an API key. Users must include a specific API key in the request, typically passed through the request header or query parameters, to validate access permissions.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/custom-toolset-authorization-method.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=7d3f282659c2a8a645f78955c2c7f813" alt="Custom Toolset Authorization" width="972" height="704" data-path="public/img/ai/custom-toolset-authorization-method.png" />

These authorization methods provide flexible options to meet the security requirements of different APIs.


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
