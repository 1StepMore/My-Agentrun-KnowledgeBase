---
title: Palantir 官方文档 · ontology-sdk · 在 Foundry 上部署一个 Ontology SDK 应用
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/deploy-osdk-application-on-foundry/
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

# 在 Foundry 上部署一个 Ontology SDK 应用

在 Developer Console 中的网页托管功能为使用 Ontology SDK 构建前端应用的开发人员提供了一个在 Foundry 上托管这些应用的选项，从而无需额外的托管基础设施。

:::callout{theme="warning"}
网页托管功能仅支持托管静态资产，并不支持运行服务器（类似于 GitHub Pages）。
:::

每个托管的网站都可以作为您的 Foundry 注册域的一个子域使用。这意味着在下面的设置过程中，您将为您的应用选择一个子域，它将从 `<YOUR-APPLICATION-SUBDOMAIN>.[YOUR-STACK-NAME].palantirfoundry.com` 提供服务。

:::callout{theme="warning"}
如果您的 Foundry 堆栈不是从以 `.palantirfoundry.com` 结尾的域提供服务，请联系 Palantir 客服支持以帮助设置网页托管，因为这需要额外的协调。
:::

## 准备您的应用

以下部分描述了在 Foundry 上托管您的 Developer Console 应用所需的步骤。

### 单页应用（SPA）渲染

