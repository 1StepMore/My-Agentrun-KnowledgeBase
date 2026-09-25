---
title: opencode 官方文档汇编（英文原版） · 01-快速开始与核心概念
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-cli.md
- VibeCoding/opencode/opencode-commands.md
- VibeCoding/opencode/opencode-keybinds.md
- VibeCoding/opencode/opencode-models.md
- VibeCoding/opencode/opencode-providers.md
- VibeCoding/opencode/opencode-tui.md
- VibeCoding/opencode/opencode-zen.md
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

> **汇编性质**：opencode 官方文档 官方原文 7 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## Start the backend server for web/mobile access

- 官方原文：https://opencode.ai/docs/cli
- 存档：`01-Raw/VibeCoding/opencode/opencode-cli.md`

The OpenCode CLI by default starts the [TUI](/docs/tui) when run without any arguments.

```bash
opencode
```

But it also accepts commands as documented on this page. This allows you to interact with OpenCode programmatically.

```bash
opencode run "Explain how closures work in JavaScript"
```

---

### tui

Start the OpenCode terminal user interface.

```bash
opencode [project]
```

#### Flags

| Flag                                        | Short | Description                                                             |
| ------------------------------------------- | ----- | ----------------------------------------------------------------------- |
| <nobr><code>{"--continue"}</code></nobr>    | `-c`  | Continue the last session                                               |
| <nobr><code>{"--session"}</code></nobr>     | `-s`  | Session ID to continue                                                  |
| <nobr><code>{"--fork"}</code></nobr>        |       | Fork the session when continuing (use with `--continue` or `--session`) |
| <nobr><code>{"--prompt"}</code></nobr>      |       | Prompt to use                                                           |
| <nobr><code>{"--model"}</code></nobr>       | `-m`  | Model to use in the form of provider/model                              |
| <nobr><code>{"--agent"}</code></nobr>       |       | Agent to use                                                            |
| <nobr><code>{"--auto"}</code></nobr>        |       | Auto-approve permissions that are not explicitly denied                 |
| <nobr><code>{"--port"}</code></nobr>        |       | Port to listen on                                                       |
| <nobr><code>{"--hostname"}</code></nobr>    |       | Hostname to listen on                                                   |
| <nobr><code>{"--mdns"}</code></nobr>        |       | Enable mDNS discovery                                                   |
| <nobr><code>{"--mdns-domain"}</code></nobr> |       | Custom mDNS domain name                                                 |
| <nobr><code>{"--cors"}</code></nobr>        |       | Additional browser origin(s) to allow CORS                              |

---

## Commands

The OpenCode CLI also has the following commands.

---

### agent

Manage agents for OpenCode.

```bash
opencode agent [command]
```

---

#### create

Create a new agent with custom configuration.

```bash
opencode agent create
```

This command will guide you through creating a new agent with a custom system prompt and permission configuration. Anything you don't allow is denied in the generated agent's frontmatter.

#### Flags

| Flag                                        | Short | Description                                                                                                                                                                                                                |
| ------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <nobr><code>{"--path"}</code></nobr>        |       | Directory to write the agent file to (defaults to global or `.opencode/agent` based on the prompt)                                                                                                                         |
| <nobr><code>{"--description"}</code></nobr> |       | What the agent should do                                                                                                                                                                                                   |
| <nobr><code>{"--mode"}</code></nobr>        |       | Agent mode: `all`, `primary`, or `subagent`                                                                                                                                                                                |
| <nobr><code>{"--permissions"}</code></nobr> |       | Comma-separated list of permissions to allow (default: all). Available: `bash`, `read`, `edit`, `glob`, `grep`, `webfetch`, `task`, `todowrite`, `websearch`, `lsp`, `skill`. Anything omitted is denied. Alias: `--tools` |
| <nobr><code>{"--model"}</code></nobr>       | `-m`  | Model to use, in `provider/model` format                                                                                                                                                                                   |

Passing all of `--path`, `--description`, `--mode`, and `--permissions` runs the command non-interactively.

---

#### list

List all available agents.

```bash
opencode agent list
```

---

### attach

Attach a terminal to an already running OpenCode backend server started via `serve` or `web` commands.

```bash
opencode attach [url]
```

This allows using the TUI with a remote OpenCode backend. For example:

```bash
# Start the backend server for web/mobile access
opencode web --port 4096 --hostname 0.0.0.0

# In another terminal, attach the TUI to the running backend
opencode attach http://10.20.30.40:4096
```

#### Flags

| Flag                                     | Short | Description                                                                |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------- |
| <nobr><code>{"--dir"}</code></nobr>      |       | Working directory to start TUI in                                          |
| <nobr><code>{"--continue"}</code></nobr> | `-c`  | Continue the last session                                                  |
| <nobr><code>{"--session"}</code></nobr>  | `-s`  | Session ID to continue                                                     |
| <nobr><code>{"--fork"}</code></nobr>     |       | Fork the session when continuing (use with `--continue` or `--session`)    |
| <nobr><code>{"--password"}</code></nobr> | `-p`  | Basic auth password (defaults to `OPENCODE_SERVER_PASSWORD`)               |
| <nobr><code>{"--username"}</code></nobr> | `-u`  | Basic auth username (defaults to `OPENCODE_SERVER_USERNAME` or `opencode`) |

---

### auth

Command to manage credentials and login for providers.

```bash
opencode auth [command]
```

---

#### login

