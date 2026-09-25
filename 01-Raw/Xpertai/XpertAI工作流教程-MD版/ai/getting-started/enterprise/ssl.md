---
title: Ssl
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
# Ssl

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Ssl

# SSL

## Enable HTTPS Service

If you need to enable HTTPS service for this system, you can do so with the following configuration:

* Obtain the certificate files and place them in the `volumes/webapp/ssl` directory, with the filenames `server.crt` and `server.key`.
* Place the custom Nginx configuration file in the `volumes/webapp/conf` directory, with the filename `nginx.conf`, configured as follows

```
user  nginx;
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
  worker_connections 1024;
}

http {
  include /etc/nginx/mime.types;
  
  log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

  access_log  /var/log/nginx/access.log  main;

  #gzip  on;

  upstream api {
    server api:3000;
  }

  server {
    listen              80;
    listen              443 ssl;
    ssl_certificate     /webapp/ssl/server.crt;
    ssl_certificate_key /webapp/ssl/server.key;

    location / {
      root /srv/pangolin;
      try_files $uri $uri/ /index.html;
    }

    location /api/ {
      proxy_pass http://api;
      proxy_set_header Host $http_host;
      proxy_connect_timeout       5s;
      proxy_read_timeout          600s;
    }
    location /public/ {
      proxy_pass http://api;
      proxy_set_header Host $http_host;
      proxy_connect_timeout       5s;
      proxy_read_timeout          30s;
    }
  }
}
```

* Specify the nginx configuration file: change `command: ['nginx', '-g', 'daemon off;']` to `command: ['nginx', '-g', 'daemon off;', '-c', '/webapp/conf/nginx.conf']`
* Modify the ports configuration to open port 443: `- "443:443"`
* Change `API_BASE_URL` in the `.env` file to `//your.domain`.
* Change `WEBAPP_PORT` in the `.env` file to `443`. If you want to enable both (80/443), you can remove this variable.

Restart the service to apply the changes.

For more technical details, please refer to [Enable HTTPS - \[ocap wiki\]](https://github.com/meta-d/ocap/wiki/Https)


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
