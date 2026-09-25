---
title: Palantir 官方文档（英文原版）· Export, edit, and import an Ontology
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/ontology-manager/export-import/
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
> 原始地址：https://palantir.com/docs/foundry/ontology-manager/export-import/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-ontology-manager-export-import.md`

# Export, edit, and import an Ontology

:::callout{theme="neutral"}
You should not depend on the exported JSON schema as it may change over time.
:::

Ontology schema definitions are stored in a [JSON file ↗](https://en.wikipedia.org/wiki/JSON). An Ontology JSON file can be exported and edited with a code editor or text editor before being imported back into Foundry. This import/export functionality enables two workflows for advanced users:

* If you prefer to make Ontology edits in code, you can bypass the Ontology Manager interface by exporting the Ontology JSON file, editing the JSON file directly in a code editor or text editor, and then importing the modified Ontology JSON file back into the platform.
* If you would like to copy the working state of one Ontology to another Ontology, you can export the Ontology’s current state as a JSON file and then import the copied JSON back into the platform (making any desired changes to the JSON in a code editor).

![Edit ontology JSON](/docs/resources/foundry/ontology-manager/import-export-edit-ontology-json.png)

## Export

You can export your Ontology working state by selecting the **Advanced** settings page from the application’s home page and then selecting **Export**.

:::callout{theme="neutral"}
Any changes you have in your working state will be included in the export.
:::

## Import

You can import a previously exported Ontology working state by selecting the **Advanced** settings page from the application’s home page and then selecting **Import**. You will be prompted to choose an Ontology file from your local drive.

Next, select **Import,** which will recreate the entire working state from the JSON file in the application. You will see the number of changes made in the file that need to be saved in the application header.

:::callout{theme="neutral"}
An exported Ontology working state with conditional formatting rules configured on its properties cannot be imported to an Ontology other than the one it was exported from.
:::

## Troubleshooting

### Error: `OntologyMetadata:UnreferencedRuleSets`

If you receive the error `OntologyMetadata:UnreferencedRuleSets`, you are trying to import an Ontology working state with conditional formatting rules that are not defined in that Ontology and cannot be transferred over. You will need to delete the conditional formatting rules from the Ontology working state before importing.
