---
title: Palantir 官方文档 · ontology-sdk · OAuth 客户端
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/oauth-clients/
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

# OAuth 客户端

:::callout{theme="neutral"}
OAuth 客户端，前称为 [**控制面板**](/docs/foundry/platform-security-third-party/third-party-apps-overview/) 中的第三方应用程序，现在在 **开发者控制台** 中创建和管理。
:::

在 OAuth 客户端可以连接到 Foundry 之前，必须在 Foundry 平台上注册。初始注册过程会为第三方应用程序创建一个名称、客户端 ID 和客户端密钥；有关客户端 ID 和客户端密钥的更多信息，请参见 [OAuth.com 文档 ↗](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/)，这些用于授权工作流程。然后，需要为授权过程配置一个重定向 URL，以及用于应用程序平台内表示的名称、描述和图标。

## 在开发者控制台中创建 OAuth 客户端

在开发者控制台中创建 OAuth 客户端的过程使用与 [Ontology SDK 应用程序](/docs/foundry/ontology-sdk/create-a-new-osdk/) 相同的创建流程。

在创建向导的 **Ontology & 资源范围** 步骤中，选择 **不，我不会使用 Ontology SDK** 来创建 OAuth 客户端。

## 在开发者控制台中管理 OAuth 客户端

[导航到 OAuth 客户端列表](/docs/foundry/ontology-sdk/navigation/) 并选择要管理的客户端。请注意，您必须在 OAuth 客户端所属组织中拥有 **管理 OAuth 2.0 客户端** 权限才能管理 OAuth 客户端。

现在您将看到 **概述** 页面，您可以在此编辑应用程序详细信息，例如应用程序名称、描述和徽标。如果您展开 **危险区域**，还可以选择删除应用程序。

![OAuth 客户端 "概述" 页面](../../foundry-docs/ontology-sdk/media/oauth-client-overview.png)

在这里，您可以导航到 **OAuth & 权限** 页面，在此查看和管理客户端详细信息。您还可以选择与其他组织共享该应用程序，这将允许他们为自己的用户启用该应用程序。

![OAuth 客户端 "OAuth & 权限" 页面](../../foundry-docs/ontology-sdk/media/oauth-client-oauth.png)
