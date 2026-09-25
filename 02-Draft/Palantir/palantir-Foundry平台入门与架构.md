---
title: Palantir 官方文档汇编 · Foundry平台入门与架构
source: Palantir 官方文档（一手来源，中文机翻版，逐篇 URL 见 sources_note）
keywords:
- Palantir
- Foundry
- AIP
- AI平台
- AI工程
sources:
- AI落地/Palantir/知识层/palantir-zh-administration-overview.md
- AI落地/Palantir/知识层/palantir-zh-getting-started.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-application-reference.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-authentication.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-debug-using-devtools.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-delivering-a-use-case.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-file-support-ticket.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-http-error-codes.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-introductory-concepts.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-issues.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-network-requirements.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-next-steps-by-role.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-orientation-and-nav.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-overview.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-projects-and-resources.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-quicksearch.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-support-overview.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-supported-browsers.md
- AI落地/Palantir/知识层/palantir-zh-getting-started-training-application.md
- AI落地/Palantir/知识层/palantir-zh-platform-overview.md
- AI落地/Palantir/知识层/palantir-zh-platform-overview-aip-capabilities.md
- AI落地/Palantir/知识层/palantir-zh-platform-overview-architecture.md
- AI落地/Palantir/知识层/palantir-zh-platform-overview-development-life-cycle.md
- AI落地/Palantir/知识层/palantir-zh-platform-overview-interoperability.md
- AI落地/Palantir/知识层/palantir-zh-platform-overview-overview.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-disabling-ignore-inherited-permissions.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-disabling-propagate-view-requirements.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-groups.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-markings.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-orgs-and-spaces.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-project-constraints.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-restricted-views.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-roles.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-users.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-3pa-api-guidance.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-authorizing-3pa-access.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-danger-zone-actions.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-enabling-3pa-access.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-manage-3pa.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-register-3pa.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-third-party-apps-overview.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-user-generated-tokens.md
- AI落地/Palantir/知识层/palantir-zh-platform-security-third-party-writing-oauth2-clients.md
state:
  phase: draft
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23 02:25:43+08:00
  time_wiki: '2026-09-23T10:40:21+08:00'
related:
- '[[企业语义层建模-从数据仓库到数字孪生]]'
- '[[LLM驱动语义层构建的五种方法论]]'
wiki_ref: 03-Wiki/AI落地/_MOC-AI落地.md
---

> **本汇编性质**：Palantir 官方文档原文（45 篇）按主题合并，逐节保留原始 URL。
> 官方标注中文页为 **未经人工验证的机器翻译**；权威表述以英文原版为准（`/docs/foundry/...` 去掉 `zh`）。
> 本汇编**不做改写**，仅去除站点导航与重复声明——可逐节回溯官方原文。
> 汇编时间：2026-09-23T02:25:43+08:00

---

## [管理] 管理和使能

> **原文取证**：本汇编据官方**中文机翻**整理；引用原句请用英文原文层 `01-Raw/AI落地/Palantir-EN/知识层/`（126 篇 E1 原文，2026-09-23 抓取）。

- 官方原文：https://palantir.com/docs/zh/foundry/administration/overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-administration-overview.md`

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

---

## [入门] 开始使用Palantir

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started.md`

# 开始使用Palantir

Palantir平台旨在帮助您以数据解决现实世界的问题。Palantir平台被以下用户使用：

* **各种类型的组织：** 从初创企业到跨国公司，再到世界各地的政府。
* **各种类型的用户：** 从IT管理员、软件工程师和数据科学家，到护士、技术人员和操作员。

## 获取访问权限

如果您准备开始但尚未获得Palantir平台的访问权限，您可以：

* **[注册AIP Now ↗](https://signup.palantirfoundry.com/signup?signupPermitCode=BUILD_WITH_AIP\&tracking-code=ptcom-docs)** 获取平台访问权限并以试用帐户开始搭建。
* **[注册AIP训练营 ↗](https://www.palantir.com/platforms/aip/bootcamp/)** 在数小时或数天内从零到应用案例，与Palantir工程师一同工作。

## 开始搭建

一旦您获得访问权限，我们推荐以下资源帮助您在Palantir平台上起步：

* **[用AIP搭建 ↗](https://build.palantir.com)** 是一个精心策划的示例、教程和入门包库，以加速您的搭建工作流程。如果您已有入学访问权限，可以在 `<your-enrollment-URL>/workspace/now/platform` 找到用AIP搭建。
* **[Palantir学习 ↗](https://learn.palantir.com/)** 门户提供课程、工作流程教程、认证等，帮助您从平台中获得最大价值。
* **[AIP Assist](/docs/foundry/assist/overview/)** 是一个由LLM驱动的工具，旨在帮助您导航、理解并通过Palantir平台生成价值。AIP Assist可以通过界面左下角的专用图标在平台内访问。
* **[Solution Designer](/docs/foundry/solution-designer/overview/)** 是一个用于创建使用Palantir平台搭建的解决方案的架构表示的交互工具。如果您已有入学访问权限，可以在 `<your-enrollment-URL>/workspace/solution-design` 找到Solution Designer。

## 继续学习

您可以通过以下资源了解更多关于Palantir平台的信息：

* [Palantir开发者论坛 ↗](https://community.palantir.com/) 是一个向其他用户提问和回答问题的空间。
* [平台文档](/docs/foundry/platform-overview/overview/) 包含关于平台功能和特性的详细信息。我们建议您从一些[入门概念](/docs/foundry/getting-started/introductory-concepts/)开始，或者根据您的角色了解更多关于[平台的下一步](/docs/foundry/getting-started/next-steps-by-role/)。

---

## [入门] 应用程序参考

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/application-reference/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-application-reference.md`

# 应用程序参考

