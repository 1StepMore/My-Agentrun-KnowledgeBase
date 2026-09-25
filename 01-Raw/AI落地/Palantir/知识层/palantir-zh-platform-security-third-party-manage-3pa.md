---
title: Palantir 官方文档 · platform-security-third-party · 管理第三方应用程序配置
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/manage-3pa/
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

# 管理第三方应用程序配置

:::callout{theme="warning"}
用户现在被重定向到[**开发者控制台**](/docs/foundry/ontology-sdk/oauth-clients/)以管理他们的应用程序配置。只有在用户未启用**开发者控制台**的情况下，才适用**控制面板**视图。
:::

您可以通过在[第三方应用程序用户界面](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface)中选择应用程序右侧的**操作**下拉菜单中的**管理应用程序**来访问管理应用程序界面。在这里，您可以查看和编辑应用程序的注册信息，如其名称、描述、标识、授权授予类型和应用程序发现设置。

:::callout{theme="neutral"}
**管理应用程序**界面仅对管理第三方应用程序的组织的被授权成员可用。

用户创建应用程序的组织被视为应用程序的管理组织，组织中拥有**管理 OAuth 2.0 客户端**权限的任何人都可以管理第三方应用程序。

管理组织可以通过应用程序发现设置确定哪些其他组织可以查看和使用该第三方应用程序。
:::

以下是为示例应用程序显示的**管理应用程序**页面示例：

![管理应用程序](../../foundry-docs/platform-security-third-party/media/3PA-manage-application-page.png)

## 删除应用程序注册

[危险区域操作](/docs/foundry/platform-security-third-party/danger-zone-actions/)位于**管理应用程序**页面的底部。

![管理应用程序：危险区域](../../foundry-docs/platform-security-third-party/media/3PA-danger-zone.png)

为了永久阻止用户授权第三方应用程序，可以撤销应用程序的注册，即从 Foundry 中删除。

这被视为“危险区域操作”，因为这是不可逆的，并且将使所有用户无法使用该第三方应用程序，除非重新注册应用程序。如果应用程序被重新注册，用户将必须重新授权第三方应用程序，因为 Foundry 将重新注册视为新注册。

了解如何从[危险区域操作文档](/docs/foundry/platform-security-third-party/danger-zone-actions/#delete-an-application-registration)中删除应用程序的注册。
