---
title: Palantir 官方文档 · 管理 · 管理和使能
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/administration/overview/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:23:28+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

![admin overview](../../foundry-docs/administration/media/7-Admin.svg)

# 管理和使能

Palantir平台提供了全套的治理和管理功能，这些功能可以通过一个称为**控制面板**的集中界面访问。平台将安全性、资源管理、应用案例生命周期和审计能力整合到一个共享基础上，可以在不同的实现中一致应用。除了核心治理之外，这还支持企业数据架构的规模化实施，包括“数据网格”和“数据织物”范式。在集中和联邦模型中，Palantir的管理、管理和使能方法能够消除安全性与丰富协作之间的传统妥协。

## 控制面板

所有管理工作流都可以在[控制面板](/docs/foundry/administration/control-panel/)中执行，这是Palantir用于管理平台的集中界面。您可以通过选择**打开其他工作区**从[工作区侧边栏](/docs/foundry/getting-started/orientation-and-nav/#the-sidebar)访问控制面板。

## 配置和管理注册

Palantir注册被定义为由平台管理员管理的一个或多个“[组织](/docs/foundry/security/orgs-and-spaces/#organizations)”。每个管理功能都可以映射到现有的治理实现（如Active Directory），并在预先存在的组和特定角色之间进行细粒度映射。通过控制面板，可以定义、联邦和实施全范围的管理任务。

[了解更多关于管理注册的信息。](/docs/foundry/administration/enrollments-and-organizations/)

## 认证

Palantir平台的访问认证是通过注册的身份提供者进行管理，这些提供者既提供用户验证，也提供驱动[安全控制](/docs/foundry/platform-security-management/manage-users/)所需的自由裁量属性。Palantir利用SAML 2.0开放标准，并提供了一种直观的机制，将元数据属性映射到平台内管理的用户属性。随着Palantir平台在一个组织中的使用扩展，并有可能涵盖外部合作伙伴组织，可以添加和管理额外的身份提供者。

[了解更多关于认证的信息。](/docs/foundry/authentication/overview/)

## 资源管理

Palantir为管理员提供了全面的资源管理工具，使他们能够了解和管理平台资源的使用情况。这套功能确保可操作的细粒度指标可以与语义上有意义的账户、项目甚至单个资源关联起来。使用可见性工作流提供了一个丰富的视角，展示了面向项目的资源支出，而资源分配工作流允许管理员定义项目如何消耗共享资源——并在需要时对这种消耗进行限制。

[了解更多关于资源管理的信息。](/docs/foundry/resource-management/overview/)

## 平台体验

Palantir提供了一系列配置选项，旨在实现组织一致性和用户体验的聚焦。这包括[可配置的工作区](/docs/foundry/carbon/overview/)，它将平台应用程序的总集成管理成一个子集，以满足特定团队或用户类型的需求。用户着陆页、平台标识和其他资产也可以定制，以确保Palantir平台与更广泛组织的外观和品牌本地集成。

了解更多关于定制平台体验的信息：

* [配置工作区](/docs/foundry/administration/configure-workspaces/)
* [配置主页URL](/docs/foundry/administration/configure-homepage-url/)
