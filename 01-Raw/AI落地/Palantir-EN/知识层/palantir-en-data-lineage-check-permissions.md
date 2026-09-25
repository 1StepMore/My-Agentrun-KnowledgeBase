---
title: Palantir 官方文档（英文原版）· Check resource permissions
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/data-lineage/check-permissions/
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
> 原始地址：https://palantir.com/docs/foundry/data-lineage/check-permissions/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-data-lineage-check-permissions.md`

# Check resource permissions

You can use Data Lineage to check users' permissions to view datasets or artifacts using the "Permissions" coloring option. To do that, start by adding nodes to the graph. You can do so using the search helper on the side panel.

![Add nodes to the graph](/docs/resources/foundry/data-lineage/data_lineage_permissions_1.gif)

Then expand the graph to view the lineage leading to your resource (read more about [exploring lineage](/docs/foundry/data-lineage/explore-lineage/)).

![Expand graph to view lineage](/docs/resources/foundry/data-lineage/data_lineage_permissions_2.gif)

Once you have done this, use the **Node color options** dropdown to select the **Permissions** color scheme.

![Select permissions color scheme](/docs/resources/foundry/data-lineage/data_lineage_permissions_3.gif)

Select the user's name from the **View as** dropdown. This will allow you to see the user's permissions to each of the nodes on the graph.

![Select user's name from dropdown](/docs/resources/foundry/data-lineage/data_lineage_permissions_4.gif)

There are two permission types you can color by:

* [Data access in datasets](#data-access-in-datasets)
* [Resource access](#resource-access)

![Permission types for coloring nodes](/docs/resources/foundry/data-lineage/data_lineage_permissions_5.png)

### Data access in datasets

Use this option to troubleshoot permissions issues. Remember that a user's data access is affected by data lineage (see [Platform Security](/docs/foundry/security/checking-permissions/)). By coloring your nodes based on the user's access to data, you can easily see what the upstream datasets are that may restrict the user's access to data.

This option only works on dataset nodes.

### Resource access

This will allow you to see the [role](/docs/foundry/security/projects-and-roles/) (such as Editor, Viewer, etc.) that is set for the selected user on the selected resource.

Use this option to view the level of access users have to your artifacts.

:::callout{theme="neutral"}
Roles do not correspond to data lineage the same way that data access does. For example, a user being an "Editor" on a Contour Analysis does not guarantee they have permissions to see the data that the analysis depends on. Make sure your users can access the underlying data when sharing a resource with them.
:::
