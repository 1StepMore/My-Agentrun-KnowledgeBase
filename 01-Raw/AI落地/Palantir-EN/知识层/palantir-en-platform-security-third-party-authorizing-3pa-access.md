---
title: Palantir 官方文档（英文原版）· Authorizing third-party application access
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/platform-security-third-party/authorizing-3pa-access/
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
> 原始地址：https://palantir.com/docs/foundry/platform-security-third-party/authorizing-3pa-access/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-authorizing-3pa-access.md`

# Authorizing third-party application access

## Authorizing third-party applications

Once a third-party application has been [registered](/docs/foundry/platform-security-third-party/register-3pa/) and [enabled](/docs/foundry/platform-security-third-party/enabling-3pa-access/) in the Foundry platform, the process for authorizing the third-party application to Foundry is simple.

:::callout{theme="neutral"}
If the desired third-party application has not been registered and enabled in the Foundry platform, register and enable it before proceeding with the authorization process or contact your Palantir representative to request registration and/or enablement.
:::

In this example, a simple test application demonstrates the workflow for authorizing a registered and enabled third-party application for Foundry access. Third-party applications may offer some kind of **Connect** option, as seen below.

![Example third-party application](/docs/resources/foundry/platform-security-third-party/3PA-user-example-test-app.png)

Attempting to connect or authorize a third-party application that has been registered and enabled will direct you to Foundry and open a confirmation screen, as seen below, in which you can choose to **Allow** or **Don’t allow** access. On this confirmation screen, Foundry will display the set of operations for which the third-party application is requesting permissions; this set of operations is determined by the author of the third-party application connector.

![Example third-party application: Connection dialog](/docs/resources/foundry/platform-security-third-party/3PA-user-connection-dialog.png)

After allowing access, you should be redirected back to the third-party application and receive a confirmation of access permission.

### Managing Authorized Applications

On Foundry’s **Settings** page, the **Authorized Applications** tab displays the third-party applications that have been approved for access. At this point, we can see that the Test application has been granted access to your account.

![Authorized applications: One application authorized](/docs/resources/foundry/platform-security-third-party/3PA-user-one-app-authorized.png)

Clicking on the **Actions** dropdown brings up the following options: **Details** and **Revoke**.

![Authorized applications: Available actions](/docs/resources/foundry/platform-security-third-party/3PA-user-available-actions.png)

Selecting **Details** displays information about the data that the third-party application can access.

![Authorized applications: Access details](/docs/resources/foundry/platform-security-third-party/3PA-user-view-details.png)

Selecting **Revoke** brings up a confirmation screen; revoking access removes the application’s ability to access information in your account.

![Authorized applications: Revoke access](/docs/resources/foundry/platform-security-third-party/3PA-user-revoke-access.png)

After revoking access, we see that no applications have been authorized to access your account. An application whose access has been revoked can be added again by repeating this workflow.

![Authorized applications: No applications authorized](/docs/resources/foundry/platform-security-third-party/3PA-user-no-apps-authorized.png)
