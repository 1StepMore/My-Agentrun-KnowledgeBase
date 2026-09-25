---
title: 🧩 Plugin Development
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
# 🧩 Plugin Development

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 🧩 Plugin Development

### [1. Overview](./overview)

* Goals and design philosophy of the plugin system
* Why plugin architecture: flexible extension, modular decoupling, ecosystem building
* Applicable scenarios for plugin development

### [2. Core Concepts of the Plugin System](./concepts/)

* **XpertPlugin**: Entry definition of a plugin
* **Enhancement Points**: Mounting points for plugins to extend system functionality
* **Plugin Lifecycle**: `register`, `onStart`, `onStop`, `onPluginBootstrap`, `onPluginDestroy`
* **Configuration Schema**: Plugin configuration definition based on `zod`
* **Strategy Pattern**:

  * Integration Strategy (system integration strategy)
  * Document Source Strategy (document data source strategy)

### 3. Plugin Directory Structure

* Explanation of plugin package.json
* Typical directory structure (`plugin.ts`, `*.strategy.ts`, `*.controller.ts`, `*.service.ts`)
* Dependency relationship between plugin and host system

### [4. Plugin Development Steps](./develop/)

1. **Initialize the plugin**: Define plugin metadata (`meta`) and configuration (`config`)
2. **Register plugin modules**: Use the `@XpertServerPlugin` decorator
3. **Implement Integration Strategy**: Define external service integration
4. **Implement Document Source Strategy**: Define data source integration
5. **Provide services and controllers**: Expose REST API / service methods
6. **Write test cases**

### [5. Plugin Example: Lark Docs Integration](./lark)

* Introduction to the Lark Docs plugin
* Configuration example
* Code breakdown (meta, IntegrationStrategy, DocumentSourceStrategy, Controller)
* Complete workflow for loading document data

### 6. Plugin Lifecycle and Events

* Plugin registration → startup → destruction
* Logging and debugging methods
* How to manage plugin state

### 7. Best Practices for Development

* Plugin decoupling and reuse
* Plugin configuration and security (key, API Key management)
* Error handling and exception isolation
* Logging and observability

### [8. Publishing and Usage](./install/)

* Plugin packaging and version management
* Plugin installation and activation
* Plugin update and uninstallation

### 9. Frequently Asked Questions (FAQ)

* How to manage dependencies between plugins and host services?
* How to register database entities in plugins?
* How to call external APIs in plugins?
* Can plugins be loaded and unloaded dynamically?


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
