---
title: "术语表 · AI 落地（Palantir 官方口径）"
source: Palantir 官方文档（一手）＋本库 FDE 实战营（E3，已标注）
evidence: E1
domain: AI落地
keywords: [Palantir, Foundry, ontology-construction, semantic-layer, digital-twin]
state:
  phase: wiki
  time_raw: "2026-09-23T00:00:00+08:00"
  time_draft: "2026-09-23T00:00:00+08:00"
  time_wiki: "2026-09-23T03:30:00+08:00"
related:
  - "[[_MOC-AI落地]]"
  - "[[palantir-本体论-Ontology官方体系]]"
---

# 术语表 · AI 落地

> **三个入口之一**：遇到不认识的词，先查这里，再顺着「出处」进权威原文。
> **E1** = Palantir 官方文档原文；**E3** = 社区/我们自己的提炼（已标注）。
> ⚠️ 中文释义来自 Palantir **官方机器翻译页**（官方声明"未经人工验证"）→ **引用请用 §六 的英文原句**。英文原文全文：`01-Raw/AI落地/Palantir-EN/知识层/`（140 页）

## 一、本体论核心（Palantir 官方 E1）

| 术语 | 官方定义 | 出处 |
|:---|:---|:---|
| **Ontology / 本体** | "Ontology 是对世界的分类。在 Foundry 中，Ontology 是组织的**数字孪生体**，是一个丰富的**语义层**，位于集成到 Foundry 中的数字资产（数据集和模型）之上。Foundry Ontology 通过将数据集和模型映射到 Object 类型、属性、链接类型和操作类型，创建了一个组织世界的完整图景。" | [ontology/core-concepts](https://palantir.com/docs/zh/foundry/ontology/core-concepts/) |
| **Object 类型** / Object / 对象集 | "**Object 类型**是一个真实世界实体或事件的**模式定义**。一个 **Object** 指的是一个 Object 类型的单个实例……一个**对象集**（object set）指的是多个 Object 实例的集合。" | 同上 |
| **属性（Property）/ 属性值 / 共享属性** | "一个 Object 类型的**属性**是一个真实世界实体或事件特征的**模式定义**。**属性值**指的是 Object 上属性的值。**共享属性**是可以在 Ontology 中的多个 Object 类型上使用的属性。" | 同上 |
| **链接类型（Link Type）/ 链接** | "**链接类型**是两个 Object 类型之间关系的**模式定义**。一个**链接**指的是两个 Object 之间该关系的单个实例。" | 同上 |
| **操作类型（Action Type）** | "**操作类型**是对 Object、属性值和链接进行一组更改或编辑的**模式定义**，用户可以一次执行。它还包括操作提交时发生的**副作用行为**。" | [action-types/overview](https://palantir.com/docs/zh/foundry/action-types/overview/) |
| **函数（Function）** | "**函数**是一段基于代码的逻辑，接受输入参数并返回输出。函数与 Ontology 本地集成：它们可以接受 Object 和对象集作为输入，读取 Object 的属性值，并可用于建立在 Ontology 上的操作类型和应用程序中。" | [functions/overview](https://palantir.com/docs/zh/foundry/functions/overview/) |
| **接口（Interface）** | "**接口**是描述 Object 类型及其功能的 Ontology 类型。接口提供 Object 类型的**多态性**，允许对具有共同形状的 Object 类型进行一致的建模和交互。" | [interfaces/overview](https://palantir.com/docs/zh/foundry/interfaces/interface-overview/) |
| **Object 视图** | "**Object 视图**是与特定 Object 相关的所有信息和工作流的**中心枢纽**。这包括关于一个 Object 的关键信息、任何链接的 Object 和相关指标，以及与该 Object 相关的分析、仪表盘和应用程序。" | [object-views/overview](https://palantir.com/docs/zh/foundry/object-views/overview/) |
| **角色（Role）** | "**角色**是 Ontology 中的**中心权限模型**。……角色可以在 Ontology 级别或单个资源级别授予。" | [ontologies/ontology-permissions](https://palantir.com/docs/zh/foundry/ontologies/ontology-permissions/) |

## 二、概念层（理解 Palantir 世界观的关键）

| 术语 | 说明 | 证据 |
|:---|:---|:---|
| **语义元素 / 动力元素** | 官方把本体拆成两类元素：**语义元素**（objects、属性、链接）定义"世界是什么"，**动力元素**（操作、函数、动态安全）定义"如何改变世界"。这是理解本体的骨架划分。 | E1 · [ontology/overview](https://palantir.com/docs/zh/foundry/ontology/overview/) |
| **数字孪生（Digital Twin）** | 官方用语的准确含义：Ontology 在许多情况下**充当组织的数字孪生体**——不是 3D 模型，而是"组织的操作层"。 | E1 |
| **语义层（Semantic Layer）** | 位于数字资产（数据集、模型）**之上**的一层，把数据映射为业务语义（Object/属性/链接）。卖点：远超"数据目录或模式设计"。 | E1 |
| **本体构建（ontology-construction）** | 本库自定术语：从原始文件/数据源到本体的工程化路径（见 [[从原始文件到语义模型的工程管道]]）。 | E3 · 我们的提炼 |

## 三、组织与交付（E3，标注为社区/自研）

| 术语 | 说明 | 证据 |
|:---|:---|:---|
| **FDE（Forward Deployed Engineer）** | 前置部署工程师：驻场客户、把通用平台能力翻译成客户具体价值。角色能力模型与现场方法论见 [[FDE的角色能力模型与现场实践]]、[[FDE实战营-组织与现场方法论]]。 | E3 |
| **交付与持续运营** | 项目交付不是终点，运营阶段的模型迭代/权限变更/用户培训同等重要：[[FDE实战营-交付与持续运营]]。 | E3 |

## 四、平台层补充（Palantir 官方 E1）

| 术语 | 官方定义 | 出处 |
|:---|:---|:---|
| **AIP 的三类功能（官方分类）** | ① **AIP Assist**：LLM 驱动的支持工具，用自然语言提问、实时获得查询帮助（侧边栏，`Ctrl/Cmd+Shift+U`）；② **平台应用内嵌的 AIP 助手**：核心应用里的原生 LLM 功能（Pipeline Builder 的"解释/正则助手/变换助手"、Notepad、Scheduler、AIP Threads[Beta]）；③ **自定义工作流的 AIP 功能**：面向开发者/数据科学家的开放式能力（如 Pipeline Builder 的 **LLM 节点**） | [aip-capabilities](https://palantir.com/docs/zh/foundry/platform-overview/aip-capabilities/) |
| **AIP（Palantir Artificial Intelligence Platform）** | 官方："**Palantir AIP 将生成式 AI 与运营连接在一起**"。与 **Foundry**（数据运营平台）、**Apollo**（自主软件部署的任务控制平台）同属一个 ***AI 网格***；三者合称 **Palantir 平台**。官方强调"关键的差异化因素是围绕 Ontology" | [platform-overview](https://palantir.com/docs/foundry/platform-overview/overview/) |

## 五、易混澄清（重要）

| 说法 | 结论 | 依据 |
|:---|:---|:---|
| **Ontology ≠ 知识图谱（Knowledge Graph）** | 官方文档**从不使用** "knowledge graph" 一词。全库检索（2411 个文件，含英文原版）：`knowledge graph` **0 命中**；`知识图谱` 仅 4 命中，**且全部出自我们自己的调研笔记**——即混用是我们引入的，不是官方口径。**对客表述应统一用 Ontology** | 本库全量 grep（2026-09-23）|

## 六、官方英文原句（可直引 · 2026-09-23 抓取）

> 上面是官方**中文机翻**（官方声明"未经人工验证"）。下面是**英文原文**，引用时请用这一组。
> 全文：`01-Raw/AI落地/Palantir-EN/知识层/`（140 页，E1 原文）

| 术语 | 官方英文原句 |
|:---|:---|
| **Ontology** | "An Ontology is **a categorization of the world**. In Foundry, the Ontology is **the digital twin of an organization**, integrating the organization's digital assets (datasets and models) into a coherent whole. The Foundry Ontology creates a complete picture of an organization's world by **mapping datasets and models to object types, properties, link types, and action types**." |
| **object type** | "An **object type** is **the schema definition of a real-world entity or event**." |
| **object / object instance** | "An **object** or **object instance** refers to **a single instance of an object type**." |
| **object set** | "An **object set** refers to **a collection of multiple object instances**." |
| **property** | "A **property** defines the object type's **characteristics**." |
| **link type** | "A **link type** defines **the relationship between two object types**." |
| **action type** | "An **action type** defines **how an object type can be modified**." |
| **Ontology（更准的定位）** | "The Palantir **Ontology** is an **operational layer** for the organization. The Ontology **sits on top of the digital assets** integrated into the Palantir platform (datasets, virtual tables, and models) and **connects them to their real-world counterparts**." ← **官方 overview 页的定位比"数字孪生"更强调"运营层"** |
| **link type / link** | "A **link type** is **the schema definition of a relationship between two object types**. A **link** refers to **a single instance of that relationship** between two objects in the same Ontology." |
| **property / property value** | "A **property** of an object type is **the schema definition of a characteristic** of a real-world entity or event. A **property value** refers to **the value of a property on an object**." |
| **shared property** | "A **shared property** is a property that **can be used on multiple object types**… allow for **consistent data modeling** across object types and **centralized management of property metadata**." |
| **value type** | "Dataset field types and property base types reflect the primitive types found in programming languages. These types are **domain-agnostic and provide no domain context**. By contrast, **value types capture the context and semantic meaning of data and centralize data validation**." |
| **struct** | "A **struct** is an Ontology property base type that **lets a single property hold several fields instead of one value**."（官方例：`Full Name` 可持有 `firstName` + `lastName`）|
| **type group / 类型组** | "Object type groups are **a classification primitive that helps users better search and explore their ontology**." |
| **title key** | "The **title key** is the property that **acts as a display name for objects of this type**."（官方例：把 `full name` 设为 `Employee` 的 title key）|
| **数字孪生（官方原句）** | "The Ontology represents the ***decisions*** in an enterprise, **not simply the data**."（官方 `why-ontology` 开篇——**这句最适合对客**） |

**官方给的"数据集 ↔ 本体"对照表**（理解本体的最短路径）：

| 数据集侧 | 本体侧 |
|:---|:---|
| dataset | **object type** |
| row | **object** |
| column | **property** |
| cell 值 | **property value** |
| join | **link** |

## 七、安全与集成层（Palantir 官方英文原句）

| 术语 | 官方定义 |
|:---|:---|
| **operations vs roles（最关键的一条）** | "**Operations** are **individual permissions** that Foundry applications check to verify a user has permission to perform a given action. **Roles** are **sets of operations**: when you grant someone a role on a resource (like a Project or a dataset), you are granting them **a set of operations on that resource and any child resources underneath it**." |
| **3PA（third-party application）** | "Foundry's **third-party application** authentication and authorization features enable **non-Foundry applications and scripts to interact securely with Foundry's APIs**. The core of these features is **OAuth2 support for external applications**." |
| **user-generated token** | 🔴 "These tokens are associated with your personal Foundry user account and **must not be used in production applications or committed to shared or public code repositories**." |
| **danger zone actions** | "…'danger zone' actions… **result in irreversible changes to an application's registration** and should be treated with caution due to their **potentially widespread and destructive effects**."（有二次确认弹窗） |
| **restricted view** | "**Restricted views** are similar to datasets but have some key differences. The contents combine **two dynamic factors: the policy definition and the user's attributes and group memberships at a specific point in time**." |
| **markings / 权限标记** | "Markings are managed in the Foundry **Settings** under the Markings section. Markings are then **applied on resources across the platform**." |
| **OSDK（Ontology SDK）** | "The **Ontology Software Development Kit (OSDK)** allows you to **access the full power of the Ontology directly from your development environment**." 支持：npm（TypeScript）/ pip 或 Conda（Python）/ Maven（Java）/ **OpenAPI spec（其他任何语言）** |

> 💡 **对交付最有用的一条**：**权限模型是"operation（最小权限）× role（操作的集合，含子资源继承）"**——对客讲权限设计时，先说清这两层，比讲"给谁什么角色"更专业。

## 缺口（不藏）

- **AIP 的模块清单**（AIP Logic / AIP Assist 等）→ 官方 `aip-capabilities` 页已入库，需要时展开
- **Foundry 侧数据术语**（pipeline / dataset / 血缘）→ 见 [[palantir-数据与血缘]]
- 与"知识图谱"的关系 → ✅ 已写成专条（见 §五，附全量检索证据）
