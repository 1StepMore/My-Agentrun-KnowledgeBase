---
title: Palantir 官方文档 · platform-security-third-party · 授权第三方应用程序访问
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/authorizing-3pa-access/
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

# 授权第三方应用程序访问

## 授权第三方应用程序

一旦第三方应用程序在Foundry平台中[注册](/docs/foundry/platform-security-third-party/register-3pa/)并[启用](/docs/foundry/platform-security-third-party/enabling-3pa-access/)，授权第三方应用程序访问Foundry的过程就很简单。

:::callout{theme="neutral"}
如果所需的第三方应用程序尚未在Foundry平台中注册和启用，请在继续授权过程之前注册并启用它，或联系您的Palantir代表以请求注册和/或启用。
:::

在此示例中，我们将使用一个简单的测试应用程序来演示授权已注册和启用的第三方应用程序以访问Foundry的工作流程。第三方应用程序可能会提供某种**连接**选项，如下所示。

![示例第三方应用程序](../../foundry-docs/platform-security-third-party/media/3PA-user-example-test-app.png)

尝试连接或授权已注册和启用的第三方应用程序将引导您进入Foundry并打开一个确认屏幕，如下所示，您可以选择**允许**或**不允许**访问。在此确认屏幕上，Foundry将显示第三方应用程序请求权限的操作集；此操作集由第三方应用程序连接器的作者确定。

![示例第三方应用程序：连接对话框](../../foundry-docs/platform-security-third-party/media/3PA-user-connection-dialog.png)

允许访问后，您应被重定向回第三方应用程序，并收到访问权限确认。

### 管理已授权的应用程序

在Foundry的**设置**页面上，**已授权的应用程序**选项卡显示已批准访问的第三方应用程序。此时，我们可以看到测试应用程序已获得访问您账户的权限。

![已授权的应用程序：一个应用程序已授权](../../foundry-docs/platform-security-third-party/media/3PA-user-one-app-authorized.png)

点击**操作**下拉菜单会显示以下选项：**详情**和**撤销**。

![已授权的应用程序：可用操作](../../foundry-docs/platform-security-third-party/media/3PA-user-available-actions.png)

选择**详情**会显示第三方应用程序可以访问的数据的信息。

![已授权的应用程序：访问详情](../../foundry-docs/platform-security-third-party/media/3PA-user-view-details.png)

选择**撤销**会弹出一个确认屏幕；撤销访问将移除应用程序访问您账户信息的能力。

![已授权的应用程序：撤销访问](../../foundry-docs/platform-security-third-party/media/3PA-user-revoke-access.png)

撤销访问后，我们看到没有应用程序被授权访问您的账户。访问被撤销的应用程序可以通过重复此工作流程再次添加。

![已授权的应用程序：没有应用程序被授权](../../foundry-docs/platform-security-third-party/media/3PA-user-no-apps-authorized.png)
