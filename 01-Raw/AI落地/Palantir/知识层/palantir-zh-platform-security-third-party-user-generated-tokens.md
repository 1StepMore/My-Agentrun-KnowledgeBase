---
title: Palantir 官方文档 · platform-security-third-party · 用户生成的词元
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/user-generated-tokens/
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

# 用户生成的词元

:::callout{theme="danger" title="危险"}
这些词元与您个人的Foundry用户账户相关联，**不得在生产应用程序中使用或提交到共享或公共代码库中**。
我们建议您在开发期间将测试API词元存储为环境变量。
以授权生产应用程序，[注册一个OAuth2应用程序](/docs/foundry/platform-security-third-party/third-party-apps-overview/)。
:::

## 概述

Foundry支持基于词元的身份验证。词元是字符的字符串，用作特定用户的安全标识。拥有这些词元相当于拥有用户的用户名和密码，因此应安全保管并保密。

## 生成

词元从设置仪表盘中生成。导航到侧边栏底部的**账户**，点击**设置**，然后点击**词元**。

![词元仪表盘](../../foundry-docs/platform-security-third-party/media/token_dashboard.png)

此界面显示为当前用户创建的用户生成词元以及其当前状态和到期日期的信息。可以从此界面禁用现有词元，这将暂时停用它们，或撤销它们，这将永久失效。要生成新词元，点击**创建词元**。这将打开一个词元创建对话框：

![词元创建](../../foundry-docs/platform-security-third-party/media/token_creation.png)

为词元赋予一个有用的名称，提供描述，并指定词元应过期的日期。点击**生成**后，词元将只显示一次以确保安全。可以根据需要复制使用，但不应以任何不安全的方式存储。

## 撤销

您可以在同一界面通过点击**撤销**来撤销单个词元。

![词元撤销](../../foundry-docs/platform-security-third-party/media/token_revoke.png)

## 不活跃用户

默认情况下，Foundry用户账户在用户30天未登录后自动停用。当用户被停用时，用户生成的API词元和发给OAuth2客户端的词元将变为无效。

否则，用户将显示为完全活跃，并且由该用户安排的工作将继续运行。例如，不活跃用户拥有的计划将继续运行。

要重新激活用户，他们只需再次登录Foundry。

特定用户可以免于自动停用。有关这方面的更多信息，请联系您的Palantir代表。
