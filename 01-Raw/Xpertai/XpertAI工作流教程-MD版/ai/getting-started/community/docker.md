---
title: Deploy with Docker Compose
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
# Deploy with Docker Compose

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy with Docker Compose

## Prerequisites

<Info>
  Before installing Xpert, ensure your machine meets the following minimum system requirements:

  * CPU >= 2 cores
  * RAM >= 4 GiB
</Info>

## Clone Xpert

```bash theme={null}
git clone https://github.com/xpert-ai/xpert.git
cd xpert
```

## Start Xpert

1. Navigate to the Docker directory in the Xpert source code

```bash theme={null}
cd docker
```

2. Copy the environment configuration file

```bash theme={null}
cp env.example .env
```

3. Start the Docker containers

```bash theme={null}
docker compose up -d
```

After executing the command, you should see output similar to the following, showing the status and port mappings of all containers:

```bash theme={null}
 ✔ Network xpert-ai_default         Created                  0.0s 
 ✔ Container xpert-ai-db-1          Started                  0.0s 
 ✔ Container xpert-ai-redis-1       Started                  0.0s 
 ✔ Container xpert-ai-api-1         Started                  0.0s 
 ✔ Container xpert-ai-webapp-1      Started                  0.0s
```

Finally, check if all containers are running successfully:

```bash theme={null}
docker compose ps
```

This includes two core services: api / webapp, and two dependency components: db / redis.

```bash theme={null}
NAME                IMAGE                                       COMMAND                  SERVICE   CREATED         STATUS                   PORTS
xpert-ai-api-1      ghcr.io/xpert-ai/xpert-api:latest           "docker-entrypoint.s…"   api       4 minutes ago   Up 4 minutes             0.0.0.0:3000->3000/tcp
xpert-ai-db-1       pgvector/pgvector:pg12                      "docker-entrypoint.s…"   db        4 minutes ago   Up 4 minutes (healthy)   5432/tcp
xpert-ai-redis-1    redis/redis-stack:latest                    "sh -c 'redis-server…"   redis     4 minutes ago   Up 4 minutes             6379/tcp, 8001/tcp
xpert-ai-webapp-1   ghcr.io/xpert-ai/xpert-webapp:latest        "./entrypoint.compos…"   webapp    4 minutes ago   Up 4 minutes             0.0.0.0:80->80/tcp, 443/tcp
```

### Enable BI Service

If you need to enable multidimensional modeling for data analysis, start the Docker containers with the `bi` profile:

```bash theme={null}
docker compose --profile bi up -d
```

### Start Milvus Service

If you need to use Milvus for knowledge base vector storage and retrieval:

* Modify the `VECTOR_STORE` configuration item in the `.env` file, setting it to `milvus`. Also, configure the Milvus account with `MILVUS_USER` and `MILVUS_PASSWORD`.
* Start the Docker containers with the `milvus` profile:

```bash theme={null}
docker compose --profile milvus up -d
```

### Start Crawl4AI service

If you need to use [Rawl4AI](/docs/ai/tool/mcp/crawl4ai) To crawl web data, please add the 'crawl4ai' configuration when executing the Docker compose command:

```bash theme={null}
docker compose --profile crawl4ai up -d
```

## Access Xpert AI

Visit the [initialization page](../onboarding/) to set up the admin account and tenant:

```bash theme={null}
# Local environment
http://localhost/

# Server environment
http://your_server_ip/
```

Change the base URL in the `.env` file to the server address when deploying Xpert AI in a server environment.

```ini theme={null}
API_BASE_URL=//your_server_ip:3000
CLIENT_BASE_URL=//your_server_ip
```

## Custom Configuration

Directly edit the environment variable values in the `.env` file. Then, restart Xpert:

```bash theme={null}
docker compose down
docker compose up -d
```

## Upgrade

Navigate to the docker directory in the Xpert source code and execute the following commands:

```bash theme={null}
cd xpert/docker
docker compose down
git pull origin main
docker compose pull
docker compose up -d
```

### Sync Environment Variable Configuration (Important)

* If the `env.example` file has been updated, be sure to modify your local `.env` file accordingly.
* Check and adjust the configuration items in the `.env` file as needed to ensure they match your actual environment. You may need to add any new variables from `env.example` to your `.env` file and update any changed values.

## Read More

If you have any questions, refer to the [FAQ](./faqs/).


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
