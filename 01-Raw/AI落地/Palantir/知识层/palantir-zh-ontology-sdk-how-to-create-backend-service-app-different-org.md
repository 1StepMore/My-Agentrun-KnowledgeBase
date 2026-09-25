---
title: Palantir 官方文档 · ontology-sdk · 使用不同的组织创建应用程序
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/how-to-create-backend-service-app-different-org/
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

# 使用不同的组织创建应用程序

在开发者控制台中开发使用机密客户端的服务或应用程序时，将会创建一个服务用户与您的应用程序一起使用。创建后，您必须授予服务用户读取和写入Ontology的必要权限。

默认情况下，服务用户将作为开发者控制台中所选组织的访客添加，如下图所示。

![开发者控制台是您作为访客的组织的一部分。](../../foundry-docs/ontology-sdk/media/guest-org-ontology-scopes.png)

但是，如果该组织与您的默认组织不同，您将无法看到该用户或授予其权限，直到您完成以下两个步骤：

1. [与您的组织共享应用程序](#share-the-application-with-your-organization)
2. [在您的组织上启用应用程序](#enable-the-application-on-your-organization)

## 与您的组织共享应用程序

按照以下步骤准备您的应用程序以供您的组织使用：

1. 在控制面板中，选择应用程序使用的组织（在下图中以红色标出）。
2. 选择您的应用程序，并使用 **应用程序发现** 界面将您的组织添加到列表中并保存您的更改。

![控制面板中的应用程序发现列表，已添加Palantir组织。](../../foundry-docs/ontology-sdk/media/developer-console-left-sidebar.png)

## 在您的组织上启用应用程序

一旦您与默认组织共享了应用程序，您可以切换回您的默认组织并再次找到该应用程序。

1. 打开控制面板中的 **第三方应用程序** 页面并找到您的应用程序。

![第三方应用程序显示在您的组织中](../../foundry-docs/ontology-sdk/media/control-panel-guest-org.png)

2. 选择 **操作**，然后选择 **启用设置**。
3. 在页面顶部，切换打开 **启用应用程序**。

![控制面板中已启用的应用程序，具有配置项目访问和权限标记限制的选项。](../../foundry-docs/ontology-sdk/media/control-panel-enable-app.png)

一旦您保存更改，服务用户将作为访客添加到您的组织中，您将能够授予任何必要的权限。
