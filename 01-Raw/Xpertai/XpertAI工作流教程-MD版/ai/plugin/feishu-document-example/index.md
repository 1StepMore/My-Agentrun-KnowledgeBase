---
title: 'Plugin Example: Lark Docs'
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
source_url: AI生成
source_type: article
source_platform: xpertai
author: XpertAI
fetch_date: '2026-05-08'
priority: 3
language: zh
notes: XpertAI官方文档
author_id: ''
publish_date: ''
---
# Plugin Example: Lark Docs

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugin Example: Lark Docs

This article demonstrates a complete plugin example, implemented based on the [Lark](https://www.feishu.cn/) platform.
The example covers plugin features, configuration, code structure, interface implementation, extension points, and more, helping you understand how to develop similar integration plugins on the **Xpert AI Platform**.

***

## Background

The Xpert AI plugin system allows developers to **extend platform functionality** via plugins. Using Lark Docs as an example, we aim to achieve the following scenarios:

* **System Integration**: Connect Lark app credentials such as AppID and AppSecret for authentication.
* **Document Loading**: Retrieve document content from Lark folders or document APIs.
* **Knowledge Management**: Convert documents into structured content usable by Xpert AI's knowledge base and agents.
* **Extension Strategies**: Implement extension points for integration, document sources, and document transformation via strategy interfaces.

The end result: Once users configure Lark integration info, Xpert AI can automatically read content from Lark Docs and include it in AI conversations and the knowledge base.

***

## 1. Clone the Plugin Template

We provide a **starter template** for plugin development to quickly build new plugins:

```sh theme={null}
git clone git@github.com:xpert-ai/xpert-plugins-starter.git lark
cd lark
```

Install dependencies:

```sh theme={null}
npm install
```

Use `nx` to create a new plugin library. Here, `packages/lark` is the plugin code directory, and `@xpert-ai/plugin-lark` is the npm package name:

```sh theme={null}
npx nx g @nx/js:lib packages/lark \
  --publishable \
  --importPath=@xpert-ai/plugin-lark \
  --bundler=tsc \
  --unitTestRunner=jest \
  --linter=eslint
```

Confirm plugin info:

```sh theme={null}
npx nx show project @xpert-ai/plugin-lark
```

> ✅ This generates a plugin named **`@xpert-ai/plugin-lark`** that will handle all Lark Docs integration features.

***

## 2. Plugin Entry Code

The plugin entry code mainly includes **meta info, config, and lifecycle functions (register/onStart/onStop)**.

```ts theme={null}
import { z } from 'zod';
import { type XpertPlugin } from '@xpert-ai/plugin-sdk';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { initI18n } from './lib/i18n.js';
import { LarkModule } from './lib/lark.module.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const ConfigSchema = z.object({});

const plugin: XpertPlugin<z.infer<typeof ConfigSchema>> = {
  meta: {
    name: '@xpert-ai/plugin-lark',
    version: '1.0.0',
    category: 'doc-source',
    displayName: 'Lark Plugin',
    description: 'Integrate Lark functionality',
    keywords: ['lark', 'feishu', 'document source'],
    author: 'Xpert AI team',
  },
  config: {
    schema: ConfigSchema,
  },
  register(ctx) {
    ctx.logger.log('register lark plugin');
    initI18n(join(__dirname, '../src'));
    return { module: LarkModule, global: true };
  },
  async onStart(ctx) {
    ctx.logger.log('lark plugin started');
  },
  async onStop(ctx) {
    ctx.logger.log('lark plugin stopped');
  },
};

export default plugin;
```

### Key Points

1. **meta**: Defines basic plugin info (name, version, category, keywords, etc.).
2. **config**: Describes the plugin config schema, allowing users to input config in the UI (reserved for future use).
3. **register**: Registers `LarkModule`, mounting the plugin to the NestJS module system.
4. **onStart/onStop**: Plugin lifecycle callbacks.

***

## 3. NestJS Module Structure

The plugin is essentially a [NestJS module](https://docs.nestjs.com/modules) (`LarkModule`), which registers various **strategy classes, controllers, or services**.

```ts theme={null}
import chalk from 'chalk';
import { XpertServerPlugin, IOnPluginBootstrap, IOnPluginDestroy } from '@xpert-ai/plugin-sdk';
import { LarkIntegrationStrategy } from './integration.strategy.js';
import { LarkController } from './lark.controller.js';
import { LarkSourceStrategy } from './source.strategy.js';
import { LarkDocTransformerStrategy } from './transformer.strategy.js';

@XpertServerPlugin({
  controllers: [LarkController],
  providers: [
    LarkIntegrationStrategy,
    LarkSourceStrategy,
    LarkDocTransformerStrategy
  ]
})
export class LarkModule implements IOnPluginBootstrap, IOnPluginDestroy {
  onPluginBootstrap(): void {
    console.log(chalk.green(`${LarkModule.name} is being bootstrapped...`));
  }
  onPluginDestroy(): void {
    console.log(chalk.green(`${LarkModule.name} is being destroyed...`));
  }
}
```

> ✅ The `Strategy` classes are extension points, for example:
>
> * `LarkIntegrationStrategy`: Handles integration with the Lark system.
> * `LarkSourceStrategy`: Defines how to load documents from Lark.
> * `LarkDocTransformerStrategy`: Defines how to transform documents into a format usable by the knowledge base.

***

## 4. API Interfaces

[Controllers](https://docs.nestjs.com/controllers) expose the plugin's REST APIs. For example, testing the Lark connection.

```ts theme={null}
@Post('test')
async connect(@Body() integration: IIntegration) {
  try {
    const botInfo = await this.integrationStrategy.validateConfig(integration.options)
    return integration
  } catch (err) {
    throw new ForbiddenException('Credentials failed')
  }
}
```

When calling the `/lark/test` endpoint (currently the default path for testing integration connectivity, will be unified later), the system validates the configuration (checks if AppID/AppSecret are valid).

***

## 5. Plugin Extension Points

### 5.1 System Integration Extension

[System integration strategy `LarkIntegrationStrategy`](./integration/) handles Lark app credential validation and bot info retrieval.

Key logic:

```ts theme={null}
async validateConfig(config: TLarkIntegrationConfig) {
  if (!config.appId || !config.appSecret) {
    throw new Error('App ID and Secret required')
  }
  const larkClient = new LarkClient({ options: config } as IIntegration)
  const botInfo = await larkClient.getBotInfo()
  if (!botInfo) throw new ForbiddenException('Bot permission denied')
  return botInfo
}
```

> ✅ Here, `LarkClient` wraps Lark OpenAPI requests.

***

### 5.2 Document Source Extension

[Document source strategy `LarkSourceStrategy`](./source/) defines how to fetch document lists from Lark.

* Config params: folder token, document type (docx/sheet/file, etc.).
* Loading logic: Calls `client.listDriveFiles(folderToken)`, returns `Document[]`.

***

### 5.3 Document Transformation Extension

[Document transformation strategy `LarkDocTransformerStrategy`](./transformer/) defines how to convert document content into knowledge base entries.

* Calls Lark API to get document body.
* Splits body into `Document` objects (for vectorization).
* Outputs in `IKnowledgeDocument` format.

***

### 5.4 Client Wrapper

All API requests are wrapped by `LarkClient`, which unifies `@larksuiteoapi/node-sdk` functionality and provides methods like:

* `getBotInfo()` Get bot info
* `listDriveFiles(folderToken)` List folder contents
* `getDocumentContent(docToken)` Get document body
* `getAllDocsInFolder(folderToken)` Recursively get all documents

This way, the **strategy layer only needs to call client methods** without worrying about API details.

***

## 6. Development Workflow Summary

1. **Prepare template**: Clone the plugin template and generate the project.
2. **Write entry code**: Define plugin meta, config, and lifecycle.
3. **Build module**: Register controllers and strategy classes in `LarkModule`.
4. **Implement strategies**:

   * Integration strategy: Handle AppID/Secret validation.
   * Source strategy: Fetch documents from Lark.
   * Transformation strategy: Convert documents to knowledge base content.
5. **Wrap client**: Manage Lark API calls in a unified way.
6. **Test API**: Use `/lark/test` to verify integration.

## 7. Build, Release, and npm Publish Workflow

After developing the `@xpert-ai/plugin-lark` plugin, you can use **Nx's build and release toolchain** to build and publish it to npm. The process includes:

### 7.1 Build the Plugin

Run the build command:

```bash theme={null}
npx nx build @xpert-ai/plugin-lark
```

* This uses Nx's builder (TypeScript compiler `tsc` by default) to compile source code to JavaScript.
* Build output goes to:

  ```
  packages/lark/dist
  ```
* The output directory contains the publishable artifacts (`index.js`, type declarations `.d.ts`, etc.).

### 7.2 Version Management

To ensure proper npm package iteration, maintain the plugin version number.
It's recommended to use Nx's **release workflow** for automatic version management:

#### Auto bump version

```bash theme={null}
npx nx release patch @xpert-ai/plugin-lark
```

* `patch`: Patch version (e.g. 1.0.0 → 1.0.1)
* `minor`: Minor version (e.g. 1.0.0 → 1.1.0)
* `major`: Major version (e.g. 1.0.0 → 2.0.0)

This command will automatically:

1. Update the `version` in `package.json`.
2. Update `CHANGELOG.md`.
3. Generate the corresponding Git tag.

> If not using `nx release`, you can manually edit the `version` field in `package.json`.

### 7.3 Publish to npm

After building and bumping the version, run the publish command:

```bash theme={null}
npx nx run @xpert-ai/plugin-lark:nx-release-publish --access public --otp=<one-time-password-if-needed>
```

* `--access public`
  Specifies the package as public (suitable for packages under the `@xpert-ai` npm scope).
* `--otp=<code>`
  If your npm account has **2FA enabled**, enter a one-time password (OTP).

> ⚠️ Before publishing, make sure the following fields in `package.json` are correct:
>
> * **`main`**: Points to the build output entry, e.g. `"dist/index.js"`
> * **`types`**: Points to type declarations, e.g. `"dist/index.d.ts"`
> * **`files`**: Only includes files to be published (e.g. `"dist/**/*"`)
> * **`publishConfig`**: Can define default publish access (e.g. `"access": "public"`)

### 7.4 Final Workflow Example

Summing up, the full workflow to publish `@xpert-ai/plugin-lark` is:

```bash theme={null}
# 1. Build the plugin
npx nx build @xpert-ai/plugin-lark

# 2. Auto bump version (patch)
npx nx release patch @xpert-ai/plugin-lark

# 3. Publish to npm
npx nx run @xpert-ai/plugin-lark:nx-release-publish --access public --otp=<one-time-password-if-needed>
```

Once successful, you'll see the latest `@xpert-ai/plugin-lark` version on npm. 🎉

***

## 8. Final Usage

After plugin development, you can use it in the Xpert AI platform to:

* Configure Lark AppID/AppSecret
* Select document folders and types
* Automatically load Lark Docs content
* Convert documents into knowledge base entries, supporting AI conversations and agent analysis


## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

## 关联问题

- 这个概念和其他知识有什么联系？
- 这个观点和我的已有认知是否冲突？

---

## 抓取备注

- 抓取时间：2026-05-08
- 抓取工具：手动导入
- 质量评分：
