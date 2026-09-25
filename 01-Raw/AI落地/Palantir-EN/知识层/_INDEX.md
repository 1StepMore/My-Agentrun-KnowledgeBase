---
title: "Palantir 英文原文层（原文取证 · 不编译）"
source: Palantir 官方文档英文原文（E1）
evidence: E1
lang: en
domain: AI落地
keywords: [Palantir, Foundry, ontology-construction, semantic-layer]
compile: false
compile_note: "知识内容已由中文版汇编为 Draft（3 篇）；本层用于引用英文原句"
state:
  phase: raw
  time_raw: "2026-09-23T07:35:00+08:00"
  time_draft: null
  time_wiki: null
---

# Palantir 英文原文层（原文取证）

## 这一层是干什么的

中文版是**官方机器翻译**，页内明确声明"翻译的准确性尚未经过验证"。所以：

| 用途 | 用哪层 |
|:---|:---|
| 快速理解概念、检索 | 中文版 `01-Raw/AI落地/Palantir/知识层/` |
| **引用原句 / 术语定义 / 对客材料** | **本层（英文原文）** |

**本层不编译**：知识内容已由中文版汇编成 3 篇 Draft（本体论 / Foundry 平台 / 数据血缘），这里只作为**原文取证源**，避免同内容重复入库。

## 抓取情况（2026-09-23）

- 抓到 **126 篇**（中文知识层共 140 页）
- **14 页英文版不存在**（HTTP 404 / Page Not Found，官方英文站无对应页）→ 这些主题**只有中文可查**：
  `getting-started/*`（调试/devtools、HTTP 错误码、问题排查、网络要求、支持概览、受支持浏览器）
  `ontology-sdk/*`（应用指标、新建 OSDK、Java 引导、导航、OAuth 客户端、权限）
  `platform-overview/architecture`、`platform-overview/interoperability`
- 抓取方式：英文站不像中文站直接给 `.md`，原文藏在本站 HTML 的 `__NEXT_DATA__.props.pageProps.markdown`
- 脚本：`~/.hermes/scripts/palantir_en_ingest.py`

## 命名约定

`palantir-en-<原中文页 slug>.md` —— 保留同名 slug，**便于与中文页一一对照**（文件名里带 zh 的旧命名已改掉）。

## 缺口

- [ ] 14 篇仅中文页的"英文口径"无法从官方英文站取证（可选：从中文页回译时明确标注"回译"）
- [ ] `ontology-sdk` 系列在英文站缺失 → 若要用 SDK 相关概念，需另找官方英文来源（如 GitHub `palantir/osdk-ts`）
