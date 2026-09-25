---
title: opencode 官方文档汇编（英文原版） · 04-集成（GitHub·GitLab·IDE·SDK·Server）
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-acp.md
- VibeCoding/opencode/opencode-github.md
- VibeCoding/opencode/opencode-gitlab.md
- VibeCoding/opencode/opencode-go.md
- VibeCoding/opencode/opencode-ide.md
- VibeCoding/opencode/opencode-sdk.md
- VibeCoding/opencode/opencode-server.md
- VibeCoding/opencode/opencode-share.md
- VibeCoding/opencode/opencode-web.md
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

> **汇编性质**：opencode 官方文档 官方原文 9 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## acp

- 官方原文：https://opencode.ai/docs/acp
- 存档：`01-Raw/VibeCoding/opencode/opencode-acp.md`

OpenCode supports the [Agent Client Protocol](https://agentclientprotocol.com) or (ACP), allowing you to use it directly in compatible editors and IDEs.

:::tip
For a list of editors and tools that support ACP, check out the [ACP progress report](https://zed.dev/blog/acp-progress-report#available-now).

ACP is an open protocol that standardizes communication between code editors and AI coding agents.

---

## Configure

To use OpenCode via ACP, configure your editor to run the `opencode acp` command.

The command starts OpenCode as an ACP-compatible subprocess that communicates with your editor over JSON-RPC via stdio.

Below are examples for popular editors that support ACP.

---

### Zed

Install OpenCode from the [Zed ACP Registry](https://zed.dev/docs/ai/external-agents#registry) by running `zed: acp registry` in the Command Palette.

To use a custom OpenCode executable instead, add it to your [Zed](https://zed.dev) configuration (`~/.config/zed/settings.json`):

```json title="~/.config/zed/settings.json"
{
  "agent_servers": {
    "OpenCode": {
      "type": "custom",
      "command": "opencode",
      "args": ["acp"]
    }
  }
}
```

To open it, use the `agent: new thread` action in the **Command Palette**.

You can also bind a keyboard shortcut by editing your `keymap.json`:

```json title="keymap.json"
[
  {
    "bindings": {
      "cmd-alt-o": [
        "agent::NewExternalAgentThread",
        {
          "agent": {
            "custom": {
              "name": "OpenCode",
              "command": {
                "command": "opencode",
                "args": ["acp"]
              }
            }
          }
        }
      ]
    }
  }
]
```

---

### JetBrains IDEs

Add to your [JetBrains IDE](https://www.jetbrains.com/) acp.json according to the [documentation](https://www.jetbrains.com/help/ai-assistant/acp.html):

```json title="acp.json"
{
  "agent_servers": {
    "OpenCode": {
      "command": "/absolute/path/bin/opencode",
      "args": ["acp"]
    }
  }
}
```

To open it, use the new 'OpenCode' agent in the AI Chat agent selector.

---

### Avante.nvim

Add to your [Avante.nvim](https://github.com/yetone/avante.nvim) configuration:

```lua
{
  acp_providers = {
    ["opencode"] = {
      command = "opencode",
      args = { "acp" }
    }
  }
}
```

If you need to pass environment variables:

```lua {6-8}
{
  acp_providers = {
    ["opencode"] = {
      command = "opencode",
      args = { "acp" },
      env = {
        OPENCODE_API_KEY = os.getenv("OPENCODE_API_KEY")
      }
    }
  }
}
```

---

### CodeCompanion.nvim

To use OpenCode as an ACP agent in [CodeCompanion.nvim](https://github.com/olimorris/codecompanion.nvim), add the following to your Neovim config:

```lua
require("codecompanion").setup({
  interactions = {
    chat = {
      adapter = {
        name = "opencode",
        model = "claude-sonnet-4",
      },
    },
  },
})
```

This config sets up CodeCompanion to use OpenCode as the ACP agent for chat.

If you need to pass environment variables (like `OPENCODE_API_KEY`), refer to [Configuring Adapters: Environment Variables](https://codecompanion.olimorris.dev/getting-started#setting-an-api-key) in the CodeCompanion.nvim documentation for full details.

## Support

OpenCode works the same via ACP as it does in the terminal. All features are supported:

:::note
Some built-in slash commands like `/undo` and `/redo` are currently unsupported.

- Built-in tools (file operations, terminal commands, etc.)
- Custom tools and slash commands
- MCP servers configured in your OpenCode config
- Project-specific rules from `AGENTS.md`
- Custom formatters and linters
- Agents and permissions system

---

## github

- 官方原文：https://opencode.ai/docs/github
- 存档：`01-Raw/VibeCoding/opencode/opencode-github.md`

OpenCode integrates with your GitHub workflow. Mention `/opencode` or `/oc` in your comment, and OpenCode will execute tasks within your GitHub Actions runner.

---

## Features

- **Triage issues**: Ask OpenCode to look into an issue and explain it to you.
- **Fix and implement**: Ask OpenCode to fix an issue or implement a feature. And it will work in a new branch and submits a PR with all the changes.
- **Secure**: OpenCode runs inside your GitHub's runners.

---

## Installation

Run the following command in a project that is in a GitHub repo:

```bash
opencode github install
```

This will walk you through installing the GitHub app, creating the workflow, and setting up secrets.

---

### Manual Setup

Or you can set it up manually.

1. **Install the GitHub app**

   Head over to [**github.com/apps/opencode-agent**](https://github.com/apps/opencode-agent). Make sure it's installed on the target repository.

2. **Add the workflow**

   Add the following workflow file to `.github/workflows/opencode.yml` in your repo. Make sure to set the appropriate `model` and required API keys in `env`.

   ```yml title=".github/workflows/opencode.yml" {24,26}
   name: opencode

   on:
     issue_comment:
       types: [created]
     pull_request_review_comment:
       types: [created]

   jobs:
     opencode:
       if: |
         contains(github.event.comment.body, '/oc') ||
         contains(github.event.comment.body, '/opencode')
       runs-on: ubuntu-latest
       permissions:
         id-token: write
       steps:
         - name: Checkout repository
           uses: actions/checkout@v6
           with:
             fetch-depth: 1
             persist-credentials: false

         - name: Run OpenCode
           uses: anomalyco/opencode/github@latest
           env:
             ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
           with:
             model: anthropic/claude-sonnet-4-20250514
             # share: true
   ```

3. **Store the API keys in secrets**

   In your organization or project **settings**, expand **Secrets and variables** on the left and select **Actions**. And add the required API keys.

---

## Configuration

- `model`: The model to use with OpenCode. Takes the format of `provider/model`. This is **required**.
- `agent`: The agent to use. Must be a primary agent. Falls back to `default_agent` from config or `"build"` if not found.
- `share`: Whether to share the OpenCode session. Defaults to **true** for public repositories.
- `prompt`: Optional custom prompt to override the default behavior. Use this to customize how OpenCode processes requests.
- `mentions`: Comma-separated list of trigger phrases, case-insensitive. Defaults to `/opencode,/oc`.
- `variant`: Model variant for provider-specific reasoning effort, for example `high`, `max`, or `minimal`.
- `oidc_base_url`: Base URL for the OIDC token exchange API. Only needed when running a custom GitHub App install. Defaults to `https://api.opencode.ai`.
- `use_github_token`: Set to `true` to use a caller-provided `GITHUB_TOKEN` instead of exchanging an OIDC token for an OpenCode App installation token. Defaults to `false`.

  Use this mode to run without installing the OpenCode GitHub App. Pass the token through `env` and grant the permissions required by your workflow:

  ```yaml
  permissions:
    contents: write
    pull-requests: write
    issues: write

  steps:
    - uses: anomalyco/opencode/github@latest
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        model: anthropic/claude-sonnet-4-20250514
        use_github_token: true
  ```

  `id-token: write` is not required in this mode because OIDC exchange is skipped. To use a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) or another GitHub App token, store it as a secret and pass that secret as `GITHUB_TOKEN` instead.

---

## Supported Events

OpenCode can be triggered by the following GitHub events:

| Event Type                    | Triggered By                           | Details                                                                                                           |
| ----------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `issue_comment`               | Comment on an issue or PR              | Mention `/opencode` or `/oc` in your comment. OpenCode reads context and can create branches, open PRs, or reply. |
| `pull_request_review_comment` | Comment on specific code lines in a PR | Mention `/opencode` or `/oc` while reviewing code. OpenCode receives file path, line numbers, and diff context.   |
| `issues`                      | Issue opened or edited                 | Automatically trigger OpenCode when issues are created or modified. Requires `prompt` input.                      |
| `pull_request`                | PR opened or updated                   | Automatically trigger OpenCode when PRs are opened, synchronized, or reopened. Useful for automated reviews.      |
| `schedule`                    | Cron-based schedule                    | Run OpenCode on a schedule. Requires `prompt` input. Output goes to logs and PRs (no issue to comment on).        |
| `workflow_dispatch`           | Manual trigger from GitHub UI          | Trigger OpenCode on demand via Actions tab. Requires `prompt` input. Output goes to logs and PRs.                 |

### Schedule Example

Run OpenCode on a schedule to perform automated tasks:

```yaml title=".github/workflows/opencode-scheduled.yml"
name: Scheduled OpenCode Task

on:
  schedule:
    - cron: "0 9 * * 1" # Every Monday at 9am UTC

jobs:
  opencode:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: write
      pull-requests: write
      issues: write
    steps:
      - name: Checkout repository
        uses: actions/checkout@v6
        with:
          persist-credentials: false

      - name: Run OpenCode
        uses: anomalyco/opencode/github@latest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        with:
          model: anthropic/claude-sonnet-4-20250514
          prompt: |
            Review the codebase for any TODO comments and create a summary.
            If you find issues worth addressing, open an issue to track them.
```

For scheduled events, the `prompt` input is **required** since there's no comment to extract instructions from. Scheduled workflows run without a user context to permission-check, so the workflow must grant `contents: write` and `pull-requests: write` if you expect OpenCode to create branches or PRs.

---

### Pull Request Example

Automatically review PRs when they are opened or updated:

```yaml title=".github/workflows/opencode-review.yml"
name: opencode-review

on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

jobs:
  review:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
      pull-requests: read
      issues: read
    steps:
      - uses: actions/checkout@v6
        with:
          persist-credentials: false
      - uses: anomalyco/opencode/github@latest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          model: anthropic/claude-sonnet-4-20250514
          use_github_token: true
          prompt: |
            Review this pull request:
            - Check for code quality issues
            - Look for potential bugs
            - Suggest improvements
```

For `pull_request` events, if no `prompt` is provided, OpenCode defaults to reviewing the pull request.

---

### Issues Triage Example

Automatically triage new issues. This example filters to accounts older than 30 days to reduce spam:

```yaml title=".github/workflows/opencode-triage.yml"
name: Issue Triage

on:
  issues:
    types: [opened]

jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: write
      pull-requests: write
      issues: write
    steps:
      - name: Check account age
        id: check
        uses: actions/github-script@v7
        with:
          script: |
            const user = await github.rest.users.getByUsername({
              username: context.payload.issue.user.login
            });
            const created = new Date(user.data.created_at);
            const days = (Date.now() - created) / (1000 * 60 * 60 * 24);
            return days >= 30;
          result-encoding: string

      - uses: actions/checkout@v6
        if: steps.check.outputs.result == 'true'
        with:
          persist-credentials: false

      - uses: anomalyco/opencode/github@latest
        if: steps.check.outputs.result == 'true'
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        with:
          model: anthropic/claude-sonnet-4-20250514
          prompt: |
            Review this issue. If there's a clear fix or relevant docs:
            - Provide documentation links
            - Add error handling guidance for code examples
            Otherwise, do not comment.
```

For `issues` events, the `prompt` input is **required** since there's no comment to extract instructions from.

---

## Custom prompts

Override the default prompt to customize OpenCode's behavior for your workflow.

```yaml title=".github/workflows/opencode.yml"
- uses: anomalyco/opencode/github@latest
  with:
    model: anthropic/claude-sonnet-4-5
    prompt: |
      Review this pull request:
      - Check for code quality issues
      - Look for potential bugs
      - Suggest improvements
```

This is useful for enforcing specific review criteria, coding standards, or focus areas relevant to your project.

---

## Examples

Here are some examples of how you can use OpenCode in GitHub.

- **Explain an issue**

  Add this comment in a GitHub issue.

  ```
  /opencode explain this issue
  ```

  OpenCode will read the entire thread, including all comments, and reply with a clear explanation.

- **Fix an issue**

  In a GitHub issue, say:

  ```
  /opencode fix this
  ```

  And OpenCode will create a new branch, implement the changes, and open a PR with the changes.

- **Review PRs and make changes**

  Leave the following comment on a GitHub PR.

  ```
  Delete the attachment from S3 when the note is removed /oc
  ```

  OpenCode will implement the requested change and commit it to the same PR.

- **Review specific code lines**

  Leave a comment directly on code lines in the PR's "Files" tab. OpenCode automatically detects the file, line numbers, and diff context to provide precise responses.

  ```
  [Comment on specific lines in Files tab]
  /oc add error handling here
  ```

  When commenting on specific lines, OpenCode receives:
  - The exact file being reviewed
  - The specific lines of code
  - The surrounding diff context
  - Line number information

  This allows for more targeted requests without needing to specify file paths or line numbers manually.

---

## gitlab

- 官方原文：https://opencode.ai/docs/gitlab
- 存档：`01-Raw/VibeCoding/opencode/opencode-gitlab.md`

OpenCode integrates with your GitLab workflow through your GitLab CI/CD pipeline or with GitLab Duo.

In both cases, OpenCode will run on your GitLab runners.

---

## GitLab CI

OpenCode works in a regular GitLab pipeline. You can build it into a pipeline as a [CI component](https://docs.gitlab.com/ee/ci/components/)

Here we are using a community-created CI/CD component for OpenCode — [nagyv/gitlab-opencode](https://gitlab.com/nagyv/gitlab-opencode).

---

### Features

- **Use custom configuration per job**: Configure OpenCode with a custom configuration directory, for example `./config/#custom-directory` to enable or disable functionality per OpenCode invocation.
- **Minimal setup**: The CI component sets up OpenCode in the background, you only need to create the OpenCode configuration and the initial prompt.
- **Flexible**: The CI component supports several inputs for customizing its behavior

---

### Setup

1. Store your OpenCode authentication JSON as a File type CI environment variables under **Settings** > **CI/CD** > **Variables**. Make sure to mark them as "Masked and hidden".
2. Add the following to your `.gitlab-ci.yml` file.

   ```yaml title=".gitlab-ci.yml"
   include:
     - component: $CI_SERVER_FQDN/nagyv/gitlab-opencode/opencode@2
       inputs:
         config_dir: ${CI_PROJECT_DIR}/opencode-config
         auth_json: $OPENCODE_AUTH_JSON # The variable name for your OpenCode authentication JSON
         command: optional-custom-command
         message: "Your prompt here"
   ```

For more inputs and use cases [check out the docs](https://gitlab.com/explore/catalog/nagyv/gitlab-opencode) for this component.

---

## GitLab Duo

OpenCode integrates with your GitLab workflow.
Mention `@opencode` in a comment, and OpenCode will execute tasks within your GitLab CI pipeline.

---

### Features

- **Triage issues**: Ask OpenCode to look into an issue and explain it to you.
- **Fix and implement**: Ask OpenCode to fix an issue or implement a feature.
  It will create a new branch and raise a merge request with the changes.
- **Secure**: OpenCode runs on your GitLab runners.

---

### Setup

OpenCode runs in your GitLab CI/CD pipeline, here's what you'll need to set it up:

:::tip
Check out the [**GitLab docs**](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/) for up to date instructions.

1.  Configure your GitLab environment
2.  Set up CI/CD
3.  Get an AI model provider API key
4.  Create a service account
5.  Configure CI/CD variables
6.  Create a flow config file, here's an example:

        <details>

    <summary>Flow configuration</summary>

    ```yaml
    image: node:22-slim
    commands:
      - echo "Installing opencode"
      - npm install --global opencode-ai
      - echo "Installing glab"
      - export GITLAB_TOKEN=$GITLAB_TOKEN_OPENCODE
      - apt-get update --quiet && apt-get install --yes curl wget gpg git && rm --recursive --force /var/lib/apt/lists/*
      - curl --silent --show-error --location "https://raw.githubusercontent.com/upciti/wakemeops/main/assets/install_repository" | bash
      - apt-get install --yes glab
      - echo "Configuring glab"
      - echo $GITLAB_HOST
      - echo "Creating OpenCode auth configuration"
      - mkdir --parents ~/.local/share/opencode
      - |
        cat > ~/.local/share/opencode/auth.json << EOF
        {
          "anthropic": {
            "type": "api",
            "key": "$ANTHROPIC_API_KEY"
          }
        }
        EOF
      - echo "Configuring git"
      - git config --global user.email "opencode@gitlab.com"
      - git config --global user.name "OpenCode"
      - echo "Testing glab"
      - glab issue list
      - echo "Running OpenCode"
      - |
        opencode run "
        You are an AI assistant helping with GitLab operations.

        Context: $AI_FLOW_CONTEXT
        Task: $AI_FLOW_INPUT
        Event: $AI_FLOW_EVENT

        Please execute the requested task using the available GitLab tools.
        Be thorough in your analysis and provide clear explanations.

        <important>
        Please use the glab CLI to access data from GitLab. The glab CLI has already been authenticated. You can run the corresponding commands.

        If you are asked to summarize an MR or issue or asked to provide more information then please post back a note to the MR/Issue so that the user can see it.
        You don't need to commit or push up changes, those will be done automatically based on the file changes you make.
        </important>
        "
      - git checkout --branch $CI_WORKLOAD_REF origin/$CI_WORKLOAD_REF
      - echo "Checking for git changes and pushing if any exist"
      - |
        if ! git diff --quiet || ! git diff --cached --quiet || [ --not --zero "$(git ls-files --others --exclude-standard)" ]; then
          echo "Git changes detected, adding and pushing..."
          git add .
          if git diff --cached --quiet; then
            echo "No staged changes to commit"
          else
            echo "Committing changes to branch: $CI_WORKLOAD_REF"
            git commit --message "Codex changes"
            echo "Pushing changes up to $CI_WORKLOAD_REF"
            git push https://gitlab-ci-token:$GITLAB_TOKEN@$GITLAB_HOST/gl-demo-ultimate-dev-ai-epic-17570/test-java-project.git $CI_WORKLOAD_REF
            echo "Changes successfully pushed"
          fi
        else
          echo "No git changes detected, skipping push"
        fi
    variables:
      - ANTHROPIC_API_KEY
      - GITLAB_TOKEN_OPENCODE
      - GITLAB_HOST
    ```

        </details>

You can refer to the [GitLab CLI agents docs](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/) for detailed instructions.

---

### Examples

Here are some examples of how you can use OpenCode in GitLab.

:::tip
You can configure to use a different trigger phrase than `@opencode`.

- **Explain an issue**

  Add this comment in a GitLab issue.

  ```
  @opencode explain this issue
  ```

  OpenCode will read the issue and reply with a clear explanation.

- **Fix an issue**

  In a GitLab issue, say:

  ```
  @opencode fix this
  ```

  OpenCode will create a new branch, implement the changes, and open a merge request with the changes.

- **Review merge requests**

  Leave the following comment on a GitLab merge request.

  ```
  @opencode review this merge request
  ```

  OpenCode will review the merge request and provide feedback.

---

## go

- 官方原文：https://opencode.ai/docs/go
- 存档：`01-Raw/VibeCoding/opencode/opencode-go.md`

export const console = config.console
export const email = `mailto:${config.email}`

OpenCode Go is a low cost **$10/month subscription** that gives you reliable access to popular open coding models.

Go works like any other provider in OpenCode. You subscribe to OpenCode Go and
get your API key. It's **completely optional** and you don't need to use it to
use OpenCode.

It is designed primarily for international users and provides stable global access.

---

## Background

Open models have gotten really good. They now reach performance close to
proprietary models for coding tasks. And because many providers can serve them
competitively, they are usually far cheaper.

However, getting reliable, low latency access to them can be difficult. Providers
vary in quality and availability.

:::tip
We tested a select group of models and providers that work well with OpenCode.

To fix this, we did a couple of things:

1. We tested a select group of open models and talked to their teams about how to
   best run them.
2. We then worked with a few providers to make sure these were being served
   correctly.
3. Finally, we benchmarked the combination of the model/provider and came up
   with a list that we feel good recommending.

OpenCode Go gives you access to these models for **$10/month**.

---

## How it works

OpenCode Go works like any other provider in OpenCode.

1. You sign in to **<a href={console}>OpenCode Zen</a>**, subscribe to Go, and
   copy your API key.
2. You run the `/connect` command in the TUI, select `OpenCode Go`, and paste
   your API key.
3. Run `/models` in the TUI to see the list of models available through Go.

:::note
Only one member per workspace can subscribe to OpenCode Go.

The current list of models includes:

- **Grok 4.7**
- **Grok 4.6**
- **GLM-5.3-Flash**
- **GLM-5.3**
- **GLM-5.2**
- **GLM-5.1**
- **GPT 5.6 Luna**
- **Kimi K3**
- **Kimi K2.7 Code**
- **Kimi K2.6**
- **LongCat-2.0**
- **MiMo-V2.6-Flash**
- **MiMo-V2.6-Pro**
- **MiMo-V2.5**
- **MiMo-V2.5-Pro**
- **MiniMax M3**
- **MiniMax M2.7**
- **Muse Spark 1.3 Contributor** ([limited regions](https://ai.developer.meta.com/legal/geographic-use-policy))
- **Muse Spark 1.2 Contributor** ([limited regions](https://ai.developer.meta.com/legal/geographic-use-policy))
- **Qwen3.8 Max**
- **Qwen3.8 Flash**
- **Qwen3.7 Max**
- **Qwen3.7 Plus**
- **Qwen3.6 Plus**
- **DeepSeek V4.1 Flash**
- **DeepSeek V4 Pro**
- **DeepSeek V4 Flash**
- **DeepSeek V4 Flash Vision Exp**
- **Hy4 preview**
- **Hy3**

The list of models may change as we test and add new ones.

---

## Where can I use it?

OpenCode Go is designed for [OpenCode](https://opencode.ai) and other coding agents
that produce similar types of requests. Traffic is monitored for abuse that
degrades the experience for other users.

Your client should:

1. Send typical coding agent traffic
2. Identify itself with its own user agent, such as `my-coding-agent/1.0`, rather
   than a generic SDK or HTTP-library name.
3. Send a stable session ID in `x-opencode-session` for each conversation so we can optimize routing and
   prompt caching.

### Validated Clients

Besides OpenCode, the following clients have been validated to work properly
with OpenCode Go. Although we do not guarantee that they will continue to work in the future.

| Client            | Session support                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hermes**        | Builds containing [PR #101864](https://github.com/NousResearch/hermes-agent/pull/101864) send the header on main and auxiliary OpenCode requests. The fix was merged after v0.21.0; that release alone does not include it.                 |
| **Claude Code**   | Go recognizes its native session header. No custom-header wrapper is needed.                                                                                                                                                                |
| **Codex**         | Go recognizes its native session header. Some versions and proxy setups still omit it; preserve the session header when forwarding requests.                                                                                                |
| **ZCode**         | Go recognizes its native session header. Our [request for `x-opencode-session`](https://github.com/zai-org/feedback/issues/492) remains open, but it is no longer necessary to send that specific header.                                   |
| **Pi**            | Current builds send session information for OpenCode. Update older installations.                                                                                                                                                           |
| **jcode**         | Update to **v0.81.6 or later**, which includes the [session-header fix](https://github.com/1jehuang/jcode/issues/1167).                                                                                                                     |
| **Kilo Code CLI** | Builds containing [PR #13752](https://github.com/Kilo-Org/kilocode/pull/13752) restore OpenCode session headers. This fix covers the CLI, not the VS Code extension. See [issue #13723](https://github.com/Kilo-Org/kilocode/issues/13723). |

### Known Problematic Clients

These clients have missing or incomplete session support in the versions we
investigated. The linked reports track fixes and workarounds.

| Client                  | Status and tracking                                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DeepSeek Harness**    | Session information arrives on some model paths, but is missing on others. We recognize its native header; the remaining work is to send it across all adapters. [Discussion #5495](https://github.com/deepseek-ai/deepseek-harness/discussions/5495). |
| **GitHub Copilot Chat** | Automatic session-header support is requested in [VS Code issue #334186](https://github.com/microsoft/vscode/issues/334186).                                                                                                                           |
| **Kimi Code**           | Automatic session-header support is requested in [issue #3506](https://github.com/MoonshotAI/kimi-code/issues/3506).                                                                                                                                   |
| **MiMo Code**           | [Issue #2317](https://github.com/XiaomiMiMo/MiMo-Code/issues/2317) has a proposed fix in [PR #2327](https://github.com/XiaomiMiMo/MiMo-Code/pull/2327), which has not yet merged.                                                                      |

## Usage limits

Usage limits are defined as monthly dollar amounts. The table below shows the
monthly limit and token costs for each model.

Each model has the following usage limits: 5-hour — 20% of the monthly limit;
weekly — 50%; and monthly — 100%.

For example, if a model has a $60 monthly limit, you can spend up to:

- **5-hour limit** — $12 of usage
- **Weekly limit** — $30 of usage
- **Monthly limit** — $60 of usage

Token prices are per 1M tokens.

| Model                                   | Input  | Output | Cached Read | Cached Write | Monthly limit                                        |
| --------------------------------------- | ------ | ------ | ----------- | ------------ | ---------------------------------------------------- |
| GLM-5.3-Flash                           | $0.15  | $0.50  | $0.03       | -            | **$60**                                              |
| GLM-5.3                                 | $1.40  | $4.40  | $0.26       | -            | **$15**                                              |
| GLM-5.2                                 | $1.40  | $4.40  | $0.26       | -            | **$60**                                              |
| GLM-5.1                                 | $1.40  | $4.40  | $0.26       | -            | **$60**                                              |
| Kimi K3                                 | $3.00  | $15.00 | $0.30       | -            | **$15**                                              |
| Kimi K2.7 Code                          | $0.95  | $4.00  | $0.19       | -            | **$60**                                              |
| Kimi K2.6                               | $0.95  | $4.00  | $0.16       | -            | **$60**                                              |
| LongCat-2.0                             | $0.30  | $1.20  | $0.006      | -            | **$60**                                              |
| MiMo-V2.6-Flash                         | $0.14  | $0.28  | $0.0028     | -            | **$60**                                              |
| MiMo-V2.6-Pro                           | $0.435 | $0.87  | $0.003625   | -            | **$15**                                              |
| MiMo-V2.5                               | $0.14  | $0.28  | $0.0028     | -            | **$60**                                              |
| MiMo-V2.5-Pro                           | $0.435 | $0.87  | $0.003625   | -            | **$15**                                              |
| MiniMax M3                              | $0.30  | $1.20  | $0.06       | -            | **$60**                                              |
| MiniMax M2.7                            | $0.30  | $1.20  | $0.06       | $0.375       | **$60**                                              |
| MiniMax M2.5                            | $0.30  | $1.20  | $0.06       | $0.375       | **$60**                                              |
| Muse Spark 1.3 Contributor              | $0.10  | $0.20  | $0.002      | -            | **$60**                                              |
| Muse Spark 1.2 Contributor              | $0.10  | $0.20  | $0.002      | -            | **$60**                                              |
| Qwen3.8 Max                             | $2.00  | $6.00  | $0.25       | $2.50        | **$15**                                              |
| Qwen3.8 Flash                           | $0.15  | $0.47  | $0.016      | $0.20        | **$30**                                              |
| Qwen3.7 Max                             | $2.50  | $7.50  | $0.50       | $3.125       | **$30**                                              |
| Qwen3.7 Plus (≤ 256K tokens)            | $0.40  | $1.60  | $0.04       | $0.50        | **$60**                                              |
| Qwen3.7 Plus (> 256K tokens)            | $1.20  | $4.80  | $0.12       | $1.50        | **$60**                                              |
| Qwen3.6 Plus (≤ 256K tokens)            | $0.50  | $3.00  | $0.05       | $0.625       | **$60**                                              |
| Qwen3.6 Plus (> 256K tokens)            | $2.00  | $6.00  | $0.20       | $2.50        | **$60**                                              |
| DeepSeek V4.1 Flash (Off-Peak)          | $0.15  | $0.60  | $0.003      | -            | ~~$15~~ **$60**<br /><small>4x · Ends Sep 27</small> |
| DeepSeek V4.1 Flash (Peak)              | $0.30  | $1.20  | $0.006      | -            | ~~$15~~ **$60**<br /><small>4x · Ends Sep 27</small> |
| DeepSeek V4 Pro (Off-Peak)              | $0.66  | $1.98  | $0.022      | -            | **$15**                                              |
| DeepSeek V4 Pro (Peak)                  | $1.32  | $3.96  | $0.044      | -            | **$15**                                              |
| DeepSeek V4 Flash (Off-Peak)            | $0.15  | $0.60  | $0.003      | -            | **$30**                                              |
| DeepSeek V4 Flash (Peak)                | $0.30  | $1.20  | $0.006      | -            | **$30**                                              |
| DeepSeek V4 Flash Vision Exp (Off-Peak) | $0.15  | $0.60  | $0.003      | -            | **$15**                                              |
| DeepSeek V4 Flash Vision Exp (Peak)     | $0.30  | $1.20  | $0.006      | -            | **$15**                                              |
| Hy4 preview                             | $0.834 | $2.501 | $0.042      | -            | **$30**                                              |
| Hy3                                     | $0.14  | $0.58  | $0.035      | -            | **$60**                                              |
| Grok 4.7 (≤ 200K tokens)                | $2.00  | $6.00  | $0.50       | -            | **$15**                                              |
| Grok 4.7 (> 200K tokens)                | $4.00  | $12.00 | $1.00       | -            | **$15**                                              |
| Grok 4.6 (≤ 200K tokens)                | $2.00  | $6.00  | $0.50       | -            | **$15**                                              |
| Grok 4.6 (> 200K tokens)                | $4.00  | $12.00 | $1.00       | -            | **$15**                                              |
| GPT 5.6 Luna (≤ 272K tokens)            | $0.20  | $1.20  | $0.02       | $0.25        | **$15**                                              |
| GPT 5.6 Luna (> 272K tokens)            | $0.40  | $1.80  | $0.04       | $0.50        | **$15**                                              |

**DeepSeek V4.1 Flash / V4 Pro / V4 Flash / V4 Flash Vision Exp:** Peak hours are 01:00-04:00 and 06:00-10:00 UTC, Monday through Friday; all other hours, including weekends, are Off-Peak. [Learn more](https://api-docs.deepseek.com/quick_start/pricing/).

**DeepSeek V4 Flash Vision Exp:** Images are converted into tokens based on their dimensions and billed as input tokens alongside text tokens. [Learn more](https://api-docs.deepseek.com/quick_start/pricing/).

### Estimated requests

The table below provides an estimated request count based on typical Go usage patterns:

| Model                                                    | requests per 5 hour       | requests per week          | requests per month          |
| -------------------------------------------------------- | ------------------------- | -------------------------- | --------------------------- |
| GLM-5.3-Flash                                            | 6,320                     | 15,790                     | 31,580                      |
| GLM-5.3                                                  | 220                       | 540                        | 1,080                       |
| GLM-5.2                                                  | 880                       | 2,150                      | 4,300                       |
| GLM-5.1                                                  | 880                       | 2,150                      | 4,300                       |
| Kimi K3                                                  | 110                       | 250                        | 490                         |
| Kimi K2.7 Code                                           | 1,350                     | 3,380                      | 6,750                       |
| Kimi K2.6                                                | 1,150                     | 2,880                      | 5,750                       |
| LongCat-2.0                                              | 11,400                    | 28,600                     | 57,200                      |
| MiMo-V2.6-Flash                                          | 30,100                    | 75,200                     | 150,400                     |
| MiMo-V2.6-Pro                                            | 3,250                     | 8,150                      | 16,300                      |
| MiMo-V2.5                                                | 30,100                    | 75,200                     | 150,400                     |
| MiMo-V2.5-Pro                                            | 3,250                     | 8,150                      | 16,300                      |
| MiniMax M3                                               | 3,200                     | 8,000                      | 16,000                      |
| MiniMax M2.7                                             | 3,400                     | 8,500                      | 17,000                      |
| Muse Spark 1.3 Contributor                               | 45,300                    | 113,300                    | 226,600                     |
| Muse Spark 1.2 Contributor                               | 45,300                    | 113,300                    | 226,600                     |
| Qwen3.8 Max                                              | 160                       | 400                        | 810                         |
| Qwen3.8 Flash                                            | 5,400                     | 13,500                     | 27,000                      |
| Qwen3.7 Max                                              | 170                       | 420                        | 840                         |
| Qwen3.7 Plus                                             | 4,300                     | 10,800                     | 21,600                      |
| Qwen3.6 Plus                                             | 3,300                     | 8,200                      | 16,300                      |
| DeepSeek V4.1 Flash<br /><small>4x · Ends Sep 27</small> | ~~6,500~~<br />**26,000** | ~~16,250~~<br />**65,000** | ~~32,500~~<br />**130,000** |
| DeepSeek V4 Pro                                          | 1,050                     | 2,600                      | 5,200                       |
| DeepSeek V4 Flash                                        | 13,000                    | 32,500                     | 65,000                      |
| DeepSeek V4 Flash Vision Exp                             | 6,500                     | 16,250                     | 32,500                      |
| Hy4 preview                                              | 1,350                     | 3,380                      | 6,770                       |
| Hy3                                                      | 4,300                     | 10,750                     | 21,500                      |
| Grok 4.7                                                 | 169                       | 423                        | 845                         |
| Grok 4.6                                                 | 169                       | 423                        | 845                         |
| GPT 5.6 Luna                                             | 2,050                     | 5,100                      | 10,250                      |

The estimates use the following token counts per request; actual usage varies.

- Grok 4.7/4.6 — 390 input, 32,500 cached, 120 output tokens per request
- GLM-5.3-Flash — 1,000 input, 55,000 cached, 200 output tokens per request
- GLM-5.3/5.2/5.1 — 700 input, 52,000 cached, 150 output tokens per request
- GPT 5.6 Luna — 1,000 input, 50,000 cached, 220 output tokens per request
- Kimi K3 — 1,050 input, 76,500 cached, 300 output tokens per request
- Kimi K2.7/K2.6 — 870 input, 55,000 cached, 200 output tokens per request
- LongCat-2.0 — 920 input, 88,900 cached, 200 output tokens per request
- DeepSeek V4.1 Flash — 410 input, 71,300 cached, 310 output tokens per request
- DeepSeek V4 Pro — 750 input, 82,000 cached, 290 output tokens per request
- DeepSeek V4 Flash — 410 input, 71,300 cached, 310 output tokens per request
- DeepSeek V4 Flash Vision Exp — 410 input, 71,300 cached, 310 output tokens per request
- MiniMax M3 — 510 input, 56,000 cached, 190 output tokens per request
- MiniMax M2.7 — 300 input, 55,000 cached, 125 output tokens per request
- Muse Spark 1.3 Contributor — 620 input, 71,400 cached, 300 output tokens per request
- Muse Spark 1.2 Contributor — 620 input, 71,400 cached, 300 output tokens per request
- MiMo-V2.6-Flash — 830 input, 71,500 cached, 295 output tokens per request
- MiMo-V2.6-Pro — 790 input, 86,000 cached, 305 output tokens per request
- MiMo-V2.5 — 830 input, 71,500 cached, 295 output tokens per request
- MiMo-V2.5-Pro — 790 input, 86,000 cached, 305 output tokens per request
- Qwen3.8 Max — 420 input, 66,000 cached, 200 output tokens per request
- Qwen3.8 Flash — 600 input, 58,000 cached, 200 output tokens per request
- Qwen3.7 Max — 420 input, 66,000 cached, 200 output tokens per request
- Qwen3.7 Plus — 500 input, 57,000 cached, 190 output tokens per request
- Qwen3.6 Plus — 500 input, 57,000 cached, 190 output tokens per request
- Hy4 preview — 830 input, 71,500 cached, 295 output tokens per request
- Hy3 — 830 input, 71,500 cached, 295 output tokens per request

You can track your current usage in the **<a href={console}>console</a>**.

:::tip
If you reach the usage limit, you can continue using the free models.

Usage limits may change as we learn from early usage and feedback.

---

### Usage beyond limits

If you also have credits on your Zen balance, you can enable the **Use balance**
option in the console. When enabled, Go will fall back to your Zen balance
after you've reached your usage limits instead of blocking requests.

---

### Why some models have lower usage

With Go, you pay $10/month, and the included monthly usage varies by model.

For most models, we make this work through bulk discounts and reserved GPU capacity. We then pass those savings on to you as higher monthly usage.

For some models, we haven't had the opportunity to negotiate a discount or host them at a lower cost, either because the model is new or because their public pricing is already discounted.

For these models, you still get a little more than if you paid the model providers directly; this is why their included monthly usage is lower.

---

## Endpoints

You can also access Go models through the following API endpoints.

| Model                        | Model ID                     | Endpoint                                         | AI SDK Package              |
| ---------------------------- | ---------------------------- | ------------------------------------------------ | --------------------------- |
| Grok 4.7                     | grok-4.7                     | `https://opencode.ai/zen/go/v1/responses`        | `@ai-sdk/openai`            |
| Grok 4.6                     | grok-4.6                     | `https://opencode.ai/zen/go/v1/responses`        | `@ai-sdk/openai`            |
| GPT 5.6 Luna                 | gpt-5.6-luna                 | `https://opencode.ai/zen/go/v1/responses`        | `@ai-sdk/openai`            |
| GLM-5.3-Flash                | glm-5.3-flash                | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| GLM-5.3                      | glm-5.3                      | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| GLM-5.2                      | glm-5.2                      | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| GLM-5.1                      | glm-5.1                      | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Kimi K3                      | kimi-k3                      | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Kimi K2.7 Code               | kimi-k2.7-code               | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Kimi K2.6                    | kimi-k2.6                    | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| LongCat-2.0                  | longcat-2.0                  | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| DeepSeek V4.1 Flash          | deepseek-v4.1-flash          | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Pro              | deepseek-v4-pro              | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Flash            | deepseek-v4-flash            | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| DeepSeek V4 Flash Vision Exp | deepseek-v4-flash-vision-exp | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| MiMo-V2.6-Flash              | mimo-v2.6-flash              | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| MiMo-V2.6-Pro                | mimo-v2.6-pro                | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| MiMo-V2.5                    | mimo-v2.5                    | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| MiMo-V2.5-Pro                | mimo-v2.5-pro                | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| MiniMax M3                   | minimax-m3                   | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| MiniMax M2.7                 | minimax-m2.7                 | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| MiniMax M2.5                 | minimax-m2.5                 | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| Muse Spark 1.3 Contributor   | muse-spark-1.3-contributor   | `https://opencode.ai/zen/go/v1/responses`        | `@ai-sdk/openai`            |
| Muse Spark 1.2 Contributor   | muse-spark-1.2-contributor   | `https://opencode.ai/zen/go/v1/responses`        | `@ai-sdk/openai`            |
| Qwen3.8 Max                  | qwen3.8-max                  | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| Qwen3.8 Flash                | qwen3.8-flash                | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| Qwen3.7 Max                  | qwen3.7-max                  | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| Qwen3.7 Plus                 | qwen3.7-plus                 | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| Qwen3.6 Plus                 | qwen3.6-plus                 | `https://opencode.ai/zen/go/v1/messages`         | `@ai-sdk/anthropic`         |
| Hy4 preview                  | hy4-preview                  | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |
| Hy3                          | hy3                          | `https://opencode.ai/zen/go/v1/chat/completions` | `@ai-sdk/openai-compatible` |

The [model id](/docs/config/#models) in your OpenCode config
uses the format `opencode-go/<model-id>`. For example, for Kimi K3, you would
use `opencode-go/kimi-k3` in your config.

---

### Models

You can fetch the full list of available models and their metadata from:

```
https://opencode.ai/zen/go/v1/models
```

---

## Privacy

| Model                        | Model training | Data retention |
| ---------------------------- | -------------- | -------------- |
| Grok 4.7                     | Not used       | 30 days        |
| Grok 4.6                     | Not used       | 30 days        |
| GPT 5.6 Luna                 | Not used       | 30 days        |
| GLM-5.3-Flash                | Not used       | 0 days         |
| GLM-5.3                      | Not used       | 0 days         |
| GLM-5.2                      | Not used       | 0 days         |
| GLM-5.1                      | Not used       | 0 days         |
| Kimi K3                      | Not used       | 0 days         |
| Kimi K2.7 Code               | Not used       | 0 days         |
| Kimi K2.6                    | Not used       | 0 days         |
| LongCat-2.0                  | Not used       | 0 days         |
| MiMo-V2.6-Pro                | Not used       | 0 days         |
| MiMo-V2.6-Flash              | Not used       | 0 days         |
| MiMo-V2.5-Pro                | Not used       | 0 days         |
| MiMo-V2.5                    | Not used       | 0 days         |
| Qwen3.8 Max                  | Not used       | 0 days         |
| Qwen3.8 Flash                | Not used       | 0 days         |
| Qwen3.7 Max                  | Not used       | 0 days         |
| Qwen3.7 Plus                 | Not used       | 0 days         |
| Qwen3.6 Plus                 | Not used       | 0 days         |
| MiniMax M3                   | Not used       | 0 days         |
| MiniMax M2.7                 | Not used       | 0 days         |
| Muse Spark 1.3 Contributor   | Yes            | Not ZDR        |
| Muse Spark 1.2 Contributor   | Yes            | Not ZDR        |
| DeepSeek V4.1 Flash          | Not used       | 0 days\*       |
| DeepSeek V4 Pro              | Not used       | 0 days\*       |
| DeepSeek V4 Flash            | Not used       | 0 days\*       |
| DeepSeek V4 Flash Vision Exp | Not used       | 0 days\*       |
| Hy4 preview                  | Not used       | 0 days         |
| Hy3                          | Not used       | 0 days         |

- **Grok 4.7/4.6:** ZDR disables important API features that depend on stored data, including the stateful Responses API, Files and Collections, and the Batch API. [Learn more](https://docs.x.ai/developers/faq/security#what-is-zero-data-retention-zdr).
- **GPT 5.6 Luna:** Abuse monitoring logs are generated for all API feature usage and retained for up to 30 days. [Learn more](https://developers.openai.com/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring).
- **Muse Spark 1.3 Contributor:** Heavily discounted token pricing in exchange for permission to use your prompts and completions to train future Meta models. Availability is limited to regions permitted by Meta's [Geographic Use Policy](https://ai.developer.meta.com/legal/geographic-use-policy). [Learn more](https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier).
- **Muse Spark 1.2 Contributor:** Heavily discounted token pricing in exchange for permission to use your prompts and completions to train future Meta models. Availability is limited to regions permitted by Meta's [Geographic Use Policy](https://ai.developer.meta.com/legal/geographic-use-policy). [Learn more](https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier).
- **DeepSeek:** ZDR agreement is renewed monthly. The current agreement is valid through September 30, 2026.

---

## Goals

We created OpenCode Go to:

1. Make AI coding **accessible** to more people with a low cost subscription.
2. Provide **reliable** access to the best open coding models.
3. Curate models that are **tested and benchmarked** for coding agent use.
4. Have **no lock-in** by allowing you to use any other provider with OpenCode as well.

---

## ide

- 官方原文：https://opencode.ai/docs/ide
- 存档：`01-Raw/VibeCoding/opencode/opencode-ide.md`

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

---

## sdk

- 官方原文：https://opencode.ai/docs/sdk
- 存档：`01-Raw/VibeCoding/opencode/opencode-sdk.md`

export const typesUrl = `${config.github}/blob/dev/packages/sdk/js/src/gen/types.gen.ts`

The opencode JS/TS SDK provides a type-safe client for interacting with the server.
Use it to build integrations and control opencode programmatically.

[Learn more](/docs/server) about how the server works. For examples, check out the [projects](/docs/ecosystem#projects) built by the community.

---

## Install

Install the SDK from npm:

```bash
npm install @opencode-ai/sdk
```

---

## Create client

Create an instance of opencode:

```javascript

const { client } = await createOpencode()
```

This starts both a server and a client

#### Options

| Option     | Type          | Description                    | Default     |
| ---------- | ------------- | ------------------------------ | ----------- |
| `hostname` | `string`      | Server hostname                | `127.0.0.1` |
| `port`     | `number`      | Server port                    | `4096`      |
| `signal`   | `AbortSignal` | Abort signal for cancellation  | `undefined` |
| `timeout`  | `number`      | Timeout in ms for server start | `5000`      |
| `config`   | `Config`      | Configuration object           | `{}`        |

---

## Config

You can pass a configuration object to customize behavior. The instance still picks up your `opencode.json`, but you can override or add configuration inline:

```javascript

const opencode = await createOpencode({
  hostname: "127.0.0.1",
  port: 4096,
  config: {
    model: "anthropic/claude-3-5-sonnet-20241022",
  },
})

console.log(`Server running at ${opencode.server.url}`)

opencode.server.close()
```

## Client only

If you already have a running instance of opencode, you can create a client instance to connect to it:

```javascript

const client = createOpencodeClient({
  baseUrl: "http://localhost:4096",
})
```

#### Options

| Option          | Type       | Description                      | Default                 |
| --------------- | ---------- | -------------------------------- | ----------------------- |
| `baseUrl`       | `string`   | URL of the server                | `http://localhost:4096` |
| `fetch`         | `function` | Custom fetch implementation      | `globalThis.fetch`      |
| `parseAs`       | `string`   | Response parsing method          | `auto`                  |
| `responseStyle` | `string`   | Return style: `data` or `fields` | `fields`                |
| `throwOnError`  | `boolean`  | Throw errors instead of return   | `false`                 |

---

## Types

The SDK includes TypeScript definitions for all API types. Import them directly:

```typescript
```

All types are generated from the server's OpenAPI specification and available in the <a href={typesUrl}>types file</a>.

---

## Errors

The SDK can throw errors that you can catch and handle:

```typescript
try {
  await client.session.get({ path: { id: "invalid-id" } })
} catch (error) {
  console.error("Failed to get session:", (error as Error).message)
}
```

---

## Structured Output

You can request structured JSON output from the model by specifying an `format` with a JSON schema. The model will use a `StructuredOutput` tool to return validated JSON matching your schema.

### Basic Usage

```typescript
const result = await client.session.prompt({
  path: { id: sessionId },
  body: {
    parts: [{ type: "text", text: "Research Anthropic and provide company info" }],
    format: {
      type: "json_schema",
      schema: {
        type: "object",
        properties: {
          company: { type: "string", description: "Company name" },
          founded: { type: "number", description: "Year founded" },
          products: {
            type: "array",
            items: { type: "string" },
            description: "Main products",
          },
        },
        required: ["company", "founded"],
      },
    },
  },
})

// Access the structured output
console.log(result.data.info.structured_output)
// { company: "Anthropic", founded: 2021, products: ["Claude", "Claude API"] }
```

### Output Format Types

| Type          | Description                                            |
| ------------- | ------------------------------------------------------ |
| `text`        | Default. Standard text response (no structured output) |
| `json_schema` | Returns validated JSON matching the provided schema    |

### JSON Schema Format

When using `type: 'json_schema'`, provide:

| Field        | Type            | Description                                                |
| ------------ | --------------- | ---------------------------------------------------------- |
| `type`       | `'json_schema'` | Required. Specifies JSON schema mode                       |
| `schema`     | `object`        | Required. JSON Schema object defining the output structure |
| `retryCount` | `number`        | Optional. Number of validation retries (default: 2)        |

### Error Handling

If the model fails to produce valid structured output after all retries, the response will include a `StructuredOutputError`:

```typescript
if (result.data.info.error?.name === "StructuredOutputError") {
  console.error("Failed to produce structured output:", result.data.info.error.message)
  console.error("Attempts:", result.data.info.error.retries)
}
```

### Best Practices

1. **Provide clear descriptions** in your schema properties to help the model understand what data to extract
2. **Use `required`** to specify which fields must be present
3. **Keep schemas focused** - complex nested schemas may be harder for the model to fill correctly
4. **Set appropriate `retryCount`** - increase for complex schemas, decrease for simple ones

---

## APIs

The SDK exposes all server APIs through a type-safe client.

---

### Global

| Method            | Description                     | Response                             |
| ----------------- | ------------------------------- | ------------------------------------ |
| `global.health()` | Check server health and version | `{ healthy: true, version: string }` |

---

#### Examples

```javascript
const health = await client.global.health()
console.log(health.data.version)
```

---

### App

| Method         | Description               | Response                                    |
| -------------- | ------------------------- | ------------------------------------------- |
| `app.log()`    | Write a log entry         | `boolean`                                   |
| `app.agents()` | List all available agents | <a href={typesUrl}><code>Agent[]</code></a> |

---

#### Examples

```javascript
// Write a log entry
await client.app.log({
  body: {
    service: "my-app",
    level: "info",
    message: "Operation completed",
  },
})

// List available agents
const agents = await client.app.agents()
```

---

### Project

| Method              | Description         | Response                                      |
| ------------------- | ------------------- | --------------------------------------------- |
| `project.list()`    | List all projects   | <a href={typesUrl}><code>Project[]</code></a> |
| `project.current()` | Get current project | <a href={typesUrl}><code>Project</code></a>   |

---

#### Examples

```javascript
// List all projects
const projects = await client.project.list()

// Get current project
const currentProject = await client.project.current()
```

---

### Path

| Method       | Description      | Response                                 |
| ------------ | ---------------- | ---------------------------------------- |
| `path.get()` | Get current path | <a href={typesUrl}><code>Path</code></a> |

---

#### Examples

```javascript
// Get current path information
const pathInfo = await client.path.get()
```

---

### Config

| Method               | Description                       | Response                                                                                              |
| -------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `config.get()`       | Get config info                   | <a href={typesUrl}><code>Config</code></a>                                                            |
| `config.providers()` | List providers and default models | `{ providers: `<a href={typesUrl}><code>Provider[]</code></a>`, default: { [key: string]: string } }` |

---

#### Examples

```javascript
const config = await client.config.get()

const { providers, default: defaults } = await client.config.providers()
```

---

### Sessions

| Method                                                     | Description                        | Notes                                                                                                                                                                                                                    |
| ---------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `session.list()`                                           | List sessions                      | Returns <a href={typesUrl}><code>Session[]</code></a>                                                                                                                                                                    |
| `session.get({ path })`                                    | Get session                        | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `session.children({ path })`                               | List child sessions                | Returns <a href={typesUrl}><code>Session[]</code></a>                                                                                                                                                                    |
| `session.create({ body })`                                 | Create session                     | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `session.delete({ path })`                                 | Delete session                     | Returns `boolean`                                                                                                                                                                                                        |
| `session.update({ path, body })`                           | Update session properties          | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `session.init({ path, body })`                             | Analyze app and create `AGENTS.md` | Returns `boolean`                                                                                                                                                                                                        |
| `session.abort({ path })`                                  | Abort a running session            | Returns `boolean`                                                                                                                                                                                                        |
| `session.share({ path })`                                  | Share session                      | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `session.unshare({ path })`                                | Unshare session                    | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `session.summarize({ path, body })`                        | Summarize session                  | Returns `boolean`                                                                                                                                                                                                        |
| `session.messages({ path })`                               | List messages in a session         | Returns `{ info: `<a href={typesUrl}><code>Message</code></a>`, parts: `<a href={typesUrl}><code>Part[]</code></a>`}[]`                                                                                                  |
| `session.message({ path })`                                | Get message details                | Returns `{ info: `<a href={typesUrl}><code>Message</code></a>`, parts: `<a href={typesUrl}><code>Part[]</code></a>`}`                                                                                                    |
| `session.prompt({ path, body })`                           | Send prompt message                | `body.noReply: true` returns UserMessage (context only). Default returns <a href={typesUrl}><code>AssistantMessage</code></a> with AI response. Supports `body.outputFormat` for [structured output](#structured-output) |
| `session.command({ path, body })`                          | Send command to session            | Returns `{ info: `<a href={typesUrl}><code>AssistantMessage</code></a>`, parts: `<a href={typesUrl}><code>Part[]</code></a>`}`                                                                                           |
| `session.shell({ path, body })`                            | Run a shell command                | Returns <a href={typesUrl}><code>AssistantMessage</code></a>                                                                                                                                                             |
| `session.revert({ path, body })`                           | Revert a message                   | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `session.unrevert({ path })`                               | Restore reverted messages          | Returns <a href={typesUrl}><code>Session</code></a>                                                                                                                                                                      |
| `postSessionByIdPermissionsByPermissionId({ path, body })` | Respond to a permission request    | Returns `boolean`                                                                                                                                                                                                        |

---

#### Examples

```javascript
// Create and manage sessions
const session = await client.session.create({
  body: { title: "My session" },
})

const sessions = await client.session.list()

// Send a prompt message
const result = await client.session.prompt({
  path: { id: session.id },
  body: {
    model: { providerID: "anthropic", modelID: "claude-3-5-sonnet-20241022" },
    parts: [{ type: "text", text: "Hello!" }],
  },
})

// Inject context without triggering AI response (useful for plugins)
await client.session.prompt({
  path: { id: session.id },
  body: {
    noReply: true,
    parts: [{ type: "text", text: "You are a helpful assistant." }],
  },
})
```

---

### Files

| Method                    | Description                        | Response                                                                                    |
| ------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `find.text({ query })`    | Search for text in files           | Array of match objects with `path`, `lines`, `line_number`, `absolute_offset`, `submatches` |
| `find.files({ query })`   | Find files and directories by name | `string[]` (paths)                                                                          |
| `find.symbols({ query })` | Find workspace symbols             | <a href={typesUrl}><code>Symbol[]</code></a>                                                |
| `file.read({ query })`    | Read a file                        | `{ type: "raw" \| "patch", content: string }`                                               |
| `file.status({ query? })` | Get status for tracked files       | <a href={typesUrl}><code>File[]</code></a>                                                  |

`find.files` supports a few optional query fields:

- `type`: `"file"` or `"directory"`
- `directory`: override the project root for the search
- `limit`: max results (1–200)

---

#### Examples

```javascript
// Search and read files
const textResults = await client.find.text({
  query: { pattern: "function.*opencode" },
})

const files = await client.find.files({
  query: { query: "*.ts", type: "file" },
})

const directories = await client.find.files({
  query: { query: "packages", type: "directory", limit: 20 },
})

const content = await client.file.read({
  query: { path: "src/index.ts" },
})
```

---

### TUI

| Method                         | Description               | Response  |
| ------------------------------ | ------------------------- | --------- |
| `tui.appendPrompt({ body })`   | Append text to the prompt | `boolean` |
| `tui.openHelp()`               | Open the help dialog      | `boolean` |
| `tui.openSessions()`           | Open the session selector | `boolean` |
| `tui.openThemes()`             | Open the theme selector   | `boolean` |
| `tui.openModels()`             | Open the model selector   | `boolean` |
| `tui.submitPrompt()`           | Submit the current prompt | `boolean` |
| `tui.clearPrompt()`            | Clear the prompt          | `boolean` |
| `tui.executeCommand({ body })` | Execute a command         | `boolean` |
| `tui.showToast({ body })`      | Show toast notification   | `boolean` |

---

#### Examples

```javascript
// Control TUI interface
await client.tui.appendPrompt({
  body: { text: "Add this to prompt" },
})

await client.tui.showToast({
  body: { message: "Task completed", variant: "success" },
})
```

---

### Auth

| Method              | Description                    | Response  |
| ------------------- | ------------------------------ | --------- |
| `auth.set({ ... })` | Set authentication credentials | `boolean` |

---

#### Examples

```javascript
await client.auth.set({
  path: { id: "anthropic" },
  body: { type: "api", key: "your-api-key" },
})
```

---

### Events

| Method              | Description               | Response                  |
| ------------------- | ------------------------- | ------------------------- |
| `event.subscribe()` | Server-sent events stream | Server-sent events stream |

---

#### Examples

```javascript
// Listen to real-time events
const events = await client.event.subscribe()
for await (const event of events.stream) {
  console.log("Event:", event.type, event.properties)
}
```

---

## server

- 官方原文：https://opencode.ai/docs/server
- 存档：`01-Raw/VibeCoding/opencode/opencode-server.md`

export const typesUrl = `${config.github}/blob/dev/packages/sdk/js/src/gen/types.gen.ts`

The `opencode serve` command runs a headless HTTP server that exposes an OpenAPI endpoint that an opencode client can use.

---

### Usage

```bash
opencode serve [--port <number>] [--hostname <string>] [--cors <origin>]
```

#### Options

| Flag            | Description                         | Default          |
| --------------- | ----------------------------------- | ---------------- |
| `--port`        | Port to listen on                   | `4096`           |
| `--hostname`    | Hostname to listen on               | `127.0.0.1`      |
| `--mdns`        | Enable mDNS discovery               | `false`          |
| `--mdns-domain` | Custom domain name for mDNS service | `opencode.local` |
| `--cors`        | Additional browser origins to allow | `[]`             |

`--cors` can be passed multiple times:

```bash
opencode serve --cors http://localhost:5173 --cors https://app.example.com
```

---

### Authentication

Set `OPENCODE_SERVER_PASSWORD` to protect the server with HTTP basic auth. The username defaults to `opencode`, or set `OPENCODE_SERVER_USERNAME` to override it. This applies to both `opencode serve` and `opencode web`.

```bash
OPENCODE_SERVER_PASSWORD=your-password opencode serve
```

---

### How it works

When you run `opencode` it starts a TUI and a server. Where the TUI is the
client that talks to the server. The server exposes an OpenAPI 3.1 spec
endpoint. This endpoint is also used to generate an [SDK](/docs/sdk).

:::tip
Use the opencode server to interact with opencode programmatically.

This architecture lets opencode support multiple clients and allows you to interact with opencode programmatically.

You can run `opencode serve` to start a standalone server. If you have the
opencode TUI running, `opencode serve` will start a new server.

---

#### Connect to an existing server

When you start the TUI it randomly assigns a port and hostname. You can instead pass in the `--hostname` and `--port` [flags](/docs/cli). Then use this to connect to its server.

The [`/tui`](#tui) endpoint can be used to drive the TUI through the server. For example, you can prefill or run a prompt. This setup is used by the OpenCode [IDE](/docs/ide) plugins.

---

## Spec

The server publishes an OpenAPI 3.1 spec that can be viewed at:

```
http://<hostname>:<port>/doc
```

For example, `http://localhost:4096/doc`. Use the spec to generate clients or inspect request and response types. Or view it in a Swagger explorer.

---

## APIs

The opencode server exposes the following APIs.

---

### Global

| Method | Path             | Description                    | Response                             |
| ------ | ---------------- | ------------------------------ | ------------------------------------ |
| `GET`  | `/global/health` | Get server health and version  | `{ healthy: true, version: string }` |
| `GET`  | `/global/event`  | Get global events (SSE stream) | Event stream                         |

---

### Project

| Method | Path               | Description             | Response                                      |
| ------ | ------------------ | ----------------------- | --------------------------------------------- |
| `GET`  | `/project`         | List all projects       | <a href={typesUrl}><code>Project[]</code></a> |
| `GET`  | `/project/current` | Get the current project | <a href={typesUrl}><code>Project</code></a>   |

---

### Path & VCS

| Method | Path    | Description                          | Response                                    |
| ------ | ------- | ------------------------------------ | ------------------------------------------- |
| `GET`  | `/path` | Get the current path                 | <a href={typesUrl}><code>Path</code></a>    |
| `GET`  | `/vcs`  | Get VCS info for the current project | <a href={typesUrl}><code>VcsInfo</code></a> |

---

### Instance

| Method | Path                | Description                  | Response  |
| ------ | ------------------- | ---------------------------- | --------- |
| `POST` | `/instance/dispose` | Dispose the current instance | `boolean` |

---

### Config

| Method  | Path                | Description                       | Response                                                                                 |
| ------- | ------------------- | --------------------------------- | ---------------------------------------------------------------------------------------- |
| `GET`   | `/config`           | Get config info                   | <a href={typesUrl}><code>Config</code></a>                                               |
| `PATCH` | `/config`           | Update config                     | <a href={typesUrl}><code>Config</code></a>                                               |
| `GET`   | `/config/providers` | List providers and default models | `{ providers: `<a href={typesUrl}>Provider[]</a>`, default: { [key: string]: string } }` |

---

### Provider

| Method | Path                             | Description                          | Response                                                                            |
| ------ | -------------------------------- | ------------------------------------ | ----------------------------------------------------------------------------------- |
| `GET`  | `/provider`                      | List all providers                   | `{ all: `<a href={typesUrl}>Provider[]</a>`, default: {...}, connected: string[] }` |
| `GET`  | `/provider/auth`                 | Get provider authentication methods  | `{ [providerID: string]: `<a href={typesUrl}>ProviderAuthMethod[]</a>` }`           |
| `POST` | `/provider/{id}/oauth/authorize` | Authorize a provider using OAuth     | <a href={typesUrl}><code>ProviderAuthAuthorization</code></a>                       |
| `POST` | `/provider/{id}/oauth/callback`  | Handle OAuth callback for a provider | `boolean`                                                                           |

---

### Sessions

| Method   | Path                                     | Description                           | Notes                                                                              |
| -------- | ---------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------- |
| `GET`    | `/session`                               | List all sessions                     | Returns <a href={typesUrl}><code>Session[]</code></a>                              |
| `POST`   | `/session`                               | Create a new session                  | body: `{ parentID?, title? }`, returns <a href={typesUrl}><code>Session</code></a> |
| `GET`    | `/session/status`                        | Get session status for all sessions   | Returns `{ [sessionID: string]: `<a href={typesUrl}>SessionStatus</a>` }`          |
| `GET`    | `/session/:id`                           | Get session details                   | Returns <a href={typesUrl}><code>Session</code></a>                                |
| `DELETE` | `/session/:id`                           | Delete a session and all its data     | Returns `boolean`                                                                  |
| `PATCH`  | `/session/:id`                           | Update session properties             | body: `{ title? }`, returns <a href={typesUrl}><code>Session</code></a>            |
| `GET`    | `/session/:id/children`                  | Get a session's child sessions        | Returns <a href={typesUrl}><code>Session[]</code></a>                              |
| `GET`    | `/session/:id/todo`                      | Get the todo list for a session       | Returns <a href={typesUrl}><code>Todo[]</code></a>                                 |
| `POST`   | `/session/:id/init`                      | Analyze app and create `AGENTS.md`    | body: `{ messageID, providerID, modelID }`, returns `boolean`                      |
| `POST`   | `/session/:id/fork`                      | Fork an existing session at a message | body: `{ messageID? }`, returns <a href={typesUrl}><code>Session</code></a>        |
| `POST`   | `/session/:id/abort`                     | Abort a running session               | Returns `boolean`                                                                  |
| `POST`   | `/session/:id/share`                     | Share a session                       | Returns <a href={typesUrl}><code>Session</code></a>                                |
| `DELETE` | `/session/:id/share`                     | Unshare a session                     | Returns <a href={typesUrl}><code>Session</code></a>                                |
| `GET`    | `/session/:id/diff`                      | Get the diff for this session         | query: `messageID?`, returns <a href={typesUrl}><code>FileDiff[]</code></a>        |
| `POST`   | `/session/:id/summarize`                 | Summarize the session                 | body: `{ providerID, modelID }`, returns `boolean`                                 |
| `POST`   | `/session/:id/revert`                    | Revert a message                      | body: `{ messageID, partID? }`, returns `boolean`                                  |
| `POST`   | `/session/:id/unrevert`                  | Restore all reverted messages         | Returns `boolean`                                                                  |
| `POST`   | `/session/:id/permissions/:permissionID` | Respond to a permission request       | body: `{ response, remember? }`, returns `boolean`                                 |

---

### Messages

| Method | Path                              | Description                             | Notes                                                                                                                                                                 |
| ------ | --------------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`  | `/session/:id/message`            | List messages in a session              | query: `limit?`, returns `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}[]`                                                        |
| `POST` | `/session/:id/message`            | Send a message and wait for response    | body: `{ messageID?, model?, agent?, noReply?, system?, tools?, parts }`, returns `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}` |
| `GET`  | `/session/:id/message/:messageID` | Get message details                     | Returns `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}`                                                                           |
| `POST` | `/session/:id/prompt_async`       | Send a message asynchronously (no wait) | body: same as `/session/:id/message`, returns `204 No Content`                                                                                                        |
| `POST` | `/session/:id/command`            | Execute a slash command                 | body: `{ messageID?, agent?, model?, command, arguments }`, returns `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}`               |
| `POST` | `/session/:id/shell`              | Run a shell command                     | body: `{ agent, model?, command }`, returns `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}`                                       |

---

### Commands

| Method | Path       | Description       | Response                                      |
| ------ | ---------- | ----------------- | --------------------------------------------- |
| `GET`  | `/command` | List all commands | <a href={typesUrl}><code>Command[]</code></a> |

---

### Files

| Method | Path                     | Description                        | Response                                                                                    |
| ------ | ------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `GET`  | `/find?pattern=<pat>`    | Search for text in files           | Array of match objects with `path`, `lines`, `line_number`, `absolute_offset`, `submatches` |
| `GET`  | `/find/file?query=<q>`   | Find files and directories by name | `string[]` (paths)                                                                          |
| `GET`  | `/find/symbol?query=<q>` | Find workspace symbols             | <a href={typesUrl}><code>Symbol[]</code></a>                                                |
| `GET`  | `/file?path=<path>`      | List files and directories         | <a href={typesUrl}><code>FileNode[]</code></a>                                              |
| `GET`  | `/file/content?path=<p>` | Read a file                        | <a href={typesUrl}><code>FileContent</code></a>                                             |
| `GET`  | `/file/status`           | Get status for tracked files       | <a href={typesUrl}><code>File[]</code></a>                                                  |

#### `/find/file` query parameters

- `query` (required) — search string (fuzzy match)
- `type` (optional) — limit results to `"file"` or `"directory"`
- `directory` (optional) — override the project root for the search
- `limit` (optional) — max results (1–200)
- `dirs` (optional) — legacy flag (`"false"` returns only files)

---

### Tools (Experimental)

| Method | Path                                        | Description                              | Response                                     |
| ------ | ------------------------------------------- | ---------------------------------------- | -------------------------------------------- |
| `GET`  | `/experimental/tool/ids`                    | List all tool IDs                        | <a href={typesUrl}><code>ToolIDs</code></a>  |
| `GET`  | `/experimental/tool?provider=<p>&model=<m>` | List tools with JSON schemas for a model | <a href={typesUrl}><code>ToolList</code></a> |

---

### LSP, Formatters & MCP

| Method | Path         | Description                | Response                                                 |
| ------ | ------------ | -------------------------- | -------------------------------------------------------- |
| `GET`  | `/lsp`       | Get LSP server status      | <a href={typesUrl}><code>LSPStatus[]</code></a>          |
| `GET`  | `/formatter` | Get formatter status       | <a href={typesUrl}><code>FormatterStatus[]</code></a>    |
| `GET`  | `/mcp`       | Get MCP server status      | `{ [name: string]: `<a href={typesUrl}>MCPStatus</a>` }` |
| `POST` | `/mcp`       | Add MCP server dynamically | body: `{ name, config }`, returns MCP status object      |

---

### Agents

| Method | Path     | Description               | Response                                    |
| ------ | -------- | ------------------------- | ------------------------------------------- |
| `GET`  | `/agent` | List all available agents | <a href={typesUrl}><code>Agent[]</code></a> |

---

### Logging

| Method | Path   | Description                                                  | Response  |
| ------ | ------ | ------------------------------------------------------------ | --------- |
| `POST` | `/log` | Write log entry. Body: `{ service, level, message, extra? }` | `boolean` |

---

### TUI

| Method | Path                    | Description                                 | Response               |
| ------ | ----------------------- | ------------------------------------------- | ---------------------- |
| `POST` | `/tui/append-prompt`    | Append text to the prompt                   | `boolean`              |
| `POST` | `/tui/open-help`        | Open the help dialog                        | `boolean`              |
| `POST` | `/tui/open-sessions`    | Open the session selector                   | `boolean`              |
| `POST` | `/tui/open-themes`      | Open the theme selector                     | `boolean`              |
| `POST` | `/tui/open-models`      | Open the model selector                     | `boolean`              |
| `POST` | `/tui/submit-prompt`    | Submit the current prompt                   | `boolean`              |
| `POST` | `/tui/clear-prompt`     | Clear the prompt                            | `boolean`              |
| `POST` | `/tui/execute-command`  | Execute a command (`{ command }`)           | `boolean`              |
| `POST` | `/tui/show-toast`       | Show toast (`{ title?, message, variant }`) | `boolean`              |
| `GET`  | `/tui/control/next`     | Wait for the next control request           | Control request object |
| `POST` | `/tui/control/response` | Respond to a control request (`{ body }`)   | `boolean`              |

---

### Auth

| Method | Path        | Description                                                     | Response  |
| ------ | ----------- | --------------------------------------------------------------- | --------- |
| `PUT`  | `/auth/:id` | Set authentication credentials. Body must match provider schema | `boolean` |

---

### Events

| Method | Path     | Description                                                                   | Response                  |
| ------ | -------- | ----------------------------------------------------------------------------- | ------------------------- |
| `GET`  | `/event` | Server-sent events stream. First event is `server.connected`, then bus events | Server-sent events stream |

---

### Docs

| Method | Path   | Description               | Response                    |
| ------ | ------ | ------------------------- | --------------------------- |
| `GET`  | `/doc` | OpenAPI 3.1 specification | HTML page with OpenAPI spec |

---

## share

- 官方原文：https://opencode.ai/docs/share
- 存档：`01-Raw/VibeCoding/opencode/opencode-share.md`

OpenCode's share feature allows you to create public links to your OpenCode conversations, so you can collaborate with teammates or get help from others.

:::note
Shared conversations are publicly accessible to anyone with the link.

---

## How it works

When you share a conversation, OpenCode:

1. Creates a unique public URL for your session
2. Syncs your conversation history to our servers
3. Makes the conversation accessible via the shareable link — `opncd.ai/s/<share-id>`

---

## Sharing

OpenCode supports three sharing modes that control how conversations are shared:

---

### Manual (default)

By default, OpenCode uses manual sharing mode. Sessions are not shared automatically, but you can manually share them using the `/share` command:

```
/share
```

This will generate a unique URL that'll be copied to your clipboard.

To explicitly set manual mode in your [config file](/docs/config):

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "manual"
}
```

---

### Auto-share

You can enable automatic sharing for all new conversations by setting the `share` option to `"auto"` in your [config file](/docs/config):

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "auto"
}
```

With auto-share enabled, every new conversation will automatically be shared and a link will be generated.

---

### Disabled

You can disable sharing entirely by setting the `share` option to `"disabled"` in your [config file](/docs/config):

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "disabled"
}
```

To enforce this across your team for a given project, add it to the `opencode.json` in your project and check into Git.

---

## Un-sharing

To stop sharing a conversation and remove it from public access:

```
/unshare
```

This will remove the share link and delete the data related to the conversation.

---

## Privacy

There are a few things to keep in mind when sharing a conversation.

---

### Data retention

Shared conversations remain accessible until you explicitly unshare them. This
includes:

- Full conversation history
- All messages and responses
- Session metadata

---

### Recommendations

- Only share conversations that don't contain sensitive information.
- Review conversation content before sharing.
- Unshare conversations when collaboration is complete.
- Avoid sharing conversations with proprietary code or confidential data.
- For sensitive projects, disable sharing entirely.

---

## For enterprises

For enterprise deployments, the share feature can be:

- **Disabled** entirely for security compliance
- **Restricted** to users authenticated through SSO only
- **Self-hosted** on your own infrastructure

[Learn more](/docs/enterprise) about using opencode in your organization.

---

## Start the web server

- 官方原文：https://opencode.ai/docs/web
- 存档：`01-Raw/VibeCoding/opencode/opencode-web.md`

OpenCode can run as a web application in your browser, providing the same powerful AI coding experience without needing a terminal.

## Getting Started

Start the web interface by running:

```bash
opencode web
```

This starts a local server on `127.0.0.1` with a random available port and automatically opens OpenCode in your default browser.

:::caution
If `OPENCODE_SERVER_PASSWORD` is not set, the server will be unsecured. This is fine for local use but should be set for network access.

:::tip[Windows Users]
For the best experience, run `opencode web` from [WSL](/docs/windows-wsl) rather than PowerShell. This ensures proper file system access and terminal integration.

---

## Configuration

You can configure the web server using command line flags or in your [config file](/docs/config).

### Port

By default, OpenCode picks an available port. You can specify a port:

```bash
opencode web --port 4096
```

### Hostname

By default, the server binds to `127.0.0.1` (localhost only). To make OpenCode accessible on your network:

```bash
opencode web --hostname 0.0.0.0
```

When using `0.0.0.0`, OpenCode will display both local and network addresses:

```
  Local access:       http://localhost:4096
  Network access:     http://192.168.1.100:4096
```

### mDNS Discovery

Enable mDNS to make your server discoverable on the local network:

```bash
opencode web --mdns
```

This automatically sets the hostname to `0.0.0.0` and advertises the server as `opencode.local`.

You can customize the mDNS domain name to run multiple instances on the same network:

```bash
opencode web --mdns --mdns-domain myproject.local
```

### CORS

To allow additional domains for CORS (useful for custom frontends):

```bash
opencode web --cors https://example.com
```

### Authentication

To protect access, set a password using the `OPENCODE_SERVER_PASSWORD` environment variable:

```bash
OPENCODE_SERVER_PASSWORD=secret opencode web
```

The username defaults to `opencode` but can be changed with `OPENCODE_SERVER_USERNAME`.

---

## Using the Web Interface

Once started, the web interface provides access to your OpenCode sessions.

### Sessions

View and manage your sessions from the homepage. You can see active sessions and start new ones.

### Server Status

Click "See Servers" to view connected servers and their status.

---

## Attaching a Terminal

You can attach a terminal TUI to a running web server:

```bash
# Start the web server
opencode web --port 4096

# In another terminal, attach the TUI
opencode attach http://localhost:4096
```

This allows you to use both the web interface and terminal simultaneously, sharing the same sessions and state.

---

## Config File

You can also configure server settings in your `opencode.json` config file:

```json
{
  "server": {
    "port": 4096,
    "hostname": "0.0.0.0",
    "mdns": true,
    "cors": ["https://example.com"]
  }
}
```

Command line flags take precedence over config file settings.
