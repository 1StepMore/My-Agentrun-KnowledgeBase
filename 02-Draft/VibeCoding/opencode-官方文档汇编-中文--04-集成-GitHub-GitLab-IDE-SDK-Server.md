---
title: opencode 官方文档汇编（中文） · 04-集成（GitHub·GitLab·IDE·SDK·Server）
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-zh-acp.md
- VibeCoding/opencode/opencode-zh-github.md
- VibeCoding/opencode/opencode-zh-gitlab.md
- VibeCoding/opencode/opencode-zh-go.md
- VibeCoding/opencode/opencode-zh-ide.md
- VibeCoding/opencode/opencode-zh-sdk.md
- VibeCoding/opencode/opencode-zh-server.md
- VibeCoding/opencode/opencode-zh-share.md
- VibeCoding/opencode/opencode-zh-web.md
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
  time_wiki: '2026-09-23T10:40:21+08:00'
wiki_ref: 03-Wiki/氛围编程/_MOC-氛围编程.md
---

> **汇编性质**：opencode 官方文档 官方原文 9 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## acp

- 官方原文：https://opencode.ai/docs/zh-cn/acp
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-acp.md`

OpenCode 支持 [Agent Client Protocol](https://agentclientprotocol.com)（ACP），允许你直接在兼容的编辑器和 IDE 中使用它。

:::tip
有关支持 ACP 的编辑器和工具列表，请查看 [ACP 进展报告](https://zed.dev/blog/acp-progress-report#available-now)。

ACP 是一个开放协议，用于标准化代码编辑器与 AI 编码代理之间的通信。

---

## 配置

要通过 ACP 使用 OpenCode，请在编辑器中配置运行 `opencode acp` 命令。

该命令会将 OpenCode 作为兼容 ACP 的子进程启动，通过 stdio 上的 JSON-RPC 与编辑器进行通信。

以下是支持 ACP 的常用编辑器的配置示例。

---

### Zed

在命令面板中运行 `zed: acp registry`，从 [Zed ACP 注册表](https://zed.dev/docs/ai/external-agents#registry)安装 OpenCode。

如果要改用自定义 OpenCode 可执行文件，请将其添加到 [Zed](https://zed.dev) 配置文件（`~/.config/zed/settings.json`）中：

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

打开方式：在**命令面板**中执行 `agent: new thread` 操作。

你也可以通过编辑 `keymap.json` 来绑定键盘快捷键：

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

根据[文档](https://www.jetbrains.com/help/ai-assistant/acp.html)，将以下内容添加到你的 [JetBrains IDE](https://www.jetbrains.com/) 的 acp.json 中：

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

打开方式：在 AI Chat 代理选择器中选择新的 'OpenCode' 代理。

---

### Avante.nvim

添加到你的 [Avante.nvim](https://github.com/yetone/avante.nvim) 配置中：

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

如果需要传递环境变量：

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

要在 [CodeCompanion.nvim](https://github.com/olimorris/codecompanion.nvim) 中将 OpenCode 用作 ACP 代理，请将以下内容添加到你的 Neovim 配置中：

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

此配置将 CodeCompanion 设置为使用 OpenCode 作为聊天的 ACP 代理。

如果需要传递环境变量（如 `OPENCODE_API_KEY`），请参阅 CodeCompanion.nvim 文档中的[配置适配器：环境变量](https://codecompanion.olimorris.dev/getting-started#setting-an-api-key)了解详细信息。

## 支持

OpenCode 通过 ACP 使用时与在终端中使用的效果完全一致。所有功能均受支持：

:::note
部分内置斜杠命令（如 `/undo` 和 `/redo`）目前暂不支持。

- 内置工具（文件操作、终端命令等）
- 自定义工具和斜杠命令
- 在 OpenCode 配置中配置的 MCP 服务器
- 来自 `AGENTS.md` 的项目级规则
- 自定义格式化工具和代码检查工具
- 代理和权限系统

---

## github

- 官方原文：https://opencode.ai/docs/zh-cn/github
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-github.md`

OpenCode 可以与你的 GitHub 工作流集成。在评论中提及 `/opencode` 或 `/oc`，OpenCode 就会在你的 GitHub Actions 运行器中执行任务。

---

## 功能特性

- **问题分类**：让 OpenCode 调查某个 Issue 并为你做出解释。
- **修复与实现**：让 OpenCode 修复 Issue 或实现某个功能。它会在新分支中工作，并提交包含所有变更的 PR。
- **安全可靠**：OpenCode 在你自己的 GitHub 运行器中运行。

---

## 安装

在一个位于 GitHub 仓库中的项目里运行以下命令：

```bash
opencode github install
```

该命令会引导你完成 GitHub App 的安装、工作流的创建以及密钥的配置。

---

### 手动设置

你也可以手动进行设置。

