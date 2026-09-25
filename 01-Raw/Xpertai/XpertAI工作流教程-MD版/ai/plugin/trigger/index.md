---
title: Trigger Plugin
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:46:22'
  time_wiki: '2026-09-23T00:46:22'
source_url: AI生成
source_type: article
source_platform: xpertai
author: XpertAI
fetch_date: '2026-05-08'
priority: 3
language: zh
notes: XpertAI官方文档
author_id: ''
publish_date: ''
---
# Trigger Plugin

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

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


## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

## 关联问题

- 这个概念和其他知识有什么联系？
- 这个观点和我的已有认知是否冲突？

---

## 抓取备注

- 抓取时间：2026-05-08
- 抓取工具：手动导入
- 质量评分：
