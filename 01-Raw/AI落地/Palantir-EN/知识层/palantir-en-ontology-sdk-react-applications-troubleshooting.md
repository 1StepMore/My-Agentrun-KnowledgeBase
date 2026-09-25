---
title: Palantir 官方文档（英文原版）· Troubleshooting
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/ontology-sdk-react-applications/troubleshooting/
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
> 原始地址：https://palantir.com/docs/foundry/ontology-sdk-react-applications/troubleshooting/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-ontology-sdk-react-applications-troubleshooting.md`

# Troubleshooting

This page contains tips for troubleshooting errors that you may encounter while developing your OSDK React application. If you have other issues or are unable to resolve your issue with this guide, [report an issue](/docs/foundry/getting-help/issues/#report-an-issue) to Palantir Support.

## Workspace errors

If working from within the Palantir platform, you will be using a VS Code workspace running on Palantir's Code Workspaces infrastructure. Further troubleshooting information can be found in the following documentation:

* [VS Code workspace troubleshooting](/docs/foundry/vs-code/troubleshooting/)
* [Code Workspaces troubleshooting](/docs/foundry/code-workspaces/troubleshooting/)

## npm troubleshooting steps

If you are having issues running your npm commands, try the following troubleshooting steps:

* Delete the lock file (`package-lock.json`) and the dependency folder (`node_modules/`), then re-run the failing command.
* Pause and resume the workspace.

### `NPM MODULE_NOT_FOUND` error: Adding new dependencies

Code Repositories requires your dependencies to be explicitly declared.

By default, we add the following npm repositories:

* Common OSDK dependencies: `foundry-sdk-asset-bundle`, `osdk-templates-bundle`
* [npmjs.com ↗](https://www.npmjs.com/) mirror: `external-npm-npmjs`
* Your OSDK:  `SDK Artifacts Repository - <rid>`

![The "Libraries" setting page in Code Repositories.](/docs/resources/foundry/ontology-sdk-react-applications/code-repositories-libraries-page.png)

The `npm install <package>` command may fail if you try to add a package that is not present in any of the backing repositories. For example, if the package you try to install is private, you must ensure it is present as a repository Artifact. Review our [Artifacts documentation](/docs/foundry/code-repositories/artifact-repositories-overview/) for more information.

Example error:

![A "Module not found" npm error.](/docs/resources/foundry/ontology-sdk-react-applications/npm-module-not-found-error.png)

:::callout{theme="neutral"}
The error `code E401 Incorrect or missing password` will be emitted by npm when **npmjs.com** is unreachable from within a VS Code workspace.
:::
