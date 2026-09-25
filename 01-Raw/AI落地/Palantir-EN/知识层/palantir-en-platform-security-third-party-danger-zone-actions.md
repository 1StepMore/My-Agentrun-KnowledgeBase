---
title: Palantir 官方文档（英文原版）· Danger zone actions
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/platform-security-third-party/danger-zone-actions/
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
> 原始地址：https://palantir.com/docs/foundry/platform-security-third-party/danger-zone-actions/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-danger-zone-actions.md`

# Danger zone actions

Foundry platform administrators have access to several “danger zone” actions for third-party applications. These are called “danger zone” actions because they result in irreversible changes to an application’s registration and should be treated with caution due to their potentially widespread and destructive effects. A warning dialog will appear in advance of executing these actions. The available “danger zone” actions are [rotating a client secret](#rotate-a-client-secret) and [deleting an application registration](#delete-an-application-registration).

## Rotate a client secret

You can rotate an application's secret on the [Manage application](/docs/foundry/platform-security-third-party/manage-3pa/) page for [confidential clients ↗](https://tools.ietf.org/html/rfc6749#section-2.1) only. Rotating the secret will require every user to set up the application again, since every client configured with the secret will cease to work given that the rotated secret is invalidated. Rotating secrets should only be done if the secret has become compromised or lost; keep in mind that the application will need to be reinstated after secret rotation.

:::callout{theme="warning"}
When might you want to rotate a secret? Given the consequences of rotating a secret, this is something that should only happen if the secret has been compromised or has become inaccessible.
:::

1. From **Control Panel**, navigate to the [Third-party applications](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface) page.
2. Click **Actions** on the application you want to modify, then click **Manage application**.
3. Scroll down and click on **Rotate secret**.
4. Review the warning dialog prior to confirming the action.
5. Confirm the action and securely store your new client secret as it will not be viewable again at any other time.

## Delete an application registration

1. From **Control Panel**, navigate to the [Third-party applications](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface) page.
2. Click **Actions** on the application you want to delete, then click **Manage application**.
3. Scroll down and click **Delete application**.
4. Review the warning dialog prior to confirming the action.
5. Confirm the action and the application will be deleted. This cannot be undone.
