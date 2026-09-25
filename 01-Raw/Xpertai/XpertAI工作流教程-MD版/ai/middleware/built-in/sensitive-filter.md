---
title: Sensitive Filter Middleware
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:53:35'
  time_wiki: '2026-09-23T00:50:32'
source_url: AI生成
source_type: article
source_platform: xpertai
author: XpertAI
fetch_date: '2026-05-08'
priority: 3
language: zh
notes: XpertAI官方文档
author_id: ''
publish_date: ''
---
# Sensitive Filter Middleware

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Sensitive Filter Middleware

This tutorial covers `@xpert-ai/plugin-sensitive-filter` from `xpert-plugins`, used to filter sensitive content on both agent input and output stages.

## Typical Use Cases

* Filter PII such as ID numbers, phone numbers, and bank cards
* Block high-risk content directly
* Rewrite recoverable content into a safe response

## Install and Enable

1. Install the plugin package in your host project:

```bash theme={null}
npm install @xpert-ai/plugin-sensitive-filter
```

2. Enable the plugin through environment variables:

```bash theme={null}
PLUGINS=@xpert-ai/plugin-sensitive-filter
```

3. Follow [Publish & Use](/en/ai/plugin/install) to ensure the host loads the plugin.

## Runtime Hooks

* `beforeAgent`: evaluate and optionally rewrite/block input
* `wrapModelCall`: evaluate and optionally rewrite/block model output
* `afterAgent`: write audit snapshot

## Configuration Modes

The middleware has two mutually exclusive modes:

* `rule`: deterministic rules (`keyword` / `regex`)
* `llm`: natural-language policy evaluation (LLM hits are enforced in rewrite behavior)

### Minimal Rule Mode Example

```json theme={null}
{
  "mode": "rule",
  "caseSensitive": false,
  "normalize": true,
  "rules": [
    {
      "id": "rule-1",
      "pattern": "ID card",
      "type": "keyword",
      "scope": "both",
      "severity": "high",
      "action": "block",
      "replacementText": "Sensitive content was blocked."
    }
  ]
}
```

In `rule` mode, each rule should include:
`pattern`, `type`, `scope`, `severity`, and `action`.

### Minimal LLM Mode Example

```json theme={null}
{
  "mode": "llm",
  "llm": {
    "model": {
      "provider": "openai",
      "model": "gpt-4o-mini"
    },
    "scope": "both",
    "rulePrompt": "If content contains ID cards, phone numbers, bank cards, or home addresses, rewrite it into a privacy-safe response.",
    "rewriteFallbackText": "[Filtered]",
    "timeoutMs": 3000
  }
}
```

In `llm` mode, runtime-required fields are:
`model`, `scope`, and `rulePrompt`.

## Validation Checklist

1. Validate the hit path in `rule` mode first.
2. Then switch to `llm` mode and validate semantic policy behavior.
3. Verify that audit records include hit details for both input and output phases when expected.

## Troubleshooting

* No effect in `rule` mode: usually caused by incomplete rule fields or mismatched `scope`.
* No effect in `llm` mode: confirm `model`, `scope`, and `rulePrompt` are all present.
* Unexpected LLM rewrite behavior: inspect audit traces for policy fallback/error hints.


## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

## 关联问题

- 这个概念和其他知识有什么联系？
- 这个观点和我的已有认知是否冲突？

---

## 抓取备注

- 抓取时间：2026-05-08
- 抓取工具：手动导入
- 质量评分：
