---
title: Palantir 官方文档（英文原版）· Value type permissions
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/value-types-permissions/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/value-types-permissions/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-value-types-permissions.md`

# Value type permissions

Permissioning for value types is managed through platform [space](/docs/foundry/platform-security-management/manage-orgs-and-spaces/#spaces). Any value types in a space are automatically imported and made available for the associated ontology. Other consumers can import the value types into their project scopes, similar to how users can import transforms profiles or inputs to pipelines.

Users who have View (read) permissions to a space can assign value types to property types or shared property types in that space and associated ontology. An Editor or Owner of a space can create, edit, or delete value types in that space.
