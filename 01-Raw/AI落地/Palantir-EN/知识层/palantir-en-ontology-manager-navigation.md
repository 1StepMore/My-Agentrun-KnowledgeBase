---
title: Palantir 官方文档（英文原版）· Navigation
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/ontology-manager/navigation/
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
> 原始地址：https://palantir.com/docs/foundry/ontology-manager/navigation/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-ontology-manager-navigation.md`

# Navigation

## Header search bar

In the middle of the header of the application is the **Search** bar. You can click into the **Search** bar or hold down `Cmd/Ctrl + K` to open the **Search** bar dialog.

![Search bar](/docs/resources/foundry/ontology-manager/oma-user-interface-navigation-search.png)

Searching in the **Search** bar from the home page will update the home page with the list of resources that match the search. You can search for any object type, property, link type, action type, shared properties, interfaces, or functions you are interested in. The search results will highlight which field your search term matched on. You can use the up-arrow and down-arrow keys on your keyboard to move through search results and see previews for the selected results. You can select **Open** or use the Enter key to open the selected result.

![Search in header](/docs/resources/foundry/ontology-manager/oma-user-interface-navigation-search-in-header.png)

## Home page filters

The **Object types**, **Link types**, **Action Types**, **Shared Properties**, **Interfaces**, and **Functions** pages can be selected from the home page sidebar. These pages allow for filtering object types and link types based on their visibility, development status, and indexing issues.

![Home page sidebar](/docs/resources/foundry/ontology-manager/oma-user-interface-navigation-homepage-sidebar.png)

Object types whose backing datasources are unregistered or have failed to reindex into Object Storage v1 (Phonograph) will have red error messages in the issue column of the object type page.

## Navigation back from a selection

Once you have opened an object type, link type, or action type, you have the option to select **Back home** from the top left corner of the view’s sidebar.

![Back home](/docs/resources/foundry/ontology-manager/oma-user-interface-navigation-back-home.png)

Hovering over the **Back home** button will also bring up quick links to recently edited object types, link types, and action types, as well as all resources that are related to the one you are currently viewing.

<img src="./media/oma-user-interface-navigation-back-home-hover.png" alt="Back home hover" width="400" />
