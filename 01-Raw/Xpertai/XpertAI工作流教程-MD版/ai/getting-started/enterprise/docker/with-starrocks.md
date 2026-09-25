---
title: Integrating StarRocks
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
# Integrating StarRocks

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating StarRocks

Deploying the Xpert analytics cloud together with StarRocks cluster in a Docker Cluster can quickly establish a data analytics platform.

## Preparation

Execute the following command on the host machine:

```
sysctl -w vm.max_map_count=2000000
```

## Installation and Deployment

Please download the installation script we provided:

```bash theme={null}
git clone https://github.com/meta-d/installer.git
```

Then, under the docker directory, first configure the environment variable file `.env`:

```bash theme={null}
cd installer/docker
cp env.tmpl .env
```

* Set the value of **INSTALLATION\_MODE** to **with-starrocks**
* Other password fields can be reset as needed

Finally, execute the following command to start the service:

```bash theme={null}
docker-compose -f docker-compose-with-starrocks.yml up -d
```

Once the service is started, access [http://localhost/](http://localhost/) to see the login page of the Xpert analytics platform.

## 1 FE x 1 BE

Deploying one frontend service and one backend service on a single node, this deployment method is suitable for small-scale data analysis scenarios.

Download the installer project code, and execute the following command under the docker directory to start the service:

```bash theme={null}
docker-compose -f docker-compose-with-doris.yml up -d
```

## 3 FE x 3 BE

Deploying three frontend services, three backend services, and a load-balanced reverse proxy service on a single node, this deployment method is suitable for large-scale data analysis scenarios. The number of services and network structure can be adjusted according to actual needs.

Download the installer project code, and execute the following command under the docker directory to start the service:

```bash theme={null}
docker-compose -f docker-compose-with-doris-fe3xbe3.yml up -d
```


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