1. **安装 GitHub App**

   前往 [**github.com/apps/opencode-agent**](https://github.com/apps/opencode-agent)，确保已在目标仓库中安装该应用。

2. **添加工作流**

   将以下工作流文件添加到仓库的 `.github/workflows/opencode.yml` 中。请确保在 `env` 中设置合适的 `model` 及所需的 API 密钥。

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
             # github_token: xxxx
   ```

3. **将 API 密钥存储到 Secrets 中**

   在你的组织或项目的 **Settings** 中，展开左侧的 **Secrets and variables**，然后选择 **Actions**，添加所需的 API 密钥。

---

## 配置

- `model`：OpenCode 使用的模型，格式为 `provider/model`。此项为**必填**。
- `agent`：要使用的代理，必须是主代理。如果未找到，则回退到配置中的 `default_agent`，若仍未找到则使用 `"build"`。
- `share`：是否共享 OpenCode 会话。对于公开仓库，默认为 **true**。
- `prompt`：可选的自定义提示词，用于覆盖默认行为。可通过此项自定义 OpenCode 处理请求的方式。
- `token`：可选的 GitHub 访问 Token，用于执行创建评论、提交变更和创建 Pull Request 等操作。默认情况下，OpenCode 使用 OpenCode GitHub App 的安装访问 Token，因此提交、评论和 Pull Request 会显示为来自该应用。

  你也可以使用 GitHub Action 运行器内置的 [`GITHUB_TOKEN`](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)，而无需安装 OpenCode GitHub App。只需确保在工作流中授予所需的权限：

  ```yaml
  permissions:
    id-token: write
    contents: write
    pull-requests: write
    issues: write
  ```

  如果你愿意，也可以使用[个人访问令牌](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)（PAT）。

---

## 支持的事件

OpenCode 可以由以下 GitHub 事件触发：

| 事件类型                      | 触发方式                     | 详情                                                                                      |
| ----------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------- |
| `issue_comment`               | 在 Issue 或 PR 上发表评论    | 在评论中提及 `/opencode` 或 `/oc`。OpenCode 会读取上下文，并可创建分支、提交 PR 或回复。  |
| `pull_request_review_comment` | 在 PR 中对特定代码行发表评论 | 在代码审查时提及 `/opencode` 或 `/oc`。OpenCode 会接收文件路径、行号和 diff 上下文。      |
| `issues`                      | Issue 被创建或编辑           | 在 Issue 创建或修改时自动触发 OpenCode。需要提供 `prompt` 输入。                          |
| `pull_request`                | PR 被创建或更新              | 在 PR 被打开、同步或重新打开时自动触发 OpenCode。适用于自动化审查场景。                   |
| `schedule`                    | 基于 Cron 的定时任务         | 按计划运行 OpenCode。需要提供 `prompt` 输入。输出会写入日志和 PR（没有 Issue 可供评论）。 |
| `workflow_dispatch`           | 从 GitHub UI 手动触发        | 通过 Actions 选项卡按需触发 OpenCode。需要提供 `prompt` 输入。输出会写入日志和 PR。       |

### 定时任务示例

按计划运行 OpenCode 以执行自动化任务：

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

对于定时事件，`prompt` 输入为**必填**，因为没有评论可供提取指令。定时工作流在运行时没有用户上下文来进行权限检查，因此如果你希望 OpenCode 创建分支或 PR，工作流必须授予 `contents: write` 和 `pull-requests: write` 权限。

---

### Pull Request 示例

在 PR 被创建或更新时自动进行审查：

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

对于 `pull_request` 事件，如果未提供 `prompt`，OpenCode 将默认对该 Pull Request 进行审查。

---

### Issue 分类示例

自动分类新建的 Issue。以下示例会过滤掉注册不满 30 天的账户以减少垃圾信息：

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

对于 `issues` 事件，`prompt` 输入为**必填**，因为没有评论可供提取指令。

---

## 自定义提示词

覆盖默认提示词，以便为你的工作流自定义 OpenCode 的行为。

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

这对于在项目中实施特定的审查标准、编码规范或关注重点非常有用。

---

## 示例

以下是在 GitHub 中使用 OpenCode 的一些示例。

- **解释 Issue**

  在 GitHub Issue 中添加以下评论：

  ```
  /opencode explain this issue
  ```

  OpenCode 会阅读整个讨论串（包括所有评论），并回复一份清晰的解释。

- **修复 Issue**

  在 GitHub Issue 中输入：

  ```
  /opencode fix this
  ```

  OpenCode 会创建一个新分支，实现变更，并提交一个包含所有修改的 PR。

- **审查 PR 并进行修改**

  在 GitHub PR 上留下以下评论：

  ```
  Delete the attachment from S3 when the note is removed /oc
  ```

  OpenCode 会实现所请求的变更并将其提交到同一个 PR 中。

- **审查特定代码行**

  在 PR 的 "Files" 选项卡中直接对代码行留下评论。OpenCode 会自动检测文件、行号和 diff 上下文，从而提供精准的响应。

  ```
  [Comment on specific lines in Files tab]
  /oc add error handling here
  ```

  当你对特定代码行发表评论时，OpenCode 会接收到：
  - 正在审查的具体文件
  - 特定的代码行
  - 周围的 diff 上下文
  - 行号信息

  这样你就可以提出更有针对性的请求，而无需手动指定文件路径或行号。

---

## gitlab

- 官方原文：https://opencode.ai/docs/zh-cn/gitlab
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-gitlab.md`

OpenCode 通过 GitLab CI/CD 流水线或 GitLab Duo 与你的 GitLab 工作流集成。

在这两种情况下，OpenCode 都将在你的 GitLab Runner 上运行。

---

## GitLab CI

OpenCode 可以在常规的 GitLab 流水线中运行。你可以将其作为 [CI 组件](https://docs.gitlab.com/ee/ci/components/) 集成到流水线中。

这里我们使用的是社区创建的 OpenCode CI/CD 组件 — [nagyv/gitlab-opencode](https://gitlab.com/nagyv/gitlab-opencode)。

---

### 功能特性

- **按任务自定义配置**：使用自定义配置目录来配置 OpenCode，例如 `./config/#custom-directory`，以便为每次 OpenCode 调用启用或禁用特定功能。
- **最小化配置**：CI 组件会在后台完成 OpenCode 的设置，你只需创建 OpenCode 配置和初始提示词即可。
- **灵活可定制**：CI 组件支持多种输入参数来自定义其行为。

---

### 设置

1. 将你的 OpenCode 身份验证 JSON 作为文件类型的 CI 环境变量存储在 **Settings** > **CI/CD** > **Variables** 下。请确保将其标记为 "Masked and hidden"。
2. 将以下内容添加到你的 `.gitlab-ci.yml` 文件中。

   ```yaml title=".gitlab-ci.yml"
   include:
     - component: $CI_SERVER_FQDN/nagyv/gitlab-opencode/opencode@2
       inputs:
         config_dir: ${CI_PROJECT_DIR}/opencode-config
         auth_json: $OPENCODE_AUTH_JSON # The variable name for your OpenCode authentication JSON
         command: optional-custom-command
         message: "Your prompt here"
   ```

有关更多输入参数和使用场景，请[查看该组件的文档](https://gitlab.com/explore/catalog/nagyv/gitlab-opencode)。

---

## GitLab Duo

OpenCode 与你的 GitLab 工作流集成。
在评论中提及 `@opencode`，OpenCode 将在你的 GitLab CI 流水线中执行任务。

---

### 功能特性

- **问题分类**：让 OpenCode 调查某个 issue 并为你解释。
- **修复与实现**：让 OpenCode 修复 issue 或实现某个功能。它会创建一个新分支，并提交包含更改的合并请求。
- **安全可靠**：OpenCode 在你的 GitLab Runner 上运行。

---

### 设置

OpenCode 在你的 GitLab CI/CD 流水线中运行，以下是设置所需的步骤：

:::tip
请查看 [**GitLab 文档**](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/) 获取最新说明。

1.  配置你的 GitLab 环境
2.  设置 CI/CD
3.  获取 AI 模型提供商的 API 密钥
4.  创建服务账户
5.  配置 CI/CD 变量
6.  创建流程配置文件，以下是一个示例：

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

详细说明请参考 [GitLab CLI agents 文档](https://docs.gitlab.com/user/duo_agent_platform/agent_assistant/)。

---

### 示例

以下是在 GitLab 中使用 OpenCode 的一些示例。

:::tip
你可以配置使用不同于 `@opencode` 的触发词。

- **解释 issue**

  在 GitLab issue 中添加以下评论。

  ```
  @opencode explain this issue
  ```

  OpenCode 会阅读该 issue 并回复清晰的解释。

- **修复 issue**

  在 GitLab issue 中输入：

  ```
  @opencode fix this
  ```

  OpenCode 会创建一个新分支，实现更改，并提交包含更改的合并请求。

- **审查合并请求**

  在 GitLab 合并请求中留下以下评论。

  ```
  @opencode review this merge request
  ```

  OpenCode 会审查合并请求并提供反馈。

---

## go

- 官方原文：https://opencode.ai/docs/zh-cn/go
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-go.md`

export const console = config.console
export const email = `mailto:${config.email}`

OpenCode Go 是一项**每月 10 美元的低成本订阅服务**，让你能够稳定地访问流行的开源编程模型。

Go 的工作方式与 OpenCode 中的任何其他提供商（provider）一样。订阅 OpenCode Go 后你将获得 API 密钥。它是 **完全可选** 的，并非使用 OpenCode 所必需的条件。

它主要面向国际用户，并提供稳定的全球访问。

---

## 背景

开源模型现在变得非常强大。在编程任务中，它们的性能已接近专有模型。由于许多提供商都可以提供具有竞争力的服务，它们通常要便宜得多。

然而，获得可靠、低延迟的访问可能很困难。各提供商在质量和可用性方面参差不齐。

:::tip
我们测试了一组经过精选且与 OpenCode 配合良好的模型和提供商。

为了解决这个问题，我们做了以下几件事：

1. 我们测试了一组精选的开源模型，并与他们的团队探讨了如何以最佳方式运行它们。
2. 随后我们与一些提供商合作，以确保正确提供这些服务。
3. 最后，我们对模型和提供商的组合进行了基准测试（benchmark），得出了一份我们乐于推荐的列表。

OpenCode Go 让你能够以**每月 10 美元**的价格访问这些模型。

---

## 工作原理

OpenCode Go 的工作方式与 OpenCode 中的其他提供商一样。

1. 登录 **<a href={console}>OpenCode Zen</a>**，订阅 Go，然后复制你的 API 密钥。
2. 在 TUI 中运行 `/connect` 命令，选择 `OpenCode Go`，然后粘贴你的 API 密钥。
3. 在 TUI 中运行 `/models` 以查看通过 Go 可用的模型列表。

:::note
每个工作空间只能有一名成员订阅 OpenCode Go。

当前支持的模型列表包括：

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
- **Muse Spark 1.3 Contributor** ([仅限部分地区](https://ai.developer.meta.com/legal/geographic-use-policy))
- **Muse Spark 1.2 Contributor** ([仅限部分地区](https://ai.developer.meta.com/legal/geographic-use-policy))
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

随着我们进行测试和添加新模型，该列表可能会发生变化。

---

## 可以在哪里使用？

OpenCode Go 适用于 [OpenCode](https://opencode.ai) 以及其他会产生类似请求的编程 Agent。

我们会监控流量，以识别影响其他用户体验的滥用行为。

你的客户端应当：

1. 发送典型的编程 Agent 流量。
2. 使用自身专属的 user agent 标识（例如 `my-coding-agent/1.0`），而不是通用的 SDK 或 HTTP 库名称。
3. 为每段对话在 `x-opencode-session` 请求头中发送稳定的会话 ID，以便我们优化路由和提示词缓存。

### 已验证的客户端

除 OpenCode 外，以下客户端已通过验证，能够正常使用 OpenCode Go。但我们无法保证它们未来仍能正常使用。

| 客户端            | 会话支持                                                                                                                                                                                                                    |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hermes**        | 包含 [PR #101864](https://github.com/NousResearch/hermes-agent/pull/101864) 的构建版本会在主要和辅助 OpenCode 请求中发送该请求头。此修复在 v0.21.0 发布后才合并，因此 v0.21.0 本身并不包含该修复。                          |
| **Claude Code**   | Go 能识别其原生会话请求头，无需额外封装来添加自定义请求头。                                                                                                                                                                 |
| **Codex**         | Go 能识别其原生会话请求头。某些版本和代理配置仍会遗漏该请求头；转发请求时请保留会话请求头。                                                                                                                                 |
| **ZCode**         | Go 能识别其原生会话请求头。我们[请求支持 `x-opencode-session` 的 issue](https://github.com/zai-org/feedback/issues/492) 仍处于开放状态，但已不再需要发送这一特定请求头。                                                    |
| **Pi**            | 当前构建版本会为 OpenCode 发送会话信息。请更新旧版安装。                                                                                                                                                                    |
| **jcode**         | 请更新至 **v0.81.6 或更高版本**，其中包含[会话请求头修复](https://github.com/1jehuang/jcode/issues/1167)。                                                                                                                  |
| **Kilo Code CLI** | 包含 [PR #13752](https://github.com/Kilo-Org/kilocode/pull/13752) 的构建版本恢复了 OpenCode 会话请求头。此修复仅适用于 CLI，不适用于 VS Code 扩展。参见 [issue #13723](https://github.com/Kilo-Org/kilocode/issues/13723)。 |

### 已知存在问题的客户端

在我们调查的版本中，以下客户端缺少会话支持，或支持不完整。相关报告链接可用于跟踪修复进展和临时解决方案。

| 客户端                  | 状态与跟踪                                                                                                                                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DeepSeek Harness**    | 某些模型调用路径会传递会话信息，但其他路径中缺失。我们能识别其原生请求头；剩余工作是在所有适配器中发送该请求头。参见[讨论 #5495](https://github.com/deepseek-ai/deepseek-harness/discussions/5495)。 |
| **GitHub Copilot Chat** | [VS Code issue #334186](https://github.com/microsoft/vscode/issues/334186) 已提出自动发送会话请求头的支持请求。                                                                                      |
| **Kimi Code**           | [issue #3506](https://github.com/MoonshotAI/kimi-code/issues/3506) 已提出自动发送会话请求头的支持请求。                                                                                              |
| **MiMo Code**           | [Issue #2317](https://github.com/XiaomiMiMo/MiMo-Code/issues/2317) 已有拟议修复 [PR #2327](https://github.com/XiaomiMiMo/MiMo-Code/pull/2327)，但尚未合并。                                          |

## 使用限制

使用限制以每月美元金额定义。下表列出了每个模型的每月限制和 token 成本。

每个模型都有以下使用限制：5 小时 — 每月限制的 20%；每周 — 50%；每月 — 100%。

例如，如果某个模型的每月限制为 $60，你最多可以使用：

- **5 小时限制** — $12 的使用额度
- **每周限制** — $30 的使用额度
- **每月限制** — $60 的使用额度

Token 价格按每 1M tokens 列示。

| 模型                                    | 输入   | 输出   | 缓存读取  | 缓存写入 | 每月限制                                                |
| --------------------------------------- | ------ | ------ | --------- | -------- | ------------------------------------------------------- |
| GLM-5.3-Flash                           | $0.15  | $0.50  | $0.03     | -        | **$60**                                                 |
| GLM-5.3                                 | $1.40  | $4.40  | $0.26     | -        | **$15**                                                 |
| GLM-5.2                                 | $1.40  | $4.40  | $0.26     | -        | **$60**                                                 |
| GLM-5.1                                 | $1.40  | $4.40  | $0.26     | -        | **$60**                                                 |
| Kimi K3                                 | $3.00  | $15.00 | $0.30     | -        | **$15**                                                 |
| Kimi K2.7 Code                          | $0.95  | $4.00  | $0.19     | -        | **$60**                                                 |
| Kimi K2.6                               | $0.95  | $4.00  | $0.16     | -        | **$60**                                                 |
| LongCat-2.0                             | $0.30  | $1.20  | $0.006    | -        | **$60**                                                 |
| MiMo-V2.6-Flash                         | $0.14  | $0.28  | $0.0028   | -        | **$60**                                                 |
| MiMo-V2.6-Pro                           | $0.435 | $0.87  | $0.003625 | -        | **$15**                                                 |
| MiMo-V2.5                               | $0.14  | $0.28  | $0.0028   | -        | **$60**                                                 |
| MiMo-V2.5-Pro                           | $0.435 | $0.87  | $0.003625 | -        | **$15**                                                 |
| MiniMax M3                              | $0.30  | $1.20  | $0.06     | -        | **$60**                                                 |
| MiniMax M2.7                            | $0.30  | $1.20  | $0.06     | $0.375   | **$60**                                                 |
| MiniMax M2.5                            | $0.30  | $1.20  | $0.06     | $0.375   | **$60**                                                 |
| Muse Spark 1.3 Contributor              | $0.10  | $0.20  | $0.002    | -        | **$60**                                                 |
| Muse Spark 1.2 Contributor              | $0.10  | $0.20  | $0.002    | -        | **$60**                                                 |
| Qwen3.8 Max                             | $2.00  | $6.00  | $0.25     | $2.50    | **$15**                                                 |
| Qwen3.8 Flash                           | $0.15  | $0.47  | $0.016    | $0.20    | **$30**                                                 |
| Qwen3.7 Max                             | $2.50  | $7.50  | $0.50     | $3.125   | **$30**                                                 |
| Qwen3.7 Plus (≤ 256K tokens)            | $0.40  | $1.60  | $0.04     | $0.50    | **$60**                                                 |
| Qwen3.7 Plus (> 256K tokens)            | $1.20  | $4.80  | $0.12     | $1.50    | **$60**                                                 |
| Qwen3.6 Plus (≤ 256K tokens)            | $0.50  | $3.00  | $0.05     | $0.625   | **$60**                                                 |
| Qwen3.6 Plus (> 256K tokens)            | $2.00  | $6.00  | $0.20     | $2.50    | **$60**                                                 |
| DeepSeek V4.1 Flash (Off-Peak)          | $0.15  | $0.60  | $0.003    | -        | ~~$15~~ **$60**<br /><small>4x · 9 月 27 日结束</small> |
| DeepSeek V4.1 Flash (Peak)              | $0.30  | $1.20  | $0.006    | -        | ~~$15~~ **$60**<br /><small>4x · 9 月 27 日结束</small> |
| DeepSeek V4 Pro (Off-Peak)              | $0.66  | $1.98  | $0.022    | -        | **$15**                                                 |
| DeepSeek V4 Pro (Peak)                  | $1.32  | $3.96  | $0.044    | -        | **$15**                                                 |
| DeepSeek V4 Flash (Off-Peak)            | $0.15  | $0.60  | $0.003    | -        | **$30**                                                 |
| DeepSeek V4 Flash (Peak)                | $0.30  | $1.20  | $0.006    | -        | **$30**                                                 |
| DeepSeek V4 Flash Vision Exp (Off-Peak) | $0.15  | $0.60  | $0.003    | -        | **$15**                                                 |
| DeepSeek V4 Flash Vision Exp (Peak)     | $0.30  | $1.20  | $0.006    | -        | **$15**                                                 |
| Hy4 preview                             | $0.834 | $2.501 | $0.042    | -        | **$30**                                                 |
| Hy3                                     | $0.14  | $0.58  | $0.035    | -        | **$60**                                                 |
| Grok 4.7 (≤ 200K tokens)                | $2.00  | $6.00  | $0.50     | -        | **$15**                                                 |
| Grok 4.7 (> 200K tokens)                | $4.00  | $12.00 | $1.00     | -        | **$15**                                                 |
| Grok 4.6 (≤ 200K tokens)                | $2.00  | $6.00  | $0.50     | -        | **$15**                                                 |
| Grok 4.6 (> 200K tokens)                | $4.00  | $12.00 | $1.00     | -        | **$15**                                                 |
| GPT 5.6 Luna (≤ 272K tokens)            | $0.20  | $1.20  | $0.02     | $0.25    | **$15**                                                 |
| GPT 5.6 Luna (> 272K tokens)            | $0.40  | $1.80  | $0.04     | $0.50    | **$15**                                                 |

**DeepSeek V4.1 Flash / V4 Pro / V4 Flash / V4 Flash Vision Exp:** Peak 时段为周一至周五的 01:00-04:00 和 06:00-10:00 UTC；其他所有时段（包括周末）均为 Off-Peak。[了解更多](https://api-docs.deepseek.com/quick_start/pricing/)。

**DeepSeek V4 Flash Vision Exp:** 图片会根据尺寸转换为 token，并与文本 token 一起按输入 token 计费。 [了解更多](https://api-docs.deepseek.com/quick_start/pricing/)。

### 预估请求数

下表根据典型的 Go 使用模式提供了预估请求数：

| Model                                                       | 每 5 小时请求数           | 每周请求数                 | 每月请求数                  |
| ----------------------------------------------------------- | ------------------------- | -------------------------- | --------------------------- |
| GLM-5.3-Flash                                               | 6,320                     | 15,790                     | 31,580                      |
| GLM-5.3                                                     | 220                       | 540                        | 1,080                       |
| GLM-5.2                                                     | 880                       | 2,150                      | 4,300                       |
| GLM-5.1                                                     | 880                       | 2,150                      | 4,300                       |
| Kimi K3                                                     | 110                       | 250                        | 490                         |
| Kimi K2.7 Code                                              | 1,350                     | 3,380                      | 6,750                       |
| Kimi K2.6                                                   | 1,150                     | 2,880                      | 5,750                       |
| LongCat-2.0                                                 | 11,400                    | 28,600                     | 57,200                      |
| MiMo-V2.6-Flash                                             | 30,100                    | 75,200                     | 150,400                     |
| MiMo-V2.6-Pro                                               | 3,250                     | 8,150                      | 16,300                      |
| MiMo-V2.5                                                   | 30,100                    | 75,200                     | 150,400                     |
| MiMo-V2.5-Pro                                               | 3,250                     | 8,150                      | 16,300                      |
| MiniMax M3                                                  | 3,200                     | 8,000                      | 16,000                      |
| MiniMax M2.7                                                | 3,400                     | 8,500                      | 17,000                      |
| Muse Spark 1.3 Contributor                                  | 45,300                    | 113,300                    | 226,600                     |
| Muse Spark 1.2 Contributor                                  | 45,300                    | 113,300                    | 226,600                     |
| Qwen3.8 Max                                                 | 160                       | 400                        | 810                         |
| Qwen3.8 Flash                                               | 5,400                     | 13,500                     | 27,000                      |
| Qwen3.7 Max                                                 | 170                       | 420                        | 840                         |
| Qwen3.7 Plus                                                | 4,300                     | 10,800                     | 21,600                      |
| Qwen3.6 Plus                                                | 3,300                     | 8,200                      | 16,300                      |
| DeepSeek V4.1 Flash<br /><small>4x · 9 月 27 日结束</small> | ~~6,500~~<br />**26,000** | ~~16,250~~<br />**65,000** | ~~32,500~~<br />**130,000** |
| DeepSeek V4 Pro                                             | 1,050                     | 2,600                      | 5,200                       |
| DeepSeek V4 Flash                                           | 13,000                    | 32,500                     | 65,000                      |
| DeepSeek V4 Flash Vision Exp                                | 6,500                     | 16,250                     | 32,500                      |
| Hy4 preview                                                 | 1,350                     | 3,380                      | 6,770                       |
| Hy3                                                         | 4,300                     | 10,750                     | 21,500                      |
| Grok 4.7                                                    | 169                       | 423                        | 845                         |
| Grok 4.6                                                    | 169                       | 423                        | 845                         |
| GPT 5.6 Luna                                                | 2,050                     | 5,100                      | 10,250                      |

预估值采用以下每次请求的 token 数量；实际使用情况会有所不同。

- Grok 4.7/4.6 — 每次请求 390 个输入 token，32,500 个缓存 token，120 个输出 token
- GLM-5.3-Flash — 每次请求 1,000 个输入 token，55,000 个缓存 token，200 个输出 token
- GLM-5.3/5.2/5.1 — 每次请求 700 个输入 token，52,000 个缓存 token，150 个输出 token
- GPT 5.6 Luna — 每次请求 1,000 个输入 token，50,000 个缓存 token，220 个输出 token
- Kimi K3 — 每次请求 1,050 个输入 token，76,500 个缓存 token，300 个输出 token
- Kimi K2.7/K2.6 — 每次请求 870 个输入 token，55,000 个缓存 token，200 个输出 token
- LongCat-2.0 — 每次请求 920 个输入 token，88,900 个缓存 token，200 个输出 token
- DeepSeek V4.1 Flash — 每次请求 410 个输入 token，71,300 个缓存 token，310 个输出 token
- DeepSeek V4 Pro — 每次请求 750 个输入 token，82,000 个缓存 token，290 个输出 token
- DeepSeek V4 Flash — 每次请求 410 个输入 token，71,300 个缓存 token，310 个输出 token
- DeepSeek V4 Flash Vision Exp — 每次请求 410 个输入 token，71,300 个缓存 token，310 个输出 token
- MiMo-V2.6-Flash — 每次请求 830 个输入 token，71,500 个缓存 token，295 个输出 token
- MiMo-V2.6-Pro — 每次请求 790 个输入 token，86,000 个缓存 token，305 个输出 token
- MiMo-V2.5 — 每次请求 830 个输入 token，71,500 个缓存 token，295 个输出 token
- MiMo-V2.5-Pro — 每次请求 790 个输入 token，86,000 个缓存 token，305 个输出 token
- MiniMax M3 — 每次请求 510 个输入 token，56,000 个缓存 token，190 个输出 token
- MiniMax M2.7 — 每次请求 300 个输入 token，55,000 个缓存 token，125 个输出 token
- Muse Spark 1.3 Contributor — 每次请求 620 个输入 token，71,400 个缓存 token，300 个输出 token
- Muse Spark 1.2 Contributor — 每次请求 620 个输入 token，71,400 个缓存 token，300 个输出 token
- Qwen3.8 Max — 每次请求 420 个输入 token，66,000 个缓存 token，200 个输出 token
- Qwen3.8 Flash — 每次请求 600 个输入 token，58,000 个缓存 token，200 个输出 token
- Qwen3.7 Max — 每次请求 420 个输入 token，66,000 个缓存 token，200 个输出 token
- Qwen3.7 Plus — 每次请求 500 个输入 token，57,000 个缓存 token，190 个输出 token
- Qwen3.6 Plus — 每次请求 500 个输入 token，57,000 个缓存 token，190 个输出 token
- Hy4 preview — 每次请求 830 个输入 token，71,500 个缓存 token，295 个输出 token
- Hy3 — 每次请求 830 个输入 token，71,500 个缓存 token，295 个输出 token

你可以在 **<a href={console}>控制台</a>** 中跟踪你当前的使用情况。

:::tip
如果你达到了使用限制，你可以继续使用免费模型。

使用限制可能会随着我们从早期使用和反馈中学习而发生变化。

---

### 超出限制的使用

如果你的 Zen 余额中还有积分，可以在控制台中启用 **使用余额（Use balance）** 选项。启用后，当你达到使用限制时，Go 会回退使用你的 Zen 余额，而不是拦截请求。

---

### 为什么某些模型的使用额度较低

使用 Go 时，你每月支付 $10，包含的每月使用额度因模型而异。

对于大多数模型，我们通过批量折扣和预留 GPU 容量来实现这一目标。然后，我们通过提高每月使用额度，将节省的成本回馈给你。

对于某些模型，我们还没有机会协商折扣或以更低的成本托管它们，这可能是因为模型较新，或者其公开价格已经是折扣价。

对于这些模型，你获得的使用额度仍会略高于直接向模型提供商付费；这就是它们包含的每月使用额度较低的原因。

---

## API 端点

你也可以通过以下 API 端点访问 Go 模型。

| 模型                         | 模型 ID                      | 端点                                             | AI SDK 包                   |
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

你的 OpenCode 配置中的 [模型 ID](/docs/config/#models) 使用 `opencode-go/<model-id>` 格式。例如，对于 Kimi K3，你将在配置中使用 `opencode-go/kimi-k3`。

---

### 模型

你可以从以下地址获取可用模型及其元数据的完整列表：

```
https://opencode.ai/zen/go/v1/models
```

---

## 隐私保护

| 模型                         | 模型训练 | 数据留存 |
| ---------------------------- | -------- | -------- |
| Grok 4.7                     | 不使用   | 30 天    |
| Grok 4.6                     | 不使用   | 30 天    |
| GPT 5.6 Luna                 | 不使用   | 30 天    |
| GLM-5.3-Flash                | 不使用   | 0 天     |
| GLM-5.3                      | 不使用   | 0 天     |
| GLM-5.2                      | 不使用   | 0 天     |
| GLM-5.1                      | 不使用   | 0 天     |
| Kimi K3                      | 不使用   | 0 天     |
| Kimi K2.7 Code               | 不使用   | 0 天     |
| Kimi K2.6                    | 不使用   | 0 天     |
| LongCat-2.0                  | 不使用   | 0 天     |
| MiMo-V2.6-Pro                | 不使用   | 0 天     |
| MiMo-V2.6-Flash              | 不使用   | 0 天     |
| MiMo-V2.5-Pro                | 不使用   | 0 天     |
| MiMo-V2.5                    | 不使用   | 0 天     |
| Qwen3.8 Max                  | 不使用   | 0 天     |
| Qwen3.8 Flash                | 不使用   | 0 天     |
| Qwen3.7 Max                  | 不使用   | 0 天     |
| Qwen3.7 Plus                 | 不使用   | 0 天     |
| Qwen3.6 Plus                 | 不使用   | 0 天     |
| MiniMax M3                   | 不使用   | 0 天     |
| MiniMax M2.7                 | 不使用   | 0 天     |
| Muse Spark 1.3 Contributor   | 是       | 非 ZDR   |
| Muse Spark 1.2 Contributor   | 是       | 非 ZDR   |
| DeepSeek V4.1 Flash          | 不使用   | 0 天     |
| DeepSeek V4 Pro              | 不使用   | 0 天     |
| DeepSeek V4 Flash            | 不使用   | 0 天     |
| DeepSeek V4 Flash Vision Exp | 不使用   | 0 天     |
| Hy4 preview                  | 不使用   | 0 天     |
| Hy3                          | 不使用   | 0 天     |

- **Grok 4.7/4.6:** ZDR 会禁用依赖所存储数据的重要 API 功能，包括有状态的 Responses API、Files and Collections 和 Batch API。[了解更多](https://docs.x.ai/developers/faq/security#what-is-zero-data-retention-zdr)。
- **GPT 5.6 Luna:** 所有 API 功能的使用都会生成滥用监控日志，并最多保留 30 天。[了解更多](https://developers.openai.com/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring)。
- **Muse Spark 1.3 Contributor:** 以允许使用你的提示词和补全结果训练未来的 Meta 模型为交换，token 价格可获得大幅折扣。仅在 Meta 的[地理使用政策](https://ai.developer.meta.com/legal/geographic-use-policy)允许的地区提供。[了解更多](https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier)。
- **Muse Spark 1.2 Contributor:** 以允许使用你的提示词和补全结果训练未来的 Meta 模型为交换，token 价格可获得大幅折扣。仅在 Meta 的[地理使用政策](https://ai.developer.meta.com/legal/geographic-use-policy)允许的地区提供。[了解更多](https://dev.meta.ai/docs/pricing-rate-limits#contributor-tier)。
- **DeepSeek:** ZDR 协议每月续签。当前协议有效期至 2026 年 9 月 30 日。

---

## 目标

我们创建 OpenCode Go 的目的是：

1. 通过低成本订阅让更多人能够 **无门槛地** 使用 AI 编程。
2. 为最佳开源编程模型提供 **可靠的** 访问。
3. 精选经过 **测试和基准评估**，适合编程 Agent 使用的模型。
4. **无锁定（no lock-in）**，允许你与 OpenCode 一起使用任何其他提供商。

---

## ide

- 官方原文：https://opencode.ai/docs/zh-cn/ide
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-ide.md`

OpenCode 可与 VS Code、Cursor 或任何支持终端的 IDE 集成。只需在终端中运行 `opencode` 即可开始使用。

---

## 用法

- **快速启动**：使用 `Cmd+Esc`（Mac）或 `Ctrl+Esc`（Windows/Linux）在分屏终端视图中打开 OpenCode，如果已有终端会话正在运行，则会自动聚焦到该会话。
- **新建会话**：使用 `Cmd+Shift+Esc`（Mac）或 `Ctrl+Shift+Esc`（Windows/Linux）启动新的 OpenCode 终端会话，即使已有会话在运行也会新建。你也可以点击界面中的 OpenCode 按钮。
- **上下文感知**：自动将当前选中内容或标签页共享给 OpenCode。
- **文件引用快捷键**：使用 `Cmd+Option+K`（Mac）或 `Alt+Ctrl+K`（Linux/Windows）插入文件引用。例如 `@File#L37-42`。

---

## 安装

在 VS Code 及其常见分支（如 Cursor、Windsurf、VSCodium）上安装 OpenCode：

1. 打开 VS Code
2. 打开集成终端
3. 运行 `opencode`——扩展将自动安装

如果你希望在 TUI 中执行 `/editor` 或 `/export` 时使用自己的 IDE，需要设置 `export EDITOR="code --wait"`。[了解更多](/docs/tui/#editor-setup)。

---

### 手动安装

在扩展商店中搜索 **OpenCode**，然后点击 **Install**。

---

### 故障排除

如果扩展未能自动安装：

- 确保你是在集成终端中运行的 `opencode`。
- 确认你的 IDE 对应的 CLI 命令已安装：
  - VS Code：`code` 命令
  - Cursor：`cursor` 命令
  - Windsurf：`windsurf` 命令
  - VSCodium：`codium` 命令
  - 如果未安装，请按 `Cmd+Shift+P`（Mac）或 `Ctrl+Shift+P`（Windows/Linux），搜索 "Shell Command: Install 'code' command in PATH"（或你的 IDE 对应的命令）
- 确保 VS Code 有权限安装扩展

---

## sdk

- 官方原文：https://opencode.ai/docs/zh-cn/sdk
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-sdk.md`

export const typesUrl = `${config.github}/blob/dev/packages/sdk/js/src/gen/types.gen.ts`

opencode JS/TS SDK 提供了一个类型安全的客户端，用于与服务器进行交互。
你可以用它来构建集成方案，并以编程方式控制 opencode。

[了解更多](/docs/server)关于服务器的工作原理。如需示例，请查看社区构建的[项目](/docs/ecosystem#projects)。

---

## 安装

从 npm 安装 SDK：

```bash
npm install @opencode-ai/sdk
```

---

## 创建客户端

创建一个 opencode 实例：

```javascript

const { client } = await createOpencode()
```

这会同时启动服务器和客户端。

#### 选项

| 选项       | 类型          | 描述                       | 默认值      |
| ---------- | ------------- | -------------------------- | ----------- |
| `hostname` | `string`      | 服务器主机名               | `127.0.0.1` |
| `port`     | `number`      | 服务器端口                 | `4096`      |
| `signal`   | `AbortSignal` | 用于取消操作的中止信号     | `undefined` |
| `timeout`  | `number`      | 服务器启动超时时间（毫秒） | `5000`      |
| `config`   | `Config`      | 配置对象                   | `{}`        |

---

## 配置

你可以传入一个配置对象来自定义行为。实例仍然会读取你的 `opencode.json`，但你可以通过内联方式覆盖或添加配置：

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

## 仅客户端模式

如果你已经有一个正在运行的 opencode 实例，可以创建一个客户端实例来连接它：

```javascript

const client = createOpencodeClient({
  baseUrl: "http://localhost:4096",
})
```

#### 选项

| 选项            | 类型       | 描述                         | 默认值                  |
| --------------- | ---------- | ---------------------------- | ----------------------- |
| `baseUrl`       | `string`   | 服务器 URL                   | `http://localhost:4096` |
| `fetch`         | `function` | 自定义 fetch 实现            | `globalThis.fetch`      |
| `parseAs`       | `string`   | 响应解析方式                 | `auto`                  |
| `responseStyle` | `string`   | 返回风格：`data` 或 `fields` | `fields`                |
| `throwOnError`  | `boolean`  | 抛出错误而非返回错误         | `false`                 |

---

## 类型

SDK 包含所有 API 类型的 TypeScript 定义。你可以直接导入它们：

```typescript
```

所有类型均根据服务器的 OpenAPI 规范生成，可在<a href={typesUrl}>类型文件</a>中查看。

---

## 错误处理

SDK 可能会抛出错误，你可以捕获并处理这些错误：

```typescript
try {
  await client.session.get({ path: { id: "invalid-id" } })
} catch (error) {
  console.error("Failed to get session:", (error as Error).message)
}
```

---

## 结构化输出

你可以通过指定带有 JSON Schema 的 `format` 来请求模型返回结构化的 JSON 输出。模型会使用 `StructuredOutput` 工具返回符合你 Schema 的经过验证的 JSON。

### 基本用法

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

### 输出格式类型

| 类型          | 描述                                    |
| ------------- | --------------------------------------- |
| `text`        | 默认值。标准文本响应（无结构化输出）    |
| `json_schema` | 返回符合所提供 Schema 的经过验证的 JSON |

### JSON Schema 格式

使用 `type: 'json_schema'` 时，需提供以下字段：

| 字段         | 类型            | 描述                                  |
| ------------ | --------------- | ------------------------------------- |
| `type`       | `'json_schema'` | 必填。指定 JSON Schema 模式           |
| `schema`     | `object`        | 必填。定义输出结构的 JSON Schema 对象 |
| `retryCount` | `number`        | 可选。验证重试次数（默认值：2）       |

### 错误处理

如果模型在所有重试后仍无法生成有效的结构化输出，响应中会包含 `StructuredOutputError`：

```typescript
if (result.data.info.error?.name === "StructuredOutputError") {
  console.error("Failed to produce structured output:", result.data.info.error.message)
  console.error("Attempts:", result.data.info.error.retries)
}
```

### 最佳实践

1. **在 Schema 属性中提供清晰的描述**，帮助模型理解需要提取的数据
2. **使用 `required`** 指定哪些字段必须存在
3. **保持 Schema 简洁** — 复杂的嵌套 Schema 可能会让模型更难正确填充
4. **设置合适的 `retryCount`** — 对于复杂 Schema 可增加重试次数，对于简单 Schema 可减少

---

## API

SDK 通过类型安全的客户端暴露所有服务器 API。

---

### Global

| 方法              | 描述                     | 响应                                 |
| ----------------- | ------------------------ | ------------------------------------ |
| `global.health()` | 检查服务器健康状态和版本 | `{ healthy: true, version: string }` |

---

#### 示例

```javascript
const health = await client.global.health()
console.log(health.data.version)
```

---

### App

| 方法           | 描述               | 响应                                        |
| -------------- | ------------------ | ------------------------------------------- |
| `app.log()`    | 写入一条日志       | `boolean`                                   |
| `app.agents()` | 列出所有可用的代理 | <a href={typesUrl}><code>Agent[]</code></a> |

---

#### 示例

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

| 方法                | 描述         | 响应                                          |
| ------------------- | ------------ | --------------------------------------------- |
| `project.list()`    | 列出所有项目 | <a href={typesUrl}><code>Project[]</code></a> |
| `project.current()` | 获取当前项目 | <a href={typesUrl}><code>Project</code></a>   |

---

#### 示例

```javascript
// List all projects
const projects = await client.project.list()

// Get current project
const currentProject = await client.project.current()
```

---

### Path

| 方法         | 描述         | 响应                                     |
| ------------ | ------------ | ---------------------------------------- |
| `path.get()` | 获取当前路径 | <a href={typesUrl}><code>Path</code></a> |

---

#### 示例

```javascript
// Get current path information
const pathInfo = await client.path.get()
```

---

### Config

| 方法                 | 描述                 | 响应                                                                                                  |
| -------------------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| `config.get()`       | 获取配置信息         | <a href={typesUrl}><code>Config</code></a>                                                            |
| `config.providers()` | 列出提供商和默认模型 | `{ providers: `<a href={typesUrl}><code>Provider[]</code></a>`, default: { [key: string]: string } }` |

---

#### 示例

```javascript
const config = await client.config.get()

const { providers, default: defaults } = await client.config.providers()
```

---

### Sessions

| 方法                                                       | 描述                       | 备注                                                                                                                                                                                           |
| ---------------------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `session.list()`                                           | 列出会话                   | 返回 <a href={typesUrl}><code>Session[]</code></a>                                                                                                                                             |
| `session.get({ path })`                                    | 获取会话                   | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `session.children({ path })`                               | 列出子会话                 | 返回 <a href={typesUrl}><code>Session[]</code></a>                                                                                                                                             |
| `session.create({ body })`                                 | 创建会话                   | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `session.delete({ path })`                                 | 删除会话                   | 返回 `boolean`                                                                                                                                                                                 |
| `session.update({ path, body })`                           | 更新会话属性               | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `session.init({ path, body })`                             | 分析应用并创建 `AGENTS.md` | 返回 `boolean`                                                                                                                                                                                 |
| `session.abort({ path })`                                  | 中止正在运行的会话         | 返回 `boolean`                                                                                                                                                                                 |
| `session.share({ path })`                                  | 分享会话                   | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `session.unshare({ path })`                                | 取消分享会话               | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `session.summarize({ path, body })`                        | 总结会话                   | 返回 `boolean`                                                                                                                                                                                 |
| `session.messages({ path })`                               | 列出会话中的消息           | 返回 `{ info: `<a href={typesUrl}><code>Message</code></a>`, parts: `<a href={typesUrl}><code>Part[]</code></a>`}[]`                                                                           |
| `session.message({ path })`                                | 获取消息详情               | 返回 `{ info: `<a href={typesUrl}><code>Message</code></a>`, parts: `<a href={typesUrl}><code>Part[]</code></a>`}`                                                                             |
| `session.prompt({ path, body })`                           | 发送提示词消息             | `body.noReply: true` 返回 UserMessage（仅注入上下文）。默认返回带有 AI 响应的 <a href={typesUrl}><code>AssistantMessage</code></a>。支持通过 `body.outputFormat` 使用[结构化输出](#结构化输出) |
| `session.command({ path, body })`                          | 向会话发送命令             | 返回 `{ info: `<a href={typesUrl}><code>AssistantMessage</code></a>`, parts: `<a href={typesUrl}><code>Part[]</code></a>`}`                                                                    |
| `session.shell({ path, body })`                            | 执行 shell 命令            | 返回 <a href={typesUrl}><code>AssistantMessage</code></a>                                                                                                                                      |
| `session.revert({ path, body })`                           | 撤回消息                   | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `session.unrevert({ path })`                               | 恢复已撤回的消息           | 返回 <a href={typesUrl}><code>Session</code></a>                                                                                                                                               |
| `postSessionByIdPermissionsByPermissionId({ path, body })` | 响应权限请求               | 返回 `boolean`                                                                                                                                                                                 |

---

#### 示例

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

| 方法                      | 描述                 | 响应                                                                                |
| ------------------------- | -------------------- | ----------------------------------------------------------------------------------- |
| `find.text({ query })`    | 搜索文件中的文本     | 包含 `path`、`lines`、`line_number`、`absolute_offset`、`submatches` 的匹配对象数组 |
| `find.files({ query })`   | 按名称查找文件和目录 | `string[]`（路径）                                                                  |
| `find.symbols({ query })` | 查找工作区符号       | <a href={typesUrl}><code>Symbol[]</code></a>                                        |
| `file.read({ query })`    | 读取文件             | `{ type: "raw" \| "patch", content: string }`                                       |
| `file.status({ query? })` | 获取已跟踪文件的状态 | <a href={typesUrl}><code>File[]</code></a>                                          |

`find.files` 支持以下可选查询字段：

- `type`：`"file"` 或 `"directory"`
- `directory`：覆盖搜索的项目根目录
- `limit`：最大结果数（1–200）

---

#### 示例

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

| 方法                           | 描述             | 响应      |
| ------------------------------ | ---------------- | --------- |
| `tui.appendPrompt({ body })`   | 向提示词追加文本 | `boolean` |
| `tui.openHelp()`               | 打开帮助对话框   | `boolean` |
| `tui.openSessions()`           | 打开会话选择器   | `boolean` |
| `tui.openThemes()`             | 打开主题选择器   | `boolean` |
| `tui.openModels()`             | 打开模型选择器   | `boolean` |
| `tui.submitPrompt()`           | 提交当前提示词   | `boolean` |
| `tui.clearPrompt()`            | 清除提示词       | `boolean` |
| `tui.executeCommand({ body })` | 执行命令         | `boolean` |
| `tui.showToast({ body })`      | 显示 Toast 通知  | `boolean` |

---

#### 示例

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

| 方法                | 描述         | 响应      |
| ------------------- | ------------ | --------- |
| `auth.set({ ... })` | 设置认证凭据 | `boolean` |

---

#### 示例

```javascript
await client.auth.set({
  path: { id: "anthropic" },
  body: { type: "api", key: "your-api-key" },
})
```

---

### Events

| 方法                | 描述               | 响应               |
| ------------------- | ------------------ | ------------------ |
| `event.subscribe()` | 服务器发送的事件流 | 服务器发送的事件流 |

---

#### 示例

```javascript
// Listen to real-time events
const events = await client.event.subscribe()
for await (const event of events.stream) {
  console.log("Event:", event.type, event.properties)
}
```

---

## server

- 官方原文：https://opencode.ai/docs/zh-cn/server
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-server.md`

export const typesUrl = `${config.github}/blob/dev/packages/sdk/js/src/gen/types.gen.ts`

`opencode serve` 命令运行一个无界面的 HTTP 服务器，暴露一个 OpenAPI 端点供 opencode 客户端使用。

---

### 用法

```bash
opencode serve [--port <number>] [--hostname <string>] [--cors <origin>]
```

#### 选项

| 标志            | 描述                  | 默认值           |
| --------------- | --------------------- | ---------------- |
| `--port`        | 监听端口              | `4096`           |
| `--hostname`    | 监听的主机名          | `127.0.0.1`      |
| `--mdns`        | 启用 mDNS 发现        | `false`          |
| `--mdns-domain` | mDNS 服务的自定义域名 | `opencode.local` |
| `--cors`        | 额外允许的浏览器来源  | `[]`             |

`--cors` 可以多次传递：

```bash
opencode serve --cors http://localhost:5173 --cors https://app.example.com
```

---

### 认证

设置 `OPENCODE_SERVER_PASSWORD` 以使用 HTTP 基本认证保护服务器。用户名默认为 `opencode`，也可以设置 `OPENCODE_SERVER_USERNAME` 来覆盖它。这适用于 `opencode serve` 和 `opencode web`。

```bash
OPENCODE_SERVER_PASSWORD=your-password opencode serve
```

---

### 工作原理

当你运行 `opencode` 时，它会启动一个 TUI 和一个服务器。TUI 是与服务器通信的客户端。服务器暴露一个 OpenAPI 3.1 规范端点。该端点也用于生成 [SDK](/docs/sdk)。

:::tip
使用 opencode 服务器以编程方式与 opencode 交互。

这种架构让 opencode 支持多个客户端，并允许你以编程方式与 opencode 交互。

你可以运行 `opencode serve` 来启动一个独立的服务器。如果你已经在运行 opencode TUI，`opencode serve` 会启动一个新的服务器。

---

#### 连接到现有服务器

当你启动 TUI 时，它会随机分配端口和主机名。你也可以传入 `--hostname` 和 `--port` [标志](/docs/cli)，然后用它来连接对应的服务器。

[`/tui`](#tui) 端点可用于通过服务器驱动 TUI。例如，你可以预填充或运行一个提示词。此方式被 OpenCode [IDE](/docs/ide) 插件所使用。

---

## 规范

服务器发布了一个 OpenAPI 3.1 规范，可在以下地址查看：

```
http://<hostname>:<port>/doc
```

例如，`http://localhost:4096/doc`。使用该规范可以生成客户端或检查请求和响应类型，也可以在 Swagger 浏览器中查看。

---

## API

opencode 服务器暴露以下 API。

---

### 全局

| 方法  | 路径             | 描述                     | 响应                                 |
| ----- | ---------------- | ------------------------ | ------------------------------------ |
| `GET` | `/global/health` | 获取服务器健康状态和版本 | `{ healthy: true, version: string }` |
| `GET` | `/global/event`  | 获取全局事件（SSE 流）   | 事件流                               |

---

### 项目

| 方法  | 路径               | 描述         | 响应                                          |
| ----- | ------------------ | ------------ | --------------------------------------------- |
| `GET` | `/project`         | 列出所有项目 | <a href={typesUrl}><code>Project[]</code></a> |
| `GET` | `/project/current` | 获取当前项目 | <a href={typesUrl}><code>Project</code></a>   |

---

### 路径和 VCS

| 方法  | 路径    | 描述                    | 响应                                        |
| ----- | ------- | ----------------------- | ------------------------------------------- |
| `GET` | `/path` | 获取当前路径            | <a href={typesUrl}><code>Path</code></a>    |
| `GET` | `/vcs`  | 获取当前项目的 VCS 信息 | <a href={typesUrl}><code>VcsInfo</code></a> |

---

### 实例

| 方法   | 路径                | 描述         | 响应      |
| ------ | ------------------- | ------------ | --------- |
| `POST` | `/instance/dispose` | 销毁当前实例 | `boolean` |

---

### 配置

| 方法    | 路径                | 描述                 | 响应                                                                                     |
| ------- | ------------------- | -------------------- | ---------------------------------------------------------------------------------------- |
| `GET`   | `/config`           | 获取配置信息         | <a href={typesUrl}><code>Config</code></a>                                               |
| `PATCH` | `/config`           | 更新配置             | <a href={typesUrl}><code>Config</code></a>                                               |
| `GET`   | `/config/providers` | 列出提供商和默认模型 | `{ providers: `<a href={typesUrl}>Provider[]</a>`, default: { [key: string]: string } }` |

---

### 提供商

| 方法   | 路径                             | 描述                    | 响应                                                                                |
| ------ | -------------------------------- | ----------------------- | ----------------------------------------------------------------------------------- |
| `GET`  | `/provider`                      | 列出所有提供商          | `{ all: `<a href={typesUrl}>Provider[]</a>`, default: {...}, connected: string[] }` |
| `GET`  | `/provider/auth`                 | 获取提供商认证方式      | `{ [providerID: string]: `<a href={typesUrl}>ProviderAuthMethod[]</a>` }`           |
| `POST` | `/provider/{id}/oauth/authorize` | 使用 OAuth 授权提供商   | <a href={typesUrl}><code>ProviderAuthAuthorization</code></a>                       |
| `POST` | `/provider/{id}/oauth/callback`  | 处理提供商的 OAuth 回调 | `boolean`                                                                           |

---

### 会话

| 方法     | 路径                                     | 描述                       | 说明                                                                              |
| -------- | ---------------------------------------- | -------------------------- | --------------------------------------------------------------------------------- |
| `GET`    | `/session`                               | 列出所有会话               | 返回 <a href={typesUrl}><code>Session[]</code></a>                                |
| `POST`   | `/session`                               | 创建新会话                 | 请求体：`{ parentID?, title? }`，返回 <a href={typesUrl}><code>Session</code></a> |
| `GET`    | `/session/status`                        | 获取所有会话的状态         | 返回 `{ [sessionID: string]: `<a href={typesUrl}>SessionStatus</a>` }`            |
| `GET`    | `/session/:id`                           | 获取会话详情               | 返回 <a href={typesUrl}><code>Session</code></a>                                  |
| `DELETE` | `/session/:id`                           | 删除会话及其所有数据       | 返回 `boolean`                                                                    |
| `PATCH`  | `/session/:id`                           | 更新会话属性               | 请求体：`{ title? }`，返回 <a href={typesUrl}><code>Session</code></a>            |
| `GET`    | `/session/:id/children`                  | 获取会话的子会话           | 返回 <a href={typesUrl}><code>Session[]</code></a>                                |
| `GET`    | `/session/:id/todo`                      | 获取会话的待办事项列表     | 返回 <a href={typesUrl}><code>Todo[]</code></a>                                   |
| `POST`   | `/session/:id/init`                      | 分析应用并创建 `AGENTS.md` | 请求体：`{ messageID, providerID, modelID }`，返回 `boolean`                      |
| `POST`   | `/session/:id/fork`                      | 在某条消息处分叉现有会话   | 请求体：`{ messageID? }`，返回 <a href={typesUrl}><code>Session</code></a>        |
| `POST`   | `/session/:id/abort`                     | 中止正在运行的会话         | 返回 `boolean`                                                                    |
| `POST`   | `/session/:id/share`                     | 分享会话                   | 返回 <a href={typesUrl}><code>Session</code></a>                                  |
| `DELETE` | `/session/:id/share`                     | 取消分享会话               | 返回 <a href={typesUrl}><code>Session</code></a>                                  |
| `GET`    | `/session/:id/diff`                      | 获取本次会话的差异         | 查询参数：`messageID?`，返回 <a href={typesUrl}><code>FileDiff[]</code></a>       |
| `POST`   | `/session/:id/summarize`                 | 总结会话                   | 请求体：`{ providerID, modelID }`，返回 `boolean`                                 |
| `POST`   | `/session/:id/revert`                    | 回退消息                   | 请求体：`{ messageID, partID? }`，返回 `boolean`                                  |
| `POST`   | `/session/:id/unrevert`                  | 恢复所有已回退的消息       | 返回 `boolean`                                                                    |
| `POST`   | `/session/:id/permissions/:permissionID` | 响应权限请求               | 请求体：`{ response, remember? }`，返回 `boolean`                                 |

---

### 消息

| 方法   | 路径                              | 描述                       | 说明                                                                                                                                                                 |
| ------ | --------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`  | `/session/:id/message`            | 列出会话中的消息           | 查询参数：`limit?`，返回 `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}[]`                                                       |
| `POST` | `/session/:id/message`            | 发送消息并等待响应         | 请求体：`{ messageID?, model?, agent?, noReply?, system?, tools?, parts }`，返回 `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}` |
| `GET`  | `/session/:id/message/:messageID` | 获取消息详情               | 返回 `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}`                                                                             |
| `POST` | `/session/:id/prompt_async`       | 异步发送消息（不等待响应） | 请求体：与 `/session/:id/message` 相同，返回 `204 No Content`                                                                                                        |
| `POST` | `/session/:id/command`            | 执行斜杠命令               | 请求体：`{ messageID?, agent?, model?, command, arguments }`，返回 `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}`               |
| `POST` | `/session/:id/shell`              | 运行 shell 命令            | 请求体：`{ agent, model?, command }`，返回 `{ info: `<a href={typesUrl}>Message</a>`, parts: `<a href={typesUrl}>Part[]</a>`}`                                       |

---

### 命令

| 方法  | 路径       | 描述         | 响应                                          |
| ----- | ---------- | ------------ | --------------------------------------------- |
| `GET` | `/command` | 列出所有命令 | <a href={typesUrl}><code>Command[]</code></a> |

---

### 文件

| 方法  | 路径                     | 描述                 | 响应                                                                                |
| ----- | ------------------------ | -------------------- | ----------------------------------------------------------------------------------- |
| `GET` | `/find?pattern=<pat>`    | 在文件中搜索文本     | 包含 `path`、`lines`、`line_number`、`absolute_offset`、`submatches` 的匹配对象数组 |
| `GET` | `/find/file?query=<q>`   | 按名称查找文件和目录 | `string[]`（路径）                                                                  |
| `GET` | `/find/symbol?query=<q>` | 查找工作区符号       | <a href={typesUrl}><code>Symbol[]</code></a>                                        |
| `GET` | `/file?path=<path>`      | 列出文件和目录       | <a href={typesUrl}><code>FileNode[]</code></a>                                      |
| `GET` | `/file/content?path=<p>` | 读取文件             | <a href={typesUrl}><code>FileContent</code></a>                                     |
| `GET` | `/file/status`           | 获取已跟踪文件的状态 | <a href={typesUrl}><code>File[]</code></a>                                          |

#### `/find/file` 查询参数

- `query`（必需）— 搜索字符串（模糊匹配）
- `type`（可选）— 将结果限制为 `"file"` 或 `"directory"`
- `directory`（可选）— 覆盖搜索的项目根目录
- `limit`（可选）— 最大结果数（1–200）
- `dirs`（可选）— 旧版标志（`"false"` 仅返回文件）

---

### 工具（实验性）

| 方法  | 路径                                        | 描述                               | 响应                                         |
| ----- | ------------------------------------------- | ---------------------------------- | -------------------------------------------- |
| `GET` | `/experimental/tool/ids`                    | 列出所有工具 ID                    | <a href={typesUrl}><code>ToolIDs</code></a>  |
| `GET` | `/experimental/tool?provider=<p>&model=<m>` | 列出指定模型的工具及其 JSON Schema | <a href={typesUrl}><code>ToolList</code></a> |

---

### LSP、格式化器和 MCP

| 方法   | 路径         | 描述                | 响应                                                     |
| ------ | ------------ | ------------------- | -------------------------------------------------------- |
| `GET`  | `/lsp`       | 获取 LSP 服务器状态 | <a href={typesUrl}><code>LSPStatus[]</code></a>          |
| `GET`  | `/formatter` | 获取格式化器状态    | <a href={typesUrl}><code>FormatterStatus[]</code></a>    |
| `GET`  | `/mcp`       | 获取 MCP 服务器状态 | `{ [name: string]: `<a href={typesUrl}>MCPStatus</a>` }` |
| `POST` | `/mcp`       | 动态添加 MCP 服务器 | 请求体：`{ name, config }`，返回 MCP 状态对象            |

---

### 代理

| 方法  | 路径     | 描述               | 响应                                        |
| ----- | -------- | ------------------ | ------------------------------------------- |
| `GET` | `/agent` | 列出所有可用的代理 | <a href={typesUrl}><code>Agent[]</code></a> |

---

### 日志

| 方法   | 路径   | 描述                                                        | 响应      |
| ------ | ------ | ----------------------------------------------------------- | --------- |
| `POST` | `/log` | 写入日志条目。请求体：`{ service, level, message, extra? }` | `boolean` |

---

### TUI

| 方法   | 路径                    | 描述                                           | 响应         |
| ------ | ----------------------- | ---------------------------------------------- | ------------ |
| `POST` | `/tui/append-prompt`    | 向提示词追加文本                               | `boolean`    |
| `POST` | `/tui/open-help`        | 打开帮助对话框                                 | `boolean`    |
| `POST` | `/tui/open-sessions`    | 打开会话选择器                                 | `boolean`    |
| `POST` | `/tui/open-themes`      | 打开主题选择器                                 | `boolean`    |
| `POST` | `/tui/open-models`      | 打开模型选择器                                 | `boolean`    |
| `POST` | `/tui/submit-prompt`    | 提交当前提示词                                 | `boolean`    |
| `POST` | `/tui/clear-prompt`     | 清除提示词                                     | `boolean`    |
| `POST` | `/tui/execute-command`  | 执行命令（`{ command }`）                      | `boolean`    |
| `POST` | `/tui/show-toast`       | 显示提示消息（`{ title?, message, variant }`） | `boolean`    |
| `GET`  | `/tui/control/next`     | 等待下一个控制请求                             | 控制请求对象 |
| `POST` | `/tui/control/response` | 响应控制请求（`{ body }`）                     | `boolean`    |

---

### 认证

| 方法  | 路径        | 描述                                         | 响应      |
| ----- | ----------- | -------------------------------------------- | --------- |
| `PUT` | `/auth/:id` | 设置认证凭据。请求体必须匹配提供商的数据结构 | `boolean` |

---

### 事件

| 方法  | 路径     | 描述                                                              | 响应             |
| ----- | -------- | ----------------------------------------------------------------- | ---------------- |
| `GET` | `/event` | 服务器发送事件流。第一个事件是 `server.connected`，之后是总线事件 | 服务器发送事件流 |

---

### 文档

| 方法  | 路径   | 描述             | 响应                          |
| ----- | ------ | ---------------- | ----------------------------- |
| `GET` | `/doc` | OpenAPI 3.1 规范 | 包含 OpenAPI 规范的 HTML 页面 |

---

## share

- 官方原文：https://opencode.ai/docs/zh-cn/share
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-share.md`

OpenCode 的分享功能允许您创建指向 OpenCode 对话的公开链接，方便与团队成员协作或向他人寻求帮助。

:::note
共享的对话对任何拥有链接的人都是公开可访问的。

---

## 工作原理

当您分享一段对话时，OpenCode 会：

1. 为您的会话创建一个唯一的公开 URL
2. 将您的对话历史同步到我们的服务器
3. 通过可分享的链接使对话可访问 — `opncd.ai/s/<share-id>`

---

## 分享模式

OpenCode 支持三种分享模式，用于控制对话的共享方式：

---

### 手动模式（默认）

默认情况下，OpenCode 使用手动分享模式。会话不会自动共享，但您可以使用 `/share` 命令手动分享：

```
/share
```

这将生成一个唯一的 URL 并复制到您的剪贴板。

要在[配置文件](/docs/config)中显式设置手动模式：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "manual"
}
```

---

### 自动分享

您可以在[配置文件](/docs/config)中将 `share` 选项设置为 `"auto"`，为所有新对话启用自动分享：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "auto"
}
```

启用自动分享后，每个新对话都会自动共享并生成链接。

---

### 禁用

您可以在[配置文件](/docs/config)中将 `share` 选项设置为 `"disabled"`，完全禁用分享功能：

```json title="opencode.json"
{
  "$schema": "https://opencode.ai/config.json",
  "share": "disabled"
}
```

要在团队中对特定项目强制执行此设置，请将其添加到项目的 `opencode.json` 文件中并提交到 Git。

---

## 取消分享

要停止分享对话并将其从公开访问中移除：

```
/unshare
```

这将移除分享链接并删除与该对话相关的数据。

---

## 隐私

分享对话时需要注意以下几点。

---

### 数据留存

共享的对话在您明确取消分享之前将一直保持可访问状态。这包括：

- 完整的对话历史
- 所有消息和回复
- 会话元数据

---

### 建议

- 仅分享不包含敏感信息的对话。
- 分享前请检查对话内容。
- 协作完成后请取消分享。
- 避免分享包含专有代码或机密数据的对话。
- 对于敏感项目，请完全禁用分享功能。

---

## 企业版

对于企业部署，分享功能可以：

- 出于安全合规考虑**完全禁用**
- **限制**为仅通过 SSO 身份验证的用户可用
- **自托管**在您自己的基础设施上

[了解更多](/docs/enterprise)关于在您的组织中使用 OpenCode 的信息。

---

## 启动 Web 服务器

- 官方原文：https://opencode.ai/docs/zh-cn/web
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-web.md`

OpenCode 可以作为 Web 应用在浏览器中运行，无需终端即可获得同样强大的 AI 编码体验。

## 快速开始

运行以下命令启动 Web 界面：

```bash
opencode web
```

这会在 `127.0.0.1` 上启动一个本地服务器，使用随机可用端口，并自动在默认浏览器中打开 OpenCode。

:::caution
如果未设置 `OPENCODE_SERVER_PASSWORD`，服务器将没有安全保护。本地使用没有问题，但在网络访问时应当设置密码。

:::tip[Windows 用户]
为获得最佳体验，建议从 [WSL](/docs/windows-wsl) 而非 PowerShell 运行 `opencode web`。这可以确保正确的文件系统访问和终端集成。

---

## 配置

你可以通过命令行标志或[配置文件](/docs/config)来配置 Web 服务器。

### 端口

默认情况下，OpenCode 会选择一个可用端口。你也可以指定端口：

```bash
opencode web --port 4096
```

### 主机名

默认情况下，服务器绑定到 `127.0.0.1`（仅限本地访问）。要使 OpenCode 在网络中可访问：

```bash
opencode web --hostname 0.0.0.0
```

使用 `0.0.0.0` 时，OpenCode 会同时显示本地地址和网络地址：

```
  Local access:       http://localhost:4096
  Network access:     http://192.168.1.100:4096
```

### mDNS 发现

启用 mDNS 可以让你的服务器在本地网络中被自动发现：

```bash
opencode web --mdns
```

这会自动将主机名设置为 `0.0.0.0`，并将服务器广播为 `opencode.local`。

你可以自定义 mDNS 域名，以便在同一网络中运行多个实例：

```bash
opencode web --mdns --mdns-domain myproject.local
```

### CORS

要为 CORS 添加额外的允许域名（适用于自定义前端）：

```bash
opencode web --cors https://example.com
```

### 身份验证

要保护服务器访问，可以通过 `OPENCODE_SERVER_PASSWORD` 环境变量设置密码：

```bash
OPENCODE_SERVER_PASSWORD=secret opencode web
```

用户名默认为 `opencode`，可以通过 `OPENCODE_SERVER_USERNAME` 进行更改。

---

## 使用 Web 界面

启动后，Web 界面提供对 OpenCode 会话的访问。

### 会话

在主页上查看和管理你的会话。你可以查看活跃的会话，也可以创建新的会话。

### 服务器状态

点击"See Servers"可以查看已连接的服务器及其状态。

---

## 连接终端

你可以将终端 TUI 连接到正在运行的 Web 服务器：

```bash
# 启动 Web 服务器
opencode web --port 4096

# 在另一个终端中连接 TUI
opencode attach http://localhost:4096
```

这样你就可以同时使用 Web 界面和终端，共享相同的会话和状态。

---

## 配置文件

你也可以在 `opencode.json` 配置文件中设置服务器选项：

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

命令行标志的优先级高于配置文件中的设置。
