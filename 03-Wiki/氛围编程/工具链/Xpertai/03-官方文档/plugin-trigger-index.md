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

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger Plugin

This section introduces extensions related to **Workflow Trigger** in the Xpert plugin system.

If you want a Digital Expert to be triggered not only from the in-platform chat interface, but also from external messaging systems or scheduled tasks, you can extend it through Trigger plugins.

## Scope of this section

* [Schedule Trigger plugin implementation](./schedule-trigger/)
* [Lark Trigger plugin implementation](./lark-trigger/)

## Design highlights

Trigger plugins typically implement the following capabilities:

1. **Trigger metadata (`meta`)**: Used to display trigger name, icon, and config form in the frontend.
2. **Configuration validation (`validate`)**: Checks required fields and binding conflicts before publishing.
3. **Publish and stop (`publish / stop`)**: Registers and releases trigger runtime resources.
4. **Bootstrap recovery strategy (`bootstrap`)**: Controls whether triggers recover automatically after system restart.

## Related features

* Workflow trigger concepts and node description: [Trigger](../../workflow/trigger/)
* Multi-entry access for Digital Expert: [Digital Expert](../../digital-expert/digital-expert/)
* Plugin system overview: [Plugin Overview](../overview/)
