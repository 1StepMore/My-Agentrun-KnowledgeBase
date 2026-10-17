---
title: Trigger Plugin
keywords:
- XpertAI
- AI-Agent
- documentation
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/plugin/trigger/index.md
state:
  phase: wiki
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
related: []
source: 历史文件，来源见 sources
evidence: E1
---

> 🔄 **2026-10-17 核验更新**：正文已刷新为官方当前版本（原快照 1410 字 → 现 2175 字）。
> 官方源：https://docs.xpertai.cn/en/ai/plugin/trigger/index.md
> 原子快照留档：`_backup/refresh-20261017/03-Wiki/氛围编程/工具链/Xpertai/03-官方文档/plugin-trigger-index.md`

# Trigger Plugins This section introduces **Workflow Trigger** extensions in the Xpert plugin system, especially how external messaging platforms route messages into Digital Experts. If you want a Digital Expert to be triggered not only from the in-platform chat interface, but also from external messaging systems or scheduled tasks, you can extend it through Trigger plugins. ## Integration vs Trigger External IM access is usually split into two objects: * **Integration**: stores platform credentials, callback URLs, long-connection settings, and runtime status. It connects Xpert AI to the external platform. * **Trigger**: lives in a Digital Expert workflow. It binds one integration to the current Digital Expert and controls session timeout, message aggregation, and routing. Creating a Lark, WeCom, or DingTalk bot is therefore not finished after saving the integration. You must also add the corresponding trigger to the target Digital Expert workflow and publish the workflow. For tenant-level installation requirements and recommended connection modes, see [Integration Overview](../integration/). ## Scope of this section * [Schedule Trigger plugin implementation](./schedule-trigger/) * [Lark Trigger](./lark-trigger/) * [WeCom Trigger](./wecom-trigger/) * [DingTalk Trigger](./dingtalk-trigger/) ## Design highlights Trigger plugins typically implement the following capabilities: 1. **Trigger metadata (`meta`)**: Used to display trigger name, icon, and config form in the frontend. 2. **Configuration validation (`validate`)**: Checks required fields and binding conflicts before publishing. 3. **Publish and stop (`publish / stop`)**: Registers and releases trigger runtime resources. 4. **Bootstrap recovery strategy (`bootstrap`)**: Controls whether triggers recover automatically after system restart. ## Related features * Workflow trigger concepts and node description: [Trigger](../../workflow/trigger/) * Multi-entry access for Digital Expert: [Digital Expert](../../agent/agent/) * Plugin system overview: [Plugin Overview](../overview/) This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.
