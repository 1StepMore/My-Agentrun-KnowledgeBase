---
title: Integrating StarRocks
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
- Xpertai/XpertAI工作流教程-MD版/ai/getting-started/enterprise/docker/with-starrocks.md
---
# Integrating StarRocks

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