OpenCode is powered by the provider list at [Models.dev](https://models.dev), so you can use `opencode auth login` to configure API keys for any provider you'd like to use. This is stored in `~/.local/share/opencode/auth.json`.

```bash
opencode auth login
```

When OpenCode starts up it loads the providers from the credentials file. And if there are any keys defined in your environments or a `.env` file in your project.

##### Flags

| Flag                                     | Short | Description                                          |
| ---------------------------------------- | ----- | ---------------------------------------------------- |
| <nobr><code>{"--provider"}</code></nobr> | `-p`  | Provider ID or name to log in to                     |
| <nobr><code>{"--method"}</code></nobr>   | `-m`  | Login method label to use, skipping method selection |

---

#### list

Lists all the authenticated providers as stored in the credentials file.

```bash
opencode auth list
```

Or the short version.

```bash
opencode auth ls
```

---

#### logout

Logs you out of a provider by clearing it from the credentials file.

```bash
opencode auth logout
```

---

### github

Manage the GitHub agent for repository automation.

```bash
opencode github [command]
```

---

#### install

Install the GitHub agent in your repository.

```bash
opencode github install
```

This sets up the necessary GitHub Actions workflow and guides you through the configuration process. [Learn more](/docs/github).

---

#### run

Run the GitHub agent. This is typically used in GitHub Actions.

```bash
opencode github run
```

##### Flags

| Flag                                  | Description                            |
| ------------------------------------- | -------------------------------------- |
| <nobr><code>{"--event"}</code></nobr> | GitHub mock event to run the agent for |
| <nobr><code>{"--token"}</code></nobr> | GitHub personal access token           |

---

### mcp

Manage Model Context Protocol servers.

```bash
opencode mcp [command]
```

---

#### add

Add an MCP server to your configuration.

```bash
opencode mcp add
```

This command will guide you through adding either a local or remote MCP server.

---

#### list

List all configured MCP servers and their connection status.

```bash
opencode mcp list
```

Or use the short version.

```bash
opencode mcp ls
```

---

#### auth

Authenticate with an OAuth-enabled MCP server.

```bash
opencode mcp auth [name]
```

If you don't provide a server name, you'll be prompted to select from available OAuth-capable servers.

You can also list OAuth-capable servers and their authentication status.

```bash
opencode mcp auth list
```

Or use the short version.

```bash
opencode mcp auth ls
```

---

#### logout

Remove OAuth credentials for an MCP server.

```bash
opencode mcp logout [name]
```

---

#### debug

Debug OAuth connection issues for an MCP server.

```bash
opencode mcp debug <name>
```

---

### models

List all available models from configured providers.

```bash
opencode models [provider]
```

This command displays all models available across your configured providers in the format `provider/model`.

This is useful for figuring out the exact model name to use in [your config](/docs/config/).

You can optionally pass a provider ID to filter models by that provider.

```bash
opencode models anthropic
```

#### Flags

| Flag                                    | Description                                                  |
| --------------------------------------- | ------------------------------------------------------------ |
| <nobr><code>{"--refresh"}</code></nobr> | Refresh the models cache from models.dev                     |
| <nobr><code>{"--verbose"}</code></nobr> | Use more verbose model output (includes metadata like costs) |

Use the `--refresh` flag to update the cached model list. This is useful when new models have been added to a provider and you want to see them in OpenCode.

```bash
opencode models --refresh
```

---

### run

Run opencode in non-interactive mode by passing a prompt directly.

```bash
opencode run [message..]
```

This is useful for scripting, automation, or when you want a quick answer without launching the full TUI. For example.

```bash "opencode run"
opencode run Explain the use of context in Go
```

You can also attach to a running `opencode serve` instance to avoid MCP server cold boot times on every run:

```bash
# Start a headless server in one terminal
opencode serve

# In another terminal, run commands that attach to it
opencode run --attach http://localhost:4096 "Explain async/await in JavaScript"
```

#### Flags

| Flag                                     | Short | Description                                                                |
| ---------------------------------------- | ----- | -------------------------------------------------------------------------- |
| <nobr><code>{"--command"}</code></nobr>  |       | The command to run, use message for args                                   |
| <nobr><code>{"--continue"}</code></nobr> | `-c`  | Continue the last session                                                  |
| <nobr><code>{"--session"}</code></nobr>  | `-s`  | Session ID to continue                                                     |
| <nobr><code>{"--fork"}</code></nobr>     |       | Fork the session when continuing (use with `--continue` or `--session`)    |
| <nobr><code>{"--share"}</code></nobr>    |       | Share the session                                                          |
| <nobr><code>{"--model"}</code></nobr>    | `-m`  | Model to use in the form of provider/model                                 |
| <nobr><code>{"--agent"}</code></nobr>    |       | Agent to use                                                               |
| <nobr><code>{"--file"}</code></nobr>     | `-f`  | File(s) to attach to message                                               |
| <nobr><code>{"--format"}</code></nobr>   |       | Format: default (formatted) or json (raw JSON events)                      |
| <nobr><code>{"--title"}</code></nobr>    |       | Title for the session (uses truncated prompt if no value provided)         |
| <nobr><code>{"--attach"}</code></nobr>   |       | Attach to a running opencode server (e.g., http://localhost:4096)          |
| <nobr><code>{"--password"}</code></nobr> | `-p`  | Basic auth password (defaults to `OPENCODE_SERVER_PASSWORD`)               |
| <nobr><code>{"--username"}</code></nobr> | `-u`  | Basic auth username (defaults to `OPENCODE_SERVER_USERNAME` or `opencode`) |
| <nobr><code>{"--dir"}</code></nobr>      |       | Directory to run in, or path on the remote server when attaching           |
| <nobr><code>{"--port"}</code></nobr>     |       | Port for the local server (defaults to random port)                        |
| <nobr><code>{"--variant"}</code></nobr>  |       | Model variant (provider-specific reasoning effort)                         |
| <nobr><code>{"--thinking"}</code></nobr> |       | Show thinking blocks                                                       |
| <nobr><code>{"--auto"}</code></nobr>     |       | Auto-approve permissions that are not explicitly denied                    |

---

### serve

Start a headless OpenCode server for API access. Check out the [server docs](/docs/server) for the full HTTP interface.

```bash
opencode serve
```

This starts an HTTP server that provides API access to opencode functionality without the TUI interface. Set `OPENCODE_SERVER_PASSWORD` to enable HTTP basic auth (username defaults to `opencode`).

#### Flags

| Flag                                        | Description                                |
| ------------------------------------------- | ------------------------------------------ |
| <nobr><code>{"--port"}</code></nobr>        | Port to listen on                          |
| <nobr><code>{"--hostname"}</code></nobr>    | Hostname to listen on                      |
| <nobr><code>{"--mdns"}</code></nobr>        | Enable mDNS discovery                      |
| <nobr><code>{"--mdns-domain"}</code></nobr> | Custom mDNS domain name                    |
| <nobr><code>{"--cors"}</code></nobr>        | Additional browser origin(s) to allow CORS |

---

### session

Manage OpenCode sessions.

```bash
opencode session [command]
```

---

#### list

List all OpenCode sessions.

```bash
opencode session list
```

##### Flags

| Flag                                      | Short | Description                          |
| ----------------------------------------- | ----- | ------------------------------------ |
| <nobr><code>{"--max-count"}</code></nobr> | `-n`  | Limit to N most recent sessions      |
| <nobr><code>{"--format"}</code></nobr>    |       | Output format: table or json (table) |

---

#### delete

Delete an OpenCode session.

```bash
opencode session delete <sessionID>
```

---

### stats

Show token usage and cost statistics for your OpenCode sessions.

```bash
opencode stats
```

#### Flags

| Flag                                    | Description                                                                 |
| --------------------------------------- | --------------------------------------------------------------------------- |
| <nobr><code>{"--days"}</code></nobr>    | Show stats for the last N days (all time)                                   |
| <nobr><code>{"--tools"}</code></nobr>   | Number of tools to show (all)                                               |
| <nobr><code>{"--models"}</code></nobr>  | Show model usage breakdown (hidden by default). Pass a number to show top N |
| <nobr><code>{"--project"}</code></nobr> | Filter by project (all projects, empty string: current project)             |

---

### export

Export session data as JSON.

```bash
opencode export [sessionID]
```

If you don't provide a session ID, you'll be prompted to select from available sessions.

#### Flags

| Flag                                     | Description                           |
| ---------------------------------------- | ------------------------------------- |
| <nobr><code>{"--sanitize"}</code></nobr> | Redact sensitive transcript/file data |

---

### import

Import session data from a JSON file or OpenCode share URL.

```bash
opencode import <file>
```

You can import from a local file or an OpenCode share URL.

```bash
opencode import session.json
opencode import https://opncd.ai/s/abc123
```

---

### web

Start a headless OpenCode server with a web interface.

```bash
opencode web
```

This starts an HTTP server and opens a web browser to access OpenCode through a web interface. Set `OPENCODE_SERVER_PASSWORD` to enable HTTP basic auth (username defaults to `opencode`).

#### Flags

| Flag                                        | Description                                |
| ------------------------------------------- | ------------------------------------------ |
| <nobr><code>{"--port"}</code></nobr>        | Port to listen on                          |
| <nobr><code>{"--hostname"}</code></nobr>    | Hostname to listen on                      |
| <nobr><code>{"--mdns"}</code></nobr>        | Enable mDNS discovery                      |
| <nobr><code>{"--mdns-domain"}</code></nobr> | Custom mDNS domain name                    |
| <nobr><code>{"--cors"}</code></nobr>        | Additional browser origin(s) to allow CORS |

---

### acp

Start an ACP (Agent Client Protocol) server.

```bash
opencode acp
```

This command starts an ACP server that communicates via stdin/stdout using nd-JSON.

#### Flags

| Flag                                        | Description                                |
| ------------------------------------------- | ------------------------------------------ |
| <nobr><code>{"--cwd"}</code></nobr>         | Working directory                          |
| <nobr><code>{"--port"}</code></nobr>        | Port to listen on                          |
| <nobr><code>{"--hostname"}</code></nobr>    | Hostname to listen on                      |
| <nobr><code>{"--mdns"}</code></nobr>        | Enable mDNS discovery                      |
| <nobr><code>{"--mdns-domain"}</code></nobr> | Custom mDNS domain name                    |
| <nobr><code>{"--cors"}</code></nobr>        | Additional browser origin(s) to allow CORS |

---

### plugin

Install a plugin and update your config.

```bash
opencode plugin <module>
```

Or use the alias.

```bash
opencode plug <module>
```

#### Flags

| Flag                                   | Short | Description                     |
| -------------------------------------- | ----- | ------------------------------- |
| <nobr><code>{"--global"}</code></nobr> | `-g`  | Install in global config        |
| <nobr><code>{"--force"}</code></nobr>  | `-f`  | Replace existing plugin version |

---

### pr

Fetch and checkout a GitHub PR branch, then run OpenCode.

```bash
opencode pr <number>
```

---

### db

Database tools.

```bash
opencode db [query]
```

#### Flags

| Flag                                   | Description                    |
| -------------------------------------- | ------------------------------ |
| <nobr><code>{"--format"}</code></nobr> | Output format: `json` or `tsv` |

---

#### path

Print the database path.

```bash
opencode db path
```

---

### debug

Debugging and troubleshooting tools.

```bash
opencode debug [command]
```

---

### uninstall

Uninstall OpenCode and remove all related files.

```bash
opencode uninstall
```

#### Flags

| Flag                                        | Short | Description                                 |
| ------------------------------------------- | ----- | ------------------------------------------- |
| <nobr><code>{"--keep-config"}</code></nobr> | `-c`  | Keep configuration files                    |
| <nobr><code>{"--keep-data"}</code></nobr>   | `-d`  | Keep session data and snapshots             |
| <nobr><code>{"--dry-run"}</code></nobr>     |       | Show what would be removed without removing |
| <nobr><code>{"--force"}</code></nobr>       | `-f`  | Skip confirmation prompts                   |

---

### upgrade

Updates opencode to the latest version or a specific version.

```bash
opencode upgrade [target]
```

To upgrade to the latest version.

```bash
opencode upgrade
```

To upgrade to a specific version.

```bash
opencode upgrade v0.1.48
```

#### Flags

| Flag                                   | Short | Description                                                       |
| -------------------------------------- | ----- | ----------------------------------------------------------------- |
| <nobr><code>{"--method"}</code></nobr> | `-m`  | The installation method that was used; curl, npm, pnpm, bun, brew |

---

## Global Flags

The opencode CLI takes the following global flags.

| Flag                                       | Short | Description                          |
| ------------------------------------------ | ----- | ------------------------------------ |
| <nobr><code>{"--help"}</code></nobr>       | `-h`  | Display help                         |
| <nobr><code>{"--version"}</code></nobr>    | `-v`  | Print version number                 |
| <nobr><code>{"--print-logs"}</code></nobr> |       | Print logs to stderr                 |
| <nobr><code>{"--log-level"}</code></nobr>  |       | Log level (DEBUG, INFO, WARN, ERROR) |
| <nobr><code>{"--pure"}</code></nobr>       |       | Run without external plugins         |

---

## Environment variables

OpenCode can be configured using environment variables.

| Variable                              | Type    | Description                                       |
| ------------------------------------- | ------- | ------------------------------------------------- |
| `OPENCODE_AUTO_SHARE`                 | boolean | Automatically share sessions                      |
| `OPENCODE_GIT_BASH_PATH`              | string  | Path to Git Bash executable on Windows            |
| `OPENCODE_CONFIG`                     | string  | Path to config file                               |
| `OPENCODE_TUI_CONFIG`                 | string  | Path to TUI config file                           |
| `OPENCODE_CONFIG_DIR`                 | string  | Path to config directory                          |
| `OPENCODE_CONFIG_CONTENT`             | string  | Inline json config content                        |
| `OPENCODE_DISABLE_AUTOUPDATE`         | boolean | Disable automatic update checks                   |
| `OPENCODE_DISABLE_PRUNE`              | boolean | Disable pruning of old data                       |
| `OPENCODE_DISABLE_TERMINAL_TITLE`     | boolean | Disable automatic terminal title updates          |
| `OPENCODE_PERMISSION`                 | string  | Inlined json permissions config                   |
| `OPENCODE_DISABLE_DEFAULT_PLUGINS`    | boolean | Disable default plugins                           |
| `OPENCODE_DISABLE_LSP_DOWNLOAD`       | boolean | Disable automatic LSP server downloads            |
| `OPENCODE_ENABLE_EXPERIMENTAL_MODELS` | boolean | Enable experimental models                        |
| `OPENCODE_DISABLE_AUTOCOMPACT`        | boolean | Disable automatic context compaction              |
| `OPENCODE_DISABLE_CLAUDE_CODE`        | boolean | Disable reading from `.claude` (prompt + skills)  |
| `OPENCODE_DISABLE_CLAUDE_CODE_PROMPT` | boolean | Disable reading `~/.claude/CLAUDE.md`             |
| `OPENCODE_DISABLE_CLAUDE_CODE_SKILLS` | boolean | Disable loading `.claude/skills`                  |
| `OPENCODE_DISABLE_MODELS_FETCH`       | boolean | Disable fetching models from remote sources       |
| `OPENCODE_DISABLE_MOUSE`              | boolean | Disable mouse capture in the TUI                  |
| `OPENCODE_FAKE_VCS`                   | string  | Fake VCS provider for testing purposes            |
| `OPENCODE_CLIENT`                     | string  | Client identifier (defaults to `cli`)             |
| `OPENCODE_ENABLE_EXA`                 | boolean | Enable Exa web search tools                       |
| `OPENCODE_ENABLE_PARALLEL`            | boolean | Enable Parallel web search tools                  |
| `OPENCODE_SERVER_PASSWORD`            | string  | Enable basic auth for `serve`/`web`               |
| `OPENCODE_SERVER_USERNAME`            | string  | Override basic auth username (default `opencode`) |
| `OPENCODE_MODELS_URL`                 | string  | Custom URL for fetching models configuration      |

---

### Experimental

These environment variables enable experimental features that may change or be removed.

| Variable                                        | Type    | Description                             |
| ----------------------------------------------- | ------- | --------------------------------------- |
| `OPENCODE_EXPERIMENTAL`                         | boolean | Enable the experimental umbrella flag   |
| `OPENCODE_EXPERIMENTAL_ICON_DISCOVERY`          | boolean | Enable icon discovery                   |
| `OPENCODE_EXPERIMENTAL_DISABLE_COPY_ON_SELECT`  | boolean | Disable copy on select in TUI           |
| `OPENCODE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS` | number  | Default timeout for bash commands in ms |
| `OPENCODE_EXPERIMENTAL_OUTPUT_TOKEN_MAX`        | number  | Max output tokens for LLM responses     |
| `OPENCODE_EXPERIMENTAL_FILEWATCHER`             | boolean | Enable file watcher for entire dir      |
| `OPENCODE_EXPERIMENTAL_OXFMT`                   | boolean | Enable oxfmt formatter                  |
| `OPENCODE_EXPERIMENTAL_LSP_TOOL`                | boolean | Enable experimental LSP tool            |
| `OPENCODE_EXPERIMENTAL_DISABLE_FILEWATCHER`     | boolean | Disable file watcher                    |
| `OPENCODE_EXPERIMENTAL_EXA`                     | boolean | Enable experimental Exa features        |
| `OPENCODE_EXPERIMENTAL_LSP_TY`                  | boolean | Enable TY LSP for python files          |
| `OPENCODE_EXPERIMENTAL_PLAN_MODE`               | boolean | Enable plan mode                        |
| `OPENCODE_EXPERIMENTAL_BACKGROUND_SUBAGENTS`    | boolean | Enable background subagent tasks        |
| `OPENCODE_EXPERIMENTAL_EVENT_SYSTEM`            | boolean | Enable experimental event system        |
| `OPENCODE_EXPERIMENTAL_NATIVE_LLM`              | boolean | Enable native LLM request path          |
| `OPENCODE_EXPERIMENTAL_PARALLEL`                | boolean | Enable parallel web search execution    |
| `OPENCODE_EXPERIMENTAL_SCOUT`                   | boolean | Enable Scout subagent                   |
| `OPENCODE_EXPERIMENTAL_WORKSPACES`              | boolean | Enable workspace support                |

---

## commands

- 官方原文：https://opencode.ai/docs/commands
- 存档：`01-Raw/VibeCoding/opencode/opencode-commands.md`

Custom commands let you specify a prompt you want to run when that command is executed in the TUI.

```bash frame="none"
/my-command
```

Custom commands are in addition to the built-in commands like `/init`, `/undo`, `/redo`, `/share`, `/help`. [Learn more](/docs/tui#commands).

---

## Create command files

Create markdown files in the `commands/` directory to define custom commands.

Create `.opencode/commands/test.md`:

```md title=".opencode/commands/test.md"
---
description: Run tests with coverage
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

The frontmatter defines command properties. The content becomes the template.

Use the command by typing `/` followed by the command name.

```bash frame="none"
"/test"
```

---

## Configure

You can add custom commands through the OpenCode config or by creating markdown files in the `commands/` directory.

---

### JSON

Use the `command` option in your OpenCode [config](/docs/config):

```json title="opencode.jsonc" {4-12}
{
  "$schema": "https://opencode.ai/config.json",
  "command": {
    // This becomes the name of the command
    "test": {
      // This is the prompt that will be sent to the LLM
      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes.",
      // This is shown as the description in the TUI
      "description": "Run tests with coverage",
      "agent": "build",
      "model": "anthropic/claude-3-5-sonnet-20241022"
    }
  }
}
```

Now you can run this command in the TUI:

```bash frame="none"
/test
```

---

### Markdown

You can also define commands using markdown files. Place them in:

- Global: `~/.config/opencode/commands/`
- Per-project: `.opencode/commands/`

```markdown title="~/.config/opencode/commands/test.md"
---
description: Run tests with coverage
agent: build
model: anthropic/claude-3-5-sonnet-20241022
---

Run the full test suite with coverage report and show any failures.
Focus on the failing tests and suggest fixes.
```

The markdown file name becomes the command name. For example, `test.md` lets
you run:

```bash frame="none"
/test
```

---

## Prompt config

The prompts for the custom commands support several special placeholders and syntax.

---

### Arguments

Pass arguments to commands using the `$ARGUMENTS` placeholder.

```md title=".opencode/commands/component.md"
---
description: Create a new component
---

Create a new React component named $ARGUMENTS with TypeScript support.
Include proper typing and basic structure.
```

Run the command with arguments:

```bash frame="none"
/component Button
```

And `$ARGUMENTS` will be replaced with `Button`.

You can also access individual arguments using positional parameters:

- `$1` - First argument
- `$2` - Second argument
- `$3` - Third argument
- And so on...

For example:

```md title=".opencode/commands/create-file.md"
---
description: Create a new file with content
---

Create a file named $1 in the directory $2
with the following content: $3
```

Run the command:

```bash frame="none"
/create-file config.json src "{ \"key\": \"value\" }"
```

This replaces:

- `$1` with `config.json`
- `$2` with `src`
- `$3` with `{ "key": "value" }`

---

### Shell output

Use _!`command`_ to inject [bash command](/docs/tui#bash-commands) output into your prompt.

For example, to create a custom command that analyzes test coverage:

```md title=".opencode/commands/analyze-coverage.md"
---
description: Analyze test coverage
---

Here are the current test results:
!`npm test`

Based on these results, suggest improvements to increase coverage.
```

Or to review recent changes:

```md title=".opencode/commands/review-changes.md"
---
description: Review recent changes
---

Recent git commits:
!`git log --oneline -10`

Review these changes and suggest any improvements.
```

Commands run in your project's root directory and their output becomes part of the prompt.

---

### File references

Include files in your command using `@` followed by the filename.

```md title=".opencode/commands/review-component.md"
---
description: Review component
---

Review the component in @src/components/Button.tsx.
Check for performance issues and suggest improvements.
```

The file content gets included in the prompt automatically.

---

## Options

Let's look at the configuration options in detail.

---

### Template

The `template` option defines the prompt that will be sent to the LLM when the command is executed.

```json title="opencode.json"
{
  "command": {
    "test": {
      "template": "Run the full test suite with coverage report and show any failures.\nFocus on the failing tests and suggest fixes."
    }
  }
}
```

This is a **required** config option.

---

### Description

Use the `description` option to provide a brief description of what the command does.

```json title="opencode.json"
{
  "command": {
    "test": {
      "description": "Run tests with coverage"
    }
  }
}
```

This is shown as the description in the TUI when you type in the command.

---

### Agent

Use the `agent` config to optionally specify which [agent](/docs/agents) should execute this command.
If this is a [subagent](/docs/agents/#subagents) the command will trigger a subagent invocation by default.
To disable this behavior, set `subtask` to `false`.

```json title="opencode.json"
{
  "command": {
    "review": {
      "agent": "plan"
    }
  }
}
```

This is an **optional** config option. If not specified, defaults to your current agent.

---

### Subtask

Use the `subtask` boolean to force the command to trigger a [subagent](/docs/agents/#subagents) invocation.
This is useful if you want the command to not pollute your primary context and will **force** the agent to act as a subagent,
even if `mode` is set to `primary` on the [agent](/docs/agents) configuration.

```json title="opencode.json"
{
  "command": {
    "analyze": {
      "subtask": true
    }
  }
}
```

This is an **optional** config option.

---

### Model

Use the `model` config to override the default model for this command.

```json title="opencode.json"
{
  "command": {
    "analyze": {
      "model": "anthropic/claude-3-5-sonnet-20241022"
    }
  }
}
```

This is an **optional** config option.

---

## Built-in

opencode includes several built-in commands like `/init`, `/undo`, `/redo`, `/share`, `/help`; [learn more](/docs/tui#commands).

:::note
Custom commands can override built-in commands.

If you define a custom command with the same name, it will override the built-in command.

---

## keybinds

- 官方原文：https://opencode.ai/docs/keybinds
- 存档：`01-Raw/VibeCoding/opencode/opencode-keybinds.md`

OpenCode has a list of keybinds that you can customize through `tui.json`.

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "leader_timeout": 2000,
  "keybinds": {
    "leader": "ctrl+x",
    "app_exit": "ctrl+c,ctrl+d,<leader>q",
    "app_debug": "none",
    "app_console": "none",
    "app_heap_snapshot": "none",
    "app_toggle_animations": "none",
    "app_toggle_file_context": "none",
    "app_toggle_diffwrap": "none",
    "app_toggle_paste_summary": "none",
    "app_toggle_session_directory_filter": "none",
    "command_list": "ctrl+p",
    "help_show": "none",
    "docs_open": "none",

    "editor_open": "<leader>e",
    "theme_list": "<leader>t",
    "theme_switch_mode": "none",
    "theme_mode_lock": "none",
    "sidebar_toggle": "<leader>b",
    "scrollbar_toggle": "none",
    "status_view": "<leader>s",

    "session_export": "<leader>x",
    "session_copy": "none",
    "session_move": "none",
    "session_new": "<leader>n",
    "session_list": "<leader>l",
    "session_timeline": "<leader>g",
    "session_fork": "none",
    "session_rename": "ctrl+r",
    "session_delete": "ctrl+d",
    "session_share": "none",
    "session_unshare": "none",
    "session_interrupt": "escape",
    "session_compact": "<leader>c",
    "session_toggle_timestamps": "none",
    "session_toggle_generic_tool_output": "none",
    "session_child_first": "<leader>down",
    "session_child_cycle": "right",
    "session_child_cycle_reverse": "left",
    "session_parent": "up",

    "stash_delete": "ctrl+d",
    "model_provider_list": "ctrl+a",
    "model_favorite_toggle": "ctrl+f",
    "model_list": "<leader>m",
    "model_cycle_recent": "f2",
    "model_cycle_recent_reverse": "shift+f2",
    "model_cycle_favorite": "none",
    "model_cycle_favorite_reverse": "none",
    "mcp_list": "none",
    "provider_connect": "none",
    "console_org_switch": "none",
    "agent_list": "<leader>a",
    "agent_cycle": "tab",
    "agent_cycle_reverse": "shift+tab",
    "variant_cycle": "ctrl+t",
    "variant_list": "none",

    "messages_page_up": "pageup,ctrl+alt+b",
    "messages_page_down": "pagedown,ctrl+alt+f",
    "messages_line_up": "ctrl+alt+y",
    "messages_line_down": "ctrl+alt+e",
    "messages_half_page_up": "ctrl+alt+u",
    "messages_half_page_down": "ctrl+alt+d",
    "messages_first": "ctrl+g,home",
    "messages_last": "ctrl+alt+g,end",
    "messages_next": "none",
    "messages_previous": "none",
    "messages_last_user": "none",
    "messages_copy": "<leader>y",
    "messages_undo": "<leader>u",
    "messages_redo": "<leader>r",
    "messages_toggle_conceal": "<leader>h",
    "tool_details": "none",
    "display_thinking": "none",

    "prompt_submit": "none",
    "prompt_editor_context_clear": "none",
    "prompt_skills": "none",
    "prompt_stash": "none",
    "prompt_stash_pop": "none",
    "prompt_stash_list": "none",
    "workspace_set": "none",

    "input_clear": "ctrl+c",
    "input_paste": {
      "key": "ctrl+v",
      "preventDefault": false
    },
    "input_submit": "return",
    "input_newline": "shift+return,ctrl+return,alt+return,ctrl+j",
    "input_move_left": "left,ctrl+b",
    "input_move_right": "right,ctrl+f",
    "input_move_up": "up",
    "input_move_down": "down",
    "input_select_left": "shift+left",
    "input_select_right": "shift+right",
    "input_select_up": "shift+up",
    "input_select_down": "shift+down",
    "input_line_home": "ctrl+a",
    "input_line_end": "ctrl+e",
    "input_select_line_home": "ctrl+shift+a",
    "input_select_line_end": "ctrl+shift+e",
    "input_visual_line_home": "alt+a",
    "input_visual_line_end": "alt+e",
    "input_select_visual_line_home": "alt+shift+a",
    "input_select_visual_line_end": "alt+shift+e",
    "input_buffer_home": "home",
    "input_buffer_end": "end",
    "input_select_buffer_home": "shift+home",
    "input_select_buffer_end": "shift+end",
    "input_delete_line": "ctrl+shift+d",
    "input_delete_to_line_end": "ctrl+k",
    "input_delete_to_line_start": "ctrl+u",
    "input_backspace": "backspace,shift+backspace",
    "input_delete": "ctrl+d,delete,shift+delete",
    "input_undo": "ctrl+-,super+z",
    "input_redo": "ctrl+.,super+shift+z",
    "input_word_forward": "alt+f,alt+right,ctrl+right",
    "input_word_backward": "alt+b,alt+left,ctrl+left",
    "input_select_word_forward": "alt+shift+f,alt+shift+right",
    "input_select_word_backward": "alt+shift+b,alt+shift+left",
    "input_delete_word_forward": "alt+d,alt+delete,ctrl+delete",
    "input_delete_word_backward": "ctrl+w,ctrl+backspace,alt+backspace",
    "input_select_all": "super+a",
    "history_previous": "up",
    "history_next": "down",

    "dialog.select.prev": "up,ctrl+p",
    "dialog.select.next": "down,ctrl+n",
    "dialog.select.page_up": "pageup",
    "dialog.select.page_down": "pagedown",
    "dialog.select.home": "home",
    "dialog.select.end": "end",
    "dialog.select.submit": "return",
    "dialog.prompt.submit": "return",
    "dialog.mcp.toggle": "space",
    "prompt.autocomplete.prev": "up,ctrl+p",
    "prompt.autocomplete.next": "down,ctrl+n",
    "prompt.autocomplete.hide": "escape",
    "prompt.autocomplete.select": "return",
    "prompt.autocomplete.complete": "tab",
    "permission.prompt.fullscreen": "ctrl+f",
    "plugins.toggle": "space",
    "dialog.plugins.install": "shift+i",

    "terminal_suspend": "ctrl+z",
    "terminal_title_toggle": "none",
    "tips_toggle": "<leader>h",
    "plugin_manager": "none",
    "plugin_install": "none",

    "which_key_toggle": "ctrl+alt+k",
    "which_key_layout_toggle": "ctrl+alt+shift+k",
    "which_key_pending_toggle": "ctrl+alt+shift+p",
    "which_key_group_previous": "ctrl+alt+left,ctrl+alt+[",
    "which_key_group_next": "ctrl+alt+right,ctrl+alt+]",
    "which_key_scroll_up": "ctrl+alt+up,ctrl+alt+p",
    "which_key_scroll_down": "ctrl+alt+down,ctrl+alt+n",
    "which_key_page_up": "ctrl+alt+pageup",
    "which_key_page_down": "ctrl+alt+pagedown",
    "which_key_home": "ctrl+alt+home",
    "which_key_end": "ctrl+alt+end"
  }
}
```

:::note
On Windows, the defaults for `input_undo` and `terminal_suspend` are different:

- `input_undo` defaults to `ctrl+z,ctrl+-,super+z` when it is not explicitly configured. The `ctrl+z` binding is added because Windows terminals do not support POSIX suspend.
- `terminal_suspend` is forced to `none` because native Windows terminals do not support POSIX suspend.

---

## Leader Key

OpenCode uses a `leader` key for many keybinds. This avoids conflicts in your terminal.

By default, `ctrl+x` is the leader key and many actions require you to first press the leader key and then the shortcut. For example, to start a new session you first press `ctrl+x` and then press `n`.

You don't need to use a leader key for your keybinds but we recommend doing so.

Some navigation keybinds intentionally do not use the leader key by default. For subagent sessions, the defaults are `session_child_first` = `<leader>down`, `session_child_cycle` = `right`, `session_child_cycle_reverse` = `left`, and `session_parent` = `up`.

`leader_timeout` controls how long OpenCode waits for the next key after the leader key. It defaults to `2000` milliseconds.

---

## Binding Values

A string can contain one shortcut or multiple comma-separated shortcuts. You can also use an array for multiple shortcuts.

For advanced cases, use an object with `key`, `event`, `preventDefault`, or `fallthrough`.

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "messages_copy": ["<leader>y", "ctrl+shift+c"],
    "input_paste": {
      "key": "ctrl+v",
      "preventDefault": false
    }
  }
}
```

---

## Disable Keybind

You can disable a keybind by adding the key to `tui.json` with a value of `"none"` or `false`.

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "keybinds": {
    "session_compact": "none"
  }
}
```

---

## Desktop Prompt Shortcuts

The OpenCode desktop app prompt input supports common Readline/Emacs-style shortcuts for editing text. These are built-in and currently not configurable via `opencode.json`.

| Shortcut | Action                                   |
| -------- | ---------------------------------------- |
| `ctrl+a` | Move to start of current line            |
| `ctrl+e` | Move to end of current line              |
| `ctrl+b` | Move cursor back one character           |
| `ctrl+f` | Move cursor forward one character        |
| `alt+b`  | Move cursor back one word                |
| `alt+f`  | Move cursor forward one word             |
| `ctrl+d` | Delete character under cursor            |
| `ctrl+k` | Kill to end of line                      |
| `ctrl+u` | Kill to start of line                    |
| `ctrl+w` | Kill previous word                       |
| `alt+d`  | Kill next word                           |
| `ctrl+t` | Transpose characters                     |
| `ctrl+g` | Cancel popovers / abort running response |

---

## Shift+Enter

Some terminals don't send modifier keys with Enter by default. You may need to configure your terminal to send `Shift+Enter` as an escape sequence.

### Windows Terminal

Open your `settings.json` at:

```
%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
```

Add this to the root-level `actions` array:

```json
"actions": [
  {
    "command": {
      "action": "sendInput",
      "input": "\u001b[13;2u"
    },
    "id": "User.sendInput.ShiftEnterCustom"
  }
]
```

Add this to the root-level `keybindings` array:

```json
"keybindings": [
  {
    "keys": "shift+enter",
    "id": "User.sendInput.ShiftEnterCustom"
  }
]
```

Save the file and restart Windows Terminal or open a new tab.

---

## models

- 官方原文：https://opencode.ai/docs/models
- 存档：`01-Raw/VibeCoding/opencode/opencode-models.md`

OpenCode uses the [AI SDK](https://ai-sdk.dev/) and [Models.dev](https://models.dev) to support **75+ LLM providers** and it supports running local models.

---

## Providers

Most popular providers are preloaded by default. If you've added the credentials for a provider through the `/connect` command, they'll be available when you start OpenCode.

Learn more about [providers](/docs/providers).

---

## Select a model

Once you've configured your provider you can select the model you want by typing in:

```bash frame="none"
/models
```

---

## Recommended models

There are a lot of models out there, with new models coming out every week.

:::tip
Consider using one of the models we recommend.

However, there are only a few of them that are good at both generating code and tool calling.

Here are several models that work well with OpenCode, in no particular order. (This is not an exhaustive list nor is it necessarily up to date):

- GPT 5.2
- GPT 5.1 Codex
- Claude Opus 4.5
- Claude Sonnet 4.5
- Minimax M2.1
- Gemini 3 Pro

---

## Set a default

To set one of these as the default model, you can set the `model` key in your
OpenCode config.

```json title="opencode.json" {3}
{
  "$schema": "https://opencode.ai/config.json",
  "model": "lmstudio/google/gemma-3n-e4b"
}
```

Here the full ID is `provider_id/model_id`. For example, if you're using [OpenCode Zen](/docs/zen), you would use `opencode/gpt-5.1-codex` for GPT 5.1 Codex.

If you've configured a [custom provider](/docs/providers#custom), the `provider_id` is key from the `provider` part of your config, and the `model_id` is the key from `provider.models`.

---

## Configure models

You can globally configure a model's options through the config.

```jsonc title="opencode.jsonc" {7-12,19-24}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "openai": {
      "models": {
        "gpt-5": {
          "options": {
            "reasoningEffort": "high",
            "textVerbosity": "low",
            "reasoningSummary": "auto",
            "include": ["reasoning.encrypted_content"],
          },
        },
      },
    },
    "anthropic": {
      "models": {
        "claude-sonnet-4-5-20250929": {
          "options": {
            "thinking": {
              "type": "enabled",
              "budgetTokens": 16000,
            },
          },
        },
      },
    },
  },
}
```

Here we're configuring global settings for two built-in models: `gpt-5` when accessed via the `openai` provider, and `claude-sonnet-4-20250514` when accessed via the `anthropic` provider.
The built-in provider and model names can be found on [Models.dev](https://models.dev).

You can also configure these options for any agents that you are using. The agent config overrides any global options here. [Learn more](/docs/agents/#additional).

You can also define custom variants that extend built-in ones. Variants let you configure different settings for the same model without creating duplicate entries:

```jsonc title="opencode.jsonc" {6-21}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "opencode": {
      "models": {
        "gpt-5": {
          "variants": {
            "high": {
              "reasoningEffort": "high",
              "textVerbosity": "low",
              "reasoningSummary": "auto",
            },
            "low": {
              "reasoningEffort": "low",
              "textVerbosity": "low",
              "reasoningSummary": "auto",
            },
          },
        },
      },
    },
  },
}
```

---

## Variants

Many models support multiple variants with different configurations. OpenCode ships with built-in default variants for popular providers.

### Built-in variants

OpenCode ships with default variants for many providers:

**Anthropic**:

- `high` - High thinking budget (default)
- `max` - Maximum thinking budget

**OpenAI**:

Varies by model but roughly:

- `none` - No reasoning
- `minimal` - Minimal reasoning effort
- `low` - Low reasoning effort
- `medium` - Medium reasoning effort
- `high` - High reasoning effort
- `xhigh` - Extra high reasoning effort

**Google**:

- `low` - Lower effort/token budget
- `high` - Higher effort/token budget

:::tip
This list is not comprehensive. Many other providers have built-in defaults too.

### Custom variants

You can override existing variants or add your own:

```jsonc title="opencode.jsonc" {7-18}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "openai": {
      "models": {
        "gpt-5": {
          "variants": {
            "thinking": {
              "reasoningEffort": "high",
              "textVerbosity": "low",
            },
            "fast": {
              "disabled": true,
            },
          },
        },
      },
    },
  },
}
```

### Cycle variants

Use the keybind `variant_cycle` to quickly switch between variants. [Learn more](/docs/keybinds).

---

## Loading models

When OpenCode starts up, it checks for models in the following priority order:

1. The `--model` or `-m` command line flag. The format is the same as in the config file: `provider_id/model_id`.

2. The model list in the OpenCode config.

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "model": "anthropic/claude-sonnet-4-20250514"
   }
   ```

   The format here is `provider/model`.

3. The last used model.

4. The first model using an internal priority.

---

## providers

- 官方原文：https://opencode.ai/docs/providers
- 存档：`01-Raw/VibeCoding/opencode/opencode-providers.md`

export const console = config.console

OpenCode uses the [AI SDK](https://ai-sdk.dev/) and [Models.dev](https://models.dev) to support **75+ LLM providers** and it supports running local models.

To add a provider you need to:

1. Add the API keys for the provider using the `/connect` command.
2. Configure the provider in your OpenCode config.

---

### Credentials

When you add a provider's API keys with the `/connect` command, they are stored
in `~/.local/share/opencode/auth.json`.

---

### Config

You can customize the providers through the `provider` section in your OpenCode
config.

---

#### Base URL

You can customize the base URL for any provider by setting the `baseURL` option. This is useful when using proxy services or custom endpoints.

```json title="opencode.json" {6}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "options": {
        "baseURL": "https://api.anthropic.com/v1"
      }
    }
  }
}
```

---

#### Hiding models

You can hide specific models from the `/models` picker for a provider using the `blacklist` option. This is useful when a provider exposes models you don't want to use or select.

```json title="opencode.json" {6}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "blacklist": ["claude-opus-4-20250514"]
    }
  }
}
```

The inverse `whitelist` option hides every model except the ones listed.

```json title="opencode.json" {6}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "anthropic": {
      "whitelist": ["claude-sonnet-4-20250514"]
    }
  }
}
```

Both options take an array of model IDs — the same IDs shown in the `/models` picker.

- `blacklist` removes the listed models from the picker.
- `whitelist` keeps only the listed models and hides the rest.
- You can combine them: `whitelist` narrows the set, then `blacklist` removes entries from it.

---

## OpenCode Zen

OpenCode Zen is a list of models provided by the OpenCode team that have been
tested and verified to work well with OpenCode. [Learn more](/docs/zen).

:::tip
If you are new, we recommend starting with OpenCode Zen.

1. Run the `/connect` command in the TUI, select `OpenCode Zen`, and head to [opencode.ai/auth](https://opencode.ai/zen).

   ```txt
   /connect
   ```

2. Sign in, add your billing details, and copy your API key.

3. Paste your API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run `/models` in the TUI to see the list of models we recommend.

   ```txt
   /models
   ```

It works like any other provider in OpenCode and is completely optional to use.

---

## OpenCode Go

OpenCode Go is a low cost subscription plan that provides reliable access to popular open coding models provided by the OpenCode team that have been
tested and verified to work well with OpenCode.

1. Run the `/connect` command in the TUI, select `OpenCode Go`, and head to [opencode.ai/auth](https://opencode.ai/zen).

   ```txt
   /connect
   ```

2. Sign in, add your billing details, and copy your API key.

3. Paste your API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run `/models` in the TUI to see the list of models we recommend.

   ```txt
   /models
   ```

It works like any other provider in OpenCode and is completely optional to use.

---

## Directory

Let's look at some of the providers in detail. If you'd like to add a provider to the
list, feel free to open a PR.

:::note
Don't see a provider here? Submit a PR.

---

### 302.AI

1. Head over to the [302.AI console](https://302.ai/), create an account, and generate an API key.

2. Run the `/connect` command and search for **302.AI**.

   ```txt
   /connect
   ```

3. Enter your 302.AI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

---

### Amazon Bedrock

To use Amazon Bedrock with OpenCode:

1. Head over to the **Model catalog** in the Amazon Bedrock console and request
   access to the models you want.

   :::tip
   You need to have access to the model you want in Amazon Bedrock.

2. **Configure authentication** using one of the following methods:

   ***

   #### Environment Variables (Quick Start)

   Set one of these environment variables while running opencode:

   ```bash
   # Option 1: Using AWS access keys
   AWS_ACCESS_KEY_ID=XXX AWS_SECRET_ACCESS_KEY=YYY opencode

   # Option 2: Using named AWS profile
   AWS_PROFILE=my-profile opencode

   # Option 3: Using Bedrock bearer token
   AWS_BEARER_TOKEN_BEDROCK=XXX opencode
   ```

   Or add them to your bash profile:

   ```bash title="~/.bash_profile"
   export AWS_PROFILE=my-dev-profile
   export AWS_REGION=us-east-1
   ```

   ***

   #### Configuration File (Recommended)

   For project-specific or persistent configuration, use `opencode.json`:

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "amazon-bedrock": {
         "options": {
           "region": "us-east-1",
           "profile": "my-aws-profile"
         }
       }
     }
   }
   ```

   **Available options:**
   - `region` - AWS region (e.g., `us-east-1`, `eu-west-1`)
   - `profile` - AWS named profile from `~/.aws/credentials`
   - `endpoint` - Custom endpoint URL for VPC endpoints (alias for generic `baseURL` option)

   :::tip
   Configuration file options take precedence over environment variables.

   ***

   #### Advanced: VPC Endpoints

   If you're using VPC endpoints for Bedrock:

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "amazon-bedrock": {
         "options": {
           "region": "us-east-1",
           "profile": "production",
           "endpoint": "https://bedrock-runtime.us-east-1.vpce-xxxxx.amazonaws.com"
         }
       }
     }
   }
   ```

   :::note
   The `endpoint` option is an alias for the generic `baseURL` option, using AWS-specific terminology. If both `endpoint` and `baseURL` are specified, `endpoint` takes precedence.

   ***

   #### Authentication Methods
   - **`AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`**: Create an IAM user and generate access keys in the AWS Console
   - **`AWS_PROFILE`**: Use named profiles from `~/.aws/credentials`. First configure with `aws configure --profile my-profile` or `aws sso login`
   - **`AWS_BEARER_TOKEN_BEDROCK`**: Generate long-term API keys from the Amazon Bedrock console
   - **`AWS_WEB_IDENTITY_TOKEN_FILE` / `AWS_ROLE_ARN`**: For EKS IRSA (IAM Roles for Service Accounts) or other Kubernetes environments with OIDC federation. These environment variables are automatically injected by Kubernetes when using service account annotations.

   ***

   #### Authentication Precedence

   Amazon Bedrock uses the following authentication priority:
   1. **Bearer Token** - `AWS_BEARER_TOKEN_BEDROCK` environment variable or token from `/connect` command
   2. **AWS Credential Chain** - Profile, access keys, shared credentials, IAM roles, Web Identity Tokens (EKS IRSA), instance metadata

   :::note
   When a bearer token is set (via `/connect` or `AWS_BEARER_TOKEN_BEDROCK`), it takes precedence over all AWS credential methods including configured profiles.

3. Run the `/models` command to select the model you want.

   ```txt
   /models
   ```

:::note
For custom inference profiles, use the model and provider name in the key and set the `id` property to the arn. This ensures correct caching.

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "amazon-bedrock": {
      // ...
      "models": {
        "anthropic-claude-sonnet-4.5": {
          "id": "arn:aws:bedrock:us-east-1:xxx:application-inference-profile/yyy"
        }
      }
    }
  }
}
```

