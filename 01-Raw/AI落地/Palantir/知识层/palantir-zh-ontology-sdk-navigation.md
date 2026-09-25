---
title: Palantir 官方文档 · ontology-sdk · 导航
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/navigation/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:24:14+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# 导航

开发者控制台是Foundry中的一个应用程序，帮助您通过Ontology SDK在代码中利用Foundry Ontology进行应用程序开发，以及OAuth客户端（前称为[控制面板](/docs/foundry/platform-security-third-party/third-party-apps-overview/)中的第三方应用程序）。

## 启用开发者控制台

要访问开发者控制台，您必须在控制面板的**Foundry Suite**部分启用开发者控制台。如果您没有权限启用开发者控制台，请联系您的Palantir代表以获取帮助。

然后，开发者控制台将出现在[应用程序门户](/docs/foundry/app-building/curating-apps/)中。

![访问开发者控制台](../../foundry-docs/ontology-sdk/media/developer-console-landing.png)

## 开发者控制台主页

开发者控制台主页列出了您有权限访问的所有应用程序。

欲了解更多信息，请查看[权限文档](/docs/foundry/ontology-sdk/permissions/#user-permissions)。

开发者控制台主页还列出了您有权限访问的所有OAuth客户端。这是您主要和来宾组织中所有拥有**管理OAuth 2.0客户端**权限的OAuth客户端列表。

![开发者控制台主页 OAuth 客户端](../../foundry-docs/ontology-sdk/media/oauth-client-overview.png)

## Ontology SDK应用程序概览

在应用程序概览页面，您可以执行以下操作：

* 查看应用程序使用的ontology资源数量。
* 与团队中的其他开发人员共享应用程序。
* 编辑显示信息。
* 删除应用程序。

![开发者控制台中的应用程序概览页面](../../foundry-docs/ontology-sdk/media/app-overview.png)

关于OAuth客户端概览页面的信息，请参见[**在开发者控制台中管理OAuth客户端**](/docs/foundry/ontology-sdk/oauth-clients/#managing-an-oauth-client-in-developer-console)。

## API文档

默认情况下，每个Ontology SDK应用程序都附带了定制的API文档，该文档针对SDK内容量身定制。要访问，请从左侧面板选择**API文档**。

此API文档包括如何安装应用程序特定的SDK、加载选定的Object类型和应用操作的指南。文档还包含参考资料，描述了基于这些实体的属性和功能的每个Ontology Object类型、操作类型和函数可用的方法。

使用左上角的下拉菜单可以在支持的语言之间切换您的API文档。

从左侧的菜单中，您可以导航到**应用程序SDK**页面来配置和生成新的SDK版本。

## OAuth和范围

从左侧菜单导航到**OAuth和范围**页面，以配置您的应用程序的身份验证流程。您还可以查看和更改**资源访问范围**，以确保授予用户的词元允许他们访问应用程序所需的所有相关资源（且不超过必要的资源）。

了解更多关于[配置权限](/docs/foundry/ontology-sdk/permissions/)的信息。

![OAuth和范围配置选项](../../foundry-docs/ontology-sdk/media/oauth-scopes-page.png)

## 共享和词元

在**共享和词元**页面，您可以配置不同的共享选项并生成长期有效的词元以供用户访问。

## Web托管

Web托管是一个仅限前端应用程序（如React单页应用程序（SPA））的部署选项。

通过Web托管，您可以在您的Foundry实例中为用户提供您以Ontology SDK搭建的前端应用程序，消除为您的应用程序配置额外托管服务（如内部节点服务器、GitHub页面等）的需求。

![Web托管部署选项](../../foundry-docs/ontology-sdk/media/hosting.png)

更多详细信息，请查看[在Foundry上部署Ontology SDK应用程序（Beta）](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/)文档。

## 应用程序指标

:::callout{theme="neutral"}
应用程序指标功能处于[测试状态](/docs/foundry/platform-overview/development-life-cycle/#beta)，在您的注册中可能不可用。
:::

应用程序指标提供了对请求数量、请求成功率和调用API端点的延迟情况的洞察。

![应用程序指标](../../foundry-docs/ontology-sdk/media/metrics.png)

[了解更多关于应用程序指标的信息。](/docs/foundry/ontology-sdk/application-metrics/)
