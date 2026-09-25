---
title: Palantir 官方文档 · ontology-sdk · 使用服务用户启动新的 Ontology SDK TypeScript 应用程序
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-server-side-typescript/
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

# 使用服务用户启动新的 Ontology SDK TypeScript 应用程序

如[权限类型](/docs/foundry/ontology-sdk/permissions/#permission-types)部分所述，Ontology SDK 可以被用于在基于服务用户权限而非最终用户权限的基础上查询数据。以下演练展示了如何使用[Next.js© ↗](https://nextjs.org/)（外部链接）通过 Ontology SDK 和服务用户获取数据。

:::callout{theme="neutral"}
在开发使用机密客户端的服务或应用程序时，将会在您的 Developer Console 应用程序中创建一个服务用户。如果您计划使用属于与默认组织不同的组织的 Ontology 创建应用程序，您必须完成[共享和启用应用程序](/docs/foundry/ontology-sdk/how-to-create-backend-service-app-different-org/)的步骤。
:::

## 1. 使用 Developer Console 创建 Ontology SDK 包

在您的 Foundry 实例中[导航到 Developer Console](/docs/foundry/ontology-sdk/navigation/)，然后选择 **+ 新应用程序**。

:::callout{theme="neutral"}
如果未出现 **+ 新应用程序** 按钮，则您可能没有正确的权限。查看[权限文档](/docs/foundry/ontology-sdk/permissions/#user-permissions)以获取更多信息。
:::

按照创建向导中的步骤操作，并添加以下详细信息：

* 在 **应用程序类型** 页面上，选择 [**后端服务**](/docs/foundry/ontology-sdk/permissions/)。

![选择使用后端服务应用程序类型](../../foundry-docs/ontology-sdk/media/app-type-backend-service.png)

* 在 **权限** 页面上，选择 [**应用程序的权限**](/docs/foundry/ontology-sdk/permissions/)。

![后端服务器权限](../../foundry-docs/ontology-sdk/media/oauth-service-user-permissions.png)

Developer Console 将根据应用程序名称为此应用程序创建一个服务用户。在上述示例中，生成的服务用户名称为 **Ontology SDK application using service user**。除了任何操作类型的[提交标准](/docs/foundry/action-types/submission-criteria/)外，您必须授予此服务用户读取您将在下一步骤中选择的[对象类型的数据](/docs/foundry/object-permissioning/overview/)所需的权限。

* 在 **Ontology 和资源范围** 页面上，选择 **是，生成一个 Ontology SDK**。

![选择您想使用 Ontology SDK](../../foundry-docs/ontology-sdk/media/app-use-ontology-sdk-option.png)

* 选择要使用的 Ontology。然后，选择您希望 Ontology SDK 包包含的对象类型和操作类型。对于本次练习，选择任何可用的对象类型。

![选择您想在 SDK 中使用的 ontology 和特定对象类型或操作类型](../../foundry-docs/ontology-sdk/media/app-ontology-resource-scopes.png)

检查并确认您输入的信息，然后选择 **创建应用程序** 以查看新应用程序的客户端密钥。复制并安全地存储该密钥，因为这是唯一可见的时间。

![复制弹出窗口中出现的服务器端客户端密钥并安全存储。](../../foundry-docs/ontology-sdk/media/oauth-client-secret-dialog.png)

:::callout{theme="neutral"}
如果您丢失了客户端密钥，您可以在 **权限和 OAuth** 页面上进行旋转并获得新密钥。请记住，这将破坏使用该服务用户和密钥的现有应用程序。
:::

最后，选择 **生成第一个版本** 以使用您新创建的 Ontology SDK。

![生成第一个 SDK](../../foundry-docs/ontology-sdk/media/sdk-generate-first.png)

## 2. 安装生成的 SDK 包

一旦 Ontology SDK 的生成完成，您将看到一组安装步骤以指导您在代码项目中安装生成的 SDK。

## 3. 在您的代码项目中使用 Ontology SDK

在本次演练中，我们使用 [Next.js© ↗](https://nextjs.org)。Next.js 支持在服务器端渲染代码，这对于我们的服务用户示例是必需的。要启动一个新的 Next.js 项目，请遵循 [Next.js© 文档 ↗](https://nextjs.org/docs/getting-started/installation)。

### 客户端和 OAuth 创建

服务用户身份验证是通过机密 OAuth 客户端完成的，该客户端允许您使用客户端密钥访问 Ontology，而无需用户身份验证。

创建一个名为 `client.ts` 的文件并输入以下代码：

```typescript
import { createConfidentialOauthClient } from "@osdk/oauth";
import { createClient } from "@osdk/client";

// 创建一个机密的OAuth客户端
export const auth = createConfidentialOauthClient(
    process.env.CLIENT_ID!, // 从环境变量中获取客户端ID
    process.env.CLIENT_SECRET!, // 从环境变量中获取客户端密钥
    process.env.STACK_URL!, // 从环境变量中获取栈的URL
);

// 创建一个客户端实例
export const client = createClient(
    process.env.STACK_URL!, // 从环境变量中获取栈的URL
    <ONTOLOGY-RID>, // 这里需要提供一个本体资源标识符（RID）
    auth // 使用上面创建的OAuth认证客户端
)
```

创建一个`.env`文件，并使用相同的变量。**不要将此文件提交到代码仓库中**。

```bash
CLIENT_ID=<YOUR CLIENT ID> # 替换为您的客户端 ID
CLIENT_SECRET=<YOUR CLIENT SECRET> # 替换为您的客户端密钥
STACK_URL=<YOUR ONTOLOGY SERVER DOMAIN NAME> # 替换为您的本体服务器域名，例如，https://myfoundrystack.com
```

### 访问Ontology

以下代码使用了名为`@serverside-osdk-example/sdk`的包中的`Country` Object类型。请将示例包名和Object类型替换为您创建的包和选择的Object类型。最后，将`{country.countryName}`替换为您的Object类型中的一个属性。

将`page.tsx`中的代码替换为以下代码：

```typescript
import { Country } from "@serverside-osdk-example/sdk";
import { client, auth } from "./client";
import { Osdk } from "@osdk/client";

// 定义一个异步函数，用于获取国家列表
async function getCountries(): Promise<Osdk.Instance<Country>[]> {
    // 处理身份验证
    await auth.signIn();
    // 需要为服务用户提供对本体的读取权限
    try {
        const resp = await client(Country).fetchPage(); // 调用客户端获取国家数据
        return resp.data; // 返回数据
    } catch (err) {
        console.log(err); // 如果发生错误，打印错误信息
    }
    console.log("No countries found"); // 如果没有找到国家，打印信息
    return [];
};

// 默认导出异步函数Home
export default async function Home() {
  const countries: Osdk.Instance<Country>[]  = await getCountries(); // 获取国家列表
  return (
    <main>
        <div>
          {countries.map((country: Osdk.Instance<Country>) => (
            <span key={country.$primaryKey}>{country.countryName}</span> // 显示每个国家的名称
            )
          )}
        </div>
    </main>
  )
}
```

要运行您的设置演示，首先运行开发服务器：

```bash
npm run dev
# 运行开发环境服务器
```

然后，使用浏览器访问 [http://localhost:3000 ↗](http://localhost:3000) 查看结果。
