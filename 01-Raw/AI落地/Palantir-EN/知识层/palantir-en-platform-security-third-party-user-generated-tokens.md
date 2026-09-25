---
title: Palantir 官方文档（英文原版）· User-generated tokens
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/platform-security-third-party/user-generated-tokens/
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
> 原始地址：https://palantir.com/docs/foundry/platform-security-third-party/user-generated-tokens/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-user-generated-tokens.md`

# User-generated tokens

:::callout{theme="danger" title="Personal tokens must not be used in production applications"}
These tokens are associated with your personal Foundry user account and **must not be used in production applications or committed to shared or public code repositories**.
We recommend you store test API tokens as environment variables during development.
For authorizing production applications, [register an OAuth2 application](/docs/foundry/platform-security-third-party/third-party-apps-overview/).
:::

Foundry supports token-based authentication. Tokens are strings of characters that serve as secure identification for a specific user. Possession of these tokens is equivalent to possessing a user's username and password, and they should be handled securely and secretly.

## Generation

Tokens are generated from the settings dashboard. Navigate to **Account** at the bottom of the sidebar, click **Settings**, then click **Tokens**.

![Token Dashboard](/docs/resources/foundry/platform-security-third-party/token_dashboard.png)

This interface shows user-generated tokens that have been created for the current user and information on their current state and expiration date. Existing tokens can be disabled from this interface, which temporarily deactivates them, or revoked, which permanently invalidates them. To generate a new token, click **Create Token**. This will open a token creation dialog:

![Token Creation](/docs/resources/foundry/platform-security-third-party/token_creation.png)

Give the token a useful name, provide a description, and specify the date when the token should expire. After clicking **Generate**, the token will be displayed one time only for security purposes. It can be copied and used as needed, but should not be stored in any insecure manner.

## Revoke

You can revoke individual tokens in the same interface by clicking **Revoke**.

![Token Revoke](/docs/resources/foundry/platform-security-third-party/token_revoke.png)

## Inactive users

By default, Foundry user accounts are automatically deactivated after 30 days of a user not logging in. When a user is deactivated, user-generated API tokens and tokens issued to OAuth2 clients become invalid.

The user will otherwise appear fully active, and work scheduled by that user will continue to run. For instance, schedules owned by an inactive user will continue to run.

For a user to be reactivated, they simply need to log in to Foundry again.

Specific users can be exempted from automatic deactivation. For more information on this, contact your Palantir representative.
