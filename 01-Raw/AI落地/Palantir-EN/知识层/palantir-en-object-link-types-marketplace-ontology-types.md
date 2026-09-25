---
title: Palantir 官方文档（英文原版）· Add object and link types to a Marketplace product
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/object-link-types/marketplace-ontology-types/
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
> 原始地址：https://palantir.com/docs/foundry/object-link-types/marketplace-ontology-types/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-object-link-types-marketplace-ontology-types.md`

# Add object and link types to a Marketplace product

Use [Foundry DevOps](/docs/foundry/devops/overview/) to include your object and link types in [Marketplace products](/docs/foundry/devops/core-concepts/#product) for other users to install and reuse. [Learn how to create your first product.](/docs/foundry/foundry-devops/create-products/)

## Unsupported features

Most [object property types](/docs/foundry/object-link-types/properties-overview/) are supported in Marketplace products, but the following are not yet available:

* [Cipher](/docs/foundry/cipher/overview/)
* Geo time
* Vector

Marketplace products do not yet support the following:

* Object types with streaming datasources

Objects themselves cannot be packaged with Marketplace. This means that, for example, object edits made by Actions cannot be packaged into a Marketplace product. However, datasets and object types can be packaged in order to create new objects after installation of a Marketplace product.

[Object types without backing datasources](/docs/foundry/object-link-types/create-object-type/#create-an-object-type-without-a-backing-datasource) are supported in Marketplace products.

If you require support for any of the unsupported features above, contact Palantir Support.

## Add object types to products

To add an object type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). [Add outputs](/docs/foundry/foundry-devops/create-products/#add-outputs) and then select the **Add ontology entities** option.

You will then be prompted to choose an object type. After selecting an object type, you will see recommendations for linked object types that you may want to add to your product.

![add object type](/docs/resources/foundry/object-link-types/marketplace-add-object-type-dialog.png)

## Add link types to products

To add a link type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/) and then select the **Link type** content type.

You will then be prompted to choose a link type as below.

![add link type](/docs/resources/foundry/object-link-types/marketplace-add-link-type-dialog.png)

While you can select link types directly, we recommend first adding your object types and then selecting relevant links via the [information panel](/docs/foundry/foundry-devops/create-products/#add-outputs) as below.

![add link type via panel](/docs/resources/foundry/object-link-types/marketplace-add-link-type-panel.png)

## Add shared properties to products

To add a shared property type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). Then, select the **Shared property** content type as shown below.

You will then be prompted to choose a shared property.

![Add a shared property to a Marketplace product.](/docs/resources/foundry/object-link-types/marketplace-add-shared-property-dialog.png)

## Add interface types to products

To add an interface type to a product, first [create a product](/docs/foundry/foundry-devops/create-products/). Then, select the **Interface** content type as shown below.

You will then be prompted to choose an interface.

![Add an interface type to a Marketplace product.](/docs/resources/foundry/object-link-types/marketplace-add-interface-dialog.png)
