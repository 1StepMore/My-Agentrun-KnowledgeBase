---
title: FAQs
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
# FAQs

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs

## 1. Domain Configuration

If you need to customize the domain for system access, please modify the following environment variables (in the `.env` file): `API_BASE_URL` and `CLIENT_BASE_URL`.\
Additionally, if you need to change the port numbers, modify `API_PORT` or `WEB_PORT`.\
Ensure that the port numbers in `API_BASE_URL` and `CLIENT_BASE_URL` match those specified in `API_PORT` and `WEB_PORT`.

For example, if your domain is `example.com` and the ports for the backend and frontend are `90` and `3001` respectively, then:

`API_BASE_URL` = `//example.com:3001`\
`CLIENT_BASE_URL` = `//example.com:90`

## 2. How to Send Emails?

To use the system's email sending functionality, you need to configure an email server.

* Refer to [Environment Variables - Email-Related Configuration](/docs/getting-started/community/environments).
* Alternatively, configure the email service settings for a tenant or organization within the system. [Custom SMTP](/docs/server/tenant/smtp)

## 3. Custom File Storage Location

When using the system, files uploaded by users are stored in the server’s local file storage by default. Administrators can change this to a network provider’s file storage service through:

* [Environment Variables](/docs/getting-started/community/environments)
* Or [Tenant Configuration](/docs/server/tenant/manage)

You can choose between **Alibaba Cloud Storage** and **Amazon Cloud Storage**.\
After selecting the storage service type, configure the corresponding authentication information.


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
