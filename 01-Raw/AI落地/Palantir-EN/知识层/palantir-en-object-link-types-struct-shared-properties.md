---
title: Palantir 官方文档（英文原版）· Struct properties and shared property types
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/struct-shared-properties/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/struct-shared-properties/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-struct-shared-properties.md`

# Struct properties and shared property types

Struct properties can be used by local and shared property types. When converting, or promoting a local property type to a shared property type, struct fields need to be re-mapped. Local struct property types backed by shared property types will inherit shared property type fields except for the struct field resource identifiers (RIDs). Struct field metadata (display name, description, aliases) will then be inherited from the shared property type, but struct fields will keep their original RIDs.

## Create a struct type shared property

1. In Ontology Manager, you can create a struct type shared property in two ways:
   * From the top right of the homepage, select **New > Shared property**
      <img src="./media/new-dropdown-menu-shared-property.png" alt="Shared property option from the New dropdown menu." width="300" />

   * Select **Shared properties > + New shared property**
      <img src="./media/new-shared-property-button.png" alt="+ New shared property option in the Shared properties tab." width="500" />

2. In the main panel, select the **New shared property** button. This will open a helper where you can configure metadata of the shared property including the name, description, aliases, and API name. Then select **Next** to proceed.

    <img src="./media/create-shared-property-modal.png" alt="The 'Create shared property' dialog." width="500" />

3. Configure the base type, value type, visibility, and whether to require values for the property.

    <img src="./media/create-shared-property-configuration.png" alt="Create shared property window on the configuration step." width="500" />

4. Select a project to save this shared property to.

    <img src="./media/create-shared-property-save-location.png" alt="Select save location for the shared property." width="500" />

5. Back in Ontology Manager, select **Save** in the upper right corner to [make the change to your ontology](/docs/foundry/ontology-manager/save-changes/).

## Attach a struct type shared property

1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.
2. In the **Property editor** to the right, scroll down to **Shared property** and select a shared property under **Assign**. This will share property metadata among both properties.

<img src="./media/spt-attachment.png" alt="The shared property dropdown in the Assign section." width="500" />

**Note:** To add new struct fields after assigning a shared property type to a local struct property type, you must add the new struct fields to the shared property type and map them to datasource columns for all local struct property types that are backed by the shared property.

## Convert a struct property type into a shared property

The following instructions detail how to convert a struct property into a struct property backed by a shared property type.

1. In Ontology Manager, open the **Properties** tab and select the desired property from the **Properties** table.
2. In the **Property editor** to the right, scroll down and select **Convert to a shared property**, which backs the struct property by a shared property type.

<img src="./media/spt-convert.png" alt="The 'Convert to a shared property' button in the Property editor." width="500" />