如果您没有在应用中包含一个[自定义404页面](#custom-404-page)，Foundry 将假定这是一个[单页应用 ↗](https://en.wikipedia.org/wiki/Single-page_application)，并将任何请求路由到该子域下的路径至 `index.html`。

### 更新重定向 URL

作为身份验证流程的一部分，您需要在代码中更新重定向 URL `<YOUR-APPLICATION-SUBDOMAIN>.[YOUR-STACK-NAME].palantirfoundry.com/auth/callback`。
您还必须将相同的重定向 URL 添加到 Developer Console 中的应用中。查看[创建一个新的 OSDK](/docs/foundry/ontology-sdk/create-a-new-osdk/)以获取更多信息。

### 准备资产

压缩包含您网站文件生产搭建的目录内容。**不要**包含目录本身。对于常见的 Web 框架，该目录通常为 `dist/`。

如果您在压缩文件中包含任何目录，这些目录将包含在您网站的路径中。

## 设置域

在 Developer Console 的应用中，从左侧菜单中选择 **网站托管**。

1. 选择应用的子域；这可以是应用名称或您选择的其他名称。然后，选择 **请求应用域**。在下面的例子中，我们选择 `my-first-hosted-app.example.palantirfoundry.com`：

   ![Domain request dialog in web hosting.](../../foundry-docs/ontology-sdk/media/web-hosting-domain-request.png)

2. 请求您注册中的信息安全官员批准，或者如果您有必要的权限，可以选择 **查看请求** 自行批准。注册管理员可以在控制面板中管理注册权限。

   ![Domain pending approval status.](../../foundry-docs/ontology-sdk/media/web-hosting-domain-pending.png)

3. 请求批准后，刷新页面。此时，**域已准备好** 应该出现，指示域已准备好使用。这可能需要几分钟完成。

   ![Domain ready status in web hosting.](../../foundry-docs/ontology-sdk/media/web-hosting-domain-ready.png)

## 上传您的资产并部署

作为开发人员，您可以选择使用 Developer Console 网站托管用户界面手动上传资产，或者使用 `@osdk/cli` 命令行工具。

* 要了解如何使用 Developer Console 用户界面上传，请遵循[下面](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/#upload-assets-using-the-developer-console)的指南。
* 要了解如何使用命令行界面上传资产，请遵循平台中的**部署应用**指南，如下面的屏幕截图所示。您可以在[公共 npm 仓库 ↗](https://www.npmjs.com/package/@osdk/cli)中找到有关 `@osdk/cli` 命令行工具的更多详细信息。

![使用 cli 部署](../../foundry-docs/ontology-sdk/media/deploy-cli-guide.png)

### 使用 Developer Console 上传资产

在以下步骤中，我们将上传之前创建的[压缩资产](/docs/foundry/ontology-sdk/deploy-osdk-application-on-foundry/#prepare-the-asset)到 Foundry。

1. 在页面的 **资产** 部分选择 **上传新资产**。

2. 在此处拖放您的 zip 存档文件，或从您的计算机中选择并选择 **上传**。

   ![Upload asset to web hosting.](../../foundry-docs/ontology-sdk/media/web-hosting-asset-upload.png)

3. 上传完成后，使用 **预览** 在部署到生产环境之前预览您的网站，或使用 **...** 选项 **部署到生产环境**，如下所示。

   ![Preview asset version.](../../foundry-docs/ontology-sdk/media/web-hosting-asset-preview.png)

   一旦选择 **部署到生产环境**，该版本将为所有用户提供服务。我们建议首先 **预览网站**。

4. 现在，选择 **查看网站** 访问已部署的网站。

   ![View deployed site.](../../foundry-docs/ontology-sdk/media/web-hosting-deployed-site.png)

## 授予网站访问权限

由 Foundry 托管的网站仅对拥有 Foundry 登录凭证的用户可用。默认情况下，任何可以访问您 Developer Console 应用的用户也可以访问已部署的网站，但这可能仅包括您和您的开发团队。
要使您的网站对其他 Foundry 用户可访问，请导航到左侧的 **共享 & 词元** 菜单。在页面的 **共享托管网站** 部分下添加用户的名字，如下所示。

![与用户共享应用。](../../foundry-docs/ontology-sdk/media/web-hosting-share.png)

## 高级配置

您可以在 **网站托管** 页面的 **高级** 选项卡中找到其他配置选项。

### 内容安全策略

默认情况下，您的应用将以受限的[内容安全策略 (CSP) ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)提供服务，仅允许从您的子域加载资源。如果需要，您可以为应用中的特定交互配置额外的 CSP 规则，它们将与默认策略合并。然而，请注意，进行这些更改可能会增加您的应用对跨站脚本 (XSS) 和数据注入攻击的漏洞。

在 **内容安全策略** 部分中，如下图所示，您可以控制应用的 CSP。更新 CSP 在检索其他地方托管的图像或内容以及调用外部服务时至关重要。

![编辑内容安全策略。](../../foundry-docs/ontology-sdk/media/web-hosting-csp-config.png)

请参阅 [Mozilla 的文档 ↗](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) 以获取语法帮助。这些字段没有验证。

## 路由匹配规则

Foundry 支持在具有和不具有扩展名和结尾斜杠的路由上提供 HTML 页面。

给定以下网站文件设计：

```markdown
├── file.html        # 一个单独的HTML文件
├── folder           # 一个包含index.html的目录
│   └── index.html   # 目录下的HTML文件
├── both.html        # 另一个单独的HTML文件
└── both             # 另一个目录，包含与目录同名的index.html
    └── index.html   # 目录下的HTML文件
```

Foundry在以下路径上提供这些HTML页面：

| 路径               | 文件               |
| ------------------ | ------------------ |
| /file              | /file.html         |
| /file/             | /file.html         |
| /file.html         | /file.html         |
| /folder            | /folder/index.html |
| /folder/           | /folder/index.html |
| /folder/index.html | /folder/index.html |
| /both              | /both.html         |
| /both.html         | /both.html         |
| /both/             | /both/index.html   |
| /both/index.html   | /both/index.html   |

Foundry不会重定向到首选路径格式，例如强制添加尾部斜杠或从路径中删除扩展名。

## 自定义404页面

您可以在网站根目录添加一个`404.html`页面，以在路径不匹配时作为自定义错误页面。这将禁用默认行为，即在路径不匹配时提供根`index.html`页面，如[单页面应用程序（SPA）渲染](#single-page-application-spa-rendering)中所述。
