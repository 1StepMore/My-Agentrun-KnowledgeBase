---
title: Palantir 官方文档 · platform-security-third-party · 为 Foundry 编写 OAuth2 客户端
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-third-party/writing-oauth2-clients/
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

# 为 Foundry 编写 OAuth2 客户端

本文件面向希望编写 OAuth2 客户端以连接到 Foundry 的 Foundry 用户或管理员。此页面提供了 [OAuth 2.0 授权框架 ↗](https://www.rfc-editor.org/rfc/rfc6749) 的描述以及 Foundry OAuth2 实现的详细信息。此外，[Foundry 第三方应用程序和 API 协议](/docs/foundry/platform-security-third-party/3pa-api-guidance/) 管理在 Foundry 平台上使用第三方应用程序的规则，第三方应用程序的创建者和管理员应予以理解。

## OAuth2 概述

OAuth2 授权框架使第三方应用程序能够获得对服务的受控访问。OAuth2 通过提供一层机制，使客户端（如第三方应用程序）能够通过使用专门发行的访问词元和刷新词元请求访问，而不是用户的凭据或静态持有者词元，从而改进了传统的客户端-服务器授权模型。OAuth2 通过使用授权授予来管理此访问，授权授予是获取访问词元的方法。

## 支持 OAuth2 集成

以下部分描述了如何在第三方应用程序中支持 OAuth2。在整个文档中，**客户端**指代第三方应用程序，**授权服务器**指代 Foundry 的授权服务器，**用户**指代第三方应用程序的终端用户。

要在 Foundry 中使用 OAuth2，您必须按照[注册第三方应用程序](/docs/foundry/platform-security-third-party/register-3pa/)的说明注册您的应用程序，并在接下来的子部分中选择一种授权选项。

### 授权码授权

授权码授权允许客户端代表现有的 Foundry 用户执行操作。应用程序必须请求他们需要访问的 Foundry 权限集，然后 Foundry 用户必须明确授予客户端对其账户上那些权限的访问。Foundry 允许将客户端限制在用户可以访问的资源的有限集，或所有资源。

授权码授权的工作流程如下：

1. 客户端创建一个 `code_verifier` 和 `code_challenge`。对于可以安全存储客户端机密的*私密客户端↗*（如基于服务器的应用程序），这是**推荐的**但不是必需的。对于无法安全存储客户端机密的[*公共客户端*↗](https://tools.ietf.org/html/rfc6749#section-2.1)（如本机应用程序），这是**必需的**。
   * `code_verifier` 是一个加密随机字符串，包含 A-Z、a-z、0-9、`-`（连字符）、`.`（句号）、`_`（下划线）和 `~`（波浪号），长度为 43 到 128 个字符。
   * `code_challenge` 是通过对 `code_verifier` 执行 SHA256 然后转换为无填充的 Base64-URL 编码值派生得到的。
2. 客户端应用程序应打开浏览器并将用户发送到[授权端点](#authorization-endpoint)URL，并将以下参数作为查询参数添加：
   * `response_type`：应设置为 `code`。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `redirect_uri`：告知授权服务器在用户批准请求后将用户重定向到哪里。如果未指定，它将默认为 Foundry 中第三方应用程序设置中的第一个重定向 URI 值。
   * `scope`：定义请求的权限。在[API 文档](/docs/foundry/api/general/overview/introduction/)中为公共 API 提供的作用域。添加 `offline_access` 作用域以获取刷新词元。如果需要多个作用域，请使用空格作为分隔符连接这些作用域。
   * `state`：应用程序生成的随机字符串，将按原样返回给应用程序。应用程序应检查返回的值是否与原始字符串匹配，以防止 CSRF 攻击。
   * `code_challenge`：如果客户端创建了 `code_challenge`，则应填充此参数。授权服务器将内部将 `code_challenge` 参数与其生成的授权码关联。
   * `code_challenge_method`：应设置为 `S256`。
3. 当用户访问 URL 时，授权服务器会向用户显示类似于以下的提示，然后用户可以选择批准应用程序的请求。

![授权请求](../../foundry-docs/platform-security-third-party/media/3PA-user-connection-dialog.png)

4. 如果请求成功，授权服务器随后将用户重定向到指定的重定向 URI，并将以下参数作为查询参数添加：
   * `code`：这是授权服务器生成的授权码。
   * `state`：这是客户端在授权请求中传递的相同参数。客户端应检查其是否与请求中发送的原始 `state` 参数匹配。
5. 客户端随后应通过调用[词元端点](#token-endpoint)来交换授权码以获取访问词元。以下参数应使用 `application/x-www-form-urlencoded` 格式发送在请求正文中：
   * `grant_type`：应设置为 `authorization_code`。
   * `code`：从授权服务器接收到的代码。
   * `redirect_uri`：用户代理将重定向到的绝对 URI。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `code_verifier`：如果客户端生成了 `code_verifier`，则应在此请求中发送它。授权服务器将验证 `code_verifier` 是否匹配在先前请求中发送的 `code_challenge`。
6. 授权服务器随后会响应一个访问词元，客户端可以使用此词元访问请求的资源，如 REST API。响应包含以下参数：
   * `access_token`：客户端可以用来访问请求资源的词元。
   * `token_type`：发行的词元类型。
   * `expires_in`：访问词元的生命周期（以秒为单位）。
   * `refresh_token`：仅在请求的作用域包含 `offline_access` 时返回。如果客户端希望在用户不在场时刷新访问词元以授权请求，应使用此词元。有关更多信息，请参见[刷新访问词元](#refreshing-an-access-token)。

### 客户端凭证授权

客户端凭证授权专为非交互式服务用户样式的工作流程设计，其中客户端执行的操作不与正常的 Foundry 用户关联。客户端不代表正常的 Foundry 用户操作。

![客户端凭证授权](../../foundry-docs/platform-security-third-party/media/3PA-client-credentials-grant.png)

相反，此授权类型会自动创建一个与客户端关联的 Foundry 服务用户，然后可以为其授予访问 Foundry 资源的权限。通过此授权获得的词元可以用于代表创建的服务用户访问资源。服务用户账户的用户名与应用程序的客户端 ID 相同。

:::callout{theme="neutral"}
默认情况下，服务账户无权访问任何资源。Foundry 管理员必须为服务用户账户指派所需的角色和权限，以便客户端在 Foundry 中执行操作。
:::

客户端凭证授权的工作流程如下：

1. 客户端调用[词元端点](#token-endpoint)。以下参数应使用 `application/x-www-form-urlencoded` 格式发送在请求正文中：
   * `grant_type`：应设置为 `client_credentials`。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `client_secret`：应设置为在 Foundry 中注册第三方应用程序时生成的客户端机密。
2. 授权服务器随后返回以下信息：
   * `access_token`：客户端可以用来访问请求资源的词元。
   * `token_type`：发行的词元类型。
   * `expires_in`：访问词元的生命周期（以秒为单位）。
3. 客户端随后可以使用访问词元访问请求的资源。

### 刷新访问词元

访问词元在一段时间后会过期，需要重新获取。任何在用户不在场时需要访问 Foundry API 的客户端都需要刷新词元。

这可以通过以下步骤完成：

1. 客户端应遵循[授权码授权](#authorization-code-grant)中概述的步骤，并将 `offline_access` 作为请求的 `scope` 参数的一部分进行指定。
2. 客户端应保存[授权码授权](#authorization-code-grant)最终步骤中返回的 `refresh_token`。
3. 如果访问词元过期，客户端随后可以通过调用[词元端点](#token-endpoint)端点并使用以下参数刷新词元：
   * `grant_type`：应设置为 `refresh_token`。
   * `refresh_token`：之前为给定用户获取的刷新词元。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `client_secret`：应设置为在 Foundry 中注册第三方应用程序时生成的客户端机密。
4. 授权服务器随后会响应以下信息：
   * `access_token` 客户端可以用来访问请求资源的词元。
   * `token_type`：发行的词元类型。
   * `expires_in`：访问词元的生命周期（以秒为单位）。
   * `refresh_token`：可以用来刷新访问词元的刷新词元。请注意，Foundry 每次使用先前发行的刷新词元时都会旋转刷新词元。请确保您保存了 `access_token` 和 `refresh_token`。

#### 刷新词元轮换

刷新词元可用于获取新的访问词元。Foundry 通过在每次使用先前发行的刷新词元时旋转刷新词元来降低与刷新词元相关的风险。
重用检测保护机制确保如果刷新词元在首次使用后一分钟内被重用，则由此授权授予创建的所有访问词元将失效，并且需要新的授权流程。
允许的一分钟重用间隔是为了应对可能的瞬态错误，如网络故障。此外，超过30天未使用的刷新词元会自动失效。这些安全措施通过确保没有长期存在的刷新词元来降低潜在被攻击的词元的风险。

## OAuth2 API 参考

以下端点可用于获取 OAuth2 词元。

### 授权端点

`GET /multipass/api/oauth2/authorize`

授权端点，供客户端用于获取授权码。

#### 查询参数

| 参数名称              | 类型     | 描述 |
|----------------------|--------|-----|
| response\_type        | 字符串  | 必须设置为 `code`。 |
| client\_id            | 字符串  | 客户端的唯一标识符。 |
| redirect\_uri         | 字符串  | 用户代理将重定向到的绝对 URI。必须与在控制面板中指定的重定向 URI 之一匹配。您可以通过导航到[管理应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)屏幕再次访问此 URI。 |
| scope                | 字符串  | 要请求的权限范围。在[API 文档](/docs/foundry/api/general/overview/introduction/)中为公共 API 提供的作用域，应作为空格分隔的字符串列出。 |
| state                | 字符串 (非必填) | 传递给服务器的任意字符串，将按原样返回给客户端。这有助于防止跨站点请求伪造。 |
| code\_challenge       | 字符串 (非必填) | 由客户端生成的代码挑战；与[带有代码交换证明密钥的授权码授权 (PKCE)](#authorization-code-grant)一起使用 |
| code\_challenge\_method| 字符串 (非必填) | 如果使用 `code_challenge`，则应设置为 `S256`。 |

#### 重定向查询参数

如果请求成功，用户的浏览器会重定向到第三方应用程序设置中指定的重定向 URI 或请求中传递的重定向 URI。重定向请求 URI 中将存在以下查询参数：

| 参数名称 | 类型                 | 描述 |
|--------|--------------------|------|
| code   | 字符串             | 生成的授权码。此代码将在 10 分钟后失效。 |
| state  | 字符串 (非必填)    | 如果 `state` 参数存在于授权请求中，则此处将包含该确切值。 |

### 词元端点

`POST /multipass/api/oauth2/token`

词元端点由客户端用于通过提供其授权授予或刷新词元来获取访问词元。

#### 头参数

| 参数名称       | 描述 |
|---------------|-----|
| Content-Type  | 必须是 `application/x-www-form-urlencoded`。 |

#### 请求正文参数

| 参数名称        | 类型   | 描述 |
|----------------|------|-----|
| grant\_type     | 字符串 | 值必须是 `authorization_code`、`refresh_token` 或 `client_credentials` |
| code           | 字符串 (非必填) | 从授权端点接收到的授权码。如果授权类型是 `authorization_code`，这是必需的 |
| refresh\_token  | 字符串 (非必填) | 当 `grant_type` 是 `refresh_token` 时，这是必需的。值应为在最初的请求中获取授权码时获得的 `refresh_token`。 |
| redirect\_uri   | 字符串 (非必填/必填) | 用户代理将重定向到的绝对 URI。如果在授权请求中指定了重定向 URI，这是**必需的**。 |
| scope          | 字符串 (非必填) | 要请求的权限范围。在[API 文档](/docs/foundry/api/general/overview/introduction/)中为公共 API 提供的作用域，应作为空格分隔的字符串列出。 |
| client\_id      | 字符串            | 客户端的唯一标识符。 |
| client\_secret  | 字符串 (非必填) | 在应用程序注册期间发行的应用程序客户端机密。当 `grant_type` 是 `client_credentials` 时，这是必需的。 |
| code\_verifier  | 字符串 (非必填) | 应用程序在授权请求之前生成的用于 PKCE 请求的代码验证器。 |

#### 响应正文

响应 JSON 具有以下字段。

| 字段名称        | 类型     | 描述 |
|---------------|--------|-----|
| access\_token  | 字符串  | 用于访问资源的凭据。 |
| token\_type    | 字符串  | 发行的词元类型。 |
| expires\_in    | 字符串  | 访问词元的生命周期（以秒为单位）。 |
| refresh\_token | 字符串 (非必填) | 用于获取新访问词元的凭据。Foundry 每次调用 `refresh_token` 授权时都会旋转 `refresh_token`。请确保您保存了 `access_token` 和 `refresh_token`。 |

### 端点出错

#### 出错响应正文

如果请求失败，只有在访问请求被拒绝的情况下，用户的浏览器才会被重定向。在所有其他情况下，将返回包含以下字段的 HTML 出错页面。

| 字段名称             | 类型     | 描述                                    |
|-------------------|--------|----------------------------------------|
| error             | 字符串  | 如下节中定义的出错代码。                |
| error\_description | 字符串  | 出错的人类可读描述                      |

#### 出错代码

| 出错代码值                | 描述                                                    |
|--------------------------|---------------------------------------------------------|
| `invalid_request`        | 请求无效。                                              |
| `unauthorized_client`    | 客户端无权请求授权码。                                  |
| `access_denied`          | 服务器拒绝了请求。                                      |
| `unsupported_response_type` | 提供的响应类型不受支持。                              |
| `invalid_scope`          | 请求的范围无效、未知或格式错误。                        |
| `server_error`           | 发生意外的服务器出错。                                  |
