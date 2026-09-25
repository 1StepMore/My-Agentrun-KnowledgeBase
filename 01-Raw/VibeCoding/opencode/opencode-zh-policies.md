---
title: "opencode 官方文档 · Policies"
source: opencode 官方文档（官方一手文档）
source_url: https://opencode.ai/docs/zh-cn/policies
evidence: E1
domain: VibeCoding
lang: zh
keywords: ["opencode", "vibe-coding", "AI编程", "claude-code"]
state:
  phase: raw
  time_raw: 2026-09-23T02:44:23+08:00
  time_draft: 2026-09-23T02:45:52+08:00
  time_wiki: null
related:
---

> 溯源：opencode 官方文档 官方原文（证据等级 E1 = 官方一手）。抓取时间 2026-09-23T02:44:23+08:00。
> 原始地址：https://opencode.ai/docs/zh-cn/policies

# Policies

Control which configured resources OpenCode may use. 

此内容尚不支持你的语言。 

Policies control whether OpenCode may perform an action on a named resource. This feature is experimental and is configured with the experimental.policies array in opencode.json.

Policies are separate from permissions. Permissions control what tools can do during a session, while policies control whether OpenCode may use a resource such as an LLM provider.
 

## Configuration

Each policy statement has three fields:
 

- effect - Either "allow" or "deny".

- action - The operation being controlled.

- resource - The resource ID or wildcard pattern the statement applies to.
 

For example, deny use of the openai provider:
 opencode.json 

{ "$schema": "https://opencode.ai/config.json", "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "openai" } ] }}
A provider denied by policy is not available for model selection or model use, even if it has credentials or is otherwise configured correctly.
 

## Available Policies

OpenCode currently supports one policy action:

 Action Resource Description provider.use Provider ID, such as openai Allow or deny use of an LLM provider. 

More policy actions may be added in the future.
 

## Matching

The resource field supports wildcard matching. Use * to match zero or more characters and ? to match one character.
 opencode.json 

{ "$schema": "https://opencode.ai/config.json", "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "company-*" } ] }}
This denies providers such as company-us and company-eu.
 

## Rule Order

When multiple statements match, the last matching statement wins. Put broad rules first, then more specific exceptions after them.

For example, allow only Anthropic:
 opencode.json 

{ "$schema": "https://opencode.ai/config.json", "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "*" }, { "effect": "allow", "action": "provider.use", "resource": "anthropic" } ] }}
If no policy matches a provider, provider use is allowed by default.

Policies may be set in both your global config and project config. If policies from both locations match the same provider, your global policy takes priority over the project policy. This prevents a repository from re-enabling a provider that you deny globally.
 

## Provider Lists

Use policies instead of the older disabled_providers and enabled_providers settings when controlling provider access.

To replace disabled_providers:
 opencode.json 

{ "experimental": { "policies": [ { "effect": "deny", "action": "provider.use", "resource": "openai" }, { "effect": "deny", "action": "provider.use", "resource": "google" } ] }}
To replace enabled_providers, deny all providers first and allow the selected providers after it:
 opencode.json { "experimental" : { "policies" : [ { "effect" : "deny" , "action" : "provider.use" , "resource" : "*" }, { "effect" : "allow" , "action" : "provider.use" , "resource" : "anthropic" }, { "effect" : "allow" , "action" : "provider.use" , "resource" : "openai" } ] } }
