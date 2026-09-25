---
title: OpenAI Codex 官方文档 · config
source: OpenAI 官方仓库 openai/codex（一手）
source_url: https://github.com/openai/codex/blob/main/docs/config.md
evidence: E1
domain: VibeCoding
lang: en
keywords:
- openai
- codex
- vibe-coding
- AI编程
state:
  phase: raw
  time_raw: '2026-09-23T03:25:00+08:00'
  time_draft: 2026-09-23T03:02:07+08:00
  time_wiki: null
related: null
---

> 溯源：OpenAI 官方仓库 openai/codex 官方文档（证据等级 E1）。抓取 2026-09-23T03:25:00+08:00。
> 原始地址：https://github.com/openai/codex/blob/main/docs/config.md

# Configuration

For basic configuration instructions, see [this documentation](https://developers.openai.com/codex/config-basic).

For advanced configuration instructions, see [this documentation](https://developers.openai.com/codex/config-advanced).

For a full configuration reference, see [this documentation](https://developers.openai.com/codex/config-reference).

## Lifecycle hooks

Admins can set top-level `allow_managed_hooks_only = true` in
`requirements.toml` to ignore user, project, and session hook configs while
still allowing managed hooks from requirements and managed config layers. This
setting is only supported in `requirements.toml`; putting it in `config.toml`
does not enable managed-hooks-only mode.
