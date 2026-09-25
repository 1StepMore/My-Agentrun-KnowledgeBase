---
title: Palantir 官方文档 · platform-security-management · 管理组织和空间
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-security-management/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:24:14+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# 管理组织和空间

## 组织

组织权限应通过[控制面板](/docs/foundry/administration/enrollments-and-organizations/)进行管理。进一步的组织配置在 Foundry 设置选项卡中进行管理。

![管理组织](../../foundry-docs/platform-security-management/media/manage-organizations.png)

### 管理组织成员资格

用户可以通过两种方式与组织关联：

#### 成员资格

用户只能是一个组织的成员。这可以在用户创建时指派，通过您的 SAML 设置映射 [Admin > Authentication > Organization assignment](/docs/foundry/authentication/org-assignment/)，或在用户界面中管理。

组织成员资格定义以下内容：

* 在用户个人资料中显示的组织。
* 其他组织用户的可见性（参见组织发现）。
* 用户创建的项目和组将自动标记为其组织，默认情况下将资源限制在组织内。

#### 客人成员资格

其他组织的用户可以查看此组织中的项目、文件、用户、组、标签类别和集合。客人可以是用户或组。虽然每个用户只有一个主要的组织成员资格，但用户可以拥有任意数量组织的客人成员资格。

:::callout{theme="neutral"}
客人成员资格将允许您查看将此组织作为主要组织的用户，但不能查看此组织的其他客人用户。将此作为主要组织的用户始终可以查看此组织的客人用户。
:::

您可以从 Foundry **设置**页面的组织选项卡中向您的组织添加客人：

![管理组织客人成员资格](/docs/resources/foundry/platform-security-management/organization-settings-page.png)

### 主页文件夹和组织

启用 Foundry 主页文件夹时，它们会自动标记为用户的组织。

:::callout{theme="warning"}
禁用主页文件夹的配置选项目前处于测试阶段。请联系 Palantir 支持以启用此功能。
:::

## 空间

:::callout{theme="neutral"}
**空间**已经从其以前的名称**命名空间**重新命名。
:::

空间设置在[控制面板](/docs/foundry/administration/enrollments-and-organizations/)的**空间**选项卡中进行管理。

![管理空间](/docs/resources/foundry/platform-security-management/spaces-tab.png)

### 空间设置

空间上的设置通过定义或限制某些方面来管理底层项目。以下是您可以在空间设置中配置的一些设置：

* **访问要求：** 一个空间受组织保护。底层项目只能由相同的组织或它们的子集保护。
* **角色：** 用户必须在空间上拥有角色并满足其访问要求才能创建项目或管理空间设置。
* **删除策略：** 删除策略定义何时删除空间及其项目。删除策略以组织为基础构建，遵循最后退出语义，即当用于删除策略的所有组织本身被删除时，空间才会被删除。
* **文件系统：** 文件系统是存储空间中所有项目数据的地方。文件系统一旦设置就不能修改。
* **资源管理：** [资源管理](/docs/foundry/resource-management/overview/)应用程序是管理[使用账户](/docs/foundry/resource-management/ecosystem/)和[资源队列](/docs/foundry/resource-management/overview/)的工具，可在空间上进行配置。
* **使用账户：** 项目的资源使用量积累到其自己的使用账户中。此使用账户作为默认值，可以在每个项目的基础上被覆盖。
* **资源队列：** 项目的计算资源从其资源队列中分配。
* **角色集：** 项目只能使用其空间允许的角色集中的角色。默认情况下，这是`项目默认`角色集，但可以替换为[自定义角色集](/docs/foundry/platform-security-management/manage-roles/)。注意，如果使用自定义角色集，则在空间上授予的角色不会继承到项目中。
* **项目默认角色：** 默认情况下，在此空间中创建的所有项目将具有这些默认角色。角色可以在每个项目的基础上被覆盖。
* **文件夹和文件上的角色授予：** 启用时，可以在默认情况下为新项目中的文件夹和文件指派用户角色。此设置仅在创建新项目时初始化此行为，并不会强制此行为应用于现有项目。了解更多关于禁用[文件夹和文件上的角色授予](/docs/foundry/security/projects-and-roles/#role-grants-on-folders-and-files)的信息。

![空间设置](../../foundry-docs/platform-security-management/media/space-settings.png)