您可以通过[侧边栏](/docs/foundry/getting-started/orientation-and-nav/#the-sidebar) 上可访问的应用程序与Palantir平台互动。本页面提供了可用应用程序的参考，并描述了何时可能需要使用每个应用程序。

## 数据集成

|应用程序  |描述  |用途  |
|---  |---  |---  |
|[Data Lineage](/docs/foundry/data-lineage/overview/) |Data Lineage显示了数据在平台中流动的图形。 |探索Palantir平台中任何数据的来源或下游使用。 |
|[Pipeline Builder](/docs/foundry/pipeline-builder/overview/) | Pipeline Builder使用内置的数据变换创建从数据源到最终输出的端到端管道。 |通过批量和流式管道集成数据以进行分析和应用程序搭建。 |
|[Code Repositories](/docs/foundry/code-repositories/overview/) \[1] \[2] |Code Repositories是一个基于网络的代码创作环境，支持版本控制和协作。|在Ontology中创建数据管道或编写函数。 |
|[Dataset Preview](/docs/foundry/dataset-preview/overview/) |Dataset Preview显示数据集的内容和历史。 |浏览数据集，了解其历史和其他元数据。 |
|[Data Health](/docs/foundry/data-health/overview/) |Data Health让您定义健康检查以确保数据集的高质量。 |添加或监控数据集的健康检查。 |
|[Data Connection](/docs/foundry/data-connection/overview/) |Data Connection允许您连接到数据源并将数据同步到Palantir平台。 |连接到组织数据源或将新数据集同步到Palantir平台。 |
|[HyperAuto (SDDI)](/docs/foundry/hyperauto/overview/) |HyperAuto在常见ERP系统之上生成端到端数据管道。 |从企业系统生成Ontology，而无需手动开发管道。 |

\[1] Code Workbook或Code Workspaces可能更适合某些数据科学工作流。[了解更多关于Code Workbook、Code Workspaces和Code Repositories的区别。](/docs/foundry/code-workbook/code-products-comparison/) <br>
\[2] 对与技术背景较少的用户，Pipeline Builder可能更适合。

## 模型集成

|应用程序  |描述  |用途  |
|---  |---  |---  |
|[Model Assets](/docs/foundry/integrate-models/integrate-overview/) | Model Assets支持将多种不同类型的模型集成到Palantir平台中。 |训练模型，并在Palantir平台中连接到外部托管的模型。 |
|[Modeling objectives](/docs/foundry/model-integration/objectives/) |一个建模目标允许组织利益相关者和模型开发人员协作和部署机器学习模型。 |提交模型；讨论建模目标，并将模型部署到生产环境中。 |

## Ontology

|应用程序  |描述  |用途  |
|---  |---  |---  |
|[Ontology Manager](/docs/foundry/ontology-manager/overview/) |Ontology Manager使您能够定义组织的Ontology。 |创建新的Object、链接和操作类型。 |
|[Object Views](/docs/foundry/object-views/overview/) |Object Views表示显示Object类型的规范方式。 |定义可以跨应用案例使用的用户界面。 |
|[Object Explorer](/docs/foundry/object-explorer/overview/) |Object Explorer允许您搜索和可视化您的Ontology。 |在Ontology中搜索和分析对象和链接。 |
|[Vertex](/docs/foundry/vertex/overview/) |Vertex使您能够探索对象关系并运行模拟。 |创建相关对象的系统图，并使用模型运行端到端模拟。 |
|[Automate](/docs/foundry/automate/overview/)  | Automate允许终端用户和应用程序搭建者查看Palantir Ontology中的数据何时发生变化。  |配置自动化以在满足特定条件时发送通知或提交操作。 |
|[Foundry Rules](/docs/foundry/foundry-rules/overview/)  |Foundry Rules使用户能够在平台中主动管理复杂的业务逻辑。 |为各种应用案例创建并应用规则到数据集、对象和时间序列。 |
|[Map](/docs/foundry/map/overview/) |Map提供强大的地理空间和时间分析与可视化能力。 |将平台中的数据集成到一个连贯的地理空间体验中。 |

## 应用程序搭建

|应用程序  |描述  |用途  |
|---  |---  |---  |
|[Workshop](/docs/foundry/workshop/overview/) \[1] |Workshop使终端用户能够创建互动和高质量的应用程序。 |使用Ontology中的数据在一个快速、点选界面中创建应用程序。|如果您的应用程序需要大量定制，Slate可能更合适。 |
|[Slate](/docs/foundry/slate/overview/) \[2] |Slate是一个可扩展的应用程序开发框架。 |使用HTML、CSS和JavaScript创建定制应用程序。 |对于低到中等复杂度的应用程序，Workshop更合适。 |
|[Carbon](/docs/foundry/carbon/overview/) |Carbon让您可以结合平台中的应用程序和其他资源，为终端用户创建精选工作空间。 |为终端用户提供结合多个应用程序或仪表盘的应用案例。 |

\[1] 如果您的应用程序需要大量定制，Slate可能更合适。 <br>
\[2] 对于低到中等复杂度的应用程序，Workshop更合适，并且通常在时间上维护成本较低。

## 分析

了解更多关于[平台中的分析应用程序和可用的分析类型](/docs/foundry/analytics/types-of-analysis/)。

|应用程序  |描述  |用途  |
|---  |---  |---  |
|[Contour](/docs/foundry/contour/overview/) \[1] |Contour在数据集上实现高规模、自上而下的分析。 |以点选方式分析表格数据。 |
|[Quiver](/docs/foundry/quiver/overview/) \[2] |Quiver实现对Object数据和时间序列的分析。 |以点选方式分析Ontology数据和时间序列。 |
|[Code Workbook](/docs/foundry/code-workbook/overview/) \[3] |Code Workbook是一个基于网络的代码分析环境。 |通过代码分析数据集，进行数据科学工作流或开发模型。 |
|[Code Workspaces](/docs/foundry/code-workspaces/overview/) \[3] |Code Workspaces将JupyterLab®和RStudio® Workbench第三方IDE引入Palantir。 |使用高质量的Palantir Ontology数据，通过首选工具提高生产力并加速数据科学和统计工作流。 |
|[Notepad](/docs/foundry/notepad/overview/) |Notepad允许创建时点文档以呈现数据供他人分享。 |展示分析工作流中的见解。 |
|[Fusion](/docs/foundry/fusion/overview/) |Fusion是Palantir平台的电子表格应用程序。 |将可编辑电子表格中的数据同步到数据集中。 |

\[1] 对于某些工作流，Quiver可能更合适。[了解更多](/docs/foundry/analytics/types-of-analysis/#point-and-click-analysis).<br>
\[2] 对于某些工作流，Contour可能更合适。[了解更多](/docs/foundry/analytics/types-of-analysis/#point-and-click-analysis).<br>
\[3] Code Repositories和Pipeline Builder推荐用于开发生产数据管道。了解更多关于[Pipeline Builder](/docs/foundry/pipeline-builder/overview/)和[Code Workbook、Code Workspaces和Code Repositories的区别](/docs/foundry/code-workbook/code-products-comparison/)。

---

## [入门] 认证

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/authentication/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-authentication.md`

# 认证

本页面提供有关如何登录 Palantir 平台的信息。在大多数情况下，您的注册管理员会将您组织现有的身份提供者与 Palantir 平台集成，以便您可以使用您在其他内部系统中使用的相同凭据登录。

或者，自 2024 年夏季起，Palantir 的自助服务无密码身份提供者可用于配置 AIP Now 和 AIP Bootcamps 的新注册。

## 您自己的身份提供者

Palantir 平台可以与您现有的身份提供者无缝集成，通过现有系统进行完整的端到端访问管理。有关如何配置身份提供者以用于 Palantir 平台的详细说明，请参阅[管理文档](/docs/foundry/authentication/overview/)。

## Palantir 自助服务用户目录

在某些情况下，您的注册可能会自动配置为内置的身份提供者。Palantir 的自助服务用户目录是**无密码**的，利用 FIDO2 密钥提供无与伦比的安全性和无缝的用户体验。

如果您使用 Palantir 自助服务用户目录注册了一个新账户，您将在注册后不久收到一封主题为“设置您的 Palantir 账户”的电子邮件。完成以下说明以设置您的账户后，您可以通过导航到 **认证 > Palantir 自助服务用户目录** 在控制面板中邀请其他用户加入您的注册。然后，选择 **管理用户**。

### 什么是密钥？

FIDO2（快速身份在线）密钥是一种旨在增强安全性和便利性的现代认证形式。密钥是一种无需使用密码即可登录账户的安全方式，消除了记住复杂密码的需要，这些密码可能很难记住且令人沮丧。使用密钥，您可以通过指纹、面部扫描、硬件词元或密码管理器登录。

### 密钥如何工作？

FIDO2 密钥是一种物理安全密钥或平台认证器，如生物识别设备或智能手机，可用于无密码认证。设备为每个服务或应用程序生成一对唯一的公钥和私钥。公钥注册在服务中，而私钥则安全地存储在设备上。

当您使用 FIDO2 密钥进行认证时，服务会向您的设备发送一个挑战。设备将使用私钥对挑战进行签名，并将签名的响应发送回服务。然后，服务使用公钥验证响应以确认您的身份。

密钥提供了几个好处：

* **强大的安全性**：公钥加密提供了高水平的安全性，由于私钥从未离开设备，它更不易受到攻击。
* **无密码认证**：FIDO2 密钥消除了密码的需要，使认证更方便，并减少钓鱼和其他与密码相关的攻击风险。
* **隐私**：每个服务生成的唯一密钥对确保您的认证信息不能用于跟踪您在不同服务中的活动。
* **易用性**：密钥提供了一个简单、用户友好的认证体验，只需要一个简单的操作，如插入安全密钥或使用生物识别设备如指纹或面部扫描。

### 设置和配置密钥

以下是如何使用 Palantir 内置无密码认证的说明。

要继续，您必须已经收到 Palantir 发送的标题为“设置您的 Palantir 账户”的电子邮件。然后，按照以下说明操作：

1. 在来自 Palantir 的电子邮件中选择 **注册** 选项以开始设置您的 Palantir 账户。

    <img alt="设置您的 Palantir 账户" src="../../foundry-docs/getting-started/media/setup-email.png" width="400">
2. 输入您的电子邮件地址和临时密码，然后选择 **下一步**。

    <img alt="注册步骤" src="../../foundry-docs/getting-started/media/sign-up-step.png" width="400">
3. 在 SMS 或电话验证之间进行选择以验证您的账户。

    <img alt="创建账户步骤" src="../../foundry-docs/getting-started/media/create-account-step.png" width="400">
4. 使用 6 位数的认证码验证您的电话号码。

    <img alt="验证电话号码步骤" src="../../foundry-docs/getting-started/media/verify-phone-step.png" width="400">
5. 如果您被邀请加入现有的注册，请同意条款和条件以继续。否则，跳至步骤 6。

    <img alt="同意条款步骤" src="../../foundry-docs/getting-started/media/tos-step.png" width="400">
6. 选择 **添加密钥**。
7. 选择一个保存密钥的目的地，然后按照屏幕上的说明操作。

   * 对于硬件词元，您可能需要选择 **使用其他设备**。
     * 然后，您需要插入您的硬件词元，输入其 PIN 和/或触摸词元上的指纹传感器。
   * 对于移动设备词元，您可能需要选择 **使用其他设备**，然后使用您的移动设备扫描二维码。
   * 为避免问题，请确保您正在使用[支持的浏览器](/docs/foundry/getting-started/supported-browsers/)。

    <img alt="创建密钥对话框" src="../../foundry-docs/getting-started/media/create-passkey-step.png" width="400">
8. 一旦您的密钥成功添加，您将看到以下屏幕：

    <img alt="成功步骤" src="../../foundry-docs/getting-started/media/success-step.png" width="400">

#### 使用密钥登录

1. 在 Palantir 登录页面，输入您的电子邮件地址并选择 **下一步**。
2. 选择 **使用密钥** 选项以使用您的密钥登录账户。
3. 按照屏幕上的密钥说明解锁您的设备并选择您的密钥。

#### 添加额外的密钥

我们建议您为您的账户添加多个密钥作为备份。每个账户最多可以添加四个密钥。

要向您的账户添加额外的密钥，请导航到 **设置 > 账户**。然后，找到 **认证**。您也可以直接访问 `<your-enrollment-URL>/workspace/settings/authentication`。

<img alt="认证设置" src="../../foundry-docs/getting-started/media/passkey-mgmt.png" width="700">

* 选择 **添加密钥** 选项。
  * 在添加额外的密钥之前，您可能会被要求重新认证。
* 选择一个保存密钥的目的地，然后按照屏幕上的说明操作。
  * 对于硬件词元，您可能需要选择 **使用其他设备**。然后，您需要插入您的硬件词元，输入其 PIN 和/或触摸词元上的指纹传感器。

#### 删除密钥

* 要删除已注册的密钥，请导航到 **设置 > 账户**。然后，找到 **认证** 或访问 `<your-enrollment-URL>/workspace/settings/authentication`。
* 使用要删除的密钥旁边的操作下拉菜单。
* 选择 **删除** 并 **确认** 您要删除密钥。一旦删除，您将无法再使用该密钥登录。

#### 重置账户

如果您无法访问任何密钥，请联系您的注册管理员以重置您的账户。为避免这种情况，我们建议您注册至少两个密钥，以防无法访问某一个密钥时高枕无忧。

### 密钥类型和最佳实践

#### 最佳实践

我们建议您为您的账户至少保留两个不同的密钥。例如，您可以将一个密钥存储在手机上，一个存储在 Chrome 配置文件中。此外，您还应配置多个[注册管理员](/docs/foundry/administration/enrollments-and-organizations-permissions/)以协助账户恢复作为备份。

#### 推荐的密钥类型

在 **Windows** 计算机上，我们推荐以下方法管理密钥：

* [在手机或 YubiKey 上创建并存储密钥 ↗](https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/?tabs=windows#create-a-passkey)
* [直接在 Google Chrome 中创建并存储密钥 ↗](https://blog.chromium.org/2022/12/introducing-passkeys-in-chrome.html)

在 **macOS** 设备上，您可以创建并存储同步到您的设备上的密钥，使用 iCloud。在 macOS 上，您可以：

* [确保您的 iCloud 密钥已启用并使用 iCloud 密钥 ↗](https://support.apple.com/en-us/109016)
* [直接在 iOS 上创建密钥 ↗](https://support.apple.com/guide/iphone/use-passkeys-to-sign-in-to-apps-and-websites-iphf538ea8d0/ios)
* [管理密钥 ↗](https://it-training.apple.com/tutorials/support/sup540)

---

## [入门] 使用 Chrome™ DevTools 进行调试

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/debug-using-devtools/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-debug-using-devtools.md`

# 使用 Chrome™ DevTools 进行调试

在本指南中，您将学习如何使用 Chrome™ 浏览器中的开发工具（DevTools）来帮助识别意外行为或收集必要的浏览器日志以提供给 Palantir 支持。

调试模糊错误的最重要工具之一是 [Chrome™ DevTools ↗](https://developer.Chrome.com/docs/devtools/)。它为调试问题提供了丰富的信息，并允许您查看网页背后发生的一些内部情况。可以将其视为打开汽车的引擎盖——您可以查看内部并了解实际发生的情况。

* [使用 Chrome™ DevTools](#use-Chrome™-devtools)
* [控制台标签](#console-tab)
* [网络标签](#network-tab)
* [在网络标签中查找追踪 ID](#finding-trace-ids-in-the-network-tab)
* [元素标签](#elements-tab)

***

## 使用 Chrome™ DevTools

您可以通过以下步骤访问控制台日志：

1. 右键单击您打开的网页上的某个元素。
2. 选择 **Inspect**。这将在网页侧边打开一个屏幕。
3. 在顶部，导航到 **Console** 标签，这是大多数错误会出现的地方。
4. 失败请求将显示为红色。找到页面上出错相关的红色请求，或支持团队指示您提供的特定请求。您可能需要在执行相关操作时打开网络窗口，以便错误消息出现。
5. 选择左侧的箭头以展开请求。通常这会包含额外的有用信息，如错误消息和 errorInstanceID。

目前重要的部分是顶部的工具栏。对于大多数故障排除，**Console** 和 **Network** 标签将包含相关错误信息，并对支持团队最有帮助。然而，**Elements** 标签也可能在识别问题时有用，因此我们也将覆盖它。

## 控制台标签

如下面的图片所示，可通过工具栏中的 **Console** 标签访问 Chrome™ 控制台，主要有两个用途。首先是供网页应用程序本身使用。网页应用程序可以在控制台中打印任何它想要的东西——调试信息、错误日志、信息消息等等。

第二个用途是用户可以运行代码片段并检查结果。然而，这种用法超出了本指南的范围。

当您遇到错误时，通常打开控制台并向上滚动历史记录，特别是查找错误（通常以红色突出显示）是很有用的。这些错误将有助于报告，并通常包含有关出错原因的更多信息。

例如，当我们加载 [使用 DevTools 进行调试的页面](/docs/foundry/getting-started/debug-using-devtools/)时，我们应该在控制台日志中找到以下代码段：

您可能会看到很多信息行，即上面的简单白色行，以及以红色显示的错误。值得注意的错误显示了一个 URL 的 GET 请求，后跟数字 404，即 HTTP 错误代码 "文件未找到"。如果我们查看控制台以获取有关错误的更多信息，这个错误将非常有用，包括文件名。在此示例中，引用了一个 `you-found-me.png`，该文件未找到。

在许多情况下，展开错误以获取其他信息也是有用的。您可以通过选择错误开头的小三角形来执行此操作：

要访问特定页面上的控制台日志：

1. 右键选择您打开的页面上的一个元素，然后选择 **Inspect**。这将在网页侧边打开一个屏幕。
2. 导航到页面顶部附近的 **Console** 标签。
3. 失败请求将显示为红色。找到页面上出错相关的红色请求。
4. 选择左侧的箭头以展开请求。通常这会包含更多信息，如错误消息和 errorInstanceID。
5. 如果您没有看到任何相关错误，请尝试在控制台日志打开的情况下重新触发导致失败的行为。

此操作可以为您的支持团队提供更多故障排除信息。您可以通过右键选择错误信息并选择 **Save as** 来获取这些日志。您可能需要将保存的文件从 `.log` 文件重命名为 TXT 文件以上传到平台。

有关更多信息，请参见 [Chrome™ DevTools 控制台概述文档 ↗](https://developer.chrome.com/docs/devtools/console/).

## 网络标签

当您在 Palantir 应用程序中选择一个按钮时，您的浏览器会向服务器发送一个请求，服务器处理后再发送一个响应。单个网页可能会发出许多请求，这些请求不会导致页面重新加载，但可能会更新您看到的数据或向服务器发送新数据。**Network** 标签让您可以检查您的浏览器发出的所有请求，以及检查收到的响应。

要访问特定页面上的网络日志：

1. 右键选择您打开的页面上的一个元素，然后选择 **Inspect**。这将在网页侧边打开一个屏幕。
2. 导航到页面顶部附近的 **Network** 标签。
3. 失败请求将显示为红色。找到页面上出错相关的红色请求。
4. 选择左侧的箭头以展开请求。通常这会包含更多信息，如错误消息和 errorInstanceID。
5. 如果您没有看到任何相关错误，请尝试在控制台日志打开的情况下重新触发导致失败的行为。

注意 `Status` 列。这包含了请求在响应中收到的 HTTP 状态代码，如本文件前面所讨论的。注意有一个 `404` 错误，以及许多以 `2` 开头的请求，这意味着请求成功。

以下是使用此视图获取更多错误信息的一些最佳实践。首先，查看侧边栏左上角的两个按钮：

红色的第一个图标表示网络标签当前正在记录。这意味着当发出新请求时，它将记录在下面的视图中。如果不可用，您应该切换**记录**。同样，如果您发现请求日志填充速度超过您可以检查的速度，您可以再次选择它以关闭记录。

第二个符号（带线圈的圆圈）可让您清除日志。这在您执行最小步骤以重现之前非常有用。此操作清除了所有当前记录请求的日志，以便您可以看到仅仅是那些新进来的请求。

使用此日志的最佳方式是：

1. 执行重现错误的最小步骤，但直到错误发生之前。
2. 清除日志。
3. 执行导致错误的最后一步。
4. 检查新请求，特别是查找任何 HTTP 错误代码。您可能希望将请求的截图附加到您的报告中。

如果您发现某个特定请求值得关注，可能是因为它有相关的 HTTP 错误代码，以下信息将非常有用以包含在错误报告中。以下是导航到主页时生成错误的请求示例：

注意它是红色的，表示错误，并且错误代码是500，这意味着内部服务器错误。这已经是有用的报告信息；我们可以附上一张错误的截图，并说它是 "500 - 内部服务器"。

首先要注意的是请求发送到的 URL。在这种情况下，`redirect?code=...` 是我们联系的 URL。这对于识别导致错误的服务非常有用。例如，如果 URL 包含 `foundry-metadata`，那么 foundry-metadata 服务就是导致问题的原因——这当然是有用的错误报告信息。

请求的 cURL 等效项也很有用。您可以通过右键选择请求本身并从菜单中选择 **Copy > Copy as cURL** 将其复制到您的报告中。

cURL 是一个命令行工具，让您可以从命令行执行请求。这按钮复制了请求的确切内容到剪贴板，并允许调试器在任何地方以任何方式运行 cURL 请求，从而可以检查请求以确定可能出错的地方。这在 4xx 错误中特别有用。如果有任何错误 ID，请注意它们。您可能希望将此副本保存为 TEXT 文件以发送给 Palantir 支持，但请注意：

* 出于安全原因，请从日志中删除任何现有的令牌，否则它们将被您的 Palantir 团队撤销。您可以通过搜索 "token" 和 "bearer" 并删除后续的字符串来检查文件是否包含令牌。
* 在共享之前编辑敏感信息。

报告中最后一个有用的元素是响应本身，您可以通过相同的复制菜单中的 **Copy response** 访问。

要访问特定页面上的 **Network** 标签：

1. 右键选择您打开的页面上的一个元素，然后选择 **Inspect**。这将在网页侧边打开一个屏幕。
2. 导航到页面顶部附近的 **Network** 标签。
3. 有时在您打开时，网络标签未填充。通过刷新页面或重新触发失败的行为来填充标签。
4. 网络标签中的第二列是 "Status"。选择 **Status** 直到按降序排序。这将把失败请求带到顶部，因为它们将有更高的状态代码。失败请求也将显示为红色。
5. 找到页面上可能与您失败相关的请求。选择请求以获取更多信息，如错误消息或 errorInstanceID。

## 在网络标签中查找追踪 ID

TraceID 是请求的唯一标识符，允许将浏览器中的进程与日志中存储的记录匹配。

要查找 traceID，请按照上一节中描述的方式打开网络标签。根据情况，不同请求可能值得调查；通常，红色（表示失败）的请求在浏览器中显示错误时很有用。

选择一个请求以查看其详细信息。

在 **Response Headers** 中找到 `x-b3-traceid`，在上图中以红色突出显示。
复制该值，在此示例中为 `255c17c75ae752a5`，并将其以文本形式与 Palantir 支持共享。

有关更多信息，请查看 [Chrome™ DevTools 检查网络活动文档 ↗](https://developer.chrome.com/docs/devtools/network/).

## 元素标签

元素标签显示您正在查看页面的 "DOM"（文档对象模型）。这构成了您在页面上看到的所有视觉内容，以其底层 HTML 形式表示：

可以使用 Inspect Element 工具来探索这棵 HTML 数据树。有两种使用方式。首先，我们可以使用指针版本，通过 DevTools 工具栏中的这个按钮访问：

选择此按钮后，指针变为 "活动"，让我们可以选择网页上的 **Elements** 并在 DOM 中查看它们。

第二种使用方式是右键选择页面上的某个内容，然后从下拉菜单中选择 **Inspect**。这与使用指针版本具有相同的效果。

如有必要，这可以为您的支持团队提供额外的信息以帮助故障排除。

有关更多信息，请查看 [Chrome™ DevTools 元素文档 ↗](https://developer.chrome.com/docs/devtools/dom/).

***

Chrome™ 是 Google Inc. 的商标。

---

## [入门] 交付应用案例

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/delivering-a-use-case/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-delivering-a-use-case.md`

# 交付应用案例

要使用Palantir平台为您的组织创造价值，您需要跨平台工作，以搭建支持运营决策过程的工具。一个**应用案例**是由专门团队为支持特定决策过程而进行的有时间限制的努力。应用案例是为一组用户在平台上交付新功能的核心。

## 应用案例示例

Palantir平台中的应用案例可以涉及广泛的不同活动和工作流程，例如：

* 生成、调查和解决与重要运营过程相关的警报。
* 优化您设施网络中的库存，以提高弹性并减轻供应链不确定性。
* 帮助您做出有关如何优化销售人员分配到您服务的不同区域的决策。

应用案例需要在平台中采取结构化和深思熟虑的方法进行搭建，同时需要理解一些新概念和术语。您可以在[应用案例生命周期](/docs/foundry/use-case-life-cycle/overview/)部分找到我们解决方案设计方法的所有细节以及案例研究和参考架构。

## 数据驱动的思维

想象一个数据科学家、质量分析师、装配线工人和高管将数据作为日常交流语言的世界。Palantir通过以下方式将数据转化为交流语言：

* 维护数据沿袭和归属，以便人们可以信任他们发现和学习的内容。
* 无论技术能力或经验如何，满足用户的需求，使每个人都能将数据融入他们的日常工作。

这种协作愿景是Palantir平台背后的驱动力。

Palantir平台旨在创建组织内的**数据驱动循环**，与您的同事和合作者同步：使用数据做出决策，记录所做的决策，然后使用数据评估决策随时间的影响。与依赖电子邮件发送的电子表格和静态分析不同，您和您的同事可以实时直接在数据上协作。

在Palantir平台上实现项目成功需要创造力和深思熟虑。对于任何给定的分析问题、组织工作流程或运营需求，往往会有多种解决方案。要选择正确的路径，您需要平衡三个因素：期望的结果、可用的数据和平台工具。

## 结果

分解项目时，考虑结果比考虑达到结果的方法更为重要。例如，与其从需要搭建销售仪表盘开始，不如尝试了解您的工作可能启用的决策和结果。例如，结果是关于按时做出有关时间和资源分配到不同销售区域的决策，还是其他？

这种理解水平可能在项目初期需要更多工作，特别是如果您在为他人搭建工具、报告或分析时。考虑一种面向结果的框架有助于您朝着现实目标前进。

灵活性和适应性可以帮助确保Palantir项目的成功。明确、面向结果的目标使得将项目分解为小的、合乎逻辑的步骤更加容易。这种问题分解是一项重要技能，因为项目通常需要多个数据源和多个平台工具协同工作。

## 数据

找出支持项目的正确数据可能是一项艰巨任务。但是，如果您有一个面向结果的框架并将项目分解为较小的步骤，则更容易从结果反向工作并识别必要的数据。

如果您的组织已经使用Palantir平台一段时间，您需要的数据可能已经在平台中。尝试探索[数据目录](/docs/foundry/projects/data-catalog/)中策划的数据集或[Object Explorer](/docs/foundry/object-explorer/overview/)中的Objects和链接。从我们的结果示例中，我们可能会识别出我们需要有关销售团队、销售区域、产品和个人销售的数据。这些Object中的每一个都应在Ontology中有一个主要表示。

如果您无法为所需数据类型识别关键数据集，请联系您的平台管理员。有时，需要扩展Ontology以包含新的组织Object或为已经存在的Object添加新属性。如我们将稍后讨论的，您可以使用数据集成层中的工具连接外部数据源并将新数据引入Palantir平台。

## 工具

每个应用程序都被设计为整个平台的一部分。熟悉平台中的不同功能以及哪个工具最适合特定任务需要时间。

一旦您了解了项目的结果和必要的数据，便更容易将每个步骤映射到特定工具。例如，假设在项目中您识别到一个子项目是为每个区域生成新的销售指标。这个子项目会创建几个附加步骤：

* 确定关键相关指标
* 获取数据
* 开发逻辑以变换数据
* 开发逻辑将数据聚合到指标中
* 为销售团队展示数据以供使用

这些步骤中的每一个都将映射到平台中的不同工具，并且随着项目的成熟，正确的工具可能会有所不同。例如，您可以通过**Contour**开始原型变换和指标，这是一款用于点击分析和数据变换的应用程序。Contour可以轻松理解数据的形态并生成图表或指标。您可以将这些指标添加到**仪表盘**中，并为销售团队创建一个快速原型以提供反馈。这可能是该项目的一个很好的终点：一些精心制作的仪表盘提供新的见解以推动销售资源分配过程的决策。

对于较大的项目或专注于生产使用的项目，您可以将逻辑转换为**Code Repositories**中的管道。在那里，您可以与其他技术用户协作并使用强大的平台工具定期更新数据。为了创建更为定制的用户体验，您可以设置**Object Views**或在**Workshop**或**Slate**中搭建自定义应用程序，以使销售团队不仅可以在仪表盘中查看数据，还可以将他们的决策反馈到系统中。

虽然平台中的许多项目不需要这种复杂性，但理解如何框架和分解项目将帮助您识别成功所需的数据和工具是有益的。

## 下一步

最后，请查看[按用户角色的下一步](/docs/foundry/getting-started/next-steps-by-role/)，以了解您应该从哪里开始。

---

## [入门] file-support-ticket

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/file-support-ticket/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-file-support-ticket.md`

# 概述

如果在查看[可用资源](/docs/foundry/getting-started/overview/#2-search-the-issues-application-and-stack-overflow)后仍未能找到适当的解决方案，那么是时候提交支持工单了。

提交工单可确保您的问题或请求得到跟踪，适当优先处理，并在必要时提升。

为了使支持过程更加高效，请按照以下步骤收集有价值的信息以提交支持工单：

<!-- TOC -->

* [1. 创建示例](#1-创建示例)
* [2. 共享相关资产](#2-共享相关资产)
* [3. 报告问题](#3-报告问题)

<!-- /TOC -->

在按照下面的说明操作之前，请确保您已使用[获取帮助页面](/docs/foundry/getting-started/support-overview/)上提供的步骤诊断了您的问题，查看了[使用Chrome™ DevTools进行调试](/docs/foundry/getting-started/debug-using-devtools/)和[HTTP错误代码](/docs/foundry/getting-started/http-error-codes/)的指南。

## 1. 创建示例

在询问您遇到的问题时，提供可以用于重现问题的清晰步骤将确保快速解决。这些步骤应该是：

* **简洁：** 使用尽可能少的步骤，同时仍能产生问题。
* **完整：** 提供重现问题所需的所有部分。
* **可验证：** 测试您即将提供的工作流程，确保它能够重现问题。

一个简洁、完整且可验证的示例可以帮助我们在您的环境之外重现问题，从而更容易找到问题的根本原因并快速解决问题。有关简洁、完整且可验证示例的更多信息，请参见Stack Overflow [简洁、完整且可验证的示例 ↗](https://stackoverflow.com/help/mcve)。

在Palantir的上下文中，这样的示例可以是重现行为的一系列步骤或重现问题的最小资源。通常，包含预期行为与观察到的行为作为示例的一部分是有用的。

### 提示

以下是一些创建简洁、完整且可验证示例的提示：

* 首先确定重现问题所需的步骤。这些步骤越具体和详细，其他人重现问题就越容易。
* 确保您的示例是简洁的，即仅包含重现问题所需的最少信息。这将有助于缩小问题的潜在原因并更容易修复。
* 包含您提供步骤的预期结果以及实际结果。这将帮助他人理解问题并确定他们是否遇到相同的问题。
* 确保您的示例是完整的，即包含重现问题所需的所有信息。如果遗漏了任何重要细节，其他人将难以重现问题并帮助您解决问题。
* 最后，确保您的示例是可验证的，即他人可以使用您提供的信息轻松重现问题。如果您的示例不可验证，他人将难以帮助您解决问题。

### 示例

以下是一个已经解决的简洁、完整且可验证问题的历史示例。

当时重现问题的步骤：

1. 打开代码库应用程序。
2. 使用侧边栏添加Graphframes库。
3. 在代码库上运行检查。

预期行为：该库应添加到代码库中且无任何错误。

实际问题行为：显示错误信息，内容为 "o257.loadClass.: java.lang.ClassNotFoundException:<Class>"

附加信息：

* 这是我的配置文件中的其他包：Python 3.6.\*，等。
* 我已经尝试过做x、y和z。
* 最近没有对该代码库进行任何更改，除了添加此包。
* 这似乎影响了使用此包的用户。

此示例仅包含重现问题所需的最少步骤，并且不需要任何专有数据。该示例被认为是完整的，因为它包含所有必要的信息，如预期和实际行为，以及已经进行的故障排除等上下文信息。它是可验证的，因为可以使用相同的步骤重现错误信息。通过提供这些信息，支持团队将能够快速重现问题并着手解决。

如果您对该问题的解决方案感兴趣，请[查看需要同时包含Conda包和jar的包](/docs/foundry/code-workbook/environment-troubleshooting/#packages-which-require-both-a-conda-package-and-a-jar)。

## 2. 共享相关资产

在文本中提供可验证的示例后，为支持团队编译以下附加资产：

* 包括您在第1步中进行的调查结果。
* 提供任何构建错误或显示的错误消息的全文。
* 复制并粘贴任何errorID/errorInstanceID的文本，以便我们进行后台审查。
* 在可能和适当的情况下，与Palantir支持团队共享所有相关资源。
  * 相关资源（Slate仪表盘、分析、代码库）。
  * 资源的基础数据集。
  * 资源依赖的任何上游数据集。

## 3. 报告问题

要在指定应用程序中报告问题，请导航到**帮助与支持 > 报告问题**并[按照向导操作](/docs/foundry/getting-started/issues/)。

作为替代方法，您也可以在[Palantir开发者论坛 ↗](https://community.palantir.com/)中请求其他用户的支持。

您还可以在[Stack overflow公共论坛 ↗](https://stackoverflow.com/questions/tagged/palantir-foundry)中提问。该网站不属于Palantir，回复通常来自非Palantir代表的用户。此论坛仅用于编程（包括无代码工具）和代码相关的问题。

在公共论坛（如Palantir开发者论坛或Stack Overflow）上发帖时，请记得删除所有敏感数据。

***

Chrome™是Google Inc.的商标。

[1]: 注意：AIP功能的可用性可能会有所变化，并且可能因客户而异。

---

## [入门] 了解 HTTP 错误代码

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/http-error-codes/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-http-error-codes.md`

# 了解 HTTP 错误代码

本指南旨在提供有关如何应对在与网页前端交互时遇到的HTTP错误代码的基本信息。虽然许多技术通常适用于任何网页界面，但我们将在使用Palantir平台的背景下描述它们。

<!-- TOC -->

* [什么是HTTP错误代码？](#什么是HTTP错误代码)
* [客户端错误](#客户端错误)
  * [400 - 错误请求](#400---错误请求)
  * [401 - 未授权](#401---未授权)
  * [403 - 禁止访问](#403---禁止访问)
  * [404 - 未找到](#404---未找到)
* [服务器错误代码](#服务器错误代码)
  * [500 - 服务器内部错误](#500---服务器内部错误)
  * [502 - 错误网关](#502---错误网关)
  * [503 - 服务不可用](#503---服务不可用)
  * [504 - 网关超时](#504---网关超时)

<!-- /TOC -->

***

## 什么是HTTP错误代码？

当您尝试打开一个网页时，您的浏览器会向服务器发送一系列请求以获取页面内容。目的是服务器接收您的请求，检查它们以确定应该提供什么内容，然后发送包含正确内容的响应。然后您的浏览器将内容拼凑起来显示页面。

本指南稍后将深入探讨请求的概念，但这里我们专注于响应。服务器返回的每个响应总是包含一个状态代码。状态代码表示服务器给您的响应的状态。它由一个三位数表示，具有相应的含义（通常由互联网工程任务组定义）。当页面加载失败时，您可能会看到这些状态代码 - 像"404"这样的术语可能对您很熟悉。在这里，我们将深入了解每个代码的含义，以及如何使用这些信息找到一些简单的修复方法或更好的错误报告。

在响应中发送的三位数的第一位表示状态类别。本指南的重要类别是：

* 2xx：如果代码以2开头，则表示请求成功。完整代码通常是200，表示一般的成功请求和响应。
* 4xx：如果代码以4开头，则表示请求由于客户端错误而未成功。客户端指的是发出请求的实体，通常是您使用的浏览器或网页。我们将在下面看到一些这些代码的示例。
* 5xx：如果代码以5开头，则表示请求由于服务器错误而未成功。这通常意味着您的请求格式正确且制作良好，但当服务器检查它并尝试确定要发送回的响应时，出了点问题。我们将在下面看到一些这些代码的示例。

现在让我们深入了解一些实际的代码。请注意，这个列表并不详尽，如果您遇到此处未列出的数字，可以参考[HTTP状态代码完整列表↗](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)。

***

## 客户端错误

### 400 - 错误请求

此错误消息表示您发送到服务器的请求内部有问题。Palantir开发人员努力确保很少遇到此错误代码，因为最常见的原因是请求语法错误，通常在底层代码中定义。然而，一个常见的"错误请求"错误原因是请求过大，导致请求中包含的数据太多，服务器无法处理。

[返回顶部](#了解-http-错误代码)

***

### 401 - 未授权

您更常见到的是"403 - 禁止访问"，而不是"401 - 未授权"，但它们在语义上非常相似。通常，401错误表示您的请求格式正确，但您未被授权进行该请求。与403不同的是，它通常用于您尝试进行授权但授权失败的情况，或者您已被标记为"被禁"。

[返回顶部](#了解-http-错误代码)

***

### 403 - 禁止访问

禁止访问错误表示您进行了一个不被允许的请求。如果存在一个访问控制列表（ACL）规则，说明您不被允许访问您尝试访问的资源，您可能会在Palantir平台中遇到此错误。例如，某些数据您的用户不被允许查看，但这也适用于服务。例如，如果您的用户不被允许访问数据沿袭应用程序，当您尝试这样做时，您可能会看到"403 - 禁止访问"。

[返回顶部](#了解-http-错误代码)

***

### 404 - 未找到

此错误表示您请求的资源不存在。例如，如果某个特定资产被移除，访问该资产会显示为"404 - 未找到"，因为您请求的资源不存在。

***

## 服务器错误代码

### 500 - 服务器内部错误

此错误表示服务器接收到请求并需要执行内部操作以生成响应。然而，在此过程中服务器内部发生了错误。

例如，假设您的服务器任务是接收包含两个数字的请求，然后将第一个数字除以第二个数字。在此示例中，如果您向服务器发送"8"和"2"的请求，它将返回状态代码200（成功），响应将包含答案"4"。但是，如果您发送"5"和"0"，您可能会看到"500 - 服务器内部错误"，因为当服务器尝试计算5/0时，它在内部引发了错误。在Palantir平台的上下文中，这意味着您需要查看相关服务的内部，以确定内部发生了什么错误。这通常意味着识别服务并查找相关日志，我们将在本指南后面进行介绍。

[返回顶部](#了解-http-错误代码)

***

### 502 - 错误网关

"网关"一词指的是服务之间连接的背后存在"间接"的元素。假设您尝试打开`https://foundry.link/workspace/magic-app`时遇到此错误。实际上发生的是您的请求到达一个服务器（"网关"服务器），然后网关服务器将您的请求传递出去。值得注意的是，magic-app可能运行在与网关不同的服务器上，因此网关必须向该服务器（称为"上游服务器"）请求响应，并打算将该响应返回给您。此错误表示上游服务器返回了无效响应。

[返回顶部](#了解-http-错误代码)

***

### 503 - 服务不可用

此错误表示服务存在，因为否则将会收到404错误。然而，服务无法处理您的请求，最常见的原因是服务已停机或过载。例如，如果Contour有太多请求，根本无法处理更多请求，您可能会收到"503 - 服务不可用"。这可能是由于计算资源不足或内部错误，例如内存泄漏。

[返回顶部](#了解-http-错误代码)

***

### 504 - 网关超时

此错误类似于"502 - 错误网关"，不同之处在于网关服务器发出了正确的请求，但未从上游服务器及时收到响应。这可能由于各种原因，包括网络连接问题、服务器停机或服务器过载。当发生504错误时，通常表示您尝试访问的网站或网络应用程序暂时不可用。通常这不是您自己的设备或互联网连接的问题。

[返回顶部](#了解-http-错误代码)

---

## [入门] 入门概念

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/introductory-concepts/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-introductory-concepts.md`

# 入门概念

在开始使用 Palantir 平台时，可以将平台中的数据分为两个部分：*数据层*和*对象层*。

## 数据层

<img alt="数据层" src="../../foundry-docs/getting-started/media/Datasets.svg" width="400">

在数据层中，数据存储在 **数据集** 中，通常表示类似于电子表格中的表格数据，但支持任何规模的数据。数据集通常来自同步到平台的组织数据源，但您也可以通过上传批准或概念性数据创建自己的数据集。

Palantir 平台中的每个数据集都维护其生成方式的记录，以便数据的来源始终得到保留和访问。这个概念被称为 **数据沿袭**。

* Palantir 记录了哪些 **输入数据集** 用于生成哪些 **输出数据集**。这样您就始终可以知道一条数据的来源，并了解数据的使用方式。
* Palantir 跟踪生成每个输出数据集所应用的 **逻辑**。例如，输入数据集可能被 *筛选* 以生成较小的输出数据集；该筛选逻辑在平台中被保留并可见。在平台中有多种编写逻辑的方式，从代码库到点击工具。

您可以使用 Palantir 的众多 **应用** 之一与数据进行交互。当您使用应用时，无论是数据集、代码还是分析，您所生成的任何内容都会作为 **资源** 存储在平台中。资源被组织到 **项目** 中，项目充当分组和组织相关工作的权限边界。我们将在接下来的章节中介绍如何访问和使用项目的详细信息。

## 对象层 (Ontology)

<img alt="对象层" src="../../foundry-docs/getting-started/media/Objects.svg" width="400">

在对象层或 Ontology 中，数据存储在 **对象** 和 **链接** 中。对象表示现实世界的概念，如飞机、车辆或客户，而链接表示对象之间的关系。对象层将存储在表格数据集中的数据（数据的行和列）转换为组织中的任何人都能理解的一系列概念。

除了帮助数据更易于理解之外，将数据从数据集转换为对象和链接还解锁了一组广泛的工具来与对象交互。您可以定义 **操作** 来描述组织中的人员如何更改对象。这使您能够搭建 **应用**，以从对象中访问数据并将用户决策捕获回系统中。

对象、链接和操作的定义共同组成了所谓的 Ontology，即组织的数字表示。开发和使用 Ontology 将数据转换为运营成果是从 Palantir 平台中获取价值的关键部分。

## 下一步

了解数据层和对象层及其差异后，您已准备好学习如何[在平台中熟悉环境](/docs/foundry/getting-started/orientation-and-nav/)。

---

## [入门] 问题应用程序

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/issues/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-issues.md`

# 问题应用程序

问题应用程序是一个支持系统，使用户能够在Palantir平台内部获得帮助。

使用问题应用程序，您可以：

* 提出有关应用程序或平台本身的问题。
* 透明地分配和解决问题、请求和问题。
* 报告平台内任何地方的资源问题，并查看哪些资源存在未解决的问题。
* 请求在平台内集成更多数据。

## 访问问题应用程序

从平台主页：

1. 在左侧导航栏中，选择位于**平台应用程序**部分右侧的**查看全部**。
2. 从**支持**下选择**问题**。

<img src="./media/issues-access.png" alt="从左侧导航栏访问问题应用程序" width="250">

## 搜索问题

从问题主页，您可以筛选和搜索特定问题，以缩小感兴趣的问题范围。默认情况下，您将看到**打开**问题概览页面。您还可以选择**已关闭**或**全部**以查看相应的视图。

1. 侧边栏筛选：左侧的侧边栏提供按以下选项进行筛选的选项：

   * 优先级
   * 指派人
   * 创建者
   * 提及
   * 标签
   * 截止日期
   * 报告日期
   * 最后更新日期

2. 搜索问题：此搜索栏允许您在所有用户输入字段中搜索，包括**标题**和**评论**。

3. 选择筛选器：选择筛选器选项允许您以与您相关的问题进行筛选（例如，指派给您的问题，由您报告的问题，或提及您的问题）。在问题应用程序中，有多种方式对显示的问题进行排序，包括：
   * 最佳匹配
   * 最近更新（默认）
   * 最近更新最少
   * 最近创建
   * 最早创建
   * 最高优先级
   * 最低优先级
   * 最早截止日期
   * 最晚截止日期

## 报告问题

要报告问题，请在工作区侧边栏中找到**帮助和支持**部分，并选择**报告问题**。

从右侧弹出的侧边栏中，您可以在**您的问题和问题**下查看您现有的问题，或选择**报告问题**以报告新问题。根据您注册的配置，创建问题时，您将经历两种问题提交流程之一。

一旦您的问题创建完成，您将返回到问题概览页面，其中列出了最近的问题，并将由相关的指派人进行审核。选择它进入问题特定页面并添加评论以提供进一步更新，或编辑其状态、优先级、截止日期、指派人、查询类型、（相关）应用程序或标签。否则，如果已达成解决方案，请选择**关闭问题**。

<img src="./media/issues-new-issue.png" alt="在报告问题中详细提示" width="800">

<img src="./media/issues-open-issue.png" alt="在报告问题中详细提示" width="800">

### 默认流程

1. 选择合适的帮助类别。

<img src="./media/issues-file-1.png" alt="提交问题" width="800">

2. 在根据选择的帮助类别要求进一步说明时，从提供的选项中选择，然后选择**下一步**。

3. 选择要共享的详细信息（例如，文件或Object，或相关应用程序），并考虑根据您的选择建议的阅读材料是否有帮助。如果您仍希望继续提交问题，请选择**下一步**。

4. 提供所有可用详细信息，包括**标题**、**描述**和任何其他详细信息，例如**优先级**、**指派人**、**关注者**、**标签**。然后选择**创建问题**。

<img src="./media/issues-advanced-details.png" alt="在报告问题中详细提示" width="800">

* **优先级：** 选择问题优先级，让支持团队知道问题的紧急程度。
* **指派人：** 选择应负责解决问题的个人。如果可能，添加可能能够协助解决问题的具体个人。请注意，问题应用程序可能会自动建议指派人。您可以取消选择自动建议的指派人，但通常不鼓励这样做，因为这些指派是根据Palantir平台管理员配置的规则进行的。
* **关注者：** 选择可能受益于问题解决意识的个人。请注意，关注者将订阅关于问题的所有更新。请注意，问题应用程序也可能会自动添加关注者；这些关注者是根据Palantir平台管理员配置的规则进行的。
* **标签：** 选择适用于您问题的标签。添加准确的标签将有助于支持团队了解您的问题、影响对象和人员以及如何最好地提供解决方案。问题应用程序也可能会自动添加标签；这些标签是根据Palantir平台管理员配置的规则添加的。某些标签可能会路由到特定支持团队，这些指派将在问题提交后自动应用。

`功能请求`类型的问题没有关联的文件或文件夹，因此`报告的文件位置`将不用于匹配任何关联的问题规则。

### 简化流程

1. 选择最能准确反映您需求的支持类型。

<img src="./media/simplified_issues_filing_flow_types.png" alt="选择支持类型。" width="800">

2. 提供尽可能多的信息，包括**标题**、**描述**、**优先级**以及任何其他详细信息，例如**关联资源**或**附件**（如适用）。然后选择**创建问题**。

<img src="./media/simplified_issues_filing_flow_details.png" alt="添加其他详细信息。" width="800">

与默认流程不同，指派人只能在问题创建后修改，除非选择了`其他`支持类型，在这种情况下，创建者负责选择合适的用户或组来解决他们的问题。

## 问题权限

问题通常对您的组织中的其他用户可访问。但是，如果问题与数据集或资源相关，则可以通过数据集或资源所在项目的[角色](/docs/foundry/security/projects-and-roles/#roles)来控制访问。您可以根据用户在数据集或资源上的文件系统权限控制用户是否可以查看问题。

**注意：** 在数据集或资源上创建问题不会授予其他用户访问该数据集或资源的权限。

### 跨组织协作

问题的访问受其关联的组织限制。默认情况下，所有问题都与创建者的组织关联。当将问题指派给该组织之外的用户或组时，更新问题的用户能够将与指派人关联的组织添加到问题中。指派人只有在问题与他们所属的组织相关联时才能查看问题（例如，他们的组织或他们被授予来宾成员资格的组织）。在重新指派问题时也是如此。

将问题指派给组时，没有严格的保证指派组的任何个人用户都能够查看问题。这是因为指派组的个别成员可能无法访问与问题关联的任何组织。

将组与组织关联并不会授予该组的所有成员访问该组织的权限。这只能通过授予组织的来宾成员资格来完成。将组指派给问题时，您应调查组成员的权限，以确认需要将哪些组织（如果有）添加到问题中，以确保成员有权响应问题。

---

## [入门] 客户端端点网络要求

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/network-requirements/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-network-requirements.md`

# 客户端端点网络要求

由于主要的Foundry前端是一个Web应用程序，建议用户使用[支持的浏览器](/docs/foundry/getting-started/supported-browsers/)以获得最佳操作效果。然而，在少数情况下，即使使用支持的浏览器，网络设置异常的用户可能会遇到问题。为了帮助调试，本页面记录了Foundry对客户端端点网络设置的一些假设。

## WebSocket支持

许多平台内的应用程序使用[WebSockets ↗](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)进行客户端与服务器之间的通信，并且Foundry假设WebSocket连接是可能的。某些代理服务器需要特殊配置或软件升级以支持WebSocket连接。如果用户通过不支持WebSockets的代理连接到Foundry，平台的大部分功能可能会变得不可用。

## HTTP/2支持

HTTP/2支持对Foundry平台的无缝性能至关重要，因为它有助于处理从Foundry应用程序到后端的大量并发请求。请注意，代理服务器可能会将HTTP/2连接降级为HTTP/1.1，这可能使Foundry应用程序变得缓慢，以至于妨碍使用。如果您在使用Foundry时遇到缓慢问题，并且您的连接通过代理连接到Foundry，您应该调查代理是否在降级连接的可能性。

---

## [入门] 根据用户角色的下一步

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/next-steps-by-role/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-next-steps-by-role.md`

# 根据用户角色的下一步

现在您已经熟悉了Palantir平台并了解其核心概念，您可以探索最适合您角色的平台功能。

在Palantir平台中，角色之间的界限可能会发生变化，一些责任和工作流程可能无法完美地融入单一角色。您可能会执行不同的角色；如果您的组织刚刚开始使用Palantir，或者您正在一个小型实施团队中工作，您可能会在日常工作中使用平台的许多部分。

考虑到这一点，以下角色通常在大多数使用Palantir的组织中采用。下面，我们讨论这些高级角色以及每种类型的用户如何起始：

* [数据工程师](#data-engineer)
* [应用构建者](#application-builder)
* [分析师](#analyst)
* [数据科学家](#data-scientist)
* [平台管理员](#platform-administrator)
* [数据治理](#data-governance)

或者，您可以通过查看[应用参考](/docs/foundry/getting-started/application-reference/)来探索Palantir平台，该参考提供了主要平台应用的高级概述。

## 数据工程师

Palantir的数据集成层为平台中发生的所有其他工作提供了基础。通过搭建和维护数据管道，数据工程师生成高质量、相关且经常更新的数据集，以满足组织的需求。多种工具可用于随着时间的推移维护数据管道的持久性，包括程序化健康检查和对底层计算的透明性。

数据工程师使用的主要工具包括用于编写数据管道的[**Pipeline Builder**](/docs/foundry/pipeline-builder/overview/)和[**Code Repositories**](/docs/foundry/code-repositories/overview/)，以及用于端到端可视化的[**Data Lineage**](/docs/foundry/data-lineage/overview/)。数据工程师需要熟悉数据管道的概念，并了解在平台中什么样的管道是高质量的。

[了解更多关于数据管道的信息。](/docs/foundry/data-integration/data-pipeline/)

## 应用构建者

Palantir的Ontology和应用构建能力使您能够快速为终端用户创建定制的高质量应用。这些终端用户通常是组织中的操作人员，可以通过数据做出更明智的决策。不仅仅是向用户展示数据，您还可以使用自定义应用通过Ontology中配置的操作类型来捕捉用户信息。

应用构建者需要熟悉Palantir的[**Ontology**](/docs/foundry/ontology/overview/)，通常这是应用构建者与数据工程师合作以建立工作流开发数据基础的层。构建者可以在[Ontology Manager](/docs/foundry/ontology-manager/overview/)中创建和维护他们组织的Ontology，并通过[Object Explorer](/docs/foundry/object-explorer/overview/)和[Object Views](/docs/foundry/object-views/overview/)探索对象和相关工作流。应用构建者可以通过[Automate](/docs/foundry/automate/overview/)创建由Ontology更改触发的警报。

为了创建和交付应用，构建者可以使用[**Workshop**](/docs/foundry/workshop/overview/)，这是Palantir的一款用于在Ontology之上进行点选应用构建的产品。为了使用代码进行开发，应用构建者可以编写[**Functions**](/docs/foundry/functions/overview/)来定义跨应用使用的业务逻辑，或者在[**Slate**](/docs/foundry/slate/overview/)中创建应用，这是Palantir用于使用HTML、CSS和JavaScript进行应用开发的框架。

[了解更多关于应用构建的信息。](/docs/foundry/app-building/overview/)

## 数据科学家

Palantir平台支持使用代码分析数据以及开发、评估和部署机器学习模型。这一功能基于数据集成层的严格性，在数据集上为模型提供沿袭和可重现性。结果是一个环境，分析和机器学习由高质量数据加速，并且建模项目的时间价值快速。

在Palantir平台中，数据科学家经常使用[**Code Workbook**](/docs/foundry/code-workbook/overview/)，这是一款用于启用基于代码的分析和开发机器学习模型的应用。Code Workbook允许您编写Python、R和SQL代码，以访问、规范化和分析由数据工程师准备的高质量数据集。然后，可以将所得分析和模型集成到Ontology中，以实现通过Palantir的应用构建框架直接向终端用户部署模型的能力。

作为替代，数据科学家可以在他们首选的第三方IDE中使用[Code Workspaces](/docs/foundry/code-workspaces/overview/)。Code Workspaces容器与Palantir生态系统的其他部分原生集成，将JupyterLab®和RStudio® Workbench IDE与Palantir平台的安全性、分支和资源管理优势相结合。

了解更多关于[模型集成](/docs/foundry/model-integration/overview/)和[基于代码的分析](/docs/foundry/analytics/types-of-analysis/#code-based-analysis)。

## 分析师

由于Palantir可以被用于搭建一个安全且高质量的数据基础，分析师可以快速找到和探索与他们需要回答的问题相关的数据。丰富的工具集可用于分析各种格式的数据——表格、关系、时间、地理空间等等。一旦您的分析产生了洞察，您可以通过创建[仪表盘](/docs/foundry/analytics/dashboards/)使其可重复，或使用[报告](/docs/foundry/analytics/reporting/)工具展示您的发现。

分析师通常使用[**Contour**](/docs/foundry/contour/overview/)在平台中探索数据集并进行大规模开放式分析，并使用[**Quiver**](/docs/foundry/quiver/overview/)分析Ontology中的数据及相关时间序列。这两个应用都支持将临时分析转换为仪表盘，并支持将发现嵌入到[**Notepad**](/docs/foundry/notepad/overview/)文档中以便与同事分享结果。

[了解更多关于分析的信息。](/docs/foundry/analytics/overview/)

## 平台管理员

平台管理员可以使用Palantir专用的管理工具配置平台，管理和了解其使用情况，并确保组织的数据被安全管理。

平台管理员通常设置[身份验证](/docs/foundry/authentication/overview/)以连接到组织的身份提供商，然后设置[**数据连接**](/docs/foundry/data-connection/overview/)以使数据流入平台。随着平台使用的成熟，管理员可以使用[**资源管理**](/docs/foundry/resource-management/overview/)管理资源消耗并确保数据被适当保护。

[了解更多关于平台管理的信息。](/docs/foundry/administration/overview/)

## 数据治理

Palantir为数据治理负责人提供了最佳的工具，以确保数据的安全性和透明性。这些工具提供了关于数据在Palantir平台中被变换和用于面向用户的应用时如何保护的保证，同时保留了您内省和验证谁可以访问哪些信息的能力。

数据治理角色的用户应该学习平台中广泛的数据安全工作流，从[保护数据基础](/docs/foundry/security/securing-a-data-foundation/)到[保护敏感数据](/docs/foundry/security/protecting-sensitive-data/)。这些功能建立在Palantir独特的数据安全概念之上，即[**Projects**](/docs/foundry/security/projects-and-roles/)和[**Markings**](/docs/foundry/security/markings/)。

[了解更多关于数据保护和治理的信息。](/docs/foundry/security/data-protection-and-governance/)

---

## [入门] 方向和导航

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/orientation-and-nav/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-orientation-and-nav.md`

# 方向和导航

您可以将 Palantir 平台视为您组织中数据的操作系统。本页提供有关如何在此操作系统中导航和找到所需工具和资源的信息，以便有效工作。

本页提供有关作为在平台中移动的根据地的\*\*[侧边栏](#the-sidebar)**和用于定位感兴趣资源或数据的**[搜索](#search)**功能的信息。您还将了解在平台中工作时可用的**[帮助和支持](#help--support)\*\*选项。最后，您的 Palantir \*\*[账户](#account)\*\*将允许您整理您的公共用户和平台设置。

## 侧边栏

侧边栏是您在平台中的固定伙伴，也是导航的起点。通过右上角的图标或使用键盘快捷键`Cmd+O`（macOS）或`Ctrl+O`（Windows）打开和折叠侧边栏。

侧边栏有五个主要部分，可让您导航到平台中的不同功能和工具：

|  |  |
| --- | --- |
| <img src="../../foundry-docs/getting-started/media/nav-sidebar.png" alt="nav-sidebar" width="250" /> | \*\*① 主页：\*\*返回到您组织的着陆页<br>\*\*① 搜索：\*\*打开快速搜索对话框<br>\*\*① 通知：\*\*查看平台和应用程序通知<br><br>\*\*② 最近：\*\*快速导航到最近访问的资源<br>\*\*② 项目和文件：\*\*跳转到项目着陆页<br>\*\*② 应用程序门户：\*\*查找并访问平台中的所有应用程序<br><br>\*\*③ 收藏夹：\*\*组织并访问您最喜欢的应用程序、资源和Object<br><br>\*\*④ 语言：\*\*更改界面语言<br><br>\*\*⑤ AIP Assist：\*\*LLM 驱动的助手以获取帮助<br>\*\*⑤ 支持：\*\*访问 Palantir 文档、培训资源和帮助<br>\*\*⑤ 账户：\*\*查找账户详情并查看权限和组<br>\*\*⑤ 其他工作空间：\*\*访问自定义工作空间和控制面板（可用性取决于权限）|

## AIP Assist

我们建议以 **AIP Assist**，Palantir 的 LLM 驱动助手，作为获取有关 Palantir 平台帮助的第一站。AIP Assist 可以用多种语言回答有关平台的问题，并提供有关如何使用平台的指导，包括教程。

您可以从侧边栏的右下角或使用键盘快捷键`Cmd+U`（macOS）或`Ctrl+U`（Windows）访问 AIP Assist。

AIP Assist 是“上下文感知”的，它可以检测您当前正在使用的应用程序，但 AIP Assist 无法访问您正在处理的任何数据。

## 主页

新的 Palantir 注册附带一个默认主页，帮助用户定位自己并了解平台。管理员或搭建者还可以为平台上的各种用户组创建自定义着陆页。一些注册可能使用完全自定义的主页，而其他注册可能使用标准组件提供对平台中常用部分的访问。

虽然大多数主页专注于导航，您可能还会在着陆页上找到有关平台的公告、组织中常见工作流程的起始点或自定义文档的链接。

## 搜索

搜索，也称为[快速搜索](/docs/foundry/getting-started/quicksearch/)，是用于在平台中导航和发现元素的工具。搜索由两个部分组成：

1. \*\*跳转模式：\*\*提供个性化结果的简短列表，直接引导用户导航到可用内容的主要类型：平台应用程序、自定义应用程序、Object、数据集和其他资源。
2. \*\*完整结果模式：\*\*旨在帮助用户找到内容并发现平台中存在的内容。用户可以通过高级筛选、丰富的元数据和排名算法来搜索平台应用程序、Object、数据集和其他文件，以突出显示最相关的结果。

要打开快速搜索，请在导航侧边栏中选择**搜索...**，或使用`⌘ + J`（macOS）或`Ctrl+J`（Windows）。

## 通知

通知面板收集来自整个平台的通知，从最新到最旧排序。大多数通知包括链接，可以直接导航到相关资源。某些通知，如访问请求，可以在行内响应，而无需导航到另一个页面。

<img src="../../foundry-docs/getting-started/media/notifications.png" alt="通知面板" width="500">

默认情况下，通知会在平台内的通知面板中和通过电子邮件传递。在**查看所有**链接下，通知按类型分组以便于导航。通知**设置**使您可以对全局和每种通知类型的传递偏好进行细粒度控制。如果通知未读，铃铛图标将有一个小的黄色徽章。如果在您使用平台时发生通知，左下角会出现一个小弹出窗口，短暂显示消息。

## 最近

最近面板仅列出您已打开或互动过的最后 20 个资源。通过**收藏夹**和**最近**，可以快速在任何项目中使用的主要资源之间导航，而无需返回**搜索**或浏览项目文件夹结构。

<img src="../../foundry-docs/getting-started/media/recent.png" alt="最近面板" width="350" />

## 项目和文件

项目和文件链接到项目文件夹结构的着陆页，在那里您可以访问顶级项目和**数据目录**、**您的文件**以及**与您共享**快捷方式。您将在本指南的下一步中了解更多关于项目的内容。

## 应用程序门户

[应用程序门户](/docs/foundry/app-building/curating-apps/)是一个工具，用于查找和访问平台中的所有应用程序，包括平台应用程序和自定义推广的应用程序。

## 收藏夹

侧边栏的收藏夹部分保留了特定应用程序、资源和单个Object的链接，以便快速导航。在 Windows 上使用 Ctrl+Click 或在 macOS 上使用 Cmd+Click 可以在新浏览器标签页中打开收藏资源。

### 收藏的应用程序

当您第一次使用平台时，您的收藏夹部分是空的，侧边栏中只会显示**应用程序**。选择**查看全部**以查看平台中的所有不同应用程序，或单击**收藏的应用程序**文本以弹出**管理您的收藏夹**视图。

|  |  |
| --- | --- |
| <img src="../../foundry-docs/getting-started/media/favorite-area.png" alt="favorite-area" width="300" /> | <img src="../../foundry-docs/getting-started/media/manage-favorites.png" alt="manage-favorites" width="450" /> |

在此视图中，您将看到基于您最近使用情况的建议应用程序和资源。我们将在本指南的后续部分介绍根据您的角色推荐的应用程序。要了解更多信息，请考虑查看[应用程序参考](/docs/foundry/getting-started/application-reference/)。

### 推广的应用程序

您可以通过在门户上选择星形图标将有用的推广应用程序从应用程序门户添加到侧边栏（见左图）。一旦在侧边栏上，推广的应用程序将出现在一个专用部分中，以便快速访问（见右图）。

|  |  |
| --- | --- |
| <img src="../../foundry-docs/getting-started/media/apps-portal-star-icon.png" alt="Promoted Apps Star Icon" width="300"/> | <img src="../../foundry-docs/getting-started/media/apps-portal-popover.png" alt="Promoted App Sidebar Popover" width="500"/> |

### 收藏的资源

您可以在导航文件夹结构时或在打开的资源中使用星形图标添加和移除收藏夹。

<img src="../../foundry-docs/getting-started/media/favorited-resource.png" alt="favorited-resource" width="450" />

<img src="../../foundry-docs/getting-started/media/favorite-in-resource.png" alt="favorite-in-resource" width="450" />

将收藏夹视为快捷方式，您可以添加和移除以保持常用资源近在手边。

### 收藏的Object

[**Object Explorer**](/docs/foundry/object-explorer/overview/)是一个您可以用来探索平台中的Object和链接的应用程序。当您导航到单个Object视图时，可以选择其标题旁边的星形图标将其保存为收藏夹。这将把Object添加到您的侧边栏。

## 帮助和支持

Palantir 提供广泛的功能、特性和组件，供您的应用案例和工作流程使用。为帮助您了解平台如何最好地满足您的需求，**帮助和支持**面板是了解更多信息和获得问题答案的起点。

### 学习平台

[Palantir 学习门户 ↗](https://learn.palantir.com/) 提供学习平台中主要工具的视频和引导教程

### 文档

您可以随时通过此侧边栏链接返回到平台文档主页。

### 支持

[Palantir 客户成功服务团队 ↗](https://www.palantir.com/customer-success-services/) 提供支持、培训和咨询服务，帮助您和您的组织充分利用平台。如果您的协议中包含此项，您可以使用**报告问题**选项联系团队以在**Issues**应用程序中创建支持票。

## 账户

单击账户面板中的您的姓名以调出您的账户概览。在这里，您可以查看最近的贡献以及您创建的受其他用户欢迎的贡献。单击**编辑个人资料**按钮查看您的**用户设置**。

### 设置

您可以使用个人资料图片和附加信息自定义您的个人资料，以便存储在平台中供您组织的用户查看。当其他用户将鼠标悬停在项目和资源中的您的姓名上时，此信息将出现。添加区分性信息有助于依赖于指派工作或共享资源的操作流程，尤其是在您与另一位同事同名的情况下。

在**账户**选项卡中的用户设置中，您可以找到您的**用户 ID**和权限**组**。如果您有关于权限或数据可见性的问题，您可能会被要求提供此信息。

**通知**选项卡是更改通知传递设置的控制中心。

## 其他工作空间

主要平台工作空间由我们一直在探索的工作空间侧边栏定义。您可以通过选择**打开其他工作空间**访问其他工作空间。

### 控制面板

管理员可以访问**控制面板**工作空间来管理注册。有关更多资源，请参阅[管理文档](/docs/foundry/administration/overview/)。

### Carbon 工作空间

应用程序搭建者可以使用**Carbon**为终端用户创建精心策划的自定义工作空间。可以将多种应用程序组合在一起，以提供量身定制的体验。

## 下一步

现在您已经了解了如何在平台中导航，接下来继续[了解项目和资源](/docs/foundry/getting-started/projects-and-resources/)。

---

## [入门] 开始使用Palantir

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-overview.md`

# 开始使用Palantir

Palantir平台旨在帮助您以数据解决现实世界的问题。Palantir平台被以下用户使用：

* **各种类型的组织：** 从初创企业到跨国公司，再到世界各地的政府。
* **各种类型的用户：** 从IT管理员、软件工程师和数据科学家，到护士、技术人员和操作员。

## 获取访问权限

如果您准备开始但尚未获得Palantir平台的访问权限，您可以：

* **[注册AIP Now ↗](https://signup.palantirfoundry.com/signup?signupPermitCode=BUILD_WITH_AIP\&tracking-code=ptcom-docs)** 获取平台访问权限并以试用帐户开始搭建。
* **[注册AIP训练营 ↗](https://www.palantir.com/platforms/aip/bootcamp/)** 在数小时或数天内从零到应用案例，与Palantir工程师一同工作。

## 开始搭建

一旦您获得访问权限，我们推荐以下资源帮助您在Palantir平台上起步：

* **[用AIP搭建 ↗](https://build.palantir.com)** 是一个精心策划的示例、教程和入门包库，以加速您的搭建工作流程。如果您已有入学访问权限，可以在 `<your-enrollment-URL>/workspace/now/platform` 找到用AIP搭建。
* **[Palantir学习 ↗](https://learn.palantir.com/)** 门户提供课程、工作流程教程、认证等，帮助您从平台中获得最大价值。
* **[AIP Assist](/docs/foundry/assist/overview/)** 是一个由LLM驱动的工具，旨在帮助您导航、理解并通过Palantir平台生成价值。AIP Assist可以通过界面左下角的专用图标在平台内访问。
* **[Solution Designer](/docs/foundry/solution-designer/overview/)** 是一个用于创建使用Palantir平台搭建的解决方案的架构表示的交互工具。如果您已有入学访问权限，可以在 `<your-enrollment-URL>/workspace/solution-design` 找到Solution Designer。

## 继续学习

您可以通过以下资源了解更多关于Palantir平台的信息：

* [Palantir开发者论坛 ↗](https://community.palantir.com/) 是一个向其他用户提问和回答问题的空间。
* [平台文档](/docs/foundry/platform-overview/overview/) 包含关于平台功能和特性的详细信息。我们建议您从一些[入门概念](/docs/foundry/getting-started/introductory-concepts/)开始，或者根据您的角色了解更多关于[平台的下一步](/docs/foundry/getting-started/next-steps-by-role/)。

---

## [入门] 项目和资源

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/projects-and-resources/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-projects-and-resources.md`

# 项目和资源

## 资源

在 Palantir 平台工作通常涉及创建**资源**。这些资源包括数据集——数据连接或变换的输出，或手动上传的数据——以及来自各种平台应用的工件，如代码库、分析、报告或应用程序。

*资源*类似于传统系统中的*文件*。在 Palantir 平台中，我们使用“资源”这一术语以避免混淆，因为某些资源，例如数据集或代码库，可以包含文件在其中。

尽管每种资源类型在不同的平台应用中打开，资源共享一些通用信息。例如，由谁最后更新了资源以及何时更新；哪些用户在不同级别上有访问权限；诸如留下评论和标记收藏的功能；以及诸如移动、共享和放入回收站的交互。此外，每个资源都有一个称为*资源标识符*或 RID 的唯一标识符，该标识符在各个应用程序中是标准化的。

## 项目

资源存在于**项目**中，它们在相关资源组之间形成边界，并提供支持协作的功能。这些功能包括管理谁可以访问项目资源的权限；显示最新的项目活动和关于使用情况的指标；以及策划项目元数据，如文档、关键资源和数据健康。每个项目都有一个用户或群组列表，他们可以访问该项目，并在项目资源上被指派**只读**、**编辑**或**所有者**权限。在项目中，资源可以被组织到**文件夹**中，以提供进一步的结构并保持整洁。

除了为协作创建的项目外，每个用户都有一个个人项目。您可以通过从侧边栏导航到**项目和文件**，然后选择**所有文件**来访问您的个人项目。随着您使用应用程序，您创建的资源将默认出现在您的个人项目中。

## 下一步

现在您已经了解了项目和资源，继续[学习关于交付应用案例](/docs/foundry/getting-started/delivering-a-use-case/)。

如果您想更深入地探索项目，包括学习如何创建和管理它们，请[在项目文档中了解更多](/docs/foundry/projects/overview/)。

---

## [入门] 快速搜索

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/quicksearch/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-quicksearch.md`

# 快速搜索

快速搜索是Palantir平台中一个用于快速、轻松搜索、导航和发现的工具。可以从左侧边栏的**搜索**图标访问快速搜索，或使用`Cmd+J`（macOS）或`Ctrl+J`（Windows）。快速搜索有两种视图模式：

1. **跳转模式：** 提供个性化的简短结果列表，以便用户直接导航到主要类型的可用内容：平台应用程序、自定义应用程序、对象、数据集和其他资源。
2. **完整结果视图：** 旨在帮助用户查找内容和发现平台中存在的内容。用户可以使用高级筛选器搜索Palantir应用程序、对象、数据集和其他文件，并找到最相关的结果以及丰富的元数据。

## 跳转模式

* **易于访问：** 要打开快速搜索，在导航侧栏中选择**搜索...**，或使用快捷键`Cmd+J`（macOS）或`Ctrl+J`（Windows）。
* **以导航为中心：** 初始对话框和下拉菜单以导航为导向。开始输入以接收建议。使用键盘跳转到平台中的任何页面。
* **仅搜索标题：** 跳转模式仅在应用程序、资源和对象的标题中搜索。要搜索其他字段和元数据，请使用完整结果模式。
* **单击即可获得完整结果：** 从对话框和下拉菜单中，按`Enter/Return`或通过**应用程序**、**对象**、**数据集**或**文件**筛选以进入高级搜索模式。
* **个性化结果：** 快速搜索中的结果根据您最近访问或收藏的资源进行个性化。

## 完整结果视图

* **以发现为中心：** 设计用于搜索和发现，用户可以比较多个搜索结果以找到对他们最有用的资源。
* **搜索多个字段：** 搜索描述、列名、文件路径等。此外，可按创建者、标签、项目、文件夹等进行筛选。
* **标签：** 界面包括一个顶级结果标签和四个可筛选的标签：**应用程序**、**对象**、**数据集**或**文件**。
* **元数据：** 用户可以查看每个结果的信息，以评估该资源是否与他们相关。按关键字高亮搜索、文件路径、查看次数、最后更新时间、关键安全元数据等。
* **排序：** 结果基于一个包含文本匹配和其他提升参数的算法进行排序。
* **筛选器：** 提供筛选器用于高级搜索。此外，通过从初始搜索下拉菜单中选择筛选标签，用户可以执行复杂的筛选搜索（例如，“我创建的项目X下的所有报告”）。
* **权限：** 快速搜索遵循平台中的所有现有权限。具有`发现`权限的内容将打开一个`请求访问`消息。用户将看不到他们无权访问的内容。

快速搜索**不会**在平台中的所有对象实例中进行搜索。快速搜索仅限于搜索250个对象类型的实例，优先级为`活动`对象类型的`重要`，然后是`正常`，然后是`实验`状态（不搜索已弃用和隐藏的对象类型）。如果用户找不到他们正在寻找的内容，他们会被提示尝试在[Object Explorer](/docs/foundry/object-explorer/search-objects/)中搜索，在那里他们可以将搜索调整为仅特定组的对象类型，甚至是特定的对象类型。

### 筛选器

您可以通过快速搜索中的筛选器快速找到平台中所需的资源和数据。通过选择**应用程序**、**对象**、**数据集**或**文件**结果类型来筛选您的搜索结果。您甚至可以通过在文件路径、标签或项目中搜索来进一步筛选。一旦应用筛选器，搜索结果视图将仅显示您选择的结果类型。

例如，我们想要搜索在我们的注册中关于“汽车”的资源。

#### 应用程序

要搜索通过Palantir应用程序搭建接口制作的模块、工作区或其他应用程序，您可以按**应用程序**进行筛选。

在我们的“汽车”搜索示例中，我们可以看到三个Workshop模块、一个Carbon工作区和一个Slate文档，这些都被正确识别为在Palantir中构建的应用程序。

#### 对象

要仅查看基于Ontology对象类型的结果，请按**对象**进行筛选。在此搜索结果视图中，您可以从与搜索词匹配的对象类型中进行选择，选择编辑或查看对象类型的谱系，并进一步深入到单个对象。

当搜索“汽车”时，我们看到几个对象类型和对象结果，并且可以进一步筛选到选定的对象类型，如`Award`或`Auto Parts`。

#### 数据集

当按**数据集**筛选时，结果视图将显示平台中与数据集名称或列名称中的搜索词匹配的可用数据集列表。

使用相同的“汽车”示例，我们可以看到包含匹配术语的数据集和列名称的38个数据集列表。

#### 文件

在快速搜索中使用**文件**标签快速找到添加到或在平台中创建的单个资源文件。使用左侧面板中的筛选器专门搜索某些文件或资源类型。

当我们搜索“汽车”时，我们收到几种不同的文件结果，包括文件夹、图表、图像和Modeling Objective。

## 高级搜索

高级搜索提供了一种超出快速搜索范围的更全面的搜索体验。当您不知道所需资源的名称或元数据时，这可能很有用。通过选择快速搜索右上角的“展开”图标进入高级搜索。

与快速搜索类似，高级搜索提供了一个**顶级**结果标签和其他按类别筛选结果的标签：**应用程序**、**数据集**和**文件**。要查询特定对象，您可以通过选择右上角的**Object explorer**从高级搜索导航到Object Explorer。

完整的高级搜索查询被捕获在一个有状态的URL中。您可以通过从浏览器中复制URL并发送给同事来分享感兴趣的查询。结果可能因用户之间的[资源访问控制](/docs/foundry/security/securing-a-data-foundation/)而异。

### AIP驱动的推荐 \[测试版]

AIP驱动的搜索推荐是一个[实验](/docs/foundry/platform-overview/development-life-cycle/#experimental)功能，并非在所有地方都可用。对于早期采用请求，请联系您的Palantir代表。

除了顶级结果外，高级搜索还提供AIP驱动的推荐，可以解析完整句子、语义查询并推荐下一步。这些建议会在**顶级**标签中以紫色框加载。

---

## [入门] 支持概述

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/support-overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-support-overview.md`

# 支持概述

如果您在使用Palantir平台时遇到任何问题，可以查看下面关于如何调查、诊断和找到合适解决方案的指导。

## 1. 调查问题

在提交支持请求之前，请按照以下步骤解决潜在问题。通过收集以下信息，可以加快调查过程，帮助我们提供最佳解决方案。

1. 首先查看平台的出错信息，并将其整理到文档中。
2. 如果出错信息不清晰或未提供可操作的下一步，请使用 [Chrome™ 开发者工具](/docs/foundry/getting-started/debug-using-devtools/) 获取关于问题的更多信息。
3. 考虑自上次平台正常运行以来是否进行了任何更改。尝试恢复这些更改并测试问题是否已解决。
4. 检查状态邮件、警报和公告，以了解已知问题或可能影响您工作的计划维护。
5. 搜索 [平台文档](/docs/foundry/) 以查看是否有有用的建议。
6. 复制errorID/errorInstanceID并与支持团队分享。
7. 使用数据沿袭调查管道中的问题（例如，权限、搭建状态、搭建计划等）。
   * 选择不同的节点着色选项（例如，`上次搭建时间`或`权限`）可以突出显示管道中资源的不同特征。
8. 如果您看到不清楚的出错信息，请检查控制台日志。

## 2. 搜索问题应用程序和Stack Overflow

通过您自己调查获得的附加信息，您可以访问：

* **问题**应用程序，以查看其他用户报告的问题，这可能有助于解决或提供您问题的见解。此应用程序通过跟踪过去的问题，提供来自Palantir支持的先前参与，以及问题解决的时间线，为平台中的问题提供透明度。

* [Palantir开发者论坛 ↗](https://community.palantir.com/) 向您的其他用户提问和回答问题。在这里，您可以找到其他Palantir用户提出的问题，并获得您面临问题的帮助。

* 我们的 [公共 Stack Overflow ↗](https://stackoverflow.com/questions/tagged/palantir-foundry) 用于编程（包括无代码工具）和代码相关问题。

## 进一步协助

如果您无法从上述资源或我们的[平台文档](/docs/foundry/)中找到解决方案，请了解如何[准备和提交支持票](/docs/foundry/getting-started/file-support-ticket/)，其中详细说明了如何收集调试信息并创建类似示例，以便Palantir支持能够快速解决您的问题。

***

Chrome™ 是Google Inc.的商标。

---

## [入门] 支持的浏览器

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/supported-browsers/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-supported-browsers.md`

# 支持的浏览器

Palantir平台完全支持在最近六个月内发布的Google Chrome和Microsoft Edge版本上使用。Palantir的移动友好应用程序需要Google Chrome、Microsoft Edge或Apple Safari。

Palantir将为使用最近六个月内发布的Mozilla Firefox版本的用户提供关键错误修复。为获得最佳效果，请尽可能使用Google Chrome或Microsoft Edge。

---

## [入门] 培训应用

- 官方原文：https://palantir.com/docs/zh/foundry/getting-started/training-application/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-getting-started-training-application.md`

# 培训应用

培训应用为您提供从[learn.palantir.com ↗](https://learn.palantir.com)精心挑选的课程集合，并链接到所有平台内和公开的学习资料，以学习如何使用Palantir平台。

<img src="../../foundry-docs/getting-started/media/training-application.png" alt="培训应用" width="800">

## 为您的组织呈现培训文档

培训应用允许您呈现记事本文档，其中包含与您的组织相关的培训信息。

要呈现包含培训材料和说明的记事本文档，请[创建一个名为](/docs/foundry/projects/tags/)`Training application`的标签类别。每个用户可访问并在标签类别`Training application`下标记的记事本文档都将在培训应用中显示。您可以自由命名类别中的标签，这些标签将显示在指向文档的链接中。

<img src="../../foundry-docs/getting-started/media/training-application-documents.png" alt="呈现与您的组织相关的培训信息的记事本文档。" width="800">

---

## [platform-overview] 平台概览

- 官方原文：https://palantir.com/docs/zh/foundry/platform-overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-overview.md`

# 平台概览

Palantir AIP 在全球最关键的商业和政府环境中推动实时、AI驱动的决策。从[公共卫生 ↗](https://www.youtube.com/watch?v=1F7apO2hFXk\&list=PLmKm_LhXXgqQra-4olkIlUtsUPAchcfJv\&index=4)到[电池生产 ↗](https://www.youtube.com/watch?v=3C4_3O2Grn4\&list=PLmKm_LhXXgqRam-Dgv5UWLhGweN9nmeUp\&index=3)，组织依赖 Palantir 在其企业中安全、可靠和有效地利用AI，并[推动运营成果 ↗](https://www.youtube.com/watch?v=CmpQTrnL3ko\&list=PLmKm_LhXXgqQQGVPa4l88ExP556vDMTgF)。

简而言之，Palantir AIP 将生成性AI与运营连接在一起。与 Foundry - Palantir 的数据运营平台 - 以及 Apollo - Palantir 用于自主软件部署的任务控制平台 - 一起，AIP 是一个 *AI 网格* 的一部分，能够提供全套的AI驱动产品，从 LLM 驱动的网络应用到使用视觉语言模型的移动应用，再到嵌入本地化 AI 的边缘应用。我们将这整套能力、功能和工具称为 *Palantir 平台*。

尽管实现和扩大 Palantir 平台的运营影响力有许多因素 —— 包括 [AIP 训练营 ↗](https://www.palantir.com/platforms/aip/bootcamp/)，客户可以在短短几小时内通过 AI 实现成果 —— 关键的差异化因素是围绕 Palantir [Ontology](#the-ontology) 的软件架构。

## Ontology

Ontology 旨在表示企业中的*决策*，而不仅仅是数据。世界上的每个组织都面临如何在瞬息万变的内部和外部条件下执行最佳决策的挑战，通常是实时的。

这些决策过程的复杂性反映在 Ontology 中，它促进了与现有企业系统的深度双向互操作性。Ontology 自动将相关数据、逻辑和操作组件集成到现代化、AI可访问的计算环境中。这不仅解锁了与 AI 协作的运营应用的快速开发，还包括传统的商业智能和分析工作流。

## 决策组件

每个决策都可以分解为**数据**、**逻辑**和**操作**。

* **数据：** 形成此决策背景的相关事实或真相是什么？
* **逻辑：** 什么组织或业务规则作为此决策的护栏？在不同假设下某些结果的概率是什么？我们在以前的类似情况下做了什么，结果如何？我们的预测和优化模型的输入是什么？
* **操作：** 此决策的“动力学”或效果是什么 - 即，该决策如何在世界上体现？我们如何减少或缩短在 AIP 中做出决策与在生产环境中产生结果之间的步骤？

在 Palantir 平台中，所有这些组件都设计为促进 AI 协作模式，以释放您的操作员、分析师和主题专家的全部潜力。

### 数据

Ontology 将数据作为[对象和链接](/docs/foundry/ontology/overview/#object-and-link-types)集成，以使运营的现实世界复杂性对人类和AI都可理解。这解锁了构建*人类+AI协作*工作流的能力。

Ontology 本地支持多种数据类型以及一些扩展基元，例如用于解锁非结构化数据的[语义搜索](/docs/foundry/functions/overview-semantic-search/)、用于处理图像和视频的[媒体引用](/docs/foundry/data-integration/media-sets/#ontologize-media-using-media-references)和用于在数据中嵌入额外约束和上下文的[值类型](/docs/foundry/object-link-types/value-types-overview/)。这些是 AI 工作流开发的数据构建块，在下面的[逻辑](#logic)和[操作](#actions)部分中有更详细的描述。

此数据模型为探索结构化、非结构化、地理空间、时间序列、模拟和其他数据模式的开箱即用应用程序提供支持。这些基础工具与上下文感知的[AIP Assist](/docs/foundry/assist/overview/)相结合，大大缩短了在平台中探索和分析数据的时间。

除了应用程序构建和分析外，在 Ontology 中建模数据会自动创建一个强大的 API 网关和 Ontology 软件开发工具包（OSDK），作为企业内连接性的“运营总线”。

#### 数据连接

数据很少以干净、正确和形状良好的格式提供，以准确和可靠地向决策者展示事实。为此，Palantir 平台提供了一个可扩展的、多模式的数据连接和集成框架，能够开箱即用地与企业数据系统协作。

[Pipeline Builder](/docs/foundry/pipeline-builder/overview/) 将[LLM数据变换](/docs/foundry/pipeline-builder/pipeline-builder-llm/)的能力放入一个点击即用的包中，使使用最新的 LLMs 来支持基于管道的变换（如分类、情感分析、摘要、实体提取或翻译）变得简单。这为在 Ontology 中自动创建“提案”供操作员审查和批准奠定了基础，无需一直运行实时模型请求的滞后。（注意，正如在下面的[逻辑](#logic)部分中讨论的，这两种与模型交互的方法是高度互补的。）

此外，[Pipeline Builder](/docs/foundry/pipeline-builder/overview/)和[Code Repositories](/docs/foundry/code-repositories/overview/)中的[AIP Assist](/docs/foundry/assist/overview/)通过一个具有深度集成的 AI 合作伙伴加速数据工程，该合作伙伴不仅能访问 Palantir 文档和通用代码片段存储库，还可以为下一步操作或相关教程提供建议。

### 逻辑

如果数据定义了我们决策的背景，逻辑则封装了丰富此背景的推理和分析，使人类+AI 团队能够做出更好的决策。这可以以模型输出和可视化的形式提供额外的上下文，呈现在运营应用中，或直接融入操作的机制中。

基于这一广泛定义，定义和执行逻辑的能力贯穿于整个平台；例如，我们可以考虑[模型](#models)、[业务逻辑](#business-logic)和[模板化分析和报告](#templated-analyses-and-reports)。

#### 模型

*生成性AI、LLMs、预测、优化器等*

像 LLMs 或预测这样的模型接受参数并提供输出，以作为当前决策的背景。在数据科学家熟悉的循环中，这些模型通常经历训练和优化的迭代过程；然而，将这些模型用作生产中的运营工作流可能是一个挑战。Palantir 的建模能力可以促进模型的运营部署。

在 Palantir 平台中，模型的完整生命周期被捕获为[建模目标](/docs/foundry/model-integration/objectives/)，而模型本身的逻辑被抽象为[模型适配器](/docs/foundry/integrate-models/integrate-overview/)。这种方法意味着无论您是[在平台中训练](/docs/foundry/integrate-models/model-asset-code-repositories/)、[自行携带容器](/docs/foundry/integrate-models/container-overview/)还是[上传预训练模型](/docs/foundry/integrate-models/model-asset-files/)，各种模型都可以通过[函数](/docs/foundry/functions/functions-on-models/)绑定到 Ontology 中，以便在运营应用中进行实时交互，或者被配置为[批量部署](/docs/foundry/manage-models/set-up-batch/)并计划在数据管道中执行。

特别是对于生成性AI，Palantir 的语言模型服务提供了一个统一的界面用于多模式交互，同时抽象了特定模型和提供商的实现细节，使得在商业可用的 LLMs 领域中进行开发变得简单。为了进一步改进结果，Palantir 的[评估](/docs/foundry/logic/evaluations-overview/)工具可以让您在时间和模型之间对 LLM 的性能进行基准测试，以监控漂移并自信地进行更改。

#### 业务逻辑

*业务规则、流程映射、语义搜索*

当建模方法采用自下而上的数据训练方法时，业务逻辑通常基于治理运营领域的显性或隐性规则，自上而下进行。这些可能存在于外部系统中，Palantir 可以通过[外部函数](/docs/foundry/data-integration/external-functions/)和[Webhooks](/docs/foundry/data-connection/webhooks-overview/)直接连接这些系统以在运营工作流中进行实时交互，或通过[外部变换](/docs/foundry/data-integration/external-transforms/)进行管道连接。业务逻辑也可以直接在 Palantir 平台内使用[规则](/docs/foundry/foundry-rules/overview/)和管道构建器为数据管道中的逻辑进行编写，以及为将在运行时执行的逻辑使用 Automate 和函数。

#### 模板化分析和报告

*对象视图、分析模板、生成的报告*

逻辑不仅存在于数据科学模型中或作为硬编码业务规则；分析师通常在一次性调查、分析或报告中捕获和收集高价值逻辑。在 Palantir 平台中，您可以使用[Contour](/docs/foundry/contour/overview/)和[Quiver](/docs/foundry/quiver/overview/)等点击分析工具以及[Code Workspaces](/docs/foundry/code-workspaces/overview/)等笔记本构建分析和仪表盘。Ontology 数据模型的语义使得很容易将这些分析产品模板化并重复使用，无论是嵌入在[对象视图](/docs/foundry/object-views/config-overview/)或[Workshop应用](/docs/foundry/workshop/module-interface/)中，还是作为独立[仪表盘](/docs/foundry/notepad/widgets-quiver-dashboard/)展示。这些对象视图、模板化分析和仪表盘可以插入运营应用中，提供一目了然的见解以指导决策，同时提供进一步临时探索的途径。

总之，这三个逻辑方面——模型、业务逻辑和模板化分析及报告——提供了一个工具箱或调色板，用户可以从中自由组合，为决策者在关键时刻提供所需的所有上下文。

### 操作

为了使任何决策产生影响，该决策必须传播到世界中。这就是操作定义企业“动词”的地方 - 也就是所做的事情 - 并控制人类操作员或 AI 代理如何确保其决策持续存在，无论是在 Ontology 数据模型中还是通过与[外部系统](/docs/foundry/action-types/side-effects-overview/)的交互。此外，在 Ontology 中捕获决策结果允许用户将特定决策与未来数据中的结果观察配对。这使得反馈循环成为可能，将未来的决策置于过去选择的背景中，并可以用于重新训练或微调模型，或者仅仅支持操作员更清晰地了解过去。

在 Ontology 中表示这些“动力学”的原子单位是[操作](/docs/foundry/action-types/overview/)，它提供了特定、细粒度的控制用于更改或创建数据，以及用于在外部系统中协调更改。可以通过一个点击配置界面简单地定义基本操作。可以通过[函数支持的操作](/docs/foundry/action-types/function-actions-overview/)和[Ontology 编辑 TypeScript API](/docs/foundry/functions/api-ontology-edits/)指定任意复杂的操作。操作也可以在[Ontology 软件开发工具包](/docs/foundry/ontology-sdk/overview/)（OSDK）和[平台API](/docs/foundry/api/ontology-resources/actions/action-basics/)中打包，以便自定义应用开发和现有第三方工具可以轻松且安全地写回到 Ontology。

每个操作的[权限](/docs/foundry/action-types/permissions/)确定哪个用户或代理在什么条件下能够执行操作，为安全、可审计和透明的控制奠定了基础。

在复杂、紧密耦合的环境中，如供应链或制造车间，一个小的变化可能会引起级联效应，产生意外或意图之外的结果。[场景](/docs/foundry/vertex/scenarios-overview/)原语允许用户通过对 Ontology 的一个分支进行更改来预测这些后果，有效地创建一个沙盒宇宙，在这个宇宙中可以对潜在变化进行预测、业务流程模型和其他分析。[Vertex](/docs/foundry/vertex/overview/)应用专门用于这种过程可视化和情景测试；[Workshop](/docs/foundry/workshop/scenarios-overview/)应用构建器本地支持情景用于开发包含“假如...”工作流的运营应用。

这些原语为安全开发在生产工作流中操作的人类+AI 团队创造了环境。操作的细粒度权限和访问控制提供了一个“控制平面”，其中代理被沙盒化，具有对其可以使用的数据和工具的特定限制。在大多数模式中，AI 代理不是直接进行更改，而是通过与[集成到 Workshop 的 AIP Logic](/docs/foundry/logic/overview/)函数的直接集成同步创建提案，或通过[Automate](/docs/foundry/automate/overview/)或[Pipeline Builder 中的 Use LLM](/docs/foundry/pipeline-builder/pipeline-builder-llm/)节点异步创建提案。生成的提案然后可以呈现给操作员以进行改进、反馈和最终决策。此基于提案的模式，除了加强“人类在回路中”范式外，还生成了有价值的元数据，使代理能够在持续反馈的情况下学习和发展。

## 接下来是什么？

体验 AIP 威力的最佳方式是开始构建。阅读[入门](/docs/foundry/getting-started/overview/)指南以获取更多信息，或者 - 如果您可以访问平台 - 只需询问 AIP Assist 根据您的目标建议从何处开始。

有关这些决策组件如何交互以指导工作流开发的更多信息，请参阅关于[提炼功能需求](/docs/foundry/use-case-life-cycle/distilling-functional-requirements/)的讨论，在[应用案例开发](/docs/foundry/use-case-life-cycle/overview/)中讨论，或在[AIP Now 展示 ↗](https://aip.palantir.com/)中找到行业特定的端到端工作流示例。

此外，您可能会对了解 AIP 的构建方式以及如何与您组织中的现有投资集成感兴趣：

* [架构](/docs/foundry/platform-overview/architecture/)
* [互操作性](/docs/foundry/platform-overview/interoperability/)
* [开发生命周期](/docs/foundry/platform-overview/development-life-cycle/)

## 平台能力

文档的其余部分被组织为[平台能力](#platform-capabilities)的集合。每个能力的摘要如下：

* [数据连接和集成](#data-connectivity-and-integration)
* [模型连接与开发](#model-connectivity-and-development)
* [Ontology 构建](#ontology-building)
* [应用案例开发](#use-case-development)
* [分析](#analytics)
* [产品交付](#product-delivery)
* [安全与治理](#security-and-governance)

### 数据连接和集成

Palantir 提供了一个可扩展的、多模式的数据连接框架，能够开箱即用地连接到企业数据系统并提供：

* 对现有数据湖和平台的就地、零复制访问；
* 一个基于 Kubernetes 的自动缩放数据构建系统，适用于批量和流式管道；
* 集成的管道调度和编排；
* 所有数据流的本地健康检查；以及
* 涵盖基于角色、分类和目的的访问控制的全面安全功能。

### 模型连接与开发

Palantir 提供一个集成的、端到端的模型开发环境（如，Python 和 R）；灵活集成使用行业标准工具集构建的外部模型；为所有开发或集成的模型提供受管路径到生产；以及一个用于持续评估部署模型的“任务控制”。架构目标是为企业中的所有业务逻辑和建模提供连接路径，无论给定的资产是在何处训练、测试和/或托管。

### Ontology 构建

如上所述，为了创建一个综合的决策中心企业模型，Ontology 集成了：

* *数据*，作为[对象和链接](/docs/foundry/ontology/overview/#object-and-link-types)；
* *逻辑*，作为[模型](/docs/foundry/model-integration/overview/)和[函数](/docs/foundry/functions/overview/)；以及
* *操作*，作为平台[操作](/docs/foundry/action-types/overview/)。

Ontology 的这些构建块使运营的现实世界复杂性对操作者和AI都可理解，解锁了构建混合人类-AI工作流的能力。额外能力包括：

* 从最终用户捕获数据回到语义基础的结构化机制；
* 用于在结构化、非结构化、地理空间、时间序列、模拟和其他范式中探索 Ontology 的开箱即用应用；以及
* 利用 Ontology 作为企业各个部分的“运营总线”的 Ontology 软件开发工具包（OSDK）。

### 应用案例开发

Palantir 的应用开发框架使企业能够构建运营工作流并开发应用案例，利用用户操作、警报和其他终端用户前线功能与工具使用、数据感知的 AIP 代理进行协作。

应用案例开发能力包括：

* 与 AIP Logic 集成以构建自定义工作流代理；
* AI 辅助、低代码/无代码应用程序构建，自动化安全实施以及底层存储和计算的管理以及数据和模型绑定；
* 具有实时预览的应用开发框架；以及
* 允许与企业进行全方位集成的 API、webhooks 和其他接口。

### 分析

平台为每种类型的用户提供分析能力，无论他们是否会编程。能力包括点选和基于代码的工具，能够进行基于表格的分析、自上而下的可视化分析、地理空间分析、时间序列分析、情景模拟等。

Palantir 的分析套件超越了传统的“只读”范式，将数据写回 Ontology，在统一的安全性、血统和治理模型中生成有价值的新见解。

平台还与常用建模环境（支持使用[Code Workspaces](/docs/foundry/code-workspaces/overview/)的 JupyterLab® 和 RStudio® Workbench 的本地使用）和商业智能平台（包括 Tableau® 和 PowerBI® 的[专用连接器](/docs/foundry/analytics-connectivity/overview/)）互操作。

### 产品交付

Palantir 平台提供 DevOps 工具来打包、部署和维护在平台中构建的数据产品。这些产品交付能力包括一个包装界面，用于创建由平台资源集合（管道、Ontology、应用程序、模型等）组成的“产品”；用于产品发现和安装的市场前台；以及通过自动升级、维护窗口等管理产品安装的能力。

### 安全与治理

Palantir 平台具有全面的、最佳实践的安全模型，该模型传播到整个平台，并且默认情况下，与信息同行无论其走向何处。能力包括：

* [所有数据的加密](/docs/foundry/security/overview/#enterprise-security)，无论是在传输中还是在静止时；
* 身份验证和身份保护控制；
* 授权控制可以结合基于角色、权限标记和目的驱动的范式；
* 强大的安全[审计日志](/docs/foundry/security/audit-logs-overview/)；以及
* 高度可扩展的信息治理、管理和[隐私控制](/docs/foundry/security/protecting-sensitive-data/)。

### 管理与支持

平台管理员可以访问一套强大的工具来管理 Palantir 平台。平台管理的核心应用是：

* [控制面板](/docs/foundry/administration/control-panel/)
* [资源管理](/docs/foundry/resource-management/overview/)
* [升级助手](/docs/foundry/upgrade-assistant/overview/)

平台管理员和项目经理还可以访问促进用户支持的资源，例如[AIP Assist](/docs/foundry/assist/overview/)。这些资源在[管理与支持文档](/docs/foundry/administration/overview/)中进行了描述。

---

## [platform-overview] AIP功能

- 官方原文：https://palantir.com/docs/zh/foundry/platform-overview/aip-capabilities/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-overview-aip-capabilities.md`

# AIP功能

Palantir平台上的应用程序配备了AIP驱动的功能。本页面描述了其中的一些功能。

AIP的AI功能可以分为三类：

* **AIP Assist:** 一个由LLM驱动的支持工具，旨在帮助用户导航、理解并利用Palantir平台生成价值。用户可以用自然语言向AIP Assist提问，并实时获得查询帮助。
* **平台应用中的AIP助手功能:** 本地的LLM支持功能，旨在帮助终端用户在Palantir平台上执行常规工作流程。这些功能高度针对性地利用平台知识来加速用户的日常操作。
* **自定义工作流程的AIP功能:** 一组允许开发人员搭建自己的LLM支持工作流程或应用程序的功能。这些是为开发人员或数据科学家构建的开放式功能。

[了解如何在平台中启用AIP功能。](/docs/foundry/administration/enable-aip-features/)

[了解AIP核心功能与自定义工作流程AIP功能的区别。](/docs/foundry/administration/enable-aip-features/#aip-and-capabilities-for-custom-workflows)

## AIP Assist侧边栏

AIP Assist侧边栏具备上下文感知功能，可以通过自然语言提示为用户提供支持。您可以从工作区导航栏中打开AIP Assist，或使用键盘快捷键（`Cmd + Shift + U`（macOS）或`Ctrl + Shift + U`（Windows））访问它。AIP Assist将显示在一个面板中，如下图所示。

[了解更多关于AIP Assist侧边栏的信息。](/docs/foundry/assist/overview/)

## 平台应用中的AIP功能

AIP功能已嵌入核心应用程序中，帮助用户加速工作流程并在平台中解锁更多价值。以下是一些精选的AIP功能示例，并不是详尽列表。AIP的最新更新可以在文档的[公告](/docs/foundry/announcements/)部分找到。

### Pipeline Builder

在Pipeline Builder中使用AIP，以帮助您更好地理解、搭建和管理您的管道。Pipeline Builder有一组核心的Assist功能和用于自定义工作流程的额外AIP功能。

Pipeline Builder中的[核心Assist功能](/docs/foundry/pipeline-builder/pipeline-builder-aip/)示例如下：

**解释:** 了解管道开发步骤，并建议相关的名称和描述。

**正则表达式助手:** 生成定制的正则表达式，适用于所有技能水平。

**变换助手:** 创建和编辑正则表达式，并轻松将字符串转换为特定的时间戳格式。

此外，具有[权限](/docs/foundry/administration/enable-aip-features/)的情况下，您可以在Pipeline Builder中使用自定义工作流程的AIP功能，例如：

[使用LLM节点](/docs/foundry/pipeline-builder/pipeline-builder-llm/)，提供了一种方便的方法，在大规模数据上执行大语言模型（LLM）。提供了五个预先设计的模板，适合初学者使用LLM，利用经验丰富的提示工程师的专业知识。

您还可以在整个数据集上运行模型之前，通过几行输入数据集[运行试验](/docs/foundry/pipeline-builder/pipeline-builder-llm/#trial-run)，以迭代您的提示。

### Notepad

AIP还为Notepad带来了[LLM驱动的功能](/docs/foundry/notepad/aip-features/)，您可以使用AIP自动拼写检查、缩短、修改或翻译文本，而不会影响文档的现有格式。

### Scheduler

您可以在[Scheduler应用程序中使用AIP](/docs/foundry/pipeline-builder/schedules-scheduler-aip/)，在创建具有特定时间触发器的数据集搭建计划时生成计划配置。在**新计划视图**侧边栏中输入计划触发器提示，以生成复杂触发器的正确cron格式。

### AIP Threads \[Beta]

[AIP Threads](/docs/foundry/threads/overview/) 使用户能够利用LLM的强大功能完成各种任务和临时分析。无需设置或技术专长即可与文档（例如PDF）和[AIP Agents](/docs/foundry/chatbot-studio/overview/)（配备企业特定信息和工具的互动助手）进行交互。开始时，您只需将文档拖放到界面中，选择您有权限访问的先前上传的文档，或选择您和您的组织创建的AIP Agent。

## 自定义工作流程的AIP功能

[自定义工作流程的AIP功能](/docs/foundry/administration/enable-aip-features/)允许开发人员和搭建者在Palantir平台中搭建自己的LLM支持工作流程或应用程序。这些功能包括但不限于AIP Logic、Pipeline Builder中的“使用LLM”节点和文本到嵌入、AIP Automate、AIP Chatbot Studio和AIP Workshop微件。这些功能本地支持大语言模型选项。

Palantir提供的LLM也可用于核心Foundry功能中，如[函数](/docs/foundry/functions/language-models/)、[变换](/docs/foundry/transforms-python/palantir-provided-models/)和通过[Code Workspaces](/docs/foundry/code-workspaces/palantir-provided-models/)的Jupyter®笔记本。

此外，现有的Palantir功能[模型集成](/docs/foundry/model-integration/overview/)允许用户连接自定义大语言模型，并从零独立搭建应用案例。

平台管理员可以通过Control Panel中的[**AIP设置**](/docs/foundry/administration/enable-aip-features/)管理这些功能的使用。

## 支持的LLM

Palantir平台提供对多种LLM（大语言模型）和文本嵌入模型的支持。

### Palantir提供的大语言模型（LLM）

我们提供了一组LLM，用于自定义工作流程的AIP功能，不同注册中的[LLM选择和可用性](/docs/foundry/administration/enable-aip-features/#llm-availability)有所不同。有关可用模型的详细信息如下：

* [GPT-4o ↗](https://platform.openai.com/docs/models/gpt-4o)
* [GPT-4 Turbo ↗](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo)
* [GPT-4 Turbo with Vision ↗](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo)
* [GPT-4 ↗](https://platform.openai.com/docs/models/gpt-4)
* [GPT-4 (32k) ↗](https://platform.openai.com/docs/models/gpt-4)
* [GPT-3.5 ↗](https://platform.openai.com/docs/models/gpt-3-5)
* [GPT-3.5 16k ↗](https://platform.openai.com/docs/models/gpt-3-5)
* [Llama3 8B Instruct ↗](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md)
* [Llama3 70B Instruct ↗](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md)
* [Llama 3.1 8B Instruct ↗](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md)
* [Llama 3.1 70B Instruct ↗](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md)
* [Llama2 13B Chat ↗](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)
* [Llama2 70B Chat ↗](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)
* [Mixtral 8x7B Instruct ↗](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)
* [Mistral 7B Instruct ↗](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
* [Anthropic Claude\_2 ↗](https://aws.amazon.com/bedrock/claude)
* [Anthropic Claude\_Instant ↗](https://aws.amazon.com/bedrock/claude)
* [Anthropic Claude 3 Sonnet ↗](https://aws.amazon.com/bedrock/claude)
* [Anthropic Claude 3.5 Sonnet ↗](https://aws.amazon.com/bedrock/claude)
* [Anthropic Claude 3 Haiku ↗](https://aws.amazon.com/bedrock/claude)

要了解LLM如何安全地处理用户提示，请通过选择**Palantir AIP常见问题**，查看[常见问题：Palantir利用第三方托管LLM的AIP的安全性和隐私 ↗](https://palantir.safebase.us/?itemName=data_privacy\&source=click)。

### 文本嵌入模型

我们也以相同的方式提供了一组文本嵌入模型。

* [Text embedding ada-002 ↗](https://platform.openai.com/docs/guides/embeddings)
* [Text embedding 3 small ↗](https://platform.openai.com/docs/guides/embeddings)
* [Text embedding 3 large ↗](https://platform.openai.com/docs/guides/embeddings)
* [Instructor Large ↗](https://huggingface.co/hkunlp/instructor-large)
* [BGE Base ↗](https://huggingface.co/BAAI/bge-base-en-v1.5)

了解如何[配置您的注册中可用的LLM](/docs/foundry/administration/enable-aip-features/#enable-llms)。

***

注意：AIP功能的可用性可能会发生变化，并且可能因客户而异。

*Jupyter®、JupyterLab®和Jupyter®徽标是NumFOCUS的商标或注册商标。*

*“OpenAI”名称和“GPT”品牌属于OpenAI。*

所有引用的第三方商标（包括徽标和图标）仍然是其各自所有者的财产。未暗示任何附属关系或认可。

---

## [platform-overview] 架构

- 官方原文：https://palantir.com/docs/zh/foundry/platform-overview/architecture/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-overview-architecture.md`

# 架构

Palantir AIP（人工智能平台）旨在扩展至所有类型的终端用户、全球最苛刻的数据驱动型工作负载以及各种基础设施基板。为实现这一目标，底层服务网格在由 [Palantir Apollo ↗](https://www.palantir.com/platforms/apollo/) 强制执行的一组软件定义原则之上运行。

随着AIP的范围和功能集的扩展，并成为许多机构的关键任务，我们需要确保：

* 平台内的数百项服务均以高可用性、冗余配置运行。除了核心后端服务，这还包括前端应用服务、分析工具、应用构建器以及每种用户类型所使用的各组成服务。
* 所有服务升级均在零停机状态下执行，具有细粒度监控，以告知如何部署、监控并可能回滚升级策略。由Apollo作为所有服务编排的全局骨干，安全自动化的水平远远超过手动或定制操作所能实现的。
* 核心服务和相关计算网格的自动扩展利用一致的容器化范式。这是通过 [Rubix ↗](https://blog.palantir.com/introducing-rubix-kubernetes-at-palantir-ab0ce16ea42e) 引擎实现的，该引擎支撑平台的所有自动扩展基础设施，并与Apollo交付平台密切配合。

由Rubix和Apollo共同驱动的服务网格包含模块化功能，可以集成到现有企业架构中。此外，平台架构最大限度地提高了未来的灵活性，以确保客户能够持续受益于最新技术，无论是由Palantir还是开源社区开发的：

* 存储架构不绑定于任何特定的底层范式。平台在架构的不同层次上使用多种存储技术。这包括blob存储（或HDFS）、水平可扩展的键/值存储、水平可扩展的关系数据库和多模式时间序列子系统等。

* 计算架构不绑定于任何特定的底层基础设施。平台不同层次的不同工作负载利用特定的运行时，每个层面都设计了灵活性。数据集成的常用运行时包括Apache Spark和Apache Flink，但如果需要，可以使用外部变换引擎。Palantir开发的引擎为Ontology和其他不易映射到现有计算模式的功能集提供支持。

* 我们努力确保最流行的开放语言在代码驱动的范式中安全且一致地可用。这包括用于数据变换的 [Python](/docs/foundry/transforms-python/overview/)、[SQL](/docs/foundry/transforms-sql/overview/) 和 [Java](/docs/foundry/transforms-java/overview/)；用于机器学习工作流的 [Python 和 R](/docs/foundry/code-workbook/workbooks-languages/)；以及用于定义工作流和前端应用的 [TypeScript](/docs/foundry/functions/overview/) 和 [JavaScript](/docs/foundry/slate/concepts-functions/)。

* 安全性和传承是AIP中每个操作的核心，并在平台架构的每一层级始终如一地执行。这确保没有单一服务（或终端用户）负责执行企业的现有安全策略，或实施维持来源所需的“记账”。从数据到决策，高可用的核心服务被设计为应用、执行和跟踪已配置、同步和/或继承的治理策略。

---

## [platform-overview] 开发生命周期

- 官方原文：https://palantir.com/docs/zh/foundry/platform-overview/development-life-cycle/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-overview-development-life-cycle.md`

# 开发生命周期

Palantir 的软件开发和产品设计方法努力在快速发展和提供客户可以依赖的稳定基础之间取得平衡。我们在保持解决客户日常面临的现实问题的同时，结合了尖端技术和框架。

实际上，这意味着 Palantir 可以与客户密切合作开发新功能。此页面概述了 Foundry 平台中功能的进展，从初始原型和开发到普遍可用。

## 开发阶段

### 实验阶段

Foundry 中的新功能始于**实验**或原型阶段。

这些是 Palantir 工程师通常与一小部分客户（通常不超过三个）合作开发的早期功能。实验功能的目标是尽快展示和验证新的功能。我们优先考虑开发速度而非长期可维护性，这使我们能够广泛探索解决方案空间。在这个开发阶段的产品预计会频繁且剧烈地变化，通常会被彻底废弃。

实验阶段的功能通常没有公开文档，并且可能不会进入 Beta 或普遍可用阶段。这是有意为之——这种开放式的实验方式在过去几年中推动了 Palantir 的一些最重要的进步，实际上 Foundry 的每个部分在其历史上的某个时刻都经历了这个阶段。

### Beta（测试版）

一旦功能的价值和方法通过一个或多个客户伙伴得到验证，就会在 **Beta** 阶段向更广泛的客户群提供。

Beta 功能的目标是大力投资于产品的长期可维护性。因此，我们缓慢地向客户推出这些功能，以便在开发过程中收集大量反馈。Beta 阶段的合作伙伴是根据他们的需求是否与已经开发的功能一致以及他们提供的反馈是否与产品最大的不确定性区域一致而选择的。

Beta 功能可能会公开记录，以帮助客户伙伴使用此早期功能，但在许多 Foundry 环境中不可用。当功能处于 Beta 阶段时，文档中会标明这一点。

Beta 功能没有保证会进展成为普遍可用，但绝大多数都会——大多数产品的不确定性在实验阶段得到解决。

### 普遍可用（GA）

**普遍可用**是用于描述 Foundry 中绝大多数功能的术语。GA 功能默认为客户启用，并构成平台的核心部分。当功能成为 GA 时，平台的其他部分可以在其基础上构建，以实现平台内的紧密集成。

在 GA 阶段，Palantir 工程师与广泛的客户群体之间存在持续的反馈循环。反馈被分类、优先排序，并被纳入 Foundry 的产品路线图中，并通过 Palantir 的 [Apollo ↗](https://www.palantir.com/platforms/apollo/) 平台快速交付给客户。

虽然 GA 功能广泛可用，但在某些情况下，您的环境可能并未启用所有功能。这是因为某些功能依赖于特定类型的基础设施，或者可能需要特定的合同协议才能启用。例如，Foundry 中的一些 GA 功能仅在 Palantir 的托管 SaaS 环境中可用，并且不支持自托管安装。

请注意，当新的功能或应用被[宣布](/docs/foundry/announcements/)为普遍可用时，可能会有一周或更长时间的延迟，才能在特定的 Foundry 注册中可用。有关功能或应用具体可用时间的详细信息，请联系您的 Palantir 代表。

除非另有说明，任何公开记录的功能都是普遍可用的。您可以依赖 GA 功能在未来得到完全支持。从平台中移除任何 GA 功能将遵循下面概述的弃用流程。

### 日落和弃用

随着开发进展，Foundry 中的现有功能或应用在某些时候可能会达到其效用或目的的终点，或被其他功能取代。功能的原始愿景可能比其已经成长到解决的问题空间更窄，或者新工具或功能可能提供了更稳健或可扩展的问题解决方法。

当先前的 GA 功能达到此阶段时，它可能会经过一个**日落**期，然后正式**弃用**。弃用的功能在平台和文档中会被特别标出。对于依赖于弃用功能的现有工作流程，集成的 [升级助手](/docs/foundry/upgrade-assistant/platform-changes/) 用于通知管理员更改并提供遵循弃用的明确截止日期。此外，对于应用级别的弃用，弃用意图和最终的弃用通知会主动与注册的平台管理员 [联系详情](/docs/foundry/administration/platform-communications/) 以及在 [Foundry 公告页面](/docs/foundry/announcements/) 上公开共享。对功能弃用的进展进行定量跟踪，以确保所有客户能够在功能最终从平台中移除之前迁移到替代方案。

## 结论

Palantir 的产品开发方法旨在实现快速功能开发和与客户的密切合作，同时确保我们的客户可以依赖 Foundry 平台中的功能作为组织数据基础设施、分析和日常运营的核心构建块。

---

## [platform-overview] 互操作性

- 官方原文：https://palantir.com/docs/zh/foundry/platform-overview/interoperability/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-overview-interoperability.md`

# 互操作性

Palantir AIP（人工智能平台）与全方位的数据系统互操作。这包括跨越传统数据、分析、治理和操作领域的工具和技术，包括边缘设备和坚固环境。消除通常在全光谱平台中发现的传统权衡，Palantir提供了一种连贯且完整的体验，同时每个功能仍然是一个独立的服务，旨在与现有或未来的技术投资连接。

## 数据互操作性

平台的每个方面都坚定地承诺开放数据格式。所有数据都以其原始格式存储，并通过标准接口访问，如REST、JDBC和安全文件系统访问。此外，所有变换后的数据默认情况下可通过开放格式访问，如parquet。这允许与现有数据平台、记录系统和现有数据架构内的其他服务进行深度连接。

除了集成，[虚拟表](/docs/foundry/data-integration/virtual-tables/)允许在现有数据系统中静止的数据连接，提供灵活的、混合的方法来管理复杂的企业数据环境。

了解更多关于这种互操作性的数据集成方法：

* 了解[数据连接](/docs/foundry/data-connection/overview/)框架。
* 探索开箱即用的数据连接[源类型](/docs/foundry/data-integration/source-type-overview/)。
* 了解如何使用[Palantir HyperAuto](/docs/foundry/hyperauto/overview/)生成开箱即用的数据管道。

## 元数据互操作性

Palantir平台提供丰富的集成模式，包括强制性（如归属、血缘）和可选性（如标签、丰富）元数据。元数据服务安全地暴露存在于项目、数据集、模型、分析、应用程序、管道编排、资源健康状况等中的所有元数据属性。这允许与现有的数据目录、元数据管理工具、主数据管理工具和现有治理架构中的其他服务进行深度连接。

了解更多关于各种类型的元数据：

* 了解[数据集元数据](/docs/foundry/data-integration/datasets/#schemas)（可通过[Python SDK ↗](https://github.com/palantir/palantir-python-sdk)访问）。
* 了解[Ontology对象类型元数据](/docs/foundry/object-link-types/object-type-metadata/)（查看[API](/docs/foundry/api/ontology-resources/object-types/get-object-type/)）。

## 语义互操作性

Palantir Ontology超越了传统的语义定义，包括驱动复杂操作的对象、链接、操作和函数的细粒度定义。组织中Ontology的所有元素都可以通过REST API访问，并通过基于JSON的创作范式进行配置。这允许与现有语义建模工具、数据目录中的Ontology和特定领域建模工具进行双向同步。

了解更多关于创建和集成Ontology：

* 查看[Ontology SDK](/docs/foundry/ontology-sdk/overview/)，了解如何在Ontology上构建应用程序和工作流。
* 了解使用[Webhooks](/docs/foundry/action-types/webhooks/)与现有事务系统集成。
* 了解在应用操作时[发送电子邮件通知](/docs/foundry/action-types/notifications/)。

## 代码与逻辑互操作性

Palantir对开放软件标准的承诺适用于数据工程、数据科学和所有其他代码驱动的创作范式。所有数据变换默认使用开放语言（如Python、Java、SparkSQL），这些语言与捆绑在平台中的开放运行时（如Spark、Flink）具有绑定。此外，所有数据科学工作流利用开放语言（如Python、R），利用相同的开放运行时，并设计为利用常见的开放格式（如ONNX）。代码库存储在高可用的git服务中，可以通过UI驱动的导出和API/编程交互安全地访问。

了解更多关于与代码和逻辑的接口：

* 查看用于数据变换的[支持语言](/docs/foundry/building-pipelines/supported-languages/)。
* 查看用于数据科学工作流的[支持语言](/docs/foundry/code-workbook/workbooks-languages/)。
* 了解[代码库](/docs/foundry/code-repositories/overview/)环境。

## 分析互操作性

Palantir平台提供全方位的分析工具来赋能用户，同时也可以与现有投资如BI和数据科学工具无缝互操作。开箱即用的连接器可用于常见系统，如Power BI®、Tableau、Jupyter和RStudio®。这些连接器使广泛的用户能够利用集成数据，同时利用最佳的数据管理、模型管理和治理。

除了数据连接器，[Code Workspaces](/docs/foundry/code-workspaces/overview/)在平台内提供了在Jupyter®和RStudio®中本地工作的无缝体验。

了解分析连接器：

* 了解[SQL & BI连接器](/docs/foundry/analytics-connectivity/overview/)如何实现与现有BI投资的集成。
* [开始使用](/docs/foundry/code-workspaces/getting-started/)在Jupyter®或RStudio®中直接与Code Workspaces合作。
* 参考Github上的[Python SDK ↗](https://github.com/palantir/palantir-python-sdk)和[R SDK ↗](https://github.com/palantir/palantir-r-sdk)，与数据科学工具集成。

## 安全互操作性

平台在平台中的所有资源上提供稳健、透明的控制。安全服务设计为利用现有的身份验证系统（如通过SAML）进行身份验证，以及现有的授权系统（如Active Directory）进行权限管理，这些权限可以跨角色、分类和目的基础的方案。通过Ontology SDK，可以灵活地扩展和管理第三方和自定义应用程序开发的权限。通过平台的REST API，可以动态和回溯地访问所有安全信息。

了解更多关于与Palantir安全服务的接口：

* 了解设置[SAML集成](/docs/foundry/authentication/overview/)进行身份验证。
* 了解Palantir如何启用[跨组织协作](/docs/foundry/security/cross-organization-collaboration/)。
* 了解[Ontology SDK](/docs/foundry/ontology-sdk/permissions/)中的权限。

***

访问[Ontology SDK](/docs/foundry/ontology-sdk/overview/)和[API文档](/docs/foundry/api/general/overview/introduction/)，了解跨全方位集成模式的更多可能性。

*Power BI®和Power BI®标志是Microsoft公司集团的商标。*
*RStudio®是Posit™的商标。*

---

## [platform-overview] 平台概览

- 官方原文：https://palantir.com/docs/zh/foundry/platform-overview/overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-overview-overview.md`

# 平台概览

Palantir AIP 在全球最关键的商业和政府环境中推动实时、AI驱动的决策。从[公共卫生 ↗](https://www.youtube.com/watch?v=1F7apO2hFXk\&list=PLmKm_LhXXgqQra-4olkIlUtsUPAchcfJv\&index=4)到[电池生产 ↗](https://www.youtube.com/watch?v=3C4_3O2Grn4\&list=PLmKm_LhXXgqRam-Dgv5UWLhGweN9nmeUp\&index=3)，组织依赖 Palantir 在其企业中安全、可靠和有效地利用AI，并[推动运营成果 ↗](https://www.youtube.com/watch?v=CmpQTrnL3ko\&list=PLmKm_LhXXgqQQGVPa4l88ExP556vDMTgF)。

简而言之，Palantir AIP 将生成性AI与运营连接在一起。与 Foundry - Palantir 的数据运营平台 - 以及 Apollo - Palantir 用于自主软件部署的任务控制平台 - 一起，AIP 是一个 *AI 网格* 的一部分，能够提供全套的AI驱动产品，从 LLM 驱动的网络应用到使用视觉语言模型的移动应用，再到嵌入本地化 AI 的边缘应用。我们将这整套能力、功能和工具称为 *Palantir 平台*。

尽管实现和扩大 Palantir 平台的运营影响力有许多因素 —— 包括 [AIP 训练营 ↗](https://www.palantir.com/platforms/aip/bootcamp/)，客户可以在短短几小时内通过 AI 实现成果 —— 关键的差异化因素是围绕 Palantir [Ontology](#the-ontology) 的软件架构。

## Ontology

Ontology 旨在表示企业中的*决策*，而不仅仅是数据。世界上的每个组织都面临如何在瞬息万变的内部和外部条件下执行最佳决策的挑战，通常是实时的。

这些决策过程的复杂性反映在 Ontology 中，它促进了与现有企业系统的深度双向互操作性。Ontology 自动将相关数据、逻辑和操作组件集成到现代化、AI可访问的计算环境中。这不仅解锁了与 AI 协作的运营应用的快速开发，还包括传统的商业智能和分析工作流。

## 决策组件

每个决策都可以分解为**数据**、**逻辑**和**操作**。

* **数据：** 形成此决策背景的相关事实或真相是什么？
* **逻辑：** 什么组织或业务规则作为此决策的护栏？在不同假设下某些结果的概率是什么？我们在以前的类似情况下做了什么，结果如何？我们的预测和优化模型的输入是什么？
* **操作：** 此决策的“动力学”或效果是什么 - 即，该决策如何在世界上体现？我们如何减少或缩短在 AIP 中做出决策与在生产环境中产生结果之间的步骤？

在 Palantir 平台中，所有这些组件都设计为促进 AI 协作模式，以释放您的操作员、分析师和主题专家的全部潜力。

### 数据

Ontology 将数据作为[对象和链接](/docs/foundry/ontology/overview/#object-and-link-types)集成，以使运营的现实世界复杂性对人类和AI都可理解。这解锁了构建*人类+AI协作*工作流的能力。

Ontology 本地支持多种数据类型以及一些扩展基元，例如用于解锁非结构化数据的[语义搜索](/docs/foundry/functions/overview-semantic-search/)、用于处理图像和视频的[媒体引用](/docs/foundry/data-integration/media-sets/#ontologize-media-using-media-references)和用于在数据中嵌入额外约束和上下文的[值类型](/docs/foundry/object-link-types/value-types-overview/)。这些是 AI 工作流开发的数据构建块，在下面的[逻辑](#logic)和[操作](#actions)部分中有更详细的描述。

此数据模型为探索结构化、非结构化、地理空间、时间序列、模拟和其他数据模式的开箱即用应用程序提供支持。这些基础工具与上下文感知的[AIP Assist](/docs/foundry/assist/overview/)相结合，大大缩短了在平台中探索和分析数据的时间。

除了应用程序构建和分析外，在 Ontology 中建模数据会自动创建一个强大的 API 网关和 Ontology 软件开发工具包（OSDK），作为企业内连接性的“运营总线”。

#### 数据连接

数据很少以干净、正确和形状良好的格式提供，以准确和可靠地向决策者展示事实。为此，Palantir 平台提供了一个可扩展的、多模式的数据连接和集成框架，能够开箱即用地与企业数据系统协作。

[Pipeline Builder](/docs/foundry/pipeline-builder/overview/) 将[LLM数据变换](/docs/foundry/pipeline-builder/pipeline-builder-llm/)的能力放入一个点击即用的包中，使使用最新的 LLMs 来支持基于管道的变换（如分类、情感分析、摘要、实体提取或翻译）变得简单。这为在 Ontology 中自动创建“提案”供操作员审查和批准奠定了基础，无需一直运行实时模型请求的滞后。（注意，正如在下面的[逻辑](#logic)部分中讨论的，这两种与模型交互的方法是高度互补的。）

此外，[Pipeline Builder](/docs/foundry/pipeline-builder/overview/)和[Code Repositories](/docs/foundry/code-repositories/overview/)中的[AIP Assist](/docs/foundry/assist/overview/)通过一个具有深度集成的 AI 合作伙伴加速数据工程，该合作伙伴不仅能访问 Palantir 文档和通用代码片段存储库，还可以为下一步操作或相关教程提供建议。

### 逻辑

如果数据定义了我们决策的背景，逻辑则封装了丰富此背景的推理和分析，使人类+AI 团队能够做出更好的决策。这可以以模型输出和可视化的形式提供额外的上下文，呈现在运营应用中，或直接融入操作的机制中。

基于这一广泛定义，定义和执行逻辑的能力贯穿于整个平台；例如，我们可以考虑[模型](#models)、[业务逻辑](#business-logic)和[模板化分析和报告](#templated-analyses-and-reports)。

#### 模型

*生成性AI、LLMs、预测、优化器等*

像 LLMs 或预测这样的模型接受参数并提供输出，以作为当前决策的背景。在数据科学家熟悉的循环中，这些模型通常经历训练和优化的迭代过程；然而，将这些模型用作生产中的运营工作流可能是一个挑战。Palantir 的建模能力可以促进模型的运营部署。

在 Palantir 平台中，模型的完整生命周期被捕获为[建模目标](/docs/foundry/model-integration/objectives/)，而模型本身的逻辑被抽象为[模型适配器](/docs/foundry/integrate-models/integrate-overview/)。这种方法意味着无论您是[在平台中训练](/docs/foundry/integrate-models/model-asset-code-repositories/)、[自行携带容器](/docs/foundry/integrate-models/container-overview/)还是[上传预训练模型](/docs/foundry/integrate-models/model-asset-files/)，各种模型都可以通过[函数](/docs/foundry/functions/functions-on-models/)绑定到 Ontology 中，以便在运营应用中进行实时交互，或者被配置为[批量部署](/docs/foundry/manage-models/set-up-batch/)并计划在数据管道中执行。

特别是对于生成性AI，Palantir 的语言模型服务提供了一个统一的界面用于多模式交互，同时抽象了特定模型和提供商的实现细节，使得在商业可用的 LLMs 领域中进行开发变得简单。为了进一步改进结果，Palantir 的[评估](/docs/foundry/logic/evaluations-overview/)工具可以让您在时间和模型之间对 LLM 的性能进行基准测试，以监控漂移并自信地进行更改。

#### 业务逻辑

*业务规则、流程映射、语义搜索*

当建模方法采用自下而上的数据训练方法时，业务逻辑通常基于治理运营领域的显性或隐性规则，自上而下进行。这些可能存在于外部系统中，Palantir 可以通过[外部函数](/docs/foundry/data-integration/external-functions/)和[Webhooks](/docs/foundry/data-connection/webhooks-overview/)直接连接这些系统以在运营工作流中进行实时交互，或通过[外部变换](/docs/foundry/data-integration/external-transforms/)进行管道连接。业务逻辑也可以直接在 Palantir 平台内使用[规则](/docs/foundry/foundry-rules/overview/)和管道构建器为数据管道中的逻辑进行编写，以及为将在运行时执行的逻辑使用 Automate 和函数。

#### 模板化分析和报告

*对象视图、分析模板、生成的报告*

逻辑不仅存在于数据科学模型中或作为硬编码业务规则；分析师通常在一次性调查、分析或报告中捕获和收集高价值逻辑。在 Palantir 平台中，您可以使用[Contour](/docs/foundry/contour/overview/)和[Quiver](/docs/foundry/quiver/overview/)等点击分析工具以及[Code Workspaces](/docs/foundry/code-workspaces/overview/)等笔记本构建分析和仪表盘。Ontology 数据模型的语义使得很容易将这些分析产品模板化并重复使用，无论是嵌入在[对象视图](/docs/foundry/object-views/config-overview/)或[Workshop应用](/docs/foundry/workshop/module-interface/)中，还是作为独立[仪表盘](/docs/foundry/notepad/widgets-quiver-dashboard/)展示。这些对象视图、模板化分析和仪表盘可以插入运营应用中，提供一目了然的见解以指导决策，同时提供进一步临时探索的途径。

总之，这三个逻辑方面——模型、业务逻辑和模板化分析及报告——提供了一个工具箱或调色板，用户可以从中自由组合，为决策者在关键时刻提供所需的所有上下文。

### 操作

为了使任何决策产生影响，该决策必须传播到世界中。这就是操作定义企业“动词”的地方 - 也就是所做的事情 - 并控制人类操作员或 AI 代理如何确保其决策持续存在，无论是在 Ontology 数据模型中还是通过与[外部系统](/docs/foundry/action-types/side-effects-overview/)的交互。此外，在 Ontology 中捕获决策结果允许用户将特定决策与未来数据中的结果观察配对。这使得反馈循环成为可能，将未来的决策置于过去选择的背景中，并可以用于重新训练或微调模型，或者仅仅支持操作员更清晰地了解过去。

在 Ontology 中表示这些“动力学”的原子单位是[操作](/docs/foundry/action-types/overview/)，它提供了特定、细粒度的控制用于更改或创建数据，以及用于在外部系统中协调更改。可以通过一个点击配置界面简单地定义基本操作。可以通过[函数支持的操作](/docs/foundry/action-types/function-actions-overview/)和[Ontology 编辑 TypeScript API](/docs/foundry/functions/api-ontology-edits/)指定任意复杂的操作。操作也可以在[Ontology 软件开发工具包](/docs/foundry/ontology-sdk/overview/)（OSDK）和[平台API](/docs/foundry/api/ontology-resources/actions/action-basics/)中打包，以便自定义应用开发和现有第三方工具可以轻松且安全地写回到 Ontology。

每个操作的[权限](/docs/foundry/action-types/permissions/)确定哪个用户或代理在什么条件下能够执行操作，为安全、可审计和透明的控制奠定了基础。

在复杂、紧密耦合的环境中，如供应链或制造车间，一个小的变化可能会引起级联效应，产生意外或意图之外的结果。[场景](/docs/foundry/vertex/scenarios-overview/)原语允许用户通过对 Ontology 的一个分支进行更改来预测这些后果，有效地创建一个沙盒宇宙，在这个宇宙中可以对潜在变化进行预测、业务流程模型和其他分析。[Vertex](/docs/foundry/vertex/overview/)应用专门用于这种过程可视化和情景测试；[Workshop](/docs/foundry/workshop/scenarios-overview/)应用构建器本地支持情景用于开发包含“假如...”工作流的运营应用。

这些原语为安全开发在生产工作流中操作的人类+AI 团队创造了环境。操作的细粒度权限和访问控制提供了一个“控制平面”，其中代理被沙盒化，具有对其可以使用的数据和工具的特定限制。在大多数模式中，AI 代理不是直接进行更改，而是通过与[集成到 Workshop 的 AIP Logic](/docs/foundry/logic/overview/)函数的直接集成同步创建提案，或通过[Automate](/docs/foundry/automate/overview/)或[Pipeline Builder 中的 Use LLM](/docs/foundry/pipeline-builder/pipeline-builder-llm/)节点异步创建提案。生成的提案然后可以呈现给操作员以进行改进、反馈和最终决策。此基于提案的模式，除了加强“人类在回路中”范式外，还生成了有价值的元数据，使代理能够在持续反馈的情况下学习和发展。

## 接下来是什么？

体验 AIP 威力的最佳方式是开始构建。阅读[入门](/docs/foundry/getting-started/overview/)指南以获取更多信息，或者 - 如果您可以访问平台 - 只需询问 AIP Assist 根据您的目标建议从何处开始。

有关这些决策组件如何交互以指导工作流开发的更多信息，请参阅关于[提炼功能需求](/docs/foundry/use-case-life-cycle/distilling-functional-requirements/)的讨论，在[应用案例开发](/docs/foundry/use-case-life-cycle/overview/)中讨论，或在[AIP Now 展示 ↗](https://aip.palantir.com/)中找到行业特定的端到端工作流示例。

此外，您可能会对了解 AIP 的构建方式以及如何与您组织中的现有投资集成感兴趣：

* [架构](/docs/foundry/platform-overview/architecture/)
* [互操作性](/docs/foundry/platform-overview/interoperability/)
* [开发生命周期](/docs/foundry/platform-overview/development-life-cycle/)

## 平台能力

文档的其余部分被组织为[平台能力](#platform-capabilities)的集合。每个能力的摘要如下：

* [数据连接和集成](#data-connectivity-and-integration)
* [模型连接与开发](#model-connectivity-and-development)
* [Ontology 构建](#ontology-building)
* [应用案例开发](#use-case-development)
* [分析](#analytics)
* [产品交付](#product-delivery)
* [安全与治理](#security-and-governance)

### 数据连接和集成

Palantir 提供了一个可扩展的、多模式的数据连接框架，能够开箱即用地连接到企业数据系统并提供：

* 对现有数据湖和平台的就地、零复制访问；
* 一个基于 Kubernetes 的自动缩放数据构建系统，适用于批量和流式管道；
* 集成的管道调度和编排；
* 所有数据流的本地健康检查；以及
* 涵盖基于角色、分类和目的的访问控制的全面安全功能。

### 模型连接与开发

Palantir 提供一个集成的、端到端的模型开发环境（如，Python 和 R）；灵活集成使用行业标准工具集构建的外部模型；为所有开发或集成的模型提供受管路径到生产；以及一个用于持续评估部署模型的“任务控制”。架构目标是为企业中的所有业务逻辑和建模提供连接路径，无论给定的资产是在何处训练、测试和/或托管。

### Ontology 构建

如上所述，为了创建一个综合的决策中心企业模型，Ontology 集成了：

* *数据*，作为[对象和链接](/docs/foundry/ontology/overview/#object-and-link-types)；
* *逻辑*，作为[模型](/docs/foundry/model-integration/overview/)和[函数](/docs/foundry/functions/overview/)；以及
* *操作*，作为平台[操作](/docs/foundry/action-types/overview/)。

Ontology 的这些构建块使运营的现实世界复杂性对操作者和AI都可理解，解锁了构建混合人类-AI工作流的能力。额外能力包括：

* 从最终用户捕获数据回到语义基础的结构化机制；
* 用于在结构化、非结构化、地理空间、时间序列、模拟和其他范式中探索 Ontology 的开箱即用应用；以及
* 利用 Ontology 作为企业各个部分的“运营总线”的 Ontology 软件开发工具包（OSDK）。

### 应用案例开发

Palantir 的应用开发框架使企业能够构建运营工作流并开发应用案例，利用用户操作、警报和其他终端用户前线功能与工具使用、数据感知的 AIP 代理进行协作。

应用案例开发能力包括：

* 与 AIP Logic 集成以构建自定义工作流代理；
* AI 辅助、低代码/无代码应用程序构建，自动化安全实施以及底层存储和计算的管理以及数据和模型绑定；
* 具有实时预览的应用开发框架；以及
* 允许与企业进行全方位集成的 API、webhooks 和其他接口。

### 分析

平台为每种类型的用户提供分析能力，无论他们是否会编程。能力包括点选和基于代码的工具，能够进行基于表格的分析、自上而下的可视化分析、地理空间分析、时间序列分析、情景模拟等。

Palantir 的分析套件超越了传统的“只读”范式，将数据写回 Ontology，在统一的安全性、血统和治理模型中生成有价值的新见解。

平台还与常用建模环境（支持使用[Code Workspaces](/docs/foundry/code-workspaces/overview/)的 JupyterLab® 和 RStudio® Workbench 的本地使用）和商业智能平台（包括 Tableau® 和 PowerBI® 的[专用连接器](/docs/foundry/analytics-connectivity/overview/)）互操作。

### 产品交付

Palantir 平台提供 DevOps 工具来打包、部署和维护在平台中构建的数据产品。这些产品交付能力包括一个包装界面，用于创建由平台资源集合（管道、Ontology、应用程序、模型等）组成的“产品”；用于产品发现和安装的市场前台；以及通过自动升级、维护窗口等管理产品安装的能力。

### 安全与治理

Palantir 平台具有全面的、最佳实践的安全模型，该模型传播到整个平台，并且默认情况下，与信息同行无论其走向何处。能力包括：

* [所有数据的加密](/docs/foundry/security/overview/#enterprise-security)，无论是在传输中还是在静止时；
* 身份验证和身份保护控制；
* 授权控制可以结合基于角色、权限标记和目的驱动的范式；
* 强大的安全[审计日志](/docs/foundry/security/audit-logs-overview/)；以及
* 高度可扩展的信息治理、管理和[隐私控制](/docs/foundry/security/protecting-sensitive-data/)。

### 管理与支持

平台管理员可以访问一套强大的工具来管理 Palantir 平台。平台管理的核心应用是：

* [控制面板](/docs/foundry/administration/control-panel/)
* [资源管理](/docs/foundry/resource-management/overview/)
* [升级助手](/docs/foundry/upgrade-assistant/overview/)

平台管理员和项目经理还可以访问促进用户支持的资源，例如[AIP Assist](/docs/foundry/assist/overview/)。这些资源在[管理与支持文档](/docs/foundry/administration/overview/)中进行了描述。

---

## [platform-security-management] 管理组织和空间

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management.md`

# 管理组织和空间

## 组织

组织权限应通过[控制面板](/docs/foundry/administration/enrollments-and-organizations/)进行管理。进一步的组织配置在 Foundry 设置选项卡中进行管理。

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

客人成员资格将允许您查看将此组织作为主要组织的用户，但不能查看此组织的其他客人用户。将此作为主要组织的用户始终可以查看此组织的客人用户。

您可以从 Foundry **设置**页面的组织选项卡中向您的组织添加客人：

### 主页文件夹和组织

启用 Foundry 主页文件夹时，它们会自动标记为用户的组织。

禁用主页文件夹的配置选项目前处于测试阶段。请联系 Palantir 支持以启用此功能。

## 空间

**空间**已经从其以前的名称**命名空间**重新命名。

空间设置在[控制面板](/docs/foundry/administration/enrollments-and-organizations/)的**空间**选项卡中进行管理。

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

---

## [platform-security-management] 从“忽略继承权限”设置迁移并禁用

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/disabling-ignore-inherited-permissions/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-disabling-ignore-inherited-permissions.md`

# 从“忽略继承权限”设置迁移并禁用

自2023年6月起，大多数客户将无法使用“忽略继承权限”安全设置。仍然使用已弃用“忽略继承权限”功能的客户强烈建议按照以下指南迁移到使用[项目](/docs/foundry/security/projects-and-roles/)和[权限标记](/docs/foundry/security/markings/)，这些提供了更好的安全性可读性和管理。

## 概述

当平台上的文件夹或文件启用“忽略继承权限”设置时，所有对这些文件夹或文件（以及其中的子文件夹和文件）的权限将被撤销，除非它们被明确添加到文件夹或文件中。例如，授予用户在项目上的`只读`权限不会自动授予该用户在启用“忽略继承权限”的文件夹上的`只读`权限。

在禁用“忽略继承权限”设置时，我们建议将文件夹或文件内容移动到具有您需要的特定权限的另一个[项目](/docs/foundry/security/projects-and-roles/)，或者用[权限标记](/docs/foundry/security/markings/)替换文件夹或文件。项目和权限标记是首选工具，因为与“忽略继承权限”设置不同，它们清晰地定义了查看底层数据所需的要求。

以下是迁移出“忽略继承权限”设置的步骤摘要：

1. 在[升级助手](/docs/foundry/upgrade-assistant/overview/)应用中开始，并选择需要迁移的文件夹或文件。
2. 完成文件夹或文件上的任何必需更新。
3. 考虑您的迁移选项，并决定哪种最适合您的情况。
4. 执行迁移。
5. 禁用文件夹或文件上的“忽略继承权限”。
6. 返回升级助手，并确认不再有与此文件夹或文件对应的待处理操作。

## 迁移步骤

### 1. 升级助手

进入Foundry的升级助手应用，并导航到启用“忽略继承权限”的特定文件夹或文件。选择该文件夹或文件以开始迁移过程。

### 2. 完成所需更新

如果看到“需要更新”通知，选择**更新**。这样做将把禁用“忽略继承权限”设置的过程与禁用和迁移出“传播查看要求”设置的附加要求分开。了解有关此[附加必需迁移](/docs/foundry/platform-security-management/disabling-propagate-view-requirements/)的更多信息。

### 3. 选择迁移方式

有多种不同的方法可以迁移出使用“忽略继承权限”设置。您选择的方法取决于数据的敏感性、平台上已有的项目和权限标记，以及企业的安全架构。以下是迁移选项列表，以及您应该问的问题，以帮助决定下一步：

* \*\*禁用权限：\*\*此文件夹或文件是否需要与其父项目分开的权限？是否由于不再相关的遗留原因启用了“忽略继承权限”？如果是这样，您可以禁用“忽略继承权限”。
* \*\*移动到另一个项目：\*\*是否存在使用您在此文件夹或文件上实施的更严格权限的其他项目？目标项目是否有类似的用户集？如果是这样，您可以将此文件夹或文件的内容移动到现有的项目中。
* \*\*创建新项目：\*\*这些数据是否需要其不存在的空间？此文件夹是否已增长到足以从其自身项目中受益？如果是这样，考虑创建一个新项目并将文件夹或文件移至其中。
* \*\*应用现有权限标记：\*\*数据是否敏感，并且是否存在语义上代表该数据的现有权限标记？您是否希望对这些资源进行下游保护？如果是这样，考虑在此文件夹或文件上应用现有权限标记。
* \*\*创建新权限标记：\*\*此文件夹或文件中的数据是否敏感且独特？您是否希望对该文件夹或文件的内容进行下游保护？如果是这样，考虑创建新的权限标记并将其应用于文件夹或文件。

### 4. 完成迁移

以下是执行上述迁移选项的说明。

#### 移动到另一个项目

在将文件夹或文件的内容移动到另一个项目之前，请查看目标项目的权限。您可能需要向目标项目添加更多用户，以反映启用“忽略继承权限”设置的文件夹和文件的原始安全设置。

要将文件夹或文件的内容移动到另一个项目，您需要在目标项目上至少具有`编辑者`权限。突出显示资源，然后右键单击并选择**移动**。有关详细说明，请查看我们的[移动和共享项目资源](/docs/foundry/projects/move-and-share-resources/)文档。

#### 创建新项目

要创建新项目，请按照步骤[创建项目](/docs/foundry/projects/create/)。您应该在项目上指派权限，以便原始文件夹或文件的用户与启用“忽略继承权限”设置的用户具有相同的权限集。这样做将确保没有人失去对这些资源的访问。

要[移动文件夹或文件的内容](/docs/foundry/projects/move-and-share-resources/#move-resources)到此新项目，突出显示资源，然后右键单击并选择**移动**。

#### 应用现有权限标记

将使用“忽略继承权限”设置访问文件夹或文件的所有用户添加为现有权限标记的成员。这确保没有人在迁移后失去访问权限。

一旦用户被添加为现有权限标记的成员，他们可能会看到在平台上应用此权限标记的任何数据。

在应用现有权限标记之前，请查看[应用权限标记的步骤](/docs/foundry/platform-security-management/manage-markings/#apply-markings)。考虑应用权限标记的下游影响，并可能锁定下游用户。当您准备好时，将权限标记应用于启用“忽略继承权限”设置的文件夹或文件。

#### 创建新权限标记

首先，[创建新的权限标记](/docs/foundry/platform-security-management/manage-markings/#create-markings)。然后，将对启用“忽略继承权限”设置的文件夹或文件具有访问权限的所有用户添加为此新权限标记的成员。这确保没有人在迁移后失去访问权限。

类似于[应用现有权限标记](#apply-an-existing-marking)，在应用权限标记之前，请查看有关如何[应用权限标记步骤](/docs/foundry/platform-security-management/manage-markings/#apply-markings)的文档。

### 5. 在文件夹或文件上禁用“忽略继承权限”

完成迁移后，请确保在最初应用的文件夹或文件上禁用“忽略继承权限”。您可以在文件夹或文件视图的右侧面板的**设置**标签中找到此选项。确认迁移完成后再禁用。如果所讨论的资源是一个没有剩余内容的文件夹，您很可能可以删除该文件夹。

禁用后，您将无法重新启用“忽略继承权限”设置。

### 6. 确认操作完成

返回升级助手，并确认不再有与此文件夹或文件对应的待处理操作。

---

## [platform-security-management] 从“传播查看要求”设置迁移并禁用

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/disabling-propagate-view-requirements/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-disabling-propagate-view-requirements.md`

# 从“传播查看要求”设置迁移并禁用

自2023年6月起，大多数客户将禁用使用“传播查看要求”安全设置。强烈建议仍在使用已弃用的“传播查看要求”功能的客户遵循以下指南，以[项目](/docs/foundry/security/projects-and-roles/)和[权限标记](/docs/foundry/security/markings/)取代这种用法，以提高安全性可读性和管理。

## 概述

当在项目上启用“传播查看要求”设置时，项目中的每个数据集都要求用户具有访问权限，以查看其下游数据集，无论它们位于此项目内还是不同的项目中。

我们建议禁用“传播查看要求”设置，并在必要时用权限标记替代。与“传播查看要求”设置不同，权限标记更清晰地定义了查看底层数据所需的要求。如果只有一些数据集包含敏感数据，请考虑为这些特定数据集添加适当的权限标记。如果整个项目都是敏感的，请在项目级别添加权限标记。

以下是迁移离开“传播查看要求”设置的步骤概要：

1. 在[升级助手](/docs/foundry/upgrade-assistant/overview/)应用中开始，并选择需要迁移的项目。
2. 考虑您的迁移选项，并决定哪种方法最适合您的情况。
3. 执行迁移。
4. 在项目上禁用“传播查看要求”。
5. 返回升级助手，确认不再有与此项目对应的待处理操作。

## 迁移步骤

### 1. 升级助手

进入Foundry中的升级助手应用，选择启用了“传播查看要求”的特定项目以开始迁移过程。

### 2. 选择如何迁移所选项目

有几种不同的方法可以从使用“传播查看要求”设置中迁移。您选择的方法取决于数据的敏感性、平台上已有的项目和权限标记，以及企业的安全架构。以下是迁移选项和帮助您决定下一步的问题清单。由于您的决定可能对隐私有重大影响，我们强烈建议阅读所有提供的选项。

#### 分类敏感数据

首先，确定项目是否包含敏感数据。背景很重要；某些数据是否被视为敏感取决于相关的隐私法规和贵组织的标准。

在Palantir中，敏感数据被定义为任何被广泛分类和/或需要额外安全的数据。一些法律正式指定特定数据元素为敏感（例如，[欧盟的一般数据保护条例](https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en)），而其他数据由数据所有者或无论法律地位如何的普遍认可决定（如社会安全号码）。数据是否被分类为敏感通常取决于数据的类型或分类（例如，个人可识别信息（PII）），工作流程的类型（如那些仅限于特定目的的工作流程），或可能触发受限访问控制的任何内容（包括敏感的企业信息）。

如上所述，常见的敏感数据示例之一是个人可识别信息（PII），其中包括直接标识符和其他可用于重新识别或识别个人的信息。

在这里，您应识别限制访问项目中的数据应限制访问从中派生的任何下游数据集、对象或资源的情况。如果项目中的数据没有PII属性，您可以跳到[在项目上禁用“传播查看要求”设置](#4-disable-propagate-view-requirements-on-the-project)。

如果项目中存在数据敏感性，请对其进行分类。例如：“此项目中的数据集X、Y和Z包含PII，而此项目中的数据集A、B和C包含财务信息”。

#### 验证是否对敏感数据应用了权限标记

[权限标记](/docs/foundry/platform-security-management/manage-markings/#use-markings)是Foundry中的一种安全控制，用于定义限制用户可见性和操作的资格标准。

与“传播查看要求”设置相似，[权限标记](/docs/foundry/security/markings/)是一种安全原语，会传播到下游数据集和资源。在考虑是否可以安全地关闭此项目的“传播查看要求”设置时，我们建议检查此项目中的敏感数据是否已被适当的权限标记保护。如果是这种情况，可能适合关闭“传播查看要求”。

使用[数据沿袭](/docs/foundry/security/checking-permissions/#data-lineage)应用程序验证数据集上的权限标记。首先，将项目中的一个或多个数据集添加到图中。然后，选择**权限**节点着色选项。受权限标记保护的资源旁边会在图上显示盾牌图标。选择一个节点，然后在右侧边栏中选择**访问信息**以展开有关该节点上的权限标记的详细信息。

例如，如果您确定启用了“传播查看要求”设置的项目仅包含一个敏感数据类别（PII），并且PII权限标记已应用于项目中每个相关数据集（无论是直接应用还是通过数据依赖关系或文件层次结构继承），那么“传播查看要求”设置可能是多余的，可以安全地[为项目禁用](#4-disable-propagate-view-requirements-on-the-project)。

#### 确定数据敏感性是否在上游或此项目内引入

如果项目包含敏感数据，并且该数据尚未被[权限标记](/docs/foundry/security/markings/)保护，那么我们建议在禁用“传播查看要求”设置之前应用权限标记，以确保下游数据持续受到安全控制的传播保护。

然而，项目不一定是对数据应用权限标记的正确位置。

##### 示例

在下面的示例中，项目中一个启用了“传播查看要求”设置的敏感数据集没有应用权限标记。然而，该敏感数据集实际上是从上游数据集派生的。

**方法1（错误）：** 如果您直接对项目中的敏感数据应用权限标记，上游数据将不会被正确标记；这会影响安全性可读性。

**方法2（推荐）：** 如果您改为对\_上游\_数据应用权限标记，那么权限标记将自动传播到此项目中的数据；两个数据集都将被正确标记。

如果您的项目中的任何敏感数据应受权限标记保护，我们建议尽可能在上游保护这些数据，以确保敏感数据在平台中的任何地方都能得到一致保护。请确保采取适当的上游操作，然后再返回您的项目并继续迁移。

#### 适当时重用现有权限标记

如果您的项目是某些敏感数据的起源（最上游位置），并且数据未受到权限标记保护，那么项目可能是对数据应用权限标记作为“传播查看要求”设置替代的正确位置。对于每个敏感数据类别，[验证平台上是否已存在](#verify-if-markings-are-applied-to-sensitive-data)正确表示此数据的权限标记。

从数据治理的角度来看，如果数据是PII，并且平台上已有PII权限标记，我们建议应用现有权限标记，而不是创建第二个PII权限标记；这确保用户授权可以在单个地方进行管理。

记录您计划重用的权限标记的决定，然后[继续迁移](#3-complete-migration)。

#### 创建新的权限标记

如果项目中敏感数据类型没有合适的权限标记，请考虑创建新的权限标记。这只有在以下情况成立时才有必要：

* 项目中的数据是独特的，没有现有的权限标记可以使用。
* 数据源于项目；如果不是，则应将权限标记应用于派生数据的上游数据集。

记录您的决定并按照以下部分中的步骤完成迁移。

### 3. 完成迁移

以下部分描述了在讨论的选项下如何完成迁移。

#### 禁用“传播查看要求”

无需操作。继续[4. 在项目上禁用“传播查看要求”](#4-disable-propagate-view-requirements-on-the-project)。

#### 应用现有权限标记

将项目中某个特定类别的敏感数据集（例如，包含PII的数据集）访问权限的所有用户添加为现有权限标记（PII）的成员。这确保在迁移后不会有人失去对项目的访问权限。注意，一旦用户被添加为现有权限标记的成员，他们可能会看到在整个平台中应用了该权限标记的任何数据。

在应用现有权限标记之前，请查看[应用权限标记](/docs/foundry/platform-security-management/manage-markings/#apply-markings)的步骤。考虑应用权限标记的下游影响，并可能锁定其他下游用户。

准备就绪后，将权限标记应用于需要它的资源集。如果项目中只有一个敏感数据类别且所有数据都属于该类别，则将权限标记应用于项目本身。否则，直接应用权限标记到敏感数据集或它们的父文件夹（如果它们位于同一位置）。

#### 创建新的权限标记

首先，[创建新的权限标记](/docs/foundry/platform-security-management/manage-markings/#create-markings)。然后，将应有权访问其描述的数据的所有用户和/或组添加为此新权限标记的成员。这确保在迁移后不会有人失去访问权限。

在尝试应用任何权限标记之前，请查看[应用权限标记的步骤](/docs/foundry/platform-security-management/manage-markings/#apply-markings)。

### 4. 在项目上禁用“传播查看要求”

在为项目中的多种敏感数据类型[完成迁移](#3-complete-migration)后，确保从项目视图右侧面板的**设置**选项卡中禁用“传播查看要求”设置。

禁用后，您将无法重新启用“传播查看要求”设置。

### 5. 确认操作完成

返回升级助手，确认不再有与此项目对应的待处理操作。

---

## [platform-security-management] 管理组

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-groups/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-groups.md`

# 管理组

在侧边栏的**平台设置**部分，选择**组**。选择一个组以在仪表盘视图中查看其详细信息。

您可以查看所选组的各种信息：

* **组名称：**我们建议不要更改组名称，尽管具有管理权限的用户可以这样做（请参阅下文的**重命名组**）。
* \*\*组描述：\*\*描述组，并对可以发现该组的组织中的所有用户可见。
* \*\*组ID：\*\*组的永久唯一ID。
* \*\*组类型：\*\*组的类型；外部、内部或[基于规则](/docs/foundry/authentication/group-assignment/)。内部领域组成员资格在Foundry中管理。
* \*\*领域：\*\*认证来源，外部或内部。对于外部组，领域标识管理该组的提供者。
* \*\*组织：\*\*定义可以看到该组及其描述的组织成员。
* \*\*成员：\*\*属于该组的用户。这些可以是单个用户或组。
* \*\*组权限：\*\*定义有权限管理组各方面的用户。有两种类型的管理权限：
  * \*\*管理权限：\*\*可以授予权限以管理组各方面、管理其成员及编辑其元数据的用户。
  * \*\*管理成员资格：\*\*可以管理组成员，包括成员资格到期属性的用户。
* \*\*属性：\*\*以键值格式存储的关于组的信息，通常由其他Foundry服务使用。

您只能查看您在组的组织中拥有`查看组成员资格`权限的组。此权限可以通过**设置 > 平台设置 > 组织**，选择感兴趣的组织，然后选择**管理**以获取**组织权限**来授予。这将显示用户和组的列表以及一个搜索框；对于已添加的用户和组，使用下拉框启用**查看组成员资格**选项。

## 成员资格到期

如果您可以`管理`某个特定组的成员资格，您可以要求新加入该组的成员资格是临时的。通过配置以下组属性来实现：

* \*\*最新到期：\*\*所有新成员资格必须在该日期之前到期。
* \*\*最大时长：\*\*所有新成员资格必须在指定的时长内到期。

可以同时设置这些属性中的一个或两个。当两者都设置时，最新允许的到期将是两者中限制性最强的属性。

此外，如果您拥有`管理成员资格`权限，您可以将临时成员添加到具有成员资格到期日期属性的组中。您可以将这些临时成员添加到没有设置`最新到期`或`最大时长`属性的组中。

任何[访问请求](/docs/foundry/approvals/overview/#requests)导致对具有`最新到期`或`最大时长`属性的组的成员资格请求将受到最大到期的限制。

### 成员资格到期通知

当临时组成员资格到期时，会向受影响的用户发送撤销通知。此外，具有临时成员资格的用户将在其成员资格到期前七天收到提醒通知。然而，如果用户被添加到到期设置少于七天的组中，他们将不会收到提醒通知。

如果用户不希望接收这些通知，他们可以在平台侧边栏的**帐户 > 设置 > 通知**中配置平台通知设置。

## 自定义审批访问请求策略

自定义策略处于测试阶段，可能不适用于您的注册。如果您想启用此功能，请联系Palantir客服支持。

具有`管理成员资格`或`管理权限`权限的用户可以为组配置自定义策略，这些策略将应用于任何导致对所选组的成员资格请求的[访问请求](/docs/foundry/approvals/overview/#requests)。这可以通过如下所示的**成员资格审批**部分进行配置：

如果组配置了自定义策略，则任何导致该组请求的访问请求将受到影响。自定义策略将应用于`组成员资格`子任务以将成员添加到特定组。为了批准访问请求，所有子任务都必须获得批准。审批策略在请求访问时和审核现有访问请求时都会进行传达。

## 项目访问

选择**项目访问**选项卡旁边的**详细信息**选项卡以查看所选组的项目访问详细信息。

**项目访问**视图允许组管理员查看组可以访问的所有项目以及授予组的特定项目角色。当决定添加或移除用户时，此视图尤其有用，因为您可以看到访问权限将如何改变。

**显示继承权限**切换默认是`打开`的，并将遍历所有嵌套的组以查找组可以访问的项目。如果您将此切换`关闭`，则列表只会显示直接应用于该组的项目。

## 重命名组

具有`管理成员资格`权限的用户可以重命名组。当用户重命名组时，一些操作会自动发生：

* 当前组将被重命名，组ID将保持不变。
* 将创建一个具有原始名称的新组，以支持可能依赖于原始组名称的应用程序。
* 原始组将成为新重命名组的成员。

## 设置和使用组联系详情

您可以为可供用户查看的每个项目指定联系详情。这被视为项目或项目中认可文件的联系点。通过选择一个组为项目指定联系详情，并在项目以及其中的所有认可数据集中显示。

<img src="./media/contact-information-email.png" alt="文件的联系信息" width="350" />

要为项目设置联系详情，首先确保该组具有联系详情。为此，选择该组，然后在页面的**联系详情**部分中选择**管理**。管理联系详情需要您具有更改组的权限。您可以定义该组是否应该通过Foundry Issues或电子邮件进行联系。

<img src="../../foundry-docs/platform-security-management/media/set-contact-details.png" alt="为组设置联系详情" width="450" />

一旦保存了联系信息，您可以将此组设为某个项目的联系点。通过侧边栏的**项目和文件**导航到项目，然后在**操作**菜单中选择**编辑项目联系**并选择所需的组。如果您希望选择的组未显示，请首先确认它已设置联系详情。

<img src="./media/edit-project-contact.png" alt="为项目设置联系详情" width="550" />

## 应用组权限

从**组详细信息**仪表盘访问**组权限**视图。具有管理权限的用户可以使用此部分将访问权限授予组而不是单个用户，以使权限更加透明和可审计。

授予组权限在为项目指派权限时特别有用，因为管理员可以通过上面提到的项目访问选项卡查看组可以访问哪些项目。我们建议项目设置至少有三个组，每个默认角色一个：只读、编辑者和所有者。您应该将项目默认角色设置为发现者。

## 限制视图组名称策略

当创建使用*组名称*作为其中一个策略术语的限制视图时，您需要指定组的领域，以便可以相应地匹配组名称。您可以在**平台设置 > 组**界面中检查组领域，并在限制视图规则编辑器的底部更改领域名称。

## 领域

### 用户领域

管理员通常在控制面板中设置外部领域提供者（例如SSO、SAML领域或ADFS）。如果需要，Foundry的**平台设置**提供了身份提供者的内部实现。这种内部身份提供者可以在外部认证系统不适用的多种场景中使用。

#### 组外部领域

外部领域是直接从外部系统（如ADFS等身份提供者）派生的组。平台设置配置定义了分配身份提供者的领域。

外部领域无法在Foundry中修改，处于只读状态。只能在外部系统中执行的操作包括重命名、将用户添加到组、修改属性和创建新组。外部领域组非常适合Foundry中的大多数授权和认证相关功能，包括：

* 指派自由和强制性控制，以及
* 启用对平台的二进制访问（例如允许或拒绝属于特定组的一组用户）。

由于外部领域组处于只读状态，用户将无法在Foundry中请求加入外部领域组的访问。然而，在[控制面板](/docs/foundry/administration/overview/)中，您可以配置用户尝试请求外部领域组访问时收到的消息。导航到**控制面板 > 身份验证 > 您的SSO > SAML > 管理 > 属性映射 > 外部组管理**以设置外部领域的自定义消息和URL。只有与外部领域相同领域的用户会看到自定义消息和URL。下面是一个管理员向其内部Jira实例添加消息和链接的示例。

配置自定义消息后，当查看该外部领域中的所有组时，您将在平台设置中看到此消息。

当用户尝试请求对授予该组角色的项目的访问时，他们将看到该消息。

最后，您可以在登录时使用外部领域组进行组织分配。通常，通过客户SSO获得的信息成为在登录时将用户分类到不同组织的输入。

所有外部领域组必须被指派一个组织。如果没有指派组织，该组将对所有用户可见，无论其组织如何。

#### 组内部领域

在Foundry中创建的组被指派到内部领域。

内部领域组可以在Foundry中进行修改。在**组**界面中可以执行的操作包括重命名、将用户添加到组、修改属性和创建新组。内部领域组是授予Foundry级别功能访问权限的理想选择，包括将服务用户帐户捆绑到内部领域组以进行白名单或黑名单处理（例如，将服务用户帐户排除在用户帐户到期规则之外）。

如果正在使用外部领域组，那么重要的是避免直接将用户指派到内部领域组。相反，用户被添加/移除的外部领域组应嵌套在内部领域组中。

---

## [platform-security-management] 管理权限标记

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-markings/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-markings.md`

# 管理权限标记

在 Foundry 设置的权限标记部分中管理权限标记。权限标记随后应用于整个平台的资源。

## 创建权限标记类别

一旦创建，权限标记类别无法删除。

管理员用户可以创建权限标记和权限标记类别，并控制其元数据、可见性和成员资格。访问平台设置的权限标记部分需要特殊的权限。

如果您是具有必要权限的管理员用户，可以通过单击平台设置的权限标记部分中的 **新建权限标记类别** 按钮来创建权限标记类别。

创建权限标记类别时，您可以设置[类别可见性](#category-visibility)并指派类别权限。默认情况下，类别创建者将是管理员。类别创建者可以选择将自己从创建者中移除，并添加其他管理员。

### 类别可见性

权限标记的可见性是基于每个类别分配的，组织类别除外。各个组织都有自己的可见性设置。

在大多数情况下，权限标记和类别的名称和描述不是敏感信息，即使是没有权限标记访问权限的用户也应该可见。此行为由类别可见性决定，默认情况下为`可见`。

如果类别可见性设置为`可见`，组织中的所有用户都可以在权限标记界面中看到该类别及其权限标记的存在。如果用户不符合权限标记权限，他们将无法看到权限标记或类别的存在。

如果权限标记类别可见性为`隐藏`，则该类别及其权限标记的存在被视为敏感信息。`隐藏`类别可以对未明确授予`类别访客`权限的所有用户不可见。

权限标记类别确保这些可见性规则：

* 可见性是为一个类别及其所有权限标记共同定义的；不能在每个权限标记的基础上分配。
* 所有有权限标记访问权限的用户可以查看类别的存在及其类别内所有其他权限标记。这些用户不会在API结果中显示为“类别访客”，但应被假设为存在。
* 所有在权限标记上有角色（管理员、移除者）的用户可以查看类别及其类别内所有权限标记的存在。这些用户不会在API结果中显示为“类别访客”，但应被假设为存在。
* 所有在类别上有角色（管理员、访客）的用户可以查看类别及其类别内所有权限标记的存在。

### 类别权限

用户可以拥有指定他们如何与权限标记类别交互的权限：

* **类别管理员：** 用户可以更改类别的描述和权限，并在类别中创建权限标记。
* **类别访客：** 用户可以看到类别及其所有权限标记的存在。

### 按组织限制类别

权限标记类别可以限制为单个组织，以确保它永远不会对该组织外的用户可见。

## 创建权限标记

一旦创建，权限标记无法删除或移动到不同的类别。

如果您是具有必要权限的管理员用户，可以通过单击平台设置的权限标记部分中的 **新建权限标记** 按钮来创建新的权限标记。然后可以指派权限标记管理员和权限标记移除者。

当您在 Foundry 中创建权限标记时，您会自动获得“管理权限”访问权限。我们建议在新权限标记上指派不同的团队成员这些权限。这样，您可以避免依赖单个管理员来管理所有权限标记权限。

### 权限标记权限

当您创建新的权限标记时，可以添加具有不同访问级别和权限的用户和组：

* **管理权限：** 用户可以授予权限以管理此权限标记、其成员和其元数据。
* **应用权限标记：** 用户可以将此权限标记应用于项目和资源。此权限仅授予应用权限标记的能力，并不授予权限标记的成员资格。
* **移除权限标记：** 用户可以从项目和资源中移除此权限标记。要移除权限标记，用户还必须能够应用权限标记。
* **成员：** 用户可以查看受此权限标记保护的资源和项目。

以上所有权限都是独立的，并不会自动为用户提供成员权限。例如，用户可以在权限标记上拥有“应用权限标记”和“管理权限”访问权限，但不是权限标记的成员。在这种情况下，用户可以将权限标记应用于平台中的文件、文件夹和项目，并管理权限标记，但无法看到用该权限标记标记的数据。

### 向用户授予权限标记

权限标记以全局方式授予用户。用户被授予权限标记后，用户被全局授权查看该权限标记限制的内容类型。但是，拥有权限标记的访问权限并不意味着用户可以查看所有具有该权限标记的内容；用户仍然必须通过其角色拥有权限。用户不能向其他用户授予权限标记访问权限，除非他们在权限标记上拥有额外的管理权限。

如果将权限标记权限授予一个组，那么新用户加入该组时将继承这些权限。

## 应用权限标记

如果您满足两个要求，则可以在资源、文件夹或项目上应用权限标记：

1. 您拥有权限标记的“应用权限标记”权限。
2. 您拥有“更新资源上的权限标记”权限，该权限默认包含在拥有者角色中。

应用权限标记是一个敏感操作，可能会限制下游用户。在将权限标记应用于现有管道之前，我们建议采取以下步骤：

1. **确认权限标记的存在：** 确保您要应用的权限标记已创建，或[创建权限标记](/docs/foundry/platform-security-management/manage-markings/#create-markings)。
2. **创建管道的分支：** 创建新分支以继续这些步骤。当将权限标记应用于现有管道时，您可能需要在管道中的某个点停止权限标记的传播（例如，以便经过清理的 PII 数据集可以由最终用户打开）。[`stop_propagating`](/docs/foundry/transforms-python/transforms-python-api-classes/#input) 语法仅在受保护的分支上生效。在新分支合并到受保护的分支之前，您无法 `stop_propagating` 继承的权限标记。
3. **查看数据沿袭：** 确认您在数据沿袭图上拥有完整的节点集，并确认您了解潜在更改的下游影响。
4. **查看管道中的事务类型：** 权限标记沿数据依赖关系在事务级别传播。增量构建的数据集（类型为 APPEND 或 UPDATE）需要特殊处理。具体而言，使用 APPEND 事务构建的数据集的最新视图将包含来自旧上游事务的依赖关系；相比之下，使用 SNAPSHOT 事务（Foundry 默认）构建的数据集的最新视图仅依赖于上游数据集的最新事务。如果您只处理 SNAPSHOT 事务，可以继续这些步骤。如果不是，请参阅有关[APPEND 和 UPDATE 事务](/docs/foundry/data-integration/datasets/#transactions)及权限标记如何传播的文档]\(../building-pipelines/remove-markings.md#scenario-3-applying-a-new-marking-followed-by-marking-removal-at-the-dataset-level)。
5. **确定何时停止继承权限标记：** 探索管道的数据沿袭中的节点，并查看列和数据预览，以确定您希望停止继承要应用的权限标记的点。例如，您可能希望在管道中删除 DOB（出生日期）列后停止传播 PII 权限标记。在此步骤中，您可以激活模拟模式，以查看权限标记将在哪里以及如何传播。
6. **预先进行必要的变换更改：** 在您的分支中，在您识别的变换中添加 `stop_propagating` 语法。将您的分支合并到受保护的分支中，以便 `stop_propagating` 语法生效。
7. **构建生产管道：** 构建所有下游的变换，包括您识别的 `stop_propagating` 节点。您需要重建具有 `stop_propagating` 语法的数据集和所有 `stop_propagating` 变换下游的数据集。如果您有下游的 `APPEND` 或 `UPDATE` 数据集，请查看[本指南](/docs/foundry/building-pipelines/remove-markings/#scenario-3-applying-a-new-marking-followed-by-marking-removal-at-the-dataset-level)。
8. **审查模拟的更改：** 审查管道的最终模拟数据沿袭。确认您的 `stop_propagating` 变换下游的数据集不受新权限标记应用的影响。确保敏感列不会出现在不会接收传播的权限标记的数据集中。
9. **应用权限标记：** 以上步骤应确认应用权限标记将保护包含敏感数据的数据集，并且权限标记不会传播到必要之外。在此时，您可以应用权限标记。

如果您在应用权限标记后发现错误（例如，一大群用户无法看到他们应该能够看到的数据），您可以移除权限标记，它将立即停止传播。然后，您应该再次审查模拟的更改以确定问题的原因。

在下面的示例中，DOB 列被移除，并且 `stop_propagating` 语法被应用于 ontology `passengers` 数据集。PII 权限标记被应用于原始 `passenger` 数据集，仅传播到清理后的 `passenger` 数据集。

## 移除权限标记

您可以移除权限标记以便更多用户访问、重新分类变换数据，或将派生资源与继承的权限标记分开。

例如，假设数据集 A 包含 PII，并且权限标记保护从数据集 A 派生的数据集。如果数据集 B 是从数据集 A 派生的，但已变换以移除 PII，您可能希望从数据集 B 中移除权限标记，以允许更广泛地使用该数据。

要移除权限标记，您必须拥有应用和移除特定权限标记的权限。您还需要通过允许更改其权限标记的角色访问感兴趣的资源。如果您使用默认角色，此访问权限在 `Owner` 角色中可用。

### 移除直接应用的权限标记

直接从文件、文件夹或项目中移除权限标记将立即从继承权限标记的任何依赖项中移除权限标记。直接移除权限标记后，您不需要重建下游数据集，因为权限标记将立即在下游移除。以下概念示例显示了直接应用的 `PII` 权限标记。

### 移除继承的权限标记

您只能从受限视图和数据集中移除继承的权限标记。如果在派生依赖文件时移除或模糊了受限内容，您可以从派生文件中移除权限标记。当继承的权限标记被移除时，下游数据集将不再受权限标记保护，更多用户可能会访问数据集。用户仍然需要访问权限标记以查看上游数据。

要从受限视图中移除继承的权限标记，请编辑受限视图并在适当的权限标记旁单击 **停止传播**。

要从数据集中移除继承的权限标记，请在您的变换代码中使用 `stop_propagating` 语法。要安全地移除继承的权限标记，请遵循以下步骤：

1. **确定移除敏感数据的位置：** 查看完整管道，并决定要移除敏感数据的位置。
2. **创建分支：** `stop_propagating` 语法仅在受保护且启用了“合并前需要安全审批”的分支上生效。您无法在分支合并到受保护的分支之前 `stop_propagating` 继承的权限标记。
3. **进行必要的变换更改：** 在您选择的数据集中，移除敏感数据并将 `stop_propagating` 语法添加到变换中。
4. **构建分支：** 构建分支并确认输出数据集中移除了敏感数据。在此阶段，由于您位于非受保护分支上，`stop_propagating` 语法不会阻止权限标记的继承。
5. **合并分支：** 在确认移除了敏感数据后，可以安全地将变换更改合并到主分支。合并分支将应用 `stop_propagating` 语法。
6. **构建主分支和下游依赖项：** `stop-propagating` 更改必须沿管道中的最新事务传播，这需要重建具有 `stop_propagating` 语法的数据集和所有 `stop_propagating` 变换下游的数据集。构建所有数据集后，确认继承的权限标记已被移除。如果有下游的 APPEND 或 UPDATE 事务，请查看[附加文档](/docs/foundry/building-pipelines/remove-markings/#scenario-3-applying-a-new-marking-followed-by-marking-removal-at-the-dataset-level)。

在下面的概念示例中，DOB 列被移除，并且 `stop_propagating` 语法被应用于 Ontology *passengers* 数据集，以阻止 PII 权限标记进一步下游传播。

## 调查权限标记继承

权限标记沿文件层次结构和数据依赖关系[继承](/docs/foundry/security/markings/#inheritance)。这意味着文件本身可以通过权限标记保护，或者数据本身通过权限标记保护。有时您需要调查权限标记的来源，并且概念上理解权限标记的不同继承方式很重要。

您可以通过选择文件以打开右侧详细信息窗格，并查看 **访问要求 > 权限标记** 部分来查看文件的权限标记。

### 调查文件层次结构

要查看文件的权限标记，请选择它并打开资源面板。在 **访问** 部分下查看。

沿文件层次结构继承的权限标记由文件夹侧边图标表示。

要找出权限标记在文件层次结构中的起点，请在 Foundry 工作区中遍历文件层次结构。在下面的概念示例中，我们可以验证 **flight data** 文件夹具有 PII 权限标记，遍历文件层次结构从原始文件及其文件夹资源开始。访问信息显示在资源侧边栏上。

### 调查数据依赖关系

要找出权限标记的来源数据依赖关系，您可以使用数据沿袭应用程序或打开数据集文件后使用比较选项卡。

由于权限标记在[文件级别](/docs/foundry/platform-security-management/manage-markings/#apply-markings)应用，但沿[事务](/docs/foundry/data-integration/datasets/#transactions)传播，因此找出权限标记何时为数据集引入可能很困难。我们建议首先检查数据沿袭应用程序以查看权限标记的来源。

使用数据沿袭应用程序，单击 **图例 > 权限类型：数据集中的数据访问**。然后展开数据沿袭的所有上游节点，并遍历数据沿袭以查看权限标记的来源。沿数据依赖关系继承的权限标记由数据沿袭侧边图标表示。

在下面的示例截图中，`employee_sensitive` 数据集是 PII 权限标记的来源：

要完整了解权限标记何时具体引入，请查看感兴趣文件上的事务。打开特定文件并导航到 **比较** 选项卡，以比较来自两个分支和时间戳的不同事务，以了解随时间推移发生的安全和逻辑更改。

在事务比较工具的底部，您可以看到逻辑和安全更改，这将帮助您准确找出权限标记何时引入或移除。下面的示例显示了由于输入被删除而移除了 PII 权限标记：

下面的示例显示了由于输入被删除而移除了 PII 权限标记：

---

## [platform-security-management] 管理组织和空间

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-orgs-and-spaces/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-orgs-and-spaces.md`

# 管理组织和空间

## 组织

组织权限应通过[控制面板](/docs/foundry/administration/enrollments-and-organizations/)进行管理。进一步的组织配置在 Foundry 设置选项卡中进行管理。

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

客人成员资格将允许您查看将此组织作为主要组织的用户，但不能查看此组织的其他客人用户。将此作为主要组织的用户始终可以查看此组织的客人用户。

您可以从 Foundry **设置**页面的组织选项卡中向您的组织添加客人：

### 主页文件夹和组织

启用 Foundry 主页文件夹时，它们会自动标记为用户的组织。

禁用主页文件夹的配置选项目前处于测试阶段。请联系 Palantir 支持以启用此功能。

## 空间

**空间**已经从其以前的名称**命名空间**重新命名。

空间设置在[控制面板](/docs/foundry/administration/enrollments-and-organizations/)的**空间**选项卡中进行管理。

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

---

## [platform-security-management] 管理项目约束

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-project-constraints/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-project-constraints.md`

# 管理项目约束

要在项目上添加约束，您必须在项目中拥有`Owner`角色，并在所有作为项目约束添加的权限标记上添加“应用权限标记”权限。如果添加或修改项目约束会导致项目中的现有文件违反您尝试添加的约束，您将无法添加或修改项目约束。

要管理约束，请导航到右侧访问面板中的权限标记部分。

## 项目约束违规

在应用项目约束后，如果某个违规的权限标记在上游某处被添加并被项目中的数据集继承，则数据集仍可能违反项目约束。这会通过警告显示在违反的数据显示集上。如果数据集违反了项目约束，则在解决违规问题之前无法搭建。

可以通过以下操作解决项目约束违规：

* 将此继承的权限标记添加为允许的项目约束。
* 从必要的变换中移除引入新权限标记的输入。
* 移除继承的上游权限标记。了解如何在我们的文档中[移除权限标记](/docs/foundry/building-pipelines/remove-markings/)。

---

## [platform-security-management] 管理受限视图

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-restricted-views/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-restricted-views.md`

# 管理受限视图

## 使用受限视图作为对象类型的后备

要在Object Explorer中为特定对象类型提供访问权限，请在[Ontology Manager](/docs/foundry/ontology-manager/overview/)中将受限视图设置为后备数据集。要成功配置并保存由受限视图支持的对象类型，您必须对受限视图的输入数据集具有`查看`权限。

## 受限视图文件权限

要创建和编辑受限视图，您必须在角色界面中的细粒度权限管理工作流中满足以下条件。要访问角色界面，请导航至设置并在侧边栏的平台设置部分中选择**角色**。访问角色界面需要特殊的平台权限；如果您需要此级别的访问权限，请联系您的Palantir代表。

|角色	|描述	|
|---	|---	|
|创建受限视图资源	|需要在文件夹/项目上。|
|为数据集创建受限视图	|需要在受限视图上游的数据集上。	|
|编辑资源细粒度策略	|编辑资源上的细粒度策略。	|
|查看资源细粒度策略	|查看资源上的细粒度策略。	|
|编辑受限视图资源	|需要对受限视图进行编辑（策略，假设权限标记）。	|
|查看受限视图资源	|查看受限视图的属性（策略，假设权限标记）。	|
|查看受限视图事务	|查看历史事务元数据（策略，假设权限标记）。	|

要搭建受限视图，您必须对输入数据集具有查看权限，并对输出受限视图具有编辑权限。

要在Contour分析中使用受限视图，您需要*读取受限视图*权限。

要配置并保存由受限视图支持的对象类型，您必须具有：

* 对受限视图输入数据集的查看权限。
* 对受限视图的编辑权限（查看/设置/更改策略）。
* 是Ontology管理员组的成员（以访问Ontology Manager）。

要在Object Explorer中使用数据集支持的对象上的细粒度策略，您必须对数据集具有*查看Ontology数据源*权限，以查看该类型的任何对象。

## 受限视图策略管理

### 策略比较

受限视图策略支持以下比较类型：

* **小于：** 比较的左右两边必须都是单值（不是集合）且类型相同。
* **小于或等于：** 比较的左右两边必须都是单值（不是集合）且类型相同。
* **等于：** 比较的左右两边必须都是单值（不是集合）且类型相同。
* **大于或等于：** 比较的左右两边必须都是单值（不是集合）且类型相同。
* **大于：** 比较的左右两边必须都是单值（不是集合）且类型相同。
* **交集：** 至少一边必须是集合，且双方必须是相同类型（或该类型的集合）。

策略被定义为模板，用户属性、组成员资格和数据值可以填充其中：

当细粒度权限资源的消费应用请求数据时（例如在[Contour](/docs/foundry/contour/overview/)中），策略模板会转换为查询，仅返回特定于用户属性和权限的行。

### 策略限制

单个策略最多可以有十个比较。受限视图策略根据策略是否将集合或常量与字段进行比较来权衡每个比较：

* 将常量与字段进行比较的权重为1。
* 将集合与字段进行比较的权重为1,000。
* 策略中所有比较的权重总和必须低于10,000。

例如，在一个基本策略中：

* 规则（1）的权重为1，因为它将常量（用户的ID）与字段匹配。
* 规则（2）的权重为1,000，因为它将集合（用户所属的所有组）与特定的Platform Administrators组匹配。
* 该策略中的权重总和为1,001（远低于10,000的限制）。

当前的策略构建限制旨在对特定策略设计施加最小的约束；它对可能超出权重限制的策略提供很少的保护。

如果在构建策略时收到权重限制错误，请联系您的Palantir代表以获取帮助。

### 策略管理

策略的更改会记录为受限视图上的新事务，但某些用户可能需要额外的控制来管理策略更改。

当您管理受限视图策略时，请考虑两个目标：

* **透明度：** 任何负责管理数据访问的人都应该了解策略以及策略如何与平台中的数据交互。
* **健全的变更管理：** 策略管理应该是一个有序的、组织化的过程。在应用更改之前，始终要审查和管理更改。

### 管理数据管道的完整性

受限视图策略对支持它们的数据引入了一系列假设。因此，只要这些假设为真，受限视图策略才能正确控制对数据的访问。考虑应用案例是否需要构建机制以确保这些假设成立，并且如果这些假设被打破，数据仍然保持安全。

解决此问题的一种方法是在受限视图上游的管道中引入一个步骤，检查对数据的假设。这些检查可能包括：

* **不变量：** 编写一份不变量列表，如果不为真，将强制受限视图数据集的下游构建失败。例如，假设当`event_occurred_in_state`的值为`NY`时，数据集中的另一列`state_name`应为`New York`。在将此数据展示给用户之前，请执行变换检查这是否为真。
* **统计数据：** 定义一组统计数据及其应始终保持的范围。例如，受限视图可能用于实施与组织层级相对应的访问控制；每个用户只能查看层级中其下属人员的数据。让变换断言，如果从一天的构建到下一天的构建，层级中的变化超过20%，则表明存在问题。在此时，负责策略管理的用户应检查以确保一切正常，然后再将此数据展示给用户。

## 受限视图限制

受限视图类似于数据集，但有一些关键区别。受限视图的内容结合了两个动态因素：（1）策略定义和（2）特定时间访问受限视图的特定用户的属性和组成员资格。虽然策略定义历史在受限视图的事务历史中维护，但事务历史不可能维护所有用户属性和组成员资格的完整历史。

受限视图旨在简化单个用户对管道的分析消费，不能被用作数据变换的输入。在Foundry中构建的管道应是可重现的，并且与运行它们的特定用户无关，这与受限视图的本质不兼容，因为受限视图提供基于用户属性的行级权限。

* 尝试在受限视图上协作构建管道的用户可能无法访问策略声明，且可能没有相同的用户属性和组成员资格。因此，每个用户可能会在受限视图中看到不同的行和汇总；因此，用户不应假设基于细粒度权限数据的工作流将与基于Foundry中常规数据集资源的工作流表现相同。
* 对于下游变换，没有强制确保后续下游变换保留策略列。相比之下，为了保护架构和列免受更改导致的受限数据暴露，受限视图是只读的。

以下列表总结了受限视图的当前限制：

|操作	|受限视图是否支持？	|解释	|
|---	|---	|---	|
|读取	|YES	|受限视图可以通过对象或在Contour中读取	|
|即时计算	|YES	|使用受限视图，可以通过对象（如在Quiver或函数中）或在数据集上（使用诸如Contour等工具）执行可访问行的计算	|
|数据输出	|YES	|基于受限视图的对象可以定义数据输出	|
|以{filetype}格式导出	|YES	|可以通过Quiver、Contour和其他应用程序导出受限视图中的数据	|
|批处理	|NO	|受限视图不支持批处理，因为不同的用户会看到不同的数据子集	|
|将输出保存为Foundry数据集	|NO	|不支持保存基于对受限视图进行变换的输出；由于Spark本身不支持行级权限，因此无法确保后续事务维护限制的保证	|
|同步到Postgres	|NO	|不支持将受限视图同步到Postgres，因为基于用户属性的行级权限不会被维护	|

---

## [platform-security-management] 管理角色

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-roles/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-roles.md`

# 管理角色

在 Foundry 设置中的角色部分管理角色。

## 自定义默认角色

以自定义您的组织角色，您必须在控制面板中获得组织管理员权限。

### 理解角色和操作

为了理解角色自定义，我们需要更深入了解操作。

操作是 Foundry 应用程序检查的单个权限，以验证用户是否有权限执行给定的操作。角色是一组操作：当您在某个资源（如项目或数据集）上为某人授予角色时，您是在该资源及其所有子资源上授予他们一组操作。每个操作都有一个名称和唯一标识符。

例如，默认拥有者角色（但不是较低角色）中包含的一个操作名为“更改默认分支”操作（标识符为：`stemma:mutate-default-branch`），允许您更改代码库的默认分支。当您在项目上授予用户拥有者角色时，该用户在该项目中的所有资源上获得 `stemma:mutate-branch`，因此他们可以更改任何代码库内部的默认分支。

### 创建自定义角色

角色管理界面可以在平台设置页面的角色选项卡下找到。

您可以创建全新的自定义角色。您可能希望创建自己的自定义角色以支持组织中的不同用户类型，如下文详细介绍的[合并者](#merger)或[支持者](#supporter)角色。

要创建您自己的自定义角色，只需点击“新角色”，然后系统会提示您进入新角色对话框：

您可以“包含”其他角色。对于上面的新合并者角色，我们包含了只读角色，这意味着只读授予的所有权限将在合并者角色中授予。一旦创建，您可以通过附加操作自定义此角色。

### 编辑默认角色

您只能编辑自定义[角色集](#role-sets)的默认角色（例如只读）。因此，要自定义您的组织角色，您首先需要创建默认角色的自定义角色集。然后您可以编辑这些默认角色。

例如，如果您希望实例上的所有编辑者都能够更改存储库的默认分支，您只需编辑编辑者角色以包含此操作。

### 示例自定义角色

以下是一些在您的情况下可能有用的自定义角色示例。

#### 合并者

合并者角色提供合并到受保护分支的能力，应该在只读角色之外授予。创建一个自定义角色，包括以下操作：

* 管理工件库
* 合并到受保护分支
* 合并拉取请求
* 更新拉取请求

#### 支持者

支持者能够查看与项目相关的问题，但无法查看任何元数据（如模式、数据集名称等）。这主要是为 Palantir 或第三方支持团队提供的，他们可能没有加入或被授权查看某些数据。支持者角色可以通过包含以下操作创建：

* 应用指派规则
* 存档问题
* 编辑问题
* 关闭和重新打开问题
* 查看问题

## 角色集

角色集是一组角色，允许在组织级别自定义角色权限，并在特定上下文中使用，例如在项目或 Ontology 中。当同一[注册](/docs/foundry/administration/enrollments-and-organizations/)中的[组织](/docs/foundry/security/orgs-and-spaces/#organizations)希望有不同角色时，角色集增加了灵活性。角色集提供以下保证：

* 同一集中的角色不依赖于该集之外的任何角色。
* 所有角色仅属于一个角色集。
* 集中的角色属于同一组织，并统一授权。
* 集中的角色被设计为在同一上下文中协同工作。目前，角色集可用的三个上下文是项目上下文、Ontology 上下文和市场安装上下文。

每个注册将至少有三个默认角色集：项目默认（拥有者、编辑者等）、Ontology 默认（Ontology 拥有者、Ontology 编辑者等）和市场安装默认（市场安装编辑者、市场安装只读等）。默认角色集及其内部角色始终对所有组织可用。

### 创建新角色集

角色管理员必须在他们管理角色的组织中拥有“管理角色和角色集”权限。此权限在控制面板中的组织管理员角色下授予。只有拥有此权限的管理员才能为组织创建新的角色集，并在属于该组织的角色集中自定义现有角色。

要为给定组织自定义角色，管理员应首先创建一个新角色集。

要进行此操作：

1. 进入**平台设置**，并点击位于右上角的角色部分下的**创建角色集**。
2. 完成新角色集表单。

创建新角色集时，管理员需要从现有角色集中复制角色。然后，管理员只需从现有角色集中进行相关更改。

此外，当复制项目默认角色集或另一个依赖于项目默认角色集的角色集时，新复制的角色集将自动更新为项目默认角色集的任何角色更新。随着 Foundry 开发的继续，Palantir 可能会添加新角色；自动接收这些权限更新可以减少未来的管理工作。

在上述角色集创建后，任何在 Org B 上具有“管理角色和角色集”权限的管理员都可以编辑此新角色集。

### 共享角色集

角色集的可见性由组织可发现性决定。组织可发现性在**平台设置**下的**组织**部分进行管理。

在上述示例中，Org B 拥有的角色集仅对 Org A 和 Org D 可见，因为它们是相互可发现的（在这种情况下，第一列切换为所有 3 行选择）。Org B 和 Org C 用户无法看到彼此的角色集。允许来自相互可发现组织的用户看到彼此的角色集有助于跨组织协作。例如，在一个应用了 Org A 和 Org B 的项目中，管理员可能希望来自 Org A 和 Org B 的用户接收仅由 Org B 定义的自定义角色。

### 应用角色集

角色集只能在空间级别应用。该空间内的所有项目、文件夹和文件只能使用在空间设置中应用的角色集中定义的角色。为管理此项，管理员可以：

1. 访问注册设置中的 [Control Panel](/docs/foundry/administration/enrollments-and-organizations/) 下的**空间**选项卡。

2. 在空间创建对话框中选择角色集，如下所示。

3. 现有角色集也可以在空间设置下的**角色集**卡片中替换为新角色集，如下所示。

如果管理员用新角色集替换空间上的当前角色集，则每个当前角色必须映射到替换角色。下面是更新现有空间上的角色集时映射对话框的示例。

完成后，整个空间中的所有角色授予将更新为它们的新替换角色。

当用户跨角色集边界移动资源（项目、文件夹或文件）且资源有直接应用的角色时，上述映射对话框也将显示。

---

## [platform-security-management] 管理用户

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-management/manage-users/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-management-manage-users.md`

# 管理用户

通过导航侧边栏进入 **账户 > 设置** 来访问用户管理页面。然后，在侧边栏的 **平台设置** 部分选择 **用户**。

在这里，您可以查看 Foundry 中用户的不同信息：

* **用户 ID：** 用户的永久唯一 ID。
* **组织：** 用户所属的[组织](/docs/foundry/administration/enrollments-and-organizations/)。
* **组：** 用户所属组的列表。
* **属性：** 以键值格式表示的用户信息，通常被其他 Foundry 服务使用。例如，用户可能有一个用于地理区域的属性，可以用来限制用户在 Ontology 中可以看到的对象。

[了解更多关于限制视图的信息。](/docs/foundry/security/restricted-views/)

## 预注册用户

具有预注册权限的平台管理员可以在用户首次登录 Foundry 之前对其执行操作。管理员可以创建用户名，给予用户适当的组成员资格，指派组织和权限标记访问等，以确保新用户在首次登录时能够正确访问资源。

创建的用户名需要与用户的登录用户名完全匹配，以便预注册操作能够正常工作。

## 用户不活跃

如果 Foundry 用户账户在 30 天内没有成功登录，则会自动被视为不活跃账户。不活跃账户在 Foundry 中的行为与活跃账户相同，唯一不同的是不活跃用户账户的所有词元在账户不活跃时均无效。

在成功登录后，不活跃用户账户将自动设置为活跃状态，重新启用所有被禁用的词元。不需要管理员采取任何行动来重新激活。

可以将某些 Foundry 组和身份验证域中的用户排除在此不活跃行为之外。有关这些排除的更多信息，请联系您的 Palantir 代表。

如果用户在登录时遇到以下信息：“您的账户已锁定。请联系您的支持人员解锁，然后重试。”，请联系您的 Palantir 代表以解锁账户。

## 故障排除

### “您的账户已被禁用”出错

如果登录失败，并显示出错信息 `您的账户已被禁用`，这意味着用户账户已被删除。您可以联系管理员，通过 `getDeletedUsers` 和 `undeleteExternalUser` 端点分别查找和“取消删除”账户。具有 `管理成员资格` 权限的组织管理员可以调用这些端点。下面列出了示例 curl 请求。

#### 通过 getDeletedUsers 查找已删除的用户

此步骤是非必填的，仅在未知已删除用户的用户 ID 时需要。

```bash
curl -XGET -H "Authorization: Bearer $TOKEN" '<FOUNDRY_URL>/multipass/api/administration/users/deleted?pageSize=<NUMBER_OF_RESULTS_TO_RETURN>&pageToken=<PAGE_START_TOKEN>'
```

此命令使用 `curl` 发送一个 HTTP GET 请求，获取已删除用户的信息。以下是各部分的含义：

* `-XGET`：指定请求方法为 GET。
* `-H "Authorization: Bearer $TOKEN"`：在请求头中添加授权信息，使用 Bearer Token 进行身份验证。
* `'<FOUNDRY_URL>/multipass/api/administration/users/deleted'`：请求的 URL，替换 `<FOUNDRY_URL>` 为实际的服务器地址。
* `pageSize=<NUMBER_OF_RESULTS_TO_RETURN>`：查询参数，指定返回结果的数量。
* `pageToken=<PAGE_START_TOKEN>`：查询参数，用于分页，指定从哪个位置开始返回结果。

````

该命令通常用于从系统中分页获取已删除用户的列表，确保替换 URL 和参数为实际值。
**注意：** 最大页面大小为1000。

#### 通过 undeleteExternalUser 恢复已删除用户
```bash
# 使用 cURL 命令恢复被删除的用户账户
# -XPOST 指定使用 POST 方法
# -H 用于设置 HTTP 请求头，这里是设置授权头，其中 $TOKEN 是访问令牌
# <FOUNDRY_URL> 是 API 的基础 URL
# <USER_ID> 是要恢复的用户的唯一标识符

curl -XPOST -H "Authorization: Bearer $TOKEN" '<FOUNDRY_URL>/multipass/api/administration/users/<USER_ID>/undelete/external'
````

---

## [platform-security-third-party] platform-security-third-party

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party.md`

# 概述

Foundry 平台的安全控制确保第三方应用程序的集成和互操作性可以在尊重既定安全措施的同时进行集中管理。第三方应用程序授权支持 [OAuth 2.0 框架](/docs/foundry/platform-security-third-party/writing-oauth2-clients/)。

第三方应用程序权限应由 Foundry 管理员管理，以确保 Foundry 平台的安全性。[控制面板](/docs/foundry/administration/control-panel/)中的第三方应用程序界面使 Foundry 管理员能够查看哪些应用程序已在 Foundry 上注册，以及哪些应用程序已被启用以供访问。在第三方应用程序界面中，管理员可以[注册新应用程序](/docs/foundry/platform-security-third-party/register-3pa/)、[管理现有应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)以及[启用或禁用应用程序](/docs/foundry/platform-security-third-party/enabling-3pa-access/)。

## 访问第三方应用程序用户界面

对于具有适当权限的用户，可以通过点击位于左侧导航栏下角的 **打开其他工作区 > [控制面板](/docs/foundry/administration/control-panel/)** 来进入第三方应用程序管理界面。然后，选择一个注册和相关的组织，最后在**组织设置**下选择**第三方应用程序**标签。

用户必须在所选组织中拥有 **第三方应用程序管理员** 角色才能访问第三方应用程序管理界面。

有关更多详细信息，请查看[控制面板中的权限](/docs/foundry/administration/enrollments-and-organizations-permissions/)。

---

## [platform-security-third-party] Foundry 第三方应用程序和 API 指南

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/3pa-api-guidance/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-3pa-api-guidance.md`

# Foundry 第三方应用程序和 API 指南

Foundry 的第三方应用程序身份验证和授权功能使非 Foundry 应用程序和脚本能够安全地与 Foundry 的 API 交互。这些功能的核心是对外部应用程序的 OAuth2 支持。
本文档提供了 Palantir 推荐使用这些功能的指导，以及潜在不当使用的示例。

通过授权第三方应用程序和 API，用户同意遵循 Palantir 与客户书面协议中商定的适当使用条款。如果您对预期使用有任何疑问，或者不确定您的计划是否合适、安全或可靠，请联系您的 Palantir 代表。

## 适当使用

* **替换服务用户账户**
  * OAuth2 授权码流程允许外部应用程序代表个人 Foundry 用户操作。这确保了权限的正确性，并提供了清晰的审计路径。使用 OAuth2 流程还确保用户明确授予应用程序代表其执行操作的权限，再次提供了清晰的审计路径。
  * 我们强烈建议使用服务账户在 Foundry 中执行操作的现有应用程序尽可能迁移到 OAuth2 授权流程。
* **与外部系统的接口**
  * *示例：一个应用程序监控内部客户系统中的更改并在 Foundry Ontology 中执行操作。*
* **特定用户工作流程的自定义应用程序**
  * *示例：一个移动电话应用程序与 Foundry 的 Ontology 和 操作 API 交互，以提供关键工作流程的简化用户体验。*
* **Foundry 流程或工作流的监控或控制**
  * *示例：一个应用程序连接到 Foundry 的监控和数据健康 API 以评估关键流程的状态，并允许其用户在需要时触发搭建。*

## 不当使用

集成第三方应用程序和使用 Foundry API 存在数据安全风险，只有在清楚了解技术和合同考虑的情况下才应进行。在规划访问数据或代表用户执行操作的开发项目时，请联系您的系统管理员以确定您的计划是否合适、安全，并符合 Foundry 的适当使用条款。

以下示例概述了在不当使用 API 访问数据或执行操作时可能会损害 Foundry 管理的数据完整性或安全性的代表性场景。

* **规避数据控制**
  * *示例：使用一个用户的词元读取数据并使用另一个用户写入。*
  * Foundry 拥有高级和细粒度的用户授权功能。在您的应用程序中共享用户账户之间的数据可能会规避这些控制。
  * 保持使用单个 Foundry 账户的完全隔离非常重要。您不得使用一个用户的词元访问数据并允许另一个用户读取、发现、写入或以任何方式与该数据交互。如果您希望允许用户共享数据，应在 Foundry 中完成，而不是在第三方应用程序中。
* **在用户不了解和未同意的情况下执行操作。**
  * 您的应用程序不得欺骗用户。您的应用程序必须清晰准确地描述在使用 Foundry 用户账户时执行的操作。
  * 您的应用程序必须请求执行其功能所需的最小角色和权限集合，不得多请求。还必须向用户明确何时将在 Foundry 中执行操作，以及这些操作将做什么。
  * 任何不清晰、意外、恶意或破坏性的应用程序行为都是被禁止的。
* **在未经访问控制考虑的情况下在 Foundry 之外检索或存储数据。**
  * Foundry 的客户依赖 Foundry 安全存储关键数据；您的应用程序必须尊重这些数据的敏感性和价值，并检索其执行功能所需的最小数据集合。
  * 您的应用程序还应尽量避免存储或缓存从 Foundry 检索的数据。一个潜在的例外情况可能是离线缓存，但应谨慎处理并获得用户明确同意。
  * 如果 Foundry 数据被移动到另一个数据存储系统中，请确认它将不再根据您组织在 Foundry 内的数据保护配置进行访问控制或审计。

---

## [platform-security-third-party] 授权第三方应用程序访问

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/authorizing-3pa-access/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-authorizing-3pa-access.md`

# 授权第三方应用程序访问

## 授权第三方应用程序

一旦第三方应用程序在Foundry平台中[注册](/docs/foundry/platform-security-third-party/register-3pa/)并[启用](/docs/foundry/platform-security-third-party/enabling-3pa-access/)，授权第三方应用程序访问Foundry的过程就很简单。

如果所需的第三方应用程序尚未在Foundry平台中注册和启用，请在继续授权过程之前注册并启用它，或联系您的Palantir代表以请求注册和/或启用。

在此示例中，我们将使用一个简单的测试应用程序来演示授权已注册和启用的第三方应用程序以访问Foundry的工作流程。第三方应用程序可能会提供某种**连接**选项，如下所示。

尝试连接或授权已注册和启用的第三方应用程序将引导您进入Foundry并打开一个确认屏幕，如下所示，您可以选择**允许**或**不允许**访问。在此确认屏幕上，Foundry将显示第三方应用程序请求权限的操作集；此操作集由第三方应用程序连接器的作者确定。

允许访问后，您应被重定向回第三方应用程序，并收到访问权限确认。

### 管理已授权的应用程序

在Foundry的**设置**页面上，**已授权的应用程序**选项卡显示已批准访问的第三方应用程序。此时，我们可以看到测试应用程序已获得访问您账户的权限。

点击**操作**下拉菜单会显示以下选项：**详情**和**撤销**。

选择**详情**会显示第三方应用程序可以访问的数据的信息。

选择**撤销**会弹出一个确认屏幕；撤销访问将移除应用程序访问您账户信息的能力。

撤销访问后，我们看到没有应用程序被授权访问您的账户。访问被撤销的应用程序可以通过重复此工作流程再次添加。

---

## [platform-security-third-party] 危险区域操作

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/danger-zone-actions/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-danger-zone-actions.md`

# 危险区域操作

Foundry平台管理员可以对第三方应用程序执行多个“危险区域”操作。这些操作被称为“危险区域”操作，因为它们会对应用程序的注册造成不可逆转的更改，并且由于其潜在的广泛和破坏性影响，应谨慎对待。在执行这些操作之前，会出现一个警告对话框。可用的“危险区域”操作有[旋转客户端密钥](#rotate-a-client-secret)和[删除应用程序注册](#delete-an-application-registration)。

## 旋转客户端密钥

您可以仅在[管理应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)页面为[机密客户端 ↗](https://tools.ietf.org/html/rfc6749#section-2.1)旋转应用程序的密钥。旋转密钥将要求每位用户重新设置应用程序，因为每个配置了该密钥的客户端将停止工作，因为旋转后的密钥已失效。仅在密钥已被泄露或丢失时才应进行密钥旋转；请记住，密钥旋转后需要重新设置应用程序。

您何时可能需要旋转密钥？鉴于旋转密钥的后果，这仅应在密钥被泄露或无法访问时进行。

1. 从**控制面板**导航到[第三方应用程序](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface)页面。
2. 点击您想要修改的应用程序的**操作**，然后点击**管理应用程序**。
3. 向下滚动并点击**旋转密钥**。
4. 在确认操作之前，查看警告对话框。
5. 确认操作并安全存储您的新客户端密钥，因为之后将无法再次查看。

## 删除应用程序注册

1. 从**控制面板**导航到[第三方应用程序](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface)页面。
2. 点击您想要删除的应用程序的**操作**，然后点击**管理应用程序**。
3. 向下滚动并点击**删除应用程序**。
4. 在确认操作之前，查看警告对话框。
5. 确认操作，应用程序将被删除。这不能被撤销。

---

## [platform-security-third-party] 启用第三方应用程序

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/enabling-3pa-access/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-enabling-3pa-access.md`

# 启用第三方应用程序

Foundry 的第三方应用程序启用框架使组织能够控制他们启用的第三方应用程序。组织可以选择启用哪些应用程序，因为启用是特定于组织的；一个组织启用的应用程序集可能包括其他组织管理的应用程序。

因此，一旦第三方应用程序在 Foundry 中注册，它需要为组织启用，组织内的用户才能使用该应用程序。这适用于注册第三方应用程序的组织以及其他组织；应用程序不会自动启用。

应用程序启用后，用户可以执行 [OAuth2 授权流程](/docs/foundry/platform-security-third-party/authorizing-3pa-access/)，以授予 Foundry 访问第三方应用程序的权限。因此，应用程序对 Foundry 资源的访问仍然需要用户明确同意授予访问权限。

## 所需权限

如果您拥有组织的 **管理 OAuth 2.0 客户端** 权限，并且第三方应用程序已对该组织可发现，那么您可以启用该应用程序、编辑该应用程序的启用详细信息或禁用该应用程序。

## 启用或禁用应用程序

通过从 [第三方应用程序用户界面](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface) 中应用程序右侧的 **操作** 下拉菜单中选择 **启用设置** 来访问启用设置界面。

以下是示例应用程序的启用设置界面：

在这里，您可以使用页面顶部的切换按钮 **启用** 或 **禁用** 您的应用程序。

禁用应用程序并不是简单的开关操作，因为重新启用应用程序需要再次完成应用程序启用工作流程。现有的应用程序授权将不会重新激活，每个用户必须重新授权新启用的应用程序。

### 项目访问

您还可以设置应用程序的项目访问范围。项目访问范围决定了在代表 Foundry 用户通过授权代码授予授权时，应用程序可以访问的项目。

* 连接到 Foundry 的第三方应用程序可以访问的资源范围受两个因素限制：
  * 授权用户可以访问的项目，以及
  * 在启用界面上定义的项目。
* 应用程序只能访问授权用户可以访问的项目与启用界面上指定的项目的交集。换句话说，启用界面提供了一种缩小应用程序对 Foundry 访问范围的方法。
* 我们建议将项目范围设置为 **不受限制**，这将授予应用程序访问授权用户可以访问的所有资源的权限。

### 权限标记限制

设置应用程序数据访问范围的另一种方法是通过权限标记限制。通过将 [权限标记](/docs/foundry/security/markings/) 应用到您的应用程序，您可以确定在代表 Foundry 用户通过授权代码授予授权和/或通过客户端凭证授予服务用户授权时，应用程序将可以访问的资源。

* 连接到 Foundry 的第三方应用程序可以访问的资源范围受两个因素限制：
  * 授权用户和/或服务用户可以访问的资源，以及
  * 通过启用界面应用的权限标记。
* 应用程序只能访问用户可以访问的资源与通过启用界面指定的权限标记允许的资源的交集。需要注意的是，即使访问受限，未标记的资源仍可能被利用，除非用户被拒绝访问这些资源。
* 我们建议将权限标记限制设置为 **不受限制**，这将授予应用程序访问授权用户和/或服务用户可以访问的所有资源的权限。

### 组织级别同意

在高级启用设置中，您可以代表组织的用户授权第三方应用程序访问 Foundry。

如果启用，用户将不需要执行 [OAuth2 授权流程](/docs/foundry/platform-security-third-party/authorizing-3pa-access/)，第三方应用程序将被授权访问该组织中所有用户的 Foundry。启用此功能时，用户不会收到通知。

我们建议不要启用组织级别同意，除非您的应用案例明确要求这样做。

---

## [platform-security-third-party] 管理第三方应用程序配置

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/manage-3pa/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-manage-3pa.md`

# 管理第三方应用程序配置

用户现在被重定向到[**开发者控制台**](/docs/foundry/ontology-sdk/oauth-clients/)以管理他们的应用程序配置。只有在用户未启用**开发者控制台**的情况下，才适用**控制面板**视图。

您可以通过在[第三方应用程序用户界面](/docs/foundry/platform-security-third-party/third-party-apps-overview/#accessing-the-third-party-applications-user-interface)中选择应用程序右侧的**操作**下拉菜单中的**管理应用程序**来访问管理应用程序界面。在这里，您可以查看和编辑应用程序的注册信息，如其名称、描述、标识、授权授予类型和应用程序发现设置。

**管理应用程序**界面仅对管理第三方应用程序的组织的被授权成员可用。

用户创建应用程序的组织被视为应用程序的管理组织，组织中拥有**管理 OAuth 2.0 客户端**权限的任何人都可以管理第三方应用程序。

管理组织可以通过应用程序发现设置确定哪些其他组织可以查看和使用该第三方应用程序。

以下是为示例应用程序显示的**管理应用程序**页面示例：

## 删除应用程序注册

[危险区域操作](/docs/foundry/platform-security-third-party/danger-zone-actions/)位于**管理应用程序**页面的底部。

为了永久阻止用户授权第三方应用程序，可以撤销应用程序的注册，即从 Foundry 中删除。

这被视为“危险区域操作”，因为这是不可逆的，并且将使所有用户无法使用该第三方应用程序，除非重新注册应用程序。如果应用程序被重新注册，用户将必须重新授权第三方应用程序，因为 Foundry 将重新注册视为新注册。

了解如何从[危险区域操作文档](/docs/foundry/platform-security-third-party/danger-zone-actions/#delete-an-application-registration)中删除应用程序的注册。

---

## [platform-security-third-party] 注册第三方应用程序

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/register-3pa/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-register-3pa.md`

# 注册第三方应用程序

用户现在被重定向到[**开发者控制台**](/docs/foundry/ontology-sdk/oauth-clients/)以注册新的应用程序配置。只有当用户未启用**开发者控制台**时，才适用**控制面板**视图。

在第三方应用程序连接到Foundry之前，必须在Foundry平台上注册。初始注册过程会为第三方应用程序创建一个名称、一个客户端ID和一个客户端密钥；有关客户端ID和客户端密钥的更多信息，请参阅[OAuth.com文档 ↗](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/)，这些在授权工作流程中被用于在。然后，需要为第三方应用程序配置一个用于授权过程的重定向URL，以及一个名称、描述和图标，这些用于第三方应用程序在平台内的表示。

## 注册

1. 要开始注册新应用程序的过程，请导航到**控制面板**中的**第三方应用程序**选项卡，然后单击**新应用程序**。

2. 这将打开**注册新应用程序**向导。将按以下顺序有四个步骤：**详细信息**、**客户端类型**、**授权授予类型**和**摘要**。

3. 在**详细信息**步骤中，为您的应用程序提供名称、描述（非必填）和徽标（非必填）。
4. 在**客户端类型**步骤中，指定应用程序的客户端类型。客户端类型指的是OAuth2标准，涉及客户端应用程序是否可以安全地存储密钥。客户端类型的两个选项是：
   * [机密客户端 ↗](https://tools.ietf.org/html/rfc6749#section-2.1)：这适用于能够安全持有其凭据的客户端；例如，在受限访问客户端凭据的安全服务器上实现的客户端。此客户端类型支持用于授权的[授权代码授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#authorization-code-grant)和[客户端凭据授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant)选项。
   * [公共客户端 ↗](https://tools.ietf.org/html/rfc6749#section-2.1)：这适用于不能安全持有其凭据的客户端；例如，授权客户端在网页浏览器本身上运行的基于浏览器的应用程序。此客户端类型支持带PKCE的[授权代码授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#authorization-code-grant)，这意味着需要使用`code_verifier`和`code_challenge`参数。[客户端凭据授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant)不被支持。 <br><br>有关这些客户端类型的更多信息，请参阅[编写OAuth2客户端](/docs/foundry/platform-security-third-party/writing-oauth2-clients/)的文档。

原生或单页应用程序，如移动应用程序，被分发给用户进行部署。因此，应用程序的二进制文件是可用的，并且可以被反编译以提取客户端密钥。然后，客户端密钥可能被用于在攻击中冒充授权用户。[代码交换证明密钥（PKCE）↗](https://oauth.net/2/pkce/)用于防止此类攻击。

5. 在**授权授予类型**步骤中，您将看到上一步中选择的客户端类型支持的授予类型。如果您选择启用[授权代码授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#authorization-code-grant)，您将需要指定至少一个**重定向URL**。

   * 在授权过程中，OAuth2使用浏览器重定向将用户从授权提供者（在本例中为Foundry）发送回用户尝试授权的客户端（在本例中为第三方应用程序）。因此，指定重定向URL有助于在第三方应用程序请求访问Foundry资源的权限时提供额外的安全性。
   * 请注意，重定向URL可以在[管理应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)屏幕中稍后更新。

   如果您选择启用[客户端凭据授予](/docs/foundry/platform-security-third-party/writing-oauth2-clients/#client-credentials-grant)（这仅对机密客户端可用），将为应用程序创建一个服务用户。该服务用户可以被授权以应用程序名义访问Foundry资源的请求。

6. 在**摘要**步骤中，将显示所提供的所有信息的概述以及仍需提供的任何缺失部分。当必填字段完成时，您可以点击屏幕右下角的**注册应用程序**。

7. 提交后，将向您显示新创建的客户端的ID和密钥（如适用）。

如果使用*机密客户端*，您**必须**在此时复制客户端密钥。离开此页面后，密钥将无法再次获得。如果您失去对客户端密钥的访问，您将需要轮换密钥。

---

## [platform-security-third-party] third-party-apps-overview

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/third-party-apps-overview/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-third-party-apps-overview.md`

# 概述

Foundry 平台的安全控制确保第三方应用程序的集成和互操作性可以在尊重既定安全措施的同时进行集中管理。第三方应用程序授权支持 [OAuth 2.0 框架](/docs/foundry/platform-security-third-party/writing-oauth2-clients/)。

第三方应用程序权限应由 Foundry 管理员管理，以确保 Foundry 平台的安全性。[控制面板](/docs/foundry/administration/control-panel/)中的第三方应用程序界面使 Foundry 管理员能够查看哪些应用程序已在 Foundry 上注册，以及哪些应用程序已被启用以供访问。在第三方应用程序界面中，管理员可以[注册新应用程序](/docs/foundry/platform-security-third-party/register-3pa/)、[管理现有应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)以及[启用或禁用应用程序](/docs/foundry/platform-security-third-party/enabling-3pa-access/)。

## 访问第三方应用程序用户界面

对于具有适当权限的用户，可以通过点击位于左侧导航栏下角的 **打开其他工作区 > [控制面板](/docs/foundry/administration/control-panel/)** 来进入第三方应用程序管理界面。然后，选择一个注册和相关的组织，最后在**组织设置**下选择**第三方应用程序**标签。

用户必须在所选组织中拥有 **第三方应用程序管理员** 角色才能访问第三方应用程序管理界面。

有关更多详细信息，请查看[控制面板中的权限](/docs/foundry/administration/enrollments-and-organizations-permissions/)。

---

## [platform-security-third-party] 用户生成的词元

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/user-generated-tokens/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-user-generated-tokens.md`

# 用户生成的词元

这些词元与您个人的Foundry用户账户相关联，**不得在生产应用程序中使用或提交到共享或公共代码库中**。
我们建议您在开发期间将测试API词元存储为环境变量。
以授权生产应用程序，[注册一个OAuth2应用程序](/docs/foundry/platform-security-third-party/third-party-apps-overview/)。

## 概述

Foundry支持基于词元的身份验证。词元是字符的字符串，用作特定用户的安全标识。拥有这些词元相当于拥有用户的用户名和密码，因此应安全保管并保密。

## 生成

词元从设置仪表盘中生成。导航到侧边栏底部的**账户**，点击**设置**，然后点击**词元**。

此界面显示为当前用户创建的用户生成词元以及其当前状态和到期日期的信息。可以从此界面禁用现有词元，这将暂时停用它们，或撤销它们，这将永久失效。要生成新词元，点击**创建词元**。这将打开一个词元创建对话框：

为词元赋予一个有用的名称，提供描述，并指定词元应过期的日期。点击**生成**后，词元将只显示一次以确保安全。可以根据需要复制使用，但不应以任何不安全的方式存储。

## 撤销

您可以在同一界面通过点击**撤销**来撤销单个词元。

## 不活跃用户

默认情况下，Foundry用户账户在用户30天未登录后自动停用。当用户被停用时，用户生成的API词元和发给OAuth2客户端的词元将变为无效。

否则，用户将显示为完全活跃，并且由该用户安排的工作将继续运行。例如，不活跃用户拥有的计划将继续运行。

要重新激活用户，他们只需再次登录Foundry。

特定用户可以免于自动停用。有关这方面的更多信息，请联系您的Palantir代表。

---

## [platform-security-third-party] 为 Foundry 编写 OAuth2 客户端

- 官方原文：https://palantir.com/docs/zh/foundry/platform-security-third-party/writing-oauth2-clients/
- 存档文件：`01-Raw/Palantir/知识层/palantir-zh-platform-security-third-party-writing-oauth2-clients.md`

# 为 Foundry 编写 OAuth2 客户端

本文件面向希望编写 OAuth2 客户端以连接到 Foundry 的 Foundry 用户或管理员。此页面提供了 [OAuth 2.0 授权框架 ↗](https://www.rfc-editor.org/rfc/rfc6749) 的描述以及 Foundry OAuth2 实现的详细信息。此外，[Foundry 第三方应用程序和 API 协议](/docs/foundry/platform-security-third-party/3pa-api-guidance/) 管理在 Foundry 平台上使用第三方应用程序的规则，第三方应用程序的创建者和管理员应予以理解。

## OAuth2 概述

OAuth2 授权框架使第三方应用程序能够获得对服务的受控访问。OAuth2 通过提供一层机制，使客户端（如第三方应用程序）能够通过使用专门发行的访问词元和刷新词元请求访问，而不是用户的凭据或静态持有者词元，从而改进了传统的客户端-服务器授权模型。OAuth2 通过使用授权授予来管理此访问，授权授予是获取访问词元的方法。

## 支持 OAuth2 集成

以下部分描述了如何在第三方应用程序中支持 OAuth2。在整个文档中，**客户端**指代第三方应用程序，**授权服务器**指代 Foundry 的授权服务器，**用户**指代第三方应用程序的终端用户。

要在 Foundry 中使用 OAuth2，您必须按照[注册第三方应用程序](/docs/foundry/platform-security-third-party/register-3pa/)的说明注册您的应用程序，并在接下来的子部分中选择一种授权选项。

### 授权码授权

授权码授权允许客户端代表现有的 Foundry 用户执行操作。应用程序必须请求他们需要访问的 Foundry 权限集，然后 Foundry 用户必须明确授予客户端对其账户上那些权限的访问。Foundry 允许将客户端限制在用户可以访问的资源的有限集，或所有资源。

授权码授权的工作流程如下：

1. 客户端创建一个 `code_verifier` 和 `code_challenge`。对于可以安全存储客户端机密的*私密客户端↗*（如基于服务器的应用程序），这是**推荐的**但不是必需的。对于无法安全存储客户端机密的[*公共客户端*↗](https://tools.ietf.org/html/rfc6749#section-2.1)（如本机应用程序），这是**必需的**。
   * `code_verifier` 是一个加密随机字符串，包含 A-Z、a-z、0-9、`-`（连字符）、`.`（句号）、`_`（下划线）和 `~`（波浪号），长度为 43 到 128 个字符。
   * `code_challenge` 是通过对 `code_verifier` 执行 SHA256 然后转换为无填充的 Base64-URL 编码值派生得到的。
2. 客户端应用程序应打开浏览器并将用户发送到[授权端点](#authorization-endpoint)URL，并将以下参数作为查询参数添加：
   * `response_type`：应设置为 `code`。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `redirect_uri`：告知授权服务器在用户批准请求后将用户重定向到哪里。如果未指定，它将默认为 Foundry 中第三方应用程序设置中的第一个重定向 URI 值。
   * `scope`：定义请求的权限。在[API 文档](/docs/foundry/api/general/overview/introduction/)中为公共 API 提供的作用域。添加 `offline_access` 作用域以获取刷新词元。如果需要多个作用域，请使用空格作为分隔符连接这些作用域。
   * `state`：应用程序生成的随机字符串，将按原样返回给应用程序。应用程序应检查返回的值是否与原始字符串匹配，以防止 CSRF 攻击。
   * `code_challenge`：如果客户端创建了 `code_challenge`，则应填充此参数。授权服务器将内部将 `code_challenge` 参数与其生成的授权码关联。
   * `code_challenge_method`：应设置为 `S256`。
3. 当用户访问 URL 时，授权服务器会向用户显示类似于以下的提示，然后用户可以选择批准应用程序的请求。

4. 如果请求成功，授权服务器随后将用户重定向到指定的重定向 URI，并将以下参数作为查询参数添加：
   * `code`：这是授权服务器生成的授权码。
   * `state`：这是客户端在授权请求中传递的相同参数。客户端应检查其是否与请求中发送的原始 `state` 参数匹配。
5. 客户端随后应通过调用[词元端点](#token-endpoint)来交换授权码以获取访问词元。以下参数应使用 `application/x-www-form-urlencoded` 格式发送在请求正文中：
   * `grant_type`：应设置为 `authorization_code`。
   * `code`：从授权服务器接收到的代码。
   * `redirect_uri`：用户代理将重定向到的绝对 URI。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `code_verifier`：如果客户端生成了 `code_verifier`，则应在此请求中发送它。授权服务器将验证 `code_verifier` 是否匹配在先前请求中发送的 `code_challenge`。
6. 授权服务器随后会响应一个访问词元，客户端可以使用此词元访问请求的资源，如 REST API。响应包含以下参数：
   * `access_token`：客户端可以用来访问请求资源的词元。
   * `token_type`：发行的词元类型。
   * `expires_in`：访问词元的生命周期（以秒为单位）。
   * `refresh_token`：仅在请求的作用域包含 `offline_access` 时返回。如果客户端希望在用户不在场时刷新访问词元以授权请求，应使用此词元。有关更多信息，请参见[刷新访问词元](#refreshing-an-access-token)。

### 客户端凭证授权

客户端凭证授权专为非交互式服务用户样式的工作流程设计，其中客户端执行的操作不与正常的 Foundry 用户关联。客户端不代表正常的 Foundry 用户操作。

相反，此授权类型会自动创建一个与客户端关联的 Foundry 服务用户，然后可以为其授予访问 Foundry 资源的权限。通过此授权获得的词元可以用于代表创建的服务用户访问资源。服务用户账户的用户名与应用程序的客户端 ID 相同。

默认情况下，服务账户无权访问任何资源。Foundry 管理员必须为服务用户账户指派所需的角色和权限，以便客户端在 Foundry 中执行操作。

客户端凭证授权的工作流程如下：

1. 客户端调用[词元端点](#token-endpoint)。以下参数应使用 `application/x-www-form-urlencoded` 格式发送在请求正文中：
   * `grant_type`：应设置为 `client_credentials`。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `client_secret`：应设置为在 Foundry 中注册第三方应用程序时生成的客户端机密。
2. 授权服务器随后返回以下信息：
   * `access_token`：客户端可以用来访问请求资源的词元。
   * `token_type`：发行的词元类型。
   * `expires_in`：访问词元的生命周期（以秒为单位）。
3. 客户端随后可以使用访问词元访问请求的资源。

### 刷新访问词元

访问词元在一段时间后会过期，需要重新获取。任何在用户不在场时需要访问 Foundry API 的客户端都需要刷新词元。

这可以通过以下步骤完成：

1. 客户端应遵循[授权码授权](#authorization-code-grant)中概述的步骤，并将 `offline_access` 作为请求的 `scope` 参数的一部分进行指定。
2. 客户端应保存[授权码授权](#authorization-code-grant)最终步骤中返回的 `refresh_token`。
3. 如果访问词元过期，客户端随后可以通过调用[词元端点](#token-endpoint)端点并使用以下参数刷新词元：
   * `grant_type`：应设置为 `refresh_token`。
   * `refresh_token`：之前为给定用户获取的刷新词元。
   * `client_id`：应设置为在 Foundry 中注册第三方应用程序时生成的 ID。
   * `client_secret`：应设置为在 Foundry 中注册第三方应用程序时生成的客户端机密。
4. 授权服务器随后会响应以下信息：
   * `access_token` 客户端可以用来访问请求资源的词元。
   * `token_type`：发行的词元类型。
   * `expires_in`：访问词元的生命周期（以秒为单位）。
   * `refresh_token`：可以用来刷新访问词元的刷新词元。请注意，Foundry 每次使用先前发行的刷新词元时都会旋转刷新词元。请确保您保存了 `access_token` 和 `refresh_token`。

#### 刷新词元轮换

刷新词元可用于获取新的访问词元。Foundry 通过在每次使用先前发行的刷新词元时旋转刷新词元来降低与刷新词元相关的风险。
重用检测保护机制确保如果刷新词元在首次使用后一分钟内被重用，则由此授权授予创建的所有访问词元将失效，并且需要新的授权流程。
允许的一分钟重用间隔是为了应对可能的瞬态错误，如网络故障。此外，超过30天未使用的刷新词元会自动失效。这些安全措施通过确保没有长期存在的刷新词元来降低潜在被攻击的词元的风险。

## OAuth2 API 参考

以下端点可用于获取 OAuth2 词元。

### 授权端点

`GET /multipass/api/oauth2/authorize`

授权端点，供客户端用于获取授权码。

#### 查询参数

| 参数名称              | 类型     | 描述 |
|----------------------|--------|-----|
| response\_type        | 字符串  | 必须设置为 `code`。 |
| client\_id            | 字符串  | 客户端的唯一标识符。 |
| redirect\_uri         | 字符串  | 用户代理将重定向到的绝对 URI。必须与在控制面板中指定的重定向 URI 之一匹配。您可以通过导航到[管理应用程序](/docs/foundry/platform-security-third-party/manage-3pa/)屏幕再次访问此 URI。 |
| scope                | 字符串  | 要请求的权限范围。在[API 文档](/docs/foundry/api/general/overview/introduction/)中为公共 API 提供的作用域，应作为空格分隔的字符串列出。 |
| state                | 字符串 (非必填) | 传递给服务器的任意字符串，将按原样返回给客户端。这有助于防止跨站点请求伪造。 |
| code\_challenge       | 字符串 (非必填) | 由客户端生成的代码挑战；与[带有代码交换证明密钥的授权码授权 (PKCE)](#authorization-code-grant)一起使用 |
| code\_challenge\_method| 字符串 (非必填) | 如果使用 `code_challenge`，则应设置为 `S256`。 |

#### 重定向查询参数

如果请求成功，用户的浏览器会重定向到第三方应用程序设置中指定的重定向 URI 或请求中传递的重定向 URI。重定向请求 URI 中将存在以下查询参数：

| 参数名称 | 类型                 | 描述 |
|--------|--------------------|------|
| code   | 字符串             | 生成的授权码。此代码将在 10 分钟后失效。 |
| state  | 字符串 (非必填)    | 如果 `state` 参数存在于授权请求中，则此处将包含该确切值。 |

### 词元端点

`POST /multipass/api/oauth2/token`

词元端点由客户端用于通过提供其授权授予或刷新词元来获取访问词元。

#### 头参数

| 参数名称       | 描述 |
|---------------|-----|
| Content-Type  | 必须是 `application/x-www-form-urlencoded`。 |

#### 请求正文参数

| 参数名称        | 类型   | 描述 |
|----------------|------|-----|
| grant\_type     | 字符串 | 值必须是 `authorization_code`、`refresh_token` 或 `client_credentials` |
| code           | 字符串 (非必填) | 从授权端点接收到的授权码。如果授权类型是 `authorization_code`，这是必需的 |
| refresh\_token  | 字符串 (非必填) | 当 `grant_type` 是 `refresh_token` 时，这是必需的。值应为在最初的请求中获取授权码时获得的 `refresh_token`。 |
| redirect\_uri   | 字符串 (非必填/必填) | 用户代理将重定向到的绝对 URI。如果在授权请求中指定了重定向 URI，这是**必需的**。 |
| scope          | 字符串 (非必填) | 要请求的权限范围。在[API 文档](/docs/foundry/api/general/overview/introduction/)中为公共 API 提供的作用域，应作为空格分隔的字符串列出。 |
| client\_id      | 字符串            | 客户端的唯一标识符。 |
| client\_secret  | 字符串 (非必填) | 在应用程序注册期间发行的应用程序客户端机密。当 `grant_type` 是 `client_credentials` 时，这是必需的。 |
| code\_verifier  | 字符串 (非必填) | 应用程序在授权请求之前生成的用于 PKCE 请求的代码验证器。 |

#### 响应正文

响应 JSON 具有以下字段。

| 字段名称        | 类型     | 描述 |
|---------------|--------|-----|
| access\_token  | 字符串  | 用于访问资源的凭据。 |
| token\_type    | 字符串  | 发行的词元类型。 |
| expires\_in    | 字符串  | 访问词元的生命周期（以秒为单位）。 |
| refresh\_token | 字符串 (非必填) | 用于获取新访问词元的凭据。Foundry 每次调用 `refresh_token` 授权时都会旋转 `refresh_token`。请确保您保存了 `access_token` 和 `refresh_token`。 |

### 端点出错

#### 出错响应正文

如果请求失败，只有在访问请求被拒绝的情况下，用户的浏览器才会被重定向。在所有其他情况下，将返回包含以下字段的 HTML 出错页面。

| 字段名称             | 类型     | 描述                                    |
|-------------------|--------|----------------------------------------|
| error             | 字符串  | 如下节中定义的出错代码。                |
| error\_description | 字符串  | 出错的人类可读描述                      |

#### 出错代码

| 出错代码值                | 描述                                                    |
|--------------------------|---------------------------------------------------------|
| `invalid_request`        | 请求无效。                                              |
| `unauthorized_client`    | 客户端无权请求授权码。                                  |
| `access_denied`          | 服务器拒绝了请求。                                      |
| `unsupported_response_type` | 提供的响应类型不受支持。                              |
| `invalid_scope`          | 请求的范围无效、未知或格式错误。                        |
| `server_error`           | 发生意外的服务器出错。                                  |

## 英文原文对照索引

> 中文版是官方**机翻**（准确性未验证）；引用原句请用英文原文层。本节列全 45 篇的来源与原文路径对照。

| 中文来源文件 | 英文原文 |
|:---|:---|
| `palantir-zh-administration-overview.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-administration-overview.md` |
| `palantir-zh-getting-started.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started.md` |
| `palantir-zh-getting-started-application-reference.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-application-reference.md` |
| `palantir-zh-getting-started-authentication.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-authentication.md` |
| `palantir-zh-getting-started-debug-using-devtools.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-getting-started-delivering-a-use-case.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-delivering-a-use-case.md` |
| `palantir-zh-getting-started-file-support-ticket.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-file-support-ticket.md` |
| `palantir-zh-getting-started-http-error-codes.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-getting-started-introductory-concepts.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-introductory-concepts.md` |
| `palantir-zh-getting-started-issues.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-getting-started-network-requirements.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-getting-started-next-steps-by-role.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-next-steps-by-role.md` |
| `palantir-zh-getting-started-orientation-and-nav.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-orientation-and-nav.md` |
| `palantir-zh-getting-started-overview.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-overview.md` |
| `palantir-zh-getting-started-projects-and-resources.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-projects-and-resources.md` |
| `palantir-zh-getting-started-quicksearch.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-quicksearch.md` |
| `palantir-zh-getting-started-support-overview.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-getting-started-supported-browsers.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-getting-started-training-application.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-getting-started-training-application.md` |
| `palantir-zh-platform-overview.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-overview.md` |
| `palantir-zh-platform-overview-aip-capabilities.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-overview-aip-capabilities.md` |
| `palantir-zh-platform-overview-architecture.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-platform-overview-development-life-cycle.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-overview-development-life-cycle.md` |
| `palantir-zh-platform-overview-interoperability.md` | ⚠️ 英文版不存在（404），仅中文可查 |
| `palantir-zh-platform-overview-overview.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-overview-overview.md` |
| `palantir-zh-platform-security-management.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management.md` |
| `palantir-zh-platform-security-management-disabling-ignore-inherited-permissions.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-disabling-ignore-inherited-permissions.md` |
| `palantir-zh-platform-security-management-disabling-propagate-view-requirements.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-disabling-propagate-view-requirements.md` |
| `palantir-zh-platform-security-management-manage-groups.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-groups.md` |
| `palantir-zh-platform-security-management-manage-markings.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-markings.md` |
| `palantir-zh-platform-security-management-manage-orgs-and-spaces.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-orgs-and-spaces.md` |
| `palantir-zh-platform-security-management-manage-project-constraints.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-project-constraints.md` |
| `palantir-zh-platform-security-management-manage-restricted-views.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-restricted-views.md` |
| `palantir-zh-platform-security-management-manage-roles.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-roles.md` |
| `palantir-zh-platform-security-management-manage-users.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-management-manage-users.md` |
| `palantir-zh-platform-security-third-party.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party.md` |
| `palantir-zh-platform-security-third-party-3pa-api-guidance.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-3pa-api-guidance.md` |
| `palantir-zh-platform-security-third-party-authorizing-3pa-access.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-authorizing-3pa-access.md` |
| `palantir-zh-platform-security-third-party-danger-zone-actions.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-danger-zone-actions.md` |
| `palantir-zh-platform-security-third-party-enabling-3pa-access.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-enabling-3pa-access.md` |
| `palantir-zh-platform-security-third-party-manage-3pa.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-manage-3pa.md` |
| `palantir-zh-platform-security-third-party-register-3pa.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-register-3pa.md` |
| `palantir-zh-platform-security-third-party-third-party-apps-overview.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-third-party-apps-overview.md` |
| `palantir-zh-platform-security-third-party-user-generated-tokens.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-user-generated-tokens.md` |
| `palantir-zh-platform-security-third-party-writing-oauth2-clients.md` | ✅ `01-Raw/AI落地/Palantir-EN/知识层/palantir-en-platform-security-third-party-writing-oauth2-clients.md` |
