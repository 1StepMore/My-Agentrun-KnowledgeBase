---
title: Self-Built Application Configuration
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
# Self-Built Application Configuration

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Self-Built Application Configuration

Customers can seamlessly showcase ChatBI's capabilities to users through the **bot** in **Feishu's Enterprise Self-Built Applications**, enabling **real-time data** analysis in conversational BI. Within the Feishu client, users can directly interact with ChatBI using natural language to query and analyze data from SAP systems or data warehouses. Users can easily perform **collaborative** data queries and business analysis within the familiar Feishu environment without switching applications, significantly improving work efficiency and decision-making speed.

## Enterprise Self-Built Applications

**Feishu Enterprise Self-Built Applications** refer to applications developed and deployed by enterprises using the open interfaces and development tools provided by the Feishu platform. These applications can be customized to meet specific business processes, team collaboration, information management, and other internal needs of the enterprise.

To access the developer backend of the Feishu Open Platform:
[https://open.feishu.cn/app](https://open.feishu.cn/app)

Click on **Create Enterprise Self-Built Application**, enter the application name and information to create it successfully, then add the **bot** capability in **Add Application Capability**, and navigate to the bot configuration page:

## Bot Settings

Input basic information such as “How to get started.” Click to go to **Events and Callbacks** to add the “Card Callback Interaction” callback for the card.

### Event Configuration

To receive message events sent by Feishu, you first need to configure the event request address:

`<Your server>/api/lark/webhook/<id>`

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/webhook.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=3d22d34785d42427e354171dfaa3e1bd" alt="Webhook" width="1682" height="878" data-path="public/img/chatbi/webhook.png" />

* Refer to the “Callback Address” attribute in [System Integration - Feishu Integration Configuration](/docs/server/organization/integration).

Add events and enable the corresponding permissions:

* `im.message.receive_v1` Receive messages v2.0
* `application.bot.menu_v6` Custom bot menu events v2.0

### Callback Configuration

Request address (same as the event configuration request address):
`<Your server>/api/lark/webhook/<id>`

Subscribed callbacks:

* `card.action.trigger` Card Callback Interaction

### Permission Management

The following permissions need to be enabled for this self-built application:

* `im:message:send_as_bot`
* `contact:contact.base:readonly`
* `contact:user.email:readonly`
* `contact:user.phone:readonly`
* `contact:user.employee_id:readonly`

### Custom Bot Menu

If you want to configure a model switching function in the custom bot menu, add the menu according to the following rule:

`select_model:e7dc6846-c893-411a-90a2-0885a45fd5f1`

Replace the uuid with the corresponding dialog model's id.

## System Settings

### Environment Configuration

When installing and deploying the system, configure the role name, which is the role initially assigned to the user created automatically by Feishu.

```ini title="File .env" theme={null}
LARK_ROLE_NAME=VIEWER
```

### Data Source

Taking the SAP system as an example, create a data source that connects to the S/4HANA system.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/sap-s4hana-data-source.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=4b71dad39a008071abc7cdf0410059a2" alt="SAP S/4HANA Data Source" width="1590" height="1522" data-path="public/img/chatbi/sap-s4hana-data-source.png" />

### Semantic Model

By connecting the data source of the S/4HANA system, create a semantic model for the cubes or individual queries in the SAP system, and interface it to ChatBI after semantic enhancement.

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/sap-s4hana-semantic-model.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=426cca632b69c397e6d322b21fbb3686" alt="SAP S/4HANA Semantic Model" width="1380" height="1452" data-path="public/img/chatbi/sap-s4hana-semantic-model.png" />

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/sap-cube-semantic-enhance.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=230af57fdaa4e6d864649281278d17d8" alt="SAP S/4HANA Cube" width="3024" height="1714" data-path="public/img/chatbi/sap-cube-semantic-enhance.png" />

### Configure Model for ChatBI Bot

Configure the enhanced SAP Cube semantic model or the self-developed data warehouse semantic model into the ChatBI service so that the Feishu bot can view and analyze it.

Refer to [Dialog Models](../models/).

References:

* [https://open.feishu.cn/document/home/qr-code-scanning-login-for-web-app/introduction](https://open.feishu.cn/document/home/qr-code-scanning-login-for-web-app/introduction)


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
