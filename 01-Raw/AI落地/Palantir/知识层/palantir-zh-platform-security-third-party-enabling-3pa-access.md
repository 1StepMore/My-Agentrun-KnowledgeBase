---
title: Palantir 官方文档 · platform-security-third-party · 启用第三方应用程序
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/enabling-3pa-access/
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

# 启用第三方应用程序

Foundry 的第三方应用程序启用框架使组织能够控制他们启用的第三方应用程序。组织可以选择启用哪些应用程序，因为启用是特定于组织的；一个组织启用的应用程序集可能包括其他组织管理的应用程序。

因此，一旦第三方应用程序在 Foundry 中注册，它需要为组织启用，组织内的用户才能使用该应用程序。这适用于注册第三方应用程序的组织以及其他组织；应用程序不会自动启用。

应用程序启用后，用户可以执行 [OAuth2 授权流程](/docs/foundry/platform-security-third-party/authorizing-3pa-access/)，以授予 Foundry 访问第三方应用程序的权限。因此，应用程序对 Foundry 资源的访问仍然需要用户明确同意授予访问权限。

## 所需权限

如果您拥有组织的 **管理 OAuth 2.0 客户端** 权限，并且第三方应用程序已对该组织可发现，那么您可以启用该应用程序、编辑该应用程序的启用详细信息或禁用该应用程序。

## 启用或禁用应用程序

通过从 [第三方应用程序用户界面](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface) 中应用程序右侧的 **操作** 下拉菜单中选择 **启用设置** 来访问启用设置界面。

以下是示例应用程序的启用设置界面：

![启用设置页面](../../foundry-docs/platform-security-third-party/media/3PA-enablement-settings-page.png)

在这里，您可以使用页面顶部的切换按钮 **启用** 或 **禁用** 您的应用程序。

:::callout{theme="danger" title="警告"}
禁用应用程序并不是简单的开关操作，因为重新启用应用程序需要再次完成应用程序启用工作流程。现有的应用程序授权将不会重新激活，每个用户必须重新授权新启用的应用程序。
:::

### 项目访问

您还可以设置应用程序的项目访问范围。项目访问范围决定了在代表 Foundry 用户通过授权代码授予授权时，应用程序可以访问的项目。

* 连接到 Foundry 的第三方应用程序可以访问的资源范围受两个因素限制：
  * 授权用户可以访问的项目，以及
  * 在启用界面上定义的项目。
* 应用程序只能访问授权用户可以访问的项目与启用界面上指定的项目的交集。换句话说，启用界面提供了一种缩小应用程序对 Foundry 访问范围的方法。
* 我们建议将项目范围设置为 **不受限制**，这将授予应用程序访问授权用户可以访问的所有资源的权限。

### 权限标记限制

设置应用程序数据访问范围的另一种方法是通过权限标记限制。通过将 [权限标记](/docs/foundry/security/markings/) 应用到您的应用程序，您可以确定在代表 Foundry 用户通过授权代码授予授权和/或通过客户端凭证授予服务用户授权时，应用程序将可以访问的资源。

* 连接到 Foundry 的第三方应用程序可以访问的资源范围受两个因素限制：
  * 授权用户和/或服务用户可以访问的资源，以及
  * 通过启用界面应用的权限标记。
* 应用程序只能访问用户可以访问的资源与通过启用界面指定的权限标记允许的资源的交集。需要注意的是，即使访问受限，未标记的资源仍可能被利用，除非用户被拒绝访问这些资源。
* 我们建议将权限标记限制设置为 **不受限制**，这将授予应用程序访问授权用户和/或服务用户可以访问的所有资源的权限。

### 组织级别同意

在高级启用设置中，您可以代表组织的用户授权第三方应用程序访问 Foundry。

如果启用，用户将不需要执行 [OAuth2 授权流程](/docs/foundry/platform-security-third-party/authorizing-3pa-access/)，第三方应用程序将被授权访问该组织中所有用户的 Foundry。启用此功能时，用户不会收到通知。

:::callout{theme="neutral"}
我们建议不要启用组织级别同意，除非您的应用案例明确要求这样做。
:::
