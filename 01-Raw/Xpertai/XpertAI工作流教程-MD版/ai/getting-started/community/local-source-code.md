---
title: Start with Local Source Code
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
# Start with Local Source Code

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Start with Local Source Code

## Prerequisites

<Info>
  Before installing Xpert, ensure your machine meets the following minimum system requirements:

  * CPU >= 2 cores
  * RAM >= 4 GiB
</Info>

## Cloning Xpert

```bash theme={null}
git clone https://github.com/xpert-ai/xpert.git
cd xpert
```

### Starting the Infrastructure

Before enabling business services, we need to deploy PostgreSQL/Redis (if not available locally). You can start them with the following commands:

```bash theme={null}
cd docker
cp env.example .env
docker compose -f docker-compose.infra.yml up -d
```

### Starting the Milvus Service

If you need to use Milvus for knowledge base vector storage and retrieval, please:

* Modify the `VECTOR_STORE` configuration item in the `.env` file, setting it to `milvus`.
* Start the Docker container with the `milvus` configuration file:

```bash theme={null}
docker compose -f docker-compose.infra.yml --profile milvus up -d
```

## Starting the Server and Web Application

Navigate to the project root directory:

* Install the [NodeJs](https://nodejs.org/en/download) LTS version or higher, e.g., 20.x.

* Install [pnpm](https://pnpm.io/installation) (if not already installed) using the command `npm i -g pnpm`.

* Use the command `pnpm bootstrap` to install NPM packages and bootstrap the solution.

* Copy the [`env.local`](./env.local) file to `.env` and adjust the settings in the file for local execution.

* Run the API and UI services using `pnpm start:api` and `pnpm start:cloud`, respectively.

* Open the XpertAI UI in a browser at [http://localhost:4200](http://localhost:4200) (the API runs at [http://localhost:3000/api](http://localhost:3000/api)).

* [Start the onboarding wizard](../onboarding/)...

* Enjoy!

### Hot Reloading

If you want the Node application to automatically restart when file changes are detected in the directory, start the server with the following two commands:

* `pnpm start:api:dev`
* `pnpm start:cloud`

## Using the OLAP Engine

If you want to use the Xpert data analysis platform with the OLAP engine, run the following commands:

* Install the Java runtime and Maven.
* `pnpm start:olap`


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
