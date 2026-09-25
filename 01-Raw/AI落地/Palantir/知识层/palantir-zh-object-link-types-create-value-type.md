---
title: Palantir 官方文档 · 对象与链接类型 · 创建值类型
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/object-link-types/create-value-type/
lang: zh
keywords:
- Palantir
- Foundry
- ontology-construction
- semantic-layer
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

# 创建值类型

按照以下步骤创建一个值类型，以便在您的平台[空间](/docs/foundry/security/orgs-and-spaces/#spaces)中使用。

1. 从平台侧边栏导航到**值类型管理器**应用程序。
2. 从左上角的下拉菜单中选择您希望创建值类型的空间。
3. 从右上角选择**创建新值类型**。
4. 为您的值类型提供一个清晰的名称、描述和唯一的API名称。

<img src="../../foundry-docs/object-link-types/media/value-type-create-metadata.png" alt="值类型元数据创建" width="500" />

5. 为您的值类型选择一个[基类型](/docs/foundry/object-link-types/type-reference/#base-types)。
6. （非必填）为您的值类型定义一个约束。验证器可以是`字符串`类型的正则表达式、枚举、范围或其他验证方法，具体取决于基类型。
   有关基类型支持的约束的完整列表，请查看我们的[值类型约束](/docs/foundry/object-link-types/value-type-constraints/)文档。

<img src="../../foundry-docs/object-link-types/media/value-type-create-constraint.png" alt="值类型约束创建" width="500" />

7. （非必填但推荐）为您的值类型提供一个示例预览值。

<img src="../../foundry-docs/object-link-types/media/value-type-create-preview.png" alt="值类型预览创建" width="500" />

8. 保存您的值类型。
