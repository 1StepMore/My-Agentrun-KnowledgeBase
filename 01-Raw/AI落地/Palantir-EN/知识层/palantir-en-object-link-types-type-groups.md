---
title: Palantir 官方文档（英文原版）· Object type groups
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/type-groups/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/type-groups/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-type-groups.md`

# Object type groups

Object type groups are a classification primitive that helps users better search and explore their ontology. Groups are created and managed using Ontology Manager, generally by ontology [owners and editors](/docs/foundry/object-link-types/type-groups/#group-permissions).

## Group configuration

Groups are created and managed via the groups menu, accessible in the Ontology Manager sidebar.

![Choose or add a new group](/docs/resources/foundry/object-link-types/groups-menu.png)

Groups can also be added directly to object types by selecting **Edit groups** in the object type overview page.

![add a group to an object type](/docs/resources/foundry/object-link-types/group-add-to-object.png)

## Group search and discovery

Groups are searchable in [Ontology Manager's **Search** bar and **Search** bar dialog](/docs/foundry/ontology-manager/navigation/#header-search-bar). The table of object types in Ontology Manager supports displaying and filtering by group. Groups are also displayed on the [Object Explorer home page](/docs/foundry/object-explorer/getting-started/#group-exploration-b-c-d).

![Filter By Group](/docs/resources/foundry/object-link-types/object-type-groups-add.png)

## Group permissions

To view object type groups, users must have **viewer** permission on the project that the object type group is in.

## Legacy group migration

As of May 22, 2024, the *group* primitive described on this page has replaced the tag-based system of legacy groups.

In most cases, legacy groups were automatically migrated to object type groups at this time. Ontology owners were notified via an Upgrade Assistant intervention if manual action was necessary.

### Group name visibility

Previously, if all object types inside a group were non-discoverable to a certain user (for example, due to access controls on backing datasets), the group was also non-discoverable to the user. As mentioned in the section above on [group permissions](/docs/foundry/object-link-types/type-groups/#group-permissions), all groups will now be discoverable to any user that can view the ontology. This change aligns group visibility with other [ontology primitives](/docs/foundry/object-permissioning/ontology-permissions-legacy/#ontology-roles) to increase clarity and transparency in governance.

### Migration of partially visible groups

Legacy groups that were not discoverable to one or more users were not eligible for automatic migration. In these cases, ontology owners were notified via an Upgrade Assistant intervention that manual action was necessary.

On May 22 2024, legacy groups that could not be safely migrated were hidden from operational users across all applications such as Workshop and Object Explorer. To provide backward compatibility, the names of legacy groups remain stored as [type class metadata](/docs/foundry/object-link-types/metadata-typeclasses/) on object types.

Ontology owners may continue to manually migrate these hidden, legacy groups using Ontology Manager. To do this, navigate to the **Ontology Configuration** menu in the bottom left corner and select **Approve all Groups for migration**.
