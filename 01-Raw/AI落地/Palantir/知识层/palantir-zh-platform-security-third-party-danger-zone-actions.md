---
title: Palantir 官方文档 · platform-security-third-party · 危险区域操作
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/danger-zone-actions/
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

# 危险区域操作

Foundry平台管理员可以对第三方应用程序执行多个“危险区域”操作。这些操作被称为“危险区域”操作，因为它们会对应用程序的注册造成不可逆转的更改，并且由于其潜在的广泛和破坏性影响，应谨慎对待。在执行这些操作之前，会出现一个警告对话框。可用的“危险区域”操作有[旋转客户端密钥](#rotate-a-client-secret)和[删除应用程序注册](#delete-an-application-registration)。

## 旋转客户端密钥

您可以仅在[管理应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)页面为[机密客户端 ↗](https://tools.ietf.org/html/rfc6749#section-2.1)旋转应用程序的密钥。旋转密钥将要求每位用户重新设置应用程序，因为每个配置了该密钥的客户端将停止工作，因为旋转后的密钥已失效。仅在密钥已被泄露或丢失时才应进行密钥旋转；请记住，密钥旋转后需要重新设置应用程序。

:::callout{theme="warning" title="警告"}
您何时可能需要旋转密钥？鉴于旋转密钥的后果，这仅应在密钥被泄露或无法访问时进行。
:::

1. 从**控制面板**导航到[第三方应用程序](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface)页面。
2. 点击您想要修改的应用程序的**操作**，然后点击**管理应用程序**。
3. 向下滚动并点击**旋转密钥**。
4. 在确认操作之前，查看警告对话框。
5. 确认操作并安全存储您的新客户端密钥，因为之后将无法再次查看。

## 删除应用程序注册

1. 从**控制面板**导航到[第三方应用程序](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface)页面。
2. 点击您想要删除的应用程序的**操作**，然后点击**管理应用程序**。
3. 向下滚动并点击**删除应用程序**。
4. 在确认操作之前，查看警告对话框。
5. 确认操作，应用程序将被删除。这不能被撤销。