---

### Anthropic

1. Once you've signed up, run the `/connect` command and select Anthropic.

   ```txt
   /connect
   ```

2. Here you can select the **Claude Pro/Max** option and it'll open your browser
   and ask you to authenticate.

   ```txt
   ┌ Select auth method
   │
   │ Manually enter API Key
   └
   ```

3. Now all the Anthropic models should be available when you use the `/models` command.

   ```txt
   /models
   ```

:::info
There are plugins that allow you to use your Claude Pro/Max models with
OpenCode. Anthropic explicitly prohibits this.

Previous versions of OpenCode came bundled with these plugins but that is no
longer the case as of 1.3.0

Other companies support freedom of choice with developer tooling - you can use
the following subscriptions in OpenCode with zero setup:

- ChatGPT Plus
- Github Copilot
- Gitlab Duo

---

### Atomic Chat

You can configure opencode to use local models through [Atomic Chat](https://atomic.chat), a desktop application that runs local LLMs behind an OpenAI-compatible API server (default endpoint `http://127.0.0.1:1337/v1`).

```json title="opencode.json" "atomic-chat" {5, 6, 8, 10-14}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "atomic-chat": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Atomic Chat (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1337/v1"
      },
      "models": {
        "<your-model-id>": {
          "name": "<your-model-name>"
        }
      }
    }
  }
}
```

In this example:

- `atomic-chat` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server. Change the host and port to match your Atomic Chat setup.
- `models` is a map of model IDs to their display names. Each ID must match the `id` returned by `GET /v1/models` — run `curl http://127.0.0.1:1337/v1/models` to list the ids currently loaded in Atomic Chat.

:::tip
If tool calls aren't working well, pick a loaded model with strong tool-calling support (for example, a Qwen-Coder or DeepSeek-Coder variant).

---

### Azure OpenAI

:::note
If you encounter "I'm sorry, but I cannot assist with that request" errors, try changing the content filter from **DefaultV2** to **Default** in your Azure resource.

1. Head over to the [Azure portal](https://portal.azure.com/) and create an **Azure OpenAI** resource. You'll need:
   - **Resource name**: This becomes part of your API endpoint (`https://RESOURCE_NAME.openai.azure.com/`)
   - **API key**: Either `KEY 1` or `KEY 2` from your resource

2. Go to [Azure AI Foundry](https://ai.azure.com/) and deploy a model.

   :::note
   The deployment name must match the model name for opencode to work properly.

3. Run the `/connect` command and search for **Azure**.

   ```txt
   /connect
   ```

4. Enter your API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

5. Set your resource name as an environment variable:

   ```bash
   AZURE_RESOURCE_NAME=XXX opencode
   ```

   Or add it to your bash profile:

   ```bash title="~/.bash_profile"
   export AZURE_RESOURCE_NAME=XXX
   ```

6. Run the `/models` command to select your deployed model.

   ```txt
   /models
   ```

#### Microsoft Entra ID (Azure CLI)

You can use your Azure CLI session instead of an API key. [Install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli), run `az login`, then run `/connect`, select **Azure**, and choose **Microsoft Entra ID (Azure CLI)**. Enter the Azure Resource name when prompted. Use `az login --tenant TENANT_ID` if the Resource belongs to a different tenant.

Find the Resource name by opening your Azure OpenAI or Foundry Resource in the [Azure portal](https://portal.azure.com/) or [Microsoft Foundry](https://ai.azure.com/). It is also the first part of the endpoint: `my-models` in `https://my-models.openai.azure.com/` or `https://my-models.services.ai.azure.com/`. If your identity can list Resources, you can also find their names and Resource groups with:

```bash
az cognitiveservices account list \
  --query "[].{name:name,resourceGroup:resourceGroup}" \
  --output table
```

OpenCode does not query Azure management APIs or discover deployments. Select a model whose catalog name matches your deployment, or configure its deployment name explicitly:

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "azure": {
      "models": {
        "gpt-5-mini": {
          "id": "gpt-production"
        }
      }
    }
  }
}
```

Assign your identity the inference role required by the deployment: **Cognitive Services OpenAI User** for Azure OpenAI models or **Cognitive Services User** for other Foundry models. OpenCode refreshes access tokens through the Azure CLI, including versions earlier than 2.54.0, so you only need to sign in again when the CLI session expires.

---

### Azure Cognitive Services

1. Head over to the [Azure portal](https://portal.azure.com/) and create an **Azure OpenAI** resource. You'll need:
   - **Resource name**: This becomes part of your API endpoint (`https://AZURE_COGNITIVE_SERVICES_RESOURCE_NAME.cognitiveservices.azure.com/`)
   - **API key**: Either `KEY 1` or `KEY 2` from your resource

2. Go to [Azure AI Foundry](https://ai.azure.com/) and deploy a model.

   :::note
   The deployment name must match the model name for opencode to work properly.

3. Run the `/connect` command and search for **Azure Cognitive Services**.

   ```txt
   /connect
   ```

4. Enter your API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

5. Set your resource name as an environment variable:

   ```bash
   AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX opencode
   ```

   Or add it to your bash profile:

   ```bash title="~/.bash_profile"
   export AZURE_COGNITIVE_SERVICES_RESOURCE_NAME=XXX
   ```

6. Run the `/models` command to select your deployed model.

   ```txt
   /models
   ```

---

### Baseten

1. Head over to the [Baseten](https://app.baseten.co/), create an account, and generate an API key.

2. Run the `/connect` command and search for **Baseten**.

   ```txt
   /connect
   ```

3. Enter your Baseten API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

---

### Cerebras

1. Head over to the [Cerebras console](https://inference.cerebras.ai/), create an account, and generate an API key.

2. Run the `/connect` command and search for **Cerebras**.

   ```txt
   /connect
   ```

3. Enter your Cerebras API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Qwen 3 Coder 480B_.

   ```txt
   /models
   ```

---

### Cloudflare AI Gateway

Cloudflare AI Gateway lets you access models from OpenAI, Anthropic, Workers AI, and more through a unified endpoint. With [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/) you don't need separate API keys for each provider.

1. Head over to the [Cloudflare dashboard](https://dash.cloudflare.com/), navigate to **AI** > **AI Gateway**, and create a new gateway. Note your **Account ID** and **Gateway ID**.

2. Run the `/connect` command and search for **Cloudflare AI Gateway**.

   ```txt
   /connect
   ```

3. Enter your **Account ID** when prompted.

   ```txt
   ┌ Enter your Cloudflare Account ID
   │
   │
   └ enter
   ```

4. Enter your **Gateway ID** when prompted.

   ```txt
   ┌ Enter your Cloudflare AI Gateway ID
   │
   │
   └ enter
   ```

5. Enter your **Cloudflare API token**.

   ```txt
   ┌ Gateway API token
   │
   │
   └ enter
   ```

6. Run the `/models` command to select a model.

   ```txt
   /models
   ```

   You can also add models through your opencode config.

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "cloudflare-ai-gateway": {
         "models": {
           "openai/gpt-4o": {},
           "anthropic/claude-sonnet-4": {}
         }
       }
     }
   }
   ```

   Alternatively, you can set environment variables instead of using `/connect`.

   ```bash title="~/.bash_profile"
   export CLOUDFLARE_ACCOUNT_ID=your-32-character-account-id
   export CLOUDFLARE_GATEWAY_ID=your-gateway-id
   export CLOUDFLARE_API_TOKEN=your-api-token
   ```

---

### Cloudflare Workers AI

Cloudflare Workers AI lets you run AI models on Cloudflare's global network directly via REST API, with no separate provider accounts needed for supported models.

1. Head over to the [Cloudflare dashboard](https://dash.cloudflare.com/), navigate to **Workers AI**, and select **Use REST API** to get your **Account ID** and create an API token.

2. Run the `/connect` command and search for **Cloudflare Workers AI**.

   ```txt
   /connect
   ```

3. Enter your **Account ID** when prompted.

   ```txt
   ┌ Enter your Cloudflare Account ID
   │
   │
   └ enter
   ```

4. Enter your **Cloudflare API key**.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

5. Run the `/models` command to select a model.

   ```txt
   /models
   ```

   Alternatively, you can set environment variables instead of using `/connect`.

   ```bash title="~/.bash_profile"
   export CLOUDFLARE_ACCOUNT_ID=your-32-character-account-id
   export CLOUDFLARE_API_KEY=your-api-token
   ```

---

### Cortecs

1. Head over to the [Cortecs console](https://cortecs.ai/), create an account, and generate an API key.

2. Run the `/connect` command and search for **Cortecs**.

   ```txt
   /connect
   ```

3. Enter your Cortecs API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Kimi K2 Instruct_.

   ```txt
   /models
   ```

---

### DeepSeek

1. Head over to the [DeepSeek console](https://platform.deepseek.com/), create an account, and click **Create new API key**.

2. Run the `/connect` command and search for **DeepSeek**.

   ```txt
   /connect
   ```

3. Enter your DeepSeek API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a DeepSeek model like _DeepSeek V4 Pro_.

   ```txt
   /models
   ```

---

### Deep Infra

1. Head over to the [Deep Infra dashboard](https://deepinfra.com/dash), create an account, and generate an API key.

2. Run the `/connect` command and search for **Deep Infra**.

   ```txt
   /connect
   ```

3. Enter your Deep Infra API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

---

### DigitalOcean

DigitalOcean's [Inference Engine](https://docs.digitalocean.com/products/inference/) provides access to open models like GPT-OSS, Llama, Qwen, and DeepSeek, plus custom [Inference Routers](https://docs.digitalocean.com/products/inference/how-to/use-inference-router/) that route each request to the cheapest, fastest, or best-fit model for a task.

OpenCode supports two authentication methods:

- **OAuth (Recommended)** — Sign in to your DigitalOcean account; OpenCode uses your DigitalOcean API token directly for inference and discovers your Inference Routers.
- **Model Access Key** — Paste an existing key from the DigitalOcean console.

#### OAuth (Recommended)

1. Run the `/connect` command and search for **DigitalOcean**.

   ```txt
   /connect
   ```

2. Select **Login with DigitalOcean**.

   ```txt
   ┌ Select auth method
   │
   │ Login with DigitalOcean
   │ Paste Model Access Key
   └
   ```

3. Your browser opens to authorize OpenCode. Sign in and approve.

   :::note
   OpenCode requests `genai:read` and `inference:query` OAuth scopes. Your DigitalOcean API token is used directly for inference — no separate Model Access Key is created.

   :::note
   Inference Routers only appear in the model picker after OAuth. Pasting a Model Access Key manually does not discover routers.

4. Run the `/models` command. Your Inference Routers appear as the format `router:` in the model selection.

   ```txt
   /models
   ```

5. To pick up newly created Inference Routers, re-run `/connect` and select **DigitalOcean** again.

#### Using a Model Access Key

If you'd rather paste a key directly:

1. Head over to the **Manage** page in the Inference section of the [DigitalOcean console](https://cloud.digitalocean.com/) and create a new key.

2. Run the `/connect` command and select **DigitalOcean**, then **Paste Model Access Key**.

   ```txt
   ┌ Enter your DigitalOcean Model Access Key
   │
   │
   └ enter
   ```

   :::note
   Inference Routers are not auto-discovered with this method. To surface them in the model picker, sign in via OAuth instead.

3. Run the `/models` command to select a model.

   ```txt
   /models
   ```

#### Environment Variable

Alternatively, set your Model Access Key as an environment variable.

```bash frame="none"
export DIGITALOCEAN_ACCESS_TOKEN=your-model-access-key
```

#### Inference Routers

Inference Routers let you define a routing policy across multiple models — picking the cheapest, fastest, or most appropriate model per request based on the task. After OAuth, OpenCode surfaces each router as `router:<router-name>` in the model picker.

Selecting a router model is a drop-in replacement for any other model — OpenCode forwards your request and DigitalOcean picks the underlying model based on your router's policy. Learn more about [Inference Routers](https://docs.digitalocean.com/products/inference/how-to/use-inference-router/)

---

### Eden AI

[Eden AI](https://www.edenai.co/) is an EU-based gateway that serves models from many vendors over a single OpenAI-compatible API, with a separate EU endpoint for teams that need inference to stay in the EU.

1. Head over to the [Eden AI platform](https://app.edenai.run/user/register) to create an account and generate an API key.

2. Run the `/connect` command and search for **Eden AI**.

   ```txt
   /connect
   ```

3. Enter your Eden AI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Mistral Large 3_ or _Claude Sonnet 5_.

   ```txt
   /models
   ```

   Eden AI model ids are themselves in `vendor/model` form, so a full reference has three segments, for example `edenai/anthropic/claude-sonnet-5`.

5. To keep requests on Eden AI's EU gateway, set its base URL.

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "edenai": {
         "options": {
           "baseURL": "https://api.eu.edenai.run/v3"
         }
       }
     }
   }
   ```

   The default is `https://api.edenai.run/v3`, so this swaps the global endpoint for the EU one. The EU endpoint serves the subset of the catalog that is available in the EU, so a model chosen in step 4 may not be reachable through it.

---

### FrogBot

1. Head over to the [FrogBot dashboard](https://app.frogbot.ai/signup), create an account, and generate an API key.

2. Run the `/connect` command and search for **FrogBot**.

   ```txt
   /connect
   ```

3. Enter your FrogBot API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

---

### Fireworks AI

1. Head over to the [Fireworks AI console](https://app.fireworks.ai/), create an account, and click **Create API Key**.

2. Run the `/connect` command and search for **Fireworks AI**.

   ```txt
   /connect
   ```

3. Enter your Fireworks AI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Kimi K2 Instruct_.

   ```txt
   /models
   ```

---

### GitLab Duo

:::caution[Experimental]
GitLab Duo support in OpenCode is experimental. Features, configuration, and
behavior may change in future releases.

OpenCode integrates with the [GitLab Duo Agent Platform](https://docs.gitlab.com/user/duo_agent_platform/),
providing AI-powered agentic chat with native tool calling capabilities.

:::note[License requirements]
GitLab Duo Agent Platform requires a **Premium** or **Ultimate** GitLab
subscription. It is available on GitLab.com and GitLab Self-Managed.
See [GitLab Duo Agent Platform prerequisites](https://docs.gitlab.com/user/duo_agent_platform/#prerequisites)
for full requirements.

1. Run the `/connect` command and select GitLab.

   ```txt
   /connect
   ```

2. Choose your authentication method:

   ```txt
   ┌ Select auth method
   │
   │ OAuth (Recommended)
   │ Personal Access Token
   └
   ```

   #### Using OAuth (Recommended)

   Select **OAuth** and your browser will open for authorization.

   #### Using Personal Access Token
   1. Go to [GitLab User Settings > Access Tokens](https://gitlab.com/-/user_settings/personal_access_tokens)
   2. Click **Add new token**
   3. Name: `OpenCode`, Scopes: `api`
   4. Copy the token (starts with `glpat-`)
   5. Enter it in the terminal

3. Run the `/models` command to see available models.

   ```txt
   /models
   ```

   Three Claude-based models are available:
   - **duo-chat-haiku-4-5** (Default) - Fast responses for quick tasks
   - **duo-chat-sonnet-4-5** - Balanced performance for most workflows
   - **duo-chat-opus-4-5** - Most capable for complex analysis

:::note
You can also specify 'GITLAB_TOKEN' environment variable if you don't want
to store token in opencode auth storage.

##### Self-Hosted GitLab

:::note[compliance note]
OpenCode uses a small model for some AI tasks like generating the session title.
It is configured to use gpt-5-nano by default, hosted by Zen. To lock OpenCode
to only use your own GitLab-hosted instance, add the following to your
`opencode.json` file. It is also recommended to disable session sharing.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "small_model": "gitlab/duo-chat-haiku-4-5",
  "share": "disabled"
}
```

For self-hosted GitLab instances:

```bash
export GITLAB_INSTANCE_URL=https://gitlab.company.com
export GITLAB_TOKEN=glpat-...
```

If your instance runs a custom AI Gateway:

```bash
GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
```

Or add to your bash profile:

```bash title="~/.bash_profile"
export GITLAB_INSTANCE_URL=https://gitlab.company.com
export GITLAB_AI_GATEWAY_URL=https://ai-gateway.company.com
export GITLAB_TOKEN=glpat-...
```

:::note
Your GitLab administrator must:

1. [Turn on GitLab Duo](https://docs.gitlab.com/user/duo_agent_platform/turn_on_off/#turn-gitlab-duo-on-or-off)
   for the user, group, or instance
2. [Turn on the Agent Platform](https://docs.gitlab.com/user/duo_agent_platform/turn_on_off/#turn-gitlab-duo-agent-platform-on-or-off)
   (GitLab 18.8+) or [enable beta and experimental features](https://docs.gitlab.com/user/duo_agent_platform/turn_on_off/#turn-on-beta-and-experimental-features)
   (GitLab 18.7 and earlier)
3. For Self-Managed, [configure your instance](https://docs.gitlab.com/administration/gitlab_duo/configure/gitlab_self_managed/)

##### OAuth for Self-Hosted instances

In order to make Oauth working for your self-hosted instance, you need to create
a new application (Settings → Applications) with the
callback URL `http://127.0.0.1:8080/callback` and following scopes:

- api (Access the API on your behalf)
- read_user (Read your personal information)
- read_repository (Allows read-only access to the repository)

Then expose application ID as environment variable:

```bash
export GITLAB_OAUTH_CLIENT_ID=your_application_id_here
```

More documentation on [opencode-gitlab-auth](https://www.npmjs.com/package/opencode-gitlab-auth) homepage.

##### Configuration

Customize through `opencode.json`:

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "gitlab": {
      "options": {
        "instanceUrl": "https://gitlab.com"
      }
    }
  }
}
```

##### GitLab Duo Agent Platform (DAP) Workflow Models

DAP workflow models provide an alternative execution path that routes tool calls
through GitLab's Duo Workflow Service (DWS) instead of the standard agentic chat.
When a `duo-workflow-*` model is selected, OpenCode will:

1. Discover available models from your GitLab namespace
2. Present a selection picker if multiple models are available
3. Cache the selected model to disk for fast subsequent startups
4. Route tool execution requests through OpenCode's permission-gated tool system

Available DAP workflow models follow the `duo-workflow-*` naming convention and
are dynamically discovered from your GitLab instance.

##### GitLab API Tools (Optional, but highly recommended)

To access GitLab tools (merge requests, issues, pipelines, CI/CD, etc.):

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-gitlab-plugin"]
}
```

This plugin provides comprehensive GitLab repository management capabilities including MR reviews, issue tracking, pipeline monitoring, and more.

---

### GitHub Copilot

To use your GitHub Copilot subscription with opencode:

:::note
Some models might need a [Pro+
subscription](https://github.com/features/copilot/plans) to use.

1. Run the `/connect` command and search for GitHub Copilot.

   ```txt
   /connect
   ```

2. Navigate to [github.com/login/device](https://github.com/login/device) and enter the code.

   ```txt
   ┌ Login with GitHub Copilot
   │
   │ https://github.com/login/device
   │
   │ Enter code: 8F43-6FCF
   │
   └ Waiting for authorization...
   ```

3. Now run the `/models` command to select the model you want.

   ```txt
   /models
   ```

---

### GMI Cloud

To use GMI Cloud with OpenCode:

1. Head over to the [GMI Cloud console](https://console.gmicloud.ai/) to create an API key. You can also review the [API reference](https://docs.gmicloud.ai/inference-engine/api-reference/llm-api-reference) for the endpoint details.

2. Run the `/connect` command and search for **GMI Cloud**.

   ```txt
   /connect
   ```

3. Enter your GMI Cloud API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select the model you want.

   ```txt
   /models
   ```

---

### Google Vertex AI

To use Google Vertex AI with OpenCode:

1. Head over to the **Model Garden** in the Google Cloud Console and check the
   models available in your region.

   :::note
   You need to have a Google Cloud project with Vertex AI API enabled.

2. Set the required environment variables:
   - `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID
   - `VERTEX_LOCATION` (optional): The region for Vertex AI (defaults to `global`)
   - Authentication (choose one):
     - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your service account JSON key file
     - Authenticate using gcloud CLI: `gcloud auth application-default login`

   Set them while running opencode.

   ```bash
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json GOOGLE_CLOUD_PROJECT=your-project-id opencode
   ```

   Or add them to your bash profile.

   ```bash title="~/.bash_profile"
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
   export GOOGLE_CLOUD_PROJECT=your-project-id
   export VERTEX_LOCATION=global
   ```

:::tip
The `global` region improves availability and reduces errors at no extra cost. Use regional endpoints (e.g., `us-central1`) for data residency requirements. [Learn more](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models#regional_and_global_endpoints)

3. Run the `/models` command to select the model you want.

   ```txt
   /models
   ```

---

### Groq

1. Head over to the [Groq console](https://console.groq.com/), click **Create API Key**, and copy the key.

2. Run the `/connect` command and search for Groq.

   ```txt
   /connect
   ```

3. Enter the API key for the provider.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select the one you want.

   ```txt
   /models
   ```

---

### Hugging Face

[Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) provides access to open models supported by 17+ providers.

1. Head over to [Hugging Face settings](https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained) to create a token with permission to make calls to Inference Providers.

2. Run the `/connect` command and search for **Hugging Face**.

   ```txt
   /connect
   ```

3. Enter your Hugging Face token.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Kimi-K2-Instruct_ or _GLM-4.6_.

   ```txt
   /models
   ```

---

### Helicone

[Helicone](https://helicone.ai) is an LLM observability platform that provides logging, monitoring, and analytics for your AI applications. The Helicone AI Gateway routes your requests to the appropriate provider automatically based on the model.

1. Head over to [Helicone](https://helicone.ai), create an account, and generate an API key from your dashboard.

2. Run the `/connect` command and search for **Helicone**.

   ```txt
   /connect
   ```

3. Enter your Helicone API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

For more providers and advanced features like caching and rate limiting, check the [Helicone documentation](https://docs.helicone.ai).

#### Optional Configs

In the event you see a feature or model from Helicone that isn't configured automatically through opencode, you can always configure it yourself.

Here's [Helicone's Model Directory](https://helicone.ai/models), you'll need this to grab the IDs of the models you want to add.

```jsonc title="~/.config/opencode/opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "helicone": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Helicone",
      "options": {
        "baseURL": "https://ai-gateway.helicone.ai",
      },
      "models": {
        "gpt-4o": {
          // Model ID (from Helicone's model directory page)
          "name": "GPT-4o", // Your own custom name for the model
        },
        "claude-sonnet-4-20250514": {
          "name": "Claude Sonnet 4",
        },
      },
    },
  },
}
```

#### Custom Headers

Helicone supports custom headers for features like caching, user tracking, and session management. Add them to your provider config using `options.headers`:

```jsonc title="~/.config/opencode/opencode.jsonc"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "helicone": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Helicone",
      "options": {
        "baseURL": "https://ai-gateway.helicone.ai",
        "headers": {
          "Helicone-Cache-Enabled": "true",
          "Helicone-User-Id": "opencode",
        },
      },
    },
  },
}
```

##### Session tracking

Helicone's [Sessions](https://docs.helicone.ai/features/sessions) feature lets you group related LLM requests together. Use the [opencode-helicone-session](https://github.com/H2Shami/opencode-helicone-session) plugin to automatically log each OpenCode conversation as a session in Helicone.

```bash
npm install -g opencode-helicone-session
```

Add it to your config.

```json title="opencode.json"
{
  "plugin": ["opencode-helicone-session"]
}
```

The plugin injects `Helicone-Session-Id` and `Helicone-Session-Name` headers into your requests. In Helicone's Sessions page, you'll see each OpenCode conversation listed as a separate session.

##### Common Helicone headers

| Header                     | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| `Helicone-Cache-Enabled`   | Enable response caching (`true`/`false`)                      |
| `Helicone-User-Id`         | Track metrics by user                                         |
| `Helicone-Property-[Name]` | Add custom properties (e.g., `Helicone-Property-Environment`) |
| `Helicone-Prompt-Id`       | Associate requests with prompt versions                       |

See the [Helicone Header Directory](https://docs.helicone.ai/helicone-headers/header-directory) for all available headers.

---

### llama.cpp

You can configure opencode to use local models through [llama.cpp's](https://github.com/ggml-org/llama.cpp) llama-server utility

```json title="opencode.json" "llama.cpp" {5, 6, 8, 10-15}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "llama.cpp": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "llama-server (local)",
      "options": {
        "baseURL": "http://127.0.0.1:8080/v1"
      },
      "models": {
        "qwen3-coder:a3b": {
          "name": "Qwen3-Coder: a3b-30b (local)",
          "limit": {
            "context": 128000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

In this example:

- `llama.cpp` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server.
- `models` is a map of model IDs to their configurations. The model name will be displayed in the model selection list.

---

### IO.NET

IO.NET offers 17 models optimized for various use cases:

1. Head over to the [IO.NET console](https://ai.io.net/), create an account, and generate an API key.

2. Run the `/connect` command and search for **IO.NET**.

   ```txt
   /connect
   ```

3. Enter your IO.NET API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

---

### LM Studio

You can configure opencode to use local models through LM Studio.

```json title="opencode.json" "lmstudio" {5, 6, 8, 10-14}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "lmstudio": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "LM Studio (local)",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1"
      },
      "models": {
        "google/gemma-3n-e4b": {
          "name": "Gemma 3n-e4b (local)"
        }
      }
    }
  }
}
```

In this example:

- `lmstudio` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server.
- `models` is a map of model IDs to their configurations. The model name will be displayed in the model selection list.

---

### Moonshot AI

To use Kimi K2 from Moonshot AI:

1. Head over to the [Moonshot AI console](https://platform.moonshot.ai/console), create an account, and click **Create API key**.

2. Run the `/connect` command and search for **Moonshot AI**.

   ```txt
   /connect
   ```

3. Enter your Moonshot API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select _Kimi K2_.

   ```txt
   /models
   ```

---

### MiniMax

1. Head over to the [MiniMax API Console](https://platform.minimax.io/login), create an account, and generate an API key.

2. Run the `/connect` command and search for **MiniMax**.

   ```txt
   /connect
   ```

3. Enter your MiniMax API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _M2.1_.

   ```txt
   /models
   ```

---

### Modal

1. Create a [shared Endpoint](https://modal.com/endpoints) for the model you want to use.

2. Create a [proxy token](https://modal.com/docs/guide/endpoints#proxy-tokens), then join its ID and secret with a period:

   ```txt
   wk-<id>.ws-<secret>
   ```

3. Run the `/connect` command, search for **Modal**, and enter the combined proxy token.

   ```txt
   /connect
   ```

4. Run the `/models` command to select one of the endpoints in your Modal workspace.

   ```txt
   /models
   ```

---

### NVIDIA

NVIDIA provides access to Nemotron models and many other open models through [build.nvidia.com](https://build.nvidia.com) for free.

1. Head over to [build.nvidia.com](https://build.nvidia.com), create an account, and generate an API key.

2. Run the `/connect` command and search for **NVIDIA**.

   ```txt
   /connect
   ```

3. Enter your NVIDIA API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like nemotron-3-super-120b-a12b.

   ```txt
   /models
   ```

#### On-Prem / NIM

You can also use NVIDIA models locally via [NVIDIA NIM](https://docs.nvidia.com/nim/) by setting a custom base URL.

```json title="opencode.json" {6}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "nvidia": {
      "options": {
        "baseURL": "http://localhost:8000/v1"
      }
    }
  }
}
```

#### Environment Variable

Alternatively, set your API key as an environment variable.

```bash frame="none"
export NVIDIA_API_KEY=nvapi-your-key-here
```

---

### Nebius Token Factory

1. Head over to the [Nebius Token Factory console](https://tokenfactory.nebius.com/), create an account, and click **Add Key**.

2. Run the `/connect` command and search for **Nebius Token Factory**.

   ```txt
   /connect
   ```

3. Enter your Nebius Token Factory API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Kimi K2 Instruct_.

   ```txt
   /models
   ```

---

### Ollama

You can configure opencode to use local models through Ollama.

:::tip
Ollama can automatically configure itself for OpenCode. See the [Ollama integration docs](https://docs.ollama.com/integrations/opencode) for details.

```json title="opencode.json" "ollama" {5, 6, 8, 10-14}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "llama2": {
          "name": "Llama 2"
        }
      }
    }
  }
}
```

In this example:

- `ollama` is the custom provider ID. This can be any string you want.
- `npm` specifies the package to use for this provider. Here, `@ai-sdk/openai-compatible` is used for any OpenAI-compatible API.
- `name` is the display name for the provider in the UI.
- `options.baseURL` is the endpoint for the local server.
- `models` is a map of model IDs to their configurations. The model name will be displayed in the model selection list.

:::tip
If tool calls aren't working, try increasing `num_ctx` in Ollama. Start around 16k - 32k.

---

### Ollama Cloud

To use Ollama Cloud with OpenCode:

1. Head over to [https://ollama.com/](https://ollama.com/) and sign in or create an account.

2. Navigate to **Settings** > **Keys** and click **Add API Key** to generate a new API key.

3. Copy the API key for use in OpenCode.

4. Run the `/connect` command and search for **Ollama Cloud**.

   ```txt
   /connect
   ```

5. Enter your Ollama Cloud API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

6. **Important**: Before using cloud models in OpenCode, you must pull the model information locally:

   ```bash
   ollama pull gpt-oss:20b-cloud
   ```

7. Run the `/models` command to select your Ollama Cloud model.

   ```txt
   /models
   ```

---

### OpenAI

We recommend signing up for [ChatGPT Plus or Pro](https://chatgpt.com/pricing).

1. Once you've signed up, run the `/connect` command and select OpenAI.

   ```txt
   /connect
   ```

2. Here you can select the **ChatGPT Plus/Pro** option and it'll open your browser
   and ask you to authenticate.

   ```txt
   ┌ Select auth method
   │
   │ ChatGPT Plus/Pro
   │ Manually enter API Key
   └
   ```

3. Now all the OpenAI models should be available when you use the `/models` command.

   ```txt
   /models
   ```

##### Compute residency

For ChatGPT OAuth, OpenCode automatically applies a regional inference residency requirement when one is advertised by your workspace credentials. It forwards the compute residency value from the credential instead of maintaining a fixed list of regions. Data residency at rest does not imply regional inference.

##### Using API keys

If you already have an API key, you can select **Manually enter API Key** and paste it in your terminal.

---

### OpenCode Zen

OpenCode Zen is a list of tested and verified models provided by the OpenCode team. [Learn more](/docs/zen).

1. Sign in to **<a href={console}>OpenCode Zen</a>** and click **Create API Key**.

2. Run the `/connect` command and search for **OpenCode Zen**.

   ```txt
   /connect
   ```

3. Enter your OpenCode API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Qwen 3 Coder 480B_.

   ```txt
   /models
   ```

---

### OpenRouter

1. Head over to the [OpenRouter dashboard](https://openrouter.ai/settings/keys), click **Create API Key**, and copy the key.

2. Run the `/connect` command and search for OpenRouter.

   ```txt
   /connect
   ```

3. Enter the API key for the provider.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Many OpenRouter models are preloaded by default, run the `/models` command to select the one you want.

   ```txt
   /models
   ```

   You can also add additional models through your opencode config.

   ```json title="opencode.json" {6}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "openrouter": {
         "models": {
           "somecoolnewmodel": {}
         }
       }
     }
   }
   ```

5. You can also customize them through your opencode config. Here's an example of specifying a provider

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "openrouter": {
         "models": {
           "moonshotai/kimi-k2": {
             "options": {
               "provider": {
                 "order": ["baseten"],
                 "allow_fallbacks": false
               }
             }
           }
         }
       }
     }
   }
   ```

---

### LLM Gateway

1. Head over to the [LLM Gateway dashboard](https://llmgateway.io/dashboard), click **Create API Key**, and copy the key.

2. Run the `/connect` command and search for LLM Gateway.

   ```txt
   /connect
   ```

3. Enter the API key for the provider.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Many LLM Gateway models are preloaded by default, run the `/models` command to select the one you want.

   ```txt
   /models
   ```

   You can also add additional models through your opencode config.

   ```json title="opencode.json" {6}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "llmgateway": {
         "models": {
           "somecoolnewmodel": {}
         }
       }
     }
   }
   ```

5. You can also customize them through your opencode config. Here's an example of specifying a provider

   ```json title="opencode.json"
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "llmgateway": {
         "models": {
           "glm-4.7": {
             "name": "GLM 4.7"
           },
           "gpt-5.2": {
             "name": "GPT-5.2"
           },
           "gemini-2.5-pro": {
             "name": "Gemini 2.5 Pro"
           },
           "claude-3-5-sonnet-20241022": {
             "name": "Claude 3.5 Sonnet"
           }
         }
       }
     }
   }
   ```

---

### Poolside

[Poolside](https://poolside.ai) provides access to its models through an OpenAI-compatible API.

1. Head over to [platform.poolside.ai](https://platform.poolside.ai), sign in, open the **API Keys** tab, and click **New key** to generate an API key.

2. Run the `/connect` command and search for **Poolside**.

   ```txt
   /connect
   ```

3. Enter your Poolside API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

#### Poolside deployment

If your organization runs a Poolside deployment, configure it as a custom OpenAI-compatible provider. Store the API key or token from your Poolside administrator in `~/.secrets/poolside-key`. Use a unique provider ID and add the model IDs available from your deployment.

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "poolside-deployment": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Poolside deployment",
      "options": {
        "baseURL": "https://poolside.example.com/openai/v1",
        "apiKey": "{file:~/.secrets/poolside-key}"
      },
      "models": {
        "<served-model-id>": {
          "name": "Poolside deployment model",
          "reasoning": true,
          "interleaved": {
            "field": "reasoning_content"
          }
        }
      }
    }
  }
}
```

Replace `poolside.example.com` with your deployment's host and `<served-model-id>` with a model ID returned by its `/openai/v1/models` endpoint. Model availability and thinking behavior depend on the deployment's configuration.

:::tip
You can also install [Poolside Agent CLI](https://github.com/poolsideai/pool) to use Poolside agents directly from your terminal.

---

### SAP AI Core

SAP AI Core provides access to 40+ models from OpenAI, Anthropic, Google, Amazon, Meta, Mistral, and AI21 through a unified platform.

1. Go to your [SAP BTP Cockpit](https://account.hana.ondemand.com/), navigate to your SAP AI Core service instance, and create a service key.

   :::tip
   The service key is a JSON object containing `clientid`, `clientsecret`, `url`, and `serviceurls.AI_API_URL`. You can find your AI Core instance under **Services** > **Instances and Subscriptions** in the BTP Cockpit.

2. Run the `/connect` command and search for **SAP AI Core**.

   ```txt
   /connect
   ```

3. Enter your service key JSON.

   ```txt
   ┌ Service key
   │
   │
   └ enter
   ```

   Or set the `AICORE_SERVICE_KEY` environment variable:

   ```bash
   AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}' opencode
   ```

   Or add it to your bash profile:

   ```bash title="~/.bash_profile"
   export AICORE_SERVICE_KEY='{"clientid":"...","clientsecret":"...","url":"...","serviceurls":{"AI_API_URL":"..."}}'
   ```

4. Optionally set deployment ID and resource group:

   ```bash
   AICORE_DEPLOYMENT_ID=your-deployment-id AICORE_RESOURCE_GROUP=your-resource-group opencode
   ```

   :::note
   These settings are optional and should be configured according to your SAP AI Core setup.

5. Run the `/models` command to select from 40+ available models.

   ```txt
   /models
   ```

---

### STACKIT

STACKIT AI Model Serving provides fully managed sovereign hosting environment for AI models, focusing on LLMs like Llama, Mistral, and Qwen, with maximum data sovereignty on European infrastructure.

1. Head over to [STACKIT Portal](https://portal.stackit.cloud), navigate to **AI Model Serving**, and create an auth token for your project.

   :::tip
   You need a STACKIT customer account, user account, and project before creating auth tokens.

2. Run the `/connect` command and search for **STACKIT**.

   ```txt
   /connect
   ```

3. Enter your STACKIT AI Model Serving auth token.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select from available models like _Qwen3-VL 235B_ or _Llama 3.3 70B_.

   ```txt
   /models
   ```

---

### OVHcloud AI Endpoints

1. Head over to the [OVHcloud panel](https://ovh.com/manager). Navigate to the `Public Cloud` section, `AI & Machine Learning` > `AI Endpoints` and in `API Keys` tab, click **Create a new API key**.

2. Run the `/connect` command and search for **OVHcloud AI Endpoints**.

   ```txt
   /connect
   ```

3. Enter your OVHcloud AI Endpoints API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _gpt-oss-120b_.

   ```txt
   /models
   ```

---

### Scaleway

To use [Scaleway Generative APIs](https://www.scaleway.com/en/docs/generative-apis/) with Opencode:

1. Head over to the [Scaleway Console IAM settings](https://console.scaleway.com/iam/api-keys) to generate a new API key.

2. Run the `/connect` command and search for **Scaleway**.

   ```txt
   /connect
   ```

3. Enter your Scaleway API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _devstral-2-123b-instruct-2512_ or _gpt-oss-120b_.

   ```txt
   /models
   ```

---

### SCX.ai

[SCX.ai](https://scx.ai) is an Australian sovereign AI platform serving open models over an OpenAI-compatible API, hosted on renewable-powered infrastructure in Australia.

1. Head over to the [SCX.ai platform](https://platform.scx.ai) to create an account and generate an API key.

2. Run the `/connect` command and search for **SCX.ai**.

   ```txt
   /connect
   ```

3. Enter your SCX.ai API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _MiniMax-M2.7_ or _GLM-5.2_.

   ```txt
   /models
   ```

---

### Snowflake Cortex

[Snowflake Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api) gives you access to frontier models (Claude, OpenAI GPT-5, and more) via an OpenAI-compatible API. All inference runs within the Snowflake perimeter and is billed in Snowflake credits. For per-model rates, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

Don't have a Snowflake account? [Sign up for a free trial](https://signup.snowflake.com/?utm_source=opencode&utm_medium=docs&utm_campaign=cortex-provider).

opencode's core workflow for coding, editing files, and running commands relies on tool calling. Only the Claude and OpenAI families within Snowflake Cortex support this. The provider is limited to those families to support the core workflow.

OpenCode supports two authentication methods:

- **Browser OAuth (Recommended)** — sign in with your IdP/SSO; no secrets to manage, tokens refresh automatically.
- **Manual bearer token** — paste a PAT or JWT from the Snowflake console.

#### Browser OAuth (Recommended)

1. Run the `/connect` command and search for **Snowflake Cortex**.

   ```txt
   /connect
   ```

2. Select **Login with Snowflake (External Browser)**.

   ```txt
   ┌ Select auth method
   │
   │ Login with Snowflake (External Browser)
   │ Paste PAT or bearer token manually
   └
   ```

3. Enter your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) when prompted, for example `myorg-myaccount` or `xy12345.us-east-1`.

   ```txt
   ┌ Snowflake Account Identifier
   │
   │
   └ enter
   ```

4. Optionally enter a Snowflake role to scope the session (e.g. `SYSADMIN`). Leave blank to use your default role.

5. Complete sign-in in the browser that opens. OpenCode captures the OAuth callback automatically and stores the token — no copy/paste needed.

6. Run the `/models` command to select a model.

   ```txt
   /models
   ```

:::note
Browser OAuth uses Snowflake's built-in `SNOWFLAKE$LOCAL_APPLICATION` security integration ([docs](https://docs.snowflake.com/en/user-guide/oauth-local-applications)), which is rolling out to all accounts. To check availability in your account:

```sql
SHOW SECURITY INTEGRATIONS LIKE 'SNOWFLAKE$LOCAL_APPLICATION';
```

If the result is empty, use the **Manual bearer token** method below while the integration rolls out to your account.

#### Manual bearer token

If you prefer to paste a token directly, or if `SNOWFLAKE$LOCAL_APPLICATION` is not yet available in your account:

1. Generate a [Programmatic Access Token (PAT)](https://docs.snowflake.com/en/user-guide/programmatic-access-tokens) in your Snowflake account.

2. Run the `/connect` command, search for **Snowflake Cortex**, and select **Paste PAT or bearer token manually**.

3. Enter your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) when prompted.

4. Paste your PAT.

5. Run the `/models` command to select a model.

   ```txt
   /models
   ```

#### Environment variable

For CI or headless environments, set a PAT or JWT before starting opencode:

```bash
export SNOWFLAKE_ACCOUNT=myorg-myaccount
export SNOWFLAKE_CORTEX_TOKEN=your-pat-or-jwt
```

:::note
`SNOWFLAKE_CORTEX_TOKEN` accepts a PAT or JWT only — the browser OAuth flow is available via `/connect` only and cannot be configured through an environment variable. `SNOWFLAKE_CORTEX_PAT` is still supported for backward compatibility.

The model catalog is provided automatically. A minimal `opencode.json` is all that's needed:

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "model": "snowflake-cortex/claude-sonnet-4-6",
  "small_model": "snowflake-cortex/claude-haiku-4-5"
}
```

---

### Together AI

1. Head over to the [Together AI console](https://api.together.ai), create an account, and click **Add Key**.

2. Run the `/connect` command and search for **Together AI**.

   ```txt
   /connect
   ```

3. Enter your Together AI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Kimi K2 Instruct_.

   ```txt
   /models
   ```

---

### Venice AI

1. Head over to the [Venice AI console](https://venice.ai), create an account, and generate an API key.

2. Run the `/connect` command and search for **Venice AI**.

   ```txt
   /connect
   ```

3. Enter your Venice AI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Llama 3.3 70B_.

   ```txt
   /models
   ```

---

### Vercel AI Gateway

Vercel AI Gateway lets you access models from OpenAI, Anthropic, Google, xAI, and more through a unified endpoint. Models are offered at list price with no markup.

1. Head over to the [Vercel dashboard](https://vercel.com/), navigate to the **AI Gateway** tab, and click **API keys** to create a new API key.

2. Run the `/connect` command and search for **Vercel AI Gateway**.

   ```txt
   /connect
   ```

3. Enter your Vercel AI Gateway API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model.

   ```txt
   /models
   ```

You can also customize models through your opencode config. Here's an example of specifying provider routing order.

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "vercel": {
      "models": {
        "anthropic/claude-sonnet-4": {
          "options": {
            "order": ["anthropic", "vertex"]
          }
        }
      }
    }
  }
}
```

Some useful routing options:

| Option              | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `order`             | Provider sequence to try                             |
| `only`              | Restrict to specific providers                       |
| `zeroDataRetention` | Only use providers with zero data retention policies |

---

### xAI

Two ways to authenticate: a SuperGrok subscription via device-code OAuth or a pay-as-you-go API key from the xAI console.

#### Option A — SuperGrok subscription

1. Run the `/connect` command and search for **xAI**.

   ```txt
   /connect
   ```

2. Select **SuperGrok Subscription**. OpenCode opens xAI's verification link with the user code pre-populated when supported.

3. Approve the consent screen. If xAI asks for a code, enter the user code displayed by OpenCode. OpenCode polls xAI's token endpoint and stores the resulting OAuth tokens once you approve.

4. Run the `/models` command to select a Grok model.

   ```txt
   /models
   ```

OpenCode refreshes the OAuth access token automatically. Any Grok or X Premium plan that includes Grok API access works; you do not need a separate `XAI_API_KEY`.

#### Option B — API key

1. Head over to the [xAI console](https://console.x.ai/), create an account, and generate an API key.

2. Run the `/connect` command and search for **xAI**.

   ```txt
   /connect
   ```

3. Select **Manually enter API Key** and paste your xAI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _Grok Beta_.

   ```txt
   /models
   ```

---

### Z.AI

1. Head over to the [Z.AI API console](https://z.ai/manage-apikey/apikey-list), create an account, and click **Create a new API key**.

2. Run the `/connect` command and search for **Z.AI**.

   ```txt
   /connect
   ```

   If you are subscribed to the **GLM Coding Plan**, select **Z.AI Coding Plan**.

3. Enter your Z.AI API key.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Run the `/models` command to select a model like _GLM-4.7_.

   ```txt
   /models
   ```

---

### ZenMux

1. Head over to the [ZenMux dashboard](https://zenmux.ai/settings/keys), click **Create API Key**, and copy the key.

2. Run the `/connect` command and search for ZenMux.

   ```txt
   /connect
   ```

3. Enter the API key for the provider.

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

4. Many ZenMux models are preloaded by default, run the `/models` command to select the one you want.

   ```txt
   /models
   ```

   You can also add additional models through your opencode config.

   ```json title="opencode.json" {6}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "zenmux": {
         "models": {
           "somecoolnewmodel": {}
         }
       }
     }
   }
   ```

---

## Custom provider

To add any **OpenAI-compatible** provider that's not listed in the `/connect` command:

:::tip
You can use any OpenAI-compatible provider with opencode. Most modern AI providers offer OpenAI-compatible APIs.

1. Run the `/connect` command and scroll down to **Other**.

   ```bash
   $ /connect

   ┌  Add credential
   │
   ◆  Select provider
   │  ...
   │  ● Other
   └
   ```

2. Enter a unique ID for the provider.

   ```bash
   $ /connect

   ┌  Add credential
   │
   ◇  Enter provider id
   │  myprovider
   └
   ```

   :::note
   Choose a memorable ID, you'll use this in your config file.

3. Enter your API key for the provider.

   ```bash
   $ /connect

   ┌  Add credential
   │
   ▲  This only stores a credential for myprovider - you will need to configure it in opencode.json, check the docs for examples.
   │
   ◇  Enter your API key
   │  sk-...
   └
   ```

4. Create or update your `opencode.json` file in your project directory:

   ```json title="opencode.json" ""myprovider"" {5-15}
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "myprovider": {
         "npm": "@ai-sdk/openai-compatible",
         "name": "My AI Provider Display Name",
         "options": {
           "baseURL": "https://api.myprovider.com/v1"
         },
         "models": {
           "my-model-name": {
             "name": "My Model Display Name"
           }
         }
       }
     }
   }
   ```

   Here are the configuration options:
   - **npm**: AI SDK package to use, `@ai-sdk/openai-compatible` for OpenAI-compatible providers (for `/v1/chat/completions`). If your provider/model uses `/v1/responses`, use `@ai-sdk/openai`.
   - **name**: Display name in UI.
   - **models**: Available models.
   - **options.baseURL**: API endpoint URL.
   - **options.apiKey**: Optionally set the API key, if not using auth.
   - **options.headers**: Optionally set custom headers.

   More on the advanced options in the example below.

5. Run the `/models` command and your custom provider and models will appear in the selection list.

---

##### Example

Here's an example setting the `apiKey`, `headers`, and model `limit` options.

```json title="opencode.json" {9,11,17-20}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "myprovider": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "My AI Provider Display Name",
      "options": {
        "baseURL": "https://api.myprovider.com/v1",
        "apiKey": "{env:ANTHROPIC_API_KEY}",
        "headers": {
          "Authorization": "Bearer custom-token"
        }
      },
      "models": {
        "my-model-name": {
          "name": "My Model Display Name",
          "limit": {
            "context": 200000,
            "output": 65536
          }
        }
      }
    }
  }
}
```

Configuration details:

- **apiKey**: Set using `env` variable syntax, [learn more](/docs/config#env-vars).
- **headers**: Custom headers sent with each request.
- **limit.context**: Maximum input tokens the model accepts.
- **limit.output**: Maximum tokens the model can generate.

The `limit` fields allow OpenCode to understand how much context you have left. Standard providers pull these from models.dev automatically.

---

## Troubleshooting

If you are having trouble with configuring a provider, check the following:

1. **Check the auth setup**: Run `opencode auth list` to see if the credentials
   for the provider are added to your config.

   This doesn't apply to providers like Amazon Bedrock, that rely on environment variables for their auth.

2. For custom providers, check the opencode config and:
   - Make sure the provider ID used in the `/connect` command matches the ID in your opencode config.
   - The right npm package is used for the provider. For example, use `@ai-sdk/cerebras` for Cerebras. And for all other OpenAI-compatible providers, use `@ai-sdk/openai-compatible` (for `/v1/chat/completions`); if a model uses `/v1/responses`, use `@ai-sdk/openai`. For mixed setups under one provider, you can override per model via `provider.npm`.
   - Check correct API endpoint is used in the `options.baseURL` field.

---

## tui

- 官方原文：https://opencode.ai/docs/tui
- 存档：`01-Raw/VibeCoding/opencode/opencode-tui.md`

OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

Running OpenCode starts the TUI for the current directory.

```bash
opencode
```

Or you can start it for a specific working directory.

```bash
opencode /path/to/project
```

Once you're in the TUI, you can prompt it with a message.

```text
Give me a quick summary of the codebase.
```

---

## File references

You can reference files in your messages using `@`. This does a fuzzy file search in the current working directory.

:::tip
You can also use `@` to reference files in your messages.

```text "@packages/functions/src/api/index.ts"
How is auth handled in @packages/functions/src/api/index.ts?
```

The content of the file is added to the conversation automatically.

Configured [references](/docs/references) also appear in `@` autocomplete. Type `@alias` to add the reference root as context, or type `@alias/` to autocomplete files inside that reference.

```text "@docs/README.md"
Compare our setup with @docs/README.md
```

---

## Bash commands

Start a message with `!` to run a shell command.

```bash frame="none"
!ls -la
```

The output of the command is added to the conversation as a tool result.

---

## Commands

When using the OpenCode TUI, you can type `/` followed by a command name to quickly execute actions. For example:

```bash frame="none"
/help
```

Most commands also have keyboard shortcuts using `ctrl+x` as the default leader key. [Learn more](/docs/keybinds).

Here are all available slash commands:

---

### connect

Add a provider to OpenCode. Allows you to select from available providers and add their API keys.

```bash frame="none"
/connect
```

---

### compact

Compact the current session. _Alias_: `/summarize`

```bash frame="none"
/compact
```

**Keybind:** `ctrl+x c`

---

### details

Toggle tool execution details.

```bash frame="none"
/details
```

---

### editor

Open external editor for composing messages. Uses the editor set in your `EDITOR` environment variable. [Learn more](#editor-setup).

```bash frame="none"
/editor
```

**Keybind:** `ctrl+x e`

---

### exit

Exit OpenCode. _Aliases_: `/quit`, `/q`

```bash frame="none"
/exit
```

**Keybind:** `ctrl+x q`

---

### export

Export current conversation to Markdown and open in your default editor. Uses the editor set in your `EDITOR` environment variable. [Learn more](#editor-setup).

```bash frame="none"
/export
```

**Keybind:** `ctrl+x x`

---

### help

Show the help dialog.

```bash frame="none"
/help
```

---

### init

Guided setup for creating or updating `AGENTS.md`. [Learn more](/docs/rules).

```bash frame="none"
/init
```

---

### models

List available models.

```bash frame="none"
/models
```

**Keybind:** `ctrl+x m`

---

### new

Start a new session. _Alias_: `/clear`

```bash frame="none"
/new
```

**Keybind:** `ctrl+x n`

---

### redo

Redo a previously undone message. Only available after using `/undo`.

:::tip
Any file changes will also be restored.

Internally, this uses Git to manage the file changes. So your project **needs to
be a Git repository**.

```bash frame="none"
/redo
```

**Keybind:** `ctrl+x r`

---

### sessions

List and switch between sessions. _Aliases_: `/resume`, `/continue`

```bash frame="none"
/sessions
```

**Keybind:** `ctrl+x l`

---

### share

Share current session. [Learn more](/docs/share).

```bash frame="none"
/share
```

---

### themes

List available themes.

```bash frame="none"
/themes
```

**Keybind:** `ctrl+x t`

---

### thinking

Toggle the visibility of thinking/reasoning blocks in the conversation. When enabled, you can see the model's reasoning process for models that support extended thinking.

:::note
This command only controls whether thinking blocks are **displayed** - it does not enable or disable the model's reasoning capabilities. To toggle actual reasoning capabilities, use `ctrl+t` to cycle through model variants.

```bash frame="none"
/thinking
```

---

### undo

Undo last message in the conversation. Removes the most recent user message, all subsequent responses, and any file changes.

:::tip
Any file changes made will also be reverted.

Internally, this uses Git to manage the file changes. So your project **needs to
be a Git repository**.

```bash frame="none"
/undo
```

**Keybind:** `ctrl+x u`

---

### unshare

Unshare current session. [Learn more](/docs/share#un-sharing).

```bash frame="none"
/unshare
```

---

## Editor setup

Both the `/editor` and `/export` commands use the editor specified in your `EDITOR` environment variable.

    ```bash
    # Example for nano or vim
    export EDITOR=nano
    export EDITOR=vim

    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    export EDITOR="code --wait"
    ```

    To make it permanent, add this to your shell profile;
    `~/.bashrc`, `~/.zshrc`, etc.

    ```bash
    set EDITOR=notepad

    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    set EDITOR=code --wait
    ```

    To make it permanent, use **System Properties** > **Environment
    Variables**.

    ```powershell
    $env:EDITOR = "notepad"

    # For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.
    # include --wait
    $env:EDITOR = "code --wait"
    ```

    To make it permanent, add this to your PowerShell profile.

Popular editor options include:

- `code` - Visual Studio Code
- `cursor` - Cursor
- `windsurf` - Windsurf
- `nvim` - Neovim editor
- `vim` - Vim editor
- `nano` - Nano editor
- `notepad` - Windows Notepad
- `subl` - Sublime Text

:::note
Some editors like VS Code need to be started with the `--wait` flag.

Some editors need command-line arguments to run in blocking mode. The `--wait` flag makes the editor process block until closed.

---

## Configure

You can customize TUI behavior through `tui.json` (or `tui.jsonc`).

```json title="tui.json"
{
  "$schema": "https://opencode.ai/tui.json",
  "theme": "opencode",
  "leader_timeout": 2000,
  "keybinds": {
    "leader": "ctrl+x",
    "command_list": "ctrl+p"
  },
  "scroll_speed": 3,
  "scroll_acceleration": {
    "enabled": false
  },
  "diff_style": "auto",
  "cursor": {
    "style": "block",
    "blinking": true
  },
  "mouse": true,
  "attention": {
    "enabled": true,
    "notifications": true,
    "sound": true,
    "volume": 0.4,
    "sound_pack": "opencode.default",
    "sounds": {
      "error": "./sounds/error.mp3"
    }
  }
}
```

This is separate from `opencode.json`, which configures server/runtime behavior.

`keybinds` is merged with built-in defaults, so you only need to configure the shortcuts you want to change.

### Options

- `theme` - Sets your UI theme. [Learn more](/docs/themes).
- `keybinds` - Customizes keyboard shortcuts. [Learn more](/docs/keybinds).
- `leader_timeout` - Controls how long OpenCode waits after the leader key. Defaults to `2000`.
- `scroll_acceleration.enabled` - Enable macOS-style scroll acceleration for smooth, natural scrolling. When enabled, scroll speed increases with rapid scrolling gestures and stays precise for slower movements. **This setting takes precedence over `scroll_speed` and overrides it when enabled.**
- `scroll_speed` - Controls how fast the TUI scrolls when using scroll commands (minimum: `0.001`, supports decimal values). Defaults to `3`. **Note: This is ignored if `scroll_acceleration.enabled` is set to `true`.**
- `diff_style` - Controls diff rendering. `"auto"` adapts to terminal width, `"stacked"` always shows a single-column layout.
- `cursor` - Controls the terminal cursor in TUI input fields. `style` defaults to `"block"`, can be `"underline"`, `"line"`, or `"default"`; `blinking` defaults to `true`. When `style` is `"default"`, the terminal default cursor is restored, so `blinking` has no effect.
- `mouse` - Enable or disable mouse capture in the TUI (default: `true`). When disabled, the terminal's native mouse selection/scrolling behavior is preserved.
- `attention` - Configures TUI desktop notifications and sounds. Disabled by default.

Use `OPENCODE_TUI_CONFIG` to load a custom TUI config path.

### Attention

The TUI can request attention for questions, permissions, session errors, and completed sessions. Enable it with `attention.enabled`; built-in events play sounds when triggered, and non-subagent events request desktop notifications only when the terminal is blurred.

- `enabled` - Enable all attention notifications and sounds. Defaults to `false`.
- `notifications` - Allow terminal-mediated desktop notifications when attention is enabled. Defaults to `true`.
- `sound` - Allow attention sounds when attention is enabled. Defaults to `true`.
- `volume` - Default sound volume from `0` to `1`. Defaults to `0.4`.
- `sound_pack` - Sound pack ID to use. Defaults to `opencode.default`.
- `sounds` - Override sound files for `default`, `question`, `permission`, `error`, `done`, or `subagent_done`. Paths can be absolute, `file://` URLs, or relative to `tui.json`.

---

## Customization

You can customize various aspects of the TUI view using the command palette (`ctrl+p`). These settings persist across restarts.

---

#### Username display

Toggle whether your username appears in chat messages. Access this through:

- Command palette: Search for "username" or "hide username"
- The setting persists automatically and will be remembered across TUI sessions

---

## zen

- 官方原文：https://opencode.ai/docs/zen
- 存档：`01-Raw/VibeCoding/opencode/opencode-zen.md`

export const console = config.console
export const email = `mailto:${config.email}`

OpenCode Zen is a list of tested and verified models provided by the OpenCode team.

Zen works like any other provider in OpenCode. You login to OpenCode Zen and get
your API key. It's **completely optional** and you don't need to use it to use
OpenCode.

---

## Background

There are a large number of models out there but only a few of
these models work well as coding agents. Additionally, most providers are
configured very differently; so you get very different performance and quality.

:::tip
We tested a select group of models and providers that work well with OpenCode.

So if you are using a model through something like OpenRouter, you can never be
sure if you are getting the best version of the model you want.

To fix this, we did a couple of things:

1. We tested a select group of models and talked to their teams about how to
   best run them.
2. We then worked with a few providers to make sure these were being served
   correctly.
3. Finally, we benchmarked the combination of the model/provider and came up
   with a list that we feel good recommending.

OpenCode Zen is an AI gateway that gives you access to these models.

---

## How it works

OpenCode Zen works like any other provider in OpenCode.

1. You sign in to **<a href={console}>OpenCode Zen</a>**, add your billing
   details, and copy your API key.
2. You run the `/connect` command in the TUI, select OpenCode Zen, and paste your API key.
3. Run `/models` in the TUI to see the list of models we recommend.

You are charged per request and you can add credits to your account.

---

## Endpoints

You can also access our models through the following API endpoints.

| Model                           | Model ID                        | Endpoint                                                  | AI SDK Package              |
| ------------------------------- | ------------------------------- | --------------------------------------------------------- | --------------------------- |
| GPT 6 Astra                     | gpt-6-astra                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.6 Sol                     | gpt-5.6-sol                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.6 Terra                   | gpt-5.6-terra                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.6 Luna                    | gpt-5.6-luna                    | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.5                         | gpt-5.5                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.5 Pro                     | gpt-5.5-pro                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4                         | gpt-5.4                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4 Pro                     | gpt-5.4-pro                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4 Mini                    | gpt-5.4-mini                    | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.4 Nano                    | gpt-5.4-nano                    | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.3 Codex                   | gpt-5.3-codex                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.3 Codex Spark             | gpt-5.3-codex-spark             | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.2                         | gpt-5.2                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.2 Codex                   | gpt-5.2-codex                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1                         | gpt-5.1                         | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1 Codex                   | gpt-5.1-codex                   | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1 Codex Max               | gpt-5.1-codex-max               | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5.1 Codex Mini              | gpt-5.1-codex-mini              | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5                           | gpt-5                           | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5 Codex                     | gpt-5-codex                     | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| GPT 5 Nano                      | gpt-5-nano                      | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Claude Fable 5.1                | claude-fable-5-1                | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Fable 5                  | claude-fable-5                  | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 5                   | claude-opus-5                   | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.8                 | claude-opus-4-8                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.7                 | claude-opus-4-7                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.6                 | claude-opus-4-6                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Opus 4.5                 | claude-opus-4-5                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Sonnet 5                 | claude-sonnet-5                 | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Sonnet 4.6               | claude-sonnet-4-6               | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Sonnet 4.5               | claude-sonnet-4-5               | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Claude Haiku 4.5                | claude-haiku-4-5                | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Gemini 3.8 Flash                | gemini-3.8-flash                | `https://opencode.ai/zen/v1/models/gemini-3.8-flash`      | `@ai-sdk/google`            |
| Gemini 3.7 Flash                | gemini-3.7-flash                | `https://opencode.ai/zen/v1/models/gemini-3.7-flash`      | `@ai-sdk/google`            |
| Gemini 3.6 Flash                | gemini-3.6-flash                | `https://opencode.ai/zen/v1/models/gemini-3.6-flash`      | `@ai-sdk/google`            |
| Gemini 3.5 Flash                | gemini-3.5-flash                | `https://opencode.ai/zen/v1/models/gemini-3.5-flash`      | `@ai-sdk/google`            |
| Gemini 3.5 Flash Lite           | gemini-3.5-flash-lite           | `https://opencode.ai/zen/v1/models/gemini-3.5-flash-lite` | `@ai-sdk/google`            |
| Gemini 3.1 Pro                  | gemini-3.1-pro                  | `https://opencode.ai/zen/v1/models/gemini-3.1-pro`        | `@ai-sdk/google`            |
| Gemini 3 Flash                  | gemini-3-flash                  | `https://opencode.ai/zen/v1/models/gemini-3-flash`        | `@ai-sdk/google`            |
| Grok 4.7                        | grok-4.7                        | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Grok 4.6                        | grok-4.6                        | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Grok 4.5                        | grok-4.5                        | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Grok Build 0.1                  | grok-build-0.1                  | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Muse Spark 1.3                  | muse-spark-1.3                  | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Muse Spark 1.2                  | muse-spark-1.2                  | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |
| Qwen3.8 Flash                   | qwen3.8-flash                   | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.7 Max                     | qwen3.7-max                     | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.7 Plus                    | qwen3.7-plus                    | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.6 Plus                    | qwen3.6-plus                    | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| Qwen3.5 Plus                    | qwen3.5-plus                    | `https://opencode.ai/zen/v1/messages`                     | `@ai-sdk/anthropic`         |
| DeepSeek V4.1 Flash             | deepseek-v4.1-flash             | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Pro                 | deepseek-v4-pro                 | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Flash               | deepseek-v4-flash               | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Flash Vision Exp    | deepseek-v4-flash-vision-exp    | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiniMax M3                      | minimax-m3                      | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiniMax M2.7                    | minimax-m2.7                    | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiniMax M2.5                    | minimax-m2.5                    | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.3 Flash                   | glm-5.3-flash                   | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.3                         | glm-5.3                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.2                         | glm-5.2                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5.1                         | glm-5.1                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| GLM 5                           | glm-5                           | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K2.5                       | kimi-k2.5                       | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K2.6                       | kimi-k2.6                       | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K2.7 Code                  | kimi-k2.7-code                  | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Kimi K3                         | kimi-k3                         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Jev 1.13                        | jev-1.13                        | `https://opencode.ai/zen/v1/systemone`                    | -                           |
| Jev 1.13 Free                   | jev-1.13-free                   | `https://opencode.ai/zen/v1/systemone`                    | -                           |
| Big Pickle                      | big-pickle                      | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiMo-V2.6-Flash Free            | mimo-v2.6-flash-free            | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| MiMo-V2.5 Free                  | mimo-v2.5-free                  | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Ling 3.0 Flash Fin Free         | ling-3.0-flash-fin-free         | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Nemotron 3 Ultra Free           | nemotron-3-ultra-free           | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Nemotron 3.5 Lightning Free     | nemotron-3.5-lightning-free     | `https://opencode.ai/zen/v1/chat/completions`             | `@ai-sdk/openai-compatible` |
| Muse Spark 1.3 Contributor Free | muse-spark-1.3-contributor-free | `https://opencode.ai/zen/v1/responses`                    | `@ai-sdk/openai`            |

The [model id](/docs/config/#models) in your OpenCode config
uses the format `opencode/<model-id>`. For example, for GPT 5.5, you would
use `opencode/gpt-5.5` in your config.

---

### Models

You can fetch the full list of available models and their metadata from:

```
https://opencode.ai/zen/v1/models
```

---

### Jev

Jev is a System One model from TypeSafe AI for fast, structured decisions. Instead of generating text, it evaluates a `state` against typed questions and returns values and probabilities that your code can use directly. It supports yes/no (`noul`), multiple-choice (`choice`), and rubric-based (`score`) questions.

Use your OpenCode Zen API key with the `https://opencode.ai/zen/v1/systemone` endpoint. This example checks whether a support request is urgent:

```bash
curl https://opencode.ai/zen/v1/systemone \
  -H "Authorization: Bearer $OPENCODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-1.13",
    "state": "My payments have failed for three days and I am losing sales. Please help now.",
    "questions": {
      "is_urgent": {
        "type": "noul",
        "instructions": "Does this request require urgent attention?"
      }
    }
  }'
```

You can ask multiple questions in one request. Jev evaluates them in parallel and returns each answer under the matching question ID:

```bash
curl https://opencode.ai/zen/v1/systemone \
  -H "Authorization: Bearer $OPENCODE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "jev-1.13",
    "state": "My order arrived late and the item is damaged. I want a refund.",
    "questions": {
      "department": {
        "type": "choice",
        "instructions": "Which team should handle this request?",
        "criteria": {
          "returns": "Refunds, exchanges, or damaged items",
          "shipping": "Delivery delays or lost packages",
          "billing": "Charges, invoices, or payment problems"
        }
      },
      "frustration": {
        "type": "score",
        "instructions": "How frustrated is the customer?",
        "criteria": ["Calm", "Frustrated", "Very angry"]
      }
    }
  }'
```

Use `jev-1.13-free` instead of `jev-1.13` to use the limited-time free model. See the [TypeSafe AI documentation](https://docs.typesafe.ai/) for details about question types and response fields.

---

## Pricing

We support a pay-as-you-go model. Below are the prices **per 1M tokens**.

| Model                             | Input  | Output  | Cached Read | Cached Write |
| --------------------------------- | ------ | ------- | ----------- | ------------ |
| Big Pickle                        | Free   | Free    | Free        | -            |
| MiMo-V2.6-Flash Free              | Free   | Free    | Free        | -            |
| MiMo-V2.5 Free                    | Free   | Free    | Free        | -            |
| Ling 3.0 Flash Fin Free           | Free   | Free    | Free        | -            |
| Nemotron 3 Ultra Free             | Free   | Free    | Free        | -            |
| Nemotron 3.5 Lightning Free       | Free   | Free    | Free        | -            |
| Muse Spark 1.3 Contributor Free   | Free   | Free    | Free        | -            |
| Jev 1.13 Free                     | Free   | Free    | -           | -            |
| Jev 1.13                          | $0.042 | Free    | -           | -            |
| MiniMax M3                        | $0.30  | $1.20   | $0.06       | -            |
| MiniMax M2.7                      | $0.30  | $1.20   | $0.06       | -            |
| MiniMax M2.5                      | $0.30  | $1.20   | $0.06       | -            |
| GLM 5.3 Flash                     | $0.15  | $0.50   | $0.03       | -            |
| GLM 5.3                           | $1.40  | $4.40   | $0.26       | -            |
| GLM 5.2                           | $1.40  | $4.40   | $0.26       | -            |
| GLM 5.1                           | $1.40  | $4.40   | $0.26       | -            |
| GLM 5                             | $1.00  | $3.20   | $0.20       | -            |
| Kimi K2.7 Code                    | $0.95  | $4.00   | $0.19       | -            |
| Kimi K3                           | $3.00  | $15.00  | $0.30       | -            |
| Kimi K2.6                         | $0.95  | $4.00   | $0.16       | -            |
| Kimi K2.5                         | $0.60  | $3.00   | $0.10       | -            |
| Qwen3.8 Flash                     | $0.15  | $0.47   | $0.016      | $0.20        |
| Qwen3.7 Max                       | $2.50  | $7.50   | $0.50       | $3.125       |
| Qwen3.7 Plus                      | $0.40  | $1.60   | $0.04       | $0.50        |
| Qwen3.6 Plus                      | $0.50  | $3.00   | $0.05       | $0.625       |
| Qwen3.5 Plus                      | $0.20  | $1.20   | $0.02       | $0.25        |
| DeepSeek V4.1 Flash               | $0.30  | $1.20   | $0.006      | -            |
| DeepSeek V4 Pro                   | $1.74  | $3.48   | $0.145      | -            |
| DeepSeek V4 Flash                 | $0.14  | $0.28   | $0.028      | -            |
| DeepSeek V4 Flash Vision Exp      | $0.14  | $0.28   | $0.028      | -            |
| Claude Fable 5.1                  | $10.00 | $50.00  | $0.25       | $12.50       |
| Claude Fable 5                    | $10.00 | $50.00  | $1.00       | $12.50       |
| Claude Opus 5                     | $5.00  | $25.00  | $0.50       | $6.25        |
| Claude Opus 4.8                   | $5.00  | $25.00  | $0.50       | $6.25        |
| Claude Opus 4.7                   | $5.00  | $25.00  | $0.50       | $6.25        |
| Claude Opus 4.6                   | $5.00  | $25.00  | $0.50       | $6.25        |
| Claude Opus 4.5                   | $5.00  | $25.00  | $0.50       | $6.25        |
| Claude Sonnet 5                   | $2.00  | $10.00  | $0.20       | $2.50        |
| Claude Sonnet 4.6                 | $3.00  | $15.00  | $0.30       | $3.75        |
| Claude Sonnet 4.5 (≤ 200K tokens) | $3.00  | $15.00  | $0.30       | $3.75        |
| Claude Sonnet 4.5 (> 200K tokens) | $6.00  | $22.50  | $0.60       | $7.50        |
| Claude Haiku 4.5                  | $1.00  | $5.00   | $0.10       | $1.25        |
| Gemini 3.8 Flash                  | $1.50  | $7.50   | $0.15       | -            |
| Gemini 3.7 Flash                  | $1.50  | $7.50   | $0.15       | -            |
| Gemini 3.6 Flash                  | $1.50  | $7.50   | $0.15       | -            |
| Gemini 3.5 Flash                  | $1.50  | $9.00   | $0.15       | -            |
| Gemini 3.5 Flash Lite             | $0.30  | $2.50   | $0.03       | -            |
| Gemini 3.1 Pro (≤ 200K tokens)    | $2.00  | $12.00  | $0.20       | -            |
| Gemini 3.1 Pro (> 200K tokens)    | $4.00  | $18.00  | $0.40       | -            |
| Gemini 3 Flash                    | $0.50  | $3.00   | $0.05       | -            |
| Grok 4.7 (≤ 200K tokens)          | $2.00  | $6.00   | $0.50       | -            |
| Grok 4.7 (> 200K tokens)          | $4.00  | $12.00  | $1.00       | -            |
| Grok 4.6 (≤ 200K tokens)          | $2.00  | $6.00   | $0.50       | -            |
| Grok 4.6 (> 200K tokens)          | $4.00  | $12.00  | $1.00       | -            |
| Grok 4.5 (≤ 200K tokens)          | $2.00  | $6.00   | $0.30       | -            |
| Grok 4.5 (> 200K tokens)          | $4.00  | $12.00  | $0.60       | -            |
| Grok Build 0.1                    | $1.00  | $2.00   | $0.20       | -            |
| Muse Spark 1.3                    | $1.25  | $4.25   | $0.15       | -            |
| Muse Spark 1.2                    | $1.25  | $4.25   | $0.15       | -            |
| GPT 6 Astra (≤ 272K tokens)       | $10.00 | $50.00  | $1.00       | $12.50       |
| GPT 6 Astra (> 272K tokens)       | $20.00 | $75.00  | $2.00       | $25.00       |
| GPT 5.6 Sol (≤ 272K tokens)       | $4.00  | $20.00  | $0.40       | $5.00        |
| GPT 5.6 Sol (> 272K tokens)       | $8.00  | $30.00  | $0.80       | $10.00       |
| GPT 5.6 Terra (≤ 272K tokens)     | $2.00  | $12.00  | $0.20       | $2.50        |
| GPT 5.6 Terra (> 272K tokens)     | $4.00  | $18.00  | $0.40       | $5.00        |
| GPT 5.6 Luna (≤ 272K tokens)      | $0.20  | $1.20   | $0.02       | $0.25        |
| GPT 5.6 Luna (> 272K tokens)      | $0.40  | $1.80   | $0.04       | $0.50        |
| GPT 5.5 (≤ 272K tokens)           | $5.00  | $30.00  | $0.50       | -            |
| GPT 5.5 (> 272K tokens)           | $10.00 | $45.00  | $1.00       | -            |
| GPT 5.5 Pro                       | $30.00 | $180.00 | $30.00      | -            |
| GPT 5.4 (≤ 272K tokens)           | $2.50  | $15.00  | $0.25       | -            |
| GPT 5.4 (> 272K tokens)           | $5.00  | $22.50  | $0.50       | -            |
| GPT 5.4 Pro                       | $30.00 | $180.00 | $30.00      | -            |
| GPT 5.4 Mini                      | $0.75  | $4.50   | $0.075      | -            |
| GPT 5.4 Nano                      | $0.20  | $1.25   | $0.02       | -            |
| GPT 5.3 Codex Spark               | $1.75  | $14.00  | $0.175      | -            |
| GPT 5.3 Codex                     | $1.75  | $14.00  | $0.175      | -            |
| GPT 5.2                           | $1.75  | $14.00  | $0.175      | -            |
| GPT 5.2 Codex                     | $1.75  | $14.00  | $0.175      | -            |
| GPT 5.1                           | $1.07  | $8.50   | $0.107      | -            |
| GPT 5.1 Codex                     | $1.07  | $8.50   | $0.107      | -            |
| GPT 5.1 Codex Max                 | $1.25  | $10.00  | $0.125      | -            |
| GPT 5.1 Codex Mini                | $0.25  | $2.00   | $0.025      | -            |
| GPT 5                             | $1.07  | $8.50   | $0.107      | -            |
| GPT 5 Codex                       | $1.07  | $8.50   | $0.107      | -            |
| GPT 5 Nano                        | $0.05  | $0.40   | $0.005      | -            |

**DeepSeek V4 Flash Vision Exp:** Images are converted into tokens based on their dimensions and billed as input tokens alongside text tokens. [Learn more](https://api-docs.deepseek.com/quick_start/pricing/).

You may notice [low-cost models](/docs/config/#models), such as Haiku, Nano, or Flash, in your usage history. OpenCode uses these models to generate session titles.

:::note
Credit card fees are passed along at cost (4.4% + $0.30 per transaction); we don't charge anything beyond that.

The free models:

- MiMo-V2.6-Flash Free is available on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- MiMo-V2.5 Free is available on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- Ling 3.0 Flash Fin Free is available on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- Nemotron 3 Ultra Free is available on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- Nemotron 3.5 Lightning Free is available on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- Big Pickle is a stealth model that's free on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- Muse Spark 1.3 Contributor Free is available on OpenCode for a limited time. The team is using this time to collect feedback and improve the model.
- Jev 1.13 Free is available on OpenCode for a limited time.

<a href={email}>Contact us</a> if you have any questions.

---

### Auto-reload

If your balance goes below $5, Zen will automatically reload $20.

You can change the auto-reload amount. You can also disable auto-reload entirely.

---

### Monthly limits

You can also set a monthly usage limit for the entire workspace and for each
member of your team.

For example, let's say you set a monthly usage limit to $20, Zen will not use
more than $20 in a month. But if you have auto-reload enabled, Zen might end up
charging you more than $20 if your balance goes below $5.

---

### Deprecated models

| Model              | Deprecation date  |
| ------------------ | ----------------- |
| GPT 5.2 Codex      | July 23, 2026     |
| GPT 5.1 Codex      | July 23, 2026     |
| GPT 5.1 Codex Max  | July 23, 2026     |
| GPT 5.1 Codex Mini | July 23, 2026     |
| GPT 5 Codex        | July 23, 2026     |
| Claude Opus 4.1    | August 5, 2026    |
| Claude Sonnet 4    | June 15, 2026     |
| Claude Haiku 3.5   | February 16, 2026 |
| Gemini 3 Pro       | March 9, 2026     |
| MiniMax M2.5       | August 5, 2026    |
| MiniMax M2.1       | March 15, 2026    |
| GLM 5              | May 14, 2026      |
| GLM 4.7            | March 15, 2026    |
| GLM 4.6            | March 15, 2026    |
| Kimi K2.5          | August 5, 2026    |
| Kimi K2 Thinking   | March 6, 2026     |
| Kimi K2            | March 6, 2026     |
| Qwen3 Coder 480B   | February 6, 2026  |

---

## Privacy

All our models are hosted in the US. Our providers follow a zero-retention policy and do not use your data for model training, with the following exceptions:

- Big Pickle: During its free period, collected data may be used to improve the model.
- MiMo-V2.6-Flash Free: During its free period, collected data may be used to improve the model.
- MiMo-V2.5 Free: During its free period, collected data may be used to improve the model.
- Ling 3.0 Flash Fin Free: During its free period, collected data may be used to improve the model.
- Nemotron 3 Ultra Free (NVIDIA free endpoints): Trial use only — do not submit personal or confidential data. Your use is logged for security purposes and to improve NVIDIA products and services. The logged session data for improvement purposes is not linked to your identity or any persistent identifier. For more information about our data processing practices, see our [Privacy Policy](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). By interacting with this endpoint, you consent to our collection, recording, and use of such information and the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf).
- Nemotron 3.5 Lightning Free (NVIDIA free endpoints): Trial use only — do not submit personal or confidential data. Your use is logged for security purposes and to improve NVIDIA products and services. The logged session data for improvement purposes is not linked to your identity or any persistent identifier. For more information about our data processing practices, see our [Privacy Policy](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf). By interacting with this endpoint, you consent to our collection, recording, and use of such information and the [NVIDIA API Trial Terms of Service](https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf).
- OpenAI APIs: Requests are retained for 30 days in accordance with [OpenAI's Data Policies](https://platform.openai.com/docs/guides/your-data).
- Anthropic APIs: Requests are retained for 30 days in accordance with [Anthropic's Data Policies](https://docs.anthropic.com/en/docs/claude-code/data-usage).
- Muse Spark 1.3 Contributor Free: Heavily discounted token pricing in exchange for permission to use your prompts and completions to train future Meta models. [Learn more](https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier).

---

## For Teams

Zen also works great for teams. You can invite teammates, assign roles, curate
the models your team uses, and more.

:::note
Workspaces are currently free for teams as a part of the beta.

Managing your workspace is currently free for teams as a part of the beta. We'll be
sharing more details on the pricing soon.

---

### Roles

You can invite teammates to your workspace and assign roles:

- **Admin**: Manage models, members, API keys, and billing
- **Member**: Manage only their own API keys

Admins can also set monthly spending limits for each member to keep costs under control.

---

### Model access

Admins can enable or disable specific models for the workspace. Requests made to a disabled model will return an error.

This is useful for cases where you want to disable the use of a model that
collects data.

---

### Bring your own key

You can use your own OpenAI or Anthropic API keys while still accessing other models in Zen.

When you use your own keys, tokens are billed directly by the provider, not by Zen.

For example, your organization might already have a key for OpenAI or Anthropic
and you want to use that instead of the one that Zen provides.

---

## Goals

We created OpenCode Zen to:

1. **Benchmark** the best models/providers for coding agents.
2. Have access to the **highest quality** options and not downgrade performance or route to cheaper providers.
3. Pass along any **price drops** by selling at cost; so the only markup is to cover our processing fees.
4. Have **no lock-in** by allowing you to use it with any other coding agent. And always let you use any other provider with OpenCode as well.
