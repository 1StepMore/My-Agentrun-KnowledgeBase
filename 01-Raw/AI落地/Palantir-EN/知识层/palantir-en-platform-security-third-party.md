---
title: Palantir 官方文档（英文原版）· Third-party applications
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/platform-security-third-party/
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
> 原始地址：https://palantir.com/docs/foundry/platform-security-third-party/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-platform-security-third-party.md`

# Third-party applications

Foundry’s platform security controls ensure that integration and interoperability with third-party applications can be centrally managed while respecting established security measures. Third-party application authorization supports the [OAuth 2.0 framework](/docs/foundry/platform-security-third-party/writing-oauth2-clients/).

:::callout{theme="warning"}
Users should use [**Developer Console**](/docs/foundry/developer-console/overview/) to manage their application configuration. The **Control Panel** view only applies if **Developer Console** has not been enabled for the user.
:::

Third-party application permissions should be managed by Foundry administrators to ensure the security of the Foundry platform. The third-party application interface in [Control Panel](/docs/foundry/administration/control-panel/) enables Foundry administrators to see which applications have been registered on Foundry as well as which applications have been enabled for access. From the third-party application interface, administrators can [register new applications](/docs/foundry/platform-security-third-party/register-3pa/), [manage existing applications](/docs/foundry/platform-security-third-party/manage-3pa/), and [enable or disable applications](/docs/foundry/platform-security-third-party/enabling-3pa-access/).

## Accessing the third-party applications user interface

For users with the appropriate permissions, the third-party application management interface can be reached by clicking **Open other workspaces > [Control Panel](/docs/foundry/administration/control-panel/)** located at the lower corner of the left navigation bar. Then, choose an enrollment and an associated organization before finally selecting the **Third-party applications** tab under **Organization Settings**.

![Third-party applications tab](/docs/resources/foundry/platform-security-third-party/3pa-0.png)

Users must hold the **Third-party application administrator** role for the selected organization in order to access the third-party application management interface.

![Third-party applications permissions](/docs/resources/foundry/platform-security-third-party/3PA-permissions.png)

For more details, review [Permissions in Control Panel](/docs/foundry/administration/enrollments-and-organizations-permissions/).
