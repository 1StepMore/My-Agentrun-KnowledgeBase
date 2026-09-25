---
title: Palantir 官方文档 · platform-security-third-party · 注册第三方应用程序
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/register-3pa/
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

# 注册第三方应用程序

:::callout{theme="warning"}
用户现在被重定向到[**开发者控制台**](/docs/foundry/ontology-sdk/oauth-clients/)以注册新的应用程序配置。只有当用户未启用**开发者控制台**时，才适用**控制面板**视图。
:::

在第三方应用程序连接到Foundry之前，必须在Foundry平台上注册。初始注册过程会为第三方应用程序创建一个名称、一个客户端ID和一个客户端密钥；有关客户端ID和客户端密钥的更多信息，请参阅[OAuth.com文档 ↗](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/)，这些在授权工作流程中被用于在。然后，需要为第三方应用程序配置一个用于授权过程的重定向URL，以及一个名称、描述和图标，这些用于第三方应用程序在平台内的表示。

## 注册

1. 要开始注册新应用程序的过程，请导航到**控制面板**中的**第三方应用程序**选项卡，然后单击**新应用程序**。

![注册新第三方应用程序](../../foundry-docs/platform-security-third-party/media/3PA-new-application-button.png)

2. 这将打开**注册新应用程序**向导。将按以下顺序有四个步骤：**详细信息**、**客户端类型**、**授权授予类型**和**摘要**。

![创建应用程序向导](../../foundry-docs/platform-security-third-party/media/create-wizard.png)

3. 在**详细信息**步骤中，为您的应用程序提供名称、描述（非必填）和徽标（非必填）。
4. 在**客户端类型**步骤中，指定应用程序的客户端类型。客户端类型指的是OAuth2标准，涉及客户端应用程序是否可以安全地存储密钥。客户端类型的两个选项是：
   * [机密客户端 ↗](https://tools.ietf.org/html/rfc6749#section-2.1)：这适用于能够安全持有其凭据的客户端；例如，在受限访问客户端凭据的安全服务器上实现的客户端。此客户端类型支持用于授权的[授权代码授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#authorization-code-grant)和[客户端凭据授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant)选项。
   * [公共客户端 ↗](https://tools.ietf.org/html/rfc6749#section-2.1)：这适用于不能安全持有其凭据的客户端；例如，授权客户端在网页浏览器本身上运行的基于浏览器的应用程序。此客户端类型支持带PKCE的[授权代码授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#authorization-code-grant)，这意味着需要使用`code_verifier`和`code_challenge`参数。[客户端凭据授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant)不被支持。 <br><br>有关这些客户端类型的更多信息，请参阅[编写OAuth2客户端](/docs/foundry/platform-security-third-party/writing-oauth2-clients/)的文档。

:::callout{theme="warning" title="警告"}
原生或单页应用程序，如移动应用程序，被分发给用户进行部署。因此，应用程序的二进制文件是可用的，并且可以被反编译以提取客户端密钥。然后，客户端密钥可能被用于在攻击中冒充授权用户。[代码交换证明密钥（PKCE）↗](https://oauth.net/2/pkce/)用于防止此类攻击。
:::

5. 在**授权授予类型**步骤中，您将看到上一步中选择的客户端类型支持的授予类型。如果您选择启用[授权代码授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#authorization-code-grant)，您将需要指定至少一个**重定向URL**。

   * 在授权过程中，OAuth2使用浏览器重定向将用户从授权提供者（在本例中为Foundry）发送回用户尝试授权的客户端（在本例中为第三方应用程序）。因此，指定重定向URL有助于在第三方应用程序请求访问Foundry资源的权限时提供额外的安全性。
   * 请注意，重定向URL可以在[管理应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)屏幕中稍后更新。

   如果您选择启用[客户端凭据授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant)（这仅对机密客户端可用），将为应用程序创建一个服务用户。该服务用户可以被授权以应用程序名义访问Foundry资源的请求。

6. 在**摘要**步骤中，将显示所提供的所有信息的概述以及仍需提供的任何缺失部分。当必填字段完成时，您可以点击屏幕右下角的**注册应用程序**。

7. 提交后，将向您显示新创建的客户端的ID和密钥（如适用）。

![成功注册应用程序](../../foundry-docs/platform-security-third-party/media/3PA-registered-page.png)

:::callout{theme="warning" title="警告"}
如果使用*机密客户端*，您**必须**在此时复制客户端密钥。离开此页面后，密钥将无法再次获得。如果您失去对客户端密钥的访问，您将需要轮换密钥。
:::
