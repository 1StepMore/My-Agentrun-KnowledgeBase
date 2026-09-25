---
title: Palantir 官方文档 · platform-overview · 互操作性
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/platform-overview/interoperability/
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
