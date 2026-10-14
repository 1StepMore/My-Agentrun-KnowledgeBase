---
title: "03-Wiki · 成品知识层（层说明，非素材）"
kind: layer-index
material: false
source: "层说明文件：由知识库维护流程编写，无外部来源（非素材）"
keywords: [知识管理]
state:
  phase: wiki
  time_raw: "2026-10-09T00:52:00+08:00"
  time_draft: "2026-10-09T00:52:00+08:00"
  time_wiki: "2026-10-09T00:52:00+08:00"
---

# 03-Wiki · 成品知识层

可直接对外引用/复用的成品条目：方法论、术语表、流程与治理。**检索默认优先返回本层**。

## 本层规矩

- frontmatter `state.phase: wiki` + `time_wiki`
- **多篇 Draft → 一篇 Wiki 同样合法**
- 本层是 `kb_search.py` 默认检索范围（`wiki` + `draft`；`01-Raw` 需加 `--raw`）

## 相关

- 关键词受控词表：`../_keywords.yaml`（frontmatter 的 `keywords` **只能写这里的规范名**）
- 检索工具：`../_tools/kb_search.py`（三层检索 + 别名映射 + 语义扩展 + 未命中路由提示）
- 层级关系：`01-Raw` →（多对一收敛）→ `02-Draft` →（多对一收敛）→ `03-Wiki`
- 三层主题对照：`../三级主题对照表.md`
