---
title: "Anthropic 开发者文档 · | `tool_configuration.allowed_tools` | array   | **Deprecated:** Use allowlist pattern with `configs` in MCPToolset | · Remote MCP servers"
source: Anthropic 开发者文档（官方一手，英文）
source_url: https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers
description: ": Connect Claude to third-party remote MCP servers through the MCP connector API. Browse example servers and review the steps to connect."
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
> 原始地址：https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers

Several companies have deployed remote MCP servers that developers can connect to by using the Anthropic MCP connector API. These servers expand the capabilities available to developers and end users by providing remote access to various services and tools through the MCP protocol.

<Note>
  The remote MCP servers listed below are third-party services designed to work with the Claude API. These servers are not owned, operated, or endorsed by Anthropic. Users should only connect to remote MCP servers they trust and should review each server's security practices and terms before connecting.
</Note>

## Connecting to remote MCP servers

To connect to a remote MCP server:

1. Review the documentation for the specific server you want to use.
2. Ensure you have the necessary authentication credentials.
3. Follow the server-specific connection instructions provided by each company.

For more information about using remote MCP servers with the Claude API, see [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector).

<Note>
  Once connected, remote MCP tools follow the same triggering behavior as any other tool. See [When Claude uses MCP tools](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#when-claude-uses-mcp-tools).
</Note>

## Remote MCP server examples

<MCPServersTable platform="mcpConnector" />

<Note>
  **Looking for more?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers).
</Note>


### MCP > MCP tunnels
