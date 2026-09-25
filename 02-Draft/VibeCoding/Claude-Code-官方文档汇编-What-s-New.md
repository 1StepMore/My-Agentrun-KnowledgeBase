---
title: Claude Code 官方文档汇编 · What's New
source: Claude Code 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w13.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w14.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w15.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w16.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w17.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w18.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w19.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w20.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w21.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w22.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w23.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w24.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w25.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w26.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w27.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w28.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w29.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w30.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w32.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w33.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w34.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w35.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w36.md
- VibeCoding/claude-code/claude-code-en-whats-new-2026-w37.md
- VibeCoding/claude-code/claude-code-en-whats-new-index.md
evidence: E1
domain: VibeCoding
keywords:
- claude-code
- vibe-coding
- AI编程
- AI-Agent
- context-engineering
state:
  phase: draft
  time_raw: 2026-09-23 02:42:51+08:00
  time_draft: 2026-09-23 03:14:06+08:00
  time_wiki: '2026-09-23T10:40:21+08:00'
wiki_ref: 03-Wiki/氛围编程/_MOC-氛围编程.md
---

> **汇编性质**：Claude Code 官方文档 官方原文 25 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## March 23–27, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w13.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w13.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 13 · March 23–27, 2026

> Auto mode for hands-off permissions, computer use built in, PR auto-fix in the cloud, transcript search, and a PowerShell tool for Windows.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-83">v2.1.83 → v2.1.85</a></span>
  <span>6 features · March 23–27</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Auto mode</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">Auto mode hands your permission prompts to a classifier. Safe edits and commands run without interrupting you; anything destructive or suspicious gets blocked and surfaced. It's the middle ground between approving every file write and running with <code>--dangerously-skip-permissions</code>.</p>

  <Frame>
    <img src="https://mintcdn.com/claude-code/CfffsX01JHFnIKvD/images/whats-new/auto-mode.png?fit=max&auto=format&n=CfffsX01JHFnIKvD&q=85&s=367c9e9d4ba5bc57ec4b935154bf1fbb" alt="Claude Code prompt footer showing 'auto mode on (shift+tab to cycle)' indicator in yellow" width="2400" height="691" data-path="images/whats-new/auto-mode.png" />
  </Frame>

  <p className="digest-feature-try">Cycle to auto with Shift+Tab, or set it as your default:</p>

  ```json ~/.claude/settings.json {3} theme={null}
  {
    "permissions": {
      "defaultMode": "auto"
    }
  }
  ```

  <a className="digest-feature-link" href="/docs/en/permission-modes">Permission modes guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Computer use</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">Claude can now control your actual desktop from the Claude Code Desktop app: open native apps, click through the iOS simulator, drive hardware control panels, and verify changes on screen. It's off by default and asks before each action. Best for the things nothing else can reach: apps without an API, proprietary tools, anything that only exists as a GUI.</p>

  <Frame>
    <img src="https://mintcdn.com/claude-code/CfffsX01JHFnIKvD/images/whats-new/computer-use.png?fit=max&auto=format&n=CfffsX01JHFnIKvD&q=85&s=d631de2017edafff463505f8ddbc0f51" alt="Claude Desktop settings with the Computer use toggle enabled, showing the option to let Claude take screenshots and control your keyboard and mouse in apps you allow" width="2376" height="1210" data-path="images/whats-new/computer-use.png" />
  </Frame>

  <p className="digest-feature-try">Enable it in Settings, grant the OS permissions, then ask Claude to verify a change end to end:</p>

  ```text title="Claude Code" wrap theme={null}
  Open the iOS simulator, tap through the onboarding flow, and screenshot each step
  ```

  <a className="digest-feature-link" href="/docs/en/desktop#let-claude-use-your-computer">Computer use guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">PR auto-fix</span>
    <span className="digest-feature-pill">Web</span>
  </div>

  <p className="digest-feature-lede">Flip a switch when you open a PR and walk away. Claude watches CI, fixes the failures, handles the nits, and pushes until it's green. No more babysitting a PR through six rounds of lint errors.</p>

  <Frame>
    <img src="https://mintcdn.com/claude-code/CfffsX01JHFnIKvD/images/whats-new/auto-fix.png?fit=max&auto=format&n=CfffsX01JHFnIKvD&q=85&s=c62b181c6c5d96929f0b43525f9f3584" alt="Claude Code web CI panel showing the Auto fix toggle enabled, with description 'Proactively fix CI failures and review comments'" width="960" height="444" data-path="images/whats-new/auto-fix.png" />
  </Frame>

  <p className="digest-feature-try">After creating a PR on Claude Code web, toggle Auto fix in the CI panel.</p>

  <a className="digest-feature-link" href="/docs/en/claude-code-on-the-web#auto-fix-pull-requests">Auto-fix pull requests</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Transcript search</span>
    <span className="digest-feature-pill">v2.1.83</span>
  </div>

  <p className="digest-feature-lede">Press <code>/</code> in transcript mode to search your conversation. <code>n</code> and <code>N</code> step through matches. Finally a way to find that one Bash command Claude ran 400 messages ago.</p>

  <p className="digest-feature-try">Open transcript mode and search:</p>

  ```text Claude Code theme={null}
  Ctrl+O    # open transcript
  /migrate  # search for "migrate"
  n         # next match
  N         # previous match
  ```

  <a className="digest-feature-link" href="/docs/en/fullscreen#search-and-review-the-conversation">Fullscreen guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">PowerShell tool</span>
    <span className="digest-feature-pill">preview</span>
    <span className="digest-feature-pill">v2.1.84</span>
  </div>

  <p className="digest-feature-lede">Windows gets a native PowerShell tool alongside Bash. Claude can run cmdlets, pipe objects, and work with Windows-native paths without translating everything through Git Bash.</p>

  <p className="digest-feature-try">Opt in from settings:</p>

  ```json .claude/settings.json {3} theme={null}
  {
    "env": {
      "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"
    }
  }
  ```

  <a className="digest-feature-link" href="/docs/en/tools-reference#powershell-tool">PowerShell tool docs</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Conditional hooks</span>
    <span className="digest-feature-pill">v2.1.85</span>
  </div>

  <p className="digest-feature-lede">Hooks can now declare an <code>if</code> field using permission rule syntax. Your pre-commit check only spawns for <code>Bash(git commit \*)</code> instead of every bash call, cutting the process overhead on busy sessions.</p>

  <p className="digest-feature-try">Scope a hook to git commits only:</p>

  ```json .claude/settings.json {5} theme={null}
  {
    "hooks": {
      "PreToolUse": [{
        "hooks": [{
          "if": "Bash(git commit *)",
          "type": "command",
          "command": ".claude/hooks/lint-staged.sh"
        }]
      }]
    }
  }
  ```

  <a className="digest-feature-link" href="/docs/en/hooks">Hooks reference</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Plugin <code>userConfig</code> now public: prompt for settings at enable time, keychain-backed secrets</div>
    <div>Pasted images insert <code>\[Image #N]</code> chips you can reference positionally</div>
    <div><code>managed-settings.d/</code> drop-in directory for layered policy fragments</div>
    <div><code>CwdChanged</code> and <code>FileChanged</code> hook events for direnv-style setups</div>
    <div>Agents can declare <code>initialPrompt</code> in frontmatter to auto-submit a first turn</div>
    <div><code>Ctrl+X Ctrl+E</code> opens your external editor, matching readline</div>
    <div>Interrupting before any response restores your input automatically</div>
    <div><code>/status</code> now works while Claude is responding</div>
    <div>Deep links open in your preferred terminal, not first-detected</div>
    <div>Idle-return nudge to <code>/clear</code> after 75+ minutes away</div>
    <div>VS Code: rate limit banner, Esc-twice rewind picker</div>
  </div>
</div>

[Full changelog for v2.1.83–v2.1.85 →](/docs/en/changelog#2-1-83)

---

## March 30 – April 3, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w14.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w14.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 14 · March 30 – April 3, 2026

> Computer use in the CLI, interactive in-product lessons, flicker-free rendering, per-tool MCP result-size overrides, and plugin executables on PATH.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-86">v2.1.86 → v2.1.91</a></span>
  <span>5 features · March 30 – April 3</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Computer use in the CLI</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">Last week computer use landed in the Desktop app. This week it's in the CLI: Claude can open native apps, click through UI, test its own changes, and fix what breaks, all from your terminal. Web apps already had verification loops; native iOS, macOS, and other GUI-only apps didn't. Now they do. Best for closing the loop on apps and tools where there's no API to call. Still early; expect rough edges.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/CfffsX01JHFnIKvD/images/whats-new/cli-computer-use.mp4?fit=max&auto=format&n=CfffsX01JHFnIKvD&q=85&s=c17a337902308d7c9121013ded0494db" data-path="images/whats-new/cli-computer-use.mp4" />
  </Frame>

  <p className="digest-feature-try">Requires macOS and a Pro or Max plan; otherwise, <code>computer-use</code> won't appear in <code>/mcp</code>. Run <code>/mcp</code>, find <code>computer-use</code>, and toggle it on. Then ask Claude to verify a change end to end:</p>

  ```text title="Claude Code" wrap theme={null}
  Open the iOS simulator, tap through onboarding, and screenshot each step
  ```

  <a className="digest-feature-link" href="/docs/en/computer-use">Computer use guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/powerup</span>
    <span className="digest-feature-pill">v2.1.90</span>
  </div>

  <p className="digest-feature-lede">Interactive lessons that teach Claude Code features through animated demos, right inside your terminal. Claude Code releases frequently, and features that would have changed how you work last month can slip by. Run <code>/powerup</code> once and you'll know what's there.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/CfffsX01JHFnIKvD/images/whats-new/powerup.mp4?fit=max&auto=format&n=CfffsX01JHFnIKvD&q=85&s=fb88beddc0ecc8029da5ab029e4b28f1" data-path="images/whats-new/powerup.mp4" />
  </Frame>

  <p className="digest-feature-try">Run it:</p>

  ```text title="Claude Code" wrap theme={null}
  /powerup
  ```

  <a className="digest-feature-link" href="/docs/en/commands">Commands reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Flicker-free rendering</span>
    <span className="digest-feature-pill">v2.1.89</span>
  </div>

  <p className="digest-feature-lede">Opt into a new alt-screen renderer with virtualized scrollback. The prompt input stays pinned to the bottom, mouse selection works across long conversations, and the flicker on redraw is gone. Unset <code>CLAUDE\_CODE\_NO\_FLICKER</code> to roll back.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/CfffsX01JHFnIKvD/images/whats-new/flicker-free.mp4?fit=max&auto=format&n=CfffsX01JHFnIKvD&q=85&s=7719e35e52a3f9734b0cf69edac333ad" data-path="images/whats-new/flicker-free.mp4" />
  </Frame>

  <p className="digest-feature-try">Set the env var and restart Claude Code:</p>

  ```bash theme={null}
  export CLAUDE_CODE_NO_FLICKER=1
  claude
  ```

  <a className="digest-feature-link" href="/docs/en/fullscreen">Fullscreen rendering</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">MCP result-size override</span>
    <span className="digest-feature-pill">v2.1.91</span>
  </div>

  <p className="digest-feature-lede">MCP server authors can now raise the truncation cap on a specific tool by setting <code>anthropic/maxResultSizeChars</code> in the tool's <code>tools/list</code> entry, up to a hard ceiling of 500K characters. The cap used to be global, so tools that occasionally returned inherently large payloads like database schemas or full file trees hit the default limit and got persisted to disk with a file reference. Per-tool overrides keep those results inline when the tool really needs them.</p>

  <p className="digest-feature-try">Annotate the tool in your server's <code>tools/list</code> response:</p>

  ```json highlight={5} theme={null}
  {
    "name": "get_schema",
    "description": "Returns the full database schema",
    "_meta": {
      "anthropic/maxResultSizeChars": 500000
    }
  }
  ```

  <a className="digest-feature-link" href="/docs/en/mcp#raise-the-limit-for-a-specific-tool">MCP reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Plugin executables on PATH</span>
    <span className="digest-feature-pill">v2.1.91</span>
  </div>

  <p className="digest-feature-lede">Place an executable in a <code>bin/</code> directory at your plugin root and Claude Code adds that directory to the Bash tool's <code>PATH</code> while the plugin is enabled. Claude can then invoke the binary as a bare command from any Bash tool call, with no absolute path or wrapper script needed. Handy for packaging CLI helpers next to the commands, agents, and hooks that call them.</p>

  <p className="digest-feature-try">Add a <code>bin/</code> directory at the plugin root:</p>

  ```text highlight={4, 5} theme={null}
  my-plugin/
  ├── .claude-plugin/
  │   └── plugin.json
  └── bin/
      └── my-tool
  ```

  <a className="digest-feature-link" href="/docs/en/plugins-reference#file-locations-reference">Plugins reference</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Auto mode follow-ups: new <code>PermissionDenied</code> hook fires on classifier denials (return <code>retry: true</code> to let Claude try a different approach), and <code>/permissions</code> → Recently denied lets you retry manually with <code>r</code></div>
    <div>New <code>defer</code> value for <code>permissionDecision</code> in <code>PreToolUse</code> hooks: <code>-p</code> sessions pause at a tool call and exit with a <code>deferred\_tool\_use</code> payload so an SDK app or custom UI can surface it, then resume with <code>--resume</code></div>
    <div><code>/buddy</code>: hatch a small creature that watches you code. An April Fools' joke, no longer available</div>
    <div><code>disableSkillShellExecution</code> setting blocks inline shell from skills, custom commands, and plugin commands</div>
    <div>Edit tool now works on files viewed via <code>cat</code> or <code>sed -n</code> without a separate Read</div>
    <div>Hook output over 50K saved to disk with a path + preview instead of injected into context</div>
    <div>Thinking summaries off by default in interactive sessions (<code>showThinkingSummaries: true</code> to restore)</div>
    <div>Voice mode: push-to-talk modifier combos, Windows WebSocket, macOS Apple Silicon mic permission</div>
    <div><code>claude-cli://</code> deep links accept multi-line prompts (encoded <code>%0A</code>)</div>
  </div>
</div>

[Full changelog for v2.1.86–v2.1.91 →](/docs/en/changelog#2-1-86)

---

## April 6–10, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w15.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w15.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 15 · April 6–10, 2026

> Ultraplan cloud planning, the Monitor tool with self-pacing /loop, /team-onboarding for packaging your setup, and /autofix-pr from your terminal.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-92">v2.1.92 → v2.1.101</a></span>
  <span>4 features · April 6–10</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Ultraplan</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">Kick off plan mode in the cloud from your terminal, then review the result in your browser. Claude drafts the plan in a Claude Code on the web session while your terminal stays free; when it's ready you comment on individual sections, ask for revisions, and choose to execute remotely or send it back to your CLI. As of v2.1.101 the first run auto-creates a default cloud environment, so there's no web setup step before you can try it.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/aFXPQxiBOW99MHS3/images/whats-new/ultraplan.mp4?fit=max&auto=format&n=aFXPQxiBOW99MHS3&q=85&s=e8f2f23730c6a5c289dbf3e7b13eadf6" data-path="images/whats-new/ultraplan.mp4" />
  </Frame>

  <p className="digest-feature-try">Run the command, or just include the keyword in any prompt:</p>

  ```text title="Claude Code" wrap theme={null}
  /ultraplan migrate the auth service from sessions to JWTs
  ```

  <a className="digest-feature-link" href="/docs/en/ultraplan">Ultraplan guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Monitor tool</span>
    <span className="digest-feature-pill">v2.1.98</span>
  </div>

  <p className="digest-feature-lede">A new built-in tool that spawns a background watcher and streams its events into the conversation: each event lands as a new transcript message that Claude reacts to immediately. Tail a training run, babysit a PR's CI, or auto-fix a dev server crash the moment it happens, all without a Bash sleep loop holding the turn open.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/aFXPQxiBOW99MHS3/images/whats-new/monitor-tool.mp4?fit=max&auto=format&n=aFXPQxiBOW99MHS3&q=85&s=f4156c15a0999de5c5157f54a3117c89" data-path="images/whats-new/monitor-tool.mp4" />
  </Frame>

  <p className="digest-feature-try">Ask Claude to watch something while you keep working:</p>

  ```text title="Claude Code" wrap theme={null}
  Tail server.log in the background and tell me the moment a 5xx shows up
  ```

  <p className="digest-feature-try">This pairs with <code>/loop</code>, which now self-paces: omit the interval and Claude schedules the next tick based on the task, or reaches for the Monitor tool to skip polling altogether.</p>

  ```text title="Claude Code" wrap theme={null}
  /loop check CI on my PR
  ```

  <a className="digest-feature-link" href="/docs/en/tools-reference#monitor-tool">Monitor tool reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/autofix-pr</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">PR auto-fix landed on the web in Week 13. Now you can turn it on without leaving your terminal: <code>/autofix-pr</code> infers the open PR for your current branch and enables auto-fix for it on Claude Code on the web in one step. Push your branch, run the command, walk away; Claude watches CI and review comments and pushes fixes until it's green.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/aFXPQxiBOW99MHS3/images/whats-new/autofix-pr.mp4?fit=max&auto=format&n=aFXPQxiBOW99MHS3&q=85&s=95f191eb4711130a128aec3f6b720527" data-path="images/whats-new/autofix-pr.mp4" />
  </Frame>

  <p className="digest-feature-try">Run it from the PR's branch:</p>

  ```text title="Claude Code" wrap theme={null}
  /autofix-pr
  ```

  <a className="digest-feature-link" href="/docs/en/claude-code-on-the-web#auto-fix-pull-requests">Auto-fix pull requests</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/team-onboarding</span>
    <span className="digest-feature-pill">v2.1.101</span>
  </div>

  <p className="digest-feature-lede">Generates a teammate ramp-up guide from your local Claude Code usage. Run it in a project you know well and hand the output to a new teammate so they can replay your setup instead of starting from defaults.</p>

  <p className="digest-feature-try">Run it from a project you've spent real time in:</p>

  ```text title="Claude Code" wrap theme={null}
  /team-onboarding
  ```

  <a className="digest-feature-link" href="/docs/en/commands">Commands reference</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Focus view: press <code>Ctrl+O</code> in flicker-free mode to collapse the view to your last prompt, a one-line tool summary with diffstats, and Claude's final response</div>
    <div>Guided <a href="/docs/en/amazon-bedrock">Amazon Bedrock</a> and <a href="/docs/en/google-vertex-ai">Google Cloud's Agent Platform</a> setup wizards on the login screen: pick "3rd-party platform" for step-by-step auth, region, credential check, and model pinning</div>
    <div><code>/agents</code> gets a tabbed layout: a Running tab shows live subagents with a <code>● N running</code> count, plus Run agent and View running instance actions in the Library tab</div>
    <div>Default effort level is now <code>high</code> for API-key, Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, Team, and Enterprise users (control with <code>/effort</code>)</div>
    <div><code>/cost</code> shows a per-model and cache-hit breakdown for subscription users</div>
    <div><code>/release-notes</code> is now an interactive version picker</div>
    <div>Status line: new <code>refreshInterval</code> setting re-runs the command every N seconds, and <code>workspace.git\_worktree</code> in the JSON input</div>
    <div><code>CLAUDE\_CODE\_PERFORCE\_MODE</code>: Edit/Write fail on read-only files with a <code>p4 edit</code> hint instead of silently overwriting</div>
    <div>OS CA certificate store is now trusted by default, so enterprise TLS proxies work without extra setup (<code>CLAUDE\_CODE\_CERT\_STORE=bundled</code> to opt out)</div>
    <div>Amazon Bedrock powered by Mantle: set <code>CLAUDE\_CODE\_USE\_MANTLE=1</code></div>
    <div>Hardened Bash tool permissions: backslash-escaped flags, env-var prefixes, <code>/dev/tcp</code> redirects, and compound commands now prompt correctly</div>
    <div><code>UserPromptSubmit</code> hooks can set the session title via <code>hookSpecificOutput.sessionTitle</code></div>
  </div>
</div>

[Full changelog for v2.1.92–v2.1.101 →](/docs/en/changelog#2-1-92)

---

## April 13–17, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w16.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w16.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 16 · April 13–17, 2026

> Claude Opus 4.7 with the new xhigh effort level, Routines on Claude Code on the web, mobile push notifications that ping your phone when Claude needs you, a /usage breakdown that shows what's driving your limits, and native binaries replacing the bundled JavaScript.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-105">v2.1.105 → v2.1.113</a></span>
  <span>5 features · April 13–17</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Opus 4.7</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Anthropic's strongest coding model yet is now the default on Max and Team Premium, and available everywhere else from <code>/model</code>. It adds a new <code>xhigh</code> effort level that sits between <code>high</code> and <code>max</code>: best results for most coding and agentic tasks, applied as the default the first time you switch to 4.7. <code>/effort</code> now opens an interactive arrow-key slider when you call it without arguments, so you can dial intelligence against speed without remembering the level names.</p>

  <p className="digest-feature-try">Switch model and effort in one go:</p>

  ```text Claude Code theme={null}
  > /model opus
  > /effort xhigh
  ```

  <a className="digest-feature-link" href="/docs/en/model-config#adjust-effort-level">Model config: effort levels</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Routines</span>
    <span className="digest-feature-pill">web</span>
  </div>

  <p className="digest-feature-lede">Templated cloud agents that fire on a schedule, a GitHub event, or an API call. Define a routine once on Claude Code on the web with a prompt, the repos it can touch, and the connectors it needs, then let PR-opened, release-published, or your own webhook trigger it without your machine running. The trigger picker now covers GitHub events with optional filters and gives every routine a tokened <code>/fire</code> endpoint for external systems.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/routines.png?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=2ba818ea9280c549511cb48b9b4d1dc5" alt="Creating a routine on Claude Code on the web with schedule, GitHub event, and API triggers" width="1440" height="810" data-path="images/whats-new/routines.png" />
  </Frame>

  <p className="digest-feature-try">Create one from the web UI, or scaffold from your terminal:</p>

  ```text Claude Code theme={null}
  > /schedule daily PR review at 9am
  ```

  <a className="digest-feature-link" href="/docs/en/routines">Routines guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/usage breakdown</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">More visibility into where your Claude Code usage goes. <code>/usage</code> now shows what's driving your limits: parallel sessions, subagents, cache misses, and long context, each with a percentage of your last 24 hours and a tip to optimize it. Press <code>d</code> or <code>w</code> to switch between day and week views.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/usage.png?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=792a4b43cbef4e2931974831f076bca6" alt="The /usage command showing a breakdown of what's contributing to limits usage" width="1204" height="1182" data-path="images/whats-new/usage.png" />
  </Frame>

  <p className="digest-feature-try">Run it any time:</p>

  ```text Claude Code theme={null}
  > /usage
  ```

  <a className="digest-feature-link" href="/docs/en/commands">Commands reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Mobile push notifications</span>
    <span className="digest-feature-pill">mobile</span>
  </div>

  <p className="digest-feature-lede">With <a href="/docs/en/remote-control">Remote Control</a> connected, Claude can send a push notification to your phone when a long task finishes or it needs a decision to keep going. Turn it on with "Push when Claude decides" in <code>/config</code>, or ask for one in your prompt. Useful when you kick off a long agent run and want to step away from the terminal.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/uII1TETOZxBUZ3lB/images/whats-new/push-notifications.mp4?fit=max&auto=format&n=uII1TETOZxBUZ3lB&q=85&s=c91a967139596500cbdb581a53822ac1" data-path="images/whats-new/push-notifications.mp4" />
  </Frame>

  <p className="digest-feature-try">Ask Claude to ping you when it's done:</p>

  ```text Claude Code theme={null}
  > notify me when the tests pass
  ```

  <a className="digest-feature-link" href="/docs/en/remote-control#mobile-push-notifications">Remote Control: mobile push notifications</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Native binaries</span>
    <span className="digest-feature-pill">v2.1.113</span>
  </div>

  <p className="digest-feature-lede">The <code>claude</code> CLI now spawns a native per-platform binary instead of bundled JavaScript, so the installed <code>claude</code> command no longer invokes Node. The npm package pulls the right binary in through an optional dependency such as <code>@anthropic-ai/claude-code-darwin-arm64</code>, so your install command doesn't change. The standalone installer already shipped this binary; npm now matches it.</p>

  <p className="digest-feature-try">Upgrade and check what you're running:</p>

  ```bash theme={null}
  claude update
  claude --version
  ```

  <a className="digest-feature-link" href="/docs/en/setup">Setup guide</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>New <a href="/docs/en/ultrareview"><code>/ultrareview</code></a>: comprehensive code review in the cloud using parallel multi-agent analysis and an adversarial critique pass. Run it bare to review your current branch, or <code>/ultrareview \<PR#></code> for a specific PR</div>
    <div><a href="/docs/en/permission-modes#eliminate-prompts-with-auto-mode">Auto mode</a> is now available for Max subscribers on Opus 4.7, and the <code>--enable-auto-mode</code> flag is no longer required</div>
    <div><a href="/docs/en/interactive-mode#session-recap">Session recap</a> shows a one-line summary of what happened while you were away; run <code>/recap</code> on demand or turn it off from <code>/config</code></div>
    <div>New <code>/tui</code> command and <code>tui</code> setting switch between classic and flicker-free rendering mid-conversation; focus view moved from <code>Ctrl+O</code> to its own <code>/focus</code> command</div>
    <div>Plugins can ship background watchers via a top-level <code>monitors</code> manifest key that auto-arms at session start or on skill invoke</div>
    <div>"Auto (match terminal)" option in <code>/theme</code> follows your terminal's dark/light mode</div>
    <div><code>/fewer-permission-prompts</code> scans your transcripts for common read-only Bash and MCP calls and proposes an allowlist for <code>.claude/settings.json</code></div>
    <div>Claude can now discover and run built-in commands like <code>/init</code>, <code>/review</code>, and <code>/security-review</code> via the Skill tool</div>
    <div><code>PreCompact</code> hooks can block compaction by exiting with code 2 or returning <code>{"{"}"decision":"block"{"}"}</code></div>
    <div><code>ENABLE\_PROMPT\_CACHING\_1H</code> opts API key, Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry users into 1-hour prompt cache TTL</div>
    <div><code>sandbox.network.deniedDomains</code> setting carves specific domains out of a broader <code>allowedDomains</code> wildcard</div>
    <div><code>/undo</code> is now an alias for <code>/rewind</code>, and <code>/proactive</code> is an alias for <code>/loop</code></div>
    <div>Hardened Bash permissions: deny rules now match through <code>env</code>/<code>sudo</code>/<code>watch</code> wrappers, and <code>Bash(find:\*)</code> allow rules no longer auto-approve <code>-exec</code> or <code>-delete</code></div>
  </div>
</div>

[Full changelog for v2.1.105–v2.1.113 →](/docs/en/changelog#2-1-105)

---

## April 20–24, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w17.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w17.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 17 · April 20–24, 2026

> /ultrareview opens as a research preview, automatic session recaps when you return to a terminal, custom color themes you can build and ship in plugins, and a redesigned Claude Code on the web.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-114">v2.1.114 → v2.1.119</a></span>
  <span>4 features · April 20–24</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/ultrareview</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">Now in public research preview. Ultrareview runs a fleet of bug-hunting agents in the cloud against your branch or a PR, and findings land back in the CLI or Desktop automatically. Run it before merging critical changes such as auth or data migrations.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/ultrareview.mp4?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=0fb1271365d38f414ad155aeb8edb08e" data-path="images/whats-new/ultrareview.mp4" />
  </Frame>

  <p className="digest-feature-try">Review the branch you're on:</p>

  ```text Claude Code theme={null}
  > /ultrareview
  ```

  <p className="digest-feature-try">Or point it at a PR:</p>

  ```text Claude Code theme={null}
  > /ultrareview 1234
  ```

  <a className="digest-feature-link" href="/docs/en/ultrareview">Ultrareview guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Session recap</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">Switch focus away from a session and come back to a one-line recap of what happened while you were gone. Helpful for staying in flow while running several Claude sessions at once.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/session-recap.mp4?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=0a8db1470bd0161a47efeb2f322af76f" data-path="images/whats-new/session-recap.mp4" />
  </Frame>

  <p className="digest-feature-try">Generate a recap on demand, or turn the automatic one off from <code>/config</code>:</p>

  ```text Claude Code theme={null}
  > /recap
  ```

  <a className="digest-feature-link" href="/docs/en/interactive-mode#session-recap">Interactive mode: session recap</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Custom themes</span>
    <span className="digest-feature-pill">v2.1.118</span>
  </div>

  <p className="digest-feature-lede">Build and switch between named color themes from <code>/theme</code>, or hand-edit JSON files in <code>\~/.claude/themes/</code>. Each theme picks a base preset and overrides only the tokens you care about. Plugins can ship themes too.</p>

  <p className="digest-feature-try">Open the theme picker and create a new one:</p>

  ```text Claude Code theme={null}
  > /theme
  ```

  <a className="digest-feature-link" href="/docs/en/terminal-config#create-a-custom-theme">Terminal config: create a custom theme</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Code on the web</span>
    <span className="digest-feature-pill">web</span>
  </div>

  <p className="digest-feature-lede">A new look for <a href="https://claude.ai/code">claude.ai/code</a> that matches the redesigned desktop app: sessions sidebar, drag-and-drop layout, and a refreshed routines view. Key parts were rebuilt for quicker responses and a more reliable experience.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/FTi4SBJ9YRs7d-5X/images/whats-new/web-redesign.jpeg?fit=max&auto=format&n=FTi4SBJ9YRs7d-5X&q=85&s=a2aca1b49e295b7337f5779038db8e2c" alt="Claude Code on the web redesign overview: new UI, speed and reliability, work across web, mobile, and CLI" width="1602" height="1610" data-path="images/whats-new/web-redesign.jpeg" />
  </Frame>

  <a className="digest-feature-link" href="/docs/en/claude-code-on-the-web">Claude Code on the web</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><a href="/docs/en/interactive-mode#vim-editor-mode">Vim visual mode</a>: press <code>v</code> for character selection or <code>V</code> for line selection in the prompt input, with operators and visual feedback</div>
    <div>Hooks can now call MCP tools directly via <a href="/docs/en/hooks#mcp-tool-hook-fields"><code>type: "mcp\_tool"</code></a>, so a hook can hit an already-connected server without spawning a process</div>
    <div><code>/cost</code> and <code>/stats</code> are merged into <a href="/docs/en/commands"><code>/usage</code></a>; the old names still work as typing shortcuts that open the relevant tab</div>
    <div><code>/config</code> changes (theme, editor mode, verbose, and similar) now persist to <code>\~/.claude/settings.json</code> and follow the same project/local/policy precedence as other <a href="/docs/en/settings">settings</a></div>
    <div><a href="/docs/en/sub-agents#fork-the-current-conversation">Forked subagents</a> can be enabled on external builds with <code>CLAUDE\_CODE\_FORK\_SUBAGENT=1</code>: a fork inherits your full conversation context instead of starting fresh</div>
    <div>Default <a href="/docs/en/model-config#adjust-effort-level">effort level</a> for Pro and Max subscribers on Opus 4.6 and Sonnet 4.6 is now <code>high</code> (was <code>medium</code>)</div>
    <div>Native macOS and Linux builds replace the <code>Glob</code> and <code>Grep</code> tools with embedded <code>bfs</code> and <code>ugrep</code> available through Bash, for faster searches without a separate tool round-trip</div>
    <div><code>--from-pr</code> now accepts GitLab merge request, Bitbucket pull request, and GitHub Enterprise PR URLs in addition to github.com</div>
    <div>Auto mode: include <code>"\$defaults"</code> in <a href="/docs/en/auto-mode-config"><code>autoMode.allow</code>, <code>soft\_deny</code>, or <code>environment</code></a> to add custom rules alongside the built-in list instead of replacing it</div>
    <div>New <a href="/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution"><code>claude plugin tag</code></a> command creates release git tags for plugins with version validation</div>
    <div>Opus 4.7 sessions now compute against the model's native 1M context window, fixing inflated <code>/context</code> percentages and premature autocompaction</div>
    <div><code>/resume</code> on large sessions is up to 67% faster and now offers to summarize stale, large sessions before re-reading them</div>
  </div>
</div>

[Full changelog for v2.1.114–v2.1.119 →](/docs/en/changelog#2-1-114)

---

## April 27 – May 1, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w18.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w18.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 18 · April 27 – May 1, 2026

> Claude Code on Windows runs without Git Bash, claude auth login accepts a pasted OAuth code when the browser callback can't reach localhost, claude project purge cleans up local state per project, and pasting a PR URL into /resume finds the session that created it.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-120">v2.1.120 → v2.1.126</a></span>
  <span>4 features · April 27 – May 1</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Sign in without a browser callback</span>
    <span className="digest-feature-pill">v2.1.126</span>
  </div>

  <p className="digest-feature-lede"><code>claude auth login</code> now accepts the OAuth code pasted directly into the terminal when the browser callback can't reach localhost. That covers WSL2, SSH sessions, and containers, where the redirect to a local port doesn't work. The same release also fixes login timeouts on slow or proxied connections and in IPv6-only devcontainers.</p>

  <p className="digest-feature-try">Sign in, then paste the code from the browser:</p>

  ```bash theme={null}
  claude auth login
  ```

  <a className="digest-feature-link" href="/docs/en/cli-reference#cli-commands">CLI reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">claude project purge</span>
    <span className="digest-feature-pill">v2.1.124</span>
  </div>

  <p className="digest-feature-lede">Delete all Claude Code state for a project: transcripts, tasks, file history, and the project's config entry. Supports `--dry-run` to preview, `-y`/`--yes` to skip confirmation, `-i`/`--interactive` to choose, and `--all` to clear every project.</p>

  <p className="digest-feature-try">Preview what would be removed:</p>

  ```bash theme={null}
  claude project purge --dry-run
  ```

  <p className="digest-feature-try">Then run it for real:</p>

  ```bash theme={null}
  claude project purge
  ```

  <a className="digest-feature-link" href="/docs/en/cli-reference">CLI reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Resume by PR URL</span>
    <span className="digest-feature-pill">v2.1.122</span>
  </div>

  <p className="digest-feature-lede">When you create a pull request with <code>gh pr create</code>, Claude Code links it to the session that produced it. Now you can get back to that session from the PR URL alone, without remembering its name.</p>

  <p className="digest-feature-try">Open the session picker:</p>

  ```text Claude Code theme={null}
  > /resume
  ```

  <p className="digest-feature-try">Paste the PR URL into the picker. The first character of the paste drops you into search mode, and the list filters to the session that created that PR. Press Enter to resume it. GitHub, GitHub Enterprise, GitLab, and Bitbucket pull and merge request URLs all work.</p>

  ```text Claude Code theme={null}
  https://github.com/your-org/your-repo/pull/1234
  ```

  <p className="digest-feature-try">To open the picker already filtered to the PR, pass the PR number on the command line:</p>

  ```bash theme={null}
  claude --from-pr 1234
  ```

  <a className="digest-feature-link" href="/docs/en/sessions#use-the-session-picker">Sessions: use the session picker</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Windows without Git Bash</span>
    <span className="digest-feature-pill">Windows</span>
  </div>

  <p className="digest-feature-lede">Git for Windows is no longer required. When Bash is absent, Claude Code uses PowerShell as the shell tool, and when the PowerShell tool is enabled it is treated as the primary shell. PowerShell 7 installed via the Microsoft Store, MSI without PATH, or a <code>.NET</code> global tool is now detected automatically.</p>

  <a className="digest-feature-link" href="/docs/en/setup">Setup guide</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>MCP servers can opt out of tool-search deferral with <code>alwaysLoad: true</code> in their config so all of that server's tools are always available</div>
    <div>New <code>claude plugin prune</code> removes orphaned auto-installed plugin dependencies, and <code>plugin uninstall --prune</code> cascades</div>
    <div><code>/skills</code> now has a type-to-filter search box so you can find a skill in a long list without scrolling</div>
    <div><code>PostToolUse</code> hooks can replace tool output for any tool via <code>hookSpecificOutput.updatedToolOutput</code>, not only MCP tools</div>
    <div>New <a href="/docs/en/ultrareview"><code>claude ultrareview</code></a> subcommand runs <code>/ultrareview</code> non-interactively from CI or scripts: prints findings to stdout (<code>--json</code> for raw output) and exits 0 on completion or 1 on failure</div>
    <div><code>--dangerously-skip-permissions</code> now bypasses prompts for writes to <code>.claude/</code>, <code>.git/</code>, <code>.vscode/</code>, shell config files, and other previously protected paths, while catastrophic removal commands still prompt as a safety net</div>
    <div>The <code>/model</code> picker can list models from your gateway's <code>/v1/models</code> endpoint when <code>ANTHROPIC\_BASE\_URL</code> points at an Anthropic-compatible gateway; opt in with <code>CLAUDE\_CODE\_ENABLE\_GATEWAY\_MODEL\_DISCOVERY=1</code> since v2.1.129</div>
    <div>MCP servers that hit a transient error during startup now auto-retry up to 3 times instead of staying disconnected</div>
    <div><code>ANTHROPIC\_BEDROCK\_SERVICE\_TIER</code> selects an Amazon Bedrock service tier: <code>default</code>, <code>flex</code>, or <code>priority</code></div>
    <div><code>/terminal-setup</code> enables iTerm2's clipboard access setting so <code>/copy</code> works, including from tmux</div>
    <div>Google Cloud's Agent Platform now supports X.509 certificate-based Workload Identity Federation (mTLS ADC)</div>
    <div>Significant memory leak fixes: image-heavy sessions, <code>/usage</code> on large transcript histories, and long-running tools without progress events</div>
  </div>
</div>

[Full changelog for v2.1.120–v2.1.126 →](/docs/en/changelog#2-1-120)

---

## May 4–8, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w19.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w19.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 19 · May 4–8, 2026

> Load plugins from .zip archives and URLs, search command history across every project with Ctrl+R, branch new worktrees from local HEAD or the remote default, and block actions unconditionally with auto mode hard deny rules.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-128">v2.1.128 → v2.1.136</a></span>
  <span>2 features · May 4–8</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Plugins from .zip archives and URLs</span>
  </div>

  <p className="digest-feature-lede">`--plugin-dir` now accepts a <code>.zip</code> plugin archive in addition to a directory, and the new `--plugin-url` flag fetches a plugin archive from a URL for the current session. Useful for trying a plugin before adding it to a marketplace, or for shipping internal plugins from an artifact store.</p>

  <p className="digest-feature-try">Load a plugin straight from a URL:</p>

  ```bash terminal theme={null}
  claude --plugin-url https://example.com/my-plugin.zip
  ```

  <a className="digest-feature-link" href="/docs/en/plugins">Plugins guide</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">History search across all your projects</span>
    <span className="digest-feature-pill">v2.1.129</span>
  </div>

  <p className="digest-feature-lede"><code>Ctrl+R</code> reverse-search now defaults to all prompts across every project, restoring the behavior from before v2.1.124. Press <code>Ctrl+S</code> while searching to narrow back to the current project or session. Handy when you remember a command you ran in another repo last week and don't want to go digging for it.</p>

  <a className="digest-feature-link" href="/docs/en/interactive-mode#command-history">Interactive mode: command history</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>New <code>worktree.baseRef</code> setting (<code>fresh</code> | <code>head</code>) controls whether <code>--worktree</code>, the <code>EnterWorktree</code> tool, and agent-isolation worktrees branch from the remote default branch or local <code>HEAD</code>; the default <code>fresh</code> keeps unpushed commits out of new worktrees</div>
    <div>New <code>settings.autoMode.hard\_deny</code> rules block matching actions unconditionally in auto mode, regardless of allow exceptions, for actions that should never run automatically even when broader allow rules apply</div>
    <div>Hooks now receive the active effort level via the `effort.level` JSON input field and the `$CLAUDE_EFFORT` environment variable, and Bash tool commands can read <code>\$CLAUDE\_EFFORT</code></div>
    <div><code>CLAUDE\_CODE\_DISABLE\_ALTERNATE\_SCREEN=1</code> opts out of the fullscreen alternate-screen renderer and keeps the conversation in the terminal's native scrollback</div>
    <div><code>CLAUDE\_CODE\_PACKAGE\_MANAGER\_AUTO\_UPDATE</code> lets Homebrew or WinGet installations run the upgrade in the background and prompt to restart</div>
    <div><code>CLAUDE\_CODE\_SESSION\_ID</code> is now in the Bash tool subprocess environment, matching the <code>session\_id</code> passed to hooks</div>
    <div><code>/mcp</code> now shows the tool count for connected servers and flags servers that connected with 0 tools</div>
    <div><code>--channels</code> now works with console (API key) authentication</div>
    <div>Subprocesses such as Bash, hooks, MCP, and LSP no longer inherit <code>OTEL\_\*</code> environment variables, so OTEL-instrumented apps run via the Bash tool no longer pick up the CLI's own OTLP endpoint</div>
    <div>Sub-agent progress summaries now hit the prompt cache, cutting <code>cache\_creation</code> token cost by roughly 3x</div>
    <div>Several OAuth and credential reliability fixes: parallel sessions no longer dead-end at 401 after a refresh-token race, MCP OAuth refresh tokens are no longer lost when multiple servers refresh concurrently, and a rare login loop from a concurrent credential write is fixed</div>
    <div>New <code>parentSettingsBehavior</code> admin key lets admins opt SDK <code>managedSettings</code> into the policy merge</div>
  </div>
</div>

[Full changelog for v2.1.128–v2.1.136 →](/docs/en/changelog#2-1-128)

---

## May 11–15, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w20.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w20.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 20 · May 11–15, 2026

> Manage every Claude Code session from one screen with agent view, keep Claude working toward a goal until a condition holds, and run fast mode on Opus 4.7 by default.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-139">v2.1.139 → v2.1.142</a></span>
  <span>3 features · May 11–15</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Agent view</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede"><code>claude agents</code> opens one screen for every Claude Code session: what's running, what's blocked on your input, and what's done. Dispatch a bug fix, a pull request review, and a flaky-test investigation as three rows, keep working in another window, and step in only when a row needs you. Attach to any row to drop into its full conversation, then press <code>←</code> to return to the list. Each background session keeps running without a terminal attached.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/ITvjicPxe1SM3GX7/images/whats-new/agent-view.mp4?fit=max&auto=format&n=ITvjicPxe1SM3GX7&q=85&s=0eefe6cbe75464c8f7902bba630ab7a4" data-path="images/whats-new/agent-view.mp4" />
  </Frame>

  <p className="digest-feature-try">Open the dashboard from your shell:</p>

  ```bash terminal theme={null}
  claude agents
  ```

  <a className="digest-feature-link" href="/docs/en/agent-view">Agent view</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/goal</span>
    <span className="digest-feature-pill">v2.1.139</span>
  </div>

  <p className="digest-feature-lede">Set a completion condition and Claude keeps working toward it across turns without you prompting each step. After every turn, a fast model checks whether the condition holds; if not, Claude starts another turn instead of handing control back. Useful for substantial work with a verifiable end state, like migrating a module until every call site compiles and tests pass. The goal clears once the condition is met, and works in interactive, <code>-p</code>, and Remote Control.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/ITvjicPxe1SM3GX7/images/whats-new/goal.mp4?fit=max&auto=format&n=ITvjicPxe1SM3GX7&q=85&s=6806df3780c548b93a02d6fa71da276b" data-path="images/whats-new/goal.mp4" />
  </Frame>

  <p className="digest-feature-try">Set a goal and let Claude run until it holds:</p>

  ```text Claude Code theme={null}
  > /goal all tests in test/auth pass and the lint step is clean
  ```

  <a className="digest-feature-link" href="/docs/en/goal">Goals</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Fast mode on Opus 4.7</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede"><code>/fast</code> now runs on Opus 4.7 by default instead of Opus 4.6. Fast mode is a high-speed Opus configuration: the same model quality at about 2.5x the speed for a higher per-token cost, useful for rapid iteration and live debugging. Pricing is unchanged at \$30/\$150 per MTok, the same as Opus 4.6 fast mode. To pin fast mode to Opus 4.6, set <code>CLAUDE\_CODE\_OPUS\_4\_6\_FAST\_MODE\_OVERRIDE=1</code>.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/ITvjicPxe1SM3GX7/images/whats-new/fast-mode-opus-47.png?fit=max&auto=format&n=ITvjicPxe1SM3GX7&q=85&s=6b6d92f7748ce5328a1ee9a269fb1a87" alt="The Claude Code model picker showing Opus 4.7 Fast 1M as the default with the Fast toggle on" width="3840" height="2160" data-path="images/whats-new/fast-mode-opus-47.png" />
  </Frame>

  <p className="digest-feature-try">Toggle fast mode, now running on Opus 4.7:</p>

  ```text Claude Code theme={null}
  > /fast
  ```

  <a className="digest-feature-link" href="/docs/en/fast-mode#understand-the-cost-tradeoff">Fast mode on Opus 4.7</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><code>claude agents</code> gained dispatch flags (<code>--add-dir</code>, <code>--settings</code>, <code>--mcp-config</code>, <code>--plugin-dir</code>, <code>--permission-mode</code>, <code>--model</code>, <code>--effort</code>, <code>--dangerously-skip-permissions</code>) to configure background sessions, and <code>claude agents --cwd \<path></code> scopes the session list to a directory</div>
    <div>New hook <code>args: string\[]</code> exec form spawns the command directly without a shell, so path placeholders never need quoting</div>
    <div>New <code>continueOnBlock</code> config option for <code>PostToolUse</code> hooks feeds the hook's rejection reason back to Claude and continues the turn instead of ending it</div>
    <div>New <code>terminalSequence</code> field in hook JSON output lets hooks emit desktop notifications, window titles, and bells without a controlling terminal</div>
    <div>The Rewind menu added "Summarize up to here" to compress earlier context while keeping recent turns intact</div>
    <div>Remote Control, <code>/schedule</code>, claude.ai MCP connectors, and notification preferences are now disabled when <code>ANTHROPIC\_API\_KEY</code>, <code>apiKeyHelper</code>, or <code>ANTHROPIC\_AUTH\_TOKEN</code> is set, even alongside a claude.ai login; unset the API key to use these features</div>
    <div>MCP stdio servers now receive <code>CLAUDE\_PROJECT\_DIR</code> in their environment, matching hooks, and plugin configs can reference <code>\${"{"}CLAUDE\_PROJECT\_DIR{"}"}</code> in commands</div>
    <div><code>claude plugin details \<name></code> shows a plugin's component inventory and projected per-session token cost, and the <code>/plugin</code> details pane now also lists the LSP servers a plugin provides</div>
    <div>Plugins with a root-level <code>SKILL.md</code> and no <code>skills/</code> subdirectory are now surfaced as a skill</div>
    <div><code>/feedback</code> can now include recent sessions from the last 24 hours or 7 days for issues spanning more than the current session</div>
    <div>Agent tool <code>subagent\_type</code> now matches case- and separator-insensitively, so <code>"Code Reviewer"</code> resolves to <code>code-reviewer</code></div>
  </div>
</div>

[Full changelog for v2.1.139–v2.1.142 →](/docs/en/changelog#2-1-139)

---

## May 18–22, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w21.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w21.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 21 · May 18–22, 2026

> Use auto mode on the Pro plan and with Sonnet 4.6, see which skills, subagents, and MCP servers drive your plan limits in /usage, and review diffs with the new /code-review command.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-143">v2.1.143 → v2.1.149</a></span>
  <span>1 feature · May 18–22</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Auto mode on the Pro plan</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">Auto mode is now available on the Pro plan and supports Sonnet 4.6 alongside Opus. It replaces permission prompts with background safety checks: routine actions run without interrupting you, and destructive or suspicious ones are blocked and surfaced.</p>

  <p className="digest-feature-try">Update Claude Code, then cycle modes with Shift+Tab; auto mode appears in the cycle once your account meets the requirements:</p>

  ```bash terminal theme={null}
  claude update
  ```

  <p className="digest-feature-try">The command prints <code>Successfully updated</code> with the new version number, or <code>Claude Code is up to date</code> if no update is needed. Once auto mode is active, the prompt footer shows <code>auto mode on</code>.</p>

  <a className="digest-feature-link" href="/docs/en/permission-modes#eliminate-prompts-with-auto-mode">Auto mode requirements</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><a href="/docs/en/costs#track-your-costs"><code>/usage</code></a> now shows a per-category breakdown of what's driving your plan limits, attributing recent usage to skills, subagents, plugins, and individual MCP servers</div>
    <div>"Extra usage" is renamed to "usage credits" across the CLI, and <code>/extra-usage</code> is now <code>/usage-credits</code>. The old name still works. The command requires signing in with your claude.ai subscription through <code>/login</code> and isn't available with API key authentication.</div>
    <div>New <a href="/docs/en/code-review"><code>/code-review</code></a> command reports correctness bugs at a chosen effort level such as <code>/code-review high</code>, and <code>--comment</code> posts findings as inline GitHub PR comments. <code>/simplify</code> remains as a separate cleanup-only review.</div>
    <div>Background sessions now appear in <code>/resume</code> alongside interactive ones, marked with <code>bg</code>, and sessions pinned with <code>Ctrl+T</code> in <code>claude agents</code> stay alive when idle</div>
    <div><code>claude agents --json</code> lists live sessions as JSON for scripting, such as status bars and session pickers</div>
    <div>The PowerShell tool is now enabled by default on Windows for Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry users; opt out with <code>CLAUDE\_CODE\_USE\_POWERSHELL\_TOOL=0</code></div>
    <div><code>claude plugin disable</code> now refuses when another enabled plugin depends on the target, and <code>claude plugin enable</code> force-enables transitive dependencies</div>
    <div>The <code>/plugin</code> marketplace browse pane shows projected context cost, and the Discover and Browse screens list a plugin's commands, agents, skills, hooks, and MCP/LSP servers before installation</div>
    <div>New <code>worktree.bgIsolation: "none"</code> setting lets background sessions edit the working copy directly without <code>EnterWorktree</code>, for repos where worktrees are impractical</div>
    <div>Markdown output renders GFM task list checkboxes, and the <code>/diff</code> detail view scrolls with the keyboard</div>
    <div>Status line JSON input now includes GitHub repo and PR information when detected</div>
    <div>Enterprise: the <code>allowAllClaudeAiMcps</code> managed setting loads claude.ai cloud MCP connectors alongside <code>managed-mcp.json</code></div>
  </div>
</div>

[Full changelog for v2.1.143–v2.1.149 →](/docs/en/changelog#2-1-143)

---

## May 25–29, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w22.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w22.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 22 · May 25–29, 2026

> Run Claude Code on Claude Opus 4.8, orchestrate large tasks with dynamic workflows, catch security issues with the security-guidance plugin, and use fast mode on Opus 4.8 at a lower price.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-150">v2.1.150 → v2.1.157</a></span>
  <span>4 features · May 25–29</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Opus 4.8</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Opus 4.8 is now the default on Max, Team Premium, Enterprise pay-as-you-go, and the Anthropic API. It defaults to high effort; use <code>/effort xhigh</code> for harder tasks. Requires v2.1.154 or later.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/QsIrGXGFg6xd7joy/images/whats-new/opus-4-8.mp4?fit=max&auto=format&n=QsIrGXGFg6xd7joy&q=85&s=6ebcf5fe136467da2b254de1fe749ea7" data-path="images/whats-new/opus-4-8.mp4" />
  </Frame>

  <p className="digest-feature-try">Switch to Opus 4.8 by name, or pick it from the model picker:</p>

  ```text title="Claude Code" wrap theme={null}
  /model claude-opus-4-8
  ```

  <a className="digest-feature-link" href="/docs/en/model-config#available-models">Model configuration</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Dynamic workflows</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">A workflow is an orchestration script Claude writes for your task and runs across many subagents in the background. Use one when a task is too large for one conversation to coordinate: a codebase-wide audit, a large migration, a research question that needs cross-checking. Manage runs with <code>/workflows</code>.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/QsIrGXGFg6xd7joy/images/whats-new/dynamic-workflows.png?fit=max&auto=format&n=QsIrGXGFg6xd7joy&q=85&s=26671fa8607cec3453ed9753f821bd4f" alt="Claude Code on Opus 4.8 showing a Dynamic workflow requested indicator for a prompt that asks for a workflow to migrate every internal fetch() call" width="3840" height="2160" data-path="images/whats-new/dynamic-workflows.png" />
  </Frame>

  <p className="digest-feature-try">Describe the task and ask for a workflow:</p>

  ```text title="Claude Code" wrap theme={null}
  create a workflow that migrates every internal fetch() call to the new HttpClient wrapper
  ```

  <a className="digest-feature-link" href="/docs/en/workflows">Dynamic workflows</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Security guidance plugin</span>
    <span className="digest-feature-pill">plugin</span>
  </div>

  <p className="digest-feature-lede">The security-guidance plugin reviews Claude's code changes for vulnerabilities and fixes them in the same session. It runs a fast pattern check on each edit, a model review at the end of each turn, and a deeper agentic review on commit or push. Add project rules in <code>.claude/claude-security-guidance.md</code>.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/QsIrGXGFg6xd7joy/images/whats-new/security-guidance.mp4?fit=max&auto=format&n=QsIrGXGFg6xd7joy&q=85&s=c91d865936411586f42b24c558bcdd1d" data-path="images/whats-new/security-guidance.mp4" />
  </Frame>

  <p className="digest-feature-try">Install it from the official Anthropic marketplace:</p>

  ```text title="Claude Code" wrap theme={null}
  /plugin install security-guidance@claude-plugins-official
  ```

  <p className="digest-feature-try">Then activate it in the current session:</p>

  ```text title="Claude Code" wrap theme={null}
  /reload-plugins
  ```

  <a className="digest-feature-link" href="/docs/en/security-guidance">Security guidance plugin</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Fast mode on Opus 4.8</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">Fast mode now defaults to Opus 4.8 at \$10/\$50 per MTok: 2x the standard rate for about 2.5x the speed. Opus 4.7 and 4.6 stay at \$30/\$150. Opus 4.6 fast mode is deprecated.</p>

  <p className="digest-feature-try">Toggle fast mode, now on Opus 4.8:</p>

  ```text title="Claude Code" wrap theme={null}
  /fast
  ```

  <a className="digest-feature-link" href="/docs/en/fast-mode#understand-the-cost-tradeoff">Fast mode pricing</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>In <code>claude agents</code>, prefix a shell command with <code>!</code> to run it as a background job you can attach to and detach from; also available as <code>claude --bg --exec 'pytest -x'</code></div>
    <div>Plugins in <code>.claude/skills</code> directories are now loaded automatically, no marketplace required, and <code>claude plugin init \<name></code> scaffolds a new plugin</div>
    <div>New <code>/reload-skills</code> command re-scans skill directories without restarting, and <code>SessionStart</code> hooks can return <code>reloadSkills: true</code> to make skills they install available in the same session</div>
    <div>Skills and commands can set <code>disallowed-tools</code> in frontmatter to remove tools from the model while the skill is active</div>
    <div>New <code>MessageDisplay</code> hook event lets hooks transform or hide assistant message text as it is displayed</div>
    <div>Claude Code now switches to your configured <code>--fallback-model</code> for the rest of the session when the primary model is not found, instead of failing every request</div>
    <div>Plugins can declare <code>defaultEnabled: false</code> in <code>plugin.json</code> or a marketplace entry, so they install without turning on until you enable them</div>
    <div>Vim mode: <code>/</code> in NORMAL mode opens reverse history search, matching Bash and Zsh vi-mode</div>
    <div>Streaming tool execution is now always enabled, including with telemetry disabled and on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry</div>
    <div><code>←←</code> to open the agents view now works on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and with telemetry disabled</div>
    <div>Claude in Chrome: pick which connected browser to use via <code>/chrome</code> → "Select browser…", or in-chat when a browser action runs with multiple connected</div>
    <div><code>claude mcp list</code> and <code>claude mcp get</code> now show unapproved <code>.mcp.json</code> servers as pending approval instead of auto-approving and connecting when output is piped</div>
  </div>
</div>

[Full changelog for v2.1.150–v2.1.157 →](/docs/en/changelog#2-1-150)

---

## June 1–5, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w23.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w23.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 23 · June 1–5, 2026

> Run auto mode on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, prompt before writing files that can run code in acceptEdits mode, list installed plugins with /plugin list, and require an approved version range for managed deployments.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-158">v2.1.158 → v2.1.165</a></span>
  <span>4 features · June 1–5</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Auto mode on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry</span>
    <span className="digest-feature-pill">v2.1.158</span>
  </div>

  <p className="digest-feature-lede">Auto mode is now available on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry for Opus 4.7 and Opus 4.8, replacing permission prompts with background safety checks on third-party providers. Opt in by setting <code>CLAUDE\_CODE\_ENABLE\_AUTO\_MODE=1</code>.</p>

  <p className="digest-feature-try">Opt in on a third-party provider, then cycle to auto mode with Shift+Tab:</p>

  ```bash terminal theme={null}
  export CLAUDE_CODE_ENABLE_AUTO_MODE=1
  ```

  <a className="digest-feature-link" href="/docs/en/permission-modes#enable-auto-mode-on-bedrock-agent-platform-or-foundry">Auto mode on third-party providers</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Safer automatic edits</span>
    <span className="digest-feature-pill">v2.1.160</span>
  </div>

  <p className="digest-feature-lede">Claude Code now prompts before writing files that can run code, even in <code>acceptEdits</code> mode. The protected set covers shell startup files such as <code>.zshenv</code> and <code>.bash\_login</code>, git config under <code>\~/.config/git/</code>, and build-tool configs such as <code>.npmrc</code>, <code>.bazelrc</code>, and <code>.pre-commit-config.yaml</code>. These writes are never auto-approved in any mode except <code>bypassPermissions</code>.</p>

  <p className="digest-feature-try">Work in acceptEdits mode; Claude now pauses before writing these files:</p>

  ```bash terminal theme={null}
  claude --permission-mode acceptEdits
  ```

  <a className="digest-feature-link" href="/docs/en/permission-modes#protected-paths">Protected paths</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">List installed plugins with /plugin list</span>
    <span className="digest-feature-pill">v2.1.163</span>
  </div>

  <p className="digest-feature-lede">The new <code>/plugin list</code> command prints your installed plugins inline, without opening the <code>/plugin</code> menu, and is also available as <code>claude plugin list</code> from the shell. In the interactive form, add `--enabled` or `--disabled` to show only plugins in that state.</p>

  <p className="digest-feature-try">List the plugins that are currently turned on:</p>

  ```text Claude Code theme={null}
  > /plugin list --enabled
  ```

  <a className="digest-feature-link" href="/docs/en/plugins-reference#plugin-list">Plugin commands</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Version requirements for managed deployments</span>
    <span className="digest-feature-pill">v2.1.163</span>
  </div>

  <p className="digest-feature-lede">Two managed settings, <code>requiredMinimumVersion</code> and <code>requiredMaximumVersion</code>, let your organization require an approved Claude Code version range. A client outside the range exits at startup and tells the user to update through the organization's method. <code>claude update</code>, <code>claude install</code>, and <code>claude doctor</code> keep working so users can still recover.</p>

  <p className="digest-feature-try">Add a floor to your managed settings so older clients refuse to start:</p>

  ```json managed-settings.json theme={null}
  {
    "requiredMinimumVersion": "2.1.163"
  }
  ```

  <a className="digest-feature-link" href="/docs/en/admin-setup#decide-what-to-enforce">Decide what to enforce</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>The trigger keyword for <a href="/docs/en/workflows">dynamic workflows</a> changed from <code>workflow</code> to <code>ultracode</code>; asking for a workflow in your own words still works, and the keyword is highlighted in violet in the prompt</div>
    <div><a href="/docs/en/hooks">Stop and SubagentStop hooks</a> can return <code>hookSpecificOutput.additionalContext</code> to give Claude feedback and keep the turn going instead of being treated as an error</div>
    <div><code>claude mcp</code> list, get, and add no longer print secrets: environment-variable references are not expanded, and credential headers and URL secrets are redacted</div>
    <div>A failed Bash command in a parallel tool batch no longer cancels the others; each tool returns its own result independently</div>
    <div>Editing a file no longer needs a separate Read first when you viewed it with a single-file <code>grep</code>, <code>egrep</code>, or <code>fgrep</code></div>
    <div>Clicking a command in the autocomplete menu now fills it into your prompt instead of running it immediately; press Enter to run</div>
    <div>Listing <code>Grep</code> or <code>Glob</code> in `--tools` now provides the dedicated search tools on native builds with embedded search, instead of silently ignoring those names</div>
    <div><code>/effort</code> now confirms when your chosen level will persist as the default for new sessions</div>
    <div><code>OTEL\_RESOURCE\_ATTRIBUTES</code> values are now attached as labels on metric datapoints, so you can slice usage metrics by custom dimensions like team or repo</div>
    <div>Windsurf is renamed to Devin Desktop in <code>/ide</code>, <code>/terminal-setup</code>, and <code>/scroll-speed</code>, following the editor's rebrand</div>
    <div><code>/btw</code> gains a <code>c to copy</code> shortcut that copies the raw markdown answer to the clipboard</div>
  </div>
</div>

[Full changelog for v2.1.158–v2.1.165 →](/docs/en/changelog#2-1-158)

---

## June 8–12, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w24.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w24.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 24 · June 8–12, 2026

> Move a session to a new directory with /cd, let subagents spawn their own subagents, and troubleshoot a broken configuration with safe mode.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-166">v2.1.166 → v2.1.176</a></span>
  <span>3 features · June 8–12</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Move a session with /cd</span>
    <span className="digest-feature-pill">v2.1.169</span>
  </div>

  <p className="digest-feature-lede">The new <code>/cd</code> command moves the current session to a different working directory without rebuilding the prompt cache: the new directory's <code>CLAUDE.md</code> is appended as a message instead of replacing the system prompt. The session relocates to the new directory's project storage, so `--resume` and `--continue` find it there. Claude prompts you to trust the directory if you haven't worked in it before.</p>

  <p className="digest-feature-try">Move the session into another project without restarting:</p>

  ```text Claude Code theme={null}
  > /cd ../other-project
  ```

  <a className="digest-feature-link" href="/docs/en/commands#all-commands">Commands reference</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Subagents can spawn subagents</span>
    <span className="digest-feature-pill">v2.1.172</span>
  </div>

  <p className="digest-feature-lede">Subagents can now spawn their own subagents. The subagent panel below the prompt shows the full tree: each row carries a count of its descendants and a path back to <code>main</code>. Subagent chains are capped at five levels deep to prevent runaway concurrent trees.</p>

  <p className="digest-feature-try">Open the agents view to watch the nested tree as work fans out:</p>

  ```text Claude Code theme={null}
  > /agents
  ```

  <a className="digest-feature-link" href="/docs/en/sub-agents#let-subagents-spawn-their-own-subagents">Spawn nested subagents</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Troubleshoot with safe mode</span>
    <span className="digest-feature-pill">v2.1.169</span>
  </div>

  <p className="digest-feature-lede">Start Claude Code with `--safe-mode`, or set <code>CLAUDE\_CODE\_SAFE\_MODE</code>, to launch with all customizations disabled: <code>CLAUDE.md</code>, skills, plugins, hooks, MCP servers, and custom commands and agents do not load. Authentication, model selection, built-in tools, and permissions still work. If a problem disappears in safe mode, one of those surfaces is the cause.</p>

  <p className="digest-feature-try">Launch a clean session to isolate a broken configuration:</p>

  ```bash terminal theme={null}
  claude --safe-mode
  ```

  <a className="digest-feature-link" href="/docs/en/debug-your-config#test-against-a-clean-configuration">Test against a clean configuration</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><a href="/docs/en/model-config#fallback-model-chains"><code>fallbackModel</code></a> configures up to three fallback models tried in order when the primary is overloaded or unavailable, and `--fallback-model` now applies to interactive sessions too</div>
    <div>Session titles are now generated in the language of your conversation; pin a specific one with the <code>language</code> setting</div>
    <div>`claude agents --json` adds `--all` to include completed sessions plus new <code>id</code> and <code>state</code> fields, and no longer omits blocked or newly dispatched sessions</div>
    <div>Browsing a marketplace's plugins in <code>/plugin</code> now has a search bar</div>
    <div>New <code>disableBundledSkills</code> setting and <code>CLAUDE\_CODE\_DISABLE\_BUNDLED\_SKILLS</code> hide bundled skills, workflows, and built-in commands from the model</div>
    <div>Deny rules accept a glob in the tool-name position, so <code>"\*"</code> denies all tools, and unknown tool names in deny rules now warn at startup</div>
    <div>Agent messaging is hardened: messages relayed via <code>SendMessage</code> from other agents no longer carry user authority, and auto mode blocks them</div>
    <div>Amazon Bedrock reads the AWS region from <code>\~/.aws</code> config files when <code>AWS\_REGION</code> is unset, and <code>/status</code> shows where the region came from</div>
    <div>New <code>enforceAvailableModels</code> managed setting makes the <code>availableModels</code> allowlist also constrain the Default model</div>
    <div>Claude in Chrome browser tools now load in a single batched call instead of one per tool</div>
    <div><code>claude update</code> announces the target version before downloading instead of going silent</div>
    <div>New <code>footerLinksRegexes</code> setting adds regex-matched link badges to the footer row</div>
  </div>
</div>

[Full changelog for v2.1.166–v2.1.176 →](/docs/en/changelog#2-1-166)

---

## June 15–19, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w25.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w25.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 25 · June 15–19, 2026

> Publish a live, shareable page from your session with Artifacts, match tool parameters in deny and ask rules, and set any setting from the prompt with /config.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-178">v2.1.178 → v2.1.183</a></span>
  <span>3 features · June 15–19</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Artifacts</span>
  </div>

  <p className="digest-feature-lede">An artifact is a live, interactive page that Claude Code publishes from your session to a private URL on claude.ai, and it updates in place as the session keeps working. Ask for one when terminal text is the wrong medium, such as a PR walkthrough with the diff annotated inline or a dashboard built from session data. Artifacts are in beta on Team and Enterprise plans.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/1ylKDoQynT1UgfEK/images/whats-new/artifacts.mp4?fit=max&auto=format&n=1ylKDoQynT1UgfEK&q=85&s=7f5391559d2bc69989621b36322fcff1" data-path="images/whats-new/artifacts.mp4" />
  </Frame>

  <p className="digest-feature-try">Ask Claude for a page, then approve the publish prompt:</p>

  ```text title="Claude Code" wrap theme={null}
  Make an artifact that walks through this PR with the diff annotated inline.
  ```

  <a className="digest-feature-link" href="/docs/en/artifacts#create-an-artifact">Create an artifact</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Match by input parameter</span>
    <span className="digest-feature-pill">v2.1.178</span>
  </div>

  <p className="digest-feature-lede">Deny and ask permission rules can now match a tool's input parameters with the <code>Tool(param:value)</code> syntax. For example, <code>Agent(model:opus)</code> matches subagent spawns that request the Opus model tier. The value accepts `*` as a wildcard, so `Agent(isolation:*)` matches any explicit isolation value.</p>

  <p className="digest-feature-try">Add a parameter rule to the deny list in <code>settings.json</code>:</p>

  ```json .claude/settings.json {3} theme={null}
  {
    "permissions": {
      "deny": ["Agent(model:opus)"]
    }
  }
  ```

  <a className="digest-feature-link" href="/docs/en/permissions#match-by-input-parameter">Match by input parameter</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Set any setting from the prompt</span>
    <span className="digest-feature-pill">v2.1.181</span>
  </div>

  <p className="digest-feature-lede">Pass <code>key=value</code> to <code>/config</code> to change a setting directly without opening the Settings interface. The syntax also works in non-interactive mode with the <code>-p</code> flag and from Remote Control.</p>

  <p className="digest-feature-try">Set the <code>thinking</code> setting from the prompt:</p>

  ```text title="Claude Code" wrap theme={null}
  /config thinking=false
  ```

  <a className="digest-feature-link" href="/docs/en/commands#all-commands">Commands reference</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Auto mode now blocks destructive git commands (`git reset --hard`, `git clean -fd`, `git stash drop`) when you didn't ask to discard local work, and blocks <code>terraform destroy</code> unless you asked for the specific stack</div>
    <div>Set the new <code>attribution.sessionUrl</code> setting to <code>false</code> to omit the claude.ai session link from commits and PRs in web and Remote Control sessions</div>
    <div>In the <code>/config</code> interface, Enter and Space both change the selected setting, and Esc now saves and closes instead of reverting</div>
    <div>New <code>sandbox.allowAppleEvents</code> opt-in setting lets sandboxed commands send Apple Events on macOS</div>
    <div>Point <code>CLAUDE\_CLIENT\_PRESENCE\_FILE</code> at a marker file to suppress mobile push notifications while you're at the machine</div>
    <div>Long paragraphs now stream line by line instead of waiting for the first line break</div>
    <div>API connection drops mid-thinking now retry automatically instead of showing "Connection closed while thinking"</div>
    <div>With <code>CLAUDE\_CODE\_EXPERIMENTAL\_AGENT\_TEAMS=1</code> set, every session has one implicit team, so you spawn teammates directly with the Agent tool's <code>name</code> parameter</div>
    <div>Skills in nested <code>.claude/skills</code> directories load when working on files there; on a name clash the nested skill appears as `<dir>:<name>` so both stay available</div>
    <div>Fixed prompt caching not reading on a custom <code>ANTHROPIC\_BASE\_URL</code> and on Microsoft Foundry</div>
    <div>Fixed Write and Edit producing zero-byte or truncated files on network drives and cloud-synced folders</div>
  </div>
</div>

[Full changelog for v2.1.178–v2.1.183 →](/docs/en/changelog#2-1-178)

---

## June 22–26, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w26.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w26.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 26 · June 22–26, 2026

> Authenticate MCP servers from your shell with claude mcp login, get a response to shell mode command output with the ! prefix, and resume a conversation from before /clear with /rewind.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-185">v2.1.185 → v2.1.193</a></span>
  <span>2 features · June 22–26</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Authenticate MCP servers from the CLI</span>
    <span className="digest-feature-pill">v2.1.186</span>
  </div>

  <p className="digest-feature-lede">New `claude mcp login <name>` and `claude mcp logout <name>` commands authenticate a configured MCP server from your shell instead of the interactive <code>/mcp</code> menu. `claude mcp login` runs the server's OAuth flow directly, and `claude mcp logout` clears the stored credentials.</p>

  <p className="digest-feature-try">Run the OAuth flow for a configured server without opening a session:</p>

  ```bash terminal theme={null}
  claude mcp login sentry
  ```

  <a className="digest-feature-link" href="/docs/en/mcp#authenticate-from-the-command-line">Authenticate from the command line</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Shell mode responds to command output</span>
    <span className="digest-feature-pill">v2.1.186</span>
  </div>

  <p className="digest-feature-lede">Commands you run with the <code>!</code> prefix now get a response from Claude once the output lands in the transcript, so you can run <code>! npm test</code> and get an explanation of the failures without a second prompt. The response costs the same as sending a normal prompt. To keep the earlier behavior, where the output is added to context without a response, set <code>respondToBashCommands</code> to <code>false</code> in <code>settings.json</code>.</p>

  <p className="digest-feature-try">Run a command and get a response to its output:</p>

  ```text Claude Code theme={null}
  > ! npm test
  ```

  <a className="digest-feature-link" href="/docs/en/interactive-mode#shell-mode-with-prefix">Shell mode with the ! prefix</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><code>/rewind</code> can now resume a conversation from before <code>/clear</code> was run</div>
    <div>New <code>sandbox.credentials</code> setting blocks sandboxed commands from reading credential files and secret environment variables</div>
    <div>Org-configured model restrictions now apply to the model picker, `--model`, <code>/model</code>, and <code>ANTHROPIC\_MODEL</code>, with a "restricted by your organization's settings" message when a restricted model is selected</div>
    <div>New <code>autoMode.classifyAllShell</code> setting routes all Bash and PowerShell commands through the auto-mode classifier, and denial reasons now show in the transcript, the denial toast, and <code>/permissions</code></div>
    <div>New <code>claude\_code.assistant\_response</code> OpenTelemetry log event carries the model's response text; deployments that already log prompt content start receiving it on upgrade, so set <code>OTEL\_LOG\_ASSISTANT\_RESPONSES=0</code> to keep prompts only</div>
    <div>Background subagents now surface permission prompts in the main session instead of auto-denying; the dialog shows which agent is asking, and Esc denies only that tool</div>
    <div><code>/install-github-app</code> can now install only the GitHub App and skip the Actions workflow and secret steps</div>
    <div>Hosts you allow in the sandbox network permission dialog are remembered for the rest of the session instead of re-prompting on every connection</div>
    <div>Streaming responses use about 37% less CPU, and long-session memory growth from the terminal output cache is reduced</div>
    <div>`/review <pr>` now uses the same review engine as <code>/code-review medium</code></div>
    <div>Bash mode <code>!</code> commands get live file path autocomplete</div>
  </div>
</div>

[Full changelog for v2.1.185–v2.1.193 →](/docs/en/changelog#2-1-185)

---

## June 29 – July 3, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w27.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w27.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 27 · June 29 – July 3, 2026

> Claude Sonnet 5 becomes the default model, Claude in Chrome reaches general availability, subagents run in the background by default, Claude Desktop arrives on Linux in beta, and /radio tunes into Claude FM.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-195">v2.1.195 → v2.1.201</a></span>
  <span>5 features · June 29 – July 3</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Sonnet 5</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Sonnet 5 is the new default model for Pro, Team Standard, and Enterprise subscription seats: top-tier coding and tool use at Sonnet pricing, with a native 1M-token context window and adaptive thinking on by default. API pricing is promotional at \$2/\$10 per MTok through August 31. Requires v2.1.197 or later.</p>

  <p className="digest-feature-try">Switch to Sonnet 5 by name, or pick it from the model picker:</p>

  ```text Claude Code theme={null}
  > /model claude-sonnet-5
  ```

  <a className="digest-feature-link" href="/docs/en/model-config#available-models">Model configuration</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude in Chrome is generally available</span>
    <span className="digest-feature-pill">v2.1.198</span>
  </div>

  <p className="digest-feature-lede">The Chrome integration is out of preview for everyone on a direct Anthropic plan. Claude Code drives your browser through the Claude in Chrome extension: it opens tabs, clicks through pages, fills forms, reads console logs, and shares your login state, so it can test the app it builds without you switching contexts.</p>

  <a className="digest-feature-link" href="/docs/en/chrome">Use Claude Code with Chrome</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Subagents run in the background by default</span>
    <span className="digest-feature-pill">v2.1.198</span>
  </div>

  <p className="digest-feature-lede">Claude now keeps working while subagents run and picks up their results when they finish, instead of pausing the conversation to wait. Claude still runs a subagent in the foreground when it needs the result before continuing, and background subagents surface every permission prompt in your main session. Pin a subagent's behavior with the <code>background</code> frontmatter field.</p>

  <a className="digest-feature-link" href="/docs/en/sub-agents#run-subagents-in-foreground-or-background">Run subagents in foreground or background</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Desktop on Linux</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">The Claude desktop app is now available on Ubuntu 22.04+ and Debian 12+ in beta, on x86\_64 and arm64. You get the same Chat, Cowork, and Claude Code experience as macOS and Windows: parallel sessions, visual diff review, an integrated terminal and editor, and live app preview. Installs from Anthropic's apt repository, so updates arrive through regular package updates.</p>

  <a className="digest-feature-link" href="/docs/en/desktop-linux">Claude Desktop on Linux</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/radio</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">Claude FM is on the air. <code>/radio</code> opens the lo-fi radio stream in your browser for something to code to, and prints the stream URL when no browser is available. Not available on Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/x358isu_VzLnyTEN/images/whats-new/radio.mp4?fit=max&auto=format&n=x358isu_VzLnyTEN&q=85&s=36a0c33859cef119c7192dceea8bcbd3" data-path="images/whats-new/radio.mp4" />
  </Frame>

  <p className="digest-feature-try">Tune in from any session:</p>

  ```text Claude Code theme={null}
  > /radio
  ```

  <a className="digest-feature-link" href="/docs/en/commands#all-commands">All commands</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><a href="/docs/en/artifacts">Artifacts</a> are now generally available and included on Pro and Max plans, joining Team and Enterprise</div>
    <div>Admins can set an <a href="/docs/en/model-config#organization-default-model">organization default model</a> in the org console; it shows as "Org default" in <code>/model</code> when you haven't picked a model yourself</div>
    <div>Stacked skill invocations like <code>/skill-a /skill-b do XYZ</code> now load all leading skills (up to 5), not only the first</div>
    <div><code>AskUserQuestion</code> dialogs no longer auto-continue by default; opt into an idle timeout via <code>/config</code></div>
    <div>The "default" permission mode is now named "Manual" across the CLI, `--help`, VS Code, and JetBrains; `--permission-mode manual` is accepted alongside `default`</div>
    <div>New <code>/dataviz</code> skill gives chart and dashboard design guidance, with a runnable color-palette validator</div>
    <div>The built-in Explore agent now inherits the main session's model (capped at Opus) instead of running on Haiku</div>
    <div>Background agents launched from <code>claude agents</code> now commit, push, and open a draft PR when they finish code work in a worktree, instead of stopping to ask</div>
    <div>Hook matchers with hyphenated identifiers like <code>code-reviewer</code> now exact-match instead of substring-matching; use <code>mcp\_\_brave-search\_\_.\*</code> to match all tools from a hyphenated MCP server</div>
    <div>Transient server rate-limit errors unrelated to your usage limit are now retried automatically with backoff for subscribers instead of failing the turn</div>
    <div>The streaming idle watchdog is now on by default for all providers: it aborts and retries when a response stream produces no events for 5 minutes (<code>CLAUDE\_ENABLE\_STREAM\_WATCHDOG=0</code> to disable)</div>
  </div>
</div>

[Full changelog for v2.1.195–v2.1.201 →](/docs/en/changelog#2-1-195)

---

## July 6–10, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w28.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w28.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 28 · July 6–10, 2026

> Browse external sites from the Desktop app's built-in browser, run a full setup checkup with /doctor, and pick up auto mode transcript protections and agent view upgrades.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-202">v2.1.202 → v2.1.206</a></span>
  <span>2 features · July 6–10</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">In-app browser on Desktop</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">Claude Code on desktop now has a built-in browser. Claude can pull up docs, designs, or any other site, and read, click through, and interact with pages the same way it does with your local dev server previews. The browser is sandboxed and configurable: you choose whether browsing sessions persist, and safety classifiers review actions on external sites.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/x358isu_VzLnyTEN/images/whats-new/desktop-browser.mp4?fit=max&auto=format&n=x358isu_VzLnyTEN&q=85&s=8033e85a1cb0a37870a79e702c18f4e4" data-path="images/whats-new/desktop-browser.mp4" />
  </Frame>

  <a className="digest-feature-link" href="/docs/en/desktop#browse-external-sites">Browse external sites</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/doctor is a full setup checkup</span>
    <span className="digest-feature-pill">v2.1.205</span>
  </div>

  <p className="digest-feature-lede"><code>/doctor</code> now diagnoses issues and can fix them, instead of printing a read-only report. It checks installation health, finds unused skills, MCP servers, and plugins versus their context cost, deduplicates local <code>CLAUDE.md</code> files against checked-in ones, proposes trimming <code>CLAUDE.md</code> content Claude could derive from the codebase, and flags slow hooks. It reports findings first and asks for confirmation before changing anything. <code>/checkup</code> is its alias.</p>

  <p className="digest-feature-try">Run a checkup from any session:</p>

  ```text Claude Code theme={null}
  > /doctor
  ```

  <a className="digest-feature-link" href="/docs/en/commands#all-commands">All commands</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Auto mode now blocks tampering with session transcript files, and asks before running <code>rm -rf</code> on a variable it can't resolve from context</div>
    <div><code>/cd</code> now suggests directory paths as you type, matching <code>/add-dir</code></div>
    <div><code>/commit-push-pr</code> auto-allows <code>git push</code> to the repo's configured push remote in addition to <code>origin</code></div>
    <div>Gateway: <code>/login</code> now supports Anthropic-operated public gateway endpoints</div>
    <div><code>EnterWorktree</code> asks for confirmation before entering a git worktree outside the project's <code>.claude/worktrees/</code> directory</div>
    <div>Background agents upgrade to a new version in the background right after a Claude Code update, instead of paying a slow stale-session upgrade when you attach</div>
    <div>Agent view rows now show a colored state word and a classifier-written headline instead of raw tool call text, and sessions that edit, merge, comment on, or push to an existing PR link it in <code>claude agents</code></div>
    <div>Auto-update binary downloads now stream to disk instead of buffering in memory, cutting the updater's peak memory usage by roughly 400 MB</div>
    <div>Background task notifications now explicitly state that no human input has occurred, preventing fabricated in-transcript approvals from being acted on</div>
    <div>Improved <code>/code-review</code> findings quality on Opus 4.8 across all effort levels</div>
  </div>
</div>

[Full changelog for v2.1.202–v2.1.206 →](/docs/en/changelog#2-1-202)

---

## July 13–17, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w29.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w29.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 29 · July 13–17, 2026

> Pull live data into published artifacts through MCP connectors, and use Claude Code with a screen reader in the new screen reader mode.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-207">v2.1.207 → v2.1.212</a></span>
  <span>2 features · July 13–17</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Artifacts call your MCP connectors</span>
    <span className="digest-feature-pill">web</span>
  </div>

  <p className="digest-feature-lede">A published artifact can now call MCP connectors each time someone views it, so a dashboard shows live data and can take actions on demand rather than a snapshot from the session that built it. Each call runs through the viewing account's own connections, and viewers approve access before the page's first connector call. This week also adds public sharing links, editor roles for shared editing on Team and Enterprise plans, and artifacts created from Claude Tag sessions.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/ItzF3QVI6L0QypjJ/images/whats-new/artifacts-mcp.mp4?fit=max&auto=format&n=ItzF3QVI6L0QypjJ&q=85&s=ff8b81ed52b26c773899dc28cec959e6" data-path="images/whats-new/artifacts-mcp.mp4" />
  </Frame>

  <p className="digest-feature-try">Name the connector and the data you want in your prompt:</p>

  ```text title="Claude Code" wrap theme={null}
  Build a dashboard artifact of open pull requests that pulls the live list through my GitHub connector when the page loads.
  ```

  <a className="digest-feature-link" href="/docs/en/artifacts#pull-live-data-with-mcp-connectors">Pull live data with MCP connectors</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Screen reader mode</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">Screen reader mode replaces the visual terminal interface with plain, linear text: instead of boxes, spinners, and in-place redraws, Claude Code prints labeled lines that a screen reader such as VoiceOver or NVDA reads in order, so you can approve permissions and review output end to end. Turn it on per session with a flag, per shell with the <code>CLAUDE\_AX\_SCREEN\_READER</code> environment variable, or everywhere with the <code>axScreenReader</code> setting.</p>

  <p className="digest-feature-try">Start a session in screen reader mode:</p>

  ```bash terminal theme={null}
  claude --ax-screen-reader
  ```

  <a className="digest-feature-link" href="/docs/en/accessibility#turn-on-screen-reader-mode">Turn on screen reader mode</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><code>/fork</code> now copies your conversation into a new background session with its own row in <code>claude agents</code> while you keep working; the in-session forked subagent it used to launch is now <code>/subtask</code></div>
    <div><a href="/docs/en/permission-modes#enable-auto-mode-on-bedrock-agent-platform-or-foundry">Auto mode</a> no longer needs the <code>CLAUDE\_CODE\_ENABLE\_AUTO\_MODE</code> opt-in on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry; administrators can turn it off with <code>disableAutoMode</code></div>
    <div>MCP tool calls that run longer than two minutes now move to the background automatically so the session stays usable; tune or disable the threshold with <code>CLAUDE\_CODE\_MCP\_AUTO\_BACKGROUND\_MS</code></div>
    <div>New <code>claude auto-mode reset</code> restores the default auto-mode configuration, and `--yes` skips the confirmation prompt</div>
    <div>New <a href="/docs/en/corporate-launcher">corporate launcher</a> support: <code>CLAUDE\_CODE\_PROCESS\_WRAPPER</code> or the <code>processWrapper</code> setting runs the processes Claude Code starts from its own binary, such as the background service and agent view sessions, through a required wrapper executable</div>
    <div><code>vimInsertModeRemaps</code> setting maps two-key insert-mode sequences such as <code>jj</code> to Escape in vim mode</div>
    <div>`--forward-subagent-text` and <code>CLAUDE\_CODE\_FORWARD\_SUBAGENT\_TEXT</code> include subagent text and thinking blocks in <a href="/docs/en/headless">stream-json output</a></div>
    <div>Session-wide caps stop runaway loops: WebSearch calls and subagent spawns each default to 200, tunable with <code>CLAUDE\_CODE\_MAX\_WEB\_SEARCHES\_PER\_SESSION</code> and <code>CLAUDE\_CODE\_MAX\_SUBAGENTS\_PER\_SESSION</code></div>
    <div>"Always allow" permission rules save at the repository root, so approvals granted in a git worktree persist across sessions and worktrees</div>
    <div>Amazon Bedrock, Google Cloud's Agent Platform, and Claude Platform on AWS now default to Claude Opus 4.8</div>
    <div>The collapsed tool summary line shows a live elapsed-time counter, so long-running tool calls visibly tick instead of looking stuck</div>
  </div>
</div>

[Full changelog for v2.1.207–v2.1.212 →](/docs/en/changelog#2-1-207)

---

## July 20–24, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w30.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w30.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 30 · July 20–24, 2026

> Opus 5 becomes the default Opus model, Claude Code Desktop adds an iOS Simulator pane, and the Claude Security plugin scans your code for vulnerabilities.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-214">v2.1.214 → v2.1.219</a></span>
  <span>3 features · July 20–24</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Opus 5</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Claude Opus 5 is the new default Opus model in Claude Code. It's the default on Max, Team Premium, Enterprise pay-as-you-go, and the Anthropic API, and on Claude Platform on AWS, Amazon Bedrock, and Google Cloud's Agent Platform. On the Anthropic API and on Max, Team, and Enterprise plans, Opus 5 runs with a <a href="/docs/en/model-config#extended-context">1M-token context window</a>; on Amazon Bedrock and Google Cloud's Agent Platform, select the 1M model variant. Fast mode moves to Opus 5 at \$10/\$50 per MTok. Requires v2.1.219 or later.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/N3yEaTYPXMXFrF6k/images/whats-new/opus-5.mp4?fit=max&auto=format&n=N3yEaTYPXMXFrF6k&q=85&s=8536b1cb3180e539008f39930403e47b" data-path="images/whats-new/opus-5.mp4" />
  </Frame>

  <p className="digest-feature-try">Switch to Opus 5 by name, or pick it from the model picker:</p>

  ```text Claude Code theme={null}
  > /model claude-opus-5
  ```

  <a className="digest-feature-link" href="/docs/en/model-config#available-models">Model configuration</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">iOS Simulator in Claude Code Desktop</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">Claude Code Desktop on macOS gets an iOS Simulator pane, in public beta on Pro, Max, and Team plans. When Claude builds, launches, or checks your app in a simulator, the pane opens next to the conversation and streams the device screen live, so you can watch Claude tap through the app to verify its changes or drive the device yourself. Requires Xcode with the iOS platform installed, and Claude Desktop v1.24012.0 or later.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/N3yEaTYPXMXFrF6k/images/whats-new/ios-simulator.jpg?fit=max&auto=format&n=N3yEaTYPXMXFrF6k&q=85&s=6c88418ed14ed0fb12cc1af75b17f2ee" alt="Claude Code Desktop with the iOS Simulator pane showing an iPhone app next to the conversation" width="2048" height="1152" data-path="images/whats-new/ios-simulator.jpg" />
  </Frame>

  <p className="digest-feature-try">Ask Claude to run or test your app, and the pane opens when the app launches:</p>

  ```text Claude Code theme={null}
  > Build the app and run it in the simulator to check the onboarding flow.
  ```

  <a className="digest-feature-link" href="/docs/en/desktop-ios-simulator#run-your-app-in-the-simulator">Test iOS apps in the simulator</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Security plugin</span>
    <span className="digest-feature-pill">plugin</span>
  </div>

  <p className="digest-feature-lede">The Claude Security plugin runs a multi-agent vulnerability scan of your codebase inside a Claude Code session: agents map your architecture, build a threat model, hunt for vulnerabilities, and independently review every finding before writing the report to a <code>CLAUDE-SECURITY-\<timestamp>/</code> directory. Scan a whole repository or only a branch's diff, a pull request, or a single commit, then turn the findings you choose into reviewed patches that you apply yourself.</p>

  <p className="digest-feature-try">Install the plugin from the official Anthropic marketplace, run <code>/reload-plugins</code>, then start a scan with <code>/claude-security</code>:</p>

  ```text Claude Code theme={null}
  > /plugin install claude-security@claude-plugins-official
  ```

  <a className="digest-feature-link" href="/docs/en/claude-security#scan-and-fix-your-codebase">Scan and fix your codebase</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div><a href="/docs/en/code-review#review-a-diff-locally"><code>/code-review</code></a> now runs as a background subagent with its own context window, so review work stays out of your conversation and the findings arrive when it completes</div>
    <div><code>/verify</code>, <code>/code-review</code>, and <code>/deep-research</code> run only when you invoke them; Claude no longer launches them on its own</div>
    <div><a href="/docs/en/interactive-mode#emoji-shortcodes">Emoji shortcodes</a> autocomplete in the prompt input: type <code>:heart:</code> to insert an emoji, or two or more characters after <code>:</code> for suggestions; turn it off with <code>emojiCompletionEnabled</code></div>
    <div>Skills with <code>context: fork</code> <a href="/docs/en/skills#run-skills-in-a-subagent">run in the background</a> by default, and <code>background: false</code> in the skill's frontmatter waits for the result in the same turn</div>
    <div>A session runs up to 20 subagents concurrently by default; change the <a href="/docs/en/sub-agents#concurrent-subagent-limit">limit</a> with <code>CLAUDE\_CODE\_MAX\_CONCURRENT\_SUBAGENTS</code></div>
    <div>`--max-budget-usd` now enforces the cap on subagents: once spend reaches it, Claude can't start more and running background subagents stop</div>
    <div>New <a href="/docs/en/sandboxing#disable-filesystem-isolation"><code>sandbox.filesystem.disabled</code></a> setting skips filesystem isolation while keeping network egress control</div>
    <div>In auto mode, the checks for dangerous <code>rm</code> commands, background jobs, and suspicious Windows paths no longer open permission dialogs; the auto-mode classifier adjudicates them instead</div>
    <div>Bash permission checks fail closed on more shell forms, including file-descriptor redirects, Zsh variable subscripts in <code>\[\[ ]]</code> comparisons, <code>help</code> and <code>man</code> invocations that could run unsafe options, and commands over 10,000 characters</div>
    <div><a href="/docs/en/fast-mode">Fast mode</a> no longer supports Opus 4.7: <code>/fast</code> now applies to Opus 5 and Opus 4.8</div>
    <div>Long-running tool calls emit a periodic progress heartbeat instead of going silent</div>
  </div>
</div>

[Full changelog for v2.1.214–v2.1.219 →](/docs/en/changelog#2-1-214)

---

## August 3–7, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w32.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w32.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 32 · August 3–7, 2026

> Claude Code sessions message each other, self-hosted environments run cloud sessions on your infrastructure, and auto mode becomes the default permission mode.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-220">v2.1.220 → v2.1.224</a></span>
  <span>3 features · August 3–7</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Cross-session messaging</span>
    <span className="digest-feature-pill">v2.1.224</span>
  </div>

  <p className="digest-feature-lede">Your Claude Code sessions can now message each other. Claude discovers your other sessions with the <code>ListAgents</code> tool and sends with <code>SendMessage</code>, either when you ask it to or on its own, such as after a change in one session affects what another is working on. A message is text Claude writes for the other session, never your conversation history or files. Available on macOS and Linux. Requires v2.1.224 or later.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/N3yEaTYPXMXFrF6k/images/whats-new/cross-session-messaging.mp4?fit=max&auto=format&n=N3yEaTYPXMXFrF6k&q=85&s=8f33c3390f78660a4a26dc980f46159f" data-path="images/whats-new/cross-session-messaging.mp4" />
  </Frame>

  <p className="digest-feature-try">With two sessions open on the same machine, ask one of them to pass something along:</p>

  ```text title="Claude Code" wrap theme={null}
  Tell the session working on the payments API that users.name is now users.display_name
  ```

  <p className="digest-feature-try">The other session shows a <code>Message from</code> row once Claude has read the message; press <code>Ctrl+O</code> to expand it. To see which sessions Claude can reach, run <code>/list-agents</code>.</p>

  <a className="digest-feature-link" href="/docs/en/cross-session-messaging#message-another-session">Message another session</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Self-hosted environments</span>
    <span className="digest-feature-pill">v2.1.224</span>
  </div>

  <p className="digest-feature-lede">Self-hosted environments run Claude Code cloud sessions on your organization's own infrastructure, in public beta on Team and Enterprise plans. Run <code>claude self-hosted-runner</code> on your machines or containers to turn them into runners. When someone picks your environment while starting a session from claude.ai, the mobile or desktop apps, or `claude --cloud`, that session runs inside your network, with access to your internal services. An Owner turns on <strong>Allow self-hosted environments</strong> in <a href="https://claude.ai/admin-settings/cloud-environments">admin settings</a> first.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/N3yEaTYPXMXFrF6k/images/whats-new/self-hosted-environments.jpg?fit=max&auto=format&n=N3yEaTYPXMXFrF6k&q=85&s=ae9152cb1670c8af517d1aee57689b14" alt="The self-hosted environments admin page listing environments such as linux-dev and macos-prod with their status and active session counts" width="2048" height="1152" data-path="images/whats-new/self-hosted-environments.jpg" />
  </Frame>

  <p className="digest-feature-try">Signed in as an Owner, run the guided setup, which walks you through creating the environment and starts a runner:</p>

  ```bash terminal theme={null}
  claude self-hosted-runner setup
  ```

  <p className="digest-feature-try">The environment shows <strong>Healthy</strong> in admin settings once the runner registers.</p>

  <a className="digest-feature-link" href="/docs/en/self-hosted-environments-quickstart#set-up-an-environment-and-runner">Self-hosted environments quickstart</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Auto mode becomes the default</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">Starting August 14, auto mode is the default permission mode for new sessions on Pro, Max, and Team plans. If you set a default mode yourself, it stays in place unless you accept the one-time switch prompt, and a default your organization manages doesn't change. You can still switch modes at any time. Already in effect on those plans: the classifier calls auto mode makes no longer count toward your usage limits.</p>

  <p className="digest-feature-try">To start every session in auto mode before the switch, set it as your default in your user settings:</p>

  ```json ~/.claude/settings.json {3} theme={null}
  {
    "permissions": {
      "defaultMode": "auto"
    }
  }
  ```

  <p className="digest-feature-try">New sessions then show <code>auto mode on</code> in the status bar.</p>

  <a className="digest-feature-link" href="/docs/en/permission-modes#eliminate-prompts-with-auto-mode">Auto mode requirements and controls</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>The VS Code extension gets <a href="/docs/en/vs-code#extension-settings">Focus view</a>, which hides tool activity behind one expandable row per turn; toggle it from the command menu or with <code>Ctrl+Alt+F</code> (<code>Ctrl+Option+F</code> on Mac)</div>
    <div>Sandbox credential files accept <a href="/docs/en/sandboxing#mask-credential-files"><code>mode: "mask"</code></a> on Linux and WSL2, so sandboxed commands read a sentinel copy while the sandbox proxy substitutes the real value on egress; credential masking also gains <code>extract</code>, JWT-aware <code>decode</code>, and AWS SigV4 re-signing options</div>
    <div>Marketplaces can distribute a plugin as a <a href="/docs/en/plugin-marketplaces#zip-archives">zip archive</a> with the new <code>archive</code> source, downloaded over HTTPS with an optional SHA-256 pin, so installs work without git or npm</div>
    <div><code>/review</code> is now an alias of <a href="/docs/en/code-review#review-a-diff-locally"><code>/code-review</code></a>, and <code>/code-review</code> with no effort level reuses the level you typed last</div>
    <div>A session you copy with <a href="/docs/en/agent-view#copy-the-session-with-%2Ffork"><code>/fork</code></a> now makes its code changes in a worktree of its own instead of the original session's checkout</div>
    <div>Plugins you install from <a href="/docs/en/discover-plugins#install-plugins"><code>/plugin</code></a> activate in the current session when it's safe to do so; the install summary reports <code>Plugin is now active.</code> or tells you to run <code>/reload-plugins</code></div>
    <div><a href="/docs/en/agent-view#how-file-edits-are-isolated">Background sessions</a> that changed code in a worktree now commit and push before finishing, open a draft pull request only when the task calls for one, and follow the git instructions in your <code>CLAUDE.md</code></div>
    <div>The 200-subagent-per-session cap is removed, so long-running sessions no longer refuse new subagents; the <a href="/docs/en/sub-agents#concurrent-subagent-limit">concurrency</a> and depth limits still apply</div>
    <div>A repository's checked-in settings can no longer turn on <a href="/docs/en/remote-control#enable-remote-control-for-all-sessions">Remote Control auto-connect</a>; set <code>remoteControlAtStartup</code> in your user or managed settings instead, and project and local settings can only turn it off</div>
    <div><a href="/docs/en/worktrees#how-claude-code-enforces-isolation">Worktree isolation</a> now blocks not only file edits but also Bash commands and git redirects that reach the main checkout, in every session type and in the session's subagents</div>
    <div>A Bash command can no longer hide part of itself from permission checks, and tab or invisible-Unicode padding no longer hides part of a command from the approval dialog</div>
    <div>PreToolUse auto-allow hooks no longer bypass tool restrictions in Claude Code's internal side tasks such as summaries and compaction</div>
    <div>The <a href="/docs/en/ultraplan">Ultraplan</a> research preview is removed, including the <code>/ultraplan</code> command and the <code>ultraplan</code> keyword; use plan mode or Claude Code on the web instead</div>
  </div>
</div>

[Full changelog for v2.1.220–v2.1.224 →](/docs/en/changelog#2-1-220)

---

## August 10–14, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w33.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w33.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 33 · August 10–14, 2026

> Claude Code Desktop auto-continues after a usage limit resets, fork mode turns on by default, and GitLab merge requests and marketplaces join GitHub.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-225">v2.1.225 → v2.1.233</a></span>
  <span>3 features · August 10–14</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Auto-continue after a usage limit on Desktop</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">When you hit your session limit in the Code tab of Claude Code Desktop, the limit card now offers an <strong>Auto-continue when limits reset</strong> checkbox. Check it, and the Desktop app retries the interrupted turn after the reset. The card shows the retry time. The weekly-limit card doesn't offer it.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/2SnAdpL4dJ18nKb3/images/whats-new/desktop-auto-continue.mp4?fit=max&auto=format&n=2SnAdpL4dJ18nKb3&q=85&s=1937f489695feaea715e48ecfd7e62cd" data-path="images/whats-new/desktop-auto-continue.mp4" />
  </Frame>

  <p className="digest-feature-try">The next time a session-limit card appears, check <strong>Auto-continue when limits reset</strong> and leave the session open. The card shows <code>Auto-resuming at</code> followed by the reset time, and the turn picks up on its own once the limit resets.</p>

  <a className="digest-feature-link" href="/docs/en/errors#youve-hit-your-session-limit">What to do when you hit a usage limit</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Fork mode on by default</span>
    <span className="digest-feature-pill">v2.1.232</span>
  </div>

  <p className="digest-feature-lede">Fork mode is now on by default in interactive sessions. Claude can request the <code>fork</code> subagent type, which inherits the full conversation and prompt cache instead of starting fresh, so you don't have to re-explain the context for a side task. Subagents Claude spawns in interactive sessions, apart from the ones an agent-team teammate spawns, also run in the background by default.</p>

  <p className="digest-feature-try">Start a fork yourself with a task that needs everything you've discussed so far:</p>

  ```text Claude Code theme={null}
  > /subtask draft unit tests for the parser changes so far
  ```

  <p className="digest-feature-try">The fork appears in the panel below your prompt and its result arrives in your conversation when it finishes. To turn fork mode off, set <code>CLAUDE\_CODE\_FORK\_SUBAGENT=0</code>.</p>

  <a className="digest-feature-link" href="/docs/en/sub-agents#turn-fork-mode-on-or-off">Turn fork mode on or off</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">GitLab merge requests and marketplaces</span>
    <span className="digest-feature-pill">v2.1.232</span>
  </div>

  <p className="digest-feature-lede">Plugin marketplaces clone bare <code>gitlab.com</code> URLs, including nested subgroups. On v2.1.233 or later, pass a GitLab merge request URL to <code>--worktree</code> to branch from it, and the <code>claude agents</code> view labels sessions linked to a merge request as <code>!N</code>. Claude Code also redacts GitLab token families such as <code>glpat-</code> and <code>glrt-</code>, and protects the <code>glab</code> CLI's config store the same way it protects <code>gh</code>.</p>

  <p className="digest-feature-try">Start a session in a worktree branched from a merge request:</p>

  ```bash terminal theme={null}
  claude --worktree https://gitlab.com/group/project/-/merge_requests/42
  ```

  <p className="digest-feature-try">When <code>origin</code> is on gitlab.com, Claude Code fetches <code>merge-requests/42/head</code> and opens the session on that branch in its own worktree.</p>

  <a className="digest-feature-link" href="/docs/en/worktrees#branch-from-a-pull-request">Branch a worktree from a pull or merge request</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Type <code>@</code> in the prompt to <a href="/docs/en/cross-session-messaging#message-another-session">mention another Claude session</a> by name, and Claude messages it directly with <code>SendMessage</code>; a bare name that matches exactly one live session now delivers without a confirmation step</div>
    <div>Interactive sessions on one machine keep <a href="/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach">unique names</a>: if you start or rename a session with a name another live session already uses, Claude Code gives yours a <code>name-word-word</code> variant and tells you</div>
    <div>Plugin marketplaces accept <a href="/docs/en/plugin-marketplaces#command-sources"><code>command</code> sources</a>: a local command prints the plugin directory, which Claude Code re-resolves each session and applies without a restart</div>
    <div>On Linux and WSL, set <a href="/docs/en/tools-reference#memory-limit-on-linux-and-wsl"><code>CLAUDE\_CODE\_TOOL\_MEMORY\_LIMIT</code></a> to a size such as <code>4G</code> to cap the memory Bash and PowerShell tool commands can use</div>
    <div>The task-tracking tools, such as <code>TaskCreate</code>, <code>TaskUpdate</code>, and <code>TodoWrite</code>, are <a href="/docs/en/tools-reference#task-tool-availability">no longer available on Opus 4.8, Sonnet 5, Fable 5, Mythos 5, and later models in those families</a>; set <code>CLAUDE\_CODE\_ENABLE\_TODO\_TOOLS=1</code> to re-enable them</div>
    <div><a href="/docs/en/code-review#review-a-diff-locally"><code>/code-review</code></a> at high, xhigh, and max effort now runs in a background agent like the other levels</div>
    <div><a href="/docs/en/discover-plugins#install-plugins"><code>/plugin install plugin\@marketplace</code></a> refreshes the marketplace first, so newly published plugins install without a manual marketplace update</div>
    <div>Settings accept <a href="/docs/en/settings-reference#marketplace-key-aliases"><code>additionalMarketplaces</code> and <code>allowedMarketplaces</code></a> as aliases for <code>extraKnownMarketplaces</code> and <code>strictKnownMarketplaces</code></div>
    <div>On newer models, Claude can <a href="/docs/en/tools-reference#write-tool-behavior">overwrite an existing file with the Write tool</a> without reading it first this session, matching the Edit tool's rules; older models require the read</div>
    <div>The VS Code extension can <a href="/docs/en/vs-code#organize-sessions-into-groups">organize the sessions list into groups</a>: right-click to create, rename, or delete a group, and Cmd/Ctrl- or Shift-click to move several sessions at once</div>
    <div>If your organization routes Claude Code through a <a href="/docs/en/claude-apps-gateway-spend-limits">Claude apps gateway with spend limits</a>, Claude Code shows the limit period, its reset time, and the operator's message when you reach the limit</div>
  </div>
</div>

[Full changelog for v2.1.225–v2.1.233 →](/docs/en/changelog#2-1-225)

---

## August 17–21, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w34.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w34.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 34 · August 17–21, 2026

> Draft editable UI artboards with the /design skill, set the Concise output style, and start a Claude Code session on your machine from your phone.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-234">v2.1.234 → v2.1.239</a></span>
  <span>3 features · August 17–21</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">/design</span>
    <span className="digest-feature-pill">research preview</span>
  </div>

  <p className="digest-feature-lede">The <code>/design</code> skill brings Claude Design's artboard workflow into the CLI and Claude Code Desktop, built on artifacts. Run it with a brief and Claude publishes a canvas of editable artboards for your UI. Pick one, tweak it, then have Claude implement it. Available on Pro, Max, Team, and Enterprise. Requires v2.1.234 or later.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/2SnAdpL4dJ18nKb3/images/whats-new/design-skill.mp4?fit=max&auto=format&n=2SnAdpL4dJ18nKb3&q=85&s=0b376a94227c14a4204af89c4c9fd7ac" data-path="images/whats-new/design-skill.mp4" />
  </Frame>

  <p className="digest-feature-try">Describe what you want designed and let Claude draft the options:</p>

  ```text Claude Code theme={null}
  > /design redesign the composer based on what people actually use it for
  ```

  <p className="digest-feature-try">Claude prints a link to the published canvas. Open it, pick an artboard, and tell Claude which option to implement.</p>

  <a className="digest-feature-link" href="/docs/en/artifacts#availability">Where artifacts are available</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Concise output style</span>
    <span className="digest-feature-pill">v2.1.237</span>
  </div>

  <p className="digest-feature-lede">Concise is a new built-in output style. Claude leads with the result and skips preamble and narration, while doing the work as thoroughly as in the Default style. When you ask for an explanation or more detail, Claude answers in full. Error reports, security warnings, and confirmations for destructive actions keep their complete content.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/2SnAdpL4dJ18nKb3/images/whats-new/concise-output-style.mp4?fit=max&auto=format&n=2SnAdpL4dJ18nKb3&q=85&s=dfb40ec8921ed1bc82eb629042a8ec17" data-path="images/whats-new/concise-output-style.mp4" />
  </Frame>

  <p className="digest-feature-try">Turn it on under <strong>Output style</strong> in <code>/config</code>, or set it in your settings file:</p>

  ```json ~/.claude/settings.json {2} theme={null}
  {
    "outputStyle": "Concise"
  }
  ```

  <p className="digest-feature-try">Run <code>/clear</code> or start a new session, and Claude's replies lead with the result.</p>

  <a className="digest-feature-link" href="/docs/en/output-styles#built-in-output-styles">Built-in output styles</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Start a session on your machine from your phone</span>
    <span className="digest-feature-pill">mobile</span>
  </div>

  <p className="digest-feature-lede">Any machine running <code>claude remote-control</code> now shows up as a device card at the top of the Code tab in the Claude app. Remote Control is also out of research preview.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/2SnAdpL4dJ18nKb3/images/whats-new/remote-control-phone-start.jpg?fit=max&auto=format&n=2SnAdpL4dJ18nKb3&q=85&s=9f0ebedab23aa0e1732cc37782573907" alt="The Code tab in the Claude mobile app with a Devices section showing a connected MacBook as a device card above the sessions list" width="1206" height="895" data-path="images/whats-new/remote-control-phone-start.jpg" />
  </Frame>

  <p className="digest-feature-try">Start Remote Control on the machine you want to reach, then open the Code tab on your phone:</p>

  ```bash terminal theme={null}
  claude remote-control
  ```

  <p className="digest-feature-try">Your machine appears as a device card at the top of the Code tab. Tap it to pick a directory and start a session there.</p>

  <a className="digest-feature-link" href="/docs/en/remote-control#start-a-remote-control-session">Start a Remote Control session</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Claude Code now continues your session automatically when a claude.ai usage limit resets; turn it off from the <strong>Continue automatically at usage limit</strong> row in <code>/config</code></div>
    <div>The optional <a href="/docs/en/interactive-mode#check-spelling-as-you-type"><code>spellcheck</code> setting</a> underlines misspelled words in the prompt input as you type, using your installed <code>aspell</code>, <code>hunspell</code>, or <code>ispell</code></div>
    <div>On a branch with an open GitLab merge request, with the <code>glab</code> CLI authenticated through <code>glab auth login</code>, the footer shows an <a href="/docs/en/interactive-mode#gitlab-merge-requests"><code>MR !N</code> badge</a> colored by whether the merge request is a draft, open, or mergeable</div>
    <div>Change the effort level from your phone or claude.ai/code and it <a href="/docs/en/remote-control#what-connected-devices-see">applies to the session on your machine</a>; Remote Control sessions hosted by Desktop or VS Code also show connected devices the session's current permission mode</div>
    <div>You can open <a href="/docs/en/permissions#manage-permissions"><code>/permissions</code></a> or run <code>/add-dir \<path></code> while Claude is working; permission rule changes apply to the rest of the current turn</div>
    <div>When background tasks keep a <a href="/docs/en/goal#background-work-defers-evaluation"><code>/goal</code></a> waiting, Claude checks in on them after 30 minutes instead of waiting indefinitely and keeps checking in, at longer intervals while the session sits idle; set <code>CLAUDE\_CODE\_GOAL\_CHECKIN\_MINUTES=0</code> to opt out</div>
    <div>Your own prompts now render markdown in the transcript, with highlighted code blocks, inline code, and lists, the same way replies do</div>
    <div>The new <a href="/docs/en/model-config#set-a-default-model-for-new-sessions"><code>ANTHROPIC\_DEFAULT\_MODEL</code></a> environment variable sets the model new sessions start on; a <code>/model</code> pick still overrides it and persists across restarts</div>
    <div>With the <code>notify\_when\_idle</code> input on <code>SendMessage</code>, Claude can ask another Claude Code session on the same machine to <a href="/docs/en/cross-session-messaging#get-a-notice-when-another-session-goes-idle">send one notice when it next goes idle</a></div>
    <div>Set <a href="/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace"><code>keybindingFlavor</code></a> to <code>"readline"</code> to make <code>Ctrl+W</code> in the prompt delete back to the previous whitespace, as Bash does, instead of stopping at punctuation such as <code>/</code></div>
    <div>On native Windows, your Claude Code sessions can now <a href="/docs/en/cross-session-messaging#availability">message each other</a> with <code>SendMessage</code> and find each other with <code>ListAgents</code>, as on macOS and Linux</div>
    <div>Self-hosted runners accept `--defer-shutdown-max-min`, which <a href="/docs/en/self-hosted-environments-deploy#defer-the-drain-past-the-first-signal">keeps serving attached sessions</a> for a set number of minutes after SIGTERM</div>
    <div>Self-hosted runners accept `--proxy-authorization-command` or `--proxy-authorization-file` to supply a fresh `Proxy-Authorization` header for <a href="/docs/en/self-hosted-environments-deploy#authenticate-to-an-egress-proxy">egress proxies that require one</a></div>
  </div>
</div>

[Full changelog for v2.1.234–v2.1.239 →](/docs/en/changelog#2-1-234)

---

## August 24–28, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w35.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w35.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 35 · August 24–28, 2026

> Resume terminal sessions in the Claude Code Desktop app, review feedback reports that Claude drafts for you, and start a session in restricted mode.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-240">v2.1.240 → v2.1.250</a></span>
  <span>3 features · August 24–28</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Resume terminal sessions in the Desktop app</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">Type <code>/resume</code> in the Claude Code Desktop prompt box to pick up any session you started from the CLI and continue it in the app with the full conversation and context intact. Search your sessions by title, folder, or branch, and preview where you left off before you resume.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/desktop-resume-cli-session.mp4?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=41e4a5fda6b9d63280589f2cbdabf44f" data-path="images/whats-new/desktop-resume-cli-session.mp4" />
  </Frame>

  <p className="digest-feature-try">In a Desktop session, run the command to list your terminal sessions:</p>

  ```text Claude Code theme={null}
  > /resume
  ```

  <p className="digest-feature-try">Select a session and press <code>Enter</code>. The conversation opens in the app where you left off.</p>

  <a className="digest-feature-link" href="/docs/en/desktop#coming-from-the-cli">Move between the CLI and Desktop</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude-drafted feedback</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede">When a tool keeps failing, Claude can't help with a request, or you point out a mistake, Claude now drafts a feedback report for you with the <code>SendFeedback</code> tool. A card above your prompt shows the draft, and you can review, send, or dismiss it from there. Nothing reaches Anthropic until you send it. Requires v2.1.238 or later.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/claude-drafted-feedback.jpg?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=5cacb3be0dffd1cbd417381f3721637e" alt="A Claude Code session where Claude has drafted a bug report titled Sandbox image pull fails behind proxy, shown as a card above the prompt with options to review, send, or dismiss" width="1440" height="756" data-path="images/whats-new/claude-drafted-feedback.jpg" />
  </Frame>

  <p className="digest-feature-try">Run <code>/feedback</code> with no argument to open your queue of drafts from every session:</p>

  ```text Claude Code theme={null}
  > /feedback
  ```

  <p className="digest-feature-try">Select a draft, then edit, send, or discard it. To turn drafting off, set <strong>Claude-drafted feedback</strong> to <code>off</code> in <code>/config</code>.</p>

  <a className="digest-feature-link" href="/docs/en/tools-reference#sendfeedback-tool-behavior">SendFeedback tool behavior</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Restricted mode</span>
    <span className="digest-feature-pill">v2.1.248</span>
  </div>

  <p className="digest-feature-lede">Restricted mode starts Claude Code without the built-in tools that run commands or code. Use it when an evaluation harness drives <code>claude</code> on a shared machine. Start it with `--restricted` or set <code>CLAUDE\_CODE\_RESTRICTED=1</code>. Claude Code also removes <code>WebFetch</code>, confines the file tools to the working directories, loads only managed settings and `--settings`, and refuses the <code>bypassPermissions</code> permission mode.</p>

  <p className="digest-feature-try">Run a non-interactive query without the command-running tools:</p>

  ```bash terminal theme={null}
  claude --restricted -p "review src/ for SQL injection risks"
  ```

  <p className="digest-feature-try">To give Claude one of the removed tools back, list it in `--tools` together with the other built-in tools you want, for example `--tools "Bash,Read,Edit"`. `--tools` is an allowlist, and its <code>default</code> preset doesn't restore the removed tools.</p>

  <a className="digest-feature-link" href="/docs/en/cli-reference#cli-flags">CLI flags</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Set the new <a href="/docs/en/settings-reference#modelpicker"><code>modelPicker</code></a> setting to extend or replace the <code>/model</code> picker's built-in list with your own ordered, labeled entries, including Amazon Bedrock or Google Cloud's Agent Platform model IDs</div>
    <div>Set <a href="/docs/en/prompt-caching#choose-the-ttl-yourself"><code>promptCacheTtl</code></a> to <code>1h</code> to keep a one-hour prompt cache on the main conversation when you use an API key or a cloud provider; <code>subagentPromptCacheTtl</code> sets the TTL for subagents and all other requests outside the main conversation</div>
    <div>On Pro, Max, Team, and Enterprise plans, <a href="/docs/en/costs#plan-usage-breakdown"><code>/usage</code></a> adds a Loops breakdown: run count, total tokens, tokens per run, and last run for the <code>/loop</code> and scheduled tasks that used the most tokens</div>
    <div>Organizations on contracted rates can set the <a href="/docs/en/costs#report-spend-at-your-contracted-rates"><code>modelPricing</code></a> managed setting so <code>/usage</code>, the status line, and OpenTelemetry report cost at those rates instead of list price</div>
    <div><code>/login</code> offers <strong>Sign in with your Console account</strong> under the <strong>Anthropic Console account</strong> option, so members of Console organizations that don't allow API keys can sign in without creating one</div>
    <div>Run <code>/permissions</code> and open the new <a href="/docs/en/auto-mode-config#edit-rules-from-permissions"><strong>Auto mode</strong> tab</a> to view and edit auto mode classifier rules without opening a settings file</div>
    <div>When auto mode is available, Bash permission prompts in the Manual and <code>acceptEdits</code> permission modes offer a <a href="/docs/en/permission-modes#switch-permission-modes"><strong>Yes, and switch to auto mode</strong></a> option; select it to approve the command and switch the session to auto mode</div>
    <div>After you <a href="/docs/en/permissions#move-the-session-to-another-directory">move a session with <code>/cd</code></a>, the new directory's project settings, hooks, <code>.mcp.json</code> servers, skills, and subagents take effect immediately instead of on the next `--resume`</div>
    <div>In non-interactive sessions, including <code>-p</code> runs, Agent SDK runs, and cloud sessions, Claude Code <a href="/docs/en/errors#the-response-above-may-be-incomplete">continues a response</a> that a server error, dropped connection, or stall cut off mid-stream, when the partial response contains text and no tool calls</div>
    <div>A subagent that stops at its <code>maxTurns</code> limit returns its output marked as partial, with a hint that Claude can <a href="/docs/en/sub-agents#resume-subagents">continue it with <code>SendMessage</code></a>, instead of appearing finished</div>
    <div>On Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, sessions on the same machine can now <a href="/docs/en/cross-session-messaging#availability">message each other</a>, <code>/loop</code> can <a href="/docs/en/scheduled-tasks#let-claude-choose-the-interval">choose its own interval</a>, and <code>/model</code> and <code>/effort</code> apply immediately instead of after the turn ends</div>
    <div>The native installer and auto-updater download a zstd-compressed build, about 75 MB instead of 340 MB on Linux x64, and native builds load code on demand, using roughly 40 to 70 MB less memory per session</div>
  </div>
</div>

[Full changelog for v2.1.240–v2.1.250 →](/docs/en/changelog#2-1-240)

---

## August 31 – September 4, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w36.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w36.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 36 · August 31 – September 4, 2026

> Switch to Claude Fable 5.1, let computer use run in the background on Desktop, and watch Claude's edits in a live /diff panel.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-251">v2.1.251 → v2.1.261</a></span>
  <span>4 features · August 31 – September 4</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Claude Fable 5.1</span>
    <span className="digest-feature-pill">new model</span>
  </div>

  <p className="digest-feature-lede">Claude Fable 5.1 is available in Claude Code with a 1M-token context window, and the <code>fable</code> alias now selects it. In Claude apps gateway sessions, <code>fable</code> still selects Fable 5. If your gateway serves Fable 5.1, run <code>/model claude-fable-5-1</code>. Requires v2.1.257 or later.</p>

  <p className="digest-feature-try">Switch the current session to Fable 5.1 and save it as your default:</p>

  ```text Claude Code theme={null}
  > /model fable
  ```

  <p className="digest-feature-try">On the Anthropic API, the picker lists Fable only once the server reports it available for your organization, but typing <code>/model fable</code> checks with the server directly.</p>

  <a className="digest-feature-link" href="/docs/en/model-config#work-with-fable">Work with Fable</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Computer use runs in the background on Desktop</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">On macOS, computer use in the Claude Code Desktop app now works in the background: Claude sees and acts in the apps you've approved while you keep working. Background computer use is in beta on Pro and Max plans.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/background-computer-use.jpg?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=a599a6c6fa544cb8d1b426b93706caf4" alt="A Claude Code Desktop session where Claude asks to use Xcode, with a Computer use permission card that reads Let Claude see and act in the apps you approve, in the background or with full control of your screen, next to an Enable button" width="1440" height="810" data-path="images/whats-new/background-computer-use.jpg" />
  </Frame>

  <a className="digest-feature-link" href="/docs/en/desktop#let-claude-use-your-computer">Let Claude use your computer</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Live diff panel in fullscreen rendering</span>
    <span className="digest-feature-pill">v2.1.260</span>
  </div>

  <p className="digest-feature-lede">In fullscreen rendering, <code>/diff</code> now opens a panel beside the conversation instead of a viewer you have to close. The panel lists the changed files with their added and removed line counts and refreshes each time Claude edits a file or runs a shell command. Select lines in the panel with the mouse to attach them to your next prompt.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/diff-panel.mp4?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=9d7553c19e7f227891cd95f1f59d796d" data-path="images/whats-new/diff-panel.mp4" />
  </Frame>

  <p className="digest-feature-try">With fullscreen rendering on, inside a git repository, and in a terminal at least 110 columns wide, toggle the panel:</p>

  ```text Claude Code theme={null}
  > /diff
  ```

  <p className="digest-feature-try">Run <code>/diff</code> again or click the <code>✕</code> in its header to close it.</p>

  <a className="digest-feature-link" href="/docs/en/interactive-mode#diff-panel">Diff panel</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Find unused skills with /skill-doctor</span>
    <span className="digest-feature-pill">CLI</span>
  </div>

  <p className="digest-feature-lede"><code>/skill-doctor</code> shows what each of your skills costs in context and how often it gets used, so you can decide which ones to turn off. Every skill in the <a href="/docs/en/skills#skill-descriptions-are-cut-short">skill listing</a> adds to your context on every turn, whether or not Claude ever uses it. Requires v2.1.252 or later and isn't available in sessions that skip <a href="/docs/en/env-vars#features-that-need-feature-flag-fetching">feature-flag fetching</a>.</p>

  <p className="digest-feature-try">Run it in an interactive session to open the report in the <code>/plugin</code> manager's <strong>Stats</strong> tab:</p>

  ```text Claude Code theme={null}
  > /skill-doctor
  ```

  <p className="digest-feature-try">In non-interactive mode with <code>-p</code>, Claude Code prints the report as text instead.</p>

  <a className="digest-feature-link" href="/docs/en/skills#find-unused-skills">Find unused skills</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>A <a href="/docs/en/hooks#premodelswitch"><code>PreModelSwitch</code></a> hook can block a model switch you request, and a <a href="/docs/en/hooks#postmodelswitch"><code>PostModelSwitch</code></a> hook can add context for Claude after the session's model changes</div>
    <div><a href="/docs/en/costs#prompt-cache-statistics"><code>/cost</code></a> adds a <code>Prompt cache (main)</code> line: the share of input tokens served from cache, the cache misses, whether the cache is warm, and a likely cause for the last miss when Claude Code can name one. Status line scripts get a matching <code>prompt\_cache</code> object</div>
    <div>Organizations can list HTTP and SSE MCP servers under the <a href="/docs/en/managed-mcp#provide-servers-through-managed-settings"><code>managedMcpServers</code></a> managed setting to give them to every user, in addition to the servers that users add on their own</div>
    <div><code>/effort</code> and the <code>/model</code> picker now <a href="/docs/en/model-config#adjust-effort-level">save a separate effort level for each model</a>; press <code>s</code> instead of <code>Enter</code> to apply a level to the current session only</div>
    <div>By default, the auto mode classifier <a href="/docs/en/permission-modes#what-the-classifier-blocks-by-default">now also blocks</a> actions such as requesting credentials from the cloud instance-metadata endpoint or connecting to sibling containers that Claude didn't start</div>
    <div>In auto mode, Claude Code asks you before Claude <a href="/docs/en/permission-modes#first-read-outside-the-working-directories">first reads a file outside your working directories</a>, with an option to block such reads from then on</div>
    <div>Raise <a href="/docs/en/settings-reference#bashoutputmaxchars"><code>bashOutputMaxChars</code></a> and <a href="/docs/en/settings-reference#taskoutputmaxchars"><code>taskOutputMaxChars</code></a>, up to 128,000 characters, so Claude receives more of the output from a successful command or background task inline</div>
    <div>The prompt's <a href="/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace">word-editing shortcuts follow readline</a> for everyone, and the <code>keybindingFlavor</code> setting no longer has any effect. <code>Ctrl+W</code> deletes back to the previous whitespace, and <code>Alt+B</code>, <code>Alt+F</code>, and <code>Alt+D</code> treat punctuation such as <code>/</code> and <code>.</code> as word breaks</div>
    <div>If you set <code>defaultMode</code> to <code>"bypassPermissions"</code> in a project's <code>.claude/settings.json</code> or <code>.claude/settings.local.json</code>, it <a href="/docs/en/permission-modes#which-mode-a-session-starts-in">no longer takes effect</a> and the session starts in Manual mode; set <code>"bypassPermissions"</code> in user or managed settings instead, or pass `--permission-mode`</div>
    <div>Seat-based Enterprise plans now <a href="/docs/en/model-config#default-model-setting">default to Opus 5</a></div>
    <div>In the VS Code extension, click the model name at the bottom of the prompt box to <a href="/docs/en/vs-code#use-the-prompt-box">open the model picker</a></div>
    <div>In the VS Code extension, select <strong>Output styles</strong> in the command menu's Customize section to <a href="/docs/en/vs-code#use-the-prompt-box">pick an output style</a>, including your custom ones</div>
  </div>
</div>

[Full changelog for v2.1.251–v2.1.261 →](/docs/en/changelog#2-1-251)

---

## September 7–11, 2026

- 官方原文：https://code.claude.com/docs/en/whats-new/2026-w37.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-2026-w37.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Week 37 · September 7–11, 2026

> Test your plugins with claude plugin eval and pop Claude Code Desktop panes out into their own windows.

<div className="digest-meta">
  <span>Releases <a href="/docs/en/changelog#2-1-263">v2.1.263 → v2.1.269</a></span>
  <span>2 features · September 7–11</span>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Test plugins with claude plugin eval</span>
    <span className="digest-feature-pill">v2.1.269</span>
  </div>

  <p className="digest-feature-lede"><code>claude plugin eval</code> runs your plugin against a suite of test cases, scores the results, and by default runs each case again without the plugin so you can see what it contributes. <code>claude plugin eval init</code> asks you what a good result looks like, then proposes test cases and the checks that score them, tries the suite once, and writes the files. Every run, and every check that has a second model judge the reply, is a real model call on your account.</p>

  <Frame>
    <img className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/plugin-eval.jpg?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=913066f6d4a2a15426e98a627802f47f" alt="Terminal output of claude plugin eval: a table of seven cases with each case's score with and without the plugin, the delta between them, the run count, and the cost, followed by a summary line with the mean delta, total duration, and total cost" width="1600" height="900" data-path="images/whats-new/plugin-eval.jpg" />
  </Frame>

  <p className="digest-feature-try">From your plugin's root directory, have Claude draft the suite:</p>

  ```bash terminal theme={null}
  claude plugin eval init
  ```

  <p className="digest-feature-try">When Claude tells you the suite is ready, exit the session that <code>claude plugin eval init</code> opened and run <code>claude plugin eval .</code> to score every case. The summary table prints in your terminal, and <code>report.html</code> under <code>evals/results/</code> has the per-run detail.</p>

  <a className="digest-feature-link" href="/docs/en/plugin-evals">Test plugins with evals</a>
</div>

<div className="digest-feature">
  <div className="digest-feature-header">
    <span className="digest-feature-title">Pop Desktop panes out into their own windows</span>
    <span className="digest-feature-pill">Desktop</span>
  </div>

  <p className="digest-feature-lede">In the Claude Code Desktop app, you can pop any pane out into its own window. Drag the diff or terminal to a second screen while Claude keeps working in the main window, then dock the pane back when you're done.</p>

  <Frame>
    <video autoPlay muted loop playsInline className="w-full" src="https://mintcdn.com/claude-code/f9HTZGyMtxIFOUgt/images/whats-new/desktop-pop-out-panes.mp4?fit=max&auto=format&n=f9HTZGyMtxIFOUgt&q=85&s=ff3770dd09bb15ed9cf17a460f3d1e23" data-path="images/whats-new/desktop-pop-out-panes.mp4" />
  </Frame>

  <a className="digest-feature-link" href="/docs/en/desktop#arrange-your-workspace">Arrange your workspace</a>
</div>

<div className="digest-wins">
  <p className="digest-wins-title">Other wins</p>

  <div className="digest-wins-grid">
    <div>Set <a href="/docs/en/settings-reference#maxeffortlevel"><code>maxEffortLevel</code></a> at the top level or per model under <code>modelSettings</code> to cap the effort level on every provider, including Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry; any higher level runs at the cap</div>
    <div>Point `--plugin-dir` at a folder of plugins to <a href="/docs/en/plugins#test-your-plugins-locally">load each immediate subfolder that has a manifest</a></div>
    <div>If WebFetch hasn't finished downloading a page within five minutes, <a href="/docs/en/tools-reference#webfetch-tool-behavior">the fetch fails with a deadline error</a> instead of hanging; set <code>CLAUDE\_CODE\_WEBFETCH\_DEADLINE\_MS</code> to change the deadline, or to <code>0</code> to remove the limit</div>
    <div>Pass `--json` to <code>claude plugin install</code>, <code>uninstall</code>, <code>update</code>, <code>enable</code>, or <code>disable</code> to print the result as <a href="/docs/en/plugins-reference#plugin-json-result">one JSON object on the last line of stdout</a></div>
    <div>When the auto mode classifier blocks an action, the reason Claude receives <a href="/docs/en/auto-mode-config#fix-a-denial-with-an-allow-rule-an-environment-entry-or-a-retry">usually names the rule that matched</a>, such as <code>\[Data Exfiltration]</code></div>
    <div>When you type <code>/</code> partway through a prompt, you can now pick from <a href="/docs/en/interactive-mode#complete-a-command-mid-prompt">a list of matching commands</a> instead of a single suggestion. The list opens as you type in fullscreen rendering. A plugin skill also matches on its name without the plugin prefix</div>
    <div>In the VS Code extension, click the agent count at the bottom of the prompt box to open the <a href="/docs/en/vs-code#use-the-prompt-box">agent map</a>, where you can open a subagent's read-only transcript or stop it</div>
    <div>In the VS Code extension, select <strong>Hooks</strong> or <strong>Permissions</strong> in the command menu's Customize section to <a href="/docs/en/vs-code#use-the-prompt-box">add or remove hooks and permission rules</a> in your user, project, and local settings</div>
    <div>Claude can pick a <a href="/docs/en/artifacts#create-an-artifact">browser-tab icon</a> to match each artifact it publishes</div>
    <div>In Claude Code on the web, take back a queued message in a cloud session before Claude reads it: remove it from the queue, or press <code>Esc</code> or <code>Up</code>, and the text returns to the message box</div>
  </div>
</div>

[Full changelog for v2.1.263–v2.1.269 →](/docs/en/changelog#2-1-263)

---

## What's new

- 官方原文：https://code.claude.com/docs/en/whats-new/index.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-whats-new-index.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What's new

> A weekly digest of notable Claude Code features, with code snippets, demos, and context on why they matter.

The weekly dev digest highlights the features most likely to change how you work. Each entry includes runnable code, a short demo, and a link to the full docs. For every bug fix and minor improvement, see the [changelog](/docs/en/changelog).

<Update label="Week 37" description="September 7–11, 2026" tags={["v2.1.263–v2.1.269"]}>
  **`claude plugin eval`**: run your plugin against a suite of test cases, score the results, and compare against a no-plugin baseline. `claude plugin eval init` drafts the cases and graders for you.

  Also this week: pop any **Claude Code Desktop pane** out into its own window and dock it back later; the **`maxEffortLevel`** setting caps the effort level on every provider; and a page that **WebFetch** hasn't finished downloading within five minutes fails instead of hanging.

  [Read the Week 37 digest →](/docs/en/whats-new/2026-w37)
</Update>

<Update label="Week 36" description="August 31 – September 4, 2026" tags={["v2.1.251–v2.1.261"]}>
  **Claude Fable 5.1**: available in Claude Code with a 1M-token context window.

  Also this week: on Pro and Max plans, **computer use in the Desktop app** works in the background on macOS while you keep working; in fullscreen rendering, **`/diff`** opens a live panel beside the conversation that refreshes as Claude edits; and **`/skill-doctor`** shows what each of your skills costs in context and how often it gets used.

  [Read the Week 36 digest →](/docs/en/whats-new/2026-w36)
</Update>

<Update label="Week 35" description="August 24–28, 2026" tags={["v2.1.240–v2.1.250"]}>
  **Resume terminal sessions in the Desktop app**: type `/resume` in the Claude Code Desktop prompt box to pick up any session you started from the CLI, with the full conversation and context intact.

  Also this week: **Claude-drafted feedback** has Claude write up a feedback report when something goes wrong in a session, which you review and send from `/feedback`; **`--restricted`** starts a session without the command-running tools or your user and project settings, for evaluation harnesses on shared machines; and the **`modelPicker`** setting controls which models the `/model` picker lists.

  [Read the Week 35 digest →](/docs/en/whats-new/2026-w35)
</Update>

<Update label="Week 34" description="August 17–21, 2026" tags={["v2.1.234–v2.1.239"]}>
  **`/design`**: a research preview that brings Claude Design's artboard workflow into the CLI and Claude Code Desktop, built on artifacts, so Claude drafts editable artboards for your UI and implements the one you pick.

  Also this week: the built-in **Concise output style** makes Claude lead with the result and skip preamble; any machine running `claude remote-control` shows up as a **device card** on your phone so you can start a session on it from the Code tab; and **`ANTHROPIC_DEFAULT_MODEL`** sets the model new sessions start on.

  [Read the Week 34 digest →](/docs/en/whats-new/2026-w34)
</Update>

<Update label="Week 33" description="August 10–14, 2026" tags={["v2.1.225–v2.1.233"]}>
  **Auto-continue after a usage limit on Desktop**: when you hit your session limit in Claude Code Desktop, check **Auto-continue when limits reset** on the limit card and the app retries the interrupted turn once the limit resets.

  Also this week: **fork mode** is on by default in interactive sessions, so Claude can delegate a side task to a subagent that inherits the full conversation; **GitLab** merge request URLs work with `--worktree` and the `claude agents` view, and marketplaces clone bare `gitlab.com` URLs; and typing **`@`** in the prompt mentions another Claude session by name.

  [Read the Week 33 digest →](/docs/en/whats-new/2026-w33)
</Update>

<Update label="Week 32" description="August 3–7, 2026" tags={["v2.1.220–v2.1.224"]}>
  **Cross-session messaging**: on macOS and Linux, your Claude Code sessions can now message each other, so Claude passes a finding or a decision from one session to another instead of you re-explaining it.

  Also this week: **self-hosted environments** run Claude Code cloud sessions on infrastructure your organization operates, in public beta on Team and Enterprise plans; **auto mode** becomes the default permission mode for new sessions on Pro, Max, and Team plans starting August 14; and the **VS Code extension** gets Focus view.

  [Read the Week 32 digest →](/docs/en/whats-new/2026-w32)
</Update>

<Update label="Week 30" description="July 20–24, 2026" tags={["v2.1.214–v2.1.219"]}>
  **Claude Opus 5**: the new default Opus model in Claude Code, with a 1M-token context window and fast mode at \$10/\$50 per MTok.

  Also this week: **Claude Code Desktop** opens an iOS Simulator pane in public beta so Claude can run your app and tap through it while you watch; the **Claude Security plugin** runs a multi-agent vulnerability scan of your codebase and turns the findings you pick into patches you apply yourself; and **`/code-review`** runs as a background subagent.

  [Read the Week 30 digest →](/docs/en/whats-new/2026-w30)
</Update>

<Update label="Week 29" description="July 13–17, 2026" tags={["v2.1.207–v2.1.212"]}>
  **Artifacts call your MCP connectors**: a published artifact can pull live data and take actions through each viewer's own MCP connectors when they open the page, and this week also adds public sharing links, editor roles on Team and Enterprise, and artifacts created from Claude Tag sessions.

  Also this week: **screen reader mode** replaces the visual terminal interface with plain, linear text for screen readers such as VoiceOver and NVDA; **`/fork`** copies your conversation into a new background session while you keep working; and **auto mode** no longer needs an opt-in variable on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry.

  [Read the Week 29 digest →](/docs/en/whats-new/2026-w29)
</Update>

<Update label="Week 28" description="July 6–10, 2026" tags={["v2.1.202–v2.1.206"]}>
  **In-app browser on Desktop**: Claude Code on desktop gets a built-in browser, so Claude can pull up docs, designs, or any other site and interact with pages the same way it does with your local dev server previews.

  Also this week: **`/doctor`** is a full setup checkup that diagnoses issues and can fix them, with `/checkup` as its alias; **auto mode** blocks transcript tampering and asks before `rm -rf` on unresolved variables; and **agent view rows** show a colored state word and a classifier-written headline.

  [Read the Week 28 digest →](/docs/en/whats-new/2026-w28)
</Update>

<Update label="Week 27" description="June 29 – July 3, 2026" tags={["v2.1.195–v2.1.201"]}>
  **Claude Sonnet 5**: the new default model for Pro, Team Standard, and Enterprise subscription seats, with top-tier coding and tool use at Sonnet pricing, a native 1M-token context window, and adaptive thinking on by default.

  Also this week: **Claude in Chrome** is generally available on all direct Anthropic plans; **subagents run in the background by default** so Claude keeps working while they run; **Claude Desktop on Linux** lands in beta on Ubuntu and Debian; and **`/radio`** tunes into Claude FM lo-fi radio.

  [Read the Week 27 digest →](/docs/en/whats-new/2026-w27)
</Update>

<Update label="Week 26" description="June 22–26, 2026" tags={["v2.1.185–v2.1.193"]}>
  **`claude mcp login`**: authenticate a configured MCP server from your shell instead of the interactive `/mcp` menu, and clear its stored credentials later with `claude mcp logout`.

  Also this week: **shell mode responds to command output** (`! npm test` gets an explanation without a second prompt); **`/rewind`** can resume a conversation from before `/clear` was run; and **background subagents** now surface permission prompts in the main session instead of auto-denying.

  [Read the Week 26 digest →](/docs/en/whats-new/2026-w26)
</Update>

<Update label="Week 25" description="June 15–19, 2026" tags={["v2.1.178–v2.1.183"]}>
  **Artifacts**: turn a session's output into a live, shareable page on claude.ai that updates in place as the session works, now in beta on Team and Enterprise plans.

  Also this week: **deny and ask rules match tool parameters** with `Tool(param:value)`, for example `Agent(model:opus)`; **`/config key=value`** sets any setting from the prompt, in `-p` mode, and from Remote Control; and **auto mode blocks destructive git commands** when you didn't ask to discard local work.

  [Read the Week 25 digest →](/docs/en/whats-new/2026-w25)
</Update>

<Update label="Week 24" description="June 8–12, 2026" tags={["v2.1.166–v2.1.176"]}>
  **`/cd`**: move the current session to a new working directory mid-conversation without rebuilding the prompt cache.

  Also this week: **sub-agents can spawn their own sub-agents** (background chains are capped at five levels deep); **`--safe-mode`** starts Claude Code with all customizations disabled for troubleshooting; and **`fallbackModel`** configures up to three fallback models tried in order.

  [Read the Week 24 digest →](/docs/en/whats-new/2026-w24)
</Update>

<Update label="Week 23" description="June 1–5, 2026" tags={["v2.1.158–v2.1.165"]}>
  **Auto mode on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry**: auto mode is now available on third-party providers for Opus 4.7 and Opus 4.8, replacing permission prompts with background safety checks.

  Also this week: **safer automatic edits** prompt before writing files that can run code in `acceptEdits` mode; **`/plugin list`** prints your installed plugins inline; and **version requirements** let managed deployments require an approved Claude Code version range.

  [Read the Week 23 digest →](/docs/en/whats-new/2026-w23)
</Update>

<Update label="Week 22" description="May 25–29, 2026" tags={["v2.1.150–v2.1.157"]}>
  **Claude Opus 4.8**: the new default model for Max, Team Premium, Enterprise pay-as-you-go, and Anthropic API accounts, with high effort by default and `/effort xhigh` for the hardest tasks.

  Also this week: **dynamic workflows** orchestrate dozens to hundreds of subagents from a script Claude writes; the **security-guidance plugin** reviews Claude's changes for vulnerabilities as it works; and **fast mode** runs on Opus 4.8 at \$10/\$50 per MTok.

  [Read the Week 22 digest →](/docs/en/whats-new/2026-w22)
</Update>

<Update label="Week 21" description="May 18–22, 2026" tags={["v2.1.143–v2.1.149"]}>
  **Auto mode on the Pro plan**: auto mode now runs on Pro accounts and supports Sonnet 4.6 alongside Opus, replacing permission prompts with background safety checks.

  Also this week: **`/usage`** breaks down what drives your plan limits by skill, subagent, plugin, and MCP server; the new **`/code-review`** command reports correctness bugs; and **background sessions** appear in `/resume` and stay alive when pinned.

  [Read the Week 21 digest →](/docs/en/whats-new/2026-w21)
</Update>

<Update label="Week 20" description="May 11–15, 2026" tags={["v2.1.139–v2.1.142"]}>
  **Agent view**: `claude agents` opens one screen for every Claude Code session, showing what's running, what's blocked on you, and what's done.

  Also this week: **`/goal`** keeps Claude working across turns until a completion condition holds; **fast mode** now runs on Opus 4.7 by default; and the **Rewind menu** can compress earlier context with "Summarize up to here".

  [Read the Week 20 digest →](/docs/en/whats-new/2026-w20)
</Update>

<Update label="Week 19" description="May 4–8, 2026" tags={["v2.1.128–v2.1.136"]}>
  **Plugins load from `.zip` archives and URLs**: `--plugin-dir` now accepts `.zip` files, and `--plugin-url` fetches a plugin archive for the current session.

  Also this week: **`worktree.baseRef`** chooses whether new worktrees branch from the remote default or local `HEAD`; **auto mode hard deny rules** block actions unconditionally regardless of allow exceptions; and **hooks see the active effort level** via `effort.level` and `$CLAUDE_EFFORT`.

  [Read the Week 19 digest →](/docs/en/whats-new/2026-w19)
</Update>

<Update label="Week 18" description="April 27 – May 1, 2026" tags={["v2.1.120–v2.1.126"]}>
  **Windows without Git Bash**: Git for Windows is no longer required, and Claude Code uses PowerShell as the shell tool when Bash is absent.

  Also this week: **`claude ultrareview`** brings cloud code review to CI and scripts; **`claude project purge`** cleans up local state for a project; and pasting a **PR URL into `/resume`** finds the session that created it.

  [Read the Week 18 digest →](/docs/en/whats-new/2026-w18)
</Update>

<Update label="Week 17" description="April 20–24, 2026" tags={["v2.1.114–v2.1.119"]}>
  **`/ultrareview`** opens as a public research preview: a fleet of bug-hunting agents runs in the cloud and findings land back in your CLI or Desktop automatically.

  Also this week: **session recap** shows you what happened while a terminal was unfocused; **custom themes** let you build and ship color palettes from `/theme` or a plugin; and **Claude Code on the web** gets a redesign with a new sessions sidebar and drag-and-drop layout.

  [Read the Week 17 digest →](/docs/en/whats-new/2026-w17)
</Update>

<Update label="Week 16" description="April 13–17, 2026" tags={["v2.1.105–v2.1.113"]}>
  **Claude Opus 4.7** lands as the new default on Max and Team Premium, with a new `xhigh` effort level that's the recommended setting for most coding work and an interactive `/effort` slider to dial it in.

  Also this week: **Routines** on Claude Code on the web fire templated cloud agents from a schedule, GitHub event, or API call; **mobile push notifications** ping your phone when a long task finishes or Claude needs you; `/usage` shows what's driving your limits; and the CLI moves to native binaries.

  [Read the Week 16 digest →](/docs/en/whats-new/2026-w16)
</Update>

<Update label="Week 15" description="April 6–10, 2026" tags={["v2.1.92–v2.1.101"]}>
  **Ultraplan** enters early preview: draft a plan in the cloud from your CLI, review and comment on it in a web editor, then run it remotely or pull it back local. The first run now auto-creates a cloud environment for you.

  Also this week: the **Monitor** tool streams background events into the conversation so Claude can tail logs and react live, `/loop` self-paces when you omit the interval, `/team-onboarding` packages your setup into a replayable guide, and `/autofix-pr` turns on PR auto-fix from your terminal.

  [Read the Week 15 digest →](/docs/en/whats-new/2026-w15)
</Update>

<Update label="Week 14" description="March 30 – April 3, 2026" tags={["v2.1.86–v2.1.91"]}>
  **Computer use** comes to the CLI in research preview: Claude can open native apps, click through UI, and verify changes from your terminal. Best for closing the loop on things only a GUI can verify.

  Also this week: `/powerup` interactive lessons, flicker-free alt-screen rendering, a per-tool MCP result-size override up to 500K, and plugin executables on the Bash tool's `PATH`.

  [Read the Week 14 digest →](/docs/en/whats-new/2026-w14)
</Update>

<Update label="Week 13" description="March 23–27, 2026" tags={["v2.1.83–v2.1.85"]}>
  **Auto mode** lands in research preview: a classifier handles your permission prompts so safe actions run without interruption and risky ones get blocked. The middle ground between approving everything and `--dangerously-skip-permissions`.

  Also this week: computer use in the Desktop app, PR auto-fix on Web, transcript search with `/`, a native PowerShell tool for Windows, and conditional `if` hooks.

  [Read the Week 13 digest →](/docs/en/whats-new/2026-w13)
</Update>
