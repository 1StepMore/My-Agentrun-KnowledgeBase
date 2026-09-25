---
title: Palantir 官方文档 · ontology-sdk · 创建一个新的 Developer Console 应用程序
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/create-a-new-osdk/
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

# 创建一个新的 Developer Console 应用程序

在此页面中，我们将逐步完成创建新 Developer Console 应用程序的以下过程：

* 向 SDK 应用程序添加 Object 类型、操作类型和其他 Ontology 资源。
* 添加用于访问平台 API 的操作和资源。
* 生成任意支持语言的包。
* 使用为您的特定应用程序 SDK 生成的自定义文档。

## 使用 Developer Console 创建应用程序

在您的 Foundry 实例中[导航至 Developer Console](/docs/foundry/ontology-sdk/navigation/)，然后选择 **+ New application**。

:::callout{theme="neutral"}
如果您没有看到 **+ New application** 按钮，您可能需要额外的权限。请参阅[权限文档](/docs/foundry/ontology-sdk/permissions/#user-permissions)了解更多详情。
:::

接下来，按照出现的创建向导中的步骤，并添加以下详细信息：

* 在 **Basic information** 页面，为您的应用程序添加一个图标；当用户看到同意屏幕时，该图标将用于识别应用程序。

![Ontology SDK 同意屏幕](../../foundry-docs/ontology-sdk/media/oauth-consent-screen-preview.png)

* 在 **Application type** 页面，选择 [**Client-facing application**](/docs/foundry/ontology-sdk/permissions/)。

![Ontology SDK 应用程序类型](../../foundry-docs/ontology-sdk/media/app-type-client-facing.png)

* 在 **Permissions** 页面的 **Authorization code grant** 部分，将重定向 URL 设置为 `http://localhost:8080/auth/callback`。

![在授权代码授予部分中正确输入重定向 URL](../../foundry-docs/ontology-sdk/media/oauth-redirect-url-config.png)

:::callout{theme="neutral"}
按照[配置 CORS](/docs/foundry/administration/configure-cors/)中的说明将 `http://localhost:8080` 添加到 Control Panel 的 CORS 策略中。
如果您没有权限配置 CORS 且您的 Foundry 管理员无法为您配置 CORS，请将重定向 URL 设置为 `https://localhost:8080/auth/callback`。
:::

### 资源

* 在 **Resources** 页面，选择 **Yes, generate an Ontology SDK**。

![选择您想要使用 Ontology SDK](../../foundry-docs/ontology-sdk/media/app-use-ontology-sdk-option.png)

* 选择一个要使用的 Ontology。然后，选择您希望 Ontology SDK 包包含的 Object 类型和操作类型。在此练习中，选择任何可用的 Object 类型。

![选择您想在 SDK 中使用的 Ontology 和特定的 Object 类型或操作类型](../../foundry-docs/ontology-sdk/media/app-ontology-resource-scopes.png)

:::callout{theme="neutral"}
您选择的数据实体控制应用程序的两个方面：

* **生成的类型：** 基于所选实体创建特定语言的绑定。此外，集成的 API 文档将根据您的选择生成。
* **应用程序词元：** 默认情况下，通过 OAuth 2.0 流程获得的词元范围限定为所选实体集合。更多详情请参阅[资源访问范围](/docs/foundry/ontology-sdk/permissions/#resource-access-scope)。
:::

* 如果您需要使用应用程序进行[平台 API 请求](/docs/foundry/api/general/overview/introduction/)，请务必通过 **Platform SDK** 选项卡添加适当的资源和操作。

![使用 Platform SDK 选项卡包含平台 SDK 资源](../../foundry-docs/ontology-sdk/media/scopes-platform-sdk-resources.png)

:::callout{theme="warning"}
**Client allowed operations** 表中授予的操作可能允许应用程序访问底层服务端点。
:::

* 审核并确认您输入的信息，然后选择 **Create application** 来创建应用程序。
* 最后，您必须选择 **Generate first version** 以获取所创建包的第一个版本。

![生成第一个 SDK](../../foundry-docs/ontology-sdk/media/sdk-generate-first.png)

## Ontology 特定文档

Developer Console 基于您选择的 Ontology 实体生成文档。此文档适用于 TypeScript、Python 和 cURL；您可以使用 Console 右上角的下拉菜单在不同语言之间切换。

![Developer Console 中 "Aircraft" Object 类型的 Ontology 特定文档。](../../foundry-docs/ontology-sdk/media/app-ontology-documentation.png)

在上述示例中，每个 Object 类型、操作类型和函数都有文档说明。文档包括如何返回特定属性或如何使用参数的代码示例；您可以直接将这些示例复制并粘贴到您的代码中。
