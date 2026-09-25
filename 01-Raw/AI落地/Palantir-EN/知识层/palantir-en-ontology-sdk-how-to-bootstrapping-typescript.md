---
title: Palantir 官方文档（英文原版）· Bootstrap a new OSDK TypeScript application
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/ontology-sdk/how-to-bootstrapping-typescript/
evidence: E1
lang: en
domain: AI落地
keywords:
- Palantir
- Foundry
- ontology-construction
- semantic-layer
state:
  phase: raw
  time_raw: '2026-09-23T06:47:11+08:00'
  time_draft: null
  time_wiki: null
related: null
compile: false
compile_note: 原文取证层：知识内容已由中文版汇编为 Draft（3 篇），本层用于引用英文原句，不重复编译
---

> 溯源：Palantir 官方英文原文（E1）。中文版为官方机翻（准确性未验证），本文件为**取证优先的原文**。抓取 2026-09-23T06:47:11+08:00。
> 原始地址：https://palantir.com/docs/foundry/ontology-sdk/how-to-bootstrapping-typescript/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-ontology-sdk-how-to-bootstrapping-typescript.md`

# Bootstrap a new OSDK TypeScript application

This page will walk you through the process of creating your frontend application on top of popular JavaScript frameworks using the `@osdk/create-app` CLI tool.

If you want to add OSDK support for an existing application, view our documentation on [adding an OSDK to an existing application](/docs/foundry/developer-console/how-to-add-to-existing-typescript/).

## 1: Prerequisites

### Create a Developer Console application

Follow the steps listed in the [create a new Developer Console application](/docs/foundry/developer-console/create-application/) page.

### Set up your token

Export your token in your local environment. Below is an example using a sample personal access token, but you can generate a longer-lived one in the Developer Console. This token should not be checked into source control because it is your personal access token.

```bash
export FOUNDRY_TOKEN=<YOUR-TOKEN-FROM-GETTING-STARTED-PAGE>
```

### Check Node version

The Typescript SDK requires Node 18 or higher to work. To check what version of Node you are using, enter the command below:

```bash
node --version
```

## 2. Quick start with `@osdk/create-app`

### Create your frontend application

Run the provided command and follow the interactive prompts to customize your project, including the project name and framework choice. You can find a version of this command with all parameters prefilled for your application on the **Getting started** page in the **API documentation** section of the Developer Console, or on the **Overview** page. Below is an example of this code, with placeholders inside the `< >` where your specific details will be filled:

```bash
npm create @osdk/app@latest -- \
    --application <RID OF YOUR DEVELOPER CONSOLE APPLICATION> \
    --foundryUrl <YOUR FOUNDRY URL> \
    --applicationUrl <SUBDOMAIN OF YOUR FOUNDRY URL USED FOR HOSTING> \
    --clientId <YOUR CLIENT ID> \
    --osdkPackage <YOUR PACKAGE NAME> \
    --osdkRegistryUrl <YOUR PACKAGE HOSTING URL> \
    --corsProxy false
```

:::callout{theme="warning"}
The `@osdk/create-app` CLI generates client code that matches the generator version of your application's OSDK package. New applications generate SDKs with the TypeScript OSDK v2 generator by default, which produces client code using `createClient` and `createPublicOauthClient`. If your application's SDK was generated with the legacy TypeScript OSDK 1.x generator, the generated `client.ts` will instead use the deprecated `FoundryClient` and `PublicClientAuth` imports. If this happens, review the [Troubleshooting](#troubleshooting) section below.
:::

### Develop your frontend application

Your project files have now been generated in a directory based on the project name you entered. A local development server can be started by running the commands below:

```bash
cd <project-directory>
npm install
npm run dev
```

#### Use OSDK React packages (optional)

If your application uses React, you can use the following libraries.

##### `@osdk/react`

Use [`@osdk/react`](/docs/foundry/ontology-sdk-react-applications/osdk-react/) for typed hooks, shared caching, actions, functions, and custom data-driven interfaces.

Install the latest version of `@osdk/react`:

```bash
npm install @osdk/react@latest
```

##### `@osdk/react-components`

Use [`@osdk/react-components`](/docs/foundry/ontology-sdk-react-applications/osdk-react-components/) for pre-built, Ontology-aware interface elements. This library builds on `@osdk/react`.

Install the latest version of `@osdk/react-components`:

```bash
npm install @osdk/react-components@latest
```

## Troubleshooting

### Generated code uses the legacy `FoundryClient` and `PublicClientAuth` imports

The `@osdk/create-app` CLI scaffolds client code that matches the generator version of your application's OSDK package. If the generated `client.ts` file contains imports similar to the following, your application's SDK was generated with the legacy TypeScript OSDK 1.x generator:

```typescript
import { FoundryClient, PublicClientAuth } from "@<application-name>/sdk";
```

TypeScript OSDK v2 replaces these imports with `createClient` from the `@osdk/client` package and `createPublicOauthClient` from the `@osdk/oauth` package. To generate modern client code, regenerate your SDK using the TypeScript OSDK v2 generator:

1. In the Developer Console, open the **SDK versions** tab of your application.
2. Generate a new version using the TypeScript OSDK v2 generator.
3. Re-run the `npm create @osdk/app@latest` command shown above, or update your SDK package dependency to the newly generated version.

For a full explanation of the differences between the two versions and how to update existing code, review the [TypeScript OSDK migration guide](/docs/foundry/ontology-sdk/typescript-osdk-migration/).
