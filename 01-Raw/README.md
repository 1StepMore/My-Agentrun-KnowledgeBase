---
title: "01-Raw · 原始素材层（层说明，非素材）"
kind: layer-index
material: false
keywords: [知识管理]
state:
  phase: raw
  time_raw: "2026-10-09T00:52:00+08:00"
---

# 01-Raw · 原始素材层

贴源保存的素材：视频转写、文档原文、网页抓取、官方文档汇编。**不做改写、不做解读**（一手来源改写会引入二手误差）。

## 本层规矩

- 每篇一个 `.md`，frontmatter 必须有 `keywords`（只写 `_keywords.yaml` 的规范名）、`state.phase: raw`
- 按来源/主题分子目录：`Bilibili/`（视频转写）· `VibeCoding/` · `AI服务商业化/` · `Loop-Engineering/` 等
- 文件命名：`<来源>-<标识>-<主题>.md`，如 `bilibili-BV1ahhz6VEHh-grok-bot-2000-prs-agent-software-factory.md`
- 中间产物（音频/转写件）放 workspace 的流水线工作目录，不放本层

## 相关

- 关键词受控词表：`../_keywords.yaml`（frontmatter 的 `keywords` **只能写这里的规范名**）
- 检索工具：`../_tools/kb_search.py`（三层检索 + 别名映射 + 语义扩展 + 未命中路由提示）
- 层级关系：`01-Raw` →（多对一收敛）→ `02-Draft` →（多对一收敛）→ `03-Wiki`
- 三层主题对照：`../三级主题对照表.md`
