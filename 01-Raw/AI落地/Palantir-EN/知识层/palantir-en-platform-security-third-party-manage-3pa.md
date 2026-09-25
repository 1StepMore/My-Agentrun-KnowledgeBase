---
title: Palantir 官方文档（英文原版）· Manage third-party application configuration
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/platform-security-third-party/manage-3pa/
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
> 原始地址：https://palantir.com/docs/foundry/platform-security-third-party/manage-3pa/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-manage-3pa.md`

# Manage third-party application configuration

:::callout{theme="warning"}
Users should use [**Developer Console**](/docs/foundry/developer-console/overview/#application-pages) to manage their application configuration. The **Control Panel** view only applies if **Developer Console** has not been enabled for the user.
:::

You can access the manage application interface by selecting **Manage application** from the **Actions** dropdown located to the right of an application in the [third-party applications user interface](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface). Here, you can review and edit an application’s registration such as its name, description, logo, authorization grant types, and application discovery settings.

:::callout{theme="neutral"}
The **Manage application** interface is only available to permissioned members of the managing Organization for a third-party application.

The organization that the user creates an application in is deemed the managing organization of the application, and anyone in the organization who has the **Manage OAuth 2.0 clients** permission can manage the third-party application.

The managing Organization can determine which other organizations can see and use the third-party application through the application discovery settings.
:::

The following is an example of a **Manage application** page shown for an example application:

![Manage application](/docs/resources/foundry/platform-security-third-party/3PA-manage-application-page.png)

## Delete an application registration

[Danger zone actions](/docs/foundry/platform-security-third-party/danger-zone-actions/) are located at the bottom of the **Manage application** page.

![Manage application: Danger zone](/docs/resources/foundry/platform-security-third-party/3PA-danger-zone.png)

To permanently prevent users from authorizing a third-party application, the application’s registration can be revoked: that is, deleted from Foundry.

This is considered a “danger zone action” as it is irrevocable and will render the third-party application unusable by all users unless the application is re-registered. If an application is re-registered, users will have to reauthorize the third-party application since Foundry treats the re-registration as a new registration.

Learn how to delete an application's registration from the [danger zone actions documentation](/docs/foundry/platform-security-third-party/danger-zone-actions/#delete-an-application-registration).
