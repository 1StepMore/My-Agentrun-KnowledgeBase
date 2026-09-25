---
title: Palantir 官方文档 · 对象与链接类型 · 值类型权限
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/object-link-types/value-types-permissions/
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

# 值类型权限

值类型的权限管理通过平台[空间](/docs/foundry/platform-security-management/manage-orgs-and-spaces/#space)进行。空间中的任何值类型都会自动导入并可用于关联的Ontology。其他使用者可以将值类型导入到他们的项目范围中，就像用户可以导入变换配置文件或管道输入一样。

具有某个空间`查看`（读取）权限的用户可以将值类型指派给该空间和关联Ontology中的属性类型或共享属性类型。空间的`编辑者`或`所有者`可以在该空间中创建、编辑或删除值类型。
