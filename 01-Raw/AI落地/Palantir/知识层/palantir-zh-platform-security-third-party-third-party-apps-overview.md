---
title: Palantir 官方文档 · platform-security-third-party · third-party-apps-overview
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/third-party-apps-overview/
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

# 概述

Foundry 平台的安全控制确保第三方应用程序的集成和互操作性可以在尊重既定安全措施的同时进行集中管理。第三方应用程序授权支持 [OAuth 2.0 框架](/docs/foundry/platform-security-third-party/writing-oauth2-clients/)。

第三方应用程序权限应由 Foundry 管理员管理，以确保 Foundry 平台的安全性。[控制面板](/docs/foundry/administration/control-panel/)中的第三方应用程序界面使 Foundry 管理员能够查看哪些应用程序已在 Foundry 上注册，以及哪些应用程序已被启用以供访问。在第三方应用程序界面中，管理员可以[注册新应用程序](/docs/foundry/platform-security-third-party/register-3pa/)、[管理现有应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)以及[启用或禁用应用程序](/docs/foundry/platform-security-third-party/enabling-3pa-access/)。

## 访问第三方应用程序用户界面

对于具有适当权限的用户，可以通过点击位于左侧导航栏下角的 **打开其他工作区 > [控制面板](/docs/foundry/administration/control-panel/)** 来进入第三方应用程序管理界面。然后，选择一个注册和相关的组织，最后在**组织设置**下选择**第三方应用程序**标签。

![Third-party applications tab](../../foundry-docs/platform-security-third-party/media/3pa-0.png)

用户必须在所选组织中拥有 **第三方应用程序管理员** 角色才能访问第三方应用程序管理界面。

![Third-party applications permissions](../../foundry-docs/platform-security-third-party/media/3PA-permissions.png)

有关更多详细信息，请查看[控制面板中的权限](/docs/foundry/administration/enrollments-and-organizations-permissions/)。
