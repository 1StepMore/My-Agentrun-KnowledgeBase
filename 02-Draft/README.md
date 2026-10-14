---
title: "02-Draft · 编译草稿层（层说明，非素材）"
kind: layer-index
material: false
source: "层说明文件：由知识库维护流程编写，无外部来源（非素材）"
keywords: [知识管理]
state:
  phase: draft
  time_raw: "2026-10-09T00:52:00+08:00"
  time_draft: "2026-10-09T00:52:00+08:00"
---

# 02-Draft · 编译草稿层

由 Raw 编译而成的结构化知识：概念合并、要点抽取、跨来源交叉印证。**允许解读**，但对每条结论标注来源与证据等级。

## 本层规矩

- **多篇 Raw → 一篇 Draft 是合法的**（多对一收敛，不是一对一管道）
- frontmatter `state.phase: draft`，并写 `time_draft`
- 上 Wiki 前的最后一道核对：事实、术语、数字都要能回溯到 Raw

## 相关

- 关键词受控词表：`../_keywords.yaml`（frontmatter 的 `keywords` **只能写这里的规范名**）
- 检索工具：`../_tools/kb_search.py`（三层检索 + 别名映射 + 语义扩展 + 未命中路由提示）
- 层级关系：`01-Raw` →（多对一收敛）→ `02-Draft` →（多对一收敛）→ `03-Wiki`
- 三层主题对照：`../三级主题对照表.md`
