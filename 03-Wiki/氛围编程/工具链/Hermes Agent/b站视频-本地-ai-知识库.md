---
keywords:
- knowledge-base
- bilibili
- setup
- beginner-tutorial
title: B站视频转本地AI知识库
state:
  phase: wiki
  time_raw: '2026-07-01T12:47:59'
  time_draft: '2026-07-01T12:47:59'
  time_wiki: '2026-07-01T12:47:59'
sources:
- Bilibili/bilibili-BV1g1dLBPEHV-bilibili-to-local-ai-knowledge-base.md
related:
- '[[LLM Wiki]]'
- '[[Carpenter LLM Wiki Vault]]'
- '[[Bilibili WebClipper]]'
- '[[Obsidian]]'
- '[[Local REST API]]'
- '[[双链笔记]]'
source: 历史文件，来源见 sources
evidence: E1
---

# B站视频转本地AI知识库

## 核心概念

1. **[[LLM Wiki]]** - Carpenter提出的核心理念，利用[[WebClipper]]将视频转化为[[Markdown]]格式笔记，让[[LLM]]能够理解和处理内容，实现知识互联与生长。

2. **[[Obsidian]]** - 本地知识库核心工具，支持[[双链笔记]]与图谱可视化，作为所有笔记的中央存储库。

3. **[[Carpenter LLM Wiki Vault]]** - 基于LLM Wiki理念构建的[[Obsidian]]模板，由UP主「效率工坊」开源，提供标准化的知识管理结构。

4. **[[Bilibili WebClipper]]** - 专门为B站开发的浏览器扩展，解决原生WebClipper无法解析B站页面结构的问题，支持Chrome/Edge/Firefox。

5. **[[WebClipper]]** - 网页剪藏工具，用于将网页内容提取并保存为结构化笔记格式。

6. **[[Local REST API]]** - Obsidian插件，为外部工具提供读写笔记库的接口，实现自动化工作流。

7. **双项链接与图谱构建** - Obsidian的核心功能，通过双向链接将笔记互联，自动生成知识图谱。

## 工作流程

```
B站视频 → Bilibili WebClipper → Markdown笔记 → Obsidian Vault → LLM可理解的知识库
```

**四步操作**：
1. 安装 Bilibili WebClipper 扩展
2. 打开任意B站视频页面
3. 点击扩展图标自动提取标题、字幕、简介
4. 文件自动存入 Vault，配合模板完成链接与图谱构建

## 总结

通过 [[Carpenter LLM Wiki]] 理念与 [[Bilibili WebClipper]] 工具的结合，终于解决了B站视频无法收入本地知识库的难题。完整工具链由 Obsidian、Local REST API、Carpenter Vault模板和Bilibili WebClipper四个组件构成，实现从视频抓取到AI可理解知识的完整闭环，让B站的优质学习资源能够像YouTube一样被系统性管理。
