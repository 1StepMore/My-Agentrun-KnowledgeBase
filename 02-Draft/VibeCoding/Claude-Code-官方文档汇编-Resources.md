---
title: Claude Code 官方文档汇编 · Resources
source: Claude Code 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/claude-code/claude-code-en-legal-and-compliance.md
evidence: E1
domain: VibeCoding
keywords:
- claude-code
- vibe-coding
- AI编程
- AI-Agent
- context-engineering
state:
  phase: draft
  time_raw: 2026-09-23 02:42:51+08:00
  time_draft: 2026-09-23 03:14:06+08:00
  time_wiki: null
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---

> **汇编性质**：Claude Code 官方文档 官方原文 1 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## Legal and compliance

- 官方原文：https://code.claude.com/docs/en/legal-and-compliance.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-legal-and-compliance.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Legal and compliance

> Legal agreements, compliance certifications, and security information for Claude Code.

## Legal agreements

### License

Your use of Claude Code is subject to:

* [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) - for Team, Enterprise, and Claude API users
* [Consumer Terms of Service](https://www.anthropic.com/legal/consumer-terms) - for Free, Pro, and Max users

### Commercial agreements

Whether you're using the Claude API directly (1P) or accessing it through Amazon Bedrock or Google Cloud's Agent Platform (3P), your existing commercial agreement will apply to Claude Code usage, unless we've mutually agreed otherwise.

### Can customers offer Claude Code in their products?

Unless we've mutually agreed otherwise, preinstalling or running Claude Code in your products or services (e.g. in hosted sandboxes or other agent infrastructure) requires agreeing to our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and complying with the conditions below:

* **The Claude Code binary must not be modified.** Claude Code must be installed and run as published by Anthropic, and customers may not remove, disable, or restrict any authentication method built into it (including methods that permit signing in with a Claude account or the user's own API key).
* **Customers may not pay for, resell, or intermediate Claude usage on their end users' behalf.** Each end user must authenticate with their own Anthropic API key, Claude subscription plan credentials, or 3P inference provider credential (Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry). That usage is billed directly to the end user under their own agreement with Anthropic or, for third-party inference providers, with the applicable provider.

**Using the Claude Code name and logo.** You can accurately say, in plain text, that your product has Claude Code preinstalled or that it runs Claude Code. But you can't use the Claude Code or Anthropic names or logos as part of your own product, feature, or company name, in your own logo, or in a way that suggests Anthropic built, endorses, or is partnered with your product. Any other use of Anthropic's names or logos is governed by our [Trademark Guidelines](https://www.anthropic.com/legal/trademark-guidelines) and requires our written permission.

Claude Code remains governed by Anthropic's standard terms (see the License and Commercial agreements sections above) regardless of the platform through which it is accessed.

## Compliance

### Healthcare compliance (BAA)

If a customer has executed a Business Associate Agreement (BAA) with Anthropic and has [Zero Data Retention (ZDR)](/docs/en/zero-data-retention) enabled for the relevant organization, that BAA extends to the customer's API traffic through Claude Code.

## Usage policy

### Acceptable use

Claude Code usage is subject to the [Anthropic Usage Policy](https://www.anthropic.com/legal/aup). Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK.

### Authentication and credential use

Claude Code authenticates with Anthropic's servers using OAuth tokens or API keys. These authentication methods serve different purposes:

* **OAuth authentication** is intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications. For the sign-in steps, see [Logging in to your Claude account](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account); for how Claude Code performs OAuth authentication, see [Authentication](/docs/en/authentication).
* **Developers** building products or services that interact with Claude's capabilities, including those using the [Agent SDK](/docs/en/agent-sdk/overview), should use API key authentication through [Claude Console](https://platform.claude.com/) or a supported cloud provider. Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials on behalf of their users. Moreover, developers may not collect, store, or intermediate Claude.ai credentials or session tokens — sign-in to a Claude account must complete through Anthropic's own flow.

This does not restrict how customers provision and manage their own API keys or third-party inference provider credentials — for example, configuring an API key in a development environment, secrets manager, or machine image for use by the customer's own authorized users — provided the resulting usage is billed to the key owner under their agreement with Anthropic (or the applicable provider) and is not resold or intermediated as described above. Nor does it prevent an end user from signing in to the unmodified Claude Code binary with their own Claude subscription, including where a platform hosts Claude Code as described under *Can customers offer Claude Code in their products?* above.

Anthropic reserves the right to take measures to enforce these restrictions and may do so without prior notice.

For questions about permitted authentication methods for your use case, please [contact sales](https://www.anthropic.com/contact-sales?utm_source=claude_code\&utm_medium=docs\&utm_content=legal_compliance_contact_sales).

## Security and trust

### Trust and safety

You can find more information in the [Anthropic Trust Center](https://trust.anthropic.com) and [Transparency Hub](https://www.anthropic.com/transparency).

### Security vulnerability reporting

Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/4f1f16ba-10d3-4d09-9ecc-c721aad90f24/embedded_submissions/new).

***

© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.
