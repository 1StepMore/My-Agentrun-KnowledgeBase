---
title: opencode 官方文档汇编（英文原版） · 05-运维与排错
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-ecosystem.md
- VibeCoding/opencode/opencode-references.md
- VibeCoding/opencode/opencode-troubleshooting.md
- VibeCoding/opencode/opencode-windows-wsl.md
evidence: E1
domain: VibeCoding
keywords:
- opencode
- vibe-coding
- AI编程
- claude-code
state:
  phase: draft
  time_raw: 2026-09-23 02:44:23+08:00
  time_draft: 2026-09-23 03:14:06+08:00
  time_wiki: null
wiki_target: false
wiki_note: 双语冗余：中文版已消化并入库
---

> **汇编性质**：opencode 官方文档 官方原文 4 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## ecosystem

- 官方原文：https://opencode.ai/docs/ecosystem
- 存档：`01-Raw/VibeCoding/opencode/opencode-ecosystem.md`

A collection of community projects built on OpenCode.

:::note
Want to add your OpenCode related project to this list? Submit a PR.

You can also check out [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) and [opencode.cafe](https://opencode.cafe), a community that aggregates the ecosystem and community.

---

## Plugins

| Name                                                                                               | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [opencode-daytona](https://github.com/daytona/integrations/tree/main/packages/opencode-plugin)     | Automatically run OpenCode sessions in isolated Daytona sandboxes with git sync and live previews  |
| [opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session)                  | Automatically inject Helicone session headers for request grouping                                 |
| [opencode-type-inject](https://github.com/nick-vi/opencode-type-inject)                            | Auto-inject TypeScript/Svelte types into file reads with lookup tools                              |
| [opencode-openai-codex-auth](https://github.com/numman-ali/opencode-openai-codex-auth)             | Use your ChatGPT Plus/Pro subscription instead of API credits                                      |
| [opencode-gemini-auth](https://github.com/jenslys/opencode-gemini-auth)                            | Use your existing Gemini plan instead of API billing                                               |
| [opencode-antigravity-auth](https://github.com/NoeFabris/opencode-antigravity-auth)                | Use Antigravity's free models instead of API billing                                               |
| [opencode-devcontainers](https://github.com/athal7/opencode-devcontainers)                         | Multi-branch devcontainer isolation with shallow clones and auto-assigned ports                    |
| [opencode-google-antigravity-auth](https://github.com/shekohex/opencode-google-antigravity-auth)   | Google Antigravity OAuth Plugin, with support for Google Search, and more robust API handling      |
| [opencode-dynamic-context-pruning](https://github.com/Tarquinen/opencode-dynamic-context-pruning)  | Optimize token usage by pruning obsolete tool outputs                                              |
| [opencode-vibeguard](https://github.com/inkdust2021/opencode-vibeguard)                            | Redact secrets/PII into VibeGuard-style placeholders before LLM calls; restore locally             |
| [opencode-websearch-cited](https://github.com/ghoulr/opencode-websearch-cited.git)                 | Add native websearch support for supported providers with Google grounded style                    |
| [opencode-pty](https://github.com/shekohex/opencode-pty.git)                                       | Enables AI agents to run background processes in a PTY, send interactive input to them.            |
| [opencode-shell-strategy](https://github.com/JRedeker/opencode-shell-strategy)                     | Instructions for non-interactive shell commands - prevents hangs from TTY-dependent operations     |
| [opencode-wakatime](https://github.com/angristan/opencode-wakatime)                                | Track OpenCode usage with Wakatime                                                                 |
| [opencode-md-table-formatter](https://github.com/franlol/opencode-md-table-formatter/tree/main)    | Clean up markdown tables produced by LLMs                                                          |
| [opencode-morph-fast-apply](https://github.com/JRedeker/opencode-morph-fast-apply)                 | 10x faster code editing with Morph Fast Apply API and lazy edit markers                            |
| [opencode-morph-plugin](https://github.com/morphllm/opencode-morph-plugin)                         | Fast Apply editing, WarpGrep codebase search, and context compaction via Morph                     |
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)                                   | Background agents, pre-built LSP/AST/MCP tools, curated agents, Claude Code compatible             |
| [opencode-notificator](https://github.com/panta82/opencode-notificator)                            | Desktop notifications and sound alerts for OpenCode sessions                                       |
| [opencode-notifier](https://github.com/mohak34/opencode-notifier)                                  | Desktop notifications and sound alerts for permission, completion, and error events                |
| [opencode-zellij-namer](https://github.com/24601/opencode-zellij-namer)                            | AI-powered automatic Zellij session naming based on OpenCode context                               |
| [opencode-skillful](https://github.com/zenobi-us/opencode-skillful)                                | Allow OpenCode agents to lazy load prompts on demand with skill discovery and injection            |
| [opencode-supermemory](https://github.com/supermemoryai/opencode-supermemory)                      | Persistent memory across sessions using Supermemory                                                |
| [@plannotator/opencode](https://github.com/backnotprop/plannotator/tree/main/apps/opencode-plugin) | Interactive plan review with visual annotation and private/offline sharing                         |
| [@openspoon/subtask2](https://github.com/spoons-and-mirrors/subtask2)                              | Extend opencode /commands into a powerful orchestration system with granular flow control          |
| [opencode-scheduler](https://github.com/different-ai/opencode-scheduler)                           | Schedule recurring jobs using launchd (Mac) or systemd (Linux) with cron syntax                    |
| [opencode-conductor](https://github.com/derekbar90/opencode-conductor)                             | Protocol-Driven Workflow: Automation of the Context -> Spec -> Plan -> Implement lifecycle.        |
| [micode](https://github.com/vtemian/micode)                                                        | Structured Brainstorm → Plan → Implement workflow with session continuity                          |
| [octto](https://github.com/vtemian/octto)                                                          | Interactive browser UI for AI brainstorming with multi-question forms                              |
| [opencode-background-agents](https://github.com/kdcokenny/opencode-background-agents)              | Claude Code-style background agents with async delegation and context persistence                  |
| [opencode-notify](https://github.com/kdcokenny/opencode-notify)                                    | Native OS notifications for OpenCode – know when tasks complete                                    |
| [opencode-workspace](https://github.com/kdcokenny/opencode-workspace)                              | Bundled multi-agent orchestration harness – 16 components, one install                             |
| [opencode-worktree](https://github.com/kdcokenny/opencode-worktree)                                | Zero-friction git worktrees for OpenCode                                                           |
| [opencode-sentry-monitor](https://github.com/stolinski/opencode-sentry-monitor)                    | Trace and debug your AI agents with Sentry AI Monitoring                                           |
| [opencode-firecrawl](https://github.com/firecrawl/opencode-firecrawl)                              | Web scraping, crawling, and search via the Firecrawl CLI                                           |
| [opencode-jfrog-plugin](https://github.com/jfrog/opencode-jfrog-plugin)                            | JFrog Plugin for seamless integration of Opencode users to JFrog platform                          |
| [opencode-goal-plugin](https://github.com/willytop8/OpenCode-goal-plugin)                          | Session-scoped `/goal` workflow that keeps objectives in context and auto-continues until complete |
| [opencode-tavily](https://github.com/tavily-ai/opencode-tavily)                                    | Web search, extraction, crawling, and deep research via the Tavily CLI                             |

---

## Projects

| Name                                                                                       | Description                                                      |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [kimaki](https://github.com/remorses/kimaki)                                               | Discord bot to control OpenCode sessions, built on the SDK       |
| [opencode.nvim](https://github.com/NickvanDyke/opencode.nvim)                              | Neovim plugin for editor-aware prompts, built on the API         |
| [portal](https://github.com/hosenur/portal)                                                | Mobile-first web UI for OpenCode over Tailscale/VPN              |
| [opencode plugin template](https://github.com/zenobi-us/opencode-plugin-template/)         | Template for building OpenCode plugins                           |
| [opencode.nvim](https://github.com/sudo-tee/opencode.nvim)                                 | Neovim frontend for opencode - a terminal-based AI coding agent  |
| [ai-sdk-provider-opencode-sdk](https://github.com/ben-vargas/ai-sdk-provider-opencode-sdk) | Vercel AI SDK provider for using OpenCode via @opencode-ai/sdk   |
| [OpenChamber](https://github.com/btriapitsyn/openchamber)                                  | Web / Desktop App and VS Code Extension for OpenCode             |
| [OpenCode-Obsidian](https://github.com/mtymek/opencode-obsidian)                           | Obsidian plugin that embeds OpenCode in Obsidian's UI            |
| [OpenWork](https://github.com/different-ai/openwork)                                       | An open-source alternative to Claude Cowork, powered by OpenCode |
| [ocx](https://github.com/kdcokenny/ocx)                                                    | OpenCode extension manager with portable, isolated profiles.     |
| [CodeNomad](https://github.com/NeuralNomadsAI/CodeNomad)                                   | Desktop, Web, Mobile and Remote Client App for OpenCode          |

---

## Agents

| Name                                                              | Description                                                  |
| ----------------------------------------------------------------- | ------------------------------------------------------------ |
| [Agentic](https://github.com/Cluster444/agentic)                  | Modular AI agents and commands for structured development    |
| [opencode-agents](https://github.com/darrenhinde/opencode-agents) | Configs, prompts, agents, and plugins for enhanced workflows |

---

## references

- 官方原文：https://opencode.ai/docs/references
- 存档：`01-Raw/VibeCoding/opencode/opencode-references.md`

References give OpenCode access to directories outside the current project. Use them to make documentation, shared libraries, examples, or another repository available while you work.

References are configured by alias in `opencode.json` or `opencode.jsonc`.

```jsonc title="opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "references": {
    "docs": {
      "path": "../product-docs",
      "description": "Use for product behavior and documentation conventions",
    },
    "sdk": {
      "repository": "anomalyco/opencode-sdk-js",
      "branch": "main",
      "description": "Use for JavaScript SDK implementation details",
    },
  },
}
```

---

## Local directories

Use `path` to reference a local directory.

```jsonc title="opencode.jsonc"
{
  "references": {
    "docs": {
      "path": "../docs",
    },
  },
}
```

Paths can be:

- Relative to the config file that defines the reference
- Absolute, such as `/home/user/docs`
- Relative to your home directory, such as `~/docs`

You can also use a string shorthand:

```jsonc title="opencode.jsonc"
{
  "references": {
    "docs": "../docs",
  },
}
```

---

## Git repositories

Use `repository` to reference a Git repository. OpenCode materializes the repository in its local repository cache and makes the checked-out source available as a reference directory.

```jsonc title="opencode.jsonc"
{
  "references": {
    "effect": {
      "repository": "Effect-TS/effect",
      "branch": "main",
    },
  },
}
```

`repository` accepts Git URLs, host/path references, and GitHub `owner/repo` shorthand. The optional `branch` field selects a branch or ref. Without `branch`, OpenCode uses the repository's default branch.

You can use string shorthand when you do not need a branch, description, or other options:

```jsonc title="opencode.jsonc"
{
  "references": {
    "effect": "Effect-TS/effect",
  },
}
```

:::note
Git references are refreshed asynchronously. A newly configured repository may take a moment to finish cloning or updating.

---

## Describe usage

Add `description` to explain when an agent should use a reference.

```jsonc title="opencode.jsonc"
{
  "references": {
    "design-system": {
      "path": "../design-system",
      "description": "Use when implementing UI components or design tokens",
    },
  },
}
```

OpenCode includes references with descriptions in agent context. Descriptions should be short and specific enough to distinguish references with similar content. References without descriptions remain available through autocomplete and direct use, but are not advertised to agents.

---

## Hide autocomplete entries

Set `hidden` to `true` to omit a reference from `@` autocomplete in the TUI.

```jsonc title="opencode.jsonc"
{
  "references": {
    "internal": {
      "path": "../internal",
      "description": "Use for internal implementation details",
      "hidden": true,
    },
  },
}
```

`hidden` only affects autocomplete. A hidden reference with a description remains included in agent context.

---

## Use references

Configured references appear in TUI `@` autocomplete. Type `@alias` to attach the reference root, or `@alias/` to search for files inside it.

```text
Compare this implementation with @sdk/src/client.ts
```

Agents also receive the resolved paths and descriptions of configured references that have descriptions in their system context, so they can inspect a reference when it is relevant without you attaching it manually.

OpenCode automatically allows reference directories through its external-directory permission boundary. Normal tool permissions still apply; for example, an agent that cannot edit files does not gain edit access because a directory is configured as a reference.

---

## Configure fields

| Field         | Local | Git | Description                                      |
| ------------- | ----- | --- | ------------------------------------------------ |
| `path`        | Yes   | No  | Local reference directory                        |
| `repository`  | No    | Yes | Git URL, host/path, or GitHub `owner/repo` value |
| `branch`      | No    | Yes | Optional Git branch or ref                       |
| `description` | Yes   | Yes | Guidance describing when to use the reference    |
| `hidden`      | Yes   | Yes | Hide the reference from TUI `@` autocomplete     |

Reference aliases cannot be empty or contain `/`, whitespace, backticks, or commas.

---

## or

- 官方原文：https://opencode.ai/docs/troubleshooting
- 存档：`01-Raw/VibeCoding/opencode/opencode-troubleshooting.md`

To debug issues with OpenCode, start by checking the logs and local data it stores on disk.

---

## Logs

Log files are written to:

- **macOS/Linux**: `~/.local/share/opencode/log/`
- **Windows**: Press `WIN+R` and paste `%USERPROFILE%\.local\share\opencode\log`

Log files are named with timestamps (e.g., `2025-01-09T123456.log`) and the most recent 10 log files are kept.

You can set the log level with the `--log-level` command-line option to get more detailed debug information. For example, `opencode --log-level DEBUG`.

---

## Storage

opencode stores session data and other application data on disk at:

- **macOS/Linux**: `~/.local/share/opencode/`
- **Windows**: Press `WIN+R` and paste `%USERPROFILE%\.local\share\opencode`

This directory contains:

- `auth.json` - Authentication data like API keys, OAuth tokens
- `log/` - Application logs
- `project/` - Project-specific data like session and message data
  - If the project is within a Git repo, it is stored in `./<project-slug>/storage/`
  - If it is not a Git repo, it is stored in `./global/storage/`

---

## Uninstall

To uninstall the OpenCode CLI and remove its related files, run:

```bash
opencode uninstall
```

The command shows what will be removed and asks for confirmation. See the [CLI reference](/docs/cli#uninstall) for options to keep your configuration or application data.

To remove OpenCode Desktop, uninstall the application through your operating system's app management tools.

---

## Desktop app

OpenCode Desktop runs a local OpenCode server (the `opencode-cli` sidecar) in the background. Most issues are caused by a misbehaving plugin, a corrupted cache, or a bad server setting.

### Quick checks

- Fully quit and relaunch the app.
- If the app shows an error screen, click **Restart** and copy the error details.
- macOS only: `OpenCode` menu -> **Reload Webview** (helps if the UI is blank/frozen).

---

### Disable plugins

If the desktop app is crashing on launch, hanging, or behaving strangely, start by disabling plugins.

#### Check the global config

Open your global config file and look for a `plugin` key.

- **macOS/Linux**: `~/.config/opencode/opencode.jsonc` (or `~/.config/opencode/opencode.json`)
- **macOS/Linux** (older installs): `~/.local/share/opencode/opencode.jsonc`
- **Windows**: Press `WIN+R` and paste `%USERPROFILE%\.config\opencode\opencode.jsonc`

If you have plugins configured, temporarily disable them by removing the key or setting it to an empty array:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [],
}
```

#### Check plugin directories

OpenCode can also load local plugins from disk. Temporarily move these out of the way (or rename the folder) and restart the desktop app:

- **Global plugins**
  - **macOS/Linux**: `~/.config/opencode/plugins/`
  - **Windows**: Press `WIN+R` and paste `%USERPROFILE%\.config\opencode\plugins`
- **Project plugins** (only if you use per-project config)
  - `<your-project>/.opencode/plugins/`

If the app starts working again, re-enable plugins one at a time to find which one is causing the issue.

---

### Clear the cache

If disabling plugins doesn't help (or a plugin install is stuck), clear the cache so OpenCode can rebuild it.

1. Quit OpenCode Desktop completely.
2. Delete the cache directory:

- **macOS**: Finder -> `Cmd+Shift+G` -> paste `~/.cache/opencode`
- **Linux**: delete `~/.cache/opencode` (or run `rm -rf ~/.cache/opencode`)
- **Windows**: Press `WIN+R` and paste `%USERPROFILE%\.cache\opencode`

3. Restart OpenCode Desktop.

---

### Fix server connection issues

OpenCode Desktop can either start its own local server (default) or connect to a server URL you configured.

If you see a **"Connection Failed"** dialog (or the app never gets past the splash screen), check for a custom server URL.

#### Clear the desktop default server URL

From the Home screen, click the server name (with the status dot) to open the Server picker. In the **Default server** section, click **Clear**.

#### Remove `server.port` / `server.hostname` from your config

If your `opencode.json(c)` contains a `server` section, temporarily remove it and restart the desktop app.

#### Check environment variables

If you have `OPENCODE_PORT` set in your environment, the desktop app will try to use that port for the local server.

- Unset `OPENCODE_PORT` (or pick a free port) and restart.

---

### Linux: Wayland / X11 issues

On Linux, some Wayland setups can cause blank windows or compositor errors.

- If you're on Wayland and the app is blank/crashing, try launching with `OC_ALLOW_WAYLAND=1`.
- If that makes things worse, remove it and try launching under an X11 session instead.

---

### Windows: WebView2 runtime

On Windows, OpenCode Desktop requires the Microsoft Edge **WebView2 Runtime**. If the app opens to a blank window or won't start, install/update WebView2 and try again.

---

### Windows: General performance issues

If you're experiencing slow performance, file access issues, or terminal problems on Windows, try using [WSL (Windows Subsystem for Linux)](/docs/windows-wsl). WSL provides a Linux environment that works more seamlessly with OpenCode's features.

---

### Notifications not showing

OpenCode Desktop only shows system notifications when:

- notifications are enabled for OpenCode in your OS settings, and
- the app window is not focused.

---

### Reset desktop app storage (last resort)

If the app won't start and you can't clear settings from inside the UI, reset the desktop app's saved state.

1. Quit OpenCode Desktop.
2. Find and delete these files (they live in the OpenCode Desktop app data directory):

- `opencode.settings.dat` (desktop default server URL)
- `opencode.global.dat` and `opencode.workspace.*.dat` (UI state like recent servers/projects)

To find the directory quickly:

- **macOS**: Finder -> `Cmd+Shift+G` -> `~/Library/Application Support` (then search for the filenames above)
- **Linux**: search under `~/.local/share` for the filenames above
- **Windows**: Press `WIN+R` -> `%APPDATA%` (then search for the filenames above)

---

## Getting help

If you're experiencing issues with OpenCode:

1. **Report issues on GitHub**

   The best way to report bugs or request features is through our GitHub repository:

   [**github.com/anomalyco/opencode/issues**](https://github.com/anomalyco/opencode/issues)

   Before creating a new issue, search existing issues to see if your problem has already been reported.

2. **Join our Discord**

   For real-time help and community discussion, join our Discord server:

   [**opencode.ai/discord**](https://opencode.ai/discord)

---

## Common issues

Here are some common issues and how to resolve them.

---

### OpenCode won't start

1. Check the logs for error messages
2. Try running with `--print-logs` to see output in the terminal
3. Ensure you have the latest version with `opencode upgrade`

---

### Authentication issues

1. Try re-authenticating with the `/connect` command in the TUI
2. Check that your API keys are valid
3. Ensure your network allows connections to the provider's API

---

### Model not available

1. Check that you've authenticated with the provider
2. Verify the model name in your config is correct
3. Some models may require specific access or subscriptions

If you encounter `ProviderModelNotFoundError` you are most likely incorrectly
referencing a model somewhere.
Models should be referenced like so: `<providerId>/<modelId>`

Examples:

- `openai/gpt-4.1`
- `openrouter/google/gemini-2.5-flash`
- `opencode/kimi-k2`

To figure out what models you have access to, run `opencode models`

---

### ProviderInitError

If you encounter a ProviderInitError, you likely have an invalid or corrupted configuration.

To resolve this:

1. First, verify your provider is set up correctly by following the [providers guide](/docs/providers)
2. If the issue persists, try clearing your stored configuration:

   ```bash
   rm -rf ~/.local/share/opencode
   ```

   On Windows, press `WIN+R` and delete: `%USERPROFILE%\.local\share\opencode`

3. Re-authenticate with your provider using the `/connect` command in the TUI.

---

### AI_APICallError and provider package issues

If you encounter API call errors, this may be due to outdated provider packages. opencode dynamically installs provider packages (OpenAI, Anthropic, Google, etc.) as needed and caches them locally.

To resolve provider package issues:

1. Clear the provider package cache:

   ```bash
   rm -rf ~/.cache/opencode
   ```

   On Windows, press `WIN+R` and delete: `%USERPROFILE%\.cache\opencode`

2. Restart opencode to reinstall the latest provider packages

This will force opencode to download the most recent versions of provider packages, which often resolves compatibility issues with model parameters and API changes.

---

### Copy/paste not working on Linux

Linux users need to have one of the following clipboard utilities installed for copy/paste functionality to work:

**For X11 systems:**

```bash
apt install -y xclip
# or
apt install -y xsel
```

**For Wayland systems:**

```bash
apt install -y wl-clipboard
```

**For headless environments:**

```bash
apt install -y xvfb
# and run:
Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &
export DISPLAY=:99.0
```

opencode will detect if you're using Wayland and prefer `wl-clipboard`, otherwise it will try to find clipboard tools in order of: `xclip` and `xsel`.

---

## windows-wsl

- 官方原文：https://opencode.ai/docs/windows-wsl
- 存档：`01-Raw/VibeCoding/opencode/opencode-windows-wsl.md`

While OpenCode can run directly on Windows, we recommend using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) for the best experience. WSL provides a Linux environment that works seamlessly with OpenCode's features.

:::tip[Why WSL?]
WSL offers better file system performance, full terminal support, and compatibility with development tools that OpenCode relies on.

---

## Setup

1. **Install WSL**

   If you haven't already, [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) using the official Microsoft guide.

2. **Install OpenCode in WSL**

   Once WSL is set up, open your WSL terminal and install OpenCode using one of the [installation methods](/docs/).

   ```bash
   curl -fsSL https://opencode.ai/install | bash
   ```

3. **Use OpenCode from WSL**

   Navigate to your project directory (access Windows files via `/mnt/c/`, `/mnt/d/`, etc.) and run OpenCode.

   ```bash
   cd /mnt/c/Users/YourName/project
   opencode
   ```

---

## Desktop App + WSL Server

If you prefer using the OpenCode Desktop app but want to run the server in WSL:

1. **Start the server in WSL** with `--hostname 0.0.0.0` to allow external connections:

   ```bash
   opencode serve --hostname 0.0.0.0 --port 4096
   ```

2. **Connect the Desktop app** to `http://localhost:4096`

:::note
If `localhost` does not work in your setup, connect using the WSL IP address instead (from WSL: `hostname -I`) and use `http://<wsl-ip>:4096`.

:::caution
When using `--hostname 0.0.0.0`, set `OPENCODE_SERVER_PASSWORD` to secure the server.

```bash
OPENCODE_SERVER_PASSWORD=your-password opencode serve --hostname 0.0.0.0
```

---

## Web Client + WSL

For the best web experience on Windows:

1. **Run `opencode web` in the WSL terminal** rather than PowerShell:

   ```bash
   opencode web --hostname 0.0.0.0
   ```

2. **Access from your Windows browser** at `http://localhost:<port>` (OpenCode prints the URL)

Running `opencode web` from WSL ensures proper file system access and terminal integration while still being accessible from your Windows browser.

---

## Accessing Windows Files

WSL can access all your Windows files through the `/mnt/` directory:

- `C:` drive → `/mnt/c/`
- `D:` drive → `/mnt/d/`
- And so on...

Example:

```bash
cd /mnt/c/Users/YourName/Documents/project
opencode
```

:::tip
For the smoothest experience, consider cloning/copying your repo into the WSL filesystem (for example under `~/code/`) and running OpenCode there.

---

## Tips

- Keep OpenCode running in WSL for projects stored on Windows drives - file access is seamless
- Use VS Code's [WSL extension](https://code.visualstudio.com/docs/remote/wsl) alongside OpenCode for an integrated development workflow
- Your OpenCode config and sessions are stored within the WSL environment at `~/.local/share/opencode/`
