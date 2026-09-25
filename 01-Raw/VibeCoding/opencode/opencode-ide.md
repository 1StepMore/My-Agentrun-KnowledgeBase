---
title: "opencode 官方文档 · ide"
source: opencode 官方文档（官方一手文档）
source_url: https://opencode.ai/docs/ide
evidence: E1
domain: VibeCoding
lang: en
keywords: ["opencode", "vibe-coding", "AI编程", "claude-code"]
state:
  phase: raw
  time_raw: 2026-09-23T02:44:23+08:00
  time_draft: 2026-09-23T02:45:52+08:00
  time_wiki: null
related:
---

> 溯源：opencode 官方文档 官方原文（证据等级 E1 = 官方一手）。抓取时间 2026-09-23T02:44:23+08:00。
> 原始地址：https://opencode.ai/docs/ide

OpenCode integrates with VS Code, Cursor, or any IDE that supports a terminal. Just run `opencode` in the terminal to get started.

---

## Usage

- **Quick Launch**: Use `Cmd+Esc` (Mac) or `Ctrl+Esc` (Windows/Linux) to open OpenCode in a split terminal view, or focus an existing terminal session if one is already running.
- **New Session**: Use `Cmd+Shift+Esc` (Mac) or `Ctrl+Shift+Esc` (Windows/Linux) to start a new OpenCode terminal session, even if one is already open. You can also click the OpenCode button in the UI.
- **Context Awareness**: Automatically share your current selection or tab with OpenCode.
- **File Reference Shortcuts**: Use `Cmd+Option+K` (Mac) or `Alt+Ctrl+K` (Linux/Windows) to insert file references. For example, `@File#L37-42`.

---

## Installation

To install OpenCode on VS Code and popular forks like Cursor, Windsurf, VSCodium:

1. Open VS Code
2. Open the integrated terminal
3. Run `opencode` - the extension installs automatically

If on the other hand you want to use your own IDE when you run `/editor` or `/export` from the TUI, you'll need to set `export EDITOR="code --wait"`. [Learn more](/docs/tui/#editor-setup).

---

### Manual Install

Search for **OpenCode** in the Extension Marketplace and click **Install**.

---

### Troubleshooting

If the extension fails to install automatically:

- Ensure you’re running `opencode` in the integrated terminal.
- Confirm the CLI for your IDE is installed:
  - For VS Code: `code` command
  - For Cursor: `cursor` command
  - For Windsurf: `windsurf` command
  - For VSCodium: `codium` command
  - If not, run `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for "Shell Command: Install 'code' command in PATH" (or the equivalent for your IDE)
- Ensure VS Code has permission to install extensions
