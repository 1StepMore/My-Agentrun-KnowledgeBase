---
title: Sensitive Filter Middleware
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/middleware/built-in/sensitive-filter.md
---
# Sensitive Filter Middleware

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
