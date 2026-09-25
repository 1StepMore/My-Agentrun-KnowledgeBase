---
title: "Anthropic 开发者文档 · CLI, SDKs, and libraries · CLI, SDKs, and libraries"
source: Anthropic 开发者文档（官方一手，英文）
source_url: https://platform.claude.com/docs/en/cli-sdks-libraries/overview
description: ": \"Official tools for building with the Claude API: the ant CLI, client SDKs in seven languages, and framework-specific libraries.\""
evidence: E1
domain: VibeCoding
lang: en
keywords: ["Anthropic", "AI-Agent", "prompt-engineering", "vibe-coding"]
state:
  phase: raw
  time_raw: 2026-09-23T03:00:00+08:00
  time_draft: 2026-09-23T02:51:20+08:00
  time_wiki: null
related:
---

> 溯源：Anthropic 官方文档全文（llms-full.txt 官方机器可读版，证据等级 E1）。抓取 2026-09-23T03:00:00+08:00。
> 原始地址：https://platform.claude.com/docs/en/cli-sdks-libraries/overview

Anthropic provides three kinds of official tooling for building with the Claude API:

* **CLI:** The `ant` command-line tool for shell scripting and interactive use.
* **Client SDKs:** General-purpose Messages API clients for Python, TypeScript, C#, Go, Java, PHP, and Ruby. Each SDK provides idiomatic interfaces, type safety, and built-in support for streaming, retries, and error handling.
* **Libraries and integrations:** Packages and compatibility layers that expose Claude inside another framework's API surface rather than the Messages API directly.

<Info>
  For the full API specification, see the [API reference](https://platform.claude.com/docs/en/api/overview).
</Info>

## CLI

<CardGroup cols={3}>
  <Card title="ant CLI" href="https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart">
    Shell scripting, typed flags, response transforms
  </Card>
</CardGroup>

## Client SDKs

<CardGroup cols={3}>
  <Card title="Python" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python">
    Sync and async clients, Pydantic models
  </Card>

  <Card title="TypeScript" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript">
    Node.js, Deno, Bun, and browser support
  </Card>

  <Card title="C#" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/csharp">
    .NET Standard 2.0+, IChatClient integration
  </Card>

  <Card title="Go" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go">
    Context-based cancellation, functional options
  </Card>

  <Card title="Java" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java">
    Builder pattern, CompletableFuture async
  </Card>

  <Card title="PHP" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php">
    Value objects, builder pattern
  </Card>

  <Card title="Ruby" href="https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby">
    Sorbet types, streaming helpers
  </Card>
</CardGroup>

## Libraries and integrations

Libraries and integrations expose Claude through another framework's API surface. They are not general-purpose Messages API clients.

<CardGroup cols={3}>
  <Card title="Apple Foundation Models" href="https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models">
    Swift package for Apple's `LanguageModelSession` API
  </Card>

  <Card title="OpenAI SDK compatibility" href="https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk">
    Use Claude through the OpenAI SDK surface
  </Card>
</CardGroup>

## Building agents or using Claude Code?

The CLI, client SDKs, and libraries are for calling the Claude API yourself: you send each request and handle each response. Claude Code, the Claude Agent SDK, and Claude Managed Agents work at a higher level, providing the agent loop, tool execution, and runtime.

<CardGroup cols={3}>
  <Card title="Claude Code" href="https://code.claude.com/docs/en/overview">
    Agentic coding tool for delegating coding tasks to Claude
  </Card>

  <Card title="Claude Agent SDK" href="https://code.claude.com/docs/en/agent-sdk/overview">
    Build agents that run in a process you operate
  </Card>

  <Card title="Claude Managed Agents" href="https://platform.claude.com/docs/en/managed-agents/overview">
    Run agents in Anthropic's managed infrastructure
  </Card>
</CardGroup>


### ant CLI
