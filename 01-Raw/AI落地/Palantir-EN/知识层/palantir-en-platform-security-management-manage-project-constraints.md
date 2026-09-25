---
title: Palantir 官方文档（英文原版）· Manage Project constraints
source: Palantir 官方文档（英文原文，__NEXT_DATA__ clean markdown）
source_url: https://palantir.com/docs/foundry/platform-security-management/manage-project-constraints/
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
> 原始地址：https://palantir.com/docs/foundry/platform-security-management/manage-project-constraints/
> 中文对照：`01-Raw/AI落地/Palantir/知识层/palantir-zh-platform-security-management-manage-project-constraints.md`

# Manage Project constraints

To add a constraint on a Project, you must have an `Owner` role on the Project and add “Apply marking" permissions on all markings added as a Project constraint. You will not be able to add or modify a Project constraint if doing so would cause an existing file in the Project to be in violation of the constraint you are trying to add.

To manage constraints, navigate to the Markings section in the Access panel to the right.

![Project Constraints - Overview](/docs/resources/foundry/platform-security-management/pmc-1.png)

## Project constraint violations

After a Project constraint is applied, a dataset could still violate the Project constraint if a violating marking was added somewhere upstream and inherited by a dataset in the Project. This is surfaced by a warning on the dataset that is in violation. If the dataset violates the Project constraints, it cannot be built until the violation is resolved.

![A dataset in a Project is marked with a violation warning.](/docs/resources/foundry/platform-security-management/pmc-violation.png)

Project constraint violations can be resolved through the following actions:

* Add this inherited marking as an allowed Project constraint.
* Remove the inputs that introduce the new marking from the necessary transformations.
* Remove the inherited upstream marking. Learn how to [remove markings](/docs/foundry/building-pipelines/remove-markings/) in our documentation.
