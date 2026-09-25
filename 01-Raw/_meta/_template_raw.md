---
title: "{{title}}"
keywords: []                     # LLM 从原文粗提取 5-8 个，优先匹配 _keywords.yaml 规范名
state:
  phase: raw                     # raw | draft | wiki（对应所在层级，永不改变）
  time_raw: "{{ISO8601}}"        # 入库时间
  time_draft: null               # ingest 到 02-Draft 时追加
  time_wiki: null                # promote 到 03-Wiki 时追加
source_url: "{{URL}}"
source_type: "{{article | video | paper | book | document | link}}"
source_platform: "{{bilibili | zhihu | juejin | wechat | github | other}}"
author: "{{作者}}"
author_id: ""
publish_date: "{{YYYY-MM-DD}}"
fetch_date: "{{YYYY-MM-DD}}"
notes: ""
priority: 3                      # 1-5（1 最高）
language: "zh"
---

# {{title}}

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

{{抓取到的完整原文}}

---

## 抓取备注

- 抓取时间：{{自动填充}}
- 抓取工具：{{web_extract / stealth / 手动导入}}
