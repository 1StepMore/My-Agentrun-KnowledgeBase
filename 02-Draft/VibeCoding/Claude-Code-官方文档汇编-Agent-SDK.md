---
title: Claude Code 官方文档汇编 · Agent SDK
source: Claude Code 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/claude-code/claude-code-en-agent-sdk-agent-loop.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-claude-code-features.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-configuration.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-cost-tracking.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-custom-tools.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-examples.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-file-checkpointing.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-hooks.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-hosting.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-mcp.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-migration-guide.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-modifying-system-prompts.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-observability.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-overview.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-permissions.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-plugins.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-quickstart.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-secure-deployment.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-session-storage.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-sessions.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-skills.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-streaming-output.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-streaming-vs-single-mode.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-structured-outputs.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-subagents.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-todo-tracking.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-tool-search.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-troubleshooting.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-typescript-v2-preview.md
- VibeCoding/claude-code/claude-code-en-agent-sdk-user-input.md
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

> **汇编性质**：Claude Code 官方文档 官方原文 30 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## How the agent loop works

- 官方原文：https://code.claude.com/docs/en/agent-sdk/agent-loop.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-agent-loop.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How the agent loop works

> Understand the message lifecycle, tool execution, context window, and architecture that power your SDK agents.

The Agent SDK lets you embed Claude Code's autonomous agent loop in your own applications. The SDK is a standalone package that gives you programmatic control over tools, permissions, cost limits, and output.

Both the TypeScript and Python SDKs bundle a native Claude Code binary, so most installs need no separate Claude Code install. See the [quickstart's install note](/docs/en/agent-sdk/quickstart) for the installs that do.

When you start an agent, the SDK runs the same [execution loop that powers Claude Code](/docs/en/how-claude-code-works#the-agentic-loop): Claude evaluates your prompt, calls tools to take action, receives the results, and repeats until the task is complete. This page explains what happens inside that loop so you can build, debug, and optimize your agents effectively.

## The loop at a glance

Every agent session follows the same cycle:

<img src="https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agent-loop-diagram.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=1c6e8f28d80dba14a7287419656f1237" className="dark:hidden" alt="Diagram of the agent loop: your prompt enters the agentic loop, where Claude evaluates and either requests tool calls, whose results feed back into another evaluation, or returns the final answer" width="720" height="212" data-path="images/agent-loop-diagram.svg" />

<img src="https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agent-loop-diagram-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=afe723c52a324d3c61fa72fb02432ab6" className="hidden dark:block" alt="Diagram of the agent loop: your prompt enters the agentic loop, where Claude evaluates and either requests tool calls, whose results feed back into another evaluation, or returns the final answer" width="720" height="212" data-path="images/agent-loop-diagram-dark.svg" />

1. **Receive prompt.** Claude receives your prompt, along with the system prompt, tool definitions, and conversation history. The SDK yields a [`SystemMessage`](#message-types) with subtype `"init"` containing session metadata.
2. **Evaluate and respond.** Claude evaluates the current state and determines how to proceed. It may respond with text, request one or more tool calls, or both. The SDK yields one or more [`AssistantMessage`](#message-types) objects, one for each content block, such as a text block or a tool call request.
3. **Execute tools.** The SDK runs each requested tool and collects the results. Each set of tool results feeds back to Claude for the next decision. You can use [hooks](/docs/en/agent-sdk/hooks) to intercept, modify, or block tool calls before they run.
4. **Repeat.** Steps 2 and 3 repeat as a cycle. Each full cycle is one turn. Claude continues calling tools and processing results until it produces a response with no tool calls.
5. **Return result.** The SDK yields a final [`AssistantMessage`](#message-types) with the text response (no tool calls), followed by a [`ResultMessage`](#message-types) with the final text, token usage, cost, and session ID.

A quick question ("what files are here?") might take one or two turns of calling `Glob` and responding with the results. A complex task ("refactor the auth module and update the tests") can chain dozens of tool calls across many turns, reading files, editing code, and running tests, with Claude adjusting its approach based on each result.

## Turns and messages

A turn is one round trip inside the loop: Claude produces output that includes tool calls, the SDK executes those tools, and the results feed back to Claude automatically. This happens without yielding control back to your code. Turns continue until Claude produces output with no tool calls, at which point the loop ends and the final result is delivered.

Consider what a full session might look like for the prompt "Fix the failing tests in auth.ts".

First, the SDK sends your prompt to Claude and yields a [`SystemMessage`](#message-types) with the session metadata. Then the loop begins:

1. **Turn 1:** Claude calls `Bash` to run `npm test`. The SDK yields an [`AssistantMessage`](#message-types) with the tool call, executes the command, then yields a [`UserMessage`](#message-types) with the output (three failures).
2. **Turn 2:** Claude calls `Read` on `auth.ts` and `auth.test.ts`. The SDK yields an `AssistantMessage` for each call and returns the file contents.
3. **Turn 3:** Claude calls `Edit` to fix `auth.ts`, then calls `Bash` to re-run `npm test`. All three tests pass. The SDK yields an `AssistantMessage` for each call.
4. **Final turn:** Claude produces a text-only response with no tool calls: "Fixed the auth bug, all three tests pass now." The SDK yields a final `AssistantMessage` with this text, then a [`ResultMessage`](#message-types) with the same text plus cost and usage.

That was four turns: three with tool calls, one final text-only response.

You can cap the loop with `max_turns` / `maxTurns`, which counts tool-use turns only. For example, `max_turns=2` in the loop above would have stopped before the edit step. You can also use `max_budget_usd` / `maxBudgetUsd` to cap turns based on a spend threshold.

Without limits, the loop runs until Claude finishes on its own, which is fine for well-scoped tasks but can run long on open-ended prompts ("improve this codebase"). Setting a budget is a good default for production agents. See [Turns and budget](#turns-and-budget) below for the option reference.

## Message types

As the loop runs, the SDK yields a stream of messages. Each message carries a type that tells you what stage of the loop it came from. The five core types are:

* **`SystemMessage`:** session lifecycle events. The `subtype` field distinguishes them:

  * `"init"`: session metadata for the run. When a `SessionStart` or `Setup` hook runs during session startup, its [hook lifecycle messages](/docs/en/agent-sdk/typescript#sdkhookstartedmessage) arrive before the `init` message
  * `"compact_boundary"`: fires after [compaction](#automatic-compaction)
  * `"informational"`: plain-text status banners from the loop
  * `"worker_shutting_down"`: the host is exiting or Remote Control disconnected

  In TypeScript, each subtype other than `"init"` is its own type in the [`SDKMessage` union](/docs/en/agent-sdk/typescript#sdkmessage) rather than a subtype of `SDKSystemMessage`.
* **`AssistantMessage`:** emitted for each content block in Claude's responses, including the final text-only one. Each carries a single content block, such as text or a tool call, and the messages from one response share a message ID.
* **`UserMessage`:** emitted after each tool execution with the tool result content sent back to Claude. Also emitted for any user inputs you stream mid-loop.
* **`StreamEvent`:** only emitted when partial messages are enabled. Contains raw API streaming events (text deltas, tool input chunks). See [Stream responses](/docs/en/agent-sdk/streaming-output).
* **`ResultMessage`:** marks the end of the agent loop. Contains the final text result, token usage, cost, and session ID. Check the `subtype` field to determine whether the task succeeded or hit a limit. A small number of trailing system events, such as `prompt_suggestion`, can arrive after it, so iterate the stream to completion rather than breaking on the result. See [Handle the result](#handle-the-result).

These five types cover the full agent loop lifecycle. Both SDKs also yield observability events such as rate-limit status and task notifications that are not required to drive the loop. See the [Python message types reference](/docs/en/agent-sdk/python#message-types) and [TypeScript message types reference](/docs/en/agent-sdk/typescript#message-types) for the complete lists.

### Handle messages

Which messages you handle depends on what you're building:

* **Final results only:** handle `ResultMessage` to get the output, cost, and whether the task succeeded or hit a limit.
* **Progress updates:** handle `AssistantMessage` to see what Claude is doing each turn, including which tools it called.
* **Live streaming:** enable partial messages (`include_partial_messages` in Python, `includePartialMessages` in TypeScript) to get `StreamEvent` messages in real time. See [Stream responses in real-time](/docs/en/agent-sdk/streaming-output).

How you check message types depends on the SDK:

* **Python:** check message types with `isinstance()` against classes imported from `claude_agent_sdk` (for example, `isinstance(message, ResultMessage)`).
* **TypeScript:** check the `type` string field (for example, `message.type === "result"`). `AssistantMessage` and `UserMessage` wrap the raw API message in a `.message` field, so content blocks are at `message.message.content`, not `message.content`.

<Accordion title="Example: Check message types and handle results">
  <CodeGroup>
    ```python Python theme={null}
    import asyncio
    from claude_agent_sdk import query, AssistantMessage, ResultMessage, TextBlock, ToolUseBlock

    async def main():
        try:
            async for message in query(prompt="Summarize this project"):
                if isinstance(message, AssistantMessage):
                    # Each AssistantMessage carries one content block
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"Claude: {block.text}")
                        elif isinstance(block, ToolUseBlock):
                            print(f"Tool call: {block.name}")
                if isinstance(message, ResultMessage):
                    if message.subtype == "success":
                        print(message.result)
                    else:
                        print(f"Stopped: {message.subtype}")
        except Exception as error:
            # A single-shot query() raises after yielding an error result. If the
            # failure was an error result, the error subtype branches above have
            # already run; connection or process failures yield no result message.
            print(f"Session ended with an error: {error}")

    asyncio.run(main())
    ```

    ```typescript TypeScript theme={null}

    try {
      for await (const message of query({ prompt: "Summarize this project" })) {
        if (message.type === "assistant") {
          // Each assistant message carries one content block
          for (const block of message.message.content) {
            if (block.type === "text") {
              console.log(`Claude: ${block.text}`);
            } else if (block.type === "tool_use") {
              console.log(`Tool call: ${block.name}`);
            }
          }
        }
        if (message.type === "result") {
          if (message.subtype === "success") {
            console.log(message.result);
          } else {
            console.log(`Stopped: ${message.subtype}`);
          }
        }
      }
    } catch (error) {
      // A single-shot query() throws after yielding an error result. If the
      // failure was an error result, the error subtype branches above have
      // already run; connection or process failures yield no result message.
      console.log(`Session ended with an error: ${error}`);
    }
    ```
  </CodeGroup>
</Accordion>

## Tool execution

Tools give your agent the ability to take action. Without tools, Claude can only respond with text. With tools, Claude can read files, run commands, search code, and interact with external services.

### Built-in tools

The SDK includes the same tools that power Claude Code:

| Category            | Tools                                                           | What they do                                                                |
| :------------------ | :-------------------------------------------------------------- | :-------------------------------------------------------------------------- |
| **File operations** | `Read`, `Edit`, `Write`                                         | Read, modify, and create files                                              |
| **Search**          | `Glob`, `Grep`                                                  | Find files by pattern, search content with regex                            |
| **Execution**       | `Bash`                                                          | Run shell commands, scripts, git operations                                 |
| **Web**             | `WebSearch`, `WebFetch`                                         | Search the web, fetch and parse pages                                       |
| **Discovery**       | `ToolSearch`                                                    | Dynamically find and load tools on-demand instead of preloading all of them |
| **Orchestration**   | `Agent`, `Skill`, `AskUserQuestion`, `TaskCreate`, `TaskUpdate` | Spawn subagents, invoke skills, ask the user, track tasks                   |

On the [models that don't get the task-tracking tools](/docs/en/agent-sdk/todo-tracking#model-availability), Claude Code provides `TaskCreate` and `TaskUpdate` only when you opt in.

Beyond built-in tools, you can:

* **Connect external services** with [MCP servers](/docs/en/agent-sdk/mcp) (databases, browsers, APIs)
* **Define custom tools** with [custom tool handlers](/docs/en/agent-sdk/custom-tools)
* **Load project skills** via [setting sources](/docs/en/agent-sdk/claude-code-features) for reusable workflows

### Tool permissions

Claude determines which tools to call based on the task, but you control whether those calls are allowed to execute. You can auto-approve specific tools, block others entirely, or require approval for everything. Three options work together to determine what runs:

* **`allowed_tools` / `allowedTools`** auto-approves listed tools. A read-only agent with `["Read", "Glob", "Grep"]` in its allowed tools list runs those tools without prompting. Tools not listed are still available, and calls to them that need approval fall through to the permission mode and `canUseTool`.
* **`disallowed_tools` / `disallowedTools`** blocks listed tools, regardless of other settings. See [Permissions](/docs/en/agent-sdk/permissions) for the order that rules are checked before a tool runs.
* **`permission_mode` / `permissionMode`** controls how much human oversight you want. The SDK evaluates the active mode together with your allow and deny rules in a fixed order, described in [How permissions are evaluated](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated). See [Permission mode](#permission-mode) for available modes.

You can also scope individual tools with rules like `"Bash(npm *)"` to allow only specific commands. See [Permissions](/docs/en/agent-sdk/permissions) for the full rule syntax.

When a tool is denied, Claude receives a rejection message as the tool result and typically attempts a different approach or reports that it couldn't proceed.

### Parallel tool execution

When Claude requests multiple tool calls in a single turn, both SDKs can run them concurrently or sequentially depending on the tool. Read-only tools (like `Read`, `Glob`, `Grep`, and MCP tools marked as read-only) can run concurrently. Tools that modify state (like `Edit`, `Write`, and `Bash`) run sequentially to avoid conflicts.

Custom tools default to sequential execution. To enable parallel execution for a custom tool, set `readOnlyHint` in its annotations. Both the [TypeScript](/docs/en/agent-sdk/typescript#tool) and [Python](/docs/en/agent-sdk/python#tool) SDKs use this field name from the MCP SDK.

## Control how the loop runs

You can limit how many turns the loop takes, how much it costs, how deeply Claude reasons, and whether tools require approval before running. All of these are fields on [`ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions) (Python) / [`Options`](/docs/en/agent-sdk/typescript#options) (TypeScript).

### Turns and budget

| Option                                         | What it controls             | Default  |
| :--------------------------------------------- | :--------------------------- | :------- |
| Max turns (`max_turns` / `maxTurns`)           | Maximum tool-use round trips | No limit |
| Max budget (`max_budget_usd` / `maxBudgetUsd`) | Maximum cost before stopping | No limit |

When either limit is hit, the SDK returns a `ResultMessage` with a corresponding error subtype (`error_max_turns` or `error_max_budget_usd`). See [Handle the result](#handle-the-result) for how to check these subtypes and [`ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions) / [`Options`](/docs/en/agent-sdk/typescript#options) for syntax.

The budget cap covers [subagents](/docs/en/agent-sdk/subagents): their spend counts toward the total. Once spend reaches the cap, spawning another subagent fails with `Budget limit reached`, and Claude Code stops any background subagents still running. The cap-enforcement behaviors require Claude Code v2.1.217 or later.

With [streaming input](/docs/en/agent-sdk/streaming-vs-single-mode), a message that is still queued when a turn ends at the max-turns limit stays queued. Claude Code doesn't add it to that turn's last model call. It starts a new turn for the message, and the max-turns count starts over for that turn. The budget total keeps accumulating across messages, and once spend reaches `maxBudgetUsd`, later messages in the same conversation end with the `error_max_budget_usd` result. A [`/clear`](/docs/en/agent-sdk/cost-tracking) starts the budget over.

### Effort level

The `effort` option controls how much reasoning Claude applies. Lower effort levels use fewer tokens per turn and reduce cost. Not all models support the effort parameter. See [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) for which models support it.

| Level      | Behavior                          | Good for                                                                                       |
| :--------- | :-------------------------------- | :--------------------------------------------------------------------------------------------- |
| `"low"`    | Minimal reasoning, fast responses | File lookups, listing directories                                                              |
| `"medium"` | Balanced reasoning                | Routine edits, standard tasks                                                                  |
| `"high"`   | Thorough analysis                 | Refactors, debugging                                                                           |
| `"xhigh"`  | Extended reasoning depth          | Coding and agentic tasks on the [models that support it](/docs/en/model-config#adjust-effort-level) |
| `"max"`    | Maximum reasoning depth           | Multi-step problems requiring deep analysis                                                    |

If you don't set `effort`, Claude Code resolves the effort level itself, in the order [Adjust effort level](/docs/en/model-config#adjust-effort-level) describes.

<Note>
  `effort` trades latency and token cost for reasoning depth within each response. [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) is a separate feature that produces `thinking` blocks in the output, and the `display` field on `ThinkingConfig` for [Python](/docs/en/agent-sdk/python#thinkingconfig) or [TypeScript](/docs/en/agent-sdk/typescript#thinkingconfig) controls whether you receive their text. They are independent: you can set `effort: "low"` with extended thinking enabled, or `effort: "max"` without it.
</Note>

Use lower effort for agents doing simple, well-scoped tasks (like listing files or running a single grep) to reduce cost and latency. Set `effort` in the top-level `query()` options for the whole session, or per subagent with the `effort` field on [`AgentDefinition`](/docs/en/agent-sdk/subagents#agentdefinition-configuration) to override the session level.

### Permission mode

The permission mode option (`permission_mode` in Python, `permissionMode` in TypeScript) controls whether the agent asks for approval before using tools:

| Mode                  | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Use case                                                                                                                                      |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `"default"`           | Tool calls that need approval and aren't covered by allow rules trigger your `canUseTool` callback; no callback means deny                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Interactive applications with a custom approval callback                                                                                      |
| `"acceptEdits"`       | Auto-approves file edits and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.); other Bash commands follow default rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | You trust Claude's edits and want faster iteration, such as during prototyping or when working in an isolated directory                       |
| `"plan"`              | Claude explores and plans without editing your source files; file edits are never auto-approved and prompt through your `canUseTool` callback                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | You want Claude to propose changes without executing them, such as during code review or when you need to approve changes before they're made |
| `"dontAsk"`           | Never prompts. Tools pre-approved by [permission rules](/docs/en/settings-reference#permission-settings) run, and so do calls that need no approval in `default` mode, such as file reads inside your working directories; every call that would otherwise prompt is denied. `AskUserQuestion`, connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), and MCP tools marked [`requiresUserInteraction`](/docs/en/mcp#require-approval-for-a-specific-tool) are denied even if you've allowed them                                                                                                                                                                                                                                    | You want a fixed, explicit tool surface for a headless agent and prefer a hard deny over silent reliance on `canUseTool` being absent         |
| `"auto"`              | Uses a model classifier to approve or deny permission prompts. See [Auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for availability and behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Autonomous agents that still want safety guardrails on tool use                                                                               |
| `"bypassPermissions"` | Runs all allowed tools without asking, except tools matched by an explicit [`ask` rule](/docs/en/settings-reference#permission-settings), connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), and tools that require user interaction. The [cross-session messaging safeguards](/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode) still apply. See [How permissions are evaluated](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) for the precedence order. In the TypeScript SDK, also requires `allowDangerouslySkipPermissions: true` in `options`. Can't be used when running as root on Unix. Use only in isolated environments where the agent's actions can't affect systems you care about | CI, containers, or other isolated environments                                                                                                |

For interactive applications, use `"default"` with a tool approval callback to surface approval prompts. For autonomous agents on a dev machine, `"acceptEdits"` auto-approves file edits and common filesystem commands (`mkdir`, `touch`, `mv`, `cp`, etc.) while still gating other `Bash` commands behind allow rules. Reserve `"bypassPermissions"` for CI, containers, or other isolated environments. See [Permissions](/docs/en/agent-sdk/permissions) for full details.

### Model

Set the `model` option to choose which model runs the session. For more information, see [Choose a model](/docs/en/agent-sdk/configuration#choose-a-model).

## The context window

The context window is the total amount of information available to Claude during a session. It does not reset between turns within a session. Everything accumulates: the system prompt, tool definitions, conversation history, tool inputs, and tool outputs. Content that stays the same across turns (system prompt, tool definitions, CLAUDE.md) is automatically [prompt cached](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), which reduces cost and latency for repeated prefixes. For how a custom system prompt or `append` text affects cache reuse across sessions, see [Modifying system prompts](/docs/en/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines).

### What consumes context

Here's how each component affects context in the SDK:

| Source                   | When it loads                                                             | Impact                                                                                                                                                                                                                                                                                                       |
| :----------------------- | :------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **System prompt**        | Every request                                                             | Small fixed cost, always present                                                                                                                                                                                                                                                                             |
| **CLAUDE.md files**      | Session start, via [`settingSources`](/docs/en/agent-sdk/claude-code-features) | Full content in every request (but prompt-cached, so only the first request pays full cost)                                                                                                                                                                                                                  |
| **Tool definitions**     | Every request; MCP schemas deferred by default                            | Built-in tool schemas load every request. [Tool search](/docs/en/agent-sdk/mcp#mcp-tool-search) defers MCP tool schemas by default, falling back to upfront loading on unsupported models and certain platforms. See [Configure tool search](/docs/en/agent-sdk/tool-search#configure-tool-search) for the full matrix |
| **Conversation history** | Accumulates over turns                                                    | Grows with each turn: prompts, responses, tool inputs, tool outputs                                                                                                                                                                                                                                          |
| **Skill descriptions**   | Session start, via setting sources                                        | Short summaries; full content loads only when invoked                                                                                                                                                                                                                                                        |

Large tool outputs consume significant context. Reading a big file or running a command with verbose output can use thousands of tokens in a single turn. Context accumulates across turns, so longer sessions with many tool calls build up significantly more context than short ones.

### Automatic compaction

When the context window approaches its limit, the SDK automatically compacts the conversation: it summarizes older history to free space, keeping your most recent exchanges and key decisions intact. The SDK emits a message with `type: "system"` and `subtype: "compact_boundary"` in the stream when this happens (in Python this is a `SystemMessage`; in TypeScript it is a separate `SDKCompactBoundaryMessage` type).

Compaction replaces older messages with a summary, so specific instructions from early in the conversation may not be preserved. Persistent rules belong in CLAUDE.md (loaded via [`settingSources`](/docs/en/agent-sdk/claude-code-features)) rather than in the initial prompt, because CLAUDE.md content is re-injected on every request.

You can customize compaction behavior in several ways:

* **Summarization instructions in CLAUDE.md:** The compactor reads your CLAUDE.md like any other context, so you can include a section telling it what to preserve when summarizing. The compactor matches on intent, so the section header is free-form.
* **`PreCompact` hook:** Run custom logic before compaction occurs, for example to archive the full transcript. The hook receives a `trigger` field (`manual` or `auto`). See [hooks](/docs/en/agent-sdk/hooks).
* **Manual compaction:** Send `/compact` as a prompt string to trigger compaction on demand. Commands sent this way are ordinary SDK inputs. See [dispatch commands by name](/docs/en/agent-sdk/skills#dispatch-commands-by-name).

<Accordion title="Example: Summarization instructions in CLAUDE.md">
  Add a section to your project's CLAUDE.md telling the compactor what to preserve. The header name isn't special; use any clear label.

  ```markdown CLAUDE.md theme={null}
  # Summary instructions

  When summarizing this conversation, always preserve:
  - The current task objective and acceptance criteria
  - File paths that have been read or modified
  - Test results and error messages
  - Decisions made and the reasoning behind them
  ```
</Accordion>

### Keep context efficient

A few strategies for long-running agents:

* **Use subagents for subtasks.** Each subagent starts with a fresh conversation (no prior message history, though it does load its own system prompt and project-level context like CLAUDE.md). It does not see the parent's turns, and only its final response returns to the parent as a tool result. The main agent's context grows by that summary, not by the full subtask transcript. See [What subagents inherit](/docs/en/agent-sdk/subagents#what-subagents-inherit) for details.
* **Be selective with tools.** Every tool definition takes context space. Use the `tools` field on [`AgentDefinition`](/docs/en/agent-sdk/subagents#agentdefinition-configuration) to scope subagents to the minimum set they need.
* **Watch MCP server costs.** [MCP tool search](/docs/en/agent-sdk/mcp#mcp-tool-search) defers MCP tool schemas by default and loads them on demand. When tool search is off or has fallen back to upfront loading, each MCP server adds all its tool schemas to every request, so a few servers with many tools can consume significant context before the agent does any work. See [Configure tool search](/docs/en/agent-sdk/tool-search#configure-tool-search) for the configurations where the fallback applies.
* **Use lower effort for routine tasks.** Set [effort](#effort-level) to `"low"` for agents that only need to read files or list directories. This reduces token usage and cost.

For a detailed breakdown of per-feature context costs, see [Understand context costs](/docs/en/features-overview#understand-context-costs).

## Sessions and continuity

Each interaction with the SDK creates or continues a session. Capture the session ID from `ResultMessage.session_id` (available in both SDKs) to resume later. The TypeScript SDK also exposes it as a direct field on the init `SystemMessage`; in Python it's nested in `SystemMessage.data`.

When you resume, the full context from previous turns is restored: files that were read, analysis that was performed, and actions that were taken. You can also fork a session to branch into a different approach without modifying the original.

See [Session management](/docs/en/agent-sdk/sessions) for the full guide on resume, continue, and fork patterns. To resume sessions across stateless containers or serverless hosts, pass a [`session_store` / `sessionStore` adapter](/docs/en/agent-sdk/session-storage) so the SDK mirrors transcripts to your own backend and another host can resume them. The Claude Code subprocess still writes to local disk first. See [Dual-write architecture](/docs/en/agent-sdk/session-storage#dual-write-architecture) for which copy outlives a fresh session versus a run resumed from the store, and how to keep the local copy ephemeral.

<Note>
  In Python, `ClaudeSDKClient` handles session IDs automatically across multiple calls. See the [Python SDK reference](/docs/en/agent-sdk/python#choosing-between-query-and-claudesdkclient) for details.
</Note>

## Handle the result

When the loop ends, the `ResultMessage` tells you what happened and gives you the output. The `subtype` field (available in both SDKs) is the primary way to check termination state.

| Result subtype                        | What happened                                                                                                                                                                           | `result` field available? |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------------: |
| `success`                             | Claude finished the task normally                                                                                                                                                       |            Yes            |
| `error_max_turns`                     | Hit the `maxTurns` limit before finishing                                                                                                                                               |             No            |
| `error_max_budget_usd`                | Hit the `maxBudgetUsd` limit before finishing                                                                                                                                           |             No            |
| `error_during_execution`              | An error interrupted the loop (for example, a cancelled request)                                                                                                                        |             No            |
| `error_max_structured_output_retries` | No valid structured output was produced within the configured retry limit: every attempt failed validation, or a model fallback retracted the completed output with no successful retry |             No            |

The `result` field holds the final text output and is only present on the `success` variant, so always check the subtype before reading it.

All result subtypes carry `total_cost_usd`, `usage`, `num_turns`, and `session_id` so you can track cost and resume even after errors. Guard for these cases:

* After a session crash, the final result is an `error_during_execution` whose cost fields may be zeroed and whose `stop_reason` is `null`, and the process exits after emitting it. See [Recover totals after a session crash](/docs/en/agent-sdk/cost-tracking#recover-totals-after-a-session-crash).
* In Python, `total_cost_usd`, `usage`, and `model_usage` are typed as optional, so check that they aren't `None` before you read them.

The `usage` field covers only the main agent loop. Use `modelUsage`, or `model_usage` in Python, for whole-tree token and cost accounting. See [Tracking costs and usage](/docs/en/agent-sdk/cost-tracking) for details on interpreting the `usage` fields.

<Note>
  When a query ends on an error result:

  * A single-shot `query()` call yields the final result message, then raises an error that includes the failure text, such as `Reached maximum number of turns`. The raise is intentional. Wrap the loop in a try block if your code needs to continue past it. The underlying Claude Code process also exits with a nonzero code.
  * A streaming input session stays alive, and you can keep sending messages, except after a session crash, which emits a final `error_during_execution` result and exits the process.
</Note>

The result also includes a `stop_reason` field (`string | null` in TypeScript, `str | None` in Python) indicating why the model stopped generating on its final turn. Common values are `end_turn` (model finished normally), `max_tokens` (hit the output token limit), and `refusal` (the model declined the request). On error results that the loop produced, `stop_reason` carries the value from the last assistant response before the loop ended; the result Claude Code synthesizes after a session crash carries `null`.

To detect refusals, check `stop_reason === "refusal"` (TypeScript) or `stop_reason == "refusal"` (Python). See [`SDKResultMessage`](/docs/en/agent-sdk/typescript#sdkresultmessage) (TypeScript) or [`ResultMessage`](/docs/en/agent-sdk/python#resultmessage) (Python) for the full type.

## Hooks

[Hooks](/docs/en/agent-sdk/hooks) are callbacks that fire at specific points in the loop: before a tool runs, after it returns, when the agent finishes, and so on. Some commonly used hooks are:

| Hook                             | When it fires                       | Common uses                                |
| :------------------------------- | :---------------------------------- | :----------------------------------------- |
| `PreToolUse`                     | Before a tool executes              | Validate inputs, block dangerous commands  |
| `PostToolUse`                    | After a tool returns                | Audit outputs, trigger side effects        |
| `UserPromptSubmit`               | When a prompt is sent               | Inject additional context into prompts     |
| `Stop`                           | When the agent finishes             | Validate the result, save session state    |
| `SubagentStart` / `SubagentStop` | When a subagent spawns or completes | Track and aggregate parallel task results  |
| `PreCompact`                     | Before context compaction           | Archive full transcript before summarizing |

Hooks run in your application process, not inside the agent's context window, so they don't consume context. Hooks can also short-circuit the loop: a `PreToolUse` hook that rejects a tool call prevents it from executing, and Claude receives the rejection message instead.

Both SDKs support all the events above. The TypeScript SDK includes additional events that Python does not yet support. See [Control execution with hooks](/docs/en/agent-sdk/hooks) for the complete event list, per-SDK availability, and the full callback API.

## Put it all together

This example combines the key concepts from this page into a single agent that fixes failing tests. It configures the agent with allowed tools (auto-approved so the agent runs autonomously), project settings, and safety limits on turns and reasoning effort. As the loop runs, it captures the session ID for potential resumption, handles the final result, and prints the total cost.

Because a single-shot `query()` call raises after yielding an error result, the loop is wrapped in a try block so the script exits cleanly when a limit is hit.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def run_agent():
      session_id = None

      try:
          async for message in query(
              prompt="Find and fix the bug causing test failures in the auth module",
              options=ClaudeAgentOptions(
                  allowed_tools=[
                      "Read",
                      "Edit",
                      "Bash",
                      "Glob",
                      "Grep",
                  ],  # Listing tools here auto-approves them (no prompting)
                  setting_sources=[
                      "project"
                  ],  # Load CLAUDE.md, skills, hooks from current directory
                  max_turns=30,  # Prevent runaway sessions
                  effort="high",  # Thorough reasoning for complex debugging
              ),
          ):
              # Handle the final result
              if isinstance(message, ResultMessage):
                  session_id = message.session_id  # Save for potential resumption

                  if message.subtype == "success":
                      print(f"Done: {message.result}")
                  elif message.subtype == "error_max_turns":
                      # Agent ran out of turns. Resume with a higher limit.
                      print(f"Hit turn limit. Resume session {session_id} to continue.")
                  elif message.subtype == "error_max_budget_usd":
                      print("Hit budget limit.")
                  else:
                      print(f"Stopped: {message.subtype}")
                  if message.total_cost_usd is not None:
                      print(f"Cost: ${message.total_cost_usd:.4f}")
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, the error subtype branches above have
          # already run; connection or process failures yield no result message.
          print(f"Session ended with an error: {error}")

  asyncio.run(run_agent())
  ```

  ```typescript TypeScript theme={null}

  let sessionId: string | undefined;

  try {
    for await (const message of query({
      prompt: "Find and fix the bug causing test failures in the auth module",
      options: {
        allowedTools: ["Read", "Edit", "Bash", "Glob", "Grep"], // Listing tools here auto-approves them (no prompting)
        settingSources: ["project"], // Load CLAUDE.md, skills, hooks from current directory
        maxTurns: 30, // Prevent runaway sessions
        effort: "high" // Thorough reasoning for complex debugging
      }
    })) {
      // Save the session ID to resume later if needed
      if (message.type === "system" && message.subtype === "init") {
        sessionId = message.session_id;
      }

      // Handle the final result
      if (message.type === "result") {
        if (message.subtype === "success") {
          console.log(`Done: ${message.result}`);
        } else if (message.subtype === "error_max_turns") {
          // Agent ran out of turns. Resume with a higher limit.
          console.log(`Hit turn limit. Resume session ${sessionId} to continue.`);
        } else if (message.subtype === "error_max_budget_usd") {
          console.log("Hit budget limit.");
        } else {
          console.log(`Stopped: ${message.subtype}`);
        }
        console.log(`Cost: $${message.total_cost_usd.toFixed(4)}`);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, the error subtype branches above have
    // already run; connection or process failures yield no result message.
    console.log(`Session ended with an error: ${error}`);
  }
  ```
</CodeGroup>

When the agent finishes successfully, the example prints a `Done:` line with the agent's summary of the fix, then a line like `Cost: $0.0312`.

## Next steps

Now that you understand the loop, here's where to go depending on what you're building:

* **Haven't run an agent yet?** Start with the [quickstart](/docs/en/agent-sdk/quickstart) to get the SDK installed and see a full example running end to end.
* **Ready to hook into your project?** [Load CLAUDE.md, skills, and filesystem hooks](/docs/en/agent-sdk/claude-code-features) so the agent follows your project conventions automatically.
* **Building an interactive UI?** Enable [streaming](/docs/en/agent-sdk/streaming-output) to show live text and tool calls as the loop runs.
* **Need tighter control over what the agent can do?** Lock down tool access with [permissions](/docs/en/agent-sdk/permissions), and use [hooks](/docs/en/agent-sdk/hooks) to audit, block, or transform tool calls before they execute.
* **Running long or expensive tasks?** Offload isolated work to [subagents](/docs/en/agent-sdk/subagents) to keep your main context lean.
* **Deploying as a service?** See [Hosting the Agent SDK](/docs/en/agent-sdk/hosting) for container and serverless guidance, and [Session storage](/docs/en/agent-sdk/session-storage) to persist sessions to your own backend.

For the broader conceptual picture of the agentic loop (not SDK-specific), see [How Claude Code works](/docs/en/how-claude-code-works). For a practical guide to designing loops in Claude Code, from turn-based to goal-based and proactive loops, see [Loop engineering: getting started with loops](https://claude.com/blog/getting-started-with-loops) on the blog.

---

## Use Claude Code features in the SDK

- 官方原文：https://code.claude.com/docs/en/agent-sdk/claude-code-features.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-claude-code-features.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude Code features in the SDK

> Load project instructions, skills, hooks, and other Claude Code features into your SDK agents.

The Agent SDK is built on the same foundation as Claude Code, which means your SDK agents have access to the same filesystem-based features: project instructions (`CLAUDE.md` and rules), skills, hooks, and more.

When you omit `settingSources`, `query()` reads the same filesystem settings as the Claude Code CLI: user, project, and local settings, CLAUDE.md files, and `.claude/` skills, agents, and commands. To run without these, pass `settingSources: []`, which limits the agent to what you configure programmatically. Managed policy settings and the global `~/.claude.json` config are read regardless of this option. For more information, see [What settingSources does not control](#what-settingsources-does-not-control).

## Control filesystem settings with settingSources

The setting sources option ([`setting_sources`](/docs/en/agent-sdk/python#claudeagentoptions) in Python, [`settingSources`](/docs/en/agent-sdk/typescript#settingsource) in TypeScript) controls which filesystem-based settings the SDK loads. Pass an explicit list to opt in to specific sources, or pass an empty array to disable user, project, and local settings.

This example loads both user-level and project-level settings by setting `settingSources` to `["user", "project"]`:

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage
  import asyncio

  async def main():
      async for message in query(
          prompt="Help me refactor the auth module",
          options=ClaudeAgentOptions(
              # "user" loads from ~/.claude/, "project" loads from ./.claude/ in cwd.
              # Together they give the agent access to CLAUDE.md, skills, hooks, and
              # permissions from both locations.
              setting_sources=["user", "project"],
              allowed_tools=["Read", "Edit", "Bash"],
          ),
      ):
          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if hasattr(block, "text"):
                      print(block.text)
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(f"\nResult: {message.result}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Help me refactor the auth module",
    options: {
      // "user" loads from ~/.claude/, "project" loads from ./.claude/ in cwd.
      // Together they give the agent access to CLAUDE.md, skills, hooks, and
      // permissions from both locations.
      settingSources: ["user", "project"],
      allowedTools: ["Read", "Edit", "Bash"]
    }
  })) {
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if (block.type === "text") console.log(block.text);
      }
    }
    if (message.type === "result" && message.subtype === "success") {
      console.log(`\nResult: ${message.result}`);
    }
  }
  ```
</CodeGroup>

When this runs, the assistant's response prints to stdout, followed by a final result line once the run completes.

Each source loads settings from a specific location, where `<cwd>` is the working directory you pass via the `cwd` option, or the process's current directory if unset. For the full type definition, see [`SettingSource`](/docs/en/agent-sdk/typescript#settingsource) (TypeScript) or [`SettingSource`](/docs/en/agent-sdk/python#settingsource) (Python).

| Source      | What it loads                                                                                                          | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------- | :--------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"project"` | Project `settings.json` and hooks; project CLAUDE.md and `.claude/rules/*.md`; project skills, commands, and subagents | `<cwd>/.claude/` for `settings.json` and hooks; `<cwd>` and every parent directory for CLAUDE.md and rules; `<cwd>` and every parent directory up to the repository root for skills, commands, and subagents, plus the `.claude/skills/`, `.claude/commands/`, and `.claude/agents/` folders of each directory you pass through the `additionalDirectories` or `add_dirs` option, which the SDK passes to Claude Code as [`--add-dir`](/docs/en/permissions#additional-directories-grant-file-access-not-configuration) |
| `"user"`    | User `settings.json`; user CLAUDE.md and `~/.claude/rules/*.md`; user skills, commands, and subagents                  | `~/.claude/` for `settings.json`, CLAUDE.md, and rules; `~/.claude/skills/`, `~/.claude/commands/`, and `~/.claude/agents/` for skills, commands, and subagents                                                                                                                                                                                                                                                                                                                                                    |
| `"local"`   | CLAUDE.local.md, `.claude/settings.local.json`                                                                         | `<cwd>/.claude/` for `settings.local.json`; `<cwd>` and every parent directory for CLAUDE.local.md                                                                                                                                                                                                                                                                                                                                                                                                                 |

Omitting `settingSources` is equivalent to `["user", "project", "local"]`.

The `cwd` option determines where the SDK looks for project-level inputs. Project `settings.json` and hooks load only from `<cwd>/.claude/` with no parent-directory fallback.

### What settingSources does not control

`settingSources` covers user, project, and local settings. A few inputs are read regardless of its value:

| Input                                                                                                                           | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | To disable                                                                                                                                                                                                                                                 |
| :------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Managed policy settings                                                                                                         | Endpoint-managed policy, such as an MDM plist, registry policy, or managed settings file, loads from the host. [Server-managed settings](/docs/en/server-managed-settings) are fetched on an [eligible configuration](/docs/en/server-managed-settings#platform-availability) when the session authenticates with a qualifying credential, such as an organization OAuth login, a directly configured API key, or a `user_oauth` [Anthropic profile](/docs/en/authentication#anthropic-profiles-and-federation-credentials) | Endpoint policy: remove the managed settings file, plist, or registry policy from the host. Server-managed settings: an [Owner](/docs/en/server-managed-settings#access-control) in your Claude organization controls them; you can't disable them from the SDK |
| `~/.claude.json` global config                                                                                                  | Always read                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Relocate with `CLAUDE_CONFIG_DIR` in `env`                                                                                                                                                                                                                 |
| Auto memory at `~/.claude/projects/<project>/memory/`                                                                           | Loaded into the system prompt at session start. The agent writes new memories there with the standard `Write` and `Edit` tools rather than a dedicated memory tool, so those tools must be enabled for the agent to save memories                                                                                                                                                                                                                                                                            | Set `autoMemoryEnabled: false` in settings, or `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env`                                                                                                                                                                |
| [claude.ai MCP connectors](/docs/en/mcp#use-mcp-servers-from-claude-ai)                                                              | Loaded when the session authenticates with your claude.ai login. Not loaded when `CLAUDE_CODE_OAUTH_TOKEN` holds a token from [`claude setup-token`](/docs/en/authentication#generate-a-long-lived-token), which can only make model requests. Passing `mcpServers: {}` does not suppress the connectors                                                                                                                                                                                                          | Set `strictMcpConfig: true`, [`disableClaudeAiConnectors: true`](/docs/en/mcp#disable-claude-ai-connectors) in settings, or `ENABLE_CLAUDEAI_MCP_SERVERS=false` in `env`                                                                                        |
| [`sandbox.credentials`](/docs/en/sandboxing#protect-credentials) `deny` entries and file `mask` entries in `~/.claude/settings.json` | When the [command sandbox](/docs/en/sandboxing) runs, Claude Code applies the `deny` entries and keeps the `credentials.files` `mask` entries as restrictions even when `settingSources` excludes user settings. Claude Code uses these entries only to narrow what sandboxed commands can access                                                                                                                                                                                                                 | Remove the entries from `~/.claude/settings.json`                                                                                                                                                                                                          |

<Warning>
  Do not rely on default `query()` options for multi-tenant isolation. Because the inputs above are read regardless of `settingSources`, an SDK process can pick up host-level configuration and per-directory memory. For multi-tenant deployments, run each tenant in its own filesystem and set `settingSources: []` plus `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env`. [Server-managed settings](/docs/en/server-managed-settings) are fetched when the process authenticates with an organization credential; filesystem isolation does not remove them. See [Secure deployment](/docs/en/agent-sdk/secure-deployment).
</Warning>

## Project instructions (CLAUDE.md and rules)

`CLAUDE.md` files and `.claude/rules/*.md` files give your agent persistent context about your project: coding conventions, build commands, architecture decisions, and instructions. When `settingSources` includes `"project"`, as in the [`settingSources` example](#control-filesystem-settings-with-settingsources), the SDK loads these files into context at session start. The agent then follows your project conventions without you repeating them in every prompt.

### CLAUDE.md load locations

| Level                 | Location                                                                      | When loaded                                                                                         |
| :-------------------- | :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| Project (root)        | `<cwd>/CLAUDE.md` or `<cwd>/.claude/CLAUDE.md`                                | `settingSources` includes `"project"`                                                               |
| Project rules         | `<cwd>/.claude/rules/*.md` and `.claude/rules/*.md` in every parent directory | `settingSources` includes `"project"`                                                               |
| Project (parent dirs) | `CLAUDE.md` files in directories above `cwd`                                  | `settingSources` includes `"project"`, loaded at session start                                      |
| Project (child dirs)  | `CLAUDE.md` files in subdirectories of `cwd`                                  | `settingSources` includes `"project"`, loaded on demand when the agent reads a file in that subtree |
| Local                 | `<cwd>/CLAUDE.local.md` and `CLAUDE.local.md` in every parent directory       | `settingSources` includes `"local"`                                                                 |
| User                  | `~/.claude/CLAUDE.md`                                                         | `settingSources` includes `"user"`                                                                  |
| User rules            | `~/.claude/rules/*.md`                                                        | `settingSources` includes `"user"`                                                                  |

All levels are additive: if both project and user CLAUDE.md files exist, the agent sees both. There is no hard precedence rule between levels; if instructions conflict, the outcome depends on how Claude interprets them. Write non-conflicting rules, or state precedence explicitly in the more specific file ("These project instructions override any conflicting user-level defaults").

<Tip>
  You can also inject context directly via `systemPrompt` without using CLAUDE.md files. See [Modify system prompts](/docs/en/agent-sdk/modifying-system-prompts). Use CLAUDE.md when you want the same context shared between interactive Claude Code sessions and your SDK agents.
</Tip>

For how to structure and organize CLAUDE.md content, see [Manage Claude's memory](/docs/en/memory).

## Skills

Skills are markdown files that give your agent specialized knowledge and invocable workflows. Unlike `CLAUDE.md` (which loads every session), skills load on demand. The agent receives skill descriptions at startup and loads the full content when relevant.

Skills are discovered from the filesystem through `settingSources`. When the `skills` option on `query()` is omitted, discovered user and project skills are enabled and the Skill tool is available, matching CLI behavior. To control which skills are enabled, pass `skills` as `"all"`, a list of skill names, or `[]` to disable all. When `skills` is set, the SDK adds the Skill tool to `allowedTools` automatically. If you also pass an explicit `tools` list, include `"Skill"` in that list so Claude can invoke skills.

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
  import asyncio

  # Skills in .claude/skills/ are discovered automatically
  # when settingSources includes "project"
  async def main():
      async for message in query(
          prompt="Review this PR using our code review checklist",
          options=ClaudeAgentOptions(
              setting_sources=["user", "project"],
              skills="all",
              allowed_tools=["Read", "Grep", "Glob"],
          ),
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Skills in .claude/skills/ are discovered automatically
  // when settingSources includes "project"
  for await (const message of query({
    prompt: "Review this PR using our code review checklist",
    options: {
      settingSources: ["user", "project"],
      skills: "all",
      allowedTools: ["Read", "Grep", "Glob"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

<Note>
  Skills must be created as filesystem artifacts (`.claude/skills/<name>/SKILL.md`). The SDK does not have a programmatic API for registering skills. See [Agent Skills in the SDK](/docs/en/agent-sdk/skills) for full details.
</Note>

## Hooks

The SDK supports two ways to define hooks, and they run side by side:

* **Filesystem hooks:** shell commands defined in `settings.json`, loaded when `settingSources` includes the relevant source. These are the same hooks you'd configure for [interactive Claude Code sessions](/docs/en/hooks-guide).
* **Programmatic hooks:** callback functions passed directly to `query()`. These run in your application process and can return structured decisions. See [Control execution with hooks](/docs/en/agent-sdk/hooks).

Hook callbacks receive the tool input and return a decision dict. Returning `{}` means allow the tool to proceed. To block execution, return a `hookSpecificOutput` object with `permissionDecision: "deny"` and a `permissionDecisionReason`. The reason is sent to Claude as the tool result. See the [hooks guide](/docs/en/agent-sdk/hooks) for the full callback signature and return types.

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher, ResultMessage
  import asyncio

  # PreToolUse hook callback. Positional args:
  #   input_data: HookInput dict with tool_name, tool_input, hook_event_name
  #   tool_use_id: str | None, the ID of the tool call being intercepted
  #   context: HookContext, reserved for future abort-signal support
  async def audit_bash(input_data, tool_use_id, context):
      command = input_data.get("tool_input", {}).get("command", "")
      if "rm -rf" in command:
          return {
              "hookSpecificOutput": {
                  "hookEventName": "PreToolUse",
                  "permissionDecision": "deny",
                  "permissionDecisionReason": "Destructive command blocked",
              }
          }
      return {}  # Empty dict: allow the tool to proceed

  # Filesystem hooks from .claude/settings.json run automatically
  # when settingSources loads them. You can also add programmatic hooks:
  async def main():
      async for message in query(
          prompt="Refactor the auth module",
          options=ClaudeAgentOptions(
              setting_sources=["project"],  # Loads hooks from .claude/settings.json
              hooks={
                  "PreToolUse": [
                      HookMatcher(matcher="Bash", hooks=[audit_bash]),
                  ]
              },
          ),
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // PreToolUse hook callback. HookInput is a discriminated union on
  // hook_event_name, so narrowing on it gives TypeScript the right
  // tool_input shape for this event.
  const auditBash = async (input: HookInput): Promise<HookJSONOutput> => {
    if (input.hook_event_name !== "PreToolUse") return {};
    const toolInput = input.tool_input as { command?: string };
    if (toolInput.command?.includes("rm -rf")) {
      return {
        hookSpecificOutput: {
          hookEventName: "PreToolUse",
          permissionDecision: "deny",
          permissionDecisionReason: "Destructive command blocked",
        },
      };
    }
    return {}; // Empty object: allow the tool to proceed
  };

  // Filesystem hooks from .claude/settings.json run automatically
  // when settingSources loads them. You can also add programmatic hooks:
  for await (const message of query({
    prompt: "Refactor the auth module",
    options: {
      settingSources: ["project"], // Loads hooks from .claude/settings.json
      hooks: {
        PreToolUse: [{ matcher: "Bash", hooks: [auditBash] }]
      }
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

### When to use which hook type

| Hook type                                 | Best for                                                                                                                                                                                                                                                                                                     |
| :---------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Filesystem** (`settings.json`)          | Sharing hooks between CLI and SDK sessions. Supports `"command"` (shell scripts), `"http"` (POST to an endpoint), `"mcp_tool"` (call a connected MCP server's tool), `"prompt"` (LLM evaluates a prompt), and `"agent"` (spawns a verifier agent). These fire in the main agent and any subagents it spawns. |
| **Programmatic** (callbacks in `query()`) | Application-specific logic, structured decisions, and in-process integration. These also fire inside subagents. The hook input, the callback's first argument, carries `agent_id` and `agent_type` fields that identify which agent fired the hook.                                                          |

<Note>
  The TypeScript SDK supports additional hook events beyond Python, including `SessionStart`, `SessionEnd`, `TeammateIdle`, and `TaskCompleted`. See the [hooks guide](/docs/en/agent-sdk/hooks) for the full event compatibility table.
</Note>

For full details on programmatic hooks, see [Control execution with hooks](/docs/en/agent-sdk/hooks). For filesystem hook syntax, see [Hooks](/docs/en/hooks).

## Choose the right feature

The Agent SDK gives you access to several ways to extend your agent's behavior. If you're unsure which to use, this table maps common goals to the right approach.

| What you want to do                                                                               | Use                                           | SDK surface                                                                                                                                                    |
| :------------------------------------------------------------------------------------------------ | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set project conventions your agent always follows                                                 | [CLAUDE.md](/docs/en/memory)                       | `settingSources: ["project"]` loads it automatically                                                                                                           |
| Give the agent reference material it loads when relevant                                          | [Skills](/docs/en/agent-sdk/skills)                | `settingSources` + `skills` option                                                                                                                             |
| Run a reusable workflow (deploy, review, release)                                                 | [User-invocable skills](/docs/en/agent-sdk/skills) | `settingSources` + `skills` option                                                                                                                             |
| Delegate an isolated subtask to a fresh context (research, review)                                | [Subagents](/docs/en/agent-sdk/subagents)          | `agents` parameter + `allowedTools: ["Agent"]`                                                                                                                 |
| Coordinate multiple Claude Code instances with shared task lists and direct inter-agent messaging | [Agent teams](/docs/en/agent-teams)                | Not directly configured via SDK options. Agent teams are a CLI feature where one session acts as the team lead, coordinating work across independent teammates |
| Run deterministic logic on tool calls (audit, block, transform)                                   | [Hooks](/docs/en/agent-sdk/hooks)                  | `hooks` parameter with callbacks, or shell scripts loaded via `settingSources`                                                                                 |
| Give Claude structured tool access to an external service                                         | [MCP](/docs/en/agent-sdk/mcp)                      | `mcpServers` parameter                                                                                                                                         |

Every feature you enable adds to your agent's context window. For per-feature costs and how these features layer together, see [Extend Claude Code](/docs/en/features-overview#understand-context-costs).

## Related resources

* [Extend Claude Code](/docs/en/features-overview): Conceptual overview of all extension features, with comparison tables and context cost analysis
* [Skills in the SDK](/docs/en/agent-sdk/skills): Full guide to using skills programmatically
* [Subagents](/docs/en/agent-sdk/subagents): Define and invoke subagents for isolated subtasks
* [Hooks](/docs/en/agent-sdk/hooks): Intercept and control agent behavior at key execution points
* [Permissions](/docs/en/agent-sdk/permissions): Control tool access with modes, rules, and callbacks
* [System prompts](/docs/en/agent-sdk/modifying-system-prompts): Inject context without CLAUDE.md files

---

## Configure your agent

- 官方原文：https://code.claude.com/docs/en/agent-sdk/configuration.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-configuration.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure your agent

> Configure Agent SDK sessions: compose the options object, set the model, environment, and limits, and find each feature option's page.

An Agent SDK session reads configuration from settings files, environment variables, and the `options` object you pass when you start it. This page shows how to compose the `options` object and what settings files and environment variables control.

For every option's type and default, see the [`Options`](/docs/en/agent-sdk/typescript#options) (TypeScript) and [`ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions) (Python) references.

## Pass options to a session

Every `query()` call accepts an options object: `Options` in TypeScript, `ClaudeAgentOptions` in Python. Each field is optional, and a session started with no options runs with the SDK's defaults. The example below configures a read-only session that summarizes a project's open TODOs. Pairs read as TypeScript / Python where the spellings differ:

* **`model`**: picks the model
* **`allowedTools` / `allowed_tools`**: pre-approves a read-only tool list
* **`maxTurns` / `max_turns`**: caps the turn count
* **`cwd`**: sets the working directory

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Summarize the open TODOs in this repo",
    options: {
      model: "claude-sonnet-5",
      allowedTools: ["Read", "Glob", "Grep"],
      maxTurns: 8,
      cwd: "/path/to/repo",
    },
  })) {
    if (message.type === "result" && message.subtype === "success" && !message.is_error) {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

  async def main():
      options = ClaudeAgentOptions(
          model="claude-sonnet-5",
          allowed_tools=["Read", "Glob", "Grep"],
          max_turns=8,
          cwd="/path/to/repo",
      )

      async for message in query(
          prompt="Summarize the open TODOs in this repo",
          options=options,
      ):
          if isinstance(message, ResultMessage) and not message.is_error:
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

Point `cwd` at one of your own projects and run the example. The summary of that project's open TODOs prints when the result message arrives.

`allowedTools` (TypeScript) or `allowed_tools` (Python) pre-approves the listed tools, so calls to them run without stopping for approval. Tools outside the list stay available. When Claude calls an unlisted tool, the permission mode decides whether the call runs. For more information, see [Allow and deny rules](/docs/en/agent-sdk/permissions#allow-and-deny-rules).

## Load settings files

Settings files supply configuration beyond the options object. Two options control how they load:

* **`settingSources` / `setting_sources`**: controls which filesystem sources load: user, project, and local. Settings files and CLAUDE.md files arrive through these sources.
* **`settings`**: loads a settings file path or an inline JSON string in either language, and TypeScript also accepts a settings object. Whichever form you pass overrides user, project, and local filesystem settings; only managed policy settings rank higher. The references document the full precedence order under [Settings precedence](/docs/en/agent-sdk/typescript#settings-precedence) for TypeScript and [Settings precedence](/docs/en/agent-sdk/python#settings-precedence) for Python.

Pass `[]` to disable user, project, and local settings. For more information, see [Use Claude Code features in the SDK](/docs/en/agent-sdk/claude-code-features).

## Choose a model

Unless the `model` option, your settings, or your environment selects a model, a new session starts on [Claude Code's default model](/docs/en/model-config#default-model-setting). For the order of those sources, see [Setting your model](/docs/en/model-config#setting-your-model). Set `model` to pin a specific model, or to pick a smaller one for faster, cheaper agents. The value takes a model alias or a full model name; aliases and the versions they resolve to are listed under [Model aliases](/docs/en/model-config#model-aliases).

Set `fallbackModel` (TypeScript) or `fallback_model` (Python) to name a backup model. When the primary is overloaded or unavailable, the session switches to the backup. The primary is retried at the start of each user turn, so the session returns to it once the outage passes.

In either language, the option accepts a single model or a comma-separated list of backups. For the order and the chain cap, see [Fallback model chains](/docs/en/model-config#fallback-model-chains). In TypeScript, a fallback equal to `model` throws an error at startup.

The examples below show a fallback list in TypeScript and a single fallback in Python:

<CodeGroup>
  ```typescript TypeScript theme={null}
  const options = {
    model: "claude-fable-5",
    fallbackModel: "claude-opus-5,claude-sonnet-5",
  };
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      model="claude-fable-5",
      fallback_model="claude-opus-5",
  )
  ```
</CodeGroup>

<span id="sampling-parameters" />

<Note>
  The [Messages API](https://platform.claude.com/docs/en/api/messages) request parameters `temperature`, `top_p`, and `max_tokens` have no fields on the options object in either language. Set the [effort level](/docs/en/agent-sdk/agent-loop#effort-level) or a [spend cap](#limit-turns-and-spend) instead, or call the Messages API when you need those parameters directly.
</Note>

## Set environment variables

The `env` option sets environment variables for the Claude Code process that runs your session. Whether your values replace the inherited environment or merge over it differs by language:

* **TypeScript**: `env` replaces the subprocess environment
* **Python**: the SDK merges your values over the inherited environment, and your values override the inherited ones

In TypeScript, spread `process.env` into `env` to keep inherited variables such as `PATH`, `HOME`, and `ANTHROPIC_API_KEY`. When you leave `env` unset, the subprocess inherits your environment in both languages.

The example routes API traffic through a gateway by setting `ANTHROPIC_BASE_URL`.

<CodeGroup>
  ```typescript TypeScript theme={null}
  const options = {
    env: { ...process.env, ANTHROPIC_BASE_URL: "https://gateway.example.com" },
  };
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      env={"ANTHROPIC_BASE_URL": "https://gateway.example.com"},
  )
  ```
</CodeGroup>

The variables you pass can also configure Claude Code itself. For the variables the Claude Code process reads, see [Environment variables](/docs/en/env-vars). To tune API timeouts and stall detection this way, follow the Handle slow or stalled API responses section in the [TypeScript reference](/docs/en/agent-sdk/typescript#handle-slow-or-stalled-api-responses) or the [Python reference](/docs/en/agent-sdk/python#handle-slow-or-stalled-api-responses).

## Set the working directory

Set `cwd` to run the session in a specific directory. When you leave `cwd` unset, the session runs in your process's working directory. Neither SDK has a setter for `cwd`. To run in a different directory, start another session with that `cwd`.

Claude Code reads the working directory to determine:

* **Project settings and hooks**: which project's [settings and hooks load](/docs/en/agent-sdk/claude-code-features)
* **Skills**: where [session skills are discovered](/docs/en/agent-sdk/skills)
* **Session storage**: which project a [stored session belongs to](/docs/en/agent-sdk/session-storage)

To let tools reach files outside the working directory, add paths with `additionalDirectories` (TypeScript) or `add_dirs` (Python). For the scope of that grant, see [Additional directories grant file access, not configuration](/docs/en/permissions#additional-directories-grant-file-access-not-configuration).

## Limit turns and spend

Cap turns and spend with `maxTurns` / `max_turns` and `maxBudgetUsd` / `max_budget_usd`. Both caps are off when unset. When a session hits a cap, the run ends with a result message whose subtype names the cap, `error_max_turns` or `error_max_budget_usd`. What happens next differs by input mode:

* **Single-shot `query()`**: the SDK yields the cap result and then raises, so wrap the loop in a try block to continue past the error
* **Streaming input**: the session stays alive past a cap result, and the max-turns count starts over for each queued message. The budget total accumulates across messages, and once spend reaches the cap, later messages in the same conversation end with the same budget result. A [`/clear`](/docs/en/agent-sdk/cost-tracking) starts the budget over

The two caps treat `0` differently:

* **`maxTurns` / `max_turns`**: `0` runs the session without a turn limit, the same as leaving the option unset
* **`maxBudgetUsd` / `max_budget_usd`**: the CLI rejects `0` as an invalid amount at startup, and the session never runs

For more information about both caps, including subagent spend, see [Turns and budget](/docs/en/agent-sdk/agent-loop#turns-and-budget).

## Change configuration mid-session

When you start a session with [streaming input](/docs/en/agent-sdk/streaming-vs-single-mode), you can switch its model and permission mode while it runs. Where you call the setters differs by language:

* **TypeScript**: methods on the object `query()` returns
* **Python**: methods on [`ClaudeSDKClient`](/docs/en/agent-sdk/python#claudesdkclient), since `query()` returns a plain iterator without control methods

Both languages have the same setters:

* **`setModel()` / `set_model()`**: switches the model. Call it with no model to switch to [Claude Code's default model](/docs/en/model-config#default-model-setting) rather than the `model` you passed in options.
* **`setPermissionMode()` / `set_permission_mode()`**: switches the permission mode

TypeScript also has `applyFlagSettings()` and `updateSettings()`:

* **`applyFlagSettings()`**: applies settings at runtime, as in `await session.applyFlagSettings({ effortLevel: "high" })`. The method takes settings file keys rather than options fields, so check the [`applyFlagSettings()` reference](/docs/en/agent-sdk/typescript#applyflagsettings) for the schema and for which keys take effect mid-session.
* **`updateSettings()`**: writes one allowlisted key to a settings file. The [`updateSettings()` reference](/docs/en/agent-sdk/typescript#updatesettings) names the key each source accepts and the version floors.
  * Pass `"localSettings"` to write the project's local settings file, as in `await session.updateSettings("localSettings", { outputStyle: "Explanatory" })`. The written key takes effect on the session's next request and persists for later sessions that load `local` settings.
  * Pass `"userSettings"` to write `effortLevel`, the only key that source accepts. Claude Code saves it as the default effort level for the session's current model, and the running session's effort doesn't change.

The example below runs a two-turn session, changes the configuration between the turns, and prints the model that answered each turn. In TypeScript, the prompt stream holds the second message until the setters have run, and the second turn runs on the new model.

<CodeGroup>
  ```typescript TypeScript theme={null}

  function userMessage(text: string): SDKUserMessage {
    return { type: "user", message: { role: "user", content: text }, parent_tool_use_id: null };
  }

  // Hold the second prompt until the setters have run.
  let startSecondTurn!: () => void;
  const secondTurnReady = new Promise<void>((resolve) => {
    startSecondTurn = resolve;
  });

  async function* turnPrompts(): AsyncGenerator<SDKUserMessage, void> {
    yield userMessage("Reply with exactly: ready");
    await secondTurnReady;
    yield userMessage("Reply with exactly: done");
  }

  const session = query({
    prompt: turnPrompts(),
    options: {
      model: "claude-sonnet-5",
    },
  });

  let turnModel = "";
  let completedTurns = 0;

  for await (const message of session) {
    if (message.type === "assistant") {
      turnModel = message.message.model;
    } else if (message.type === "result") {
      completedTurns += 1;
      if (completedTurns === 1) {
        console.log(`First turn model: ${turnModel}`);
        await session.setModel("claude-opus-5");
        await session.setPermissionMode("acceptEdits");
        startSecondTurn();
      } else {
        console.log(`Second turn model: ${turnModel}`);
        break;
      }
    }
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, ClaudeSDKClient

  async def main():
      options = ClaudeAgentOptions(model="claude-sonnet-5")

      async with ClaudeSDKClient(options=options) as client:
          await client.query("Reply with exactly: ready")
          first_model = ""
          async for message in client.receive_response():
              if isinstance(message, AssistantMessage):
                  first_model = message.model

          await client.set_model("claude-opus-5")
          await client.set_permission_mode("acceptEdits")

          await client.query("Reply with exactly: done")
          second_model = ""
          async for message in client.receive_response():
              if isinstance(message, AssistantMessage):
                  second_model = message.model

      print(f"First turn model: {first_model}")
      print(f"Second turn model: {second_model}")

  asyncio.run(main())
  ```
</CodeGroup>

On the Claude API, the program prints `First turn model: claude-sonnet-5`, then `Second turn model: claude-opus-5` after the switch.

<Note>
  Each model has its own prompt cache, so after a mid-session switch the next request recomputes the full conversation uncached at the new model's rates. For more information, see [Switching models](/docs/en/prompt-caching#switching-models).
</Note>

## Configure specific features

The table below maps each option to the feature it configures. For options this page doesn't cover, see the [TypeScript](/docs/en/agent-sdk/typescript#options) and [Python](/docs/en/agent-sdk/python#claudeagentoptions) references. If you know your goal but not which option serves it, start from [Choose the right feature](/docs/en/agent-sdk/claude-code-features#choose-the-right-feature).

| TypeScript                | Python                      | Controls                                 | Covered in                                                                                                                                                                                                        |
| ------------------------- | --------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `permissionMode`          | `permission_mode`           | What the agent can do without approval   | [Configure permissions](/docs/en/agent-sdk/permissions)                                                                                                                                                                |
| `allowedTools`            | `allowed_tools`             | Which tool calls are pre-approved        | [Configure permissions](/docs/en/agent-sdk/permissions)                                                                                                                                                                |
| `canUseTool`              | `can_use_tool`              | Your approval callback for tool calls    | [Handle tool approval requests](/docs/en/agent-sdk/user-input#handle-tool-approval-requests)                                                                                                                           |
| `systemPrompt`            | `system_prompt`             | The agent's instructions                 | [Modifying system prompts](/docs/en/agent-sdk/modifying-system-prompts)                                                                                                                                                |
| `settingSources`          | `setting_sources`           | Which filesystem settings load           | [Use Claude Code features in the SDK](/docs/en/agent-sdk/claude-code-features)                                                                                                                                         |
| `mcpServers`              | `mcp_servers`               | External tool servers                    | [Connect to external tools with MCP](/docs/en/agent-sdk/mcp)                                                                                                                                                           |
| `agents`                  | `agents`                    | Subagent definitions                     | [Subagents](/docs/en/agent-sdk/subagents)                                                                                                                                                                              |
| `hooks`                   | `hooks`                     | Callbacks at lifecycle points            | [Hooks](/docs/en/agent-sdk/hooks)                                                                                                                                                                                      |
| `skills`                  | `skills`                    | Which skills load                        | [Extend agents with skills](/docs/en/agent-sdk/skills)                                                                                                                                                                 |
| `plugins`                 | `plugins`                   | Which plugins load                       | [Plugins](/docs/en/agent-sdk/plugins)                                                                                                                                                                                  |
| `outputFormat`            | `output_format`             | Structured output schemas                | [Structured outputs](/docs/en/agent-sdk/structured-outputs)                                                                                                                                                            |
| `resume`                  | `resume`                    | Continuing a stored session              | [Sessions](/docs/en/agent-sdk/sessions)                                                                                                                                                                                |
| `forkSession`             | `fork_session`              | Branching a session                      | [Sessions](/docs/en/agent-sdk/sessions)                                                                                                                                                                                |
| `sessionStore`            | `session_store`             | External session persistence             | [Session storage](/docs/en/agent-sdk/session-storage)                                                                                                                                                                  |
| `enableFileCheckpointing` | `enable_file_checkpointing` | Rewindable file edits                    | [File checkpointing](/docs/en/agent-sdk/file-checkpointing)                                                                                                                                                            |
| `effort`                  | `effort`                    | How much work Claude puts into responses | [Effort level](/docs/en/agent-sdk/agent-loop#effort-level)                                                                                                                                                             |
| `sandbox`                 | `sandbox`                   | Sandbox behavior for tool execution      | [TypeScript](/docs/en/agent-sdk/typescript#sandbox-configuration) and [Python](/docs/en/agent-sdk/python#sandbox-configuration) references, with deployment context in [Secure deployment](/docs/en/agent-sdk/secure-deployment) |

## Next steps

To see configuration composed into working agents:

* **[Quickstart](/docs/en/agent-sdk/quickstart)**: build and run a first agent end to end
* **[Examples](/docs/en/agent-sdk/examples)**: find a complete, runnable project or a guided Claude Cookbook recipe that matches what you want to build
* **[Multi-tenant isolation](/docs/en/agent-sdk/hosting#multi-tenant-isolation)**: isolate each tenant's settings and memory with `settingSources` / `setting_sources`, `env`, and `cwd`

---

## Track cost and usage

- 官方原文：https://code.claude.com/docs/en/agent-sdk/cost-tracking.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-cost-tracking.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Track cost and usage

> Learn how to track token usage, estimate costs, and configure prompt caching with the Claude Agent SDK.

The Claude Agent SDK provides detailed token usage information for each interaction with Claude. This guide explains how to properly track usage and understand cost reporting, especially when dealing with parallel tool uses and multi-step conversations.

For complete API documentation, see the [TypeScript SDK reference](/docs/en/agent-sdk/typescript) and [Python SDK reference](/docs/en/agent-sdk/python).

<Warning>
  The `total_cost_usd` and `costUSD` fields are client-side estimates, not authoritative billing data. The SDK computes them locally from a price table bundled at build time, unless a [`modelPricing`](/docs/en/settings-reference#modelpricing) table is in effect. They can drift from what you are actually billed when:

  * pricing changes
  * the installed SDK version does not recognize a model
  * billing rules apply that the client cannot model

  One billing rule the SDK does model is [data residency pricing](https://platform.claude.com/docs/en/about-claude/pricing#data-residency-pricing). When a response's `usage` reports `inference_geo: "us"`, the SDK multiplies the list price of that response's tokens by 1.1. Per-request fees such as web search aren't multiplied. Requires TypeScript Agent SDK v0.3.239 or later, or Python Agent SDK v0.2.144 or later.

  Use these fields for development insight and approximate budgeting. For authoritative billing, use the [Usage and Cost API](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api) or the Usage page in the [Claude Console](https://platform.claude.com/usage). Do not bill end users or trigger financial decisions from these fields.
</Warning>

## Understand token usage

The TypeScript and Python SDKs expose the same usage data with different field names:

* **TypeScript** provides per-step token breakdowns on each assistant message (`message.message.id`, `message.message.usage`), per-model cost via `modelUsage` on the result message, and a cumulative total on the result message.
* **Python** provides per-step token breakdowns on each assistant message as `message.usage` and `message.message_id`, per-model cost via `model_usage` on the result message, and the cumulative total on the result message as `total_cost_usd`.

Both SDKs use the same underlying cost model and expose the same granularity. The difference is in field naming and where per-step usage is nested.

Cost tracking depends on understanding how the SDK scopes usage data:

* **`query()` call:** one invocation of the SDK's `query()` function. A single call can involve multiple steps: Claude responds, uses tools, gets results, and responds again. Each call produces one [`result`](/docs/en/agent-sdk/typescript#sdkresultmessage) message at the end, except in [streaming input mode](/docs/en/agent-sdk/streaming-vs-single-mode), where one `query()` call carries multiple user turns and each turn emits its own `result` message.
* **Step:** a single request/response cycle within a `query()` call. Each step produces assistant messages with token usage.
* **Session:** a series of `query()` calls linked by a session ID through the `resume` option. A resumed call's results report the session's whole spend, not just that call's own. See [Accumulate costs across multiple calls](#accumulate-costs-across-multiple-calls) for how the totals carry over.

The following diagram shows the message stream from a single `query()` call, with token usage reported at each step and the cumulative estimate at the end:

<img src="https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agent-sdk/message-usage-flow.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=68497aee338e01cc745323af7aea378e" className="dark:hidden" alt="Diagram showing a query producing two steps of messages. Step 1 has four assistant messages sharing the same ID and usage (count once), Step 2 has one assistant message with a new ID, and the final result message shows the estimated total_cost_usd." width="760" height="520" data-path="images/agent-sdk/message-usage-flow.svg" />

<img src="https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agent-sdk/message-usage-flow-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=8ea95085abc0a6b7f55ecef498bd4d14" className="hidden dark:block" alt="Diagram showing a query producing two steps of messages. Step 1 has four assistant messages sharing the same ID and usage (count once), Step 2 has one assistant message with a new ID, and the final result message shows the estimated total_cost_usd." width="760" height="520" data-path="images/agent-sdk/message-usage-flow-dark.svg" />

    When Claude responds, it sends one or more assistant messages. In TypeScript, each assistant message contains a nested `BetaMessage` (accessed via `message.message`) with an `id` and a [`usage`](https://platform.claude.com/docs/en/api/messages) object with token counts (`input_tokens`, `output_tokens`). In Python, the `AssistantMessage` dataclass exposes the same data directly via `message.usage` and `message.message_id`. When Claude uses multiple tools in one turn, all messages in that turn share the same ID, so deduplicate by ID to avoid double-counting.

    When the `query()` call completes, the SDK emits a result message with `total_cost_usd` and cumulative `usage`, typed as [`SDKResultMessage`](/docs/en/agent-sdk/typescript#sdkresultmessage) in TypeScript and [`ResultMessage`](/docs/en/agent-sdk/python#resultmessage) in Python. If you only need the estimated total, you can ignore the per-step usage and read this single value.

    If you make multiple independent `query()` calls, each result reflects only the cost of that individual call. A call that resumes a session also counts the session's earlier spend.

    In streaming input mode, each turn emits its own result message. See [Track costs in streaming input mode](#track-costs-in-streaming-input-mode) for how to read call totals in that mode.

## Track costs in streaming input mode

In [streaming input mode](/docs/en/agent-sdk/streaming-vs-single-mode), one `query()` call carries multiple user turns and each turn emits its own result message. The result fields differ in scope:

* **`usage`**: covers only that turn, and within it only the main agent loop, not any subagents it ran.
* **`total_cost_usd` and `modelUsage`, or `model_usage` in Python**: carry the running total for the whole call so far, plus any spend restored when the call resumed a session.

In a call where your app never sends `/clear`, `/reset`, or `/new`, read the latest result for call totals rather than summing across results.

The running totals start over each time your app sends one of those three commands, and inside a `query()` call nothing else resets them. Three results matter for your accounting:

* **The `/clear` turn's own result**: covers only what has run since the reset, and carries a new `session_id`.
* **Every later result**: keeps counting from that reset.
* **The last result before each `/clear`**: holds the total for the turns since the previous reset.

To total the whole call, add the last result from before each `/clear` to the call's final result. Every other result, including the `/clear` turn's own, is superseded by a later one.

In TypeScript, the SDK also emits an [`SDKConversationResetMessage`](/docs/en/agent-sdk/typescript#sdkconversationresetmessage) at each reset, so you can detect resets from the stream. In Python, the SDK likewise emits a `ConversationResetMessage`. Before Python SDK v0.2.137, the Python iterator dropped that message, so on those versions count the resets yourself from the `/clear` turns your app sends.

`maxBudgetUsd` (TypeScript) or `max_budget_usd` (Python) counts only the call's own spend: totals restored from a resumed session don't count against it, and a `/clear` starts the budget over.

## Get the total cost of a query

The result message, typed as [`SDKResultMessage`](/docs/en/agent-sdk/typescript#sdkresultmessage) in TypeScript and [`ResultMessage`](/docs/en/agent-sdk/python#resultmessage) in Python, marks the end of the agent loop for a `query()` call. It includes `total_cost_usd`, the cumulative estimated cost across all steps in that call. A call that resumes a session also counts the session's earlier spend. Two caveats apply when you read the value:

* In Python the field is typed as optional, so check that it isn't `None` before you read it.
* Success and error results both carry it, though the final result of a [session crash](#recover-totals-after-a-session-crash) may carry it zeroed.

In streaming input mode, read call totals as described in [Track costs in streaming input mode](#track-costs-in-streaming-input-mode).

The three result-level fields differ in what they count when the agent spawns [subagents](/docs/en/agent-sdk/subagents). Use `modelUsage`, or `model_usage` in Python, for whole-tree token accounting; the `usage` field undercounts as soon as nesting occurs.

| Field                        | Subagent activity                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------- |
| `usage`                      | Excluded. Counts only the top-level agent loop, so tokens consumed inside subagents are not added |
| `total_cost_usd`             | Included. Counts subagent requests alongside the top-level loop                                   |
| `modelUsage` / `model_usage` | Included. Counts subagent requests alongside the top-level loop, broken down by model             |

In [single message input mode](/docs/en/agent-sdk/streaming-vs-single-mode#single-message-input), when background subagents are still running at the end of the final turn, Claude Code waits for them, up to the cap described in [background tasks at exit](/docs/en/headless#background-tasks-at-exit), before emitting the result. The result's `total_cost_usd`, `duration_api_ms`, and `modelUsage`, or `model_usage` in Python, include the work done during that wait.

The following examples iterate over the message stream from a `query()` call and print the total cost when the `result` message arrives:

<CodeGroup>
  ```typescript TypeScript theme={null}

  try {
    for await (const message of query({ prompt: "Summarize this project" })) {
      if (message.type === "result") {
        console.log(`Total cost: $${message.total_cost_usd}`);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, it still carried total_cost_usd and the
    // branch above has already run; connection or process failures yield
    // no result message.
    console.error(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ResultMessage
  import asyncio

  async def main():
      try:
          async for message in query(prompt="Summarize this project"):
              if isinstance(message, ResultMessage):
                  print(f"Total cost: ${message.total_cost_usd or 0}")
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, the branch above has already run;
          # connection or process failures yield no result message.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

To bound how much subagents can add to `total_cost_usd`, set the [depth, concurrency, and spend limits](/docs/en/agent-sdk/subagents#cap-subagent-depth-concurrency-and-spend) on the query.

## Track per-step and per-model usage

The examples in this section use TypeScript field names. In Python, the equivalent fields are [`AssistantMessage.usage`](/docs/en/agent-sdk/python#assistantmessage) and `AssistantMessage.message_id` for per-step usage, and [`ResultMessage.model_usage`](/docs/en/agent-sdk/python#resultmessage) for per-model breakdowns.

### Track per-step usage

Each assistant message contains a nested `BetaMessage` (accessed via `message.message`) with an `id` and `usage` object with token counts. When Claude uses tools in parallel, multiple messages share the same `id` with identical usage data. Track which IDs you've already counted and skip duplicates to avoid inflated totals.

<Warning>
  The deduplicated per-step values are accurate for input and cache tokens. Per-step `output_tokens` is a placeholder, so [read output tokens from the result message](#read-output-tokens-from-the-result-message).
</Warning>

The following example accumulates input tokens across all steps, counting each unique main-loop message ID only once and skipping subagent messages, and reads the output total from the result message, which covers the main loop:

```typescript theme={null}

const seenIds = new Set<string>();
let totalInputTokens = 0;
let resultOutputTokens = 0;

try {
  for await (const message of query({ prompt: "Summarize this project" })) {
    if (message.type === "assistant" && !message.parent_tool_use_id) {
      const msgId = message.message.id;

      // Parallel tool calls share the same ID, only count once
      if (!seenIds.has(msgId)) {
        seenIds.add(msgId);
        totalInputTokens += message.message.usage.input_tokens;
      }
    }
    if (message.type === "result") {
      // Per-step output_tokens is a placeholder; the result message
      // carries the accumulated output total.
      resultOutputTokens = message.usage.output_tokens;
    }
  }
} catch (error) {
  // A single-shot query() throws after yielding an error result, so the
  // input total below still reflects the steps that ran before the failure.
  console.error(`Session ended with an error: ${error}`);
}

console.log(`Steps: ${seenIds.size}`);
console.log(`Input tokens: ${totalInputTokens}`);
console.log(`Output tokens: ${resultOutputTokens}`);
```

### Break down usage per model

The result message includes [`modelUsage`](/docs/en/agent-sdk/typescript#modelusage), a map of model name to per-model token counts and cost. This is useful when you run multiple models (for example, Haiku for subagents and Opus for the main agent) and want to see where tokens are going.

Each entry's `costBasis` says which price table priced that model's latest request: `list` for list price, `managed` for a [`modelPricing`](/docs/en/settings-reference#modelpricing) table, or `unknown` when neither matched the model ID. The field requires Claude Code v2.1.246 or later.

The following example runs a query and prints the cost and token breakdown for each model used:

```typescript theme={null}

try {
  for await (const message of query({ prompt: "Summarize this project" })) {
    if (message.type !== "result") continue;

    for (const [modelName, usage] of Object.entries(message.modelUsage)) {
      console.log(`${modelName}: $${usage.costUSD.toFixed(4)}`);
      console.log(`  Input tokens: ${usage.inputTokens}`);
      console.log(`  Output tokens: ${usage.outputTokens}`);
      console.log(`  Cache read: ${usage.cacheReadInputTokens}`);
      console.log(`  Cache creation: ${usage.cacheCreationInputTokens}`);
    }
  }
} catch (error) {
  // A single-shot query() throws after yielding an error result. If the
  // failure was an error result, the per-model breakdown above has already
  // printed; connection or process failures yield no result message.
  console.error(`Session ended with an error: ${error}`);
}
```

## Accumulate costs across multiple calls

Each `query()` call returns `total_cost_usd` on its results. How you combine the values depends on whether the calls share a session:

* **Independent calls, with no `resume` or `continue` option**: each result covers only its own call, so add the totals yourself, as the examples below do.
* **Calls that resume the same session**: Claude Code saves the session's totals to its [transcript](/docs/en/sessions#where-transcripts-are-stored) when the process exits normally and restores them when a later call resumes or forks the session. Each result already includes the session's earlier spend. Read the latest result for the session total; summing results double-counts the restored spend. Before v2.1.277, a session that you resumed through the SDK or `claude -p` started its totals at zero, so each call's results covered only that call.

In streaming input mode, read each call's total as described in [Track costs in streaming input mode](#track-costs-in-streaming-input-mode). For a call that ended in a crash, see [Recover totals after a session crash](#recover-totals-after-a-session-crash).

The following examples run two `query()` calls sequentially, add each call's `total_cost_usd` to a running total, and print both the per-call and combined cost:

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Track cumulative cost across multiple query() calls
  let totalSpend = 0;

  const prompts = [
    "Read the files in src/ and summarize the architecture",
    "List all exported functions in src/auth.ts"
  ];

  for (const prompt of prompts) {
    try {
      for await (const message of query({ prompt })) {
        if (message.type === "result") {
          totalSpend += message.total_cost_usd;
          console.log(`This call: $${message.total_cost_usd}`);
        }
      }
    } catch (error) {
      // A single-shot query() throws after yielding an error result. If the
      // failure was an error result, this call's cost was already counted;
      // connection or process failures yield no result message. Continue
      // with the next prompt.
      console.error(`Call failed: ${error}`);
    }
  }

  console.log(`Total spend: $${totalSpend.toFixed(4)}`);
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ResultMessage
  import asyncio

  async def main():
      # Track cumulative cost across multiple query() calls
      total_spend = 0.0

      prompts = [
          "Read the files in src/ and summarize the architecture",
          "List all exported functions in src/auth.ts",
      ]

      for prompt in prompts:
          try:
              async for message in query(prompt=prompt):
                  if isinstance(message, ResultMessage):
                      cost = message.total_cost_usd or 0
                      total_spend += cost
                      print(f"This call: ${cost}")
          except Exception as error:
              # A single-shot query() raises after yielding an error result. If
              # the failure was an error result, this call's cost was already
              # counted; connection or process failures yield no result message.
              # Continue with the next prompt.
              print(f"Call failed: {error}")

      print(f"Total spend: ${total_spend:.4f}")

  asyncio.run(main())
  ```
</CodeGroup>

## Handle errors, caching, and output token counts

For accurate cost tracking, account for the placeholder output count on assistant messages, the tokens a failed conversation consumed, and cache token pricing.

### Read output tokens from the result message

Claude Code builds each assistant message from the usage the API reported when the response began, so the message's `output_tokens` is only the count the API had reported at `message_start`, before the response was generated. One API response can produce several assistant messages, and every one of them carries that same placeholder.

The API reports the real output count at the end of the response, and Claude Code adds it to the result message. Read output tokens from the result's `usage`, or from `modelUsage` for a per-model breakdown.

To watch a response's output count grow while it streams, set `includePartialMessages`, or `include_partial_messages` in Python, and read `usage` from each `message_delta` stream event, typed as [`SDKPartialAssistantMessage`](/docs/en/agent-sdk/typescript#sdkpartialassistantmessage) in TypeScript and [`StreamEvent`](/docs/en/agent-sdk/python#streamevent) in Python.

### Track costs on failed conversations

Both success and error result messages include `usage` and `total_cost_usd`; in Python both fields are typed as optional, so check that they aren't `None` before you read them.

If a conversation fails midway, you still consumed tokens up to the point of failure. Read cost data from every result message, whether its `subtype` is `success` or one of the error subtypes. On some error results, `usage` reports less than the call spent:

* **`error_during_execution` after a [session crash](#recover-totals-after-a-session-crash)**: every cost field may be zeroed.
* **`error_max_budget_usd`**: `usage` leaves out the response that crossed the budget, while `total_cost_usd` and `modelUsage` include it.

Where you have the choice, account from `total_cost_usd` or `modelUsage` rather than `usage`.

### Recover totals after a session crash

When the Claude Code process crashes, it emits a final `error_during_execution` result and exits, in single-shot and streaming input mode alike. That result may carry zeroed `usage`, `total_cost_usd`, and `modelUsage`, so recover the call's totals from what arrived before it. Step 1 recovers the full totals whenever an earlier result exists; the fallback in step 2 recovers only the main loop's input and cache tokens.

1. Use the result of the turn before the crash. In streaming input mode, it holds the running total described in [Track costs in streaming input mode](#track-costs-in-streaming-input-mode). Go to step 2 instead when that result can't help you:
   * The call was single-shot, so no earlier result exists.
   * The crash happened on the first turn.
   * The turn before the crash was the `/clear` itself, so its result covers only the reset.
2. Sum the `usage` on the assistant messages instead, counting each API response once, as the [Track per-step usage](#track-per-step-usage) example does. In single-shot mode, sum all of them; in streaming input mode, sum the ones that arrived after the last result. This gives you the main loop's input and cache tokens. Subagent usage isn't recoverable this way, and neither are output tokens or USD cost, because [per-step `output_tokens` is a placeholder](#read-output-tokens-from-the-result-message).

### Track cache tokens

The Agent SDK automatically uses [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) to reduce costs on repeated content. You do not need to configure caching yourself. The usage object includes two additional fields for cache tracking:

* `cache_creation_input_tokens`: tokens used to create new cache entries (charged at a higher rate than standard input tokens).
* `cache_read_input_tokens`: tokens read from existing cache entries (charged at a reduced rate).

Track these separately from `input_tokens` to understand caching savings. In TypeScript, these fields are typed on the [`Usage`](/docs/en/agent-sdk/typescript#usage) object. In Python, they appear as keys in the [`ResultMessage.usage`](/docs/en/agent-sdk/python#resultmessage) dict (for example, `message.usage.get("cache_read_input_tokens", 0)`).

### Extend the prompt cache TTL to one hour

Your own turns fall in the [main conversation TTL bucket](/docs/en/prompt-caching#which-ttl-each-request-gets), together with the helpers Claude Code runs inline with them. The requests Claude Code makes outside that conversation, such as [subagents](/docs/en/agent-sdk/subagents), have a [separate TTL control](/docs/en/prompt-caching#choose-the-ttl-yourself).

Cache entries for your own turns use a 5-minute TTL by default when you authenticate with an API key or run on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or [Claude Platform on AWS](/docs/en/claude-platform-on-aws). If your workload runs many short sessions against the same system prompt and context with gaps longer than 5 minutes between them, the cache expires between sessions and each new session pays full input price.

To request a 1-hour TTL on cache writes, set the [`ENABLE_PROMPT_CACHING_1H`](/docs/en/env-vars) environment variable. You can export it in your shell or container environment, or pass it through `options.env`.

The following example enables 1-hour TTL for an agent running on Amazon Bedrock. Because it sets `CLAUDE_CODE_USE_BEDROCK`, it requires working AWS credentials for [Amazon Bedrock](/docs/en/amazon-bedrock); without them the query fails.

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import ClaudeAgentOptions, query
  import asyncio

  async def main():
      options = ClaudeAgentOptions(
          env={
              "CLAUDE_CODE_USE_BEDROCK": "1",
              "ENABLE_PROMPT_CACHING_1H": "1",
          },
      )

      async for message in query(prompt="Summarize this project", options=options):
          print(message)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  const options = {
    env: {
      ...process.env,
      CLAUDE_CODE_USE_BEDROCK: "1",
      ENABLE_PROMPT_CACHING_1H: "1",
    },
  };

  for await (const message of query({ prompt: "Summarize this project", options })) {
    console.log(message);
  }
  ```
</CodeGroup>

Cache writes with a 1-hour TTL are billed at a higher rate than 5-minute writes, so enabling this trades higher write cost for more cache reads. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details. On a Claude subscription within your plan's included usage, you get the 1-hour TTL on your own turns, and on some of the helper requests Claude Code makes beside them, without setting this variable, and Claude Code drops those turns to the 5-minute TTL once you're drawing on [usage credits](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans).

`ENABLE_PROMPT_CACHING_1H` asks for the 1-hour TTL on every request in both buckets. To choose a TTL for each bucket separately, use these controls instead. Each takes `5m` or `1h` and takes precedence over `ENABLE_PROMPT_CACHING_1H`:

* Main conversation: the `CLAUDE_CODE_PROMPT_CACHE_TTL` [environment variable](/docs/en/env-vars), or the [`promptCacheTtl`](/docs/en/settings-reference#promptcachettl) setting
* Everything else: the `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` environment variable, or the [`subagentPromptCacheTtl`](/docs/en/settings-reference#subagentpromptcachettl) setting

Setting `promptCacheTtl` to `1h` keeps the 1-hour cache on the main conversation while you're drawing on usage credits. For the full precedence order, see [choose the TTL yourself](/docs/en/prompt-caching#choose-the-ttl-yourself).

## Related documentation

* [TypeScript SDK Reference](/docs/en/agent-sdk/typescript) - Complete API documentation
* [SDK Overview](/docs/en/agent-sdk/overview) - Getting started with the SDK
* [SDK Permissions](/docs/en/agent-sdk/permissions) - Managing tool permissions

---

## Give Claude custom tools

- 官方原文：https://code.claude.com/docs/en/agent-sdk/custom-tools.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-custom-tools.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Give Claude custom tools

> Define custom tools with the Claude Agent SDK's in-process MCP server so Claude can call your functions, hit your APIs, and perform domain-specific operations.

Custom tools extend the Agent SDK by letting you define your own functions that Claude can call during a conversation. Using the SDK's in-process MCP server, you can give Claude access to databases, external APIs, domain-specific logic, or any other capability your application needs.

## Quick reference

| What you want to do                          | Do this                                                                                                                                                                                                       |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Define a tool                                | Use [`@tool`](/docs/en/agent-sdk/python#tool) (Python) or [`tool()`](/docs/en/agent-sdk/typescript#tool) (TypeScript) with a name, description, schema, and handler. See [Create a custom tool](#create-a-custom-tool). |
| Register a tool with Claude                  | Wrap in `create_sdk_mcp_server` / `createSdkMcpServer` and pass to `mcpServers` in `query()`. See [Call a custom tool](#call-a-custom-tool).                                                                  |
| Pre-approve a tool                           | Add to your allowed tools. See [Configure allowed tools](#configure-allowed-tools).                                                                                                                           |
| Remove a built-in tool from Claude's context | Pass a `tools` array listing only the built-ins you want. See [Configure allowed tools](#configure-allowed-tools).                                                                                            |
| Let Claude call tools in parallel            | Set `readOnlyHint: true` on tools with no side effects. See [Add tool annotations](#add-tool-annotations).                                                                                                    |
| Control the error message Claude reads       | Return `isError: true` to compose the message instead of surfacing the raw exception. See [Handle errors](#handle-errors).                                                                                    |
| Return images or files                       | Use `image` or `resource` blocks in the content array. See [Return images and resources](#return-images-and-resources).                                                                                       |
| Return a machine-readable JSON result        | Set `structuredContent` on the result. See [Return structured data](#return-structured-data).                                                                                                                 |
| Scale to many tools                          | Use [tool search](/docs/en/agent-sdk/tool-search) to load tools on demand.                                                                                                                                         |

## Create a custom tool

A tool is defined by four parts, passed as arguments to the [`tool()`](/docs/en/agent-sdk/typescript#tool) helper in TypeScript or the [`@tool`](/docs/en/agent-sdk/python#tool) decorator in Python:

* **Name:** a unique identifier Claude uses to call the tool.
* **Description:** what the tool does. Claude reads this to decide when to call it.
* **Input schema:** the arguments Claude must provide. In TypeScript this is always a [Zod schema](https://zod.dev/), and the handler's `args` are typed from it automatically. In Python this is a dict mapping names to types, like `{"latitude": float}`, which the SDK converts to JSON Schema for you. The Python decorator also accepts a full [JSON Schema](https://json-schema.org/understanding-json-schema/about) dict directly when you need enums, ranges, optional fields, or nested objects.
* **Handler:** the async function that runs when Claude calls the tool. It receives the validated arguments and must return an object with:
  * `content` (required): an array of result blocks, each with a `type` of `"text"`, `"image"`, `"audio"`, `"resource"`, or `"resource_link"`. See [Return images and resources](#return-images-and-resources) for non-text blocks.
  * `structuredContent` (optional): a JSON object holding the result as machine-readable data, returned alongside `content`. See [Return structured data](#return-structured-data).
  * `isError` (optional): set to `true` to signal a tool failure so Claude can react to it. See [Handle errors](#handle-errors).

After defining a tool, wrap it in a server with [`createSdkMcpServer`](/docs/en/agent-sdk/typescript#createsdkmcpserver) (TypeScript) or [`create_sdk_mcp_server`](/docs/en/agent-sdk/python#create_sdk_mcp_server) (Python). The server runs in-process inside your application, not as a separate process.

### Weather tool example

This example defines a `get_temperature` tool and wraps it in an MCP server. It only sets up the tool; to pass it to `query` and run it, see [Call a custom tool](#call-a-custom-tool) below.

<CodeGroup>
  ```python Python theme={null}
  from typing import Any
  import httpx
  from claude_agent_sdk import tool, create_sdk_mcp_server

  # Define a tool: name, description, input schema, handler
  @tool(
      "get_temperature",
      "Get the current temperature at a location",
      {"latitude": float, "longitude": float},
  )
  async def get_temperature(args: dict[str, Any]) -> dict[str, Any]:
      async with httpx.AsyncClient() as client:
          response = await client.get(
              "https://api.open-meteo.com/v1/forecast",
              params={
                  "latitude": args["latitude"],
                  "longitude": args["longitude"],
                  "current": "temperature_2m",
                  "temperature_unit": "fahrenheit",
              },
          )
          data = response.json()

      # Return a content array - Claude sees this as the tool result
      return {
          "content": [
              {
                  "type": "text",
                  "text": f"Temperature: {data['current']['temperature_2m']}°F",
              }
          ]
      }

  # Wrap the tool in an in-process MCP server
  weather_server = create_sdk_mcp_server(
      name="weather",
      version="1.0.0",
      tools=[get_temperature],
  )
  ```

  ```typescript TypeScript theme={null}

  // Define a tool: name, description, input schema, handler
  const getTemperature = tool(
    "get_temperature",
    "Get the current temperature at a location",
    {
      latitude: z.number().describe("Latitude coordinate"), // .describe() adds a field description Claude sees
      longitude: z.number().describe("Longitude coordinate")
    },
    async (args) => {
      // args is typed from the schema: { latitude: number; longitude: number }
      const response = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&current=temperature_2m&temperature_unit=fahrenheit`
      );
      const data: any = await response.json();

      // Return a content array - Claude sees this as the tool result
      return {
        content: [{ type: "text", text: `Temperature: ${data.current.temperature_2m}°F` }]
      };
    }
  );

  // Wrap the tool in an in-process MCP server
  const weatherServer = createSdkMcpServer({
    name: "weather",
    version: "1.0.0",
    tools: [getTemperature]
  });
  ```
</CodeGroup>

See the [`tool()`](/docs/en/agent-sdk/typescript#tool) TypeScript reference or the [`@tool`](/docs/en/agent-sdk/python#tool) Python reference for full parameter details, including JSON Schema input formats and return value structure.

<Tip>
  To make a parameter optional: in TypeScript, add `.default()` to the Zod field. In Python, the dict schema treats every key as required, so leave the parameter out of the schema, mention it in the description string, and read it with `args.get()` in the handler. The [`get_precipitation_chance` tool below](#add-more-tools) shows both patterns.
</Tip>

### Call a custom tool

Pass the MCP server you created to `query` via the `mcpServers` option. The key in `mcpServers` becomes the `{server_name}` segment in each tool's fully qualified name: `mcp__{server_name}__{tool_name}`. List that name in `allowedTools` so the tool runs without a permission prompt.

These snippets reuse the `weatherServer` from the [weather tool example](#weather-tool-example) to ask Claude what the weather is in a specific location.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={"weather": weather_server},
          allowed_tools=["mcp__weather__get_temperature"],
      )

      async for message in query(
          prompt="What's the temperature in San Francisco?",
          options=options,
      ):
          # ResultMessage is the final message after all tool calls complete
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "What's the temperature in San Francisco?",
    options: {
      mcpServers: { weather: weatherServer },
      allowedTools: ["mcp__weather__get_temperature"]
    }
  })) {
    // "result" is the final message after all tool calls complete
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

Combine this snippet with the tool and server definitions from the [weather tool example](#weather-tool-example) in one file, then run it with `python weather.py` for Python or `npx tsx weather.ts` for TypeScript. Claude calls `get_temperature` and the script prints a one-line answer with the current temperature in San Francisco.

### Add more tools

A server holds as many tools as you list in its `tools` array. With more than one tool on a server, you can list each one in `allowedTools` individually or use the wildcard `mcp__weather__*` to cover every tool the server exposes.

The example below defines a second tool, `get_precipitation_chance`, and replaces the `weatherServer` definition from the [weather tool example](#weather-tool-example) with one that lists both tools in the array.

<CodeGroup>
  ```python Python theme={null}
  # Define a second tool for the same server
  @tool(
      "get_precipitation_chance",
      "Get the hourly precipitation probability for a location. "
      "Optionally pass 'hours' (1-24) to control how many hours to return.",
      {"latitude": float, "longitude": float},
  )
  async def get_precipitation_chance(args: dict[str, Any]) -> dict[str, Any]:
      # 'hours' isn't in the schema - read it with .get() to make it optional
      hours = args.get("hours", 12)
      async with httpx.AsyncClient() as client:
          response = await client.get(
              "https://api.open-meteo.com/v1/forecast",
              params={
                  "latitude": args["latitude"],
                  "longitude": args["longitude"],
                  "hourly": "precipitation_probability",
                  "forecast_days": 1,
              },
          )
          data = response.json()
      chances = data["hourly"]["precipitation_probability"][:hours]

      return {
          "content": [
              {
                  "type": "text",
                  "text": f"Next {hours} hours: {'%, '.join(map(str, chances))}%",
              }
          ]
      }

  # Rebuild the server with both tools in the array
  weather_server = create_sdk_mcp_server(
      name="weather",
      version="1.0.0",
      tools=[get_temperature, get_precipitation_chance],
  )
  ```

  ```typescript TypeScript theme={null}
  // Define a second tool for the same server
  const getPrecipitationChance = tool(
    "get_precipitation_chance",
    "Get the hourly precipitation probability for a location",
    {
      latitude: z.number(),
      longitude: z.number(),
      hours: z
        .number()
        .int()
        .min(1)
        .max(24)
        .default(12) // .default() makes the parameter optional
        .describe("How many hours of forecast to return")
    },
    async (args) => {
      const response = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${args.latitude}&longitude=${args.longitude}&hourly=precipitation_probability&forecast_days=1`
      );
      const data: any = await response.json();
      const chances = data.hourly.precipitation_probability.slice(0, args.hours);

      return {
        content: [{ type: "text", text: `Next ${args.hours} hours: ${chances.join("%, ")}%` }]
      };
    }
  );

  // Rebuild the server with both tools in the array
  const weatherServer = createSdkMcpServer({
    name: "weather",
    version: "1.0.0",
    tools: [getTemperature, getPrecipitationChance]
  });
  ```
</CodeGroup>

[Tool search](/docs/en/agent-sdk/tool-search) is on by default and defers SDK MCP tools: Claude sees each tool's name in a compact list and loads its full schema on demand. With tool search disabled, every tool in this array consumes context window space on every turn. In TypeScript, pass `alwaysLoad: true` in the `extras` argument of [`tool()`](/docs/en/agent-sdk/typescript#tool) or in the options of [`createSdkMcpServer()`](/docs/en/agent-sdk/typescript#createsdkmcpserver) to keep a tool's full schema in the initial prompt.

### Add tool annotations

[Tool annotations](https://modelcontextprotocol.io/docs/concepts/tools#tool-annotations) are optional metadata describing how a tool behaves. Pass them as the fifth argument to `tool()` helper in TypeScript or via the `annotations` keyword argument for the `@tool` decorator in Python. All hint fields are Booleans.

| Field             | Default | Meaning                                                                                                               |
| :---------------- | :------ | :-------------------------------------------------------------------------------------------------------------------- |
| `readOnlyHint`    | `false` | Tool does not modify its environment. Controls whether the tool can be called in parallel with other read-only tools. |
| `destructiveHint` | `true`  | Tool may perform destructive updates. Informational only.                                                             |
| `idempotentHint`  | `false` | Repeated calls with the same arguments have no additional effect. Informational only.                                 |
| `openWorldHint`   | `true`  | Tool reaches systems outside your process. Informational only.                                                        |

Annotations are metadata, not enforcement. A tool marked `readOnlyHint: true` can still write to disk if that's what the handler does. Keep the annotation accurate to the handler.

This example adds `readOnlyHint` to the `get_temperature` tool from the [weather tool example](#weather-tool-example).

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import tool, ToolAnnotations

  @tool(
      "get_temperature",
      "Get the current temperature at a location",
      {"latitude": float, "longitude": float},
      annotations=ToolAnnotations(
          readOnlyHint=True
      ),  # Lets Claude batch this with other read-only calls
  )
  async def get_temperature(args):
      return {"content": [{"type": "text", "text": "..."}]}
  ```

  ```typescript TypeScript theme={null}

  tool(
    "get_temperature",
    "Get the current temperature at a location",
    { latitude: z.number(), longitude: z.number() },
    async (args) => ({ content: [{ type: "text", text: `...` }] }),
    { annotations: { readOnlyHint: true } } // Lets Claude batch this with other read-only calls
  );
  ```
</CodeGroup>

See `ToolAnnotations` in the [TypeScript](/docs/en/agent-sdk/typescript#toolannotations) or [Python](/docs/en/agent-sdk/python#toolannotations) reference.

## Control tool access

The [weather tool example](#weather-tool-example) registered a server and listed tools in `allowedTools`. This section covers how to scope access when you have multiple tools or want to restrict built-ins. For how tool names are constructed, see [Call a custom tool](#call-a-custom-tool).

### Configure allowed tools

The `tools` option and the allowed/disallowed lists affect two layers: availability, which controls whether a tool appears in Claude's context, and permission, which controls whether a call is approved once Claude attempts it. `tools` and bare-name `disallowedTools` entries change availability. `allowedTools` and scoped `disallowedTools` rules change permission. If you name one of the [task-tracking tools](/docs/en/agent-sdk/todo-tracking#model-availability) in `allowedTools`, Claude Code also opts the session in.

| Option                    | Layer        | Effect                                                                                                                                                                                                                                                           |
| :------------------------ | :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tools: ["Read", "Grep"]` | Availability | Only the listed built-ins are in Claude's context. Unlisted built-ins are removed. MCP tools are unaffected.                                                                                                                                                     |
| `tools: []`               | Availability | All built-ins are removed. Claude can only use your MCP tools.                                                                                                                                                                                                   |
| allowed tools             | Permission   | Listed tools run without a permission prompt. Other unlisted tools remain available; calls go through the [permission flow](/docs/en/agent-sdk/permissions).                                                                                                          |
| disallowed tools          | Both         | A bare tool name such as `"Bash"` removes the tool from Claude's context, the same as omitting it from `tools`. A scoped rule such as `"Bash(rm *)"` leaves the tool in context and denies only calls that match [as written](/docs/en/permissions#bash-rule-limits). |

To remove a built-in entirely, omit it from `tools` or list its bare name in `disallowedTools` (Python: `disallowed_tools`); both keep the tool out of context so Claude never attempts it. A scoped `disallowedTools` rule blocks matching calls but leaves the tool visible, so Claude may waste a turn trying it. See [Configure permissions](/docs/en/agent-sdk/permissions) for the full evaluation order.

## Handle errors

A handler error doesn't stop the agent loop. The SDK's in-process MCP server catches uncaught exceptions and returns them as error results, so how you report an error determines what Claude reads, not whether the query fails:

| What happens                                                                             | Result                                                                                                                                    |
| :--------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Handler throws an uncaught exception                                                     | The MCP server converts it to an error result carrying the raw exception message. Claude sees that message, and the agent loop continues. |
| Handler catches the error and returns `isError: true` (TS) / `"is_error": True` (Python) | Claude sees the message you compose. You can add context the raw exception lacks, such as which request failed or what to try instead.    |

In both cases Claude can retry, try a different tool, or explain the failure. Catch errors yourself when the raw exception message isn't enough for Claude to act on.

The example below catches two kinds of failures inside the handler and composes the error message Claude reads. A non-200 HTTP status is caught from the response and returned as an error result. A network error or invalid JSON is caught by the surrounding `try/except` (Python) or `try/catch` (TypeScript) and also returned as an error result. In both cases Claude receives a message that describes the failure instead of a bare exception string.

<CodeGroup>
  ```python Python theme={null}
  import json
  import httpx
  from typing import Any
  from claude_agent_sdk import tool

  @tool(
      "fetch_data",
      "Fetch data from an API",
      {"endpoint": str},  # Simple schema
  )
  async def fetch_data(args: dict[str, Any]) -> dict[str, Any]:
      try:
          async with httpx.AsyncClient() as client:
              response = await client.get(args["endpoint"])
              if response.status_code != 200:
                  # Return the failure as a tool result so Claude can react to it.
                  # is_error marks this as a failed call rather than odd-looking data.
                  return {
                      "content": [
                          {
                              "type": "text",
                              "text": f"API error: {response.status_code} {response.reason_phrase}",
                          }
                      ],
                      "is_error": True,
                  }

              data = response.json()
              return {"content": [{"type": "text", "text": json.dumps(data, indent=2)}]}
      except Exception as e:
          # Composes the message Claude reads. An uncaught exception would
          # reach Claude as the raw str(e) with no context.
          return {
              "content": [{"type": "text", "text": f"Failed to fetch data: {str(e)}"}],
              "is_error": True,
          }
  ```

  ```typescript TypeScript theme={null}

  tool(
    "fetch_data",
    "Fetch data from an API",
    {
      endpoint: z.string().url().describe("API endpoint URL")
    },
    async (args) => {
      try {
        const response = await fetch(args.endpoint);

        if (!response.ok) {
          // Return the failure as a tool result so Claude can react to it.
          // isError marks this as a failed call rather than odd-looking data.
          return {
            content: [
              {
                type: "text",
                text: `API error: ${response.status} ${response.statusText}`
              }
            ],
            isError: true
          };
        }

        const data = await response.json();
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(data, null, 2)
            }
          ]
        };
      } catch (error) {
        // Composes the message Claude reads. An uncaught throw would
        // reach Claude as the raw error message with no context.
        return {
          content: [
            {
              type: "text",
              text: `Failed to fetch data: ${error instanceof Error ? error.message : String(error)}`
            }
          ],
          isError: true
        };
      }
    }
  );
  ```
</CodeGroup>

## Return images and resources

The `content` array in a tool result accepts `text`, `image`, `audio`, `resource`, and `resource_link` blocks. You can mix them in the same response. In TypeScript, the SDK saves audio blocks to disk and Claude receives a text block with the saved file path; in Python, the SDK drops audio blocks from the tool result and logs a warning.

Claude receives each resource link block as a text block containing the link's name, URI, and description. In TypeScript, your application also receives the links themselves as [`resourceLinks`](/docs/en/agent-sdk/typescript#sdkmcpresourcelink) on the user message's `tool_use_result`; in Python, the SDK flattens them to text before the CLI sees the result, so the Python [`resourceLinks` key](/docs/en/agent-sdk/python#usermessage) is never produced for in-process tools.

### Images

An image block carries the image bytes inline, encoded as base64. There is no URL field. To return an image that lives at a URL, fetch it in the handler, read the response bytes, and base64-encode them before returning. The result is processed as visual input.

| Field      | Type      | Notes                                                                      |
| :--------- | :-------- | :------------------------------------------------------------------------- |
| `type`     | `"image"` |                                                                            |
| `data`     | `string`  | Base64-encoded bytes. Raw base64 only, no `data:image/...;base64,` prefix  |
| `mimeType` | `string`  | Required. For example `image/png`, `image/jpeg`, `image/webp`, `image/gif` |

<CodeGroup>
  ```python Python theme={null}
  import base64
  import httpx
  from claude_agent_sdk import tool

  # Define a tool that fetches an image from a URL and returns it to Claude
  @tool("fetch_image", "Fetch an image from a URL and return it to Claude", {"url": str})
  async def fetch_image(args):
      async with httpx.AsyncClient() as client:  # Fetch the image bytes
          response = await client.get(args["url"])

      return {
          "content": [
              {
                  "type": "image",
                  "data": base64.b64encode(response.content).decode(
                      "ascii"
                  ),  # Base64-encode the raw bytes
                  "mimeType": response.headers.get(
                      "content-type", "image/png"
                  ),  # Read MIME type from the response
              }
          ]
      }
  ```

  ```typescript TypeScript theme={null}

  tool(
    "fetch_image",
    "Fetch an image from a URL and return it to Claude",
    {
      url: z.string().url()
    },
    async (args) => {
      const response = await fetch(args.url); // Fetch the image bytes
      const buffer = Buffer.from(await response.arrayBuffer()); // Read into a Buffer for base64 encoding
      const mimeType = response.headers.get("content-type") ?? "image/png";

      return {
        content: [
          {
            type: "image",
            data: buffer.toString("base64"), // Base64-encode the raw bytes
            mimeType
          }
        ]
      };
    }
  );
  ```
</CodeGroup>

### Resources

A resource block embeds a piece of content identified by a URI. The URI is a label for Claude to reference; the actual content rides in the block's `text` or `blob` field. Use this when your tool produces something that makes sense to address by name later, such as a generated file or a record from an external system.

| Field               | Type         | Notes                                                                                                                                      |
| :------------------ | :----------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| `type`              | `"resource"` |                                                                                                                                            |
| `resource.uri`      | `string`     | Identifier for the content. Any URI scheme                                                                                                 |
| `resource.text`     | `string`     | The content, if it's text. Provide this or `blob`, not both                                                                                |
| `resource.blob`     | `string`     | The content base64-encoded, if it's binary. TypeScript only: the Python SDK drops binary resources from the tool result and logs a warning |
| `resource.mimeType` | `string`     | Optional                                                                                                                                   |

This example shows a resource block returned from inside a tool handler. The URI `file:///tmp/report.md` is a label that Claude can reference later; the SDK does not read from that path.

<CodeGroup>
  ```typescript TypeScript theme={null}
  return {
    content: [
      {
        type: "resource",
        resource: {
          uri: "file:///tmp/report.md", // Label for Claude to reference, not a path the SDK reads
          mimeType: "text/markdown",
          text: "# Report\n..." // The actual content, inline
        }
      }
    ]
  };
  ```

  ```python Python theme={null}
  return {
      "content": [
          {
              "type": "resource",
              "resource": {
                  "uri": "file:///tmp/report.md",  # Label for Claude to reference, not a path the SDK reads
                  "mimeType": "text/markdown",
                  "text": "# Report\n...",  # The actual content, inline
              },
          }
      ]
  }
  ```
</CodeGroup>

These block shapes come from the MCP `CallToolResult` type. See the [MCP specification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool-result) for the full definition.

## Return structured data

`structuredContent` is an optional JSON object on the result, separate from the `content` array. Use it to return raw values that Claude can read as exact fields instead of parsing them out of a text string or image.

When `structuredContent` is set, Claude receives the JSON plus any image or resource blocks from `content`. Text blocks in `content` are not forwarded, since they are assumed to duplicate the structured data. The example below renders a chart as an image block and returns the data points behind it in `structuredContent` from the same handler. In the snippet, `chartPngBuffer` is a `Buffer` holding the rendered PNG bytes.

```typescript TypeScript theme={null}
return {
  content: [
    {
      type: "image",
      data: chartPngBuffer.toString("base64"),
      mimeType: "image/png"
    }
  ],
  structuredContent: {
    series: "temperature_2m",
    unit: "fahrenheit",
    points: [62.1, 63.4, 65.0, 64.2]
  }
};
```

<Note>
  The Python `@tool` decorator forwards only `content` and `is_error` from the handler's return dict. To return `structuredContent` from Python, run a [standalone MCP server](/docs/en/agent-sdk/mcp) instead of an in-process SDK server.
</Note>

## Example: unit converter

This tool converts values between units of length, temperature, and weight. A user can ask "convert 100 kilometers to miles" or "what is 72°F in Celsius," and Claude picks the right unit type and units from the request.

It demonstrates two patterns:

* **Enum schemas:** `unit_type` is constrained to a fixed set of values. In TypeScript, use `z.enum()`. In Python, the dict schema doesn't support enums, so the full JSON Schema dict is required.
* **Unsupported input handling:** when a conversion pair isn't found, the handler returns `isError: true` so Claude can tell the user what went wrong rather than treating a failure as a normal result.

<CodeGroup>
  ```python Python theme={null}
  from typing import Any
  from claude_agent_sdk import tool, create_sdk_mcp_server

  # z.enum() in TypeScript becomes an "enum" constraint in JSON Schema.
  # The dict schema has no equivalent, so full JSON Schema is required.
  @tool(
      "convert_units",
      "Convert a value from one unit to another",
      {
          "type": "object",
          "properties": {
              "unit_type": {
                  "type": "string",
                  "enum": ["length", "temperature", "weight"],
                  "description": "Category of unit",
              },
              "from_unit": {
                  "type": "string",
                  "description": "Unit to convert from, e.g. kilometers, fahrenheit, pounds",
              },
              "to_unit": {"type": "string", "description": "Unit to convert to"},
              "value": {"type": "number", "description": "Value to convert"},
          },
          "required": ["unit_type", "from_unit", "to_unit", "value"],
      },
  )
  async def convert_units(args: dict[str, Any]) -> dict[str, Any]:
      conversions = {
          "length": {
              "kilometers_to_miles": lambda v: v * 0.621371,
              "miles_to_kilometers": lambda v: v * 1.60934,
              "meters_to_feet": lambda v: v * 3.28084,
              "feet_to_meters": lambda v: v * 0.3048,
          },
          "temperature": {
              "celsius_to_fahrenheit": lambda v: (v * 9) / 5 + 32,
              "fahrenheit_to_celsius": lambda v: (v - 32) * 5 / 9,
              "celsius_to_kelvin": lambda v: v + 273.15,
              "kelvin_to_celsius": lambda v: v - 273.15,
          },
          "weight": {
              "kilograms_to_pounds": lambda v: v * 2.20462,
              "pounds_to_kilograms": lambda v: v * 0.453592,
              "grams_to_ounces": lambda v: v * 0.035274,
              "ounces_to_grams": lambda v: v * 28.3495,
          },
      }

      key = f"{args['from_unit']}_to_{args['to_unit']}"
      fn = conversions.get(args["unit_type"], {}).get(key)

      if not fn:
          return {
              "content": [
                  {
                      "type": "text",
                      "text": f"Unsupported conversion: {args['from_unit']} to {args['to_unit']}",
                  }
              ],
              "is_error": True,
          }

      result = fn(args["value"])
      return {
          "content": [
              {
                  "type": "text",
                  "text": f"{args['value']} {args['from_unit']} = {result:.4f} {args['to_unit']}",
              }
          ]
      }

  converter_server = create_sdk_mcp_server(
      name="converter",
      version="1.0.0",
      tools=[convert_units],
  )
  ```

  ```typescript TypeScript theme={null}

  const convert = tool(
    "convert_units",
    "Convert a value from one unit to another",
    {
      unit_type: z.enum(["length", "temperature", "weight"]).describe("Category of unit"),
      from_unit: z
        .string()
        .describe("Unit to convert from, e.g. kilometers, fahrenheit, pounds"),
      to_unit: z.string().describe("Unit to convert to"),
      value: z.number().describe("Value to convert")
    },
    async (args) => {
      type Conversions = Record<string, Record<string, (v: number) => number>>;

      const conversions: Conversions = {
        length: {
          kilometers_to_miles: (v) => v * 0.621371,
          miles_to_kilometers: (v) => v * 1.60934,
          meters_to_feet: (v) => v * 3.28084,
          feet_to_meters: (v) => v * 0.3048
        },
        temperature: {
          celsius_to_fahrenheit: (v) => (v * 9) / 5 + 32,
          fahrenheit_to_celsius: (v) => ((v - 32) * 5) / 9,
          celsius_to_kelvin: (v) => v + 273.15,
          kelvin_to_celsius: (v) => v - 273.15
        },
        weight: {
          kilograms_to_pounds: (v) => v * 2.20462,
          pounds_to_kilograms: (v) => v * 0.453592,
          grams_to_ounces: (v) => v * 0.035274,
          ounces_to_grams: (v) => v * 28.3495
        }
      };

      const key = `${args.from_unit}_to_${args.to_unit}`;
      const fn = conversions[args.unit_type]?.[key];

      if (!fn) {
        return {
          content: [
            {
              type: "text",
              text: `Unsupported conversion: ${args.from_unit} to ${args.to_unit}`
            }
          ],
          isError: true
        };
      }

      const result = fn(args.value);
      return {
        content: [
          {
            type: "text",
            text: `${args.value} ${args.from_unit} = ${result.toFixed(4)} ${args.to_unit}`
          }
        ]
      };
    }
  );

  const converterServer = createSdkMcpServer({
    name: "converter",
    version: "1.0.0",
    tools: [convert]
  });
  ```
</CodeGroup>

Once the server is defined, pass it to `query` the same way as the weather example. This example sends three different prompts in a loop to show the same tool handling different unit types. For each response, it inspects `AssistantMessage` objects (which contain the tool calls Claude made during that turn) and prints each `ToolUseBlock` before printing the final `ResultMessage` text. This lets you see when Claude is using the tool versus answering from its own knowledge.

Because [tool search](/docs/en/agent-sdk/tool-search) is on by default, the output may also include a `ToolSearch` call as Claude loads the deferred tool schema.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import (
      query,
      ClaudeAgentOptions,
      ResultMessage,
      AssistantMessage,
      ToolUseBlock,
  )

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={"converter": converter_server},
          allowed_tools=["mcp__converter__convert_units"],
      )

      prompts = [
          "Convert 100 kilometers to miles.",
          "What is 72°F in Celsius?",
          "How many pounds is 5 kilograms?",
      ]

      for prompt in prompts:
          try:
              async for message in query(prompt=prompt, options=options):
                  if isinstance(message, AssistantMessage):
                      for block in message.content:
                          if isinstance(block, ToolUseBlock):
                              print(f"[tool call] {block.name}({block.input})")
                  elif isinstance(message, ResultMessage) and message.subtype == "success":
                      print(f"Q: {prompt}\nA: {message.result}\n")
          except Exception as error:
              # A single-shot query() raises after yielding an error result. Only success
              # results are printed above, so handle the failure here and continue with
              # the next prompt.
              print(f"Call failed: {error}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  const prompts = [
    "Convert 100 kilometers to miles.",
    "What is 72°F in Celsius?",
    "How many pounds is 5 kilograms?"
  ];

  for (const prompt of prompts) {
    try {
      for await (const message of query({
        prompt,
        options: {
          mcpServers: { converter: converterServer },
          allowedTools: ["mcp__converter__convert_units"]
        }
      })) {
        if (message.type === "assistant") {
          for (const block of message.message.content) {
            if (block.type === "tool_use") {
              console.log(`[tool call] ${block.name}`, block.input);
            }
          }
        } else if (message.type === "result" && message.subtype === "success") {
          console.log(`Q: ${prompt}\nA: ${message.result}\n`);
        }
      }
    } catch (error) {
      // A single-shot query() throws after yielding an error result. Only success
      // results are logged above, so handle the failure here and continue with
      // the next prompt.
      console.error(`Call failed: ${error}`);
    }
  }
  ```
</CodeGroup>

## Next steps

You can mix the patterns on this page in the same server: a single server can hold a database tool, an API gateway tool, and an image renderer alongside each other.

From here:

* If your server grows to dozens of tools, see [tool search](/docs/en/agent-sdk/tool-search) to defer loading them until Claude needs them.
* To connect to external MCP servers (filesystem, GitHub, Slack) instead of building your own, see [Connect MCP servers](/docs/en/agent-sdk/mcp).
* To control which tools run automatically versus requiring approval, see [Configure permissions](/docs/en/agent-sdk/permissions).

---

## Examples

- 官方原文：https://code.claude.com/docs/en/agent-sdk/examples.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-examples.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples

> Find a complete, runnable Agent SDK project or a guided recipe in the Claude Cookbook that matches what you want to build.

This page routes you to complete, runnable Agent SDK projects and guided Claude Cookbook recipes. TypeScript applications live in the [`claude-agent-sdk-demos`](https://github.com/anthropics/claude-agent-sdk-demos) repo, and Python recipes live in the [Claude Cookbook](https://platform.claude.com/cookbook).

## Run a minimal agent first

If you haven't built anything with the SDK yet, start with one of these before a full application:

* [Agent SDK quickstart](/docs/en/agent-sdk/quickstart): build your first working agent in TypeScript or Python, with setup steps included. The agent finds and fixes bugs in a sample file.

* [Hello World](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world): a minimal TypeScript project to clone when you want to start from repo code

## Explore a TypeScript application

The TypeScript applications in [`claude-agent-sdk-demos`](https://github.com/anthropics/claude-agent-sdk-demos) are demos for local development, from an email client to a multi-agent research system. Clone the demo whose shape matches what you're building.

## Work through a Python recipe

The Claude Cookbook's Agent SDK series is a sequence of recipes, each a Python notebook, that progresses from a simple research agent to sophisticated multi-agent systems. Each notebook builds on the previous one, introducing new concepts and capabilities. Start with [the one-liner research agent](https://platform.claude.com/cookbook/claude-agent-sdk-00-the-one-liner-research-agent) and work forward.

For recipes across Claude products, see the full [Claude Cookbook](https://platform.claude.com/cookbook).

---

## Rewind file changes with checkpointing

- 官方原文：https://code.claude.com/docs/en/agent-sdk/file-checkpointing.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-file-checkpointing.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rewind file changes with checkpointing

> Track file changes during agent sessions and restore files to any previous state

File checkpointing tracks file modifications made through the Write, Edit, and NotebookEdit tools during an agent session, allowing you to rewind files to any previous state. Want to try it out? Jump to the [interactive example](#try-it-out).

With checkpointing, you can:

* **Undo unwanted changes** by restoring files to a known good state
* **Explore alternatives** by restoring to a checkpoint and trying a different approach
* **Recover from errors** when the agent makes incorrect modifications

<Warning>
  Only changes made through the Write, Edit, and NotebookEdit tools are tracked. Changes made through Bash commands (like `echo > file.txt` or `sed -i`) are not captured by the checkpoint system, and neither are edits a [subagent](/docs/en/agent-sdk/subagents) applies, except a [skill with `context: fork`](/docs/en/skills#run-skills-in-a-subagent) that runs in the foreground.
</Warning>

## How checkpointing works

When you enable file checkpointing, the SDK creates backups of files before modifying them through the Write, Edit, or NotebookEdit tools. User messages in the response stream include a checkpoint UUID that you can use as a restore point.

<Note>
  File rewinding restores files on disk to a previous state. It does not rewind the conversation itself. The conversation history and context remain intact after calling `rewindFiles()` (TypeScript) or `rewind_files()` (Python).
</Note>

When you rewind to a checkpoint, Claude Code deletes the files it created and restores the files it modified to their content at that point. Claude Code skips a tracked path that is a symlink, hard link, or other non-regular file. It also skips a tracked file whose parent directory no longer resolves to its checkpoint-time location, or whose backup it can't read safely. [`RewindFilesResult`](/docs/en/agent-sdk/typescript#rewindfilesresult) counts every skipped path in its `skippedLinks` field. Skipping requires Claude Code v2.1.216 or later; before v2.1.216, a rewind wrote and deleted through links at tracked paths.

## Implement checkpointing

To use file checkpointing, enable it in your options, capture checkpoint UUIDs from the response stream, then call `rewindFiles()` (TypeScript) or `rewind_files()` (Python) when you need to restore.

The following example shows the complete flow: enable checkpointing, capture the checkpoint UUID and session ID from the response stream, then resume the session later to rewind files. Each step is explained in detail below. The examples in this section use the prompt "Refactor the authentication module". Run them in a project that contains an authentication module, or change the prompt to name files that exist in your project, so you can watch files change and see the rewind restore them.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import (
      ClaudeSDKClient,
      ClaudeAgentOptions,
      UserMessage,
      ResultMessage,
  )

  async def main():
      # Step 1: Enable checkpointing
      options = ClaudeAgentOptions(
          enable_file_checkpointing=True,
          permission_mode="acceptEdits",  # Auto-accept file edits without prompting
          extra_args={
              "replay-user-messages": None
          },  # Required to receive checkpoint UUIDs in the response stream
      )

      checkpoint_id = None
      session_id = None

      # Run the query and capture checkpoint UUID and session ID
      async with ClaudeSDKClient(options) as client:
          await client.query("Refactor the authentication module")

          # Step 2: Capture checkpoint UUID from the first user message
          async for message in client.receive_response():
              if isinstance(message, UserMessage) and message.uuid and not checkpoint_id:
                  checkpoint_id = message.uuid
              if isinstance(message, ResultMessage) and not session_id:
                  session_id = message.session_id

      # Step 3: Later, rewind by resuming the session with an empty prompt
      if checkpoint_id and session_id:
          async with ClaudeSDKClient(
              ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
          ) as client:
              await client.query("")  # Empty prompt to open the connection
              async for message in client.receive_response():
                  await client.rewind_files(checkpoint_id)
                  break
          print(f"Rewound to checkpoint: {checkpoint_id}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  async function main() {
    // Step 1: Enable checkpointing
    const opts = {
      enableFileCheckpointing: true,
      permissionMode: "acceptEdits" as const, // Auto-accept file edits without prompting
      extraArgs: { "replay-user-messages": null } // Required to receive checkpoint UUIDs in the response stream
    };

    const response = query({
      prompt: "Refactor the authentication module",
      options: opts
    });

    let checkpointId: string | undefined;
    let sessionId: string | undefined;

    // Step 2: Capture checkpoint UUID from the first user message
    try {
      for await (const message of response) {
        if (message.type === "user" && message.uuid && !checkpointId) {
          checkpointId = message.uuid;
        }
        if ("session_id" in message && !sessionId) {
          sessionId = message.session_id;
        }
      }
    } catch (error) {
      // A single-shot query() throws after yielding an error result. If the
      // failure was an error result, sessionId and checkpointId were already
      // captured by the loop above; connection or process failures yield no
      // result message.
      console.error(`Session ended with an error: ${error}`);
    }

    // Step 3: Later, rewind by resuming the session with an empty prompt
    if (checkpointId && sessionId) {
      const rewindQuery = query({
        prompt: "", // Empty prompt to open the connection
        options: { ...opts, resume: sessionId }
      });

      for await (const msg of rewindQuery) {
        await rewindQuery.rewindFiles(checkpointId);
        break;
      }
      console.log(`Rewound to checkpoint: ${checkpointId}`);
    }
  }

  main();
  ```
</CodeGroup>

    Configure your SDK options to enable checkpointing and receive checkpoint UUIDs:

    | Option                   | Python                                      | TypeScript                                    | Description                                      |
    | ------------------------ | ------------------------------------------- | --------------------------------------------- | ------------------------------------------------ |
    | Enable checkpointing     | `enable_file_checkpointing=True`            | `enableFileCheckpointing: true`               | Tracks file changes for rewinding                |
    | Receive checkpoint UUIDs | `extra_args={"replay-user-messages": None}` | `extraArgs: { 'replay-user-messages': null }` | Required to get user message UUIDs in the stream |

    <CodeGroup>
      ```python Python theme={null}
      options = ClaudeAgentOptions(
          enable_file_checkpointing=True,
          permission_mode="acceptEdits",
          extra_args={"replay-user-messages": None},
      )

      async with ClaudeSDKClient(options) as client:
          await client.query("Refactor the authentication module")
      ```

      ```typescript TypeScript theme={null}
      const response = query({
        prompt: "Refactor the authentication module",
        options: {
          enableFileCheckpointing: true,
          permissionMode: "acceptEdits" as const,
          extraArgs: { "replay-user-messages": null }
        }
      });
      ```
    </CodeGroup>

    With the `replay-user-messages` option set, each user message in the response stream has a UUID that serves as a checkpoint.

    For most use cases, capture the first user message UUID (`message.uuid`); rewinding to it restores the tracked files to their original state. To store multiple checkpoints and rewind to intermediate states, see [Multiple restore points](#multiple-restore-points).

    Capturing the session ID (`message.session_id`) is optional; you only need it if you want to rewind later, after the stream completes. If you're calling `rewindFiles()` immediately while still processing messages (as the example in [Checkpoint before risky operations](#checkpoint-before-risky-operations) does), you can skip capturing the session ID.

    <CodeGroup>
      ```python Python theme={null}
      checkpoint_id = None
      session_id = None

      async for message in client.receive_response():
          # Capture the first user message UUID as the checkpoint
          if isinstance(message, UserMessage) and message.uuid and checkpoint_id is None:
              checkpoint_id = message.uuid
          # Capture session ID from the result message
          if isinstance(message, ResultMessage):
              session_id = message.session_id
      ```

      ```typescript TypeScript theme={null}
      let checkpointId: string | undefined;
      let sessionId: string | undefined;

      for await (const message of response) {
        // Capture the first user message UUID as the checkpoint
        if (message.type === "user" && message.uuid && !checkpointId) {
          checkpointId = message.uuid;
        }
        // Capture session ID from any message that has it
        if ("session_id" in message) {
          sessionId = message.session_id;
        }
      }
      ```
    </CodeGroup>

    To rewind after the stream completes, resume the session with an empty prompt and call `rewind_files()` (Python) or `rewindFiles()` (TypeScript) with your checkpoint UUID. You can also rewind during the stream; see [Checkpoint before risky operations](#checkpoint-before-risky-operations) for that pattern.

    <CodeGroup>
      ```python Python theme={null}
      async with ClaudeSDKClient(
          ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
      ) as client:
          await client.query("")  # Empty prompt to open the connection
          async for message in client.receive_response():
              if checkpoint_id:
                  await client.rewind_files(checkpoint_id)
              break
      ```

      ```typescript TypeScript theme={null}
      const rewindQuery = query({
        prompt: "", // Empty prompt to open the connection
        options: { ...opts, resume: sessionId }
      });

      for await (const msg of rewindQuery) {
        if (checkpointId) {
          await rewindQuery.rewindFiles(checkpointId);
        }
        break;
      }
      ```
    </CodeGroup>

    If you capture the session ID and checkpoint ID, you can also rewind from the CLI. This command requires the `claude` executable, which comes from [installing Claude Code](/docs/en/setup) and is not installed by the SDK package. The SDK enables checkpointing for you, but when you run `claude -p` directly you must set the `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING` environment variable:

    ```bash theme={null}
    CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=true claude -p --resume <session-id> --rewind-files <checkpoint-uuid>
    ```

    The `--rewind-files` flag doesn't appear in `claude --help` output, but the CLI accepts it as shown. When the rewind succeeds, the command prints `Files rewound to state at message <checkpoint-uuid>` and exits without sending a prompt.

## Common patterns

These patterns show different ways to capture and use checkpoint UUIDs depending on your use case.

### Checkpoint before risky operations

This pattern keeps only the most recent checkpoint UUID, updating it before each agent turn. If something goes wrong during processing, you can immediately rewind to the last safe state and break out of the loop.

Before running this example, replace `your_revert_condition` (Python) or `yourRevertCondition` (TypeScript) with your own check, such as error detection or a validation failure; the placeholder is not defined in the example.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, UserMessage

  async def main():
      options = ClaudeAgentOptions(
          enable_file_checkpointing=True,
          permission_mode="acceptEdits",
          extra_args={"replay-user-messages": None},
      )

      safe_checkpoint = None

      async with ClaudeSDKClient(options) as client:
          await client.query("Refactor the authentication module")

          async for message in client.receive_response():
              # Update checkpoint before each agent turn starts
              # This overwrites the previous checkpoint. Only keep the latest
              if isinstance(message, UserMessage) and message.uuid:
                  safe_checkpoint = message.uuid

              # Decide when to revert based on your own logic
              # For example: error detection, validation failure, or user input
              if your_revert_condition and safe_checkpoint:
                  await client.rewind_files(safe_checkpoint)
                  # Exit the loop after rewinding, files are restored
                  break

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  async function main() {
    const response = query({
      prompt: "Refactor the authentication module",
      options: {
        enableFileCheckpointing: true,
        permissionMode: "acceptEdits" as const,
        extraArgs: { "replay-user-messages": null }
      }
    });

    let safeCheckpoint: string | undefined;

    for await (const message of response) {
      // Update checkpoint before each agent turn starts
      // This overwrites the previous checkpoint. Only keep the latest
      if (message.type === "user" && message.uuid) {
        safeCheckpoint = message.uuid;
      }

      // Decide when to revert based on your own logic
      // For example: error detection, validation failure, or user input
      if (yourRevertCondition && safeCheckpoint) {
        await response.rewindFiles(safeCheckpoint);
        // Exit the loop after rewinding, files are restored
        break;
      }
    }
  }

  main();
  ```
</CodeGroup>

### Multiple restore points

If Claude makes changes across multiple turns, you might want to rewind to a specific point rather than all the way back. For example, if Claude refactors a file in turn one and adds tests in turn two, you might want to keep the refactor but undo the tests.

This pattern stores all checkpoint UUIDs in an array with metadata. After the session completes, you can rewind to any previous checkpoint:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from dataclasses import dataclass
  from datetime import datetime
  from claude_agent_sdk import (
      ClaudeSDKClient,
      ClaudeAgentOptions,
      UserMessage,
      ResultMessage,
  )

  # Store checkpoint metadata for better tracking
  @dataclass
  class Checkpoint:
      id: str
      description: str
      timestamp: datetime

  async def main():
      options = ClaudeAgentOptions(
          enable_file_checkpointing=True,
          permission_mode="acceptEdits",
          extra_args={"replay-user-messages": None},
      )

      checkpoints = []
      session_id = None

      async with ClaudeSDKClient(options) as client:
          await client.query("Refactor the authentication module")

          async for message in client.receive_response():
              if isinstance(message, UserMessage) and message.uuid:
                  checkpoints.append(
                      Checkpoint(
                          id=message.uuid,
                          description=f"After turn {len(checkpoints) + 1}",
                          timestamp=datetime.now(),
                      )
                  )
              if isinstance(message, ResultMessage) and not session_id:
                  session_id = message.session_id

      # Later: rewind to any checkpoint by resuming the session
      if checkpoints and session_id:
          target = checkpoints[0]  # Pick any checkpoint
          async with ClaudeSDKClient(
              ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
          ) as client:
              await client.query("")  # Empty prompt to open the connection
              async for message in client.receive_response():
                  await client.rewind_files(target.id)
                  break
          print(f"Rewound to: {target.description}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Store checkpoint metadata for better tracking
  interface Checkpoint {
    id: string;
    description: string;
    timestamp: Date;
  }

  async function main() {
    const opts = {
      enableFileCheckpointing: true,
      permissionMode: "acceptEdits" as const,
      extraArgs: { "replay-user-messages": null }
    };

    const response = query({
      prompt: "Refactor the authentication module",
      options: opts
    });

    const checkpoints: Checkpoint[] = [];
    let sessionId: string | undefined;

    try {
      for await (const message of response) {
        if (message.type === "user" && message.uuid) {
          checkpoints.push({
            id: message.uuid,
            description: `After turn ${checkpoints.length + 1}`,
            timestamp: new Date()
          });
        }
        if ("session_id" in message && !sessionId) {
          sessionId = message.session_id;
        }
      }
    } catch (error) {
      // A single-shot query() throws after yielding an error result. If the
      // failure was an error result, sessionId and the checkpoints array were
      // already populated by the loop above; connection or process failures
      // yield no result message.
      console.error(`Session ended with an error: ${error}`);
    }

    // Later: rewind to any checkpoint by resuming the session
    if (checkpoints.length > 0 && sessionId) {
      const target = checkpoints[0]; // Pick any checkpoint
      const rewindQuery = query({
        prompt: "", // Empty prompt to open the connection
        options: { ...opts, resume: sessionId }
      });

      for await (const msg of rewindQuery) {
        await rewindQuery.rewindFiles(target.id);
        break;
      }
      console.log(`Rewound to: ${target.description}`);
    }
  }

  main();
  ```
</CodeGroup>

## Try it out

This complete example creates a small utility file, has the agent add documentation comments, shows you the changes, then asks if you want to rewind.

Before you begin, make sure you have the [Claude Agent SDK installed](/docs/en/agent-sdk/quickstart).

    Create a new file called `utils.py` (Python) or `utils.ts` (TypeScript) and paste the following code:

    <CodeGroup>
      ```python utils.py theme={null}
      def add(a, b):
          return a + b

      def subtract(a, b):
          return a - b

      def multiply(a, b):
          return a * b

      def divide(a, b):
          if b == 0:
              raise ValueError("Cannot divide by zero")
          return a / b
      ```

      ```typescript utils.ts theme={null}
      export function add(a: number, b: number): number {
        return a + b;
      }

      export function subtract(a: number, b: number): number {
        return a - b;
      }

      export function multiply(a: number, b: number): number {
        return a * b;
      }

      export function divide(a: number, b: number): number {
        if (b === 0) {
          throw new Error("Cannot divide by zero");
        }
        return a / b;
      }
      ```
    </CodeGroup>

    Create a new file called `try_checkpointing.py` (Python) or `try_checkpointing.ts` (TypeScript) in the same directory as your utility file, and paste the following code.

    This script asks Claude to add doc comments to your utility file, then gives you the option to rewind and restore the original.

    <CodeGroup>
      ```python try_checkpointing.py theme={null}
      import asyncio
      from claude_agent_sdk import (
          ClaudeSDKClient,
          ClaudeAgentOptions,
          UserMessage,
          ResultMessage,
      )

      async def main():
          # Configure the SDK with checkpointing enabled
          # - enable_file_checkpointing: Track file changes for rewinding
          # - permission_mode: Auto-accept file edits without prompting
          # - extra_args: Required to receive user message UUIDs in the stream
          options = ClaudeAgentOptions(
              enable_file_checkpointing=True,
              permission_mode="acceptEdits",
              extra_args={"replay-user-messages": None},
          )

          checkpoint_id = None  # Store the user message UUID for rewinding
          session_id = None  # Store the session ID for resuming

          print("Running agent to add doc comments to utils.py...\n")

          # Run the agent and capture checkpoint data from the response stream
          async with ClaudeSDKClient(options) as client:
              await client.query("Add doc comments to utils.py")

              async for message in client.receive_response():
                  # Capture the first user message UUID - this is our restore point
                  if isinstance(message, UserMessage) and message.uuid and not checkpoint_id:
                      checkpoint_id = message.uuid
                  # Capture the session ID so we can resume later
                  if isinstance(message, ResultMessage):
                      session_id = message.session_id

          print("Done! Open utils.py to see the added doc comments.\n")

          # Ask the user if they want to rewind the changes
          if checkpoint_id and session_id:
              response = input("Rewind to remove the doc comments? (y/n): ")

              if response.lower() == "y":
                  # Resume the session with an empty prompt, then rewind
                  async with ClaudeSDKClient(
                      ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
                  ) as client:
                      await client.query("")  # Empty prompt opens the connection
                      async for message in client.receive_response():
                          await client.rewind_files(checkpoint_id)  # Restore files
                          break

                  print(
                      "\n✓ File restored! Open utils.py to verify the doc comments are gone."
                  )
              else:
                  print("\nKept the modified file.")

      asyncio.run(main())
      ```

      ```typescript try_checkpointing.ts theme={null}

      async function main() {
        // Configure the SDK with checkpointing enabled
        // - enableFileCheckpointing: Track file changes for rewinding
        // - permissionMode: Auto-accept file edits without prompting
        // - extraArgs: Required to receive user message UUIDs in the stream
        const opts = {
          enableFileCheckpointing: true,
          permissionMode: "acceptEdits" as const,
          extraArgs: { "replay-user-messages": null }
        };

        let sessionId: string | undefined; // Store the session ID for resuming
        let checkpointId: string | undefined; // Store the user message UUID for rewinding

        console.log("Running agent to add doc comments to utils.ts...\n");

        // Run the agent and capture checkpoint data from the response stream
        const response = query({
          prompt: "Add doc comments to utils.ts",
          options: opts
        });

        try {
          for await (const message of response) {
            // Capture the first user message UUID - this is our restore point
            if (message.type === "user" && message.uuid && !checkpointId) {
              checkpointId = message.uuid;
            }
            // Capture the session ID so we can resume later
            if ("session_id" in message) {
              sessionId = message.session_id;
            }
          }
        } catch (error) {
          // A single-shot query() throws after yielding an error result. If the
          // failure was an error result, checkpointId and sessionId were already
          // captured by the loop above; connection or process failures yield no
          // result message.
          console.error(`Session ended with an error: ${error}`);
        }

        console.log("Done! Open utils.ts to see the added doc comments.\n");

        // Ask the user if they want to rewind the changes
        if (checkpointId && sessionId) {
          const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
          });

          const answer = await new Promise<string>((resolve) => {
            rl.question("Rewind to remove the doc comments? (y/n): ", resolve);
          });
          rl.close();

          if (answer.toLowerCase() === "y") {
            // Resume the session with an empty prompt, then rewind
            const rewindQuery = query({
              prompt: "", // Empty prompt opens the connection
              options: { ...opts, resume: sessionId }
            });

            for await (const msg of rewindQuery) {
              await rewindQuery.rewindFiles(checkpointId); // Restore files
              break;
            }

            console.log("\n✓ File restored! Open utils.ts to verify the doc comments are gone.");
          } else {
            console.log("\nKept the modified file.");
          }
        }
      }

      main();
      ```
    </CodeGroup>

    Run the script from the same directory as your utility file.

    <Tip>
      Open your utility file (`utils.py` or `utils.ts`) in your IDE or editor before running the script. You'll see the file update in real-time as the agent adds doc comments, then revert back to the original when you choose to rewind.
    </Tip>

      <Tab title="Python">
        ```bash theme={null}
        python try_checkpointing.py
        ```
      </Tab>

      <Tab title="TypeScript">
        ```bash theme={null}
        npx tsx try_checkpointing.ts
        ```
      </Tab>

    You'll see the agent add doc comments, then a prompt asking if you want to rewind. If you choose yes, the file is restored to its original state.

## Limitations

File checkpointing has the following limitations:

| Limitation                         | Description                                                                                                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Write/Edit/NotebookEdit tools only | Changes made through Bash commands are not tracked                                                                                                                               |
| Subagent edits                     | Edits a [subagent](/docs/en/agent-sdk/subagents) applies aren't tracked or restored, except a skill with `context: fork` running in the foreground; use git to revert untracked edits |
| Same session                       | Checkpoints are tied to the session that created them                                                                                                                            |
| File content only                  | Creating, moving, or deleting directories is not undone by rewinding                                                                                                             |
| Local files                        | Remote or network files are not tracked                                                                                                                                          |

## Troubleshooting

### Checkpointing options not recognized

If `enableFileCheckpointing` or `rewindFiles()` isn't available, you may be on an older SDK version.

**Solution**: Update to the latest SDK version:

* **Python**: `pip install --upgrade claude-agent-sdk`
* **TypeScript**: `npm install @anthropic-ai/claude-agent-sdk@latest`

### User messages don't have UUIDs

If `message.uuid` is `undefined` or missing, you're not receiving checkpoint UUIDs.

**Cause**: The `replay-user-messages` option isn't set.

**Solution**: Add `extra_args={"replay-user-messages": None}` (Python) or `extraArgs: { 'replay-user-messages': null }` (TypeScript) to your options.

### "No file checkpoint found for this message" error

This error occurs when the checkpoint data doesn't exist for the specified user message UUID.

**Common causes**:

* File checkpointing was not enabled on the original session (`enable_file_checkpointing` or `enableFileCheckpointing` was not set to `true`)
* The session wasn't properly completed before attempting to resume and rewind

**Solution**: Ensure `enable_file_checkpointing=True` (Python) or `enableFileCheckpointing: true` (TypeScript) was set on the original session, then use the pattern shown in the examples: capture the first user message UUID, complete the session fully, then resume with an empty prompt and call `rewindFiles()` once.

### "File rewinding is not enabled" error

This error occurs when you attempt a non-interactive rewind without checkpointing enabled: running bare `claude -p` with `--rewind-files`, or running an SDK session, including a resumed one, whose options don't enable checkpointing. The SDK sets the `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING` environment variable internally only when `enable_file_checkpointing` (Python) or `enableFileCheckpointing` (TypeScript) is enabled on the session performing the rewind; the bare CLI never sets it.

**Solution**: For the bare CLI, set the environment variable when running the command:

```bash theme={null}
CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=true claude -p --resume <session-id> --rewind-files <checkpoint-uuid>
```

For the SDK, set `enable_file_checkpointing=True` (Python) or `enableFileCheckpointing: true` (TypeScript) on the resumed session, as the examples on this page do.

### "ProcessTransport is not ready for writing" error

This error occurs when you call `rewindFiles()` or `rewind_files()` after you've finished iterating through the response. The connection to the CLI process closes when the loop completes.

**Solution**: Resume the session with an empty prompt, then call rewind on the new query:

<CodeGroup>
  ```python Python theme={null}
  # Resume session with empty prompt, then rewind
  async with ClaudeSDKClient(
      ClaudeAgentOptions(enable_file_checkpointing=True, resume=session_id)
  ) as client:
      await client.query("")
      async for message in client.receive_response():
          if checkpoint_id:
              await client.rewind_files(checkpoint_id)
          break
  ```

  ```typescript TypeScript theme={null}
  // Resume session with empty prompt, then rewind
  const rewindQuery = query({
    prompt: "",
    options: { ...opts, resume: sessionId }
  });

  try {
    for await (const msg of rewindQuery) {
      if (checkpointId) {
        await rewindQuery.rewindFiles(checkpointId);
      }
      break;
    }
  } catch (error) {
    // An error here means the rewind didn't complete, for example the checkpoint
    // wasn't found or the session couldn't be resumed.
    console.error(`Rewind session ended with an error: ${error}`);
  }
  ```
</CodeGroup>

## Next steps

* **[Sessions](/docs/en/agent-sdk/sessions)**: learn how to resume sessions, which is required for rewinding after the stream completes. Covers session IDs, resuming conversations, and session forking.
* **[Permissions](/docs/en/agent-sdk/permissions)**: configure which tools Claude can use and how file modifications are approved. Useful if you want more control over when edits happen.
* **[TypeScript SDK reference](/docs/en/agent-sdk/typescript)**: complete API reference including all options for `query()` and the `rewindFiles()` method.
* **[Python SDK reference](/docs/en/agent-sdk/python)**: complete API reference including all options for `ClaudeAgentOptions` and the `rewind_files()` method.

---

## Intercept and control agent behavior with hooks

- 官方原文：https://code.claude.com/docs/en/agent-sdk/hooks.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-hooks.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Intercept and control agent behavior with hooks

> Intercept and customize agent behavior at key execution points with hooks

Hooks are callback functions that run your code in response to agent events, like a tool being called, a session starting, or execution stopping. With hooks, you can:

* **Block dangerous operations** before they execute, like destructive shell commands or unauthorized file access
* **Log and audit** every tool call for compliance, debugging, or analytics
* **Transform inputs and outputs** to sanitize data, inject credentials, or redirect file paths
* **Require human approval** for sensitive actions like database writes or API calls
* **Track session lifecycle** to manage state, clean up resources, or send notifications

## How hooks work

    Something happens during agent execution and the SDK fires an event: a tool is about to be called (`PreToolUse`), a tool returned a result (`PostToolUse`), a subagent started or stopped, the agent is idle, or execution finished. See the [full list of events](#available-hooks).

    The SDK checks for hooks registered for that event type. This includes callback hooks you pass in `options.hooks` and shell command hooks from settings files when the corresponding [`settingSources`](/docs/en/agent-sdk/typescript#settingsource) or [`setting_sources`](/docs/en/agent-sdk/python#settingsource) entry is enabled, which it is for default `query()` options.

    If a hook has a [`matcher`](#matchers) pattern (like `"Write|Edit"`), the SDK tests it against the event's target (for example, the tool name). Hooks without a matcher run for every event of that type.

    Each matching hook's [callback function](#callback-functions) receives input about what's happening: the tool name, its arguments, the session ID, and other event-specific details.

    After performing any operations (logging, API calls, validation), your callback returns an [output object](#outputs) that tells the agent what to do: allow the operation, block it, modify the input, or inject context into the conversation.

The following example puts these steps together. It registers a `PreToolUse` hook (step 1) with a `"Write|Edit"` matcher (step 3) so the callback only fires for file-writing tools. When triggered, the callback receives the tool's input (step 4), checks if the file path targets a `.env` file, and returns `permissionDecision: "deny"` to block the operation (step 5):

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import (
      AssistantMessage,
      ClaudeSDKClient,
      ClaudeAgentOptions,
      HookMatcher,
      ResultMessage,
  )

  # Define a hook callback that receives tool call details
  async def protect_env_files(input_data, tool_use_id, context):
      # Extract the file path from the tool's input arguments
      file_path = input_data["tool_input"].get("file_path", "")
      file_name = file_path.split("/")[-1]

      # Block the operation if targeting a .env file
      if file_name == ".env":
          return {
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "deny",
                  "permissionDecisionReason": "Cannot modify .env files",
              }
          }

      # Return empty object to allow the operation
      return {}

  async def main():
      options = ClaudeAgentOptions(
          hooks={
              # Register the hook for PreToolUse events
              # The matcher filters to only Write and Edit tool calls
              "PreToolUse": [HookMatcher(matcher="Write|Edit", hooks=[protect_env_files])]
          }
      )

      async with ClaudeSDKClient(options=options) as client:
          await client.query("Create a .env file with the standard local development database configuration")
          async for message in client.receive_response():
              # Filter for assistant and result messages
              if isinstance(message, (AssistantMessage, ResultMessage)):
                  print(message)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Define a hook callback with the HookCallback type
  const protectEnvFiles: HookCallback = async (input, toolUseID, { signal }) => {
    // Cast input to the specific hook type for type safety
    const preInput = input as PreToolUseHookInput;

    // Cast tool_input to access its properties (typed as unknown in the SDK)
    const toolInput = preInput.tool_input as Record<string, unknown>;
    const filePath = toolInput?.file_path as string;
    const fileName = filePath?.split("/").pop();

    // Block the operation if targeting a .env file
    if (fileName === ".env") {
      return {
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "deny",
          permissionDecisionReason: "Cannot modify .env files"
        }
      };
    }

    // Return empty object to allow the operation
    return {};
  };

  for await (const message of query({
    prompt: "Create a .env file with the standard local development database configuration",
    options: {
      hooks: {
        // Register the hook for PreToolUse events
        // The matcher filters to only Write and Edit tool calls
        PreToolUse: [{ matcher: "Write|Edit", hooks: [protectEnvFiles] }]
      }
    }
  })) {
    // Filter for assistant and result messages
    if (message.type === "assistant" || message.type === "result") {
      console.log(message);
    }
  }
  ```
</CodeGroup>

When you run either script, Claude attempts to create the `.env` file, the hook denies the tool call, and Claude's final response explains that it can't create `.env` files.

## Available hooks

The SDK provides hooks for different stages of agent execution. Some hooks are available in both SDKs, while others are TypeScript-only.

| Hook Event                                             | Python SDK | TypeScript SDK | What triggers it                                                                                                                        | Example use case                                                                                                                                          |
| ------------------------------------------------------ | ---------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PreToolUse`                                           | Yes        | Yes            | Tool call request (can block or modify)                                                                                                 | Block dangerous shell commands                                                                                                                            |
| `PostToolUse`                                          | Yes        | Yes            | Tool execution result                                                                                                                   | Log all file changes to audit trail                                                                                                                       |
| `PostToolUseFailure`                                   | Yes        | Yes            | Tool execution failure                                                                                                                  | Handle or log tool errors                                                                                                                                 |
| `PostToolBatch`                                        | No         | Yes            | A full batch of tool calls resolves, once per batch before the next model call                                                          | Inject conventions once for the whole batch                                                                                                               |
| `UserPromptSubmit`                                     | Yes        | Yes            | User prompt submission                                                                                                                  | Inject additional context into prompts                                                                                                                    |
| [`UserPromptExpansion`](/docs/en/hooks#userpromptexpansion) | No         | Yes            | A user-typed command, or an MCP prompt, expands into a prompt before it reaches Claude. Doesn't fire when Claude invokes a skill itself | Block a command from direct invocation or add context when a skill is typed                                                                               |
| `MessageDisplay`                                       | No         | Yes            | An assistant message with text completes, once per message with the full message text                                                   | Redact or reformat the displayed text without changing the transcript                                                                                     |
| `Stop`                                                 | Yes        | Yes            | Agent execution stop                                                                                                                    | Save session state before exit                                                                                                                            |
| `StopFailure`                                          | No         | Yes            | The turn ends with an API error instead of a normal stop                                                                                | Log failures or send alerts                                                                                                                               |
| `SubagentStart`                                        | Yes        | Yes            | Subagent initialization                                                                                                                 | Track parallel task spawning                                                                                                                              |
| `SubagentStop`                                         | Yes        | Yes            | Subagent completion                                                                                                                     | Aggregate results from parallel tasks                                                                                                                     |
| `PreCompact`                                           | Yes        | Yes            | Conversation compaction request                                                                                                         | Archive full transcript before summarizing                                                                                                                |
| `PostCompact`                                          | No         | Yes            | Conversation compaction completes                                                                                                       | Log the generated summary                                                                                                                                 |
| [`PreModelSwitch`](/docs/en/hooks#premodelswitch)           | No         | Yes            | A requested model switch, before it happens (can block)                                                                                 | Block switching to a specific model                                                                                                                       |
| [`PostModelSwitch`](/docs/en/hooks#postmodelswitch)         | No         | Yes            | The session's model changes, including an automatic fallback                                                                            | Give Claude model-specific guidance for the new model                                                                                                     |
| `PermissionRequest`                                    | Yes        | Yes            | A tool call needs a permission decision                                                                                                 | Custom permission handling                                                                                                                                |
| `PermissionDenied`                                     | No         | Yes            | Auto mode denies a tool call, including denials without a classifier verdict                                                            | Log denials, or tell the model it may retry; Claude Code ignores `retry: true` for no-verdict denials. See [PermissionDenied](/docs/en/hooks#permissiondenied) |
| `SessionStart`                                         | No         | Yes            | Session initialization                                                                                                                  | Initialize logging and telemetry                                                                                                                          |
| `SessionEnd`                                           | No         | Yes            | Session termination                                                                                                                     | Clean up temporary resources                                                                                                                              |
| `Notification`                                         | Yes        | Yes            | Agent status messages                                                                                                                   | Send agent status updates to Slack or PagerDuty                                                                                                           |
| `Setup`                                                | No         | Yes            | Session setup/maintenance                                                                                                               | Run initialization tasks                                                                                                                                  |
| `TeammateIdle`                                         | No         | Yes            | Teammate becomes idle                                                                                                                   | Reassign work or notify                                                                                                                                   |
| `TaskCreated`                                          | No         | Yes            | A task is created via the `TaskCreate` tool                                                                                             | Enforce task naming conventions                                                                                                                           |
| [`TaskCompleted`](/docs/en/hooks#taskcompleted)             | No         | Yes            | A task is marked completed                                                                                                              | Require passing tests before a task closes                                                                                                                |
| `Elicitation`                                          | No         | Yes            | An MCP server requests user input mid-task                                                                                              | Respond to MCP input requests programmatically                                                                                                            |
| `ElicitationResult`                                    | No         | Yes            | A user responds to an MCP elicitation                                                                                                   | Modify or block the response before it returns to the server                                                                                              |
| `ConfigChange`                                         | No         | Yes            | Configuration file changes                                                                                                              | Reload settings dynamically                                                                                                                               |
| `InstructionsLoaded`                                   | No         | Yes            | A `CLAUDE.md` or rules file is loaded into context                                                                                      | Audit which instruction files load                                                                                                                        |
| `WorktreeCreate`                                       | No         | Yes            | Git worktree created                                                                                                                    | Track isolated workspaces                                                                                                                                 |
| `WorktreeRemove`                                       | No         | Yes            | Git worktree removed                                                                                                                    | Clean up workspace resources                                                                                                                              |
| `CwdChanged`                                           | No         | Yes            | The working directory changes during a session                                                                                          | Reload environment variables per directory                                                                                                                |
| `FileChanged`                                          | No         | Yes            | A watched file is modified, created, or deleted                                                                                         | Reload configuration when project files change                                                                                                            |
| `DirectoryAdded`                                       | No         | Yes            | A working directory is added during a session                                                                                           | Install dependencies for a repository added mid-session                                                                                                   |

## Configure hooks

To configure a hook, pass it in the `hooks` field of your agent options (`ClaudeAgentOptions` in Python, the `options` object in TypeScript). This snippet assumes you have already defined a hook callback, like `protect_env_files` in Python or `protectEnvFiles` in TypeScript from the example above:

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      hooks={"PreToolUse": [HookMatcher(matcher="Bash", hooks=[my_callback])]}
  )

  async with ClaudeSDKClient(options=options) as client:
      await client.query("Your prompt")
      async for message in client.receive_response():
          print(message)
  ```

  ```typescript TypeScript theme={null}
  for await (const message of query({
    prompt: "Your prompt",
    options: {
      hooks: {
        PreToolUse: [{ matcher: "Bash", hooks: [myCallback] }]
      }
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

The `hooks` option is a dictionary in Python or an object in TypeScript, where:

* **Keys**: [hook event names](#available-hooks) such as `'PreToolUse'`, `'PostToolUse'`, and `'Stop'`
* **Values**: arrays of [matchers](#matchers), each containing an optional filter pattern and your [callback functions](#callback-functions)

### Matchers

Use matchers to filter when your callbacks fire. The `matcher` field matches against a different value depending on the hook event type. For example, tool-based hooks match against the tool name, while `Notification` hooks match against the notification type.

SDK matchers follow the same rules as [matchers in settings files](/docs/en/hooks#matcher-patterns). That section documents the exact-string and regular-expression evaluation paths, their version requirements, and the matcher values for each event type.

| Option    | Type             | Default     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | ---------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `matcher` | `string`         | `undefined` | Pattern matched against the event's filter field, following the [rules for matchers in settings files](/docs/en/hooks#matcher-patterns). For tool hooks, this is the tool name. Built-in tools include `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebFetch`, `Agent`, and others (see [Tool Input Types](/docs/en/agent-sdk/typescript#tool-input-types) for the full list). MCP tools use the pattern `mcp__<server>__<action>`, where `<server>` is the key you use in the `mcpServers` configuration. |
| `hooks`   | `HookCallback[]` | -           | Required. Array of callback functions to execute when the pattern matches                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `timeout` | `number`         | `undefined` | Timeout in seconds. When omitted, Claude Code applies the [event's default timeout](#hook-timeout). Your SDK callbacks follow the `command` hook defaults                                                                                                                                                                                                                                                                                                                                             |

Use the `matcher` pattern to target specific tools whenever possible. A matcher with `'Bash'` only runs for Bash commands, while omitting the pattern runs your callbacks for every occurrence of the event. Omit it on purpose to log every tool call your session makes.

### Callback functions

#### Inputs

Every hook callback receives three arguments:

* **Input data:** a typed object containing event details. Each hook type has its own input shape. For example, `PreToolUseHookInput` includes `tool_name` and `tool_input`, while `NotificationHookInput` includes `message`. See the full type definitions in the [TypeScript](/docs/en/agent-sdk/typescript#hookinput) and [Python](/docs/en/agent-sdk/python#hookinput) SDK references.
  * All hook inputs share `session_id`, `cwd`, and `hook_event_name`.
  * `agent_id` and `agent_type` are populated when the hook fires inside a subagent. In TypeScript, these are on the base hook input and available to all hook types. In Python, they are optional fields on `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, and `PermissionRequest`, and required fields on `SubagentStart` and `SubagentStop`.
* **Tool use ID** (`str | None` / `string | undefined`): correlates `PreToolUse` and `PostToolUse` events for the same tool call.
* **Context:** in TypeScript, contains a `signal` property (`AbortSignal`) for cancellation. In Python, this argument is reserved for future use.

#### Outputs

Your callback returns an object with two categories of fields:

* **Top-level fields** are accepted on every event: `systemMessage` shows a message to the user, and `continue` (`continue_` in Python) determines whether the agent keeps running after this hook. Some events discard them or deliver them elsewhere. Each [event's section](/docs/en/hooks#hook-events) on the hooks page says where they land.
* **`hookSpecificOutput`** controls the current operation. The fields you set inside depend on the hook event type:
  * For `PreToolUse` hooks, this is where you set `permissionDecision` (`"allow"`, `"deny"`, `"ask"`, or `"defer"`), `permissionDecisionReason`, and `updatedInput`. If you return `"defer"`, the query ends so you can [resume it later](/docs/en/hooks#defer-a-tool-call-for-later).
  * For `PostToolUse` hooks, you can set `additionalContext` to append information to the tool result. To replace the tool's output before Claude sees it, set `updatedToolOutput`, which works for any tool in both SDKs. The older `updatedMCPToolOutput` field replaces MCP tool output only and is deprecated.
  * In the TypeScript SDK, a `PostToolUse` callback can also return `classifierContext`, a short note about the tool call's result for the [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) permission classifier. Because your callback runs in your application's own process, the classifier may weigh a user statement you relay in the note as user intent. The field requires TypeScript Agent SDK v0.3.236 or later. [Annotate a result for the auto mode classifier](/docs/en/hooks#annotate-a-result-for-the-auto-mode-classifier) covers the length cap, the synchronous-only rule, and what not to put in the note.

Return `{}` to allow the operation without changes. SDK callback hooks use the same JSON output format as [Claude Code shell command hooks](/docs/en/hooks#json-output), which documents every field and event-specific option. For the SDK type definitions, see the [TypeScript](/docs/en/agent-sdk/typescript#synchookjsonoutput) and [Python](/docs/en/agent-sdk/python#synchookjsonoutput) SDK references.

<Note>
  When multiple hooks or permission rules apply, `deny` takes priority over `defer`, which takes priority over `ask`, which takes priority over `allow`. If any hook returns `deny`, the operation is blocked regardless of other hooks.
</Note>

#### Asynchronous output

By default, the agent waits for your hook to return before proceeding. If your hook performs a side effect, such as logging or sending a webhook, and doesn't need to influence the agent's behavior, you can return an async output instead. This tells the agent to continue immediately without waiting for the hook to finish. In this snippet, `send_to_logging_service` in Python and `sendToLoggingService` in TypeScript stand in for any logging function you define:

<CodeGroup>
  ```python Python theme={null}
  async def async_hook(input_data, tool_use_id, context):
      # Start a background task, then return immediately
      asyncio.create_task(send_to_logging_service(input_data))
      return {"async_": True, "asyncTimeout": 30000}
  ```

  ```typescript TypeScript theme={null}
  const asyncHook: HookCallback = async (input, toolUseID, { signal }) => {
    // Start a background task, then return immediately
    sendToLoggingService(input).catch(console.error);
    return { async: true, asyncTimeout: 30000 };
  };
  ```
</CodeGroup>

| Field          | Type     | Description                                                                                                    |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| `async`        | `true`   | Signals async mode. The agent proceeds without waiting. In Python, use `async_` to avoid the reserved keyword. |
| `asyncTimeout` | `number` | Optional timeout in milliseconds for the background operation                                                  |

<Note>
  Async outputs can't block, modify, or inject context into the operation since the agent has already moved on. Use them only for side effects like logging, metrics, or notifications.
</Note>

## Examples

Several examples in this section show only the callback function. To run one, register the callback under the matching event in the `hooks` field of your options, as shown in [Configure hooks](#configure-hooks).

### Modify tool input

This example intercepts Write tool calls and rewrites the `file_path` argument to prepend `/sandbox`, redirecting all file writes to a sandboxed directory. The callback returns `updatedInput` with the modified path and `permissionDecision: 'allow'` to auto-approve the rewritten operation:

<CodeGroup>
  ```python Python theme={null}
  async def redirect_to_sandbox(input_data, tool_use_id, context):
      if input_data["hook_event_name"] != "PreToolUse":
          return {}

      if input_data["tool_name"] == "Write":
          original_path = input_data["tool_input"].get("file_path", "")
          return {
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "allow",
                  "updatedInput": {
                      **input_data["tool_input"],
                      "file_path": f"/sandbox{original_path}",
                  },
              }
          }
      return {}
  ```

  ```typescript TypeScript theme={null}
  const redirectToSandbox: HookCallback = async (input, toolUseID, { signal }) => {
    if (input.hook_event_name !== "PreToolUse") return {};

    const preInput = input as PreToolUseHookInput;
    const toolInput = preInput.tool_input as Record<string, unknown>;
    if (preInput.tool_name === "Write") {
      const originalPath = toolInput.file_path as string;
      return {
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "allow",
          updatedInput: {
            ...toolInput,
            file_path: `/sandbox${originalPath}`
          }
        }
      };
    }
    return {};
  };
  ```
</CodeGroup>

<Note>
  Pair `updatedInput` with `permissionDecision: 'allow'` to auto-approve the modified input, or `permissionDecision: 'ask'` to show it to the user. If you omit `permissionDecision`, the modified input still applies and flows through the normal permission evaluation. With `'defer'`, `updatedInput` is ignored. Always return a new object rather than mutating the original `tool_input`.
</Note>

To confirm the redirect, set the prefix to a path you can write to, such as `./sandbox` or `/tmp/sandbox` (macOS doesn't allow creating a root-level `/sandbox` directory), then ask the agent to write a file: the Write tool's result in the message stream names the path with your sandbox prefix rather than the one Claude requested.

### Add context and block a tool

This example blocks writes to the `/etc` directory and explains why to both the model and the user:

* `permissionDecision: 'deny'` stops the tool call.
* `permissionDecisionReason` tells the model why, so it avoids retrying.
* `systemMessage` shows the user what happened.

<CodeGroup>
  ```python Python theme={null}
  async def block_etc_writes(input_data, tool_use_id, context):
      file_path = input_data["tool_input"].get("file_path", "")

      if file_path.startswith("/etc"):
          return {
              # Top-level field: message shown to the user
              "systemMessage": "Remember: system directories like /etc are protected.",
              # hookSpecificOutput: block the operation
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "deny",
                  "permissionDecisionReason": "Writing to /etc is not allowed",
              },
          }
      return {}
  ```

  ```typescript TypeScript theme={null}
  const blockEtcWrites: HookCallback = async (input, toolUseID, { signal }) => {
    const preInput = input as PreToolUseHookInput;
    const toolInput = preInput.tool_input as Record<string, unknown>;
    const filePath = toolInput?.file_path as string;

    if (filePath?.startsWith("/etc")) {
      return {
        // Top-level field: message shown to the user
        systemMessage: "Remember: system directories like /etc are protected.",
        // hookSpecificOutput: block the operation
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "deny",
          permissionDecisionReason: "Writing to /etc is not allowed"
        }
      };
    }
    return {};
  };
  ```
</CodeGroup>

### Auto-approve specific tools

By default, the agent may prompt for permission before using certain tools. This example auto-approves read-only filesystem tools (Read, Glob, Grep) by returning `permissionDecision: 'allow'`, letting them run without user confirmation while leaving all other tools subject to normal permission checks:

<CodeGroup>
  ```python Python theme={null}
  async def auto_approve_read_only(input_data, tool_use_id, context):
      if input_data["hook_event_name"] != "PreToolUse":
          return {}

      read_only_tools = ["Read", "Glob", "Grep"]
      if input_data["tool_name"] in read_only_tools:
          return {
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "allow",
                  "permissionDecisionReason": "Read-only tool auto-approved",
              }
          }
      return {}
  ```

  ```typescript TypeScript theme={null}
  const autoApproveReadOnly: HookCallback = async (input, toolUseID, { signal }) => {
    if (input.hook_event_name !== "PreToolUse") return {};

    const preInput = input as PreToolUseHookInput;
    const readOnlyTools = ["Read", "Glob", "Grep"];
    if (readOnlyTools.includes(preInput.tool_name)) {
      return {
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "allow",
          permissionDecisionReason: "Read-only tool auto-approved"
        }
      };
    }
    return {};
  };
  ```
</CodeGroup>

### Register multiple hooks

When an event fires, all matching hooks run in parallel. For permission decisions, the most restrictive result applies: a single `deny` blocks the tool call regardless of what the other hooks return. Because completion order is non-deterministic, write each hook to act independently rather than relying on another hook having run first.

The example below registers three independent checks for every tool call:

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      hooks={
          "PreToolUse": [
              HookMatcher(hooks=[authorization_check]),
              HookMatcher(hooks=[input_validator]),
              HookMatcher(hooks=[audit_logger]),
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    hooks: {
      PreToolUse: [
        { hooks: [authorizationCheck] },
        { hooks: [inputValidator] },
        { hooks: [auditLogger] }
      ]
    }
  };
  ```
</CodeGroup>

### Filter with multi-tool matchers

Use multi-tool matchers to share one callback across related tools. This example registers three matchers with different scopes:

* A pipe-separated exact list (`Write|Edit|NotebookEdit`) triggers `file_security_hook` only for file modification tools.
* A regex (`^mcp__`) triggers `mcp_audit_hook` for any MCP tool whose name starts with `mcp__`.
* An omitted matcher triggers `global_logger` for every tool call regardless of name.

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      hooks={
          "PreToolUse": [
              # Match file modification tools
              HookMatcher(matcher="Write|Edit|NotebookEdit", hooks=[file_security_hook]),
              # Match all MCP tools
              HookMatcher(matcher="^mcp__", hooks=[mcp_audit_hook]),
              # Match everything (no matcher)
              HookMatcher(hooks=[global_logger]),
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    hooks: {
      PreToolUse: [
        // Match file modification tools
        { matcher: "Write|Edit|NotebookEdit", hooks: [fileSecurityHook] },

        // Match all MCP tools
        { matcher: "^mcp__", hooks: [mcpAuditHook] },

        // Match everything (no matcher)
        { hooks: [globalLogger] }
      ]
    }
  };
  ```
</CodeGroup>

### Track subagent activity

Use `SubagentStop` hooks to monitor when subagents finish their work. See the full input type in the [TypeScript](/docs/en/agent-sdk/typescript#hookinput) and [Python](/docs/en/agent-sdk/python#hookinput) SDK references. This example logs a summary each time a subagent completes:

<CodeGroup>
  ```python Python theme={null}
  async def subagent_tracker(input_data, tool_use_id, context):
      # Log subagent details when it finishes
      print(f"[SUBAGENT] Completed: {input_data['agent_id']}")
      print(f"  Transcript: {input_data['agent_transcript_path']}")
      print(f"  Tool use ID: {tool_use_id}")
      print(f"  Stop hook active: {input_data.get('stop_hook_active')}")
      return {}

  options = ClaudeAgentOptions(
      hooks={"SubagentStop": [HookMatcher(hooks=[subagent_tracker])]}
  )
  ```

  ```typescript TypeScript theme={null}

  const subagentTracker: HookCallback = async (input, toolUseID, { signal }) => {
    // Cast to SubagentStopHookInput to access subagent-specific fields
    const subInput = input as SubagentStopHookInput;

    // Log subagent details when it finishes
    console.log(`[SUBAGENT] Completed: ${subInput.agent_id}`);
    console.log(`  Transcript: ${subInput.agent_transcript_path}`);
    console.log(`  Tool use ID: ${toolUseID}`);
    console.log(`  Stop hook active: ${subInput.stop_hook_active}`);
    return {};
  };

  const options = {
    hooks: {
      SubagentStop: [{ hooks: [subagentTracker] }]
    }
  };
  ```
</CodeGroup>

### Make HTTP requests from hooks

Hooks can perform asynchronous operations like HTTP requests. Catch errors inside your hook instead of letting them propagate.

This example sends a webhook after each tool completes, logging which tool ran and when. The hook catches errors from a failed webhook:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  import urllib.request
  from datetime import datetime

  def _send_webhook(tool_name):
      """Synchronous helper that POSTs tool usage data to an external webhook."""
      data = json.dumps(
          {
              "tool": tool_name,
              "timestamp": datetime.now().isoformat(),
          }
      ).encode()
      req = urllib.request.Request(
          "https://api.example.com/webhook",
          data=data,
          headers={"Content-Type": "application/json"},
          method="POST",
      )
      urllib.request.urlopen(req)

  async def webhook_notifier(input_data, tool_use_id, context):
      # Only fire after a tool completes (PostToolUse), not before
      if input_data["hook_event_name"] != "PostToolUse":
          return {}

      try:
          # Run the blocking HTTP call in a thread to avoid blocking the event loop
          await asyncio.to_thread(_send_webhook, input_data["tool_name"])
      except Exception as e:
          # Log the error but don't raise
          print(f"Webhook request failed: {e}")

      return {}
  ```

  ```typescript TypeScript theme={null}

  const webhookNotifier: HookCallback = async (input, toolUseID, { signal }) => {
    // Only fire after a tool completes (PostToolUse), not before
    if (input.hook_event_name !== "PostToolUse") return {};

    try {
      await fetch("https://api.example.com/webhook", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          tool: (input as PostToolUseHookInput).tool_name,
          timestamp: new Date().toISOString()
        }),
        // Pass signal so the request cancels if the hook times out
        signal
      });
    } catch (error) {
      // Handle cancellation separately from other errors
      if (error instanceof Error && error.name === "AbortError") {
        console.log("Webhook request cancelled");
      }
      // Don't re-throw
    }

    return {};
  };

  // Register as a PostToolUse hook
  for await (const message of query({
    prompt: "Refactor the auth module",
    options: {
      hooks: {
        PostToolUse: [{ hooks: [webhookNotifier] }]
      }
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

To confirm the hook fires, point the webhook URL at an endpoint you can watch and send a prompt that uses a tool: the hook sends a POST with the tool name and timestamp after each tool completes.

### Forward notifications to Slack

Use `Notification` hooks to receive system notifications from the agent and forward them to external services. In SDK sessions, Claude Code runs this hook for the following notification types:

* [`permission_prompt`](/docs/en/hooks#notification) once a permission request has waited about six seconds on your [`canUseTool` callback](/docs/en/agent-sdk/user-input). Requires TypeScript Agent SDK v0.3.233 or later, or Python Agent SDK v0.2.139 or later
* `elicitation_complete` and `elicitation_response` for user-prompt elicitation flows

Claude Code emits the other types, such as `idle_prompt`, `auth_success`, and `elicitation_dialog`, from interactive UI that SDK sessions don't run.

Each notification includes a `message` field with a human-readable description and optionally a `title`.

This example forwards every notification to a Slack channel. It requires a [Slack incoming webhook URL](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/), which you create by adding an app to your Slack workspace and enabling incoming webhooks:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  import urllib.request

  from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher

  def _send_slack_notification(message):
      """Synchronous helper that sends a message to Slack via incoming webhook."""
      data = json.dumps({"text": f"Agent status: {message}"}).encode()
      req = urllib.request.Request(
          "https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
          data=data,
          headers={"Content-Type": "application/json"},
          method="POST",
      )
      urllib.request.urlopen(req)

  async def notification_handler(input_data, tool_use_id, context):
      try:
          # Run the blocking HTTP call in a thread to avoid blocking the event loop
          await asyncio.to_thread(_send_slack_notification, input_data.get("message", ""))
      except Exception as e:
          print(f"Failed to send notification: {e}")

      # Return empty object. Notification hooks don't modify agent behavior
      return {}

  async def main():
      options = ClaudeAgentOptions(
          hooks={
              # Register the hook for Notification events (no matcher needed)
              "Notification": [HookMatcher(hooks=[notification_handler])],
          },
      )

      async with ClaudeSDKClient(options=options) as client:
          await client.query("Analyze this codebase")
          async for message in client.receive_response():
              print(message)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Define a hook callback that sends notifications to Slack
  const notificationHandler: HookCallback = async (input, toolUseID, { signal }) => {
    // Cast to NotificationHookInput to access the message field
    const notification = input as NotificationHookInput;

    try {
      // POST the notification message to a Slack incoming webhook
      await fetch("https://hooks.slack.com/services/YOUR/WEBHOOK/URL", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: `Agent status: ${notification.message}`
        }),
        // Pass signal so the request cancels if the hook times out
        signal
      });
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") {
        console.log("Notification cancelled");
      } else {
        console.error("Failed to send notification:", error);
      }
    }

    // Return empty object. Notification hooks don't modify agent behavior
    return {};
  };

  // Register the hook for Notification events (no matcher needed)
  for await (const message of query({
    prompt: "Analyze this codebase",
    options: {
      hooks: {
        Notification: [{ hooks: [notificationHandler] }]
      }
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

When a `Notification` event fires, the hook posts the notification's `message`, prefixed with `Agent status:`, to the channel your webhook targets.

## Fix common issues

### Hook not firing

* Verify the hook event name is correct and case-sensitive (`PreToolUse`, not `preToolUse`)
* Check that your matcher pattern matches the tool name exactly
* Ensure the hook is under the correct event type in `options.hooks`
* For non-tool hooks that support matchers, like `Notification` and `SubagentStop`, matchers match against different fields, and `Stop` ignores matchers entirely (see [matcher patterns](/docs/en/hooks#matcher-patterns))
* Hooks may not fire when the agent hits the [`max_turns`](/docs/en/agent-sdk/python#claudeagentoptions) limit because the session ends before hooks can execute

### Matcher not filtering as expected

Matchers only match tool names, not file paths or other arguments. To filter by file path, check `tool_input.file_path` inside your hook:

```typescript theme={null}
const myHook: HookCallback = async (input, toolUseID, { signal }) => {
  const preInput = input as PreToolUseHookInput;
  const toolInput = preInput.tool_input as Record<string, unknown>;
  const filePath = toolInput?.file_path as string;
  if (!filePath?.endsWith(".md")) return {}; // Skip non-markdown files
  // Process markdown files...
  return {};
};
```

### Hook timeout

Claude Code runs each callback with a timeout, which you set in seconds with the `timeout` field on its `HookMatcher`. When you don't set one, Claude Code uses the event's default: 600 seconds for most events, 30 seconds for `UserPromptSubmit`, `PreModelSwitch`, and `PostModelSwitch`, and 10 seconds for `MessageDisplay`. Claude Code runs `SessionEnd` callbacks during shutdown under the shorter [SessionEnd timeout budget](/docs/en/hooks#sessionend-input), 1.5 seconds by default.

When a callback exceeds its timeout, Claude Code cancels it and discards its output, and the session continues rather than hanging. What happens next depends on the event:

* `PreToolUse`: Claude Code doesn't run the tool call, Claude receives a tool result stating the hook didn't respond before its timeout, and the turn continues. If another `PreToolUse` hook returned an explicit deny, Claude receives that denial instead of the timeout error. Before v2.1.210, Claude Code reported the timeout to Claude as a user rejection, which made unattended sessions stop and wait for input.
* `PostToolUse` and `PostToolUseFailure`: Claude Code keeps the tool result and the turn continues.
* `UserPromptSubmit` and [`UserPromptExpansion`](/docs/en/hooks#userpromptexpansion): Claude Code blocks the prompt with a message naming the hook and the timeout, and the session continues. Because a callback on these events can act as a policy gate, Claude Code never lets a timed-out prompt through unscreened. Before v2.1.208, Claude Code ended the query with `error_during_execution` when a callback on these events timed out.
* `Stop` and `SubagentStop`: the timed-out callback counts as returning no decision. The agent or subagent stops as if that callback had allowed it, and a decision from your other hooks on the event still applies. Before Claude Code v2.1.273, a timed-out `Stop` or `SubagentStop` callback counted as a failed hook run, and Claude Code discarded the decisions of your other hooks on the event.
* `SessionStart`: the timed-out callback counts as returning no output, and the session continues with the output of your other `SessionStart` hooks.
* `PreModelSwitch`: Claude Code blocks the model switch. A hook that doesn't answer hasn't approved the switch.
* Other events, such as `Notification`, `PreCompact`, and `PostModelSwitch`: Claude Code logs the failure and continues.

The first time a `Stop` or `SessionStart` callback times out in the main session, Claude Code also adds an [`SDKInformationalMessage`](/docs/en/agent-sdk/typescript#sdkinformationalmessage) to the message stream saying the app driving the session didn't respond. Later timeouts don't repeat that message while your app stays unresponsive.

If you interrupt the query while a callback is pending, Claude Code cancels the pending tool call. Before v2.1.208, the tool call could still proceed if you interrupted during a pending `PreToolUse` callback.

If your callback needs more time, set a higher `timeout` on its `HookMatcher`. In TypeScript, use the `AbortSignal` from the third callback argument to handle cancellation gracefully when the timeout fires.

### Tool blocked unexpectedly

* Check all `PreToolUse` hooks for `permissionDecision: 'deny'` returns
* Add logging to your hooks to see what `permissionDecisionReason` they're returning
* Verify matcher patterns aren't too broad: an empty matcher matches all tools

### Modified input not applied

* Ensure `updatedInput` is inside `hookSpecificOutput`, not at the top level:

  ```typescript theme={null}
  return {
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "allow",
      updatedInput: { command: "new command" }
    }
  };
  ```

* Don't pair `updatedInput` with `permissionDecision: 'defer'`, which drops the modified input. Omitting `permissionDecision` is fine: the modified input still applies through the normal permission evaluation. You can also return `'allow'` to auto-approve the modified input or `'ask'` to show it to the user for approval

* Include `hookEventName` in `hookSpecificOutput` to identify which hook type the output is for

### Session hooks not available in Python

`SessionStart` and `SessionEnd` can be registered as SDK callback hooks in TypeScript, but aren't available in the Python SDK because its `HookEvent` type omits them. In Python, they are only available as [shell command hooks](/docs/en/hooks#hook-events) defined in settings files such as `.claude/settings.json`. To load shell command hooks from your SDK application, include the appropriate setting source with [`setting_sources`](/docs/en/agent-sdk/python#settingsource) or [`settingSources`](/docs/en/agent-sdk/typescript#settingsource):

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      setting_sources=["project"],  # Loads .claude/settings.json including hooks
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    settingSources: ["project"] // Loads .claude/settings.json including hooks
  };
  ```
</CodeGroup>

To run initialization logic as a Python SDK callback instead, use the first message from `client.receive_response()` as your trigger.

### Subagent permission prompts multiplying

When spawning multiple subagents, each one may request permissions separately for its own tool calls. To avoid repeated prompts, use `PreToolUse` hooks to auto-approve specific tools, or configure permission rules, which subagents [inherit from the parent conversation](/docs/en/sub-agents#permission-modes).

### Recursive hook loops with subagents

A `UserPromptSubmit` hook that spawns subagents can create infinite loops if those subagents trigger the same hook. To prevent this:

* Use a shared variable or session state to track whether you're already inside a subagent
* Scope hooks to only run for the top-level agent session

### systemMessage not appearing in output

The `systemMessage` field shows a message to the user, not the model. On Claude Code v2.1.227 or later, a hook's `systemMessage` can surface in the message stream as an [`SDKInformationalMessage`](/docs/en/agent-sdk/typescript#sdkinformationalmessage). Whether it does depends on the event. Each [event's section](/docs/en/hooks#hook-events) on the hooks page says how output surfaces. To pass context to the model instead, return [`additionalContext`](/docs/en/hooks#add-context-for-claude).

Before v2.1.227, the SDK surfaced hook output in the message stream only for `SessionStart` and `Setup` hooks. For any other event, the output appeared only in the lifecycle events that [`includeHookEvents`](/docs/en/agent-sdk/typescript#options) (`include_hook_events` in Python) adds. That option's entry covers which lifecycle events each hook event produces.

If you need to surface hook decisions to your application reliably, log them separately or use a dedicated output channel.

## Related resources

* [Claude Code hooks reference](/docs/en/hooks): full JSON input/output schemas, event documentation, and matcher patterns
* [Claude Code hooks guide](/docs/en/hooks-guide): shell command hook examples and walkthroughs
* [TypeScript SDK reference](/docs/en/agent-sdk/typescript): hook types, input/output definitions, and configuration options
* [Python SDK reference](/docs/en/agent-sdk/python): hook types, input/output definitions, and configuration options
* [Permissions](/docs/en/agent-sdk/permissions): control what your agent can do
* [Custom tools](/docs/en/agent-sdk/custom-tools): build tools to extend agent capabilities

---

## Hosting the Agent SDK

- 官方原文：https://code.claude.com/docs/en/agent-sdk/hosting.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-hosting.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hosting the Agent SDK

> Deploy the Agent SDK in production: subprocess architecture, session persistence, scaling, observability, and multi-tenant isolation for Docker, Kubernetes, and sandbox providers.

The Agent SDK spawns and supervises a `claude` CLI subprocess that owns a shell, a working directory, and session files on disk. Hosting it is not like hosting a stateless API wrapper. Every running agent is a long-lived process tied to local state, which shapes how you allocate resources, persist sessions, and scale across tenants.

This page covers self-hosting on your own infrastructure. For deployable Dockerfiles and Kubernetes manifests, see the [hosting cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/claude_agent_sdk/hosting).

If you don't need to run the agent loop itself on your own infrastructure, consider [Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) instead. Anthropic hosts the agent loop, and your application sends events and receives streamed results through the client SDKs or the REST API. Tool execution runs in an Anthropic-managed cloud sandbox or a [self-hosted sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) on your own infrastructure.

## The subprocess model

Every hosting decision on this page follows from how the SDK runs the agent. When your code calls `query()`, the SDK spawns a separate `claude` CLI process and talks to it over stdio. That subprocess owns the shell, the working directory, and the JSONL session transcripts on local disk.

<img src="https://mintcdn.com/claude-code/ikqp3_70mqIahteV/images/agent-sdk/hosting-subprocess.svg?fit=max&auto=format&n=ikqp3_70mqIahteV&q=85&s=9dac857ca9d3b1410c3734900c386004" className="dark:hidden" alt="Request flow: client to your app, which spawns a claude CLI subprocess over stdio inside the container; the subprocess writes to local disk and calls api.anthropic.com over HTTPS" width="920" height="220" data-path="images/agent-sdk/hosting-subprocess.svg" />

<img src="https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agent-sdk/hosting-subprocess-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=3fdeff3d7f44b2b67762668acfbb25f5" className="hidden dark:block" alt="Request flow: client to your app, which spawns a claude CLI subprocess over stdio inside the container; the subprocess writes to local disk and calls api.anthropic.com over HTTPS" width="920" height="220" data-path="images/agent-sdk/hosting-subprocess-dark.svg" />

One agent session maps to one subprocess. Running N concurrent sessions means N subprocesses, each with its own process tree and transcript file. By default they all inherit your application's working directory. When sessions need separate filesystems, pass a distinct `cwd` in the options of each session's `query()` call:

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Summarize the files in this directory",
    options: { cwd: "/work/session-a" },
  })) {
    console.log(message);
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import ClaudeAgentOptions, query

  async def main():
      async for message in query(
          prompt="Summarize the files in this directory",
          options=ClaudeAgentOptions(cwd="/work/session-a"),
      ):
          print(message)

  asyncio.run(main())
  ```
</CodeGroup>

The TypeScript examples on this page use top-level `await`, so save them as `.mts` files or set `"type": "module"` in `package.json`.

### State that lives on local disk

Three kinds of agent state live on the container's filesystem by default. None of them survive a container restart, a scale-down, or a move to a different node.

| State                       | Default location                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| Session transcripts         | `~/.claude/projects/`, or the `projects/` directory under `CLAUDE_CONFIG_DIR` if set             |
| `CLAUDE.md` memory files    | `~/.claude/CLAUDE.md` for the user tier and the session's working directory for the project tier |
| Working-directory artifacts | The session's working directory                                                                  |

To persist transcripts across hosts, configure a [`SessionStore` adapter](/docs/en/agent-sdk/session-storage). Memory files and other working-directory artifacts need their own storage strategy, such as a mounted volume or an object-store sync.

For how sessions, resumption, and forking work at the API level, see [Sessions](/docs/en/agent-sdk/sessions).

## Choose a session pattern

These four patterns cover session lifecycle: how long a container lives relative to the sessions it serves. For where the container runs, the [hosting cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/07_Hosting_the_agent.ipynb) has [deployable code](https://github.com/anthropics/claude-cookbooks/tree/main/claude_agent_sdk/hosting) for local Docker, Modal, and Kubernetes. Choose a session pattern here and a deployment target from the cookbook.

### Ephemeral sessions

Create a container for each user task and destroy it when the task completes. Best for one-off tasks. The user may still interact with the AI while the task is completing, but once completed the container is destroyed.

Example workloads include bug investigation and fix, invoice and receipt extraction, document translation, and media transformation.

The container runs a one-shot entrypoint that reads the task from the `TASK_PROMPT` environment variable, calls the SDK, and exits.

<CodeGroup>
  ```typescript TypeScript theme={null}

  const prompt = process.env.TASK_PROMPT!;
  for await (const message of query({ prompt, options: { maxTurns: 20 } })) {
    console.log(message);
  }
  ```

  ```python Python theme={null}
  import asyncio
  import os

  from claude_agent_sdk import ClaudeAgentOptions, query

  async def main():
      async for message in query(
          prompt=os.environ["TASK_PROMPT"],
          options=ClaudeAgentOptions(max_turns=20),
      ):
          print(message)

  asyncio.run(main())
  ```
</CodeGroup>

The script prints each message as it arrives, including a result message whose `subtype` is `success` when the task completes within the turn limit. If the task hits the 20-turn limit instead, the result message's `subtype` is `error_max_turns` and the `query()` call raises an error after yielding it, so wrap the loop in a try block if the container needs to exit cleanly. See [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result) for the error subtypes.

### Long-running sessions

Run persistent container instances, often hosting multiple SDK processes per container, to serve ongoing work. Best for agents that take autonomous action, serve content, or handle high-volume message streams.

Example workloads include an email agent that triages and responds to incoming mail, a site builder that hosts a per-user editable site through container ports, and a chat bot that handles continuous traffic from a platform like Slack.

The container exposes an HTTP or WebSocket endpoint and maps each active session to a long-lived query and the subprocess behind it. In TypeScript, use [`streamInput()`](/docs/en/agent-sdk/typescript#query-object) to add turns to an active session and [`startup()`](/docs/en/agent-sdk/typescript#startup) to pre-warm subprocesses ahead of incoming traffic. In Python, use [`ClaudeSDKClient`](/docs/en/agent-sdk/python#claudesdkclient) to hold a session open across turns. Size the container so it can hold the maximum number of concurrent sessions in memory.

### Hybrid sessions

Ephemeral containers that hydrate from a [`SessionStore`](/docs/en/agent-sdk/session-storage) on startup and persist updates back. Best for sessions that span many interactions but sit idle between them. The container spins down during idle periods and spins back up when the user returns.

Example workloads include a personal project manager with intermittent check-ins, deep research that pauses and resumes over hours, and a customer support agent that loads ticket history across interactions.

Tune your provider's idle timeout to how frequently you expect users to return. Shutting a container down without a `SessionStore` configured loses the transcript with it, so the store is required for this pattern, not optional.

The pattern hinges on resuming a session by ID with a shared store attached:

<CodeGroup>
  ```typescript TypeScript theme={null}

  declare const userInput: string;
  declare const sessionId: string;          // looked up from your database by user
  declare const sessionStore: SessionStore; // an object store, key-value store, database, or your own adapter

  for await (const message of query({
    prompt: userInput,
    options: { resume: sessionId, sessionStore },
  })) {
    // ...
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, SessionStore
  import asyncio

  user_input: str = ...
  session_id: str = ...              # looked up from your database by user
  session_store: SessionStore = ...  # an object store, key-value store, database, or your own adapter

  async def main():
      async for message in query(
          prompt=user_input,
          options=ClaudeAgentOptions(
              resume=session_id,
              session_store=session_store,
          ),
      ):
          ...

  asyncio.run(main())
  ```
</CodeGroup>

### Multi-agent container

Run multiple SDK subprocesses inside one container. Best for agents that must collaborate closely, for example multi-agent simulations where the agents interact with each other in a shared environment.

Give each agent its own working directory so they do not overwrite each other's files, and isolate settings loading so per-agent `CLAUDE.md` files do not leak across agents. See [Multi-tenant isolation](#multi-tenant-isolation) for the specific options.

## Provision the container

### Container-based sandboxing

Run the SDK inside a sandboxed container for process isolation, resource limits, network control, and an ephemeral filesystem.

Questions to answer when choosing a provider:

* **Who runs the sandbox**: a sandbox-as-a-service provider operates the infrastructure for you, while self-hosted options give you software to run on your own.
* **Cold-start latency**: how long from "create a sandbox" to "ready to accept the first request." Ephemeral patterns need sub-second starts. Long-running patterns tolerate more.
* **Persistent storage**: whether the provider offers durable volumes or only ephemeral disk. The hybrid pattern needs durable storage somewhere, whether in the sandbox or alongside it.
* **Pricing model**: per-second, per-request, or flat hourly billing. Per-second pricing suits bursty ephemeral workloads. Hourly suits long-running sessions.
* **Networking**: support for custom egress rules, outbound proxies, and private VPC peering for regulated environments.

For self-hosted options such as Docker, gVisor, and Firecracker, and detailed isolation configuration, see [Isolation Technologies](/docs/en/agent-sdk/secure-deployment#isolation-technologies).

### Runtime dependencies

The container needs your SDK's language runtime:

* Python 3.10+ for the Python SDK, or Node.js 18+ for the TypeScript SDK
* Both the TypeScript and Python SDKs bundle a native Claude Code binary for most installs, and the spawned CLI needs no separate Node.js install. See the [quickstart's install note](/docs/en/agent-sdk/quickstart) for the installs that need a separate native Claude Code install.

The bundled binary is pinned to the SDK package version, so updating the SDK is how you update the CLI. The SDK follows semver: take patch releases continuously and review the [TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md) or [Python](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md) changelog before taking a minor.

### Resources

1 GiB RAM, 5 GiB disk, and 1 CPU per agent is a reasonable starting point for a freshly started instance. Memory usage grows with session length and tool activity, so size for the session lengths and concurrency you actually need rather than the idle baseline. See [Scaling and concurrency](#scaling-and-concurrency) for how to work out agents per host.

### Network

The SDK needs outbound HTTPS to `api.anthropic.com`, or to your provider's regional endpoint when running on Amazon Bedrock or Google Cloud's Agent Platform. If your agents use [MCP servers](/docs/en/agent-sdk/mcp) or external tools, they need outbound access to those endpoints as well. For production, route outbound traffic through an egress proxy that enforces domain allowlists, injects credentials, and logs requests. See [Secure Deployment](/docs/en/agent-sdk/secure-deployment) for the full pattern.

For inbound traffic, expose an HTTP or WebSocket port on the container. Your application handles client requests on that port and calls the SDK internally; the subprocess itself does not listen on the network.

## Handle production concerns

Work through these decisions before shipping a self-hosted agent.

### Session and state persistence

Default local disk is lost on restart, scale-down, or a move to a different node. For any session a user expects to resume, mirror the transcript to durable storage with a [`SessionStore` adapter](/docs/en/agent-sdk/session-storage). See [Reference implementations](/docs/en/agent-sdk/session-storage#reference-implementations) for example adapters for an object store, a key-value store, and a database, and a conformance suite for your own.

Three things to know about how `SessionStore` behaves:

* **Transcripts only**: `SessionStore` mirrors transcripts, not `CLAUDE.md` memory files or other working-directory artifacts. Mount a shared volume or sync those separately.
* **Mirror, not replacement**: the subprocess writes to local disk first, and the SDK forwards a copy of each batch to the store. A fresh session's local transcript outlives the run; a run resumed from the store deletes its local copy at the end, so the store holds the only durable copy. See [Dual-write architecture](/docs/en/agent-sdk/session-storage#dual-write-architecture).
* **`mirror_error` messages**: when the SDK can't deliver a batch to the store, it drops the batch, emits a `{ type: "system", subtype: "mirror_error" }` message, and continues the query. Alert on these if store durability matters. See [Mirror writes are best-effort](/docs/en/agent-sdk/session-storage#mirror-writes-are-best-effort) for the retry and timeout behavior.

### Observability

Agent SDK agents are long-lived processes that spawn tool calls across many API round-trips. Without telemetry you cannot see which tools ran, how long they took, or where a session stalled.

The SDK inherits OpenTelemetry configuration from the environment. Set the OTEL environment variables at the container or orchestrator level so every `query()` call exports spans, metrics, and log events to your collector. The example below enables OTLP export for all three signals. `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA` is required only for traces; omit it if you export metrics and logs alone.

```bash title=".env" theme={null}
CLAUDE_CODE_ENABLE_TELEMETRY=1
CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1
OTEL_TRACES_EXPORTER=otlp
OTEL_METRICS_EXPORTER=otlp
OTEL_LOGS_EXPORTER=otlp
OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
OTEL_EXPORTER_OTLP_ENDPOINT=http://collector.example.com:4318
```

Prompt text and tool inputs are not included in exports by default. See [Control sensitive data in exports](/docs/en/agent-sdk/observability#control-sensitive-data-in-exports) for the opt-in flags, and [Observability](/docs/en/agent-sdk/observability) for the full signal catalog.

### Auth and secrets

Three auth concerns matter at hosting time:

* **Anthropic API**: the subprocess reads `ANTHROPIC_API_KEY` from its environment. Supply it from your secret manager, or set `ANTHROPIC_BASE_URL` to route model calls through a proxy that injects the key outside the container. See [Credential management](/docs/en/agent-sdk/secure-deployment#credential-management) for the proxy pattern and [Setup in the SDK quickstart](/docs/en/agent-sdk/quickstart#setup) for supported authentication methods.
* **Inbound**: put authentication at a gateway in front of the agent container. The agent should receive pre-authenticated requests and should not be the component that validates user tokens.
* **Outbound tools**: keep tool credentials out of the agent environment. Route outbound calls through a proxy that injects API keys after the request leaves the container. The agent makes the call; the proxy adds the credential.

### Scaling and concurrency

Each session runs in its own subprocess, so concurrency on a host is bounded by how many subprocesses its RAM can hold.

Size each host with this formula:

```text theme={null}
agents per host = (host RAM - overhead) / (per-session RAM ceiling)
```

Measure the per-session ceiling by running a representative session to your target length under your expected tool load and recording peak RSS. The 1 GiB starting point in [Resources](#resources) is a floor, not the ceiling.

Horizontal-scale routing depends on your pattern. For long-running sessions, where containers hold many sessions, run a pool of containers behind a load balancer and pin each session to one container using consistent hashing on `sessionId`. A pinned session keeps hitting the same container, and therefore the same running subprocess, until it is evicted or the container restarts.

### Cost

Anthropic token cost typically dominates container infrastructure cost by an order of magnitude or more. A minimally provisioned container runs roughly \$0.05 per hour, while a single long agent session can spend dollars in tokens. See [Cost tracking](/docs/en/agent-sdk/cost-tracking) for per-session token accounting.

### Multi-tenant isolation

Default SDK behavior reads settings and `CLAUDE.md` memory files from the filesystem. In a shared container that serves multiple tenants, those files can leak one tenant's context into another tenant's session.

To isolate tenants inside a shared container:

* Pass `settingSources: []` in TypeScript or `setting_sources=[]` in Python to skip user, project, and local settings.
* Set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` in `env`. [Auto memory](/docs/en/memory#auto-memory) at `~/.claude/projects/<project>/memory/` loads into the system prompt regardless of `settingSources`. See [What settingSources does not control](/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control) for the other inputs that load unconditionally.
* Point `CLAUDE_CONFIG_DIR` at a per-tenant directory so tenants do not share the `~/.claude.json` global config. When each config directory serves one working directory and you don't share a [`SessionStore`](/docs/en/agent-sdk/session-storage) across tenants, you can also set [`CLAUDE_CODE_PROJECT_DIR_NAME`](/docs/en/sessions#name-the-project-directory-yourself) in `env` to keep the transcript paths under it short. Requires TypeScript Agent SDK v0.3.234 or later, or Python Agent SDK v0.2.140 or later.
* Use a per-tenant working directory. Pass `cwd` explicitly on every `query()` call.
* Apply per-tenant egress rules at your proxy, such as distinct outbound IPs, credentials, or domain allowlists, so a compromised tenant cannot exfiltrate data via another tenant's outbound policy.

The example below applies the settings, auto memory, config directory, and working directory options together. Construct `tenantDir` and `configDir` so each tenant gets a path no other tenant can read. In TypeScript, `env` replaces the subprocess environment, so spread `...process.env` to keep inherited variables like `PATH` and `ANTHROPIC_API_KEY`. In Python, `env` is merged on top of the inherited environment.

<CodeGroup>
  ```typescript TypeScript theme={null}

  declare const prompt: string;
  declare const tenantDir: string;
  declare const configDir: string;

  for await (const message of query({
    prompt,
    options: {
      cwd: tenantDir,
      settingSources: [],
      env: {
        ...process.env,
        CLAUDE_CONFIG_DIR: configDir,
        CLAUDE_CODE_DISABLE_AUTO_MEMORY: "1",
      },
    },
  })) {
    // ...
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions
  import asyncio

  prompt: str = ...
  tenant_dir: str = ...
  config_dir: str = ...

  async def main():
      async for message in query(
          prompt=prompt,
          options=ClaudeAgentOptions(
              cwd=tenant_dir,
              setting_sources=[],
              env={
                  "CLAUDE_CONFIG_DIR": config_dir,
                  "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
              },
          ),
      ):
          ...

  asyncio.run(main())
  ```
</CodeGroup>

## Known limitations

Plan around these in your deployment design.

| Limitation                                          | What to do                                                                                                                                                                                                                               |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No top-level session timeout                        | A session does not time out on its own. Set `maxTurns` in TypeScript or `max_turns` in Python to bound how many tool-use round trips the agent takes before stopping.                                                                    |
| Memory growth over long sessions                    | Cap session length or recycle subprocesses periodically. See [Scaling and concurrency](#scaling-and-concurrency).                                                                                                                        |
| Large parallel-subagent fanouts can hit rate limits | Break work into smaller batches rather than issuing one wide dispatch.                                                                                                                                                                   |
| No per-subagent wall-clock deadline                 | Cap each [subagent](/docs/en/agent-sdk/subagents) with `maxTurns` in its `AgentDefinition`. `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` sets a stall watchdog that fires when a subagent stops producing output; it isn't a total-runtime deadline. |

## Troubleshoot deployment failures

Use this section when an agent that works on your machine fails in a deployed service. Each item below names a failure and links the entry that covers it:

* **CLI not found at service start**: in Python, a container or service manager runs your application with a different `PATH` than your shell, so an install that works locally isn't visible to the process. In TypeScript, the image build skipped the SDK's optional dependencies, or `pathToClaudeCodeExecutable` points at a file that doesn't exist in the image. See [Claude Code not found](/docs/en/agent-sdk/troubleshooting#clinotfounderror-claude-code-not-found).
* **CLI present in the image but won't launch**: Claude Code can't start from a binary that doesn't match the container's architecture or libc, or from a file that lost its execute permission in the image build. See [Failed to start Claude Code](/docs/en/agent-sdk/troubleshooting#cliconnectionerror-failed-to-start-claude-code).
* **Claude Code process exits mid-run**: the error your application receives depends on the SDK language and on whether the CLI reported an error result first. The entries under [CLI process exit](/docs/en/agent-sdk/troubleshooting#cli-process-exit) cover each message.

## Next steps

* [Hosting cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/07_Hosting_the_agent.ipynb): notebook walkthrough with [deployable code](https://github.com/anthropics/claude-cookbooks/tree/main/claude_agent_sdk/hosting) for Docker, Modal, and Kubernetes.
* [Session storage](/docs/en/agent-sdk/session-storage): persist transcripts across hosts with a `SessionStore` adapter.
* [Observability](/docs/en/agent-sdk/observability): export OTEL traces, metrics, and logs to your collector.
* [Secure deployment](/docs/en/agent-sdk/secure-deployment): network controls, credential management, and isolation hardening.
* [Cost tracking](/docs/en/agent-sdk/cost-tracking): per-session token and cost accounting.

---

## Connect to external tools with MCP

- 官方原文：https://code.claude.com/docs/en/agent-sdk/mcp.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-mcp.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect to external tools with MCP

> Configure MCP servers to extend your agent with external tools. Covers transport types, tool search for large tool sets, authentication, and error handling.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) is an open standard for connecting AI agents to external tools and data sources. With MCP, your agent can query databases, integrate with APIs like Slack and GitHub, and connect to other services without writing custom tool implementations.

MCP servers can run as local processes, connect over HTTP, or execute directly within your SDK application.

<Note>
  This page covers MCP configuration for the Agent SDK. To add MCP servers to the Claude Code CLI so they load in every project, see [MCP installation scopes](/docs/en/mcp#mcp-installation-scopes).
</Note>

## Quickstart

This example connects to the [Claude Code documentation](https://code.claude.com/docs) MCP server using [HTTP transport](#http%2Fsse-servers) and uses [`allowedTools`](#allow-mcp-tools) with a wildcard to permit all tools from the server.

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Use the docs MCP server to explain what hooks are in Claude Code",
    options: {
      mcpServers: {
        "claude-code-docs": {
          type: "http",
          url: "https://code.claude.com/docs/mcp"
        }
      },
      allowedTools: ["mcp__claude-code-docs__*"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={
              "claude-code-docs": {
                  "type": "http",
                  "url": "https://code.claude.com/docs/mcp",
              }
          },
          allowed_tools=["mcp__claude-code-docs__*"],
      )

      async for message in query(
          prompt="Use the docs MCP server to explain what hooks are in Claude Code",
          options=options,
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

The agent connects to the documentation server, searches for information about hooks, and returns the results.

## Add an MCP server

You can configure MCP servers in code when calling `query()`, or in a `.mcp.json` file loaded via [`settingSources`](#from-a-config-file).

### In code

Pass MCP servers directly in the `mcpServers` option. This example starts a local filesystem MCP server for `/Users/me/projects`. Replace that path with a directory on your machine:

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "List files in my project",
    options: {
      mcpServers: {
        filesystem: {
          command: "npx",
          args: ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
        }
      },
      allowedTools: ["mcp__filesystem__*"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={
              "filesystem": {
                  "command": "npx",
                  "args": [
                      "-y",
                      "@modelcontextprotocol/server-filesystem",
                      "/Users/me/projects",
                  ],
              }
          },
          allowed_tools=["mcp__filesystem__*"],
      )

      async for message in query(prompt="List files in my project", options=options):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

### From a config file

Create a `.mcp.json` file at your project root. The file is picked up when the `project` setting source is enabled, which it is for default `query()` options. If you set `settingSources` explicitly, include `"project"` for this file to load. Replace `/Users/me/projects` with a directory on your machine:

```json theme={null}
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
    }
  }
}
```

## Connection timing

Claude Code registers the servers you pass in `options.mcpServers` at startup and emits the [init message](#error-handling) once the first-turn wait, if any, resolves. Whether each `options.mcpServers` server delays the first turn, and when it connects, depends on its type:

| Server type                                                                            | Delays the first turn?                                 | First-turn wait timeout                                                                     |
| :------------------------------------------------------------------------------------- | :----------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| stdio server, or HTTP/SSE server without a cached tool list                            | Yes, until it connects                                 | [`MCP_TIMEOUT`](/docs/en/env-vars), 30 seconds by default; the connection fails at that deadline |
| Remote server with a cached tool list, saved by Claude Code from a previous connection | No; the cached tools are available from the first turn | None; connects on its first tool call, and that deferred connect has its own timeout        |
| In-process [SDK server](#sdk-mcp-servers)                                              | Yes, until it connects and lists its tools             | None; the connect and tool listing requests each have their own timeout                     |

Servers loaded from [settings files](#from-a-config-file) such as `.mcp.json` or from plugins commonly show `pending` in the init message. When `options.mcpServers` holds a stdio, HTTP, or SSE server, the first turn waits for these pending servers too, up to `MCP_TIMEOUT`. When `options.mcpServers` is empty or holds only SDK servers, the first turn waits up to 2 seconds instead:

* **With [tool search](/docs/en/agent-sdk/tool-search), the default**: the wait covers still-pending servers configured with [`alwaysLoad: true`](/docs/en/mcp#exempt-a-server-from-deferral) and not the rest. The rest keep connecting in the background. [Tool availability](/docs/en/mcp#tool-availability) describes how Claude reaches their tools once they connect.
* **Without tool search**: the wait covers every pending server. [Configure tool search](/docs/en/agent-sdk/tool-search#configure-tool-search) covers what turns tool search off. If you exclude the `ToolSearch` tool from the session, for example through `disallowedTools`, the session also runs without tool search.

If you set `permissionPromptToolName`, the first turn also waits for that tool's server in every case, up to `MCP_TIMEOUT`.

To set the first-turn wait yourself, add `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` to the [`env` option](/docs/en/agent-sdk/configuration#set-environment-variables), for example `CLAUDE_CODE_MCP_STARTUP_WAIT_MS: "5000"`. The first turn then waits up to that many milliseconds for every pending server, whether or not tool search is available. This deadline also replaces the `MCP_TIMEOUT` first-turn wait for stdio, HTTP, and SSE servers in `options.mcpServers`. `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` requires Claude Code v2.1.274 or later.

Servers still pending when the wait ends keep connecting in the background. Set the variable to `0` to skip the wait. A `permissionPromptToolName` server keeps its own `MCP_TIMEOUT` wait regardless of the value.

To block startup itself at a separate, earlier phase than the first-turn wait, before the init message is sent:

* Set [`MCP_CONNECTION_NONBLOCKING`](/docs/en/env-vars) to `0` to block on the whole connection batch. Claude Code caps that wait at 5 seconds by default. Adjust the cap with the [`MCP_CONNECT_TIMEOUT_MS`](/docs/en/env-vars) environment variable, in milliseconds. Servers still pending at that deadline keep connecting in the background.
* Set `alwaysLoad: true` on a server's config to make its tools available at their full schemas on the first turn, [exempt from tool search deferral](/docs/en/mcp#exempt-a-server-from-deferral). Claude Code waits at startup for that server's tools, capped at the same deadline, while other servers keep connecting in the background; a remote server with a cached tool list supplies them without connecting, per the table above.

The `system` message with subtype `init` reports each server's status at the moment it's emitted; see [Error handling](#error-handling) for reading those statuses.

## Allow MCP tools

MCP tools require explicit permission before Claude can use them. Without permission, Claude will see that tools are available but won't be able to call them.

### Tool naming convention

MCP tools follow the naming pattern `mcp__<server-name>__<tool-name>`. For example, a GitHub server named `"github"` with a `list_issues` tool becomes `mcp__github__list_issues`.

### Auto-approve with allowedTools

Use `allowedTools` to auto-approve specific MCP tools so Claude can use them without a permission prompt:

<CodeGroup>
  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      mcpServers: {
        // your servers
      },
      allowedTools: [
        "mcp__github__*", // All tools from the github server
        "mcp__db__query", // Only the query tool from db server
        "mcp__slack__send_message" // Only send_message from slack server
      ]
    }
  };
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      mcp_servers={
          # your servers
      },
      allowed_tools=[
          "mcp__github__*",  # All tools from the github server
          "mcp__db__query",  # Only the query tool from db server
          "mcp__slack__send_message",  # Only send_message from slack server
      ],
  )
  ```
</CodeGroup>

Wildcards (`*`) let you allow all tools from a server without listing each one individually.

<Note>
  **Prefer `allowedTools` over permission modes for MCP access.** `permissionMode: "acceptEdits"` does not auto-approve MCP tools (only file edits and filesystem Bash commands). `permissionMode: "bypassPermissions"` does auto-approve MCP tools but also disables most other safety prompts, which is broader than necessary; see [How permissions are evaluated](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) for the prompts that remain. A wildcard in `allowedTools` grants exactly the MCP server you want and nothing more. See [Permission modes](/docs/en/agent-sdk/permissions#permission-modes) for a full comparison.
</Note>

### Discover available tools

To see what tools an MCP server provides, check the server's documentation or inspect the `tools` array in the `system` init message. MCP tool names start with `mcp__`.

Claude Code emits the init message after the [first-turn connection wait](#connection-timing) for servers passed in `options.mcpServers`, so the `tools` array lists the `mcp__` tools of each server that has connected by then, plus those of servers with a [cached tool list](#connection-timing), which connect on first use. Tools of any other server that hasn't connected are absent; see [Error handling](#error-handling) for reading each server's status.

This filter prints the MCP tool names:

<CodeGroup>
  ```typescript TypeScript theme={null}

  const options = {
    mcpServers: {
      // your servers
    },
  };

  for await (const message of query({ prompt: "...", options })) {
    if (message.type === "system" && message.subtype === "init") {
      const mcpTools = message.tools.filter((name) => name.startsWith("mcp__"));
      console.log("Available MCP tools:", mcpTools);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={
              # your servers
          },
      )
      async for message in query(prompt="...", options=options):
          if isinstance(message, SystemMessage) and message.subtype == "init":
              mcp_tools = [t for t in message.data.get("tools", []) if t.startswith("mcp__")]
              print("Available MCP tools:", mcp_tools)

  asyncio.run(main())
  ```
</CodeGroup>

You can also ask Claude to list the tools available from a server.

## Transport types

MCP servers communicate with your agent using different transport protocols. Check the server's documentation to see which transport it supports:

* If the docs give you a **command to run** (like `npx @modelcontextprotocol/server-filesystem`), use stdio
* If the docs give you a **URL**, use HTTP or SSE
* If you're building your own tools in code, use an SDK MCP server

### stdio servers

Local processes that communicate via stdin/stdout. Use this for MCP servers you run on the same machine. For the `.mcp.json` form, use the same fields shown at [From a config file](#from-a-config-file). In code, pass the command and its arguments. Replace `/Users/me/projects` with a directory on your machine:

<CodeGroup>
  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      mcpServers: {
        filesystem: {
          command: "npx",
          args: ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
        }
      },
      allowedTools: ["mcp__filesystem__read_file", "mcp__filesystem__list_directory"]
    }
  };
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      mcp_servers={
          "filesystem": {
              "command": "npx",
              "args": [
                  "-y",
                  "@modelcontextprotocol/server-filesystem",
                  "/Users/me/projects",
              ],
          }
      },
      allowed_tools=["mcp__filesystem__read_file", "mcp__filesystem__list_directory"],
  )
  ```
</CodeGroup>

### HTTP/SSE servers

Use HTTP or SSE for cloud-hosted MCP servers and remote APIs. For the `.mcp.json` form, use the same fields as the example at [HTTP headers for remote servers](#http-headers-for-remote-servers), with `"type": "sse"` for an SSE server. In code, pass the server's URL:

<CodeGroup>
  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      mcpServers: {
        "remote-api": {
          type: "sse",
          url: "https://api.example.com/mcp/sse",
          headers: {
            Authorization: `Bearer ${process.env.API_TOKEN}`
          }
        }
      },
      allowedTools: ["mcp__remote-api__*"]
    }
  };
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      mcp_servers={
          "remote-api": {
              "type": "sse",
              "url": "https://api.example.com/mcp/sse",
              "headers": {"Authorization": f"Bearer {os.environ['API_TOKEN']}"},
          }
      },
      allowed_tools=["mcp__remote-api__*"],
  )
  ```
</CodeGroup>

For the streamable HTTP transport, use `"type": "http"` instead. In `.mcp.json` and other JSON config files, `"streamable-http"` is accepted as an alias for `"http"`. The SDKs' `McpHttpServerConfig` type declares only `"http"`, so use `"http"` for servers you pass in code.

### SDK MCP servers

Define custom tools directly in your application code instead of running a separate server process. See the [custom tools guide](/docs/en/agent-sdk/custom-tools) for implementation details.

An SDK MCP server registered by an [`initialize` control request](/docs/en/agent-sdk/typescript#sdkcontrolinitializeresponse) begins connecting as soon as Claude Code processes the request.

## MCP tool search

When you have many MCP tools configured, tool definitions can consume a significant portion of your context window. Tool search solves this by withholding tool definitions from context and loading only the ones Claude needs for each turn.

Tool search is enabled by default. See [Tool search](/docs/en/agent-sdk/tool-search) for configuration options, best practices, and using tool search with custom SDK tools.

## Authentication

Most MCP servers require authentication to access external services. Pass credentials through environment variables in the server configuration.

### Pass credentials via environment variables

Use the `env` field to pass API keys, tokens, and other credentials to the MCP server:

  <Tab title="In code">
    <CodeGroup>
      ```typescript TypeScript hidelines={1,-1} theme={null}
      const _ = {
        options: {
          mcpServers: {
            "api-server": {
              command: "npx",
              args: ["-y", "@your-org/api-mcp-server"],
              env: {
                API_KEY: process.env.API_KEY
              }
            }
          },
          allowedTools: ["mcp__api-server__*"]
        }
      };
      ```

      ```python Python theme={null}
      options = ClaudeAgentOptions(
          mcp_servers={
              "api-server": {
                  "command": "npx",
                  "args": ["-y", "@your-org/api-mcp-server"],
                  "env": {"API_KEY": os.environ["API_KEY"]},
              }
          },
          allowed_tools=["mcp__api-server__*"],
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title=".mcp.json">
    ```json theme={null}
    {
      "mcpServers": {
        "api-server": {
          "command": "npx",
          "args": ["-y", "@your-org/api-mcp-server"],
          "env": {
            "API_KEY": "${API_KEY}"
          }
        }
      }
    }
    ```

    The `${API_KEY}` syntax expands environment variables at runtime.
  </Tab>

### HTTP headers for remote servers

For HTTP and SSE servers, pass authentication headers directly in the server configuration:

  <Tab title="In code">
    <CodeGroup>
      ```typescript TypeScript hidelines={1,-1} theme={null}
      const _ = {
        options: {
          mcpServers: {
            "secure-api": {
              type: "http",
              url: "https://api.example.com/mcp",
              headers: {
                Authorization: `Bearer ${process.env.API_TOKEN}`
              }
            }
          },
          allowedTools: ["mcp__secure-api__*"]
        }
      };
      ```

      ```python Python theme={null}
      options = ClaudeAgentOptions(
          mcp_servers={
              "secure-api": {
                  "type": "http",
                  "url": "https://api.example.com/mcp",
                  "headers": {"Authorization": f"Bearer {os.environ['API_TOKEN']}"},
              }
          },
          allowed_tools=["mcp__secure-api__*"],
      )
      ```
    </CodeGroup>
  </Tab>

  <Tab title=".mcp.json">
    ```json theme={null}
    {
      "mcpServers": {
        "secure-api": {
          "type": "http",
          "url": "https://api.example.com/mcp",
          "headers": {
            "Authorization": "Bearer ${API_TOKEN}"
          }
        }
      }
    }
    ```

    The `${API_TOKEN}` syntax expands environment variables at runtime.
  </Tab>

For a complete working example of a remote server authenticated with headers, see [List issues from a repository](#list-issues-from-a-repository).

### OAuth2 authentication

The [MCP specification supports OAuth 2.1](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) for authorization. The SDK doesn't open a browser or run an interactive OAuth flow. When a configured server returns an authorization challenge and no stored token is available, the agent run continues without that server's tools, and the server reports status `needs-auth`. The `mcp_servers` array of the [system init message](/docs/en/agent-sdk/typescript#sdksystemmessage) may still show `pending` for that server when it's emitted. To confirm whether a server needs credentials, poll `mcpServerStatus()` in the TypeScript SDK or [`get_mcp_status()`](/docs/en/agent-sdk/python#methods) in Python.

To supply credentials, complete the OAuth flow in your own application and pass the resulting access token in the server's `headers`:

<CodeGroup>
  ```typescript TypeScript theme={null}
  // After completing OAuth flow in your app.
  // Implement getAccessTokenFromOAuthFlow for your OAuth provider.
  const accessToken = await getAccessTokenFromOAuthFlow();

  const options = {
    mcpServers: {
      "oauth-api": {
        type: "http",
        url: "https://api.example.com/mcp",
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      }
    },
    allowedTools: ["mcp__oauth-api__*"]
  };
  ```

  ```python Python theme={null}
  # After completing OAuth flow in your app.
  # Implement get_access_token_from_oauth_flow for your OAuth provider.
  access_token = await get_access_token_from_oauth_flow()

  options = ClaudeAgentOptions(
      mcp_servers={
          "oauth-api": {
              "type": "http",
              "url": "https://api.example.com/mcp",
              "headers": {"Authorization": f"Bearer {access_token}"},
          }
      },
      allowed_tools=["mcp__oauth-api__*"],
  )
  ```
</CodeGroup>

## Examples

### List issues from a repository

This example connects to the remote [GitHub MCP server](https://github.com/github/github-mcp-server) to list recent issues. The example includes debug logging to verify the MCP connection and tool calls.

Before running, create a [GitHub personal access token](https://github.com/settings/personal-access-tokens) with read access to the repositories you want to query and set it as an environment variable:

```bash theme={null}
export GITHUB_TOKEN=YOUR_GITHUB_PAT
```

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "List the 3 most recent issues in anthropics/claude-code",
    options: {
      mcpServers: {
        github: {
          type: "http",
          url: "https://api.githubcopilot.com/mcp/",
          headers: {
            Authorization: `Bearer ${process.env.GITHUB_TOKEN}`
          }
        }
      },
      allowedTools: ["mcp__github__list_issues"]
    }
  })) {
    // Verify MCP server connected successfully
    if (message.type === "system" && message.subtype === "init") {
      console.log("MCP servers:", message.mcp_servers);
    }

    // Log when Claude calls an MCP tool
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if (block.type === "tool_use" && block.name.startsWith("mcp__")) {
          console.log("MCP tool called:", block.name);
        }
      }
    }

    // Print the final result
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  import os
  from claude_agent_sdk import (
      query,
      ClaudeAgentOptions,
      ResultMessage,
      SystemMessage,
      AssistantMessage,
  )

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={
              "github": {
                  "type": "http",
                  "url": "https://api.githubcopilot.com/mcp/",
                  "headers": {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"},
              }
          },
          allowed_tools=["mcp__github__list_issues"],
      )

      async for message in query(
          prompt="List the 3 most recent issues in anthropics/claude-code",
          options=options,
      ):
          # Verify MCP server connected successfully
          if isinstance(message, SystemMessage) and message.subtype == "init":
              print("MCP servers:", message.data.get("mcp_servers"))

          # Log when Claude calls an MCP tool
          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if hasattr(block, "name") and block.name.startswith("mcp__"):
                      print("MCP tool called:", block.name)

          # Print the final result
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

In the `MCP servers:` line, a `status` of `connected` for `github` confirms the token works. If Claude Code has a [cached tool list](#connection-timing) for the server, the status can read `pending` instead and the server connects on its first tool call. If the status is `failed` or `needs-auth`, see [Error handling](#error-handling) before trusting the result, since Claude can fall back to built-in tools when the server is unavailable.

### Query a database

This example uses [DBHub](https://github.com/bytebase/dbhub) to query a Postgres database. The agent automatically discovers the database schema, writes the SQL query, and returns the results.

DBHub's `execute_sql` tool runs whatever SQL the agent emits, including writes, unless you restrict it. Setting `readonly = true` in the [DBHub configuration file](https://dbhub.ai/config/toml) makes DBHub reject `INSERT`, `UPDATE`, `DELETE`, and DDL statements, so the example cannot modify your data even if the agent emits a write. DBHub resolves `${DATABASE_URL}` from the process environment when it loads the config, so the connection string stays out of the file. Create this `dbhub.toml` next to your script:

```toml dbhub.toml theme={null}
[[sources]]
id = "production"
dsn = "${DATABASE_URL}"

[[tools]]
name = "execute_sql"
source = "production"
readonly = true
```

The script then points DBHub at the config file instead of passing a connection string directly. Before running, set the `DATABASE_URL` environment variable to your connection string. Replace the placeholder values with your own database details:

```bash theme={null}
export DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    // Natural language query - Claude writes the SQL
    prompt: "How many users signed up last week? Break it down by day.",
    options: {
      mcpServers: {
        postgres: {
          command: "npx",
          // dbhub.toml sets readonly = true, so execute_sql rejects writes
          args: ["-y", "@bytebase/dbhub", "--config", "dbhub.toml"]
        }
      },
      allowedTools: ["mcp__postgres__execute_sql"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={
              "postgres": {
                  "command": "npx",
                  # dbhub.toml sets readonly = true, so execute_sql rejects writes
                  "args": [
                      "-y",
                      "@bytebase/dbhub",
                      "--config",
                      "dbhub.toml",
                  ],
              }
          },
          allowed_tools=["mcp__postgres__execute_sql"],
      )

      # Natural language query - Claude writes the SQL
      async for message in query(
          prompt="How many users signed up last week? Break it down by day.",
          options=options,
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

## Error handling

MCP servers can fail to connect for various reasons: the server process might not be installed, credentials might be invalid, or a remote server might be unreachable.

Claude Code emits a `system` message with subtype `init` at the start of each query. This message includes the connection status for each MCP server. The `status` field can be `"pending"`, `"connected"`, `"failed"`, `"needs-auth"`, or `"disabled"`. Claude Code emits the init message after the [first-turn connection wait](#connection-timing) for servers passed in `options.mcpServers`, so such a server that connected within the wait shows `"connected"`.

In the init message, don't treat `"pending"` as a failure on its own. It can mean any of these:

* The server hasn't connected yet. See [how long Claude Code waits for it before the first turn](#connection-timing)
* The server's tool list was [served from the cache](#connection-timing), with a connection made on first use
* The connection deadline expired. Such a server reports `"pending"` or `"failed"` depending on timing

Check for `"failed"` or `"needs-auth"` to detect servers that won't be usable:

<CodeGroup>
  ```typescript TypeScript theme={null}

  try {
    for await (const message of query({
      prompt: "Process data",
      options: {
        mcpServers: {
          // Replace dataServer with your server configuration
          "data-processor": dataServer
        }
      }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        const unavailableServers = message.mcp_servers.filter(
          (s) => s.status === "failed" || s.status === "needs-auth"
        );

        if (unavailableServers.length > 0) {
          console.warn("Unavailable MCP servers:", unavailableServers);
        }
      }

      if (message.type === "result" && message.subtype === "error_during_execution") {
        console.error("Execution failed");
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, the error subtype branch above has
    // already run; a failure to start or reach the Claude Code process
    // yields no result message. MCP servers that fail to connect don't
    // throw: use the status check above, and note that servers still
    // "pending" at init need a later status check.
    console.log(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage, ResultMessage

  async def main():
      # Replace data_server with your server configuration
      options = ClaudeAgentOptions(mcp_servers={"data-processor": data_server})

      try:
          async for message in query(prompt="Process data", options=options):
              if isinstance(message, SystemMessage) and message.subtype == "init":
                  unavailable_servers = [
                      s
                      for s in message.data.get("mcp_servers", [])
                      if s.get("status") in ("failed", "needs-auth")
                  ]

                  if unavailable_servers:
                      print(f"Unavailable MCP servers: {unavailable_servers}")

              if (
                  isinstance(message, ResultMessage)
                  and message.subtype == "error_during_execution"
              ):
                  print("Execution failed")
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, the error subtype branch above has
          # already run; a failure to start or reach the Claude Code process
          # yields no result message. MCP servers that fail to connect don't
          # raise: use the status check above, and note that servers still
          # "pending" at init need a later status check.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

A remote server's status can also change after it reports `"connected"`. When the connection to it drops mid-session, Claude Code moves the server back to `"pending"` while [reconnecting](/docs/en/mcp#automatic-reconnection). A later `mcpServerStatus()` call in TypeScript, or [`ClaudeSDKClient.get_mcp_status()`](/docs/en/agent-sdk/python#methods) in Python, can then report `"pending"` for a server you saw connected earlier, with no configuration change on your side.

After five reconnection attempts fail, the server reports `"failed"`, or `"needs-auth"` when it needs authorizing again. To retry manually, call [`reconnectMcpServer()`](/docs/en/agent-sdk/typescript#methods) in TypeScript or [`ClaudeSDKClient.reconnect_mcp_server()`](/docs/en/agent-sdk/python#methods) in Python.

## Troubleshooting

### Server shows "failed" status

Check the `init` message to see which servers failed to connect:

<CodeGroup>
  ```typescript TypeScript theme={null}
  if (message.type === "system" && message.subtype === "init") {
    for (const server of message.mcp_servers) {
      if (server.status === "failed") {
        console.error(`Server ${server.name} failed to connect`);
      }
    }
  }
  ```

  ```python Python theme={null}
  if isinstance(message, SystemMessage) and message.subtype == "init":
      for server in message.data.get("mcp_servers", []):
          if server.get("status") == "failed":
              print(f"Server {server['name']} failed to connect")
  ```
</CodeGroup>

A `"pending"` status doesn't mean the server failed. See [Error handling](#error-handling) for the cases it covers at init. To get updated statuses later in the session, call the query's `mcpServerStatus()` method in the TypeScript SDK, or [`ClaudeSDKClient.get_mcp_status()`](/docs/en/agent-sdk/python#methods) in Python.

Common causes:

* **Missing environment variables**: Ensure required tokens and credentials are set. For stdio servers, check the `env` field matches what the server expects.
* **Server not installed**: For `npx` commands, verify the package exists and Node.js is in your PATH.
* **Invalid connection string**: For database servers, verify the connection string format and that the database is accessible.
* **Network issues**: For remote HTTP/SSE servers, check the URL is reachable and any firewalls allow the connection.

### Tools not being called

If Claude sees tools but doesn't use them, check that you've granted permission with `allowedTools`:

<CodeGroup>
  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      mcpServers: {
        // your servers
      },
      allowedTools: ["mcp__servername__*"] // Auto-approve calls from this server
    }
  };
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      mcp_servers={
          # your servers
      },
      allowed_tools=["mcp__servername__*"],  # Auto-approve calls from this server
  )
  ```
</CodeGroup>

### Connection timeouts

MCP server connections time out after 30 seconds by default. To change how long a running tool call may take, set [`MCP_TOOL_TIMEOUT`](/docs/en/env-vars). If your server takes longer to start, the connection fails. Raise the connection limit with the [`MCP_TIMEOUT`](/docs/en/env-vars) environment variable, in milliseconds. For servers that need more startup time, also consider:

* Using a lighter-weight server if available
* Pre-warming the server before starting your agent
* Checking server logs for slow initialization causes

In TypeScript, you can set the tool-call limit for a single [SDK MCP server](#sdk-mcp-servers) by passing [`timeout` to `createSdkMcpServer()`](/docs/en/agent-sdk/typescript#createsdkmcpserver).

### Tool output exceeds maximum allowed tokens

The SDK applies the same MCP output limit as Claude Code. When a tool result with no image content is larger than 25,000 tokens, Claude Code saves the output to a file and replaces the tool result with an error message that names the file path, so the agent can read the output back in portions.

Raise the limit with the [`MAX_MCP_OUTPUT_TOKENS`](/docs/en/env-vars) environment variable. See [MCP output limits and warnings](/docs/en/mcp#mcp-output-limits-and-warnings) for the full behavior, including how a server can declare a higher per-tool limit with the `anthropic/maxResultSizeChars` annotation.

## Related resources

* **[Custom tools guide](/docs/en/agent-sdk/custom-tools)**: Build your own MCP server that runs in-process with your SDK application
* **[Permissions](/docs/en/agent-sdk/permissions)**: Control which MCP tools your agent can use with `allowedTools` and `disallowedTools`
* **[TypeScript SDK reference](/docs/en/agent-sdk/typescript)**: Full API reference including MCP configuration options
* **[Python SDK reference](/docs/en/agent-sdk/python)**: Full API reference including MCP configuration options
* **[MCP server directory](https://github.com/modelcontextprotocol/servers)**: Browse available MCP servers for databases, APIs, and more

---

## Migrate to Claude Agent SDK

- 官方原文：https://code.claude.com/docs/en/agent-sdk/migration-guide.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-migration-guide.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrate to Claude Agent SDK

> Guide for migrating the Claude Code TypeScript and Python SDKs to the Claude Agent SDK

## Overview

The Claude Code SDK has been renamed to the **Claude Agent SDK** and its documentation has been reorganized. This change reflects the SDK's broader capabilities for building AI agents beyond just coding tasks.

Migrating from the OpenAI Agents SDK instead? The [OpenAI Agents SDK migration recipe](https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk) maps each primitive onto the Claude Agent SDK through a single worked example.

## What's Changed

| Aspect                     | Old                         | New                                                                      |
| :------------------------- | :-------------------------- | :----------------------------------------------------------------------- |
| **Package Name (TS/JS)**   | `@anthropic-ai/claude-code` | `@anthropic-ai/claude-agent-sdk`                                         |
| **Python Package**         | `claude-code-sdk`           | `claude-agent-sdk`                                                       |
| **Documentation Location** | Claude Code docs            | Claude Code docs → dedicated [Agent SDK](/docs/en/agent-sdk/overview) section |

## Migration Steps

### For TypeScript/JavaScript Projects

**1. Uninstall the old package:**

```bash theme={null}
npm uninstall @anthropic-ai/claude-code
```

**2. Install the new package:**

```bash theme={null}
npm install @anthropic-ai/claude-agent-sdk
```

**3. Update your imports:**

Change all imports from `@anthropic-ai/claude-code` to `@anthropic-ai/claude-agent-sdk`:

```typescript theme={null}
// Before

// After
```

**4. Update package.json:**

If `@anthropic-ai/claude-code` is still listed in your `package.json`, replace it with `@anthropic-ai/claude-agent-sdk` and update the version range as well, for example from `"^0.0.42"` to `"^0.3.0"`.

**5. Review [breaking changes](#breaking-changes)**

Make any code changes needed to complete the migration.

### For Python Projects

**1. Uninstall the old package:**

```bash theme={null}
pip uninstall -y claude-code-sdk
```

If the old package isn't installed, pip prints `WARNING: Skipping claude-code-sdk as it is not installed.` That's expected and you can continue to the next step.

**2. Install the new package:**

```bash theme={null}
pip install claude-agent-sdk
```

If `claude-code-sdk` is listed in your `requirements.txt` or `pyproject.toml`, replace it with `claude-agent-sdk`.

**3. Update your imports:**

Change all imports from `claude_code_sdk` to `claude_agent_sdk`:

```python theme={null}
# Before
from claude_code_sdk import query, ClaudeCodeOptions

# After
from claude_agent_sdk import query, ClaudeAgentOptions
```

**4. Review [breaking changes](#breaking-changes)**

Make any code changes needed to complete the migration.

## Breaking changes

<Warning>
  To improve isolation and explicit configuration, Claude Agent SDK v0.1.0 introduces breaking changes for users migrating from Claude Code SDK.
</Warning>

### Python: ClaudeCodeOptions renamed to ClaudeAgentOptions

**What changed:** The Python SDK type `ClaudeCodeOptions` has been renamed to `ClaudeAgentOptions`.

**Migration:**

```python theme={null}
# BEFORE (claude-code-sdk)
from claude_code_sdk import query, ClaudeCodeOptions

options = ClaudeCodeOptions(model="claude-opus-4-7", permission_mode="acceptEdits")

# AFTER (claude-agent-sdk)
from claude_agent_sdk import query, ClaudeAgentOptions

options = ClaudeAgentOptions(model="claude-opus-4-7", permission_mode="acceptEdits")
```

### System prompt no longer default

**What changed:** The SDK no longer uses Claude Code's system prompt by default.

**Migration:**

<CodeGroup>
  ```typescript TypeScript theme={null}

  // BEFORE (v0.0.x) - Used Claude Code's system prompt by default
  const before = query({ prompt: "Hello" });

  // AFTER (v0.1.0) - Uses minimal system prompt by default
  // To get the old behavior, explicitly request Claude Code's preset:
  const presetResult = query({
    prompt: "Hello",
    options: {
      systemPrompt: { type: "preset", preset: "claude_code" }
    }
  });

  // Or use a custom system prompt:
  const customResult = query({
    prompt: "Hello",
    options: {
      systemPrompt: "You are a helpful coding assistant"
    }
  });
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions
  import asyncio

  async def main():
      # BEFORE (v0.0.x) - Used Claude Code's system prompt by default
      async for message in query(prompt="Hello"):
          print(message)

      # AFTER (v0.1.0) - Uses minimal system prompt by default
      # To get the old behavior, explicitly request Claude Code's preset:
      async for message in query(
          prompt="Hello",
          options=ClaudeAgentOptions(
              system_prompt={"type": "preset", "preset": "claude_code"}  # Use the preset
          ),
      ):
          print(message)

      # Or use a custom system prompt:
      async for message in query(
          prompt="Hello",
          options=ClaudeAgentOptions(system_prompt="You are a helpful coding assistant"),
      ):
          print(message)

  asyncio.run(main())
  ```
</CodeGroup>

### Settings sources default

This default was briefly changed in v0.1.0 to load no filesystem settings and then reverted, so no migration action is needed.

**Current behavior:** Omitting `settingSources` on `query()` loads user, project, and local filesystem settings, matching the CLI. This includes `~/.claude/settings.json`, `.claude/settings.json`, `.claude/settings.local.json`, CLAUDE.md files, and custom commands.

To run isolated from filesystem settings, pass `settingSources: []`, or `setting_sources=[]` in Python. See [Control filesystem settings with settingSources](/docs/en/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources) for what each source loads.

Isolation is especially important for CI/CD pipelines, deployed applications, test environments, and multi-tenant systems where local customizations should not leak in.

<Note>
  Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option, so upgrade before relying on `setting_sources=[]`. See [What settingSources does not control](/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control) for inputs that are read even when `settingSources` is `[]`.
</Note>

## Next Steps

* Explore the [Agent SDK Overview](/docs/en/agent-sdk/overview) to learn about available features
* Check out the [TypeScript SDK Reference](/docs/en/agent-sdk/typescript) for detailed API documentation
* Review the [Python SDK Reference](/docs/en/agent-sdk/python) for Python-specific documentation
* Learn about [Custom Tools](/docs/en/agent-sdk/custom-tools) and [MCP Integration](/docs/en/agent-sdk/mcp)

---

## Modifying system prompts

- 官方原文：https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-modifying-system-prompts.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Modifying system prompts

> Choose between the `claude_code` preset and a custom system prompt, and customize behavior with CLAUDE.md, output styles, append, or a fully custom prompt.

System prompts define Claude's behavior, capabilities, and response style. Start from the `claude_code` preset for CLI or IDE-like coding tools where a human watches and steers the work. Write your own prompt for agents with a different surface, identity, or permission model.

## How system prompts work

A system prompt is the initial instruction set that shapes how Claude behaves throughout a conversation. The Agent SDK has three starting points for it:

* **Minimal default**: when you don't set `systemPrompt` in TypeScript or `system_prompt` in Python, the SDK uses a minimal prompt that covers tool calling but omits the rest of the `claude_code` preset's content, including its security and safety instructions and its context about the working directory and environment. This differs from `claude -p`, which uses the Claude Code system prompt by default. If you're migrating from the CLI and want matching behavior, set the `claude_code` preset.
* **`claude_code` preset**: the system prompt that the Claude Code CLI uses, with tool usage instructions, security and safety instructions, and context about the working directory and environment. Set `systemPrompt: { type: "preset", preset: "claude_code" }` in TypeScript or `system_prompt={"type": "preset", "preset": "claude_code"}` in Python, optionally with `append` to add your own instructions on the end.
* **Custom string**: a prompt you write yourself. The SDK sends only what you provide.

### Decide on a starting point

The deciding factor is how closely your agent resembles Claude Code: a coding agent operating in a repository, with a human watching streaming output and steering the work. The further your product is from that, the more you'll want to write your own prompt.

| You're building                                                                                              | Use                                | What you get                                                                                                                  |
| :----------------------------------------------------------------------------------------------------------- | :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| A CLI or IDE-like coding tool where a human watches and steers, and Claude Code's defaults are what you want | `claude_code` preset               | The Claude Code prompt, including tool guidance, safety rules, and environment context                                        |
| The same kind of tool, plus product-specific rules like coding standards, output format, or domain context   | `claude_code` preset with `append` | Everything above, with your instructions added after the preset. Nothing is removed, so this is the lowest-risk customization |
| An agent with a different surface, identity, or permission model, or a non-coding agent                      | Custom prompt string               | Only what you write. You take responsibility for replacing the tool guidance and safety instructions your agent still needs   |
| A thin tool-calling loop with no agent persona, where you supply all behavior in the user prompt             | No `systemPrompt` option           | The minimal default: tool-calling support and nothing else                                                                    |

"Different from Claude Code" usually means one of the following:

* **Different surface**: the output isn't read in a terminal by the person who triggered it. Chat UIs, structured-output consumers, and non-coding automation each need a prompt that matches how their output is rendered and reviewed. Unattended coding automation, like a CI job that fixes lint errors or reviews diffs, still fits the preset because the work itself is what the preset is written for.
* **Different identity**: the agent shouldn't present itself as Claude Code. A support bot, a data-analysis assistant, or any domain-specific agent needs its own name, scope, and persona.
* **Different permission model**: the agent runs autonomously without a human approving each step, or operates on a narrow set of resources. Claude Code's prompt assumes a human is in the loop with access to a full toolset.
* **Non-coding tasks**: most of Claude Code's prompt is coding guidance. For research, content, or operations agents, that guidance competes with the instructions you actually need.

The [comparison table](#compare-the-four-approaches) shows what each customization method preserves.

## Customize agent behavior

`append` and a custom prompt string each change the system prompt directly, and an output style changes the instructions Claude Code gives Claude for every response. CLAUDE.md takes a different path: the SDK reads it and injects its content into the conversation as project context, so it shapes behavior alongside whichever system prompt you choose. [Skills](/docs/en/agent-sdk/skills), [hooks](/docs/en/agent-sdk/hooks), and [permissions](/docs/en/agent-sdk/permissions) also shape behavior outside the system prompt and are covered on their own pages.

### CLAUDE.md files for project-level instructions

CLAUDE.md files give Claude persistent project context and instructions. The SDK injects their content into the conversation and leaves the system prompt untouched, so they work with any system prompt configuration. For what to put in CLAUDE.md, where to place it, and how to write effective instructions, see [When to add to CLAUDE.md](/docs/en/memory#when-to-add-to-claude-md) and the rest of [How Claude remembers your project](/docs/en/memory). This section covers what's specific to the SDK: how CLAUDE.md loads.

The SDK reads CLAUDE.md when the matching setting source is enabled: `'project'` loads `CLAUDE.md` or `.claude/CLAUDE.md` from the working directory, and `'user'` loads `~/.claude/CLAUDE.md`. Default `query()` options enable both sources, so CLAUDE.md loads automatically. If you set `settingSources` in TypeScript or `setting_sources` in Python explicitly, include the sources you need. CLAUDE.md loading is controlled by setting sources, not by the `claude_code` preset.

#### Load CLAUDE.md with the SDK

To load CLAUDE.md, set `settingSources` to include the level where you keep your CLAUDE.md. The example below loads a project-level CLAUDE.md alongside the `claude_code` preset, so Claude has both the coding-agent prompt and your project's conventions:

<CodeGroup>
  ```typescript TypeScript theme={null}

  const messages = [];

  for await (const message of query({
    prompt: "Add a new React component for user profiles",
    options: {
      systemPrompt: {
        type: "preset",
        preset: "claude_code" // Use Claude Code's system prompt
      },
      settingSources: ["project"] // Loads CLAUDE.md from project
    }
  })) {
    messages.push(message);
  }

  // Now Claude has access to your project guidelines from CLAUDE.md
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions

  messages = []

  async def main():
      async for message in query(
          prompt="Add a new React component for user profiles",
          options=ClaudeAgentOptions(
              system_prompt={
                  "type": "preset",
                  "preset": "claude_code",  # Use Claude Code's system prompt
              },
              setting_sources=["project"],  # Loads CLAUDE.md from project
          ),
      ):
          messages.append(message)

  asyncio.run(main())

  # Now Claude has access to your project guidelines from CLAUDE.md
  ```
</CodeGroup>

When you run either example, the SDK streams messages as Claude works: a system init message, assistant messages, user messages carrying tool results, and a final result message with the session outcome.

CLAUDE.md is persistent across all sessions in a project, shared with your team through git, and discovered automatically without code changes. It is not loaded if you pass an empty `settingSources` array.

### Output styles for persistent configurations

Output styles are saved sets of instructions that change Claude's role, tone, and output format. They're stored as markdown files and can be reused across sessions and projects.

#### Create an output style

An output style is a markdown file with [frontmatter](/docs/en/output-styles#frontmatter) for metadata, followed by the prompt content. Save it to `~/.claude/output-styles/` for a user-level style available in every project, or `.claude/output-styles/` in your repository for a project-level style you can commit and share with your team.

A custom output style leaves the `claude_code` preset's software engineering instructions out and uses your own. To keep them and layer your instructions on top, set `keep-coding-instructions: true` in the frontmatter. Those instructions are only in Claude Code's full system prompt, so the setting has no effect in a session on the shorter system prompt, which you pin on or off with [`CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT`](/docs/en/env-vars#variables). Keep them when your agent is still doing software engineering work. Leave them out when you're replacing the role entirely.

The example below defines a code-review persona that keeps the coding instructions, since reviewing code still benefits from Claude Code's security and code-quality guidance. Save it as `~/.claude/output-styles/code-reviewer.md` to make it available across projects:

```markdown ~/.claude/output-styles/code-reviewer.md theme={null}
---
name: Code Reviewer
description: Thorough code review assistant
keep-coding-instructions: true
---

You are an expert code reviewer.

For every code submission:
1. Check for bugs and security issues
2. Evaluate performance
3. Suggest improvements
4. Rate code quality (1-10)
```

#### Activate an output style

Once created, activate output styles via:

* **CLI**: run `/output-style <style>`, for example `/output-style concise`, or run `/config` and select one. The `/output-style` command requires Claude Code v2.1.269 or later.
* **Settings**: set `outputStyle` in `.claude/settings.local.json`
* **TypeScript SDK**: set `outputStyle` inside the inline `settings` object passed to `query()`, or point `settings` at a settings file that sets it. `outputStyle` is not a top-level `Options` field:

  ```typescript theme={null}
  const options = { settings: { outputStyle: "Explanatory" } };
  ```

In the Python SDK, set `outputStyle` through the `settings` option, which takes a JSON string such as `'{"outputStyle": "Explanatory"}'` or a path to a settings file that sets it.

**Note for SDK users:** Output styles are loaded when you include `settingSources: ['user']` or `settingSources: ['project']` (TypeScript) / `setting_sources=["user"]` or `setting_sources=["project"]` (Python) in your options.

### Append to the `claude_code` preset

You can use the Claude Code preset with an `append` property to add your custom instructions while preserving all built-in functionality.

<CodeGroup>
  ```typescript TypeScript theme={null}

  const messages = [];

  for await (const message of query({
    prompt: "Help me write a Python function to calculate fibonacci numbers",
    options: {
      systemPrompt: {
        type: "preset",
        preset: "claude_code",
        append: "Always include detailed docstrings and type hints in Python code."
      }
    }
  })) {
    messages.push(message);
    if (message.type === "assistant") {
      console.log(message.message.content);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage

  messages = []

  async def main():
      async for message in query(
          prompt="Help me write a Python function to calculate fibonacci numbers",
          options=ClaudeAgentOptions(
              system_prompt={
                  "type": "preset",
                  "preset": "claude_code",
                  "append": "Always include detailed docstrings and type hints in Python code.",
              }
          ),
      ):
          messages.append(message)
          if isinstance(message, AssistantMessage):
              print(message.content)

  asyncio.run(main())
  ```
</CodeGroup>

#### Improve prompt caching across users and machines

By default, two sessions that use the same `claude_code` preset and `append` text still cannot share a prompt cache entry if they run from different working directories. This is because the preset embeds per-session context in the system prompt ahead of your `append` text: the working directory, whether it's a git repository, the platform, the active shell, the OS version, and auto memory paths. Any difference in that context produces a different system prompt and a cache miss. CLAUDE.md content doesn't affect the system prompt cache because the SDK injects it into the conversation, not the system prompt.

To make the system prompt identical across sessions, set `excludeDynamicSections: true` in TypeScript or `"exclude_dynamic_sections": True` in Python. The per-session context moves into the first user message, leaving only the static preset and your `append` text in the system prompt so identical configurations share a cache entry across users and machines.

<Note>
  `excludeDynamicSections` requires `@anthropic-ai/claude-agent-sdk` v0.2.98 or later, or `claude-agent-sdk` v0.1.58 or later for Python. Set it on the preset object form only. The SDK ignores it when you pass a custom prompt instead of the preset; to keep a custom prompt's instructions cached in the TypeScript SDK, see [Cache the static part of a custom prompt](#cache-the-static-part-of-a-custom-prompt).
</Note>

The following example pairs a shared `append` block with `excludeDynamicSections` so a fleet of agents running from different directories can reuse the same cached system prompt:

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Triage the open issues in this repo",
    options: {
      systemPrompt: {
        type: "preset",
        preset: "claude_code",
        append: "You operate Acme's internal triage workflow. Label issues by component and severity.",
        excludeDynamicSections: true
      }
    }
  })) {
    // ...
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions

  async def main():
      async for message in query(
          prompt="Triage the open issues in this repo",
          options=ClaudeAgentOptions(
              system_prompt={
                  "type": "preset",
                  "preset": "claude_code",
                  "append": "You operate Acme's internal triage workflow. Label issues by component and severity.",
                  "exclude_dynamic_sections": True,
              },
          ),
      ):
          ...

  asyncio.run(main())
  ```
</CodeGroup>

**Tradeoffs:** the working directory, the git-repo flag, the platform, the active shell, the OS version, and auto memory paths still reach Claude, but as part of the first user message rather than the system prompt. Instructions in the user message carry marginally less weight than the same text in the system prompt, so Claude may rely on them less strongly when reasoning about the current directory or auto memory paths. Enable this option when cross-session cache reuse matters more than maximally authoritative environment context.

For the equivalent flag in non-interactive CLI mode, see [`--exclude-dynamic-system-prompt-sections`](/docs/en/cli-reference).

### Custom system prompts

You can provide a custom string as `systemPrompt` to replace the default entirely with your own instructions.

<CodeGroup>
  ```typescript TypeScript theme={null}

  const customPrompt = `You are a Python coding specialist.
  Follow these guidelines:
  - Write clean, well-documented code
  - Use type hints for all functions
  - Include comprehensive docstrings
  - Prefer functional programming patterns when appropriate
  - Always explain your code choices`;

  const messages = [];

  for await (const message of query({
    prompt: "Create a data processing pipeline",
    options: {
      systemPrompt: customPrompt
    }
  })) {
    messages.push(message);
    if (message.type === "assistant") {
      console.log(message.message.content);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage

  custom_prompt = """You are a Python coding specialist.
  Follow these guidelines:
  - Write clean, well-documented code
  - Use type hints for all functions
  - Include comprehensive docstrings
  - Prefer functional programming patterns when appropriate
  - Always explain your code choices"""

  messages = []

  async def main():
      async for message in query(
          prompt="Create a data processing pipeline",
          options=ClaudeAgentOptions(system_prompt=custom_prompt),
      ):
          messages.append(message)
          if isinstance(message, AssistantMessage):
              print(message.content)

  asyncio.run(main())
  ```
</CodeGroup>

In Python, load a large custom prompt from a file with `system_prompt={"type": "file", "path": "..."}` instead of passing it as a string. The Python SDK passes a string prompt as one command-line argument to the CLI subprocess, so a prompt that exceeds the OS argument-length limit fails at process spawn before any API request is sent. On Linux the error is `Argument list too long`. See [`SystemPromptFile`](/docs/en/agent-sdk/python#systempromptfile) for the platform thresholds and the Windows behavior.

#### Cache the static part of a custom prompt

In the TypeScript SDK, you can pass a custom prompt as an array of strings instead of one string, with the `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` marker between the static part and the rest. Use this when your prompt combines instructions that are the same on every request with context that changes per request, such as the customer or ticket the agent is handling. When you pass both parts as one string, a change to the per-request part changes the whole system prompt, so the static instructions miss the cache too. The array form isn't available in the Python SDK; [`ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions) lists the forms `system_prompt` accepts.

<Note>
  Claude Code splits the prompt only when it calls the Claude API directly or runs on [Claude Platform on AWS](/docs/en/claude-platform-on-aws). In every other configuration, such as Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or an [LLM gateway](/docs/en/llm-gateway-connect), it sends the whole prompt as one block, the same as passing one string. The same happens whenever you set [`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`](/docs/en/llm-gateway-protocol#disable-pre-release-capabilities).
</Note>

To split the prompt, import `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` from `@anthropic-ai/claude-agent-sdk` and pass it as its own array element between the two parts. The SDK sends the strings before the marker as one text block and the strings after it as a second block, each with its own cache breakpoint. In the example below, a support agent loads its triage instructions from a file and receives details about one ticket on each request, so the instructions stay cached while the ticket details change:

```typescript TypeScript theme={null}

// Identical on every request
const instructions = await readFile("triage-instructions.md", "utf8");
// Different on every request
const ticketContext = "Customer plan: Enterprise. Other open tickets from this customer: 3.";

for await (const message of query({
  prompt: "Triage ticket 4821",
  options: {
    systemPrompt: [instructions, SYSTEM_PROMPT_DYNAMIC_BOUNDARY, ticketContext]
  }
})) {
  // ...
}
```

[Track cache tokens](/docs/en/agent-sdk/cost-tracking#track-cache-tokens) describes the `cache_creation_input_tokens` and `cache_read_input_tokens` fields on each result message.

The SDK assembles the blocks from the array as follows:

* The SDK joins the strings on each side of the marker with a blank line between them and removes the marker itself, so the marker text doesn't reach Claude.
* If you include the marker more than once, the first one is the split and the SDK removes the others.
* If you leave the marker out, the SDK joins all the strings into one block, the same as passing one string.

With the CLI's [`--system-prompt` or `--system-prompt-file` flags](/docs/en/cli-reference#system-prompt-flags), the prompt is one string, so there is no array to carry the marker. Include a line containing only `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` between the static and per-request parts instead. Claude Code splits the prompt at the first such line into the same two blocks and removes that line. Requires Claude Code v2.1.275 or later.

In the SDK, prefer the array form, which carries the boundary without a marker line.

### Change the prompt of an existing session

By default, if you pass a different `append` or custom prompt when you return to a session with `resume` or `continue`, Claude doesn't see it on the next turn. Claude Code records the system prompt on a session's first request and reuses that record until the session is compacted. The new text takes effect after that compaction, or in a new session.

#### Update Claude's instructions mid-session

If the instructions you put in the system prompt need to change while a session is running, for example because your user switched the agent to a read-only mode or edited its configuration in your app, send the new instructions in the conversation instead of changing `systemPrompt`:

* **In your next message**: include the new instructions in the next user message you send.
* **From a hook**: return [`additionalContext`](/docs/en/hooks#add-context-for-claude) from a `UserPromptSubmit` or `PostToolUse` [hook callback](/docs/en/agent-sdk/hooks#outputs), written as a factual statement such as "The workspace is now read-only". The SDK inserts the text into the conversation at the point where the hook fired, so the recorded prompt stays unchanged.

#### Turn recording off while you iterate on wording

While you iterate on prompt wording and want each edit to reach a session you resume, set `snapshot` to false on the object form of the system prompt. Claude Code then rebuilds the prompt on every request. The field is available on the preset and custom forms of [`systemPrompt`](/docs/en/agent-sdk/typescript#options) in TypeScript and of [`system_prompt`](/docs/en/agent-sdk/python#systempromptpreset) in Python, and requires `@anthropic-ai/claude-agent-sdk` v0.3.257 or later, or `claude-agent-sdk` v0.2.153 or later.

Keep recording on in production. With recording off, a different `append` or custom prompt on a resumed session reaches Claude on the next turn, and that request can't reuse the session's [prompt cache](/docs/en/prompt-caching#how-the-cache-is-organized). Where the API enforces [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking), Claude also loses its thinking from earlier turns.

Outside of [cloud sessions](/docs/en/cloud-environments), if you start Claude Code in [bare mode](/docs/en/headless#start-faster-with-bare-mode) by passing `--bare` through `extraArgs` or setting `CLAUDE_CODE_SIMPLE=1`, recording stays off unless you set `snapshot: true`.

Recording an `append` or custom prompt by default requires Claude Code v2.1.265 or later, which the TypeScript Agent SDK bundles from v0.3.265 and the Python Agent SDK from v0.2.153. Before Claude Code v2.1.268, sessions that don't [fetch feature flags](/docs/en/env-vars#features-that-need-feature-flag-fetching), including sessions on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, rebuilt the prompt on every request and `snapshot` had no effect.

## Compare the four approaches

The four customization methods differ in where they live, how they're shared, and what they preserve from the `claude_code` preset.

| Feature                 | CLAUDE.md        | Output Styles             | `systemPrompt` with append | Custom `systemPrompt`  |
| ----------------------- | ---------------- | ------------------------- | -------------------------- | ---------------------- |
| **Persistence**         | Per-project file | Saved as files            | Session only               | Session only           |
| **Reusability**         | Per-project      | Across projects           | Code duplication           | Code duplication       |
| **Management**          | On filesystem    | CLI + files               | In code                    | In code                |
| **Default tools**       | Preserved        | Preserved                 | Preserved                  | Lost (unless included) |
| **Built-in safety**     | Maintained       | Maintained                | Maintained                 | Must be added          |
| **Environment context** | Automatic        | Automatic                 | Automatic                  | Must be provided       |
| **Customization level** | Additions only   | Replace or extend default | Additions only             | Complete control       |
| **Version control**     | With project     | Yes                       | With code                  | With code              |
| **Scope**               | Project-specific | User or project           | Code session               | Code session           |

"With append" means using `systemPrompt: { type: "preset", preset: "claude_code", append: "..." }` in TypeScript or `system_prompt={"type": "preset", "preset": "claude_code", "append": "..."}` in Python. CLAUDE.md doesn't change the system prompt itself: the SDK injects its content into the conversation as project context.

## Combine approaches

The approaches compose. A persistent output style or CLAUDE.md sets the long-lived behavior, and `append` layers session-specific instructions on top without touching the saved configuration.

### Combine an output style with session-specific additions

The example below assumes a Code Reviewer output style is already active. The `append` block layers session-specific focus areas on top of the persona, so a single review session can prioritize OAuth and token storage without changing the saved output style:

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Assuming "Code Reviewer" output style is active (via /config or settings)
  // Add session-specific focus areas
  const messages = [];

  for await (const message of query({
    prompt: "Review this authentication module",
    options: {
      systemPrompt: {
        type: "preset",
        preset: "claude_code",
        append: `
          For this review, prioritize:
          - OAuth 2.0 compliance
          - Token storage security
          - Session management
        `
      }
    }
  })) {
    messages.push(message);
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions

  # Assuming "Code Reviewer" output style is active (via /config or settings)
  # Add session-specific focus areas
  messages = []

  async def main():
      async for message in query(
          prompt="Review this authentication module",
          options=ClaudeAgentOptions(
              system_prompt={
                  "type": "preset",
                  "preset": "claude_code",
                  "append": """
                  For this review, prioritize:
                  - OAuth 2.0 compliance
                  - Token storage security
                  - Session management
                  """,
              }
          ),
      ):
          messages.append(message)

  asyncio.run(main())
  ```
</CodeGroup>

## See also

* [Output styles](/docs/en/output-styles): create, manage, and share output styles for the CLI, including the file format and storage locations
* [How Claude remembers your project](/docs/en/memory): what to put in CLAUDE.md, where to place it, and how to write effective project instructions
* [TypeScript SDK reference](/docs/en/agent-sdk/typescript): the full `Options` type, including `systemPrompt`, `settingSources`, and `settings`
* [Python SDK reference](/docs/en/agent-sdk/python): the full `ClaudeAgentOptions` type, including `system_prompt` and `setting_sources`
* [Settings](/docs/en/settings): the `settings.json` reference, including where output styles and other configuration are stored

---

## Observability with OpenTelemetry

- 官方原文：https://code.claude.com/docs/en/agent-sdk/observability.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-observability.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Observability with OpenTelemetry

> Export traces, metrics, and events from the Agent SDK to your observability backend using OpenTelemetry.

When you run agents in production, you need visibility into what they did:

* which tools they called
* how long each model request took
* how many tokens were spent
* where failures occurred

The Agent SDK can export this data as OpenTelemetry traces, metrics, and log events to any backend that accepts the OpenTelemetry Protocol (OTLP), whether a hosted observability platform or a self-hosted collector.

This guide explains how the SDK emits telemetry, how to configure the export, and how to tag and filter the data once it reaches your backend. To read token usage and cost directly from the SDK response stream instead of exporting to a backend, see [Track cost and usage](/docs/en/agent-sdk/cost-tracking).

## How telemetry flows from the SDK

The Agent SDK runs the Claude Code CLI as a child process and communicates with it over a local pipe. The CLI has OpenTelemetry instrumentation built in: it records spans around each model request and tool execution, emits metrics for token and cost counters, and emits structured log events for prompts and tool results. The SDK does not produce telemetry of its own. Instead, it passes configuration through to the CLI process, and the CLI exports directly to your collector.

Configuration is passed as environment variables. By default, the child process inherits your application's environment, so you can configure telemetry in either of two places:

* **Process environment:** set the variables in your shell, container, or orchestrator before your application starts. Every `query()` call picks them up automatically with no code change. This is the recommended approach for production deployments.
* **Per-call options:** set the variables in `ClaudeAgentOptions.env` (Python) or `options.env` (TypeScript). Use this when different agents in the same process need different telemetry settings. In Python, `env` is merged on top of the inherited environment. In TypeScript, `env` replaces the inherited environment entirely, so include `...process.env` in the object you pass.

The CLI exports three independent OpenTelemetry signals. Each has its own enable switch and its own exporter, so you can turn on only the ones you need.

| Signal     | What it contains                                                            | Enable with                                                         |
| ---------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Metrics    | Counters for tokens, cost, sessions, lines of code, and tool decisions      | `OTEL_METRICS_EXPORTER`                                             |
| Log events | Structured records for each prompt, API request, API error, and tool result | `OTEL_LOGS_EXPORTER`                                                |
| Traces     | Spans for each interaction, model request, tool call, and hook (beta)       | `OTEL_TRACES_EXPORTER` plus `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` |

For the complete list of metric names, event names, and attributes, see the Claude Code [Monitoring](/docs/en/monitoring-usage) reference. The Agent SDK emits the same data because it runs the same CLI. Span names are listed in [Read agent traces](#read-agent-traces) below.

## Enable telemetry export

Telemetry is off until you set `CLAUDE_CODE_ENABLE_TELEMETRY=1` and choose at least one exporter. The most common configuration sends all three signals over OTLP HTTP to a collector.

The following example sets the variables in a dictionary and passes them through `options.env`. The agent runs a single task, and the CLI exports spans, metrics, and events to the collector at `collector.example.com` while the loop consumes the response stream:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions

  OTEL_ENV = {
      "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
      # Required for traces, which are in beta. Metrics and log events do not need this.
      "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA": "1",
      # Choose an exporter per signal. Use otlp for the SDK; see the Note below.
      "OTEL_TRACES_EXPORTER": "otlp",
      "OTEL_METRICS_EXPORTER": "otlp",
      "OTEL_LOGS_EXPORTER": "otlp",
      # Standard OTLP transport configuration.
      "OTEL_EXPORTER_OTLP_PROTOCOL": "http/protobuf",
      "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.example.com:4318",
      "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer your-token",
  }

  async def main():
      options = ClaudeAgentOptions(env=OTEL_ENV)
      async for message in query(
          prompt="List the files in this directory", options=options
      ):
          print(message)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  const otelEnv = {
    CLAUDE_CODE_ENABLE_TELEMETRY: "1",
    // Required for traces, which are in beta. Metrics and log events do not need this.
    CLAUDE_CODE_ENHANCED_TELEMETRY_BETA: "1",
    // Choose an exporter per signal. Use otlp for the SDK; see the Note below.
    OTEL_TRACES_EXPORTER: "otlp",
    OTEL_METRICS_EXPORTER: "otlp",
    OTEL_LOGS_EXPORTER: "otlp",
    // Standard OTLP transport configuration.
    OTEL_EXPORTER_OTLP_PROTOCOL: "http/protobuf",
    OTEL_EXPORTER_OTLP_ENDPOINT: "http://collector.example.com:4318",
    OTEL_EXPORTER_OTLP_HEADERS: "Authorization=Bearer your-token",
  };

  for await (const message of query({
    prompt: "List the files in this directory",
    // env replaces the inherited environment in TypeScript, so spread
    // process.env first to keep PATH, ANTHROPIC_API_KEY, and other variables.
    options: { env: { ...process.env, ...otelEnv } },
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

Because the child process inherits your application's environment by default, you can achieve the same result by exporting these variables in a Dockerfile, Kubernetes manifest, or shell profile and omitting `options.env` entirely.

To confirm that export is working, check your collector's logs for incoming spans, metrics, and log events after the task completes. The CLI fails silently on export errors by default: if the endpoint is unreachable or rejects the data, the agent still runs normally and the CLI drops the telemetry without surfacing an error in your application. To surface exporter errors, set [`CLAUDE_CODE_OTEL_DIAG_STDERR=1`](/docs/en/env-vars) alongside the exporter variables and read the diagnostics through the SDK's `stderr` callback (Python) or `stderr` option (TypeScript). Requires Claude Code v2.1.179 or later.

<Note>
  The `console` exporter writes telemetry to standard output, which the SDK uses
  as its message channel. Do not set `console` as an exporter value when running
  through the SDK. To inspect telemetry locally, point
  `OTEL_EXPORTER_OTLP_ENDPOINT` at a local OpenTelemetry Collector instead.
</Note>

### Flush telemetry from short-lived calls

The CLI batches telemetry and exports on an interval. On a clean process exit it attempts to flush pending data, but the flush is bounded by a short timeout, so spans can still be dropped if the collector is slow to respond. If your process is killed before the CLI shuts down, anything still in the batch buffer is lost. Lowering the export intervals reduces both windows.

By default, metrics export every 60 seconds and traces and logs export every 5 seconds. The following example shortens all three intervals so that data reaches the collector while a short task is still running:

<CodeGroup>
  ```python Python theme={null}
  OTEL_ENV = {
      # ... exporter configuration from the previous example ...
      "OTEL_METRIC_EXPORT_INTERVAL": "1000",
      "OTEL_LOGS_EXPORT_INTERVAL": "1000",
      "OTEL_TRACES_EXPORT_INTERVAL": "1000",
  }
  ```

  ```typescript TypeScript theme={null}
  const otelEnv = {
    // ... exporter configuration from the previous example ...
    OTEL_METRIC_EXPORT_INTERVAL: "1000",
    OTEL_LOGS_EXPORT_INTERVAL: "1000",
    OTEL_TRACES_EXPORT_INTERVAL: "1000",
  };
  ```
</CodeGroup>

## Read agent traces

Traces give you the most detailed view of an agent run. With `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` set, each step of the agent loop becomes a span you can inspect in your tracing backend:

* **`claude_code.interaction`:** wraps a single turn of the agent loop, from receiving a prompt to producing a response.
* **`claude_code.llm_request`:** wraps each call to the Claude API, with model name, latency, and token counts as attributes.
* **`claude_code.tool`:** wraps each tool invocation, with child spans for the permission wait (`claude_code.tool.blocked_on_user`) and the execution itself (`claude_code.tool.execution`).
* **`claude_code.hook`:** wraps each [hook](/docs/en/agent-sdk/hooks) execution. Requires detailed beta tracing (`ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT`), a pair that also [changes where your logs and traces go](/docs/en/env-vars#variables).

The `llm_request`, `tool`, and `hook` spans are children of the enclosing `claude_code.interaction` span. When the agent spawns a subagent through the Agent tool, the subagent's `llm_request` and `tool` spans nest under the parent agent's `claude_code.tool` span, so the full delegation chain appears as one trace.

Spans carry a `session.id` attribute by default. When you make several `query()` calls against the same [session](/docs/en/agent-sdk/sessions), filter on `session.id` in your backend to see them as one timeline. Claude Code omits the attribute if you set `OTEL_METRICS_INCLUDE_SESSION_ID` to a falsy value.

<Note>
  Tracing is in beta. Span names and attributes may change between releases. See
  [Traces (beta)](/docs/en/monitoring-usage#traces-beta) in the Monitoring reference
  for the trace exporter configuration variables.
</Note>

## Link traces to your application

The SDK automatically propagates W3C trace context into the CLI subprocess. When you call `query()` while an OpenTelemetry span is active in your application, the SDK injects `TRACEPARENT` and `TRACESTATE` into the child process environment, and the CLI reads them so its `claude_code.interaction` span becomes a child of your span. The agent run then appears inside your application's trace instead of as a disconnected root.

OTLP event log records emitted during the run carry the same trace context: with `TRACEPARENT` set, each record's `trace_id` and `span_id` match your application's trace, so you can join [events](/docs/en/monitoring-usage#events) to spans in your backend. Before v2.1.212, event records emitted outside an active span didn't carry `trace_id` or `span_id`.

When trace-context propagation is enabled, the CLI also forwards `TRACEPARENT` to every Bash and PowerShell command it runs. If a command launched through the Bash tool emits its own OpenTelemetry spans, those spans nest under the `claude_code.tool.execution` span that wraps the command.

Auto-injection is skipped when you set `TRACEPARENT` explicitly in `options.env`, so you can pin a specific parent context if needed. Interactive CLI sessions ignore inbound `TRACEPARENT` entirely; only Agent SDK and `claude -p` runs honor it. See [Traces (beta)](/docs/en/monitoring-usage#traces-beta) in the Monitoring reference for the full span and attribute reference.

## Tag telemetry from your agent

By default, the CLI reports `service.name` as `claude-code`. If you run several agents, or run the SDK alongside other services that export to the same collector, override the service name and add resource attributes so you can filter by agent in your backend.

The following example renames the service and attaches deployment metadata. These values are applied as OpenTelemetry resource attributes on every span, metric, and event the agent emits:

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      env={
          # ... exporter configuration from the Enable telemetry export example ...
          "OTEL_SERVICE_NAME": "support-triage-agent",
          "OTEL_RESOURCE_ATTRIBUTES": "service.version=1.4.0,deployment.environment=production",
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    env: {
      ...process.env,
      // ... exporter configuration from the Enable telemetry export example ...
      OTEL_SERVICE_NAME: "support-triage-agent",
      OTEL_RESOURCE_ATTRIBUTES:
        "service.version=1.4.0,deployment.environment=production",
    },
  };
  ```
</CodeGroup>

## Attribute actions to your end users

The CLI attaches [identity attributes](/docs/en/monitoring-usage#standard-attributes) to every event based on the credential it uses to call Anthropic. When you build an application that serves many end users from one deployment, these attributes identify your service's credential, not the end user on whose behalf the agent acted.

To make tool calls and MCP activity attributable to your application's end users, inject end-user identity as resource attributes on each `query()` call. Percent-encode values before interpolating them, since `OTEL_RESOURCE_ATTRIBUTES` [reserves commas, spaces, and equals signs](/docs/en/monitoring-usage#multi-team-organization-support). The following example attaches the requesting user and tenant to every span and event from one request. It assumes a `request` object from your web framework carrying the user and tenant IDs:

<CodeGroup>
  ```python Python theme={null}
  from urllib.parse import quote

  options = ClaudeAgentOptions(
      env={
          # ... exporter configuration from the Enable telemetry export example ...
          # request is the incoming request object from your web framework.
          "OTEL_RESOURCE_ATTRIBUTES": f"enduser.id={quote(request.user_id)},tenant.id={quote(request.tenant_id)}",
      },
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    env: {
      ...process.env,
      // ... exporter configuration from the Enable telemetry export example ...
      // request is the incoming request object from your web framework.
      OTEL_RESOURCE_ATTRIBUTES: `enduser.id=${encodeURIComponent(request.userId)},tenant.id=${encodeURIComponent(request.tenantId)}`,
    },
  };
  ```
</CodeGroup>

With end-user identity attached, the `tool_decision`, `tool_result`, `mcp_server_connection`, and `permission_mode_changed` events, which export as log records named with a `claude_code.` prefix, become a per-user audit trail you can forward to a Security Information and Event Management (SIEM) platform. See [Audit security events](/docs/en/monitoring-usage#audit-security-events) in the Monitoring reference for the full list of security-relevant events and the attributes each one carries.

## Control sensitive data in exports

Telemetry is structural by default. Durations, model names, and tool names are recorded on every span; token counts are recorded when the underlying API request returns usage data, so spans for failed or aborted requests may omit them. The content your agent reads and writes is not recorded by default. These opt-in variables add content to the exported data:

| Variable                  | Adds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `OTEL_LOG_USER_PROMPTS=1` | Prompt text on `claude_code.user_prompt` events and on the `claude_code.interaction` span                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `OTEL_LOG_TOOL_DETAILS=1` | Tool input arguments (file paths, shell commands, search patterns) on `claude_code.tool_result` events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `OTEL_LOG_TOOL_CONTENT=1` | A [`tool.output` span event](/docs/en/monitoring-usage#tool-output-span-event) on `claude_code.tool` with file contents and Bash output, truncated at 60 KB by default, configurable via `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`, which requires Claude Code v2.1.214 or later. Requires [tracing](#read-agent-traces) to be enabled. Span attributes carry tool content under [their own gates](/docs/en/monitoring-usage#new-context-gates)                                                                                                                                                                |
| `OTEL_LOG_RAW_API_BODIES` | Full Anthropic Messages API request and response JSON as `claude_code.api_request_body` and `claude_code.api_response_body` log events. Set to `1` for inline bodies truncated at 60 KB by default, or `file:<dir>` for untruncated bodies on disk with a `body_ref` path in the event. `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` configures the inline truncation limit, and requires Claude Code v2.1.214 or later. Bodies include the entire conversation history and have extended-thinking content redacted. Enabling this implies consent to everything the three variables above would reveal |

Leave these unset unless your observability pipeline is approved to store the data your agent handles. See [Security and privacy](/docs/en/monitoring-usage#security-and-privacy) in the Monitoring reference for the full list of attributes and redaction behavior.

## Related documentation

These guides cover adjacent topics for monitoring and deploying agents:

* [Track cost and usage](/docs/en/agent-sdk/cost-tracking): read token and cost data from the message stream without an external backend.
* [Hosting the Agent SDK](/docs/en/agent-sdk/hosting): deploy agents in containers where you can set OpenTelemetry variables at the environment level.
* [Monitoring](/docs/en/monitoring-usage): the complete reference for every environment variable, metric, and event the CLI emits.

---

## Agent SDK overview

- 官方原文：https://code.claude.com/docs/en/agent-sdk/overview.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-overview.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent SDK overview

> Build production AI agents with Claude Code as a library

An agent is an application that completes a task by planning its own steps and calling tools that read files, run commands, or edit code. The Agent SDK gives you the same tools, [agent loop](/docs/en/agent-sdk/agent-loop), and context management that power Claude Code, programmable in Python and TypeScript.

## Compare the Agent SDK to other Claude tools

The Agent SDK, the CLI, the Client SDK, and Managed Agents differ in who runs the agent, what comes built in, and how you reach it. Find the row that matches how you want to build and run yours.

| You want to                                                                                      | Use                                                                               | What you get                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Embed Claude Code's agent in your own Python or TypeScript application, in a process you operate | **Agent SDK**                                                                     | A library that runs the Claude Code binary, with Claude Code's [capabilities](#capabilities), such as built-in tools, permissions, sessions, and hooks.                                                                                                                                                                                                                                       |
| Do interactive development or run one-off tasks from a terminal                                  | [**Claude Code CLI**](/docs/en/overview)                                               | The terminal interface, built for daily interactive use.                                                                                                                                                                                                                                                                                                                                      |
| Call the Claude API directly from your own code                                                  | [**Client SDK**](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) | Direct access to the Claude API from any of the client SDK languages. You write the tool loop yourself, or let the client SDK's beta [tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner) drive it.                                                                                                                                                       |
| Have Anthropic host the agent, configured through the Claude API                                 | [**Managed Agents**](https://platform.claude.com/docs/en/managed-agents/overview) | A hosted agent harness that runs the agent loop, with sessions in an Anthropic-managed cloud sandbox or a [self-hosted sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) on your own infrastructure. Use it from the [SDK for your language](https://platform.claude.com/docs/en/managed-agents/quickstart#install-the-sdk), the `ant` CLI, or the REST API. |

To drive the same agent loop from a language other than Python or TypeScript, [run the CLI as a subprocess](/docs/en/headless) with the `-p` flag and `--output-format json`.

## Capabilities

These Claude Code capabilities are available in the SDK:

| Capability                   | What it does                                                                                 | Learn more                                                                                                                                                                                                     |
| ---------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Built-in tools               | Read, write, edit files, run commands, and search the web                                    | [Tools reference](/docs/en/tools-reference)                                                                                                                                                                         |
| Hooks                        | Run custom code at key points in the agent lifecycle                                         | [Hooks](/docs/en/agent-sdk/hooks)                                                                                                                                                                                   |
| Subagents                    | Spawn specialized agents for focused subtasks                                                | [Subagents](/docs/en/agent-sdk/subagents)                                                                                                                                                                           |
| MCP                          | Connect external tools and data sources via the Model Context Protocol                       | [MCP](/docs/en/agent-sdk/mcp)                                                                                                                                                                                       |
| Permissions                  | Control which tools run automatically, which need approval                                   | [Permissions](/docs/en/agent-sdk/permissions)                                                                                                                                                                       |
| Sessions                     | Maintain context across exchanges, resume or fork later                                      | [Sessions](/docs/en/agent-sdk/sessions)                                                                                                                                                                             |
| Skills, commands, and memory | Load automatically from your project's `.claude/` and from `~/.claude/`, same as Claude Code | [Skills](/docs/en/agent-sdk/skills), [Commands](/docs/en/agent-sdk/skills#commands-in-agent-sdk-sessions), [Memory](/docs/en/agent-sdk/modifying-system-prompts), [Configuration loading](/docs/en/agent-sdk/claude-code-features) |
| Plugins                      | Package skills, agents, hooks, and MCP servers, and load them by local path                  | [Plugins](/docs/en/agent-sdk/plugins)                                                                                                                                                                               |

## Get started

Follow the [Quickstart](/docs/en/agent-sdk/quickstart) to install the SDK, set your API key, and build your first agent, one that finds and fixes bugs in existing code.

<Note>
  Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Use the API key authentication methods described in the [Quickstart](/docs/en/agent-sdk/quickstart) instead.
</Note>

## Changelog

View the full changelog for SDK updates, bug fixes, and new features:

* **TypeScript SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/CHANGELOG.md)
* **Python SDK**: [view CHANGELOG.md](https://github.com/anthropics/claude-agent-sdk-python/blob/main/CHANGELOG.md)

## Report bugs

If you encounter bugs or issues with the Agent SDK:

* **TypeScript SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-typescript/issues)
* **Python SDK**: [report issues on GitHub](https://github.com/anthropics/claude-agent-sdk-python/issues)

## Branding guidelines

For partners integrating the Claude Agent SDK, use of Claude branding is optional. When referencing Claude in your product:

**Allowed:**

* "Claude Agent", preferred for dropdown menus
* "Claude", when within a menu already labeled "Agents"
* "\{YourAgentName} Powered by Claude", if you have an existing agent name

**Not permitted:**

* "Claude Code" or "Claude Code Agent"
* Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code or any Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).

## License and terms

Use of the Claude Agent SDK is governed by [Anthropic's Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), including when you use it to power products and services that you make available to your own customers and end users, except to the extent a specific component or dependency is covered by a different license as indicated in that component's LICENSE file.

## Next steps

These resources cover deeper technical detail and example projects for building with the Agent SDK.

* [Quickstart](/docs/en/agent-sdk/quickstart): build your first agent that finds and fixes bugs
* [Migration guide](/docs/en/agent-sdk/migration-guide): migrate from the Claude Code SDK packages to the Agent SDK
* [Agent loop](/docs/en/agent-sdk/agent-loop): how Claude plans, calls tools, and decides when a task is done
* [Example agents](https://github.com/anthropics/claude-agent-sdk-demos): demo apps for local development
* [TypeScript SDK](/docs/en/agent-sdk/typescript): full TypeScript API reference and examples
* [Python SDK](/docs/en/agent-sdk/python): full Python API reference and examples
* [Agent harness design](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code): how the Claude Code team uses dynamic workflows to orchestrate many subagents at once

---

## Configure permissions

- 官方原文：https://code.claude.com/docs/en/agent-sdk/permissions.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-permissions.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure permissions

> Control how your agent uses tools with permission modes, hooks, and declarative allow/deny rules.

The Claude Agent SDK provides permission controls to manage how Claude uses tools. Use permission modes and rules to define what's allowed automatically, and the [`canUseTool` callback](/docs/en/agent-sdk/user-input) to handle everything else at runtime.

## How permissions are evaluated

When Claude requests a tool, the SDK checks permissions in this order:

    Run [hooks](/docs/en/agent-sdk/hooks) first. A hook can deny the call outright or pass it on. A hook that returns `allow` does not skip the deny and ask rules below; those are evaluated regardless of the hook result. A `PreToolUse` hook allow also can't approve an `rm` or `rmdir` removal targeting a [critical path](/docs/en/permission-modes#critical-paths).

    Check `deny` rules (from `disallowed_tools` and [settings.json](/docs/en/settings-reference#permission-settings)). If a deny rule matches, the tool is blocked, even in `bypassPermissions` mode. Bare-name deny rules like `Bash` remove the tool from Claude's context before this evaluation begins, so only scoped rules like `Bash(rm *)` are checked at this step.

    Check `ask` rules from [settings.json](/docs/en/settings-reference#permission-settings). If an ask rule matches, the call falls through to your [`canUseTool` callback](/docs/en/agent-sdk/user-input) for confirmation, even in `bypassPermissions` mode.

    Tools that require user interaction behave the same way: `AskUserQuestion` and MCP tools whose server sets [`_meta["anthropic/requiresUserInteraction"]`](/docs/en/mcp#require-approval-for-a-specific-tool) always fall through to the callback, even when an allow rule matches. In `dontAsk` mode both cases are denied instead, because that mode never prompts. The MCP annotation requires Claude Code v2.1.199 or later.

    [claude.ai connector](/docs/en/mcp#organization-controls-on-connector-tools) tools your organization has set to `ask` also leave the flow at this step. Every call falls through to the callback, even in `bypassPermissions` mode and even when an allow rule matches. The callback receives the reason `Your organization requires approval for this tool`. In `dontAsk` mode the call is denied instead, because that mode never prompts.

    Apply the active [permission mode](#permission-modes):

    * In `bypassPermissions` mode, Claude Code approves everything that reaches this step except `rm` and `rmdir` removals targeting a [critical path](/docs/en/permission-modes#critical-paths), which fall through instead.
    * In `acceptEdits` mode, Claude Code approves the file operations listed under [Accept edits mode](#accept-edits-mode-acceptedits).
    * In `plan` mode, Claude Code sends file-edit and shell-write tools to your `canUseTool` callback regardless of allow rules, so write operations can't be auto-approved while planning.
    * In other modes, the request falls through.

    Check `allow` rules (from `allowed_tools` and settings.json). If a rule matches, the tool is approved. A call the tool approves on its own is resolved at this step too, with no rule needed: for example a file read inside your working directories or a [read-only Bash command](/docs/en/permissions#read-only-commands). `rm` and `rmdir` removals targeting a [critical path](/docs/en/permission-modes#critical-paths) are never approved by an allow rule: they reach your callback in the modes that prompt, go to the [classifier](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) in `auto` mode on Claude Code v2.1.218 or later, and are denied in `dontAsk` mode.

    If not resolved by any of the above, call your [`canUseTool` callback](/docs/en/agent-sdk/user-input) for a decision. In `dontAsk` mode, this step is skipped and the tool is denied.

    In the TypeScript SDK, if you set [`permissionPrompts: 'none'`](/docs/en/agent-sdk/typescript#options), your callback isn't called at this step. A [`PermissionRequest` hook](/docs/en/hooks#permissionrequest) still gets a chance to decide, and if it doesn't, Claude Code denies the call. The option requires Claude Code v2.1.259 or later.

<img src="https://mintcdn.com/claude-code/jYgs7qigNjO1Badj/images/agent-sdk/permissions-flow.svg?fit=max&auto=format&n=jYgs7qigNjO1Badj&q=85&s=c771ad9085b1277d3708027a49c744bc" className="dark:hidden" alt="Diagram of the six-step permission evaluation flow matching the steps above: a tool request passes through hooks, deny rules, ask rules, permission mode, allow rules, and canUseTool. Hooks, deny rules, and canUseTool can route down to Blocked; permission mode bypass, allow rules, and canUseTool can route up to Execute; ask rules route to canUseTool." width="1180" height="260" data-path="images/agent-sdk/permissions-flow.svg" />

<img src="https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/agent-sdk/permissions-flow-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=e53a91e9059cbf51852b7cedb4dd4251" className="hidden dark:block" alt="Diagram of the six-step permission evaluation flow matching the steps above: a tool request passes through hooks, deny rules, ask rules, permission mode, allow rules, and canUseTool. Hooks, deny rules, and canUseTool can route down to Blocked; permission mode bypass, allow rules, and canUseTool can route up to Execute; ask rules route to canUseTool." width="1180" height="260" data-path="images/agent-sdk/permissions-flow-dark.svg" />

If you pass a `canUseTool` callback in a configuration where the TypeScript SDK expects the evaluation order to auto-approve calls before the callback is consulted, the SDK emits a Node.js process warning once when the query is constructed. The warning's code is `CLAUDE_SDK_CAN_USE_TOOL_SHADOWED`. Two configurations trigger it:

* `permissionMode: 'bypassPermissions'`, which auto-approves every call that reaches the permission mode step apart from the [actions no mode auto-approves](/docs/en/permission-modes#actions-no-mode-auto-approves)
* Each bare `allowedTools` entry such as `"Read"`, which auto-approves that whole tool before the callback is consulted, apart from the [actions no mode auto-approves](/docs/en/permission-modes#actions-no-mode-auto-approves)

Entries with a specifier such as `Bash(ls *)` and the `acceptEdits` mode don't trigger it, and allow rules coming from settings files aren't visible to the check.

Listen with `process.on('warning', ...)` and match the code to log or suppress it. To gate every tool call regardless of mode and rules, use a [`PreToolUse` hook](/docs/en/agent-sdk/hooks) instead.

This page focuses on **allow and deny rules** and **permission modes**. For the other steps:

* **Hooks:** run custom code to allow, deny, or modify tool requests. See [Control execution with hooks](/docs/en/agent-sdk/hooks).
* **canUseTool callback:** prompt users for approval at runtime, when no earlier step resolves the call. See [Handle approvals and user input](/docs/en/agent-sdk/user-input).

## Allow and deny rules

`allowed_tools` and `disallowed_tools` (TypeScript: `allowedTools` / `disallowedTools`) add entries to the allow and deny rule lists in the evaluation flow above. If you name one of the [task-tracking tools](/docs/en/agent-sdk/todo-tracking#model-availability) in `allowed_tools`, Claude Code also opts the session in. Any other tool not listed in `allowed_tools` is still available to Claude, and a call to it that needs approval falls through to the permission mode. Deny rules behave differently depending on whether they name a tool or scope a pattern within one.

| Option                            | Effect                                                                                                                                                                                                                                         |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `allowed_tools=["Read", "Grep"]`  | `Read` and `Grep` are auto-approved. Other tools not listed here still exist, and calls to them that need approval fall through to the permission mode and `canUseTool`.                                                                       |
| `disallowed_tools=["Bash"]`       | The `Bash` tool definition is removed from the request. Claude does not see the tool and cannot attempt it.                                                                                                                                    |
| `disallowed_tools=["Bash(rm *)"]` | `Bash` stays available. Calls matching `rm *` [as written](/docs/en/permissions#bash-rule-limits) are denied in every permission mode, including `bypassPermissions`. Other `Bash` calls, including `/bin/rm`, fall through to the permission mode. |
| `disallowed_tools=["*"]`          | Every tool definition is removed from the request. Tool-name globs are supported in deny rules: `"*"` matches every tool and `"mcp__*"` matches every MCP tool across all servers.                                                             |

Allow rules accept tool-name globs only after a literal `mcp__<server>__` prefix. The server segment must be glob-free so the rule names a specific server you configured: `mcp__puppeteer__*` matches every tool from the `puppeteer` server, and `mcp__github__get_*` matches its `get_` tools. An unanchored entry like `allowed_tools=["*"]` or `allowed_tools=["mcp__*"]` is ignored with a startup warning and does not auto-approve anything.

Scoped rules for `Read` and `Edit` take a path pattern. `Edit(path)` rules govern all built-in tools that write files, including `Write` and `NotebookEdit`; a `Write(path)` rule is never matched by the file permission checks.

Use `//path` for an absolute filesystem path: a deny rule of `Edit(//secrets/**)` blocks writes anywhere under `/secrets` on disk. With a single leading slash, `Edit(/secrets/**)` anchors at the rule's source instead. For rules passed through `allowed_tools` or `disallowed_tools`, that means the session's working directory, so the rule doesn't block `/secrets` on disk. See [Read and Edit rules](/docs/en/permissions#read-and-edit) for the four anchor forms and how rules from settings files resolve.

<Warning>
  **Auto-approved tools never reach `canUseTool`.** A tool call approved at any earlier step, by `acceptEdits` or `bypassPermissions`, or by an allow rule, skips your `canUseTool` callback, so permission checks you put there are silently bypassed for that tool. `AskUserQuestion`, MCP tools marked [`_meta["anthropic/requiresUserInteraction"]`](/docs/en/mcp#require-approval-for-a-specific-tool), connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), and `rm` and `rmdir` removals targeting a [critical path](/docs/en/permission-modes#critical-paths) still reach the callback, even when an allow rule matches. In `auto` mode, critical-path removals go to the [classifier](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) instead of the callback, while the other calls listed here still reach it; the classifier routing requires Claude Code v2.1.218 or later. In `dontAsk` mode these calls are denied instead, without invoking the callback.

  Coverage depends on the entry's form: a bare name like `Read` or `mcp__github__get_issue` auto-approves every call to that tool apart from the exceptions above, while a scoped rule like `Bash(npm test *)` auto-approves only matching calls, and other `Bash` calls that need approval still fall through to the callback. For checks that must run on every tool call, use a [`PreToolUse` hook](/docs/en/agent-sdk/hooks): hooks run before every other step, and a hook deny applies even in `bypassPermissions` mode.
</Warning>

For a locked-down agent, pair `allowedTools` with `permissionMode: "dontAsk"`:

```typescript theme={null}
const options = {
  allowedTools: ["Read", "Glob", "Grep"],
  permissionMode: "dontAsk"
};
```

Listed tools are approved, apart from the [actions no mode auto-approves](/docs/en/permission-modes#actions-no-mode-auto-approves), and every other call that would prompt is denied instead. Calls that need no approval in `default` mode run whether or not you list them, such as [read-only Bash commands](/docs/en/permissions#read-only-commands), tools like `Agent` that don't ask before running, and file reads inside your working directories. To put a tool out of Claude's reach entirely, add its bare name to `disallowedTools`.

<Warning>
  **`allowed_tools` does not constrain `bypassPermissions`.** `allowed_tools` pre-approves the tools you list. Other unlisted tools are not matched by any allow rule and fall through to the permission mode, where `bypassPermissions` approves them. Setting `allowed_tools=["Read"]` alongside `permission_mode="bypassPermissions"` still approves every tool, including `Bash`, `Write`, and `Edit`. If you need `bypassPermissions` but want specific tools blocked, use `disallowed_tools`.
</Warning>

You can also configure allow, deny, and ask rules declaratively in `.claude/settings.json`. These rules are read when the `project` setting source is enabled, which it is for default `query()` options. If you set `setting_sources` (TypeScript: `settingSources`) explicitly, include `"project"` for them to apply. See [Permission settings](/docs/en/settings-reference#permission-settings) for the rule syntax.

## Permission modes

Permission modes provide global control over how Claude uses tools. You can set the permission mode when calling `query()` or change it dynamically during streaming sessions.

### Available modes

The SDK supports these permission modes:

| Mode                | Description                  | Tool behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :------------------ | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default`           | Standard permission behavior | No mode-based auto-approvals; calls that need approval and match no allow rule trigger your `canUseTool` callback                                                                                                                                                                                                                                                                                                                                                                |
| `dontAsk`           | Deny instead of prompting    | Any call that would otherwise prompt is denied. Calls approved by `allowed_tools` or rules run, and so do calls that need no approval in `default` mode; connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools) and tools that require user interaction are denied even if you've pre-approved them, as are `rm` and `rmdir` removals targeting a [critical path](/docs/en/permission-modes#critical-paths). `canUseTool` is never called |
| `acceptEdits`       | Auto-accept file edits       | File edits and [filesystem operations](#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) are automatically approved                                                                                                                                                                                                                                                                                                                                                    |
| `bypassPermissions` | Bypass permission checks     | Tools run without permission prompts, except for the [actions no mode auto-approves](/docs/en/permission-modes#actions-no-mode-auto-approves). Use with caution                                                                                                                                                                                                                                                                                                                       |
| `plan`              | Planning mode                | Claude explores and plans without editing your source files; file edits are never auto-approved and prompt through your `canUseTool` callback                                                                                                                                                                                                                                                                                                                                    |
| `auto`              | Model-classified approvals   | A model classifier approves or denies permission prompts. See [Auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for availability                                                                                                                                                                                                                                                                                                                                |

<Warning>
  **Subagent inheritance:** A subagent runs in the parent session's permission mode unless you set `permissionMode` on its [`AgentDefinition`](/docs/en/agent-sdk/typescript#agentdefinition) and the parent session is in `default`, `dontAsk`, or `plan` mode. Even then, Claude Code never applies a `"bypassPermissions"` value. A subagent runs in `bypassPermissions` mode only when the parent session itself does. The `bypassPermissions` exception requires Claude Code v2.1.267 or later.

  Subagents may have different system prompts and less constrained behavior than your main agent, so inheriting `bypassPermissions` grants them full, autonomous system access. The [actions no mode auto-approves](/docs/en/permission-modes#actions-no-mode-auto-approves) still apply.
</Warning>

### Set permission mode

You can set the permission mode once when starting a query, or change it dynamically while the session is active.

  <Tab title="At query time">
    Pass `permission_mode` (Python) or `permissionMode` (TypeScript) when creating a query. This mode applies for the entire session unless changed dynamically.

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      from claude_agent_sdk import query, ClaudeAgentOptions

      async def main():
          async for message in query(
              prompt="Help me refactor this code",
              options=ClaudeAgentOptions(
                  permission_mode="default",  # Set the mode here
              ),
          ):
              if hasattr(message, "result"):
                  print(message.result)

      asyncio.run(main())
      ```

      ```typescript TypeScript theme={null}

      async function main() {
        for await (const message of query({
          prompt: "Help me refactor this code",
          options: {
            permissionMode: "default" // Set the mode here
          }
        })) {
          if ("result" in message) {
            console.log(message.result);
          }
        }
      }

      main();
      ```
    </CodeGroup>
  </Tab>

  <Tab title="During streaming">
    Call `set_permission_mode()` (Python) or `setPermissionMode()` (TypeScript) to change the mode mid-session. The new mode takes effect immediately for all subsequent tool requests. This lets you start restrictive and loosen permissions as trust builds, for example switching to `acceptEdits` after reviewing Claude's initial approach.

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

      async def main():
          async with ClaudeSDKClient(
              options=ClaudeAgentOptions(
                  permission_mode="default",  # Start in default mode
              )
          ) as client:
              await client.query("Help me refactor this code")

              # Change mode dynamically mid-session
              await client.set_permission_mode("acceptEdits")

              # Process messages with the new permission mode
              async for message in client.receive_response():
                  if hasattr(message, "result"):
                      print(message.result)

      asyncio.run(main())
      ```

      ```typescript TypeScript theme={null}

      async function main() {
        const q = query({
          prompt: "Help me refactor this code",
          options: {
            permissionMode: "default" // Start in default mode
          }
        });

        // Change mode dynamically mid-session
        await q.setPermissionMode("acceptEdits");

        // Process messages with the new permission mode
        for await (const message of q) {
          if ("result" in message) {
            console.log(message.result);
          }
        }
      }

      main();
      ```
    </CodeGroup>
  </Tab>

### Mode details

#### Accept edits mode (`acceptEdits`)

Auto-approves file operations so Claude can edit code without prompting. Other tools (like Bash commands that aren't filesystem operations) still require normal permissions.

**Auto-approved operations:**

* File edits (Edit, Write tools)
* Filesystem commands: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`

Both apply only to paths inside the working directory or `additionalDirectories`. In `acceptEdits` mode, Claude Code doesn't auto-approve the request when Claude:

* Works on a path outside that scope
* Writes to a protected path
* Removes a [critical path](/docs/en/permission-modes#critical-paths) with `rm` or `rmdir`

**Use when:** you trust Claude's edits and want faster iteration, such as during prototyping or when working in an isolated directory.

#### Don't ask mode (`dontAsk`)

Converts any permission prompt into a denial, without calling `canUseTool`. Tools pre-approved by `allowed_tools`, `settings.json` allow rules, or a hook run as normal, and so do calls that need no approval in `default` mode, such as file reads inside your working directories and calls to `Agent`. Connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), tools that require user interaction, and `rm` and `rmdir` removals targeting a [critical path](/docs/en/permission-modes#critical-paths) are denied even when an allow rule matches. A `PreToolUse` hook allow doesn't clear a critical-path removal either.

**Use when:** you want a fixed, explicit tool surface for a headless agent and prefer a hard deny over silent reliance on `canUseTool` being absent.

#### Bypass permissions mode (`bypassPermissions`)

Auto-approves tool uses without prompting, except the cases listed in the warning below. Hooks still execute and can block operations if needed.

<Warning>
  Use with extreme caution. Claude has full system access in this mode. Only use in controlled environments where you trust all possible operations.

  `allowed_tools` does not constrain this mode. Every tool is approved, not just the ones you listed. These controls still apply:

  * Deny rules, explicit `ask` rules, and hooks are evaluated before the mode check and can still block a tool.
  * Connector tools [your organization set to `ask`](/docs/en/mcp#organization-controls-on-connector-tools), tools that require user interaction, and `rm` and `rmdir` removals targeting a [critical path](/docs/en/permission-modes#critical-paths) still fall through to your `canUseTool` callback.
  * The [cross-session messaging safeguards](/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode) still apply.
</Warning>

#### Plan mode (`plan`)

Claude explores the codebase and produces a plan without editing your source files. Read-only tools run as they do in the `default` permission mode.

File edits are never auto-approved in plan mode, even when an allow rule matches. They prompt through your `canUseTool` callback instead. On Claude Code v2.1.212 or later, shell commands that modify files, such as `touch` and `rm`, reach your `canUseTool` callback the same way.

If you set `allowDangerouslySkipPermissions: true` alongside `permissionMode: 'plan'`, file edits and shell commands that modify files still reach your `canUseTool` callback. The option lets you switch to `bypassPermissions` later with `setPermissionMode()`.

Claude may use `AskUserQuestion` to clarify requirements before finalizing the plan. See [Handle approvals and user input](/docs/en/agent-sdk/user-input#handle-clarifying-questions) for handling these prompts.

**Use when:** you want Claude to propose changes without executing them, such as during code review or when you need to approve changes before they're made.

## Related resources

For the other steps in the permission evaluation flow:

* [Handle approvals and user input](/docs/en/agent-sdk/user-input): interactive approval prompts and clarifying questions
* [Hooks guide](/docs/en/agent-sdk/hooks): run custom code at key points in the agent lifecycle
* [Permission rules](/docs/en/settings-reference#permission-settings): declarative allow/deny rules in `settings.json`

---

## Plugins in the SDK

- 官方原文：https://code.claude.com/docs/en/agent-sdk/plugins.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-plugins.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins in the SDK

> Load custom plugins to extend Claude Code with skills, agents, hooks, and MCP servers through the Agent SDK

Plugins let you extend Claude Code with custom functionality that can be shared across projects. Through the Agent SDK, you can programmatically load plugins from local directories to add capabilities to your agent sessions. A plugin can include:

* **Skills**: capabilities Claude invokes autonomously when relevant. You can also invoke a plugin skill directly with `/plugin-name:skill-name`.
* **Agents**: specialized subagents for specific tasks
* **Hooks**: event handlers that respond to tool use and other events
* **MCP servers**: external tool integrations via Model Context Protocol

For complete information on plugin structure and how to create plugins, see [Plugins](/docs/en/plugins).

## Loading plugins

Load plugins by providing their local file system paths in your options configuration. The `type` field must be `"local"`, the only value the SDK accepts. The SDK supports loading multiple plugins from different locations.

To use a plugin distributed through a [marketplace](/docs/en/plugin-marketplaces) or remote repository, download it first and provide the local directory path. For the directory layout a plugin needs, see the [Plugin structure reference](#plugin-structure-reference) below.

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Hello",
    options: {
      plugins: [
        { type: "local", path: "./my-plugin" },
        { type: "local", path: "/absolute/path/to/another-plugin" }
      ]
    }
  })) {
    // Plugin commands, agents, and other features are now available
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions

  async def main():
      async for message in query(
          prompt="Hello",
          options=ClaudeAgentOptions(
              plugins=[
                  {"type": "local", "path": "./my-plugin"},
                  {"type": "local", "path": "/absolute/path/to/another-plugin"},
              ]
          ),
      ):
          # Plugin commands, agents, and other features are now available
          pass

  asyncio.run(main())
  ```
</CodeGroup>

### Path specifications

Plugin paths can be:

* **Relative paths**: resolved relative to the `cwd` option (for example, `"./plugins/my-plugin"`)
* **Absolute paths**: full file system paths (for example, `"/home/user/plugins/my-plugin"`)

<Note>
  The path should point to the plugin's root directory: the parent of `skills/`, `agents/`, `hooks/`, `commands/`, or `.claude-plugin/`.
</Note>

## Verifying plugin installation

When plugins load successfully, they appear in the system initialization message. You can verify that your plugins are available:

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Hello",
    options: {
      plugins: [{ type: "local", path: "./my-plugin" }]
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      // Check loaded plugins
      console.log("Plugins:", message.plugins);
      // Example: [{ name: "my-plugin", path: "/absolute/path/to/my-plugin" }]

      // Plugin skills appear with the plugin name as a prefix
      console.log("Skills:", message.skills);
      // Example: ["my-plugin:greet"]

      // Plugin commands use the same prefix, and skills appear here too
      console.log("Commands:", message.slash_commands);
      // Example: ["compact", "context", "my-plugin:custom-command", "my-plugin:greet"]
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage

  async def main():
      async for message in query(
          prompt="Hello",
          options=ClaudeAgentOptions(
              plugins=[{"type": "local", "path": "./my-plugin"}]
          ),
      ):
          if isinstance(message, SystemMessage) and message.subtype == "init":
              # Check loaded plugins
              print("Plugins:", message.data.get("plugins"))
              # Example: [{"name": "my-plugin", "path": "/absolute/path/to/my-plugin"}]

              # Plugin skills appear with the plugin name as a prefix
              print("Skills:", message.data.get("skills"))
              # Example: ["my-plugin:greet"]

              # Plugin commands use the same prefix, and skills appear here too
              print("Commands:", message.data.get("slash_commands"))
              # Example: ["compact", "context", "my-plugin:custom-command", "my-plugin:greet"]

  asyncio.run(main())
  ```
</CodeGroup>

## Using plugin skills

Skills from plugins are automatically namespaced with the plugin name to avoid conflicts. To invoke one directly, send `/plugin-name:skill-name` as the prompt.

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Load a plugin with a custom /greet skill
  for await (const message of query({
    prompt: "/my-plugin:greet", // Use plugin skill with namespace
    options: {
      plugins: [{ type: "local", path: "./my-plugin" }]
    }
  })) {
    // Claude executes the custom greeting skill from the plugin
    if (message.type === "assistant") {
      console.log(message.message.content);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock

  async def main():
      # Load a plugin with a custom /greet skill
      async for message in query(
          prompt="/my-plugin:greet",  # Use plugin skill with namespace
          options=ClaudeAgentOptions(
              plugins=[{"type": "local", "path": "./my-plugin"}]
          ),
      ):
          # Claude executes the custom greeting skill from the plugin
          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if isinstance(block, TextBlock):
                      print(f"Claude: {block.text}")

  asyncio.run(main())
  ```
</CodeGroup>

<Note>
  If you installed a plugin via the CLI (for example, `/plugin install my-plugin@marketplace`), you can still use it in the SDK by providing its installation path. Check `~/.claude/plugins/` for CLI-installed plugins.
</Note>

## Complete example

Here's a full example demonstrating plugin loading and usage:

<CodeGroup>
  ```typescript TypeScript theme={null}

  async function runWithPlugin() {
    const pluginPath = fileURLToPath(new URL("./plugins/my-plugin", import.meta.url));

    console.log("Loading plugin from:", pluginPath);

    for await (const message of query({
      prompt: "What custom commands do you have available?",
      options: {
        plugins: [{ type: "local", path: pluginPath }],
        maxTurns: 3
      }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        console.log("Loaded plugins:", message.plugins);
        console.log("Available skills:", message.skills);
        console.log("Available commands:", message.slash_commands);
      }

      if (message.type === "assistant") {
        console.log("Assistant:", message.message.content);
      }
    }
  }

  runWithPlugin().catch(console.error);
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  """Example demonstrating how to use plugins with the Agent SDK."""

  import asyncio
  from pathlib import Path

  from claude_agent_sdk import (
      AssistantMessage,
      ClaudeAgentOptions,
      SystemMessage,
      TextBlock,
      query,
  )

  async def run_with_plugin():
      """Example using a custom plugin."""
      plugin_path = Path(__file__).parent / "plugins" / "my-plugin"

      print(f"Loading plugin from: {plugin_path}")

      options = ClaudeAgentOptions(
          plugins=[{"type": "local", "path": str(plugin_path)}],
          max_turns=3,
      )

      async for message in query(
          prompt="What custom commands do you have available?", options=options
      ):
          if isinstance(message, SystemMessage) and message.subtype == "init":
              print(f"Loaded plugins: {message.data.get('plugins')}")
              print(f"Available skills: {message.data.get('skills')}")
              print(f"Available commands: {message.data.get('slash_commands')}")

          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if isinstance(block, TextBlock):
                      print(f"Assistant: {block.text}")

  if __name__ == "__main__":
      asyncio.run(run_with_plugin())
  ```
</CodeGroup>

## Plugin structure reference

A plugin directory typically contains a `.claude-plugin/plugin.json` manifest file. The manifest is optional. When omitted, Claude Code auto-discovers components from the directory layout. The directory can include:

```text theme={null}
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest (optional, components auto-discovered without it)
├── skills/                   # Agent Skills (invoked autonomously or via /plugin-name:skill-name)
│   └── my-skill/
│       └── SKILL.md
├── commands/                 # Skills as flat .md files
│   └── custom-cmd.md
├── agents/                   # Custom agents
│   └── specialist.md
├── hooks/                    # Event handlers
│   └── hooks.json
└── .mcp.json                # MCP server definitions
```

<Note>
  The `commands/` directory holds skills as flat Markdown files. Use `skills/` for new plugins. Claude Code supports both locations.
</Note>

## Multiple plugin sources

Combine plugins from different locations:

```typescript theme={null}

plugins: [
  { type: "local", path: "./local-plugin" },
  {
    type: "local",
    path: path.join(os.homedir(), ".claude", "custom-plugins", "shared-plugin")
  }
];
```

<Note>
  The SDK doesn't expand tilde paths like `~/plugins`. If a plugin path doesn't exist, the SDK skips that plugin and the session continues, so check the `plugins` list in the init message to confirm each plugin loaded.
</Note>

## Troubleshooting

### Plugin not loading

If your plugin doesn't appear in the init message:

1. **Check the path**: ensure the path points to the plugin root directory, the parent of `skills/`, `agents/`, `hooks/`, `commands/`, or `.claude-plugin/`
2. **Validate plugin.json**: if your plugin includes a manifest, ensure it has valid JSON syntax
3. **Check file permissions**: ensure the plugin directory is readable
4. **Confirm the directory exists**: the SDK skips a nonexistent path, and the plugin doesn't appear in the init message's `plugins` list

### Skills not appearing

If plugin skills don't work:

1. **Use the namespace**: invoke plugin skills as `/plugin-name:skill-name`
2. **Check init message**: verify the skill appears in the `skills` list with the correct namespace
3. **Validate skill files**: ensure each skill has a `SKILL.md` file in its own subdirectory under `skills/`, for example `skills/my-skill/SKILL.md`

## See also

* [Plugins](/docs/en/plugins) - Complete plugin development guide
* [Plugins reference](/docs/en/plugins-reference) - Technical specifications
* [Commands](/docs/en/agent-sdk/skills#dispatch-commands-by-name) - Dispatching commands in the SDK
* [Subagents](/docs/en/agent-sdk/subagents) - Working with specialized agents
* [Skills](/docs/en/agent-sdk/skills) - Using Agent Skills

---

## Quickstart

- 官方原文：https://code.claude.com/docs/en/agent-sdk/quickstart.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-quickstart.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Get started with the Python or TypeScript Agent SDK to build AI agents that work autonomously

Use the Agent SDK to build an AI agent that reads your code, finds bugs, and fixes them, all without manual intervention.

**What you'll do:**

1. Set up a project with the Agent SDK
2. Create a file with some buggy code
3. Run an agent that finds and fixes the bugs automatically

## Prerequisites

* **Node.js 18+** or **Python 3.10+**
* An **Anthropic account**. If you don't have one, [sign up here](https://platform.claude.com/).

## Setup

    Create a new directory for this quickstart:

    ```bash theme={null}
    mkdir my-agent
    cd my-agent
    ```

    For your own projects, you can run the SDK from any folder; it will have access to files in that directory and its subdirectories by default.

    Install the Agent SDK package for your language:

      <Tab title="TypeScript (new project)">
        ```bash theme={null}
        npm init -y
        npm pkg set type=module
        npm install @anthropic-ai/claude-agent-sdk
        npm install --save-dev tsx
        ```

        Setting `"type": "module"` in `package.json` lets your agent script use top-level `await`, and [tsx](https://tsx.hirok.io) runs TypeScript files directly. npm prints `added N packages` when the install succeeds.
      </Tab>

      <Tab title="TypeScript (existing project)">
        ```bash theme={null}
        npm install @anthropic-ai/claude-agent-sdk
        npm install --save-dev tsx
        ```

        [tsx](https://tsx.hirok.io) runs TypeScript files directly. If your project uses CommonJS, name your agent script `agent.mts` instead of `agent.ts`. The `.mts` extension makes tsx treat the file as an ES module, so top-level `await` works without converting your whole project to ES modules. Use `agent.mts` in place of `agent.ts` in the create and run steps later in this quickstart.
      </Tab>

      <Tab title="Python (uv)">
        [Install uv](https://docs.astral.sh/uv/), a fast Python package manager that handles virtual environments automatically. Then initialize a project and add the SDK:

        ```bash theme={null}
        uv init
        uv add claude-agent-sdk
        ```
      </Tab>

      <Tab title="Python (pip)">
        Create and activate a virtual environment, then install the package.

        On macOS or Linux:

        ```bash theme={null}
        python3 -m venv .venv
        source .venv/bin/activate
        pip install claude-agent-sdk
        ```

        On Windows:

        ```powershell theme={null}
        py -m venv .venv
        .venv\Scripts\Activate.ps1
        pip install claude-agent-sdk
        ```

        If PowerShell blocks `Activate.ps1` with an execution policy error, run `Set-ExecutionPolicy -Scope Process RemoteSigned` first.
      </Tab>

    <Note>
      Both the TypeScript and Python SDKs bundle a native Claude Code binary, so most installs need no separate Claude Code install. Some installs have no bundled binary:

      * If pip installs the Python SDK's source distribution instead of a platform wheel, for example on ARM64 Windows, no binary is bundled. [Install Claude Code natively](/docs/en/setup#install-claude-code). The Python SDK finds it on your `PATH`.
      * The TypeScript SDK installs its binary through npm optional dependencies, so an install that skips them, for example `npm ci --omit=optional`, gets no binary even on a supported platform. Reinstall without skipping optional dependencies, or [install Claude Code natively](/docs/en/setup#install-claude-code) and set `pathToClaudeCodeExecutable` to its path.
    </Note>

    Get an API key from the [Claude Console](https://platform.claude.com/), then set it as an environment variable in the shell where you'll run your agent:

      <Tab title="macOS / Linux">
        ```bash theme={null}
        export ANTHROPIC_API_KEY=your-api-key
        ```
      </Tab>

      <Tab title="Windows (PowerShell)">
        ```powershell theme={null}
        $env:ANTHROPIC_API_KEY = "your-api-key"
        ```
      </Tab>

    The SDK reads the key from the environment of the process that runs your agent; it doesn't load `.env` files automatically. If you keep the key in a `.env` file, load it yourself, for example with the `dotenv` package, before calling the SDK.

    The SDK also supports authentication via third-party API providers:

    * **Amazon Bedrock**: set `CLAUDE_CODE_USE_BEDROCK=1` environment variable and configure AWS credentials
    * **Claude Platform on AWS**: set `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` and `ANTHROPIC_AWS_WORKSPACE_ID`, then configure AWS credentials
    * **Google Cloud's Agent Platform**: set `CLAUDE_CODE_USE_VERTEX=1` environment variable and configure Google Cloud credentials
    * **Microsoft Foundry**: set `CLAUDE_CODE_USE_FOUNDRY=1` environment variable and configure Azure credentials

    See the setup guides for [Amazon Bedrock](/docs/en/amazon-bedrock), [Claude Platform on AWS](/docs/en/claude-platform-on-aws), [Google Cloud's Agent Platform](/docs/en/google-vertex-ai), or [Microsoft Foundry](/docs/en/microsoft-foundry) for details.

    <Note>
      Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead.
    </Note>

## Create a buggy file

This quickstart walks you through building an agent that can find and fix bugs in code. First, you need a file with some intentional bugs for the agent to fix. Create `utils.py` in the `my-agent` directory and paste the following code:

```python theme={null}
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def get_user_name(user):
    return user["name"].upper()
```

This code has two bugs:

1. `calculate_average([])` crashes with division by zero
2. `get_user_name(None)` crashes with a TypeError

## Build an agent that finds and fixes bugs

Create `agent.py` if you're using the Python SDK, or `agent.ts` for TypeScript. Use `agent.mts` instead if your existing project uses CommonJS:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

  async def main():
      # Agentic loop: streams messages as Claude works
      async for message in query(
          prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Edit", "Glob"],  # Auto-approve these tools
              permission_mode="acceptEdits",  # Auto-approve file edits
          ),
      ):
          # Print human-readable output
          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if hasattr(block, "text"):
                      print(block.text)  # Claude's reasoning
                  elif hasattr(block, "name"):
                      print(f"Tool: {block.name}")  # Tool being called
          elif isinstance(message, ResultMessage):
              print(f"Done: {message.subtype}")  # Final result

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Agentic loop: streams messages as Claude works
  for await (const message of query({
    prompt: "Review utils.py for bugs that would cause crashes. Fix any issues you find.",
    options: {
      allowedTools: ["Read", "Edit", "Glob"], // Auto-approve these tools
      permissionMode: "acceptEdits" // Auto-approve file edits
    }
  })) {
    // Print human-readable output
    if (message.type === "assistant" && message.message?.content) {
      for (const block of message.message.content) {
        if ("text" in block) {
          console.log(block.text); // Claude's reasoning
        } else if ("name" in block) {
          console.log(`Tool: ${block.name}`); // Tool being called
        }
      }
    } else if (message.type === "result") {
      console.log(`Done: ${message.subtype}`); // Final result
    }
  }
  ```
</CodeGroup>

This code has three main parts:

1. **`query`**: the main entry point that creates the agentic loop. It returns an async iterator, so you use `async for` to stream messages as Claude works. See the full API in the [Python](/docs/en/agent-sdk/python#query) or [TypeScript](/docs/en/agent-sdk/typescript#query) SDK reference.

2. **`prompt`**: what you want Claude to do. Claude figures out which tools to use based on the task.

3. **`options`**: configuration for the agent. This example uses `allowedTools` to pre-approve `Read`, `Edit`, and `Glob`, and `permissionMode: "acceptEdits"` to auto-approve file changes. Other options include `systemPrompt`, `mcpServers`, and more. See all options for [Python](/docs/en/agent-sdk/python#claudeagentoptions) or [TypeScript](/docs/en/agent-sdk/typescript#options).

The `async for` loop keeps running as Claude thinks, calls tools, observes results, and decides what to do next. Each iteration yields a message: Claude's reasoning, a tool call, a tool result, or the final outcome. The SDK handles the orchestration, tool execution, context management, and retries, so you consume the stream. The loop ends when Claude finishes the task or hits an error.

The message handling inside the loop filters for human-readable output. Without filtering, you'd see raw message objects including system initialization and internal state, which is useful for debugging but noisy otherwise.

<Note>
  This example uses streaming to show progress in real-time. If you don't need live output (for example, for background jobs or CI pipelines), you can collect all messages at once. See [Streaming vs. single-turn mode](/docs/en/agent-sdk/streaming-vs-single-mode) for details.
</Note>

### Run your agent

Your agent is ready. Run it with the following command:

  <Tab title="TypeScript">
    ```bash theme={null}
    npx tsx agent.ts
    ```

    If you named your script `agent.mts`, run `npx tsx agent.mts` instead.
  </Tab>

  <Tab title="Python (uv)">
    ```bash theme={null}
    uv run agent.py
    ```
  </Tab>

  <Tab title="Python (pip)">
    With your virtual environment still activated:

    ```bash theme={null}
    python agent.py
    ```
  </Tab>

As it works, the agent prints its reasoning and each tool it calls, ending with `Done: success`. After running, check `utils.py`. You'll see defensive code handling empty lists and null users. Your agent autonomously:

1. **Read** `utils.py` to understand the code
2. **Analyzed** the logic and identified edge cases that would crash
3. **Edited** the file to add proper error handling

This is what makes the Agent SDK different: Claude executes tools directly instead of asking you to implement them.

<Note>
  If you see an authentication error such as `Not logged in` or `Invalid API key`, make sure you've set the `ANTHROPIC_API_KEY` environment variable in the shell where you run your agent. The SDK doesn't load `.env` files automatically. See the [full troubleshooting guide](/docs/en/troubleshooting) for more help.
</Note>

### Try other prompts

Now that your agent is set up, try some different prompts:

* `"Add docstrings to all functions in utils.py"`
* `"Add type hints to all functions in utils.py"`
* `"Create a README.md documenting the functions in utils.py"`

### Customize your agent

You can modify your agent's behavior by changing the options. Here are a few examples:

**Add web search capability:**

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      allowed_tools=["Read", "Edit", "Glob", "WebSearch"], permission_mode="acceptEdits"
  )
  ```

  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      allowedTools: ["Read", "Edit", "Glob", "WebSearch"],
      permissionMode: "acceptEdits"
    }
  };
  ```
</CodeGroup>

**Give Claude a custom system prompt:**

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      allowed_tools=["Read", "Edit", "Glob"],
      permission_mode="acceptEdits",
      system_prompt="You are a senior Python developer. Always follow PEP 8 style guidelines.",
  )
  ```

  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      allowedTools: ["Read", "Edit", "Glob"],
      permissionMode: "acceptEdits",
      systemPrompt: "You are a senior Python developer. Always follow PEP 8 style guidelines."
    }
  };
  ```
</CodeGroup>

**Run commands in the terminal:**

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      allowed_tools=["Read", "Edit", "Glob", "Bash"], permission_mode="acceptEdits"
  )
  ```

  ```typescript TypeScript hidelines={1,-1} theme={null}
  const _ = {
    options: {
      allowedTools: ["Read", "Edit", "Glob", "Bash"],
      permissionMode: "acceptEdits"
    }
  };
  ```
</CodeGroup>

With `Bash` enabled, try: `"Write unit tests for utils.py, run them, and fix any failures"`

Each of these snippets sets fields on the same options object. For more information, see [Configure your agent](/docs/en/agent-sdk/configuration).

## Key concepts

**Tools** control what your agent can do:

| Tools                                  | What the agent can do   |
| -------------------------------------- | ----------------------- |
| `Read`, `Glob`, `Grep`                 | Read-only analysis      |
| `Read`, `Edit`, `Glob`                 | Analyze and modify code |
| `Read`, `Edit`, `Bash`, `Glob`, `Grep` | Full automation         |

**Permission modes** control how much human oversight you want. The SDK evaluates the active mode together with your allow and deny rules in a fixed order, described in [How permissions are evaluated](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated). For the full list of modes, their behavior, and when to use each, see [Permission mode in How the agent loop works](/docs/en/agent-sdk/agent-loop#permission-mode).

## Next steps

Now that you've created your first agent, learn how to extend its capabilities and tailor it to your use case:

* **[Configure your agent](/docs/en/agent-sdk/configuration)**: compose the options object and find the page that covers each setting
* **[Permissions](/docs/en/agent-sdk/permissions)**: control what your agent can do and when it needs approval
* **[Hooks](/docs/en/agent-sdk/hooks)**: run custom code before or after tool calls
* **[Sessions](/docs/en/agent-sdk/sessions)**: build multi-turn agents that maintain context
* **[MCP servers](/docs/en/agent-sdk/mcp)**: connect to databases, browsers, APIs, and other external systems
* **[Hosting](/docs/en/agent-sdk/hosting)**: deploy agents to Docker, cloud, and CI/CD
* **[Example agents](https://github.com/anthropics/claude-agent-sdk-demos)**: see complete examples: email assistant, research agent, and more
* **[Troubleshooting](/docs/en/agent-sdk/troubleshooting)**: fix Agent SDK errors by the exact message you see

---

## Securely deploying AI agents

- 官方原文：https://code.claude.com/docs/en/agent-sdk/secure-deployment.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-secure-deployment.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Securely deploying AI agents

> A guide to securing Claude Code and Agent SDK deployments with isolation, credential management, and network controls

Claude Code and the Agent SDK can execute code, access files, and interact with external services on your behalf.

Unlike traditional software that follows predetermined code paths, these tools generate their actions dynamically based on context and goals. This flexibility is what makes them useful, but it also means their behavior can be influenced by the content they process: files, webpages, or user input. This is sometimes called prompt injection. For example, if a repository's README contains unusual instructions, Claude Code might incorporate those into its actions in ways the operator didn't anticipate. This guide covers practical ways to reduce this risk.

Not every deployment needs maximum security. A developer running Claude Code on their laptop has different requirements than a company processing customer data in a multi-tenant environment. This guide presents options ranging from Claude Code's built-in security features to hardened production architectures, so you can choose what fits your situation.

## Threat model

Agents can take unintended actions due to prompt injection (instructions embedded in content they process) or model error. Claude models are designed to resist this; see the [model overview](https://platform.claude.com/docs/en/about-claude/models/overview) and the system card for the model you deploy for evaluation details.

Defense in depth is still good practice though. For example, if an agent processes a malicious file that instructs it to send customer data to an external server, network controls can block that request entirely.

## Built-in security features

Claude Code includes several security features that address common concerns. See the [security documentation](/docs/en/security) for full details.

* **Permissions system**: Every tool and bash command can be configured to allow, block, or prompt the user for approval. Use glob patterns to create rules like "allow all npm commands" or "block any command with sudo". Organizations can set policies that apply across all users. See [permissions](/docs/en/permissions).
* **Command parsing for permissions**: Before executing bash commands, Claude Code parses them into an AST and matches the result against your permission rules. Commands that cannot be parsed cleanly, or that do not match an allow rule, require explicit approval. A small set of constructs such as `eval` always require approval regardless of allow rules. This is a permission gate, not a sandbox; apart from built-in safety checks such as the [critical-path check](/docs/en/permission-modes#critical-paths) on `rm` and `rmdir` and the [protected paths](/docs/en/permission-modes#protected-paths) list, it does not infer whether a command is dangerous from its target path or effects.
* **Web search summarization**: Search results are summarized rather than passing raw content directly into the context, reducing the risk of prompt injection from malicious web content.
* **Sandbox mode**: Bash commands can run in a sandboxed environment that restricts filesystem and network access. See the [sandboxing documentation](/docs/en/sandboxing) for details.

## Security principles

For deployments that require additional hardening beyond Claude Code's defaults, these principles guide the available options.

### Security boundaries

A security boundary separates components with different trust levels. For high-security deployments, you can place sensitive resources (like credentials) outside the boundary containing the agent. If something goes wrong in the agent's environment, resources outside that boundary remain protected.

For example, rather than giving an agent direct access to an API key, you could run a proxy outside the agent's environment that injects the key into requests. The agent can make API calls, but it never sees the credential itself. This pattern is useful for multi-tenant deployments or when processing untrusted content.

### Least privilege

When needed, you can restrict the agent to only the capabilities required for its specific task:

| Resource            | Restriction options                             |
| ------------------- | ----------------------------------------------- |
| Filesystem          | Mount only needed directories, prefer read-only |
| Network             | Restrict to specific endpoints via proxy        |
| Credentials         | Inject via proxy rather than exposing directly  |
| System capabilities | Drop Linux capabilities in containers           |

### Defense in depth

For high-security environments, layering multiple controls provides additional protection. Options include:

* Container isolation
* Network restrictions
* Filesystem controls
* Request validation at a proxy

The right combination depends on your threat model and operational requirements.

## Isolation technologies

Different isolation technologies offer different tradeoffs between security strength, performance, and operational complexity.

<Info>
  In all of these configurations, Claude Code (or your Agent SDK application) runs inside the isolation boundary (the sandbox, container, or VM). The security controls described below restrict what the agent can access from within that boundary.
</Info>

| Technology              | Isolation strength             | Performance overhead | Complexity  |
| ----------------------- | ------------------------------ | -------------------- | ----------- |
| Sandbox runtime         | Good (secure defaults)         | Very low             | Low         |
| Containers (Docker)     | Setup dependent                | Low                  | Medium      |
| gVisor                  | Excellent (with correct setup) | Medium/High          | Medium      |
| VMs (Firecracker, QEMU) | Excellent (with correct setup) | High                 | Medium/High |

### Sandbox runtime

For lightweight isolation without containers, [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) enforces filesystem and network restrictions at the OS level.

The main advantage is simplicity: no Docker configuration, container images, or networking setup required. The proxy and filesystem restrictions are built in.

**How it works:**

* **Filesystem**: Uses OS primitives (`bubblewrap` on Linux, `sandbox-exec` on macOS) to restrict read/write access to configured paths
* **Network**: Removes network namespace (Linux) or uses Seatbelt profiles (macOS) to route network traffic through a built-in proxy
* **Configuration**: JSON-based allowlists for domains and filesystem paths

**Setup:**

```bash theme={null}
npm install @anthropic-ai/sandbox-runtime
```

Then create a configuration file specifying allowed paths and domains.

**Security considerations:**

1. **Same-host kernel**: Unlike VMs, sandboxed processes share the host kernel. A kernel vulnerability could theoretically enable escape. For some threat models this is acceptable, but if you need kernel-level isolation, use gVisor or a separate VM.

2. **No TLS inspection**: The proxy allowlists domains based on the client-supplied hostname and does not terminate or inspect encrypted traffic. Code running inside the sandbox can potentially use [domain fronting](https://en.wikipedia.org/wiki/Domain_fronting) or similar techniques to reach hosts outside the allowlist. If your threat model requires stronger guarantees, configure a [TLS-terminating proxy](#traffic-forwarding). See the [sandboxing security limitations](/docs/en/sandboxing#security-limitations) for more detail. Separately, if the agent has permissive credentials for an allowed domain, ensure it cannot use that domain to trigger other network requests or to exfiltrate data.

For many single-developer and CI/CD use cases, sandbox-runtime raises the bar significantly with minimal setup. The sections below cover containers and VMs for deployments requiring stronger isolation.

### Containers

Containers provide isolation through Linux namespaces. Each container has its own view of the filesystem, process tree, and network stack, while sharing the host kernel.

A security-hardened container configuration might look like this:

```bash theme={null}
docker run \
  --cap-drop ALL \
  --security-opt no-new-privileges \
  --security-opt seccomp=/path/to/seccomp-profile.json \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \
  --tmpfs /home/agent:rw,noexec,nosuid,size=500m \
  --network none \
  --memory 2g \
  --cpus 2 \
  --pids-limit 100 \
  --user 1000:1000 \
  -v /path/to/code:/workspace:ro \
  -v /var/run/proxy.sock:/var/run/proxy.sock:ro \
  agent-image
```

Here's what each option does:

| Option                             | Purpose                                                                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--cap-drop ALL`                   | Removes Linux capabilities like `NET_ADMIN` and `SYS_ADMIN` that could enable privilege escalation                                                      |
| `--security-opt no-new-privileges` | Prevents processes from gaining privileges through setuid binaries                                                                                      |
| `--security-opt seccomp=...`       | Restricts available syscalls; Docker's default blocks \~44, custom profiles can block more                                                              |
| `--read-only`                      | Makes the container's root filesystem immutable, preventing the agent from persisting changes                                                           |
| `--tmpfs /tmp:...`                 | Provides a writable temporary directory that's cleared when the container stops                                                                         |
| `--network none`                   | Removes all network interfaces; the agent communicates through the mounted Unix socket below                                                            |
| `--memory 2g`                      | Limits memory usage to prevent resource exhaustion                                                                                                      |
| `--pids-limit 100`                 | Limits process count to prevent fork bombs                                                                                                              |
| `--user 1000:1000`                 | Runs as a non-root user                                                                                                                                 |
| `-v ...:/workspace:ro`             | Mounts code read-only so the agent can analyze but not modify it. **Avoid mounting sensitive host directories like `~/.ssh`, `~/.aws`, or `~/.config`** |
| `-v .../proxy.sock:...`            | Mounts a Unix socket connected to a proxy running outside the container (see below)                                                                     |

**Unix socket architecture:**

With `--network none`, the container has no network interfaces at all. The only way for the agent to reach the outside world is through the mounted Unix socket, which connects to a proxy running on the host. This proxy can enforce domain allowlists, inject credentials, and log all traffic.

This is the same architecture used by [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime). Even if the agent is compromised via prompt injection, it cannot exfiltrate data to arbitrary servers. It can only communicate through the proxy, which controls what domains are reachable. For more details, see the [Claude Code sandboxing blog post](https://www.anthropic.com/engineering/claude-code-sandboxing).

**Additional hardening options:**

| Option           | Purpose                                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| `--userns-remap` | Maps container root to unprivileged host user; requires daemon configuration but limits damage from container escape |
| `--ipc private`  | Isolates inter-process communication to prevent cross-container attacks                                              |

### gVisor

Standard containers share the host kernel: when code inside a container makes a system call, it goes directly to the same kernel that runs the host. This means a kernel vulnerability could allow container escape. gVisor addresses this by intercepting system calls in userspace before they reach the host kernel, implementing its own compatibility layer that handles most syscalls without involving the real kernel.

If an agent runs malicious code (perhaps due to prompt injection), that code runs in the container and could attempt kernel exploits. With gVisor, the attack surface is much smaller: the malicious code would need to exploit gVisor's userspace implementation first and would have limited access to the real kernel.

To use gVisor with Docker, install the `runsc` runtime and configure the daemon:

```json /etc/docker/daemon.json theme={null}
{
  "runtimes": {
    "runsc": {
      "path": "/usr/local/bin/runsc"
    }
  }
}
```

Then run containers with:

```bash theme={null}
docker run --runtime=runsc agent-image
```

**Performance considerations:**

| Workload              | Overhead                                           |
| --------------------- | -------------------------------------------------- |
| CPU-bound computation | \~0% (no syscall interception)                     |
| Simple syscalls       | \~2× slower                                        |
| File I/O intensive    | Up to 10-200× slower for heavy open/close patterns |

For multi-tenant environments or when processing untrusted content, the additional isolation is often worth the overhead.

### Virtual machines

VMs provide hardware-level isolation through CPU virtualization extensions. Each VM runs its own kernel, creating a strong boundary. A vulnerability in the guest kernel doesn't directly compromise the host. However, VMs aren't automatically "more secure" than alternatives like gVisor. VM security depends heavily on the hypervisor and device emulation code.

Firecracker is designed for lightweight microVM isolation. It can boot VMs in under 125ms with less than 5 MiB memory overhead, stripping away unnecessary device emulation to reduce attack surface.

With this approach, the agent VM has no external network interface. Instead, it communicates through `vsock` (virtual sockets). All traffic routes through vsock to a proxy on the host, which enforces allowlists and injects credentials before forwarding requests.

### Cloud deployments

For cloud deployments, you can combine any of the above isolation technologies with cloud-native network controls:

1. Run agent containers in a private subnet with no internet gateway
2. Configure cloud firewall rules (AWS Security Groups, GCP VPC firewall) to block all egress except to your proxy
3. Run a proxy (such as [Envoy](https://www.envoyproxy.io/) with its `credential_injector` filter) that validates requests, enforces domain allowlists, injects credentials, and forwards to external APIs
4. Assign minimal IAM permissions to the agent's service account, routing sensitive access through the proxy where possible
5. Log all traffic at the proxy for audit purposes

## Credential management

Agents often need credentials to call APIs, access repositories, or interact with cloud services. The challenge is providing this access without exposing the credentials themselves.

### The proxy pattern

The recommended approach is to run a proxy outside the agent's security boundary that injects credentials into outgoing requests. The agent sends requests without credentials, the proxy adds them, and forwards the request to its destination.

This pattern has several benefits:

1. The agent never sees the actual credentials
2. The proxy can enforce an allowlist of permitted endpoints
3. The proxy can log all requests for auditing
4. Credentials are stored in one secure location rather than distributed to each agent

### Configuring Claude Code to use a proxy

Claude Code supports two methods for routing sampling requests through a proxy:

**Option 1: ANTHROPIC\_BASE\_URL (simple but only for sampling API requests)**

```bash theme={null}
export ANTHROPIC_BASE_URL="http://localhost:8080"
```

This tells Claude Code and the Agent SDK to send sampling requests to your proxy instead of the Claude API directly. Your proxy receives plaintext HTTP requests, can inspect and modify them (including injecting credentials), then forwards to the real API.

**Option 2: HTTP\_PROXY / HTTPS\_PROXY (system-wide)**

```bash theme={null}
export HTTP_PROXY="http://localhost:8080"
export HTTPS_PROXY="http://localhost:8080"
```

Claude Code and the Agent SDK respect these standard environment variables, routing all HTTP traffic through the proxy. For HTTPS, the proxy creates an encrypted CONNECT tunnel: it cannot see or modify request contents without TLS interception.

### Implementing a proxy

You can build your own proxy or use an existing one:

* [Envoy Proxy](https://www.envoyproxy.io/): production-grade proxy with `credential_injector` filter for adding auth headers
* [mitmproxy](https://mitmproxy.org/): TLS-terminating proxy for inspecting and modifying HTTPS traffic
* [Squid](http://www.squid-cache.org/): caching proxy with access control lists
* [LiteLLM](https://github.com/BerriAI/litellm): LLM gateway with credential injection and rate limiting

### Credentials for other services

Beyond sampling from the Claude API, agents often need authenticated access to other services, such as git repositories, databases, and internal APIs. There are two main approaches:

#### Custom tools

Provide access through an MCP server or custom tool that routes requests to a service running outside the agent's security boundary. The agent calls the tool, but the actual authenticated request happens outside. The tool calls to a proxy which injects the credentials.

For example, a git MCP server could accept commands from the agent but forward them to a git proxy running on the host, which adds authentication before contacting the remote repository. The agent never sees the credentials.

Advantages:

* **No TLS interception**: The external service makes authenticated requests directly
* **Credentials stay outside**: The agent only sees the tool interface, not the underlying credentials

#### Traffic forwarding

For Claude API calls, `ANTHROPIC_BASE_URL` lets you route requests to a proxy that can inspect and modify them in plaintext. But for other HTTPS services (GitHub, npm registries, internal APIs), the traffic is often encrypted end-to-end. Even if you route it through a proxy via `HTTP_PROXY`, the proxy only sees an opaque TLS tunnel and can't inject credentials.

To modify HTTPS traffic to arbitrary services, without using a custom tool, you need a TLS-terminating proxy that decrypts traffic, inspects or modifies it, then re-encrypts it before forwarding. This requires:

1. Running the proxy outside the agent's container
2. Installing the proxy's CA certificate in the agent's trust store (so the agent trusts the proxy's certificates)
3. Configuring `HTTP_PROXY`/`HTTPS_PROXY` to route traffic through the proxy

This approach handles any HTTP-based service without writing custom tools, but adds complexity around certificate management.

Note that not all programs respect `HTTP_PROXY`/`HTTPS_PROXY`. Most tools (curl, pip, npm, git) do, but some may bypass these variables and connect directly. For example, Node.js `fetch()` ignores these variables by default; in Node 24+ you can set `NODE_USE_ENV_PROXY=1` to enable support. For comprehensive coverage, you can use [proxychains](https://github.com/haad/proxychains) to intercept network calls, or configure iptables to redirect outbound traffic to a transparent proxy.

<Info>
  A **transparent proxy** intercepts traffic at the network level, so the client doesn't need to be configured to use it. Regular proxies require clients to explicitly connect and speak HTTP CONNECT or SOCKS. Transparent proxies (like Squid or mitmproxy in transparent mode) can handle raw redirected TCP connections.
</Info>

Both approaches still require the TLS-terminating proxy and trusted CA certificate. They just ensure traffic actually reaches the proxy.

## Filesystem configuration

Filesystem controls determine what files the agent can read and write.

### Read-only code mounting

When the agent needs to analyze code but not modify it, mount the directory read-only:

```bash theme={null}
docker run -v /path/to/code:/workspace:ro agent-image
```

<Warning>
  Even read-only access to a code directory can expose credentials. Common files to exclude or sanitize before mounting:

  | File                                                    | Risk                                  |
  | ------------------------------------------------------- | ------------------------------------- |
  | `.env`, `.env.local`                                    | API keys, database passwords, secrets |
  | `~/.git-credentials`                                    | Git passwords/tokens in plaintext     |
  | `~/.aws/credentials`                                    | AWS access keys                       |
  | `~/.config/gcloud/application_default_credentials.json` | Google Cloud ADC tokens               |
  | `~/.azure/`                                             | Azure CLI credentials                 |
  | `~/.docker/config.json`                                 | Docker registry auth tokens           |
  | `~/.kube/config`                                        | Kubernetes cluster credentials        |
  | `.npmrc`, `.pypirc`                                     | Package registry tokens               |
  | `*-service-account.json`                                | GCP service account keys              |
  | `*.pem`, `*.key`                                        | Private keys                          |

  Consider copying only the source files needed, or using `.dockerignore`-style filtering.
</Warning>

### Writable locations

If the agent needs to write files, you have a few options depending on whether you want changes to persist:

For ephemeral workspaces in containers, use `tmpfs` mounts that exist only in memory and are cleared when the container stops:

```bash theme={null}
docker run \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=100m \
  --tmpfs /workspace:rw,noexec,size=500m \
  agent-image
```

If you want to review changes before persisting them, an overlay filesystem lets the agent write without modifying underlying files. Changes are stored in a separate layer you can inspect, apply, or discard. For fully persistent output, mount a dedicated volume but keep it separate from sensitive directories.

## Further reading

* [Claude Code security documentation](/docs/en/security)
* [Hosting the Agent SDK](/docs/en/agent-sdk/hosting)
* [Handling permissions](/docs/en/agent-sdk/permissions)
* [Sandbox runtime](https://github.com/anthropic-experimental/sandbox-runtime)
* [The Lethal Trifecta for AI Agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
* [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
* [Docker Security Best Practices](https://docs.docker.com/engine/security/)
* [gVisor Documentation](https://gvisor.dev/docs/)
* [Firecracker Documentation](https://firecracker-microvm.github.io/)

---

## Persist sessions to external storage

- 官方原文：https://code.claude.com/docs/en/agent-sdk/session-storage.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-session-storage.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Persist sessions to external storage

> Mirror Agent SDK session transcripts to your own object store, key-value store, or database so other hosts can resume your sessions.

By default, the SDK writes session transcripts to JSONL files under `~/.claude/projects/` on the local filesystem. A `SessionStore` adapter lets you mirror those transcripts to your own backend, such as an object store, a key-value store, or a database, so a session created on one host can be resumed on another host running from a matching working directory.

Common reasons to use a session store:

* **Multi-host deployments.** Serverless functions, autoscaled workers, and CI runners don't share a filesystem. A shared store lets replicas resume each other's sessions.
* **Durability.** Local containers are ephemeral. An external store survives restarts and redeploys.
* **Compliance and audit.** Keep transcripts in storage you already govern, with your own retention rules, encryption, and access controls.

## The `SessionStore` interface

A `SessionStore` is an object with two required methods, `append` and `load`, and four optional methods. The SDK calls `append` to write transcript entries during a query and `load` to read them back for resume.

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Exported from @anthropic-ai/claude-agent-sdk as
  // SessionStore, SessionKey, SessionStoreEntry, SessionSummaryEntry.

  type SessionKey = {
    projectKey: string;
    sessionId: string;
    subpath?: string;
  };

  type SessionStore = {
    // Required
    append(key: SessionKey, entries: SessionStoreEntry[]): Promise<void>;
    load(key: SessionKey): Promise<SessionStoreEntry[] | null>;

    // Optional
    listSessions?(
      projectKey: string,
    ): Promise<Array<{ sessionId: string; mtime: number }>>;
    listSessionSummaries?(projectKey: string): Promise<SessionSummaryEntry[]>;
    delete?(key: SessionKey): Promise<void>;
    listSubkeys?(key: {
      projectKey: string;
      sessionId: string;
    }): Promise<string[]>;
  };

  type SessionSummaryEntry = {
    sessionId: string;
    mtime: number;
    data: Record<string, unknown>;
  };
  ```

  ```python Python theme={null}
  # Exported from claude_agent_sdk as
  # SessionStore, SessionKey, SessionStoreEntry, SessionSummaryEntry.

  class SessionKey(TypedDict):
      project_key: str
      session_id: str
      subpath: NotRequired[str]

  class SessionStore(Protocol):
      # Required
      async def append(
          self, key: SessionKey, entries: list[SessionStoreEntry]
      ) -> None: ...
      async def load(self, key: SessionKey) -> list[SessionStoreEntry] | None: ...

      # Optional — omit or raise NotImplementedError
      async def list_sessions(
          self, project_key: str
      ) -> list[SessionStoreListEntry]: ...
      async def list_session_summaries(
          self, project_key: str
      ) -> list[SessionSummaryEntry]: ...
      async def delete(self, key: SessionKey) -> None: ...
      async def list_subkeys(self, key: SessionListSubkeysKey) -> list[str]: ...

  class SessionSummaryEntry(TypedDict):
      session_id: str
      mtime: int
      data: dict[str, Any]
  ```
</CodeGroup>

`SessionKey` addresses one transcript. `projectKey` is a stable, filesystem-safe encoding of the working directory, `sessionId` is the session UUID, and `subpath` is set when the entry belongs to a subagent transcript or sidecar file rather than the main conversation.

Because `projectKey` encodes the working directory, resume or continue from the store from a working directory matching the original run's. In TypeScript, if you set [`CLAUDE_CODE_PROJECT_DIR_NAME`](/docs/en/sessions#name-the-project-directory-yourself) beside `CLAUDE_CONFIG_DIR` in a query's [`env` option](/docs/en/agent-sdk/typescript#options), the SDK keys that query's entries, and its `resume` and `continue` lookups, by that name instead. Because standalone helpers such as `listSessions` and `deleteSession` take no `env` and read the process environment, set `CLAUDE_CONFIG_DIR` and the same name in the host process environment too. Requires Agent SDK v0.3.234 or later.

Treat `subpath` as an opaque key suffix; it follows the on-disk layout, for example `subagents/agent-<id>`. When `subpath` is undefined the key refers to the main transcript.

| Method                 | Required | Called when                                                                                                                                                                                                                                                                                               |
| :--------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `append`               | Yes      | After each batch of transcript entries is written locally. Entries are JSON-safe objects, one per line in the local JSONL.                                                                                                                                                                                |
| `load`                 | Yes      | Before the subprocess spawns when `resume` is set or `continue: true` resolves the newest store session, and once per session when listing falls back from `listSessionSummaries`. Return `null` if the session is unknown.                                                                               |
| `listSessions`         | No       | By `listSessions({ sessionStore })` and by `query()`/`startup()` with `continue: true`. If undefined, `continue: true` throws, and `listSessions({ sessionStore })` throws unless `listSessionSummaries` is implemented.                                                                                  |
| `listSessionSummaries` | No       | By `listSessions({ sessionStore })` to read metadata for all sessions in one call. Maintain the summaries inside `append`. If undefined, listing falls back to `listSessions` plus a per-session `load`.                                                                                                  |
| `delete`               | No       | By `deleteSession({ sessionStore })`. Deleting the main key (no `subpath`) must cascade to all subkeys for that session and also remove the session's summary entry, so a deleted session stops appearing in `listSessionSummaries`. If undefined, deletion is a no-op, which suits append-only backends. |
| `listSubkeys`          | No       | During resume, to discover subagent transcripts. If undefined, only the main transcript is restored.                                                                                                                                                                                                      |

In a `SessionSummaryEntry`, `mtime` is the sidecar's storage write time and must share a clock source with the `mtime` values `listSessions` returns. `data` is opaque SDK-owned state; persist it verbatim without interpreting it.

Build the entries by calling the exported `foldSessionSummary` helper, `fold_session_summary` in Python, on each batch inside `append`. Skip batches whose key has a `subpath`; subagent transcripts must not contribute to the main session's summary. The fold never sets `mtime`: stamp it at persist time, through the `options.mtime` argument in TypeScript or by overwriting the field on the returned entry in Python. Concurrent `append` calls for the same session can race on the sidecar, so serialize the read-fold-write with a transaction, a compare-and-swap, or a per-session lock; the fold itself is pure.

For what the SDK does with the transcript `load` returns, see [Resume from the store](#resume-from-the-store).

## Quick start

The SDK ships an `InMemorySessionStore` for development and testing. The example below runs a query with the store attached, captures the session ID from the result message, then resumes from the store in a second `query()` call. The second call passes the same store instance plus `resume`, so the SDK loads the transcript from the store instead of the local filesystem:

<CodeGroup>
  ```typescript TypeScript theme={null}

  const store = new InMemorySessionStore();

  let sessionId: string | undefined;
  try {
    for await (const message of query({
      prompt: "List the TypeScript files under src/",
      options: { sessionStore: store },
    })) {
      if (message.type === "result") {
        sessionId = message.session_id;
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, sessionId was already captured by the loop
    // above; connection or process failures yield no result message.
    console.error(`Session ended with an error: ${error}`);
  }

  // Resume from the store. The agent has full context from the first call.
  for await (const message of query({
    prompt: "Summarize what those files do",
    options: { sessionStore: store, resume: sessionId },
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import (
      ClaudeAgentOptions,
      InMemorySessionStore,
      ResultMessage,
      query,
  )

  store = InMemorySessionStore()

  async def main():
      session_id = None
      try:
          async for message in query(
              prompt="List the Python files under src/",
              options=ClaudeAgentOptions(session_store=store),
          ):
              if isinstance(message, ResultMessage):
                  session_id = message.session_id
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, session_id was already captured by the
          # loop above; connection or process failures yield no result message.
          print(f"Session ended with an error: {error}")

      # Resume from the store. The agent has full context from the first call.
      async for message in query(
          prompt="Summarize what those files do",
          options=ClaudeAgentOptions(session_store=store, resume=session_id),
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

The second query prints a summary of the files from the first query, which shows the agent resumed with full context from the store.

## Write your own adapter

Implement `append` and `load` against your backend. Add `listSessions`, `listSessionSummaries`, `delete`, and `listSubkeys` if you want `listSessions()`, one-call metadata reads, `deleteSession()`, and subagent resume to work against the store.

Entries passed to `append` are typed as `SessionStoreEntry` (a `{ type: string; ... }` object). Treat them as opaque JSON-safe values: persist them in order and return them from `load` in the same order. `load` must return entries that are deep-equal to what was appended; byte-equal serialization is not required, so a backend that reorders object keys, such as a binary JSON column type, is fine.

## Reference implementations

Both SDK repositories include runnable reference adapters under [`examples/session-stores/`](https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/examples/session-stores) in TypeScript and [`examples/session_stores/`](https://github.com/anthropics/claude-agent-sdk-python/tree/main/examples/session_stores) in Python. There is one adapter per storage type, and each shows how `append` and `load` map onto that kind of backend. They are not published as packages; copy the adapter for the type closest to your backend into your project, install your backend's client, and adapt it.

| Storage type                          | Storage model                                                                                                   | Example adapter                                                                                                                                                                                                                                            |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Object store                          | One part file per `append()`; `load()` lists the parts, sorts them, and concatenates.                           | S3 ([TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/examples/session-stores/s3), [Python](https://github.com/anthropics/claude-agent-sdk-python/blob/main/examples/session_stores/s3_session_store.py))                   |
| Key-value store                       | One list per transcript that `append()` pushes to and `load()` reads in range, plus a sorted index of sessions. | Redis ([TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/examples/session-stores/redis), [Python](https://github.com/anthropics/claude-agent-sdk-python/blob/main/examples/session_stores/redis_session_store.py))          |
| Relational database or document store | One row or document per entry, stored as JSON and ordered by a key assigned on insert.                          | Postgres ([TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript/tree/main/examples/session-stores/postgres), [Python](https://github.com/anthropics/claude-agent-sdk-python/blob/main/examples/session_stores/postgres_session_store.py)) |

Each adapter takes a pre-configured client instance, so you control credentials, TLS, region, and pooling. The following example wires the object-store adapter into `query()` and then resumes from it on another host:

```typescript TypeScript theme={null}

const store = new S3SessionStore({
  bucket: "my-claude-sessions",
  prefix: "transcripts",
  client: new S3Client({ region: "us-east-1" }),
});

for await (const message of query({
  prompt: "Hello!",
  options: { sessionStore: store },
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}

// Later, possibly on a different host:
for await (const message of query({
  prompt: "Continue where we left off",
  options: { sessionStore: store, resume: "previous-session-id" },
})) {
  // ...
}
```

### Validate your adapter

Both SDKs ship a conformance suite that asserts the behavioral contract `append`, `load`, and the optional methods must satisfy. Tests for optional methods skip automatically when those methods are not implemented.

In TypeScript, copy [`shared/conformance.ts`](https://github.com/anthropics/claude-agent-sdk-typescript/blob/main/examples/session-stores/shared/conformance.ts) from the example directory into your test suite. In Python, the suite ships in the package. To run it with pytest, which isn't an SDK dependency, install pytest first:

```bash theme={null}
pip install pytest
```

Then pass your adapter to the suite in a test file as a zero-argument factory, which `run_session_store_conformance` calls once per contract to build a fresh store:

```python Python theme={null}
import pytest
from claude_agent_sdk.testing import run_session_store_conformance

@pytest.mark.anyio
async def test_my_store_conformance():
    await run_session_store_conformance(MyRedisStore)
```

Passing the `MyRedisStore` class itself, as this example does, works when the constructor takes no arguments. For an adapter that takes a pre-configured client, pass a lambda that constructs the store instead. Because the contracts reuse the same session keys, each store the factory returns must start with empty storage, so have the lambda provision isolated backing storage per call, such as a fresh in-memory fake, a unique key prefix, or a new test database.

## Behavior notes

### Dual-write architecture

The Claude Code subprocess always writes each batch of transcript entries to local disk first, and the SDK then forwards the same batch to your store's `append()`, so the store is a mirror of the local transcript rather than a replacement for it. Which copy outlives the run depends on how the run started:

* **Fresh session, or a resume when the store has nothing for the session**: the local transcript under your config directory outlives the run, and the store receives a copy.
* **Run [resumed from the store](#resume-from-the-store)**: the local copy is deleted at run end, so the store holds the only durable copy.

If you don't want a fresh session to leave a transcript on local disk, set `CLAUDE_CONFIG_DIR` to a temp directory in `options.env`. A run resumed from the store already deletes its local copy, so it needs no such setting. In TypeScript, spread `process.env` into `env` as well, since the [`env` option](/docs/en/agent-sdk/typescript#options) replaces the subprocess environment.

If your app signs in through files in the config directory, such as OAuth credentials or an `apiKeyHelper` in your user `settings.json`, copy those files into the temp directory first, or set `ANTHROPIC_API_KEY` in `env` instead. Otherwise the run fails with `Not logged in`.

Two options conflict with the mirror, and the SDK throws at startup if you combine either with a store:

* **`persistSession: false`** in TypeScript: turns off the local writes the mirror is built from. The Python SDK has no equivalent option.
* **File checkpointing**, `enableFileCheckpointing` in TypeScript or `enable_file_checkpointing` in Python: writes its file backups straight to local disk, and the SDK doesn't mirror them to the store.

### Resume from the store

When you pass `resume`, or `continue: true` in TypeScript or `continue_conversation=True` in Python, together with a store, the SDK asks the store for a transcript before it spawns the subprocess:

* **`resume`**: the SDK asks for the session whose ID you passed.
* **`continue: true`** or **`continue_conversation=True`**: the SDK asks for the store's newest session.

When the store returns the transcript, the SDK writes it into a temporary config directory, runs the subprocess with `CLAUDE_CONFIG_DIR` pointing there, and deletes the directory when the run ends. The local transcript that run writes is deleted with it, which is why the store holds the only durable copy on this path.

The SDK also seeds the temporary directory with files from your real config directory. What it copies differs by language:

* **TypeScript**: credentials, `.claude.json`, and your user `settings.json`. From `settings.json` it strips the keys that misbehave under a temporary config directory: `enabledPlugins`, `extraKnownMarketplaces`, its [`additionalMarketplaces`](/docs/en/settings-reference#extraknownmarketplaces) alias, and any `CLAUDE_CONFIG_DIR` in the file's `env` block. Before Agent SDK v0.3.232, the SDK didn't strip the alias. Auth configured in settings, such as [`apiKeyHelper`](/docs/en/settings-reference#apikeyhelper), works when you resume from the store. Before Agent SDK v0.3.222, the TypeScript SDK copied only credentials and `.claude.json`.
* **Python**: credentials and `.claude.json` only, so an app that authenticates through `apiKeyHelper` in your user `settings.json` fails with `Not logged in` when resuming from a store. An `apiKeyHelper` in managed or project settings still works, because Claude Code reads those files from locations that `CLAUDE_CONFIG_DIR` doesn't affect.

When the store has nothing for the session, the SDK runs under your real config directory instead, and the outcome depends on which option you passed:

* **`resume`**: both SDKs pass the ID through to the subprocess, which resumes the local transcript exactly as `resume` does without a store.
* **`continue: true`** in TypeScript: the SDK starts a fresh session.
* **`continue_conversation=True`** in Python: the SDK continues from the newest local session.

### Mirror writes are best-effort

If `append()` rejects, the SDK retries the batch up to two more times with a short backoff, for at most three attempts in total. A call that times out isn't retried, since the original call may still land. If the batch still fails, the SDK logs the error, emits a `{ type: "system", subtype: "mirror_error" }` message into the iterator, drops the batch, and continues the query. Because a retried batch can re-deliver entries that already landed, deduplicate by `entry.uuid` in your `append()` implementation.

A store outage doesn't interrupt the agent, since the subprocess writes locally first. Monitor for `mirror_error` if you need to detect store data loss. On a run [resumed from the store](#resume-from-the-store), a dropped batch has no surviving copy once the run ends.

### `getSessionMessages` returns the post-compaction chain

`getSessionMessages({ sessionStore })` returns the linked message chain the agent would see on resume. After auto-compaction, earlier turns are replaced by a summary, so a session whose store holds 503 raw entries may return 18 messages from `getSessionMessages`. For the full raw history, including pre-compaction turns and metadata entries, call `store.load(key)` directly.

### `forkSession` is not a byte copy

`forkSession({ sessionStore })` reads the source entries, rewrites every `sessionId` field and remaps message UUIDs, then appends the transformed entries under a new key. An adapter-level copy or `CopyObject` shortcut would produce a transcript that still references the old session ID, so the SDK does not use one.

### Subagent transcripts

Subagent transcripts are mirrored under `subpath: "subagents/agent-<id>"`. `listSubagents({ sessionStore })` requires the adapter to implement `listSubkeys`; `getSubagentMessages({ sessionStore })` uses it when available but falls back to the direct subpath when it is undefined. Resume also calls `listSubkeys` to restore subagent files; without it, only the main transcript is materialized.

### Retention

The SDK never deletes from your store on its own. Retention is the adapter's responsibility: use your backend's expiry or lifecycle mechanism, or run scheduled cleanup, according to your compliance requirements.

Local transcripts under `CLAUDE_CONFIG_DIR` are swept independently by the `cleanupPeriodDays` setting, following the [retention sweep rules](/docs/en/claude-directory#cleaned-up-automatically). A run [resumed from the store](#resume-from-the-store) leaves no local transcript, so for those runs your store's retention is the only retention there is.

## Supported on

The following TypeScript SDK functions accept a `sessionStore` option and operate against the store instead of the local filesystem when it is provided:

* [`query()`](/docs/en/agent-sdk/typescript#query)
* [`startup()`](/docs/en/agent-sdk/typescript#startup)
* [`listSessions()`](/docs/en/agent-sdk/typescript#listsessions)
* [`getSessionInfo()`](/docs/en/agent-sdk/typescript#getsessioninfo)
* [`getSessionMessages()`](/docs/en/agent-sdk/typescript#getsessionmessages)
* [`renameSession()`](/docs/en/agent-sdk/typescript#renamesession)
* [`tagSession()`](/docs/en/agent-sdk/typescript#tagsession)
* [`deleteSession()`](/docs/en/agent-sdk/typescript)
* [`forkSession()`](/docs/en/agent-sdk/typescript)
* [`listSubagents()`](/docs/en/agent-sdk/typescript)
* [`getSubagentMessages()`](/docs/en/agent-sdk/typescript)

In the Python SDK, set `session_store` in [`ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions) to run `query()` against a store. The remaining operations each have a store-backed Python function that takes the store as an argument: `list_sessions_from_store()`, `get_session_info_from_store()`, `get_session_messages_from_store()`, `list_subagents_from_store()`, `get_subagent_messages_from_store()`, `rename_session_via_store()`, `tag_session_via_store()`, `delete_session_via_store()`, and `fork_session_via_store()`. `startup()` has no Python equivalent. The standalone functions documented in the [Python SDK reference](/docs/en/agent-sdk/python#functions), such as `list_sessions()`, read local session files.

## Related resources

* [Work with sessions](/docs/en/agent-sdk/sessions): Continue, resume, and fork without a custom store
* [Host the SDK](/docs/en/agent-sdk/hosting): Deployment patterns for multi-host environments
* [TypeScript `Options`](/docs/en/agent-sdk/typescript#options): Full option reference
* [Reference implementations](#reference-implementations): Runnable example adapters for an object store, a key-value store, and a database, in both SDK repositories

---

## Work with sessions

- 官方原文：https://code.claude.com/docs/en/agent-sdk/sessions.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-sessions.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Work with sessions

> How sessions persist agent conversation history, and when to use continue, resume, and fork to return to a prior run.

A session is the conversation history the SDK accumulates while your agent works. It contains your prompt, every tool call the agent made, every tool result, and every response. The SDK writes it to disk automatically so you can return to it later.

Returning to a session means the agent has full context from before: files it already read, analysis it already performed, decisions it already made. You can ask a follow-up question, recover from an interruption, or branch off to try a different approach.

<Note>
  Sessions persist the **conversation**, not the filesystem. To snapshot and revert file changes the agent made, use [file checkpointing](/docs/en/agent-sdk/file-checkpointing).
</Note>

This guide covers how to pick the right approach for your app, the SDK interfaces that track sessions automatically, how to capture session IDs and use `resume` and `fork` manually, and what to know about resuming sessions across hosts.

## Choose an approach

How much session handling you need depends on your application's shape. Session management comes into play when you send multiple prompts that should share context. Within a single `query()` call, the agent already takes as many turns as it needs, and permission prompts and `AskUserQuestion` are [handled in-loop](/docs/en/agent-sdk/user-input) (they don't end the call).

| What you're building                                    | What to use                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One-shot task: single prompt, no follow-up              | Nothing extra. One `query()` call handles it.                                                                                                                                                                                                                                  |
| Multi-turn chat in one process                          | [`ClaudeSDKClient` (Python) or `continue: true` (TypeScript)](#automatic-session-management). The SDK tracks the session for you with no ID handling.                                                                                                                          |
| Pick up where you left off after a process restart      | `continue_conversation=True` (Python) / `continue: true` (TypeScript). Resumes the most recent session in the directory, no ID needed.                                                                                                                                         |
| Resume a specific past session (not the most recent)    | Capture the session ID and pass it to `resume`.                                                                                                                                                                                                                                |
| Try an alternative approach without losing the original | Fork the session.                                                                                                                                                                                                                                                              |
| Stateless task, don't want anything written to disk     | Set [`persistSession: false`](/docs/en/agent-sdk/typescript#options) (TypeScript only). The session exists only in memory for the duration of the call. In Python, set [`CLAUDE_CODE_SKIP_PROMPT_HISTORY`](/docs/en/env-vars) in the `env` option to suppress transcript writes instead. |

### Continue, resume, and fork

Continue, resume, and fork are option fields you set on `query()` ([`ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions) in Python, [`Options`](/docs/en/agent-sdk/typescript#options) in TypeScript).

**Continue** and **resume** both pick up an existing session and add to it. The difference is how they find that session:

* **Continue** finds the most recent session in the current directory. You don't track anything. Works well when your app runs one conversation at a time.
* **Resume** takes a specific session ID. You track the ID. Required when you have multiple sessions (for example, one per user in a multi-user app) or want to return to one that isn't the most recent.

**Fork** is different: it creates a new session that starts with a copy of the original's history. The original stays unchanged. Use fork to try a different direction while keeping the option to go back.

## Automatic session management

Both SDKs offer an interface that tracks session state for you across calls, so you don't pass IDs around manually. Use these for multi-turn conversations within a single process.

### Python: `ClaudeSDKClient`

[`ClaudeSDKClient`](/docs/en/agent-sdk/python#claudesdkclient) handles session IDs internally. Each call to `client.query()` automatically continues the same session. Call [`client.receive_response()`](/docs/en/agent-sdk/python#claudesdkclient) to iterate over the messages for the current query. Use the client as an async context manager so connection setup and teardown are handled for you, or call `connect()` and `disconnect()` manually.

This example runs two queries against the same `client`. The first asks the agent to analyze a module; the second asks it to refactor that module. Because both calls go through the same client instance, the second query has full context from the first without any explicit `resume` or session ID:

```python Python theme={null}
import asyncio
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    TextBlock,
)

def print_response(message):
    """Print only the human-readable parts of a message."""
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text)
    elif isinstance(message, ResultMessage):
        cost = (
            f"${message.total_cost_usd:.4f}"
            if message.total_cost_usd is not None
            else "N/A"
        )
        print(f"[done: {message.subtype}, cost: {cost}]")

async def main():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Edit", "Glob", "Grep"],
    )

    async with ClaudeSDKClient(options=options) as client:
        # First query: client captures the session ID internally
        await client.query("Analyze the auth module")
        async for message in client.receive_response():
            print_response(message)

        # Second query: automatically continues the same session
        await client.query("Now refactor it to use JWT")
        async for message in client.receive_response():
            print_response(message)

asyncio.run(main())
```

Each query prints the agent's text response followed by a status line from the result message, such as `[done: success, cost: $0.0042]`.

See the [Python SDK reference](/docs/en/agent-sdk/python#choosing-between-query-and-claudesdkclient) for details on when to use `ClaudeSDKClient` vs the standalone `query()` function.

### TypeScript: `continue: true`

The TypeScript SDK doesn't have a session-holding client object like Python's `ClaudeSDKClient`. Instead, pass `continue: true` on each subsequent `query()` call and the SDK picks up the most recent session in the current directory. No ID tracking required.

This example makes two separate `query()` calls. The first creates a fresh session; the second sets `continue: true`, which tells the SDK to find and resume the most recent session on disk. The agent has full context from the first call:

```typescript TypeScript theme={null}

// First query: creates a new session
try {
  for await (const message of query({
    prompt: "Analyze the auth module",
    options: { allowedTools: ["Read", "Glob", "Grep"] }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
} catch (error) {
  // A single-shot query() throws after yielding an error result,
  // so the follow-up query below still runs.
  console.error(`Session ended with an error: ${error}`);
}

// Second query: continue: true resumes the most recent session
for await (const message of query({
  prompt: "Now refactor it to use JWT",
  options: {
    continue: true,
    allowedTools: ["Read", "Edit", "Write", "Glob", "Grep"]
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}
```

<Note>
  The experimental [V2 session API](/docs/en/agent-sdk/typescript-v2-preview), which provided `createSession()` with a `send` / `stream` pattern, was removed in TypeScript Agent SDK 0.3.142. Use the `query()` function and the session options described on this page instead.
</Note>

## Use session options with `query()`

### Capture the session ID

Resume and fork require a session ID. Read it from the `session_id` field on the result message ([`ResultMessage`](/docs/en/agent-sdk/python#resultmessage) in Python, [`SDKResultMessage`](/docs/en/agent-sdk/typescript#sdkresultmessage) in TypeScript), which is present on every result regardless of success or error. In TypeScript the ID is also available earlier as a direct field on the init `SystemMessage`; in Python it's nested inside `SystemMessage.data`.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      session_id = None

      try:
          async for message in query(
              prompt="Analyze the auth module and suggest improvements",
              options=ClaudeAgentOptions(
                  allowed_tools=["Read", "Glob", "Grep"],
              ),
          ):
              if isinstance(message, ResultMessage):
                  session_id = message.session_id
                  if message.subtype == "success":
                      print(message.result)
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, the loop above already captured session_id;
          # connection or process failures yield no result message, so session_id stays None.
          print(f"Session ended with an error: {error}")

      print(f"Session ID: {session_id}")
      return session_id

  session_id = asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  let sessionId: string | undefined;

  try {
    for await (const message of query({
      prompt: "Analyze the auth module and suggest improvements",
      options: { allowedTools: ["Read", "Glob", "Grep"] }
    })) {
      if (message.type === "result") {
        sessionId = message.session_id;
        if (message.subtype === "success") {
          console.log(message.result);
        }
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, the loop above already captured sessionId;
    // connection or process failures yield no result message, so sessionId stays undefined.
    console.error(`Session ended with an error: ${error}`);
  }

  console.log(`Session ID: ${sessionId}`);
  ```
</CodeGroup>

When the query completes, the script prints the agent's response followed by a line such as `Session ID: 5b3f2c1a-8d4e-4f6b-9a7c-2e1d0f9b8a6c`. In the next sections, you pass this ID to `resume`.

### Resume by ID

Pass a session ID to `resume` to return to that specific session. The agent picks up with full context from wherever the session left off. Common reasons to resume:

* **Follow up on a completed task.** The agent already analyzed something; now you want it to act on that analysis without re-reading files.
* **Recover from a limit.** The first run ended with `error_max_turns` or `error_max_budget_usd` (see [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result)); resume with a higher limit. In a single-shot `query()` call the SDK raises after yielding that error result, so catch the error before resuming.
* **Restart your process.** You captured the ID before shutdown and want to restore the conversation.

This example resumes the session from [Capture the session ID](#capture-the-session-id) with a follow-up prompt. Because you're resuming, the agent already has the prior analysis in context:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  session_id = "..."  # The ID you captured in the previous example

  async def main():
      # Earlier session analyzed the code; now build on that analysis
      async for message in query(
          prompt="Now implement the refactoring you suggested",
          options=ClaudeAgentOptions(
              resume=session_id,
              allowed_tools=["Read", "Edit", "Write", "Glob", "Grep"],
          ),
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  const sessionId = "..."; // The ID you captured in the previous example

  // Earlier session analyzed the code; now build on that analysis
  for await (const message of query({
    prompt: "Now implement the refactoring you suggested",
    options: {
      resume: sessionId,
      allowedTools: ["Read", "Edit", "Write", "Glob", "Grep"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

You should see a response that builds on the earlier analysis instead of starting fresh. That confirms the agent resumed the session with its prior context intact.

<Tip>
  Claude Code stores sessions under `~/.claude/projects/<encoded-cwd>/*.jsonl`. If you set the `CLAUDE_CONFIG_DIR` environment variable, look under `$CLAUDE_CONFIG_DIR/projects/` instead.

  To find your session's directory, replace every non-alphanumeric character in the absolute working directory with `-`: `/Users/me/proj` becomes `-Users-me-proj`. For a working directory whose converted name exceeds 200 characters, Claude Code [truncates the name and appends a hash](/docs/en/sessions#where-transcripts-are-stored), so match the first 200 characters of the converted name when you list `projects/`.

  If you set [`CLAUDE_CODE_PROJECT_DIR_NAME`](/docs/en/sessions#name-the-project-directory-yourself) beside `CLAUDE_CONFIG_DIR`, look under that name in `projects/` instead. Requires TypeScript Agent SDK v0.3.234 or later, or Python Agent SDK v0.2.140 or later.

  You can resume from any working directory:

  * **Cross-directory lookup**: Claude Code searches beyond the current project directory to find the ID; see [Resume a session](/docs/en/sessions#resume-a-session) for the exact lookup order and how duplicate copies are handled.
  * **Same machine only**: the session file still needs to exist on the current machine.

  Before v2.1.223, the lookup was scoped to the current project directory and its git worktrees; SDK versions that bundle an older CLI still behave this way.
</Tip>

To resume sessions across machines or in serverless environments, mirror transcripts to shared storage with a [`SessionStore` adapter](/docs/en/agent-sdk/session-storage).

### Fork to explore alternatives

Forking creates a new session that starts with a copy of the original's history but diverges from that point. The fork gets its own session ID; the original's ID and history stay unchanged. You end up with two independent sessions you can resume separately.

<Note>
  Forking branches the conversation history, not the filesystem. If a forked agent edits files, those changes are real and visible to any session working in the same directory. To branch and revert file changes, use [file checkpointing](/docs/en/agent-sdk/file-checkpointing).
</Note>

This example builds on [Capture the session ID](#capture-the-session-id): you've already analyzed an auth module in `session_id` and want to explore OAuth2 without losing the JWT-focused thread. The first block forks the session and captures the fork's ID (`forked_id`); the second block resumes the original `session_id` to continue down the JWT path. You now have two session IDs pointing at two separate histories:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  session_id = "..."  # The ID you captured in the previous example

  async def main():
      # Fork: branch from session_id into a new session
      forked_id = None
      try:
          async for message in query(
              prompt="Instead of JWT, outline how OAuth2 would work for the auth module",
              options=ClaudeAgentOptions(
                  resume=session_id,
                  fork_session=True,
                  max_turns=5,
              ),
          ):
              if isinstance(message, ResultMessage):
                  forked_id = message.session_id  # The fork's ID, distinct from session_id
                  if message.subtype == "success":
                      print(message.result)
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, forked_id was already captured by the
          # loop above; connection or process failures yield no result message.
          print(f"Session ended with an error: {error}")

      print(f"Forked session: {forked_id}")

      # Original session is untouched; resuming it continues the JWT thread
      try:
          async for message in query(
              prompt="Continue with the JWT approach",
              options=ClaudeAgentOptions(resume=session_id),
          ):
              if isinstance(message, ResultMessage) and message.subtype == "success":
                  print(message.result)
      except Exception as error:
          # A single-shot query() raises after yielding an error result.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  const sessionId = "..."; // The ID you captured in the previous example

  // Fork: branch from sessionId into a new session
  let forkedId: string | undefined;

  try {
    for await (const message of query({
      prompt: "Instead of JWT, outline how OAuth2 would work for the auth module",
      options: {
        resume: sessionId,
        forkSession: true,
        maxTurns: 5
      }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        forkedId = message.session_id; // The fork's ID, distinct from sessionId
      }
      if (message.type === "result" && message.subtype === "success") {
        console.log(message.result);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, forkedId was already captured by the loop
    // above; connection or process failures yield no result message.
    console.error(`Session ended with an error: ${error}`);
  }

  console.log(`Forked session: ${forkedId}`);

  // Original session is untouched; resuming it continues the JWT thread
  try {
    for await (const message of query({
      prompt: "Continue with the JWT approach",
      options: { resume: sessionId }
    })) {
      if (message.type === "result" && message.subtype === "success") {
        console.log(message.result);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result.
    console.error(`Session ended with an error: ${error}`);
  }
  ```
</CodeGroup>

You should see that `forkedId` differs from the original session ID. Resuming the original session still continues the JWT thread, which confirms the fork did not modify the original history.

## Resume across hosts

Session files are local to the machine that created them. To resume a session on a different host (CI workers, ephemeral containers, serverless), pick the approach that fits:

* **Pass a session store.** Attach a [`sessionStore` / `session_store` adapter](/docs/en/agent-sdk/session-storage) so the SDK mirrors transcripts to your own backend and another host can resume them. The store lookup key derives from the working directory, so resume from a `cwd` matching the original run's.

* **Move the session file.** Persist `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` from the first run and restore it inside any directory under `~/.claude/projects/` on the new host before calling `resume`.

  Claude Code searches beyond the current project directory to find the ID; see [Resume a session](/docs/en/sessions#resume-a-session) for the exact lookup order and how duplicate copies are handled. Before v2.1.223, the lookup was scoped to the current project directory and its git worktrees; SDK versions that bundle an older CLI still behave this way.

* **Don't rely on session resume.** Capture the results you need (analysis output, decisions, file diffs) as application state and pass them into a fresh session's prompt. This is often more robust than shipping transcript files around.

Both SDKs expose functions for enumerating sessions on disk and reading their messages: [`listSessions()`](/docs/en/agent-sdk/typescript#listsessions) and [`getSessionMessages()`](/docs/en/agent-sdk/typescript#getsessionmessages) in TypeScript, [`list_sessions()`](/docs/en/agent-sdk/python#list_sessions) and [`get_session_messages()`](/docs/en/agent-sdk/python#get_session_messages) in Python. Use them to build custom session pickers, cleanup logic, or transcript viewers.

Both SDKs also expose functions for looking up and mutating individual sessions: [`get_session_info()`](/docs/en/agent-sdk/python#get_session_info), [`rename_session()`](/docs/en/agent-sdk/python#rename_session), and [`tag_session()`](/docs/en/agent-sdk/python#tag_session) in Python, and [`getSessionInfo()`](/docs/en/agent-sdk/typescript#getsessioninfo), [`renameSession()`](/docs/en/agent-sdk/typescript#renamesession), and [`tagSession()`](/docs/en/agent-sdk/typescript#tagsession) in TypeScript. Use them to organize sessions by tag or give them human-readable titles.

## Related resources

* [How the agent loop works](/docs/en/agent-sdk/agent-loop): Understand turns, messages, and context accumulation within a session
* [File checkpointing](/docs/en/agent-sdk/file-checkpointing): Snapshot and revert file changes the agent made within a session
* [Python `ClaudeAgentOptions`](/docs/en/agent-sdk/python#claudeagentoptions): Full session option reference for Python
* [TypeScript `Options`](/docs/en/agent-sdk/typescript#options): Full session option reference for TypeScript

---

## Extend agents with skills

- 官方原文：https://code.claude.com/docs/en/agent-sdk/skills.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-skills.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Extend agents with skills

> Control which skills Claude can invoke in Claude Agent SDK sessions, dispatch commands by name, and author skills your sessions discover

Agent Skills extend Claude with specialized capabilities that Claude invokes when relevant. Skills are packaged as `SKILL.md` files containing instructions, descriptions, and optional supporting resources. This page also covers [commands in Agent SDK sessions](#commands-in-agent-sdk-sessions).

For comprehensive information about skills, including benefits, architecture, and authoring guidelines, see the [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## How skills work with the Agent SDK

When using the Claude Agent SDK, skills are:

* **Defined as filesystem artifacts**: you create each skill as a `SKILL.md` file in its own directory, such as `.claude/skills/<name>/SKILL.md`
* **Loaded from filesystem**: the SDK loads skills from the filesystem locations governed by `settingSources` (TypeScript) or `setting_sources` (Python)
* **Automatically discovered**: once filesystem settings load, the SDK discovers skill metadata at startup from user and project directories, and loads the full content when Claude invokes the skill
* **Model-invoked**: Claude autonomously chooses when to use them based on context
* **User-invoked**: you dispatch a skill directly by sending `/<name>` in a prompt. See [Commands in Agent SDK sessions](#commands-in-agent-sdk-sessions)
* **Scoped via the `skills` option**: discovered skills are enabled by default. Pass a list of skill names, `"all"`, or `[]` to control which skills Claude can invoke

Unlike subagents, which you can define in the [`agents` option](/docs/en/agent-sdk/subagents#programmatic-definition-recommended), you create skills as files on disk. The SDK doesn't provide a programmatic API for registering them.

<Note>
  Skills are discovered through the filesystem setting sources. With default `query()` options, the SDK loads user and project sources, so skills in `~/.claude/skills/`, `<cwd>/.claude/skills/`, and `.claude/skills/` in any parent directory of `<cwd>` up to the repository root are available. The project source also covers `<dir>/.claude/skills/` in each directory you pass through `additionalDirectories` (TypeScript) or `add_dirs` (Python), because the SDK passes those directories to Claude Code as [`--add-dir`](/docs/en/skills#skills-from-additional-directories). If you set `settingSources` explicitly, include `'project'` to keep project and added-directory skills and `'user'` to keep your personal skills, or use the [`plugins` option](/docs/en/agent-sdk/plugins) to load skills from a specific path.
</Note>

## Use skills with the Agent SDK

Set the `skills` option on `query()` to control which skills Claude can invoke in the session. When omitted, discovered skills are enabled and the Skill tool is available, matching CLI behavior. Pass `"all"` to let Claude invoke every discovered skill, a list of skill names to allow only those, or `[]` to let Claude invoke none.

For example, to let Claude invoke only two named skills:

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(skills=["pdf", "docx"])
  ```

  ```typescript TypeScript theme={null}
  const options = { skills: ["pdf", "docx"] };
  ```
</CodeGroup>

### Set up skills in a session

When you set `skills`, the SDK adds the Skill tool to `allowedTools` automatically. If you also pass an explicit `tools` list, include `"Skill"` in that list so Claude can invoke skills.

Once configured, Claude automatically discovers skills from the filesystem and invokes them when relevant to the user's request.

The following example enables every discovered skill in a session and pre-approves the tools that skills commonly need. The example sets `cwd` to the process's current working directory, so run it from inside a project that has a `.claude/skills/` directory in the current directory or any parent up to the repository root:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import os

  from claude_agent_sdk import query, ClaudeAgentOptions

  async def main():
      options = ClaudeAgentOptions(
          cwd=os.getcwd(),  # .claude/skills/ here or in a parent directory
          setting_sources=["user", "project"],  # Load skills from filesystem
          skills="all",  # Let Claude invoke every discovered skill
          allowed_tools=["Read", "Write", "Bash"],
      )

      async for message in query(
          prompt="Help me process this PDF document", options=options
      ):
          print(message)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Help me process this PDF document",
    options: {
      cwd: process.cwd(), // .claude/skills/ here or in a parent directory
      settingSources: ["user", "project"], // Load skills from filesystem
      skills: "all", // Let Claude invoke every discovered skill
      allowedTools: ["Read", "Write", "Bash"]
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

### Confirm skills loaded

Near the start of the stream, the SDK yields a system message with subtype `init`. Check its `skills` array to confirm your skills loaded before Claude starts working. The array includes the user-invocable skills that you have defined with a `description` or `when_to_use` frontmatter field, along with [bundled skills included with Claude Code](/docs/en/skills#bundled-skills).

The array lists user-invocable skills only. A skill with [`user-invocable: false`](/docs/en/skills#control-who-invokes-a-skill) in its frontmatter loads and remains available to Claude, but doesn't appear in the array. The array lists the same skills whether or not they're in your `skills` list.

### Allow only specific skills

To let Claude invoke only specific skills, pass their names in the `skills` list. Names match the `name` field in `SKILL.md` or the skill's directory name. Use `plugin:skill` for plugin-provided skills.

The list takes exact skill names only. If an entry can't work as an exact name, `query()` rejects the list before the session starts. See [Invalid skill name error](#invalid-skill-name-error) for the name rules and the error each SDK raises.

The model doesn't see unlisted skills and the Skill tool rejects them, while their files remain on disk and stay reachable through Read and Bash. Restricting the list doesn't restrict [dispatch by name](#dispatch-commands-by-name).

To let Claude invoke every discovered skill, pass `skills: "all"` rather than a wildcard.

## Commands in Agent SDK sessions

This section is the SDK's command documentation. A command is anything you run by sending `/<name>` in a prompt. Entries on the command surface differ in what backs them:

* **Built-in commands**: execute logic coded into the Claude Code process the SDK runs, for example `/compact`
* **Bundled skills**: prompt artifacts included with Claude Code, for example `/code-review`
* **Your skills**: prompt artifacts that you author, each a directory holding a `SKILL.md` file. A user-invocable skill's name joins the surface automatically, so dispatching your own `/security-check` and running a built-in work the same way
* **Custom command files**: an older artifact form with the same behavior, flat Markdown files in `.claude/commands/` whose filenames become command names. Skills are their recommended successor

By default, both you and Claude can invoke any skill. You can restrict either path through the skill's [frontmatter](/docs/en/skills#control-who-invokes-a-skill). For definitions of command and skill, see the glossary's [Command](/docs/en/glossary#command) and [Skill](/docs/en/glossary#skill) entries. See [Commands in Claude Code](/docs/en/commands) for every built-in and [Extend Claude with skills](/docs/en/skills) for the complete guide to both artifact forms.

### Discover available commands

You can dispatch commands that work without an interactive terminal through the SDK. The `system/init` message lists the ones available in your session in its `slash_commands` field. Commands that need an interactive terminal, such as `/theme` and `/terminal-setup`, don't appear in the list. Access the field when your session starts:

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Hello Claude",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      console.log("Available commands:", message.slash_commands);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage

  async def main():
      async for message in query(prompt="Hello Claude", options=ClaudeAgentOptions(max_turns=1)):
          if isinstance(message, SystemMessage) and message.subtype == "init":
              print("Available commands:", message.data["slash_commands"])

  asyncio.run(main())
  ```
</CodeGroup>

The printed list mixes built-in commands, bundled skills, your user-invocable skills, and `.claude/commands/` files:

```text theme={null}
Available commands: ["clear", "compact", "context", "usage", "code-review", "verify", "security-check", ...]
```

A skill with [`user-invocable: false`](/docs/en/skills#control-who-invokes-a-skill) in its frontmatter doesn't appear in this list or in the `skills` array from [Confirm skills loaded](#confirm-skills-loaded). Sessions that configure [MCP servers](/docs/en/agent-sdk/mcp) can also expose [MCP prompts as commands](/docs/en/mcp#use-mcp-prompts-as-commands).

### Dispatch commands by name

Send a command by including it in your prompt string, the same way you send regular text. Dispatch doesn't depend on the `skills` option. Sending `/<name>` runs a user-invocable skill even when your `skills` list omits it. Commands that act on conversation history, such as `/compact`, need prior messages to work with.

A `/<name>` that matches neither a command in the session nor a built-in Claude Code command doesn't fail the query. Claude Code sends the prompt to Claude as an ordinary message, with a note that the command didn't run, so the query spends a model turn and returns Claude's reply. Before v2.1.274, a `/<name>` that matched nothing returned `Unknown command: /<name>` as the result without a model turn.

A `/<name>` that matches a built-in Claude Code command that isn't available in the session, such as `/theme`, returns `/theme isn't available in this environment.` as the result without a model turn.

<Note>
  A command can hit the `maxTurns` / `max_turns` limit like any other prompt, ending the query with an error result instead of `success`. For the error-result contract, see [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result). If your command might hit the limit, wrap the loop in a `try`/`catch` in TypeScript or `try`/`except` in Python, as shown in [Single Message Input](/docs/en/agent-sdk/streaming-vs-single-mode#single-message-input), or set `maxTurns` high enough for the work to complete.
</Note>

### Compact history with `/compact`

The `/compact` command reduces the size of your conversation history by summarizing older messages while preserving important context. Compaction needs an existing conversation with enough prior messages to summarize. This example has a conversation first, then compacts it and reads the `compact_boundary` system message that reports the result:

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Compaction needs existing history, so have a conversation first
  try {
    for await (const message of query({
      prompt: "Explain what this project does",
      options: { maxTurns: 2 }
    })) {
      if (message.type === "result" && message.subtype === "success") {
        console.log(message.result);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result,
    // so the follow-up query below still runs.
    console.error(`Session ended with an error: ${error}`);
  }

  // Compact the same conversation
  for await (const message of query({
    prompt: "/compact",
    options: { continue: true, maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "compact_boundary") {
      console.log("Compaction completed");
      console.log("Pre-compaction tokens:", message.compact_metadata.pre_tokens);
      console.log("Trigger:", message.compact_metadata.trigger);
      // Example output:
      // Compaction completed
      // Pre-compaction tokens: 1842
      // Trigger: manual
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage, SystemMessage

  async def main():
      # Compaction needs existing history, so have a conversation first
      try:
          async for message in query(
              prompt="Explain what this project does",
              options=ClaudeAgentOptions(max_turns=2),
          ):
              if isinstance(message, ResultMessage) and message.subtype == "success":
                  print(message.result)
      except Exception as error:
          # A single-shot query() raises after yielding an error result,
          # so the follow-up query below still runs.
          print(f"Session ended with an error: {error}")

      # Compact the same conversation
      async for message in query(
          prompt="/compact",
          options=ClaudeAgentOptions(continue_conversation=True, max_turns=1),
      ):
          if isinstance(message, SystemMessage) and message.subtype == "compact_boundary":
              print("Compaction completed")
              print("Pre-compaction tokens:", message.data["compact_metadata"]["pre_tokens"])
              print("Trigger:", message.data["compact_metadata"]["trigger"])
              # Example output:
              # Compaction completed
              # Pre-compaction tokens: 1842
              # Trigger: manual

  asyncio.run(main())
  ```
</CodeGroup>

<Note>
  A `compact_boundary` message only arrives when compaction ran. With nothing to summarize, `/compact` reports the reason instead of raising. The run still ends with a `success` result and no `compact_boundary` message, and the result text carries the reason, for example `Not enough messages to compact.` after a single short exchange. A fresh one-shot `query()` call starts with empty context, so use this pattern in a session with prior turns, for example in [streaming input mode](/docs/en/agent-sdk/streaming-vs-single-mode) or when resuming a session.
</Note>

### Reset context with `/clear`

The `/clear` command resets the conversation to an empty context, so subsequent prompts start with no prior conversation history. The previous conversation remains on disk. You can return to that conversation by passing its session ID to the [`resume` option](/docs/en/agent-sdk/sessions#resume-by-id).

`/clear` is useful in [streaming input mode](/docs/en/agent-sdk/streaming-vs-single-mode), where you send multiple prompts over a single connection. For one-shot `query()` calls, each call already starts with empty context, so sending `/clear` has no practical effect. Start a new `query()` instead.

## Create skills

Create each skill as a directory containing a `SKILL.md` file with YAML frontmatter and Markdown content. The `description` field determines when Claude invokes your skill.

**Example directory structure**:

```text theme={null}
.claude/skills/security-check/
└── SKILL.md
```

### Choose a discovery level

Save skills at either of the two most common [discovery levels](/docs/en/skills#where-skills-live):

* **Project skills**: `.claude/skills/`, available only in the current project
* **Personal skills**: `~/.claude/skills/`, available across all your projects

If you have existing custom command files in `.claude/commands/`, they keep working. A command file at `.claude/commands/deploy.md` creates `/deploy` and works the same way as a skill at `.claude/skills/deploy/SKILL.md` would. If a command file and a skill share a name, see [Resolve skills that share a name](/docs/en/skills#resolve-skills-that-share-a-name) for which one runs. The SDK loads `.claude/commands/` and `~/.claude/commands/` files from the same two scopes as skills. See [Extend Claude with skills](/docs/en/skills) for the complete guide to both artifact forms.

### Create and dispatch your first skill

To see the full flow, create `.claude/skills/security-check/SKILL.md`:

```markdown theme={null}
---
name: security-check
description: Run a security vulnerability scan
---

Analyze the codebase for security vulnerabilities including:
- SQL injection risks
- XSS vulnerabilities
- Exposed credentials
- Insecure configurations
```

Once the file exists, the skill is available through the SDK. Claude invokes it when a request matches its description, and you can dispatch it directly:

<CodeGroup>
  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "/security-check",
    options: { maxTurns: 10 }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      async for message in query(
          prompt="/security-check", options=ClaudeAgentOptions(max_turns=10)
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```
</CodeGroup>

A successful run ends with a `success` result whose text carries the scan findings. Against a small Express app with seeded issues, the result text begins:

```text theme={null}
**Security scan of `app.js` — 4 findings (most severe first):**

1. **SQL Injection** (line 8) — `req.query.name` is concatenated directly into the SQL string. Trivially exploitable (`' OR '1'='1`, `'; DROP TABLE users;--`). **Fix:** use parameterized queries, e.g. `db.query("SELECT * FROM users WHERE name = ?", [req.query.name], cb)`.
...
```

The skill's name also appears in the init message's `slash_commands` array.

<Note>
  Claude Code includes bundled `code-review` and `verify` skills. If you name a `.claude/commands/` file after one of them, for example `.claude/commands/code-review.md`, the file's command shadows the bundled skill and `slash_commands` lists the name once.
</Note>

## Pre-approve tools for skills

<Note>
  For project and personal skills, Claude Code applies the [`allowed-tools`](/docs/en/skills#pre-approve-tools-for-a-skill) frontmatter field in SDK sessions. You can also pre-approve tools for these skills through the `allowedTools` option (`allowed_tools` in Python) in your query configuration. Skills [synced from claude.ai](/docs/en/skills#how-claude-code-handles-the-frontmatter-of-a-synced-skill) follow their own frontmatter rules.
</Note>

Skills run with the session's tools. The example below pre-approves `Read`, `Grep`, and `Glob` with `allowedTools` (`allowed_tools` in Python), so Claude can inspect files while running the [security-check skill](#create-and-dispatch-your-first-skill) without stopping for approval:

<CodeGroup>
  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions

  options = ClaudeAgentOptions(
      setting_sources=["user", "project"],  # Load skills from filesystem
      skills="all",
      allowed_tools=["Read", "Grep", "Glob"],
  )

  async def main():
      async for message in query(prompt="Check this project for security issues", options=options):
          print(message)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Check this project for security issues",
    options: {
      settingSources: ["user", "project"], // Load skills from filesystem
      skills: "all",
      allowedTools: ["Read", "Grep", "Glob"]
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

In the stream, the skill invocation appears as a Skill tool use, followed by Read calls on the project files. The run ends with a `success` result whose text carries the findings.

The list pre-approves the named tools rather than restricting the others. For the full permission flow, including permission modes and the `canUseTool` callback, see [Permissions](/docs/en/agent-sdk/permissions).

## Troubleshooting

### Skills not found

**Check settingSources configuration**: the SDK discovers skills through the `user` and `project` setting sources. If you set `settingSources`/`setting_sources` explicitly and omit those sources, the SDK doesn't load skills:

<CodeGroup>
  ```python Python theme={null}
  # Skills not loaded: setting_sources excludes user and project
  options = ClaudeAgentOptions(setting_sources=[], skills="all")

  # Skills loaded: user and project sources included
  options = ClaudeAgentOptions(
      setting_sources=["user", "project"],
      skills="all",
  )
  ```

  ```typescript TypeScript theme={null}
  // Skills not loaded: settingSources excludes user and project
  const optionsWithoutSkills = {
    settingSources: [],
    skills: "all"
  };

  // Skills loaded: user and project sources included
  const optionsWithSkills = {
    settingSources: ["user", "project"],
    skills: "all"
  };
  ```
</CodeGroup>

For which skill directories each source loads, see the [filesystem sources table](/docs/en/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources). For more details on `settingSources`/`setting_sources`, see the [TypeScript SDK reference](/docs/en/agent-sdk/typescript#settingsource) or [Python SDK reference](/docs/en/agent-sdk/python#settingsource).

**Check working directory**: the SDK loads skills from `.claude/skills/` in the `cwd` option and in every parent directory up to the repository root. Ensure `cwd` points at or below the directory containing `.claude/skills/`, within the same repository:

<CodeGroup>
  ```python Python theme={null}
  # Ensure your cwd points to the directory containing .claude/skills/
  options = ClaudeAgentOptions(
      cwd="/path/to/project",  # .claude/skills/ here or in a parent directory
      setting_sources=["user", "project"],  # Loads skills from these sources
      skills="all",
  )
  ```

  ```typescript TypeScript theme={null}
  // Ensure your cwd points to the directory containing .claude/skills/
  const options = {
    cwd: "/path/to/project", // .claude/skills/ here or in a parent directory
    settingSources: ["user", "project"], // Loads skills from these sources
    skills: "all"
  };
  ```
</CodeGroup>

See [Use skills with the Agent SDK](#use-skills-with-the-agent-sdk) for the complete pattern.

**Verify filesystem location**:

```bash theme={null}
# Check project skills
ls .claude/skills/*/SKILL.md

# Check personal skills
ls ~/.claude/skills/*/SKILL.md
```

### Skill not being used

**Check the `skills` option**: if you passed a `skills` list, confirm the skill's name is included. When Claude tries to invoke an unlisted skill, the Skill tool returns `Skill <name> is not in this session's skills allowlist`. Add the name to your list, or dispatch the skill directly by sending `/<name>` in a prompt, which works without listing.

**Check the description**: ensure it's specific and includes relevant keywords. See [Agent Skills best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#writing-effective-descriptions) for guidance on writing effective descriptions.

### Invalid skill name error

When a name in your `skills` list can't work as an exact skill name, `query()` rejects the list before starting the Claude Code process. Names that trigger the rejection include:

* An empty name
* A name containing parentheses, commas, or control characters
* A name padded with whitespace
* A wildcard form such as a bare `*` or a `:*` suffix

Each SDK surfaces the rejection differently:

  <Tab title="TypeScript">
    The TypeScript SDK throws an `Error` stating the rule the entry broke. For example, `skills: ["docs:*"]` throws:

    ```text theme={null}
    Invalid skill name "docs:*": wildcard-suffix names are not allowed; list each skill by its exact name.
    ```

    An empty name reports `Skill names must be non-empty strings.`

    Before TypeScript Agent SDK 0.3.221, the SDK didn't run this check.
  </Tab>

  <Tab title="Python">
    The Python SDK raises `ValueError` stating the rule the entry broke. For example, `skills=["docs:*"]` raises:

    ```text theme={null}
    ValueError: Invalid skill name 'docs:*': wildcard-suffix names are not allowed; list each skill by its exact name.
    ```

    An empty name reports `Skill names must be non-empty strings`.

    Before Python Agent SDK 0.2.129, the SDK didn't run this check.
  </Tab>

### Additional troubleshooting

For general skills troubleshooting, such as YAML syntax errors and debugging, see the [Claude Code skills troubleshooting section](/docs/en/skills#troubleshooting).

## Next steps

The [Claude Code skills guide](/docs/en/skills) covers authoring in depth. Its guidance applies to SDK sessions. Start with these sections:

* [Frontmatter reference](/docs/en/skills#frontmatter-reference): every supported field
* [Pass arguments to skills](/docs/en/skills#pass-arguments-to-skills): `$ARGUMENTS`, `$0`, `$1`, and skill stacking. The [full substitution table](/docs/en/skills#available-string-substitutions) adds named arguments and the `${CLAUDE_*}` variables
* [Inject dynamic context](/docs/en/skills#inject-dynamic-context): `` !`command` `` lines that run before Claude sees the skill content
* [Choose where skills load](/docs/en/skills#where-skills-live): every skill location, plugin namespacing, and which skill runs when two share a name

## Related resources

* [Commands in Claude Code](/docs/en/commands): the full command surface, including every built-in
* [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): conceptual overview, benefits, and architecture
* [Agent Skills best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): authoring guidelines for effective skills
* [Agent Skills cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction): example skills and templates
* [Subagents in the SDK](/docs/en/agent-sdk/subagents): similar filesystem-based agents with programmatic options
* [SDK overview](/docs/en/agent-sdk/overview): general SDK concepts
* [TypeScript SDK reference](/docs/en/agent-sdk/typescript): complete API documentation
* [Python SDK reference](/docs/en/agent-sdk/python): complete API documentation

---

## Stream responses in real-time

- 官方原文：https://code.claude.com/docs/en/agent-sdk/streaming-output.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-streaming-output.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream responses in real-time

> Get real-time responses from the Agent SDK as text and tool calls stream in

By default, the Agent SDK yields a complete `AssistantMessage` for each non-empty content block, such as a text block or a tool call, after Claude finishes generating that block. To receive incremental updates as text and tool calls are generated, enable partial message streaming.

<Tip>
  This page covers output streaming (receiving tokens in real-time). For input modes (how you send messages), see [Send messages to agents](/docs/en/agent-sdk/streaming-vs-single-mode). You can also [stream responses using the Agent SDK via the CLI](/docs/en/headless).
</Tip>

## Enable streaming output

To enable streaming, set `include_partial_messages` (Python) or `includePartialMessages` (TypeScript) to `true` in your options. This causes the SDK to yield `StreamEvent` messages containing raw API events as they arrive, in addition to the usual `AssistantMessage` and `ResultMessage`.

Your code then needs to:

1. Check each message's type to distinguish `StreamEvent` from other message types
2. For `StreamEvent`, extract the `event` field and check its `type`
3. Look for `content_block_delta` events where `delta.type` is `text_delta`, which contain the actual text chunks

The example below enables streaming and prints text chunks as they arrive. Notice the nested type checks: first for `StreamEvent`, then for `content_block_delta`, then for `text_delta`:

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions
  from claude_agent_sdk.types import StreamEvent
  import asyncio

  async def stream_response():
      options = ClaudeAgentOptions(
          include_partial_messages=True,
          allowed_tools=["Bash", "Read"],
      )

      async for message in query(prompt="List the files in my project", options=options):
          if isinstance(message, StreamEvent):
              event = message.event
              if event.get("type") == "content_block_delta":
                  delta = event.get("delta", {})
                  if delta.get("type") == "text_delta":
                      print(delta.get("text", ""), end="", flush=True)

  asyncio.run(stream_response())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "List the files in my project",
    options: {
      includePartialMessages: true,
      allowedTools: ["Bash", "Read"]
    }
  })) {
    if (message.type === "stream_event") {
      const event = message.event;
      if (event.type === "content_block_delta") {
        if (event.delta.type === "text_delta") {
          process.stdout.write(event.delta.text);
        }
      }
    }
  }
  ```
</CodeGroup>

## StreamEvent reference

When partial messages are enabled, you receive raw Claude API streaming events wrapped in an object. The type has different names in each SDK:

* **Python**: [`StreamEvent`](/docs/en/agent-sdk/python#streamevent) (import from `claude_agent_sdk.types`)
* **TypeScript**: [`SDKPartialAssistantMessage`](/docs/en/agent-sdk/typescript#sdkpartialassistantmessage) with `type: 'stream_event'`

Both contain raw Claude API events, not accumulated text. You need to extract and accumulate text deltas yourself.

The `parent_tool_use_id` field is always `None` in Python and `null` in TypeScript. Stream events are emitted for the main session only; token-level deltas from subagents aren't forwarded. To attribute output to a subagent, use complete messages, which carry `parent_tool_use_id`. See [Detect subagent invocation](/docs/en/agent-sdk/subagents#detect-subagent-invocation).

Claude Code sets `user_message_uuid` on the turn's first non-ping stream event, and again when the message the turn is answering changes, under the conditions in [`user_message_uuid`](/docs/en/agent-sdk/typescript#user_message_uuid). The Python `StreamEvent` doesn't expose this field.

The `event` field contains the raw streaming event from the [Claude API](https://platform.claude.com/docs/en/build-with-claude/streaming#event-types). Common event types include:

| Event Type            | Description                                     |
| :-------------------- | :---------------------------------------------- |
| `message_start`       | Start of a new message                          |
| `content_block_start` | Start of a new content block (text or tool use) |
| `content_block_delta` | Incremental update to content                   |
| `content_block_stop`  | End of a content block                          |
| `message_delta`       | Message-level updates (stop reason, usage)      |
| `message_stop`        | End of the message                              |

## Message flow

Claude Code emits an `AssistantMessage` as each non-empty content block completes, so a response with a text block and a tool call yields two `AssistantMessage` objects. Each one carries only its own content block, and both share the same message ID, which you read as `message.message.id` in TypeScript and `message.message_id` in Python. With partial messages enabled, each `AssistantMessage` arrives before that block's `content_block_stop` event, and you receive messages in this order:

```text theme={null}
StreamEvent (message_start)
StreamEvent (content_block_start) - text block
StreamEvent (content_block_delta) - text chunks...
AssistantMessage - complete text block
StreamEvent (content_block_stop)
StreamEvent (content_block_start) - tool_use block
StreamEvent (content_block_delta) - tool input chunks...
AssistantMessage - complete tool_use block
StreamEvent (content_block_stop)
StreamEvent (message_delta)
StreamEvent (message_stop)
... tool executes ...
... more streaming events for next turn ...
ResultMessage - final result
```

Without partial messages enabled, you receive all message types except `StreamEvent`. Common types include `SystemMessage` (session initialization), `AssistantMessage` (complete content blocks), `ResultMessage` (final result), and a compact boundary message indicating when conversation history was compacted (`SDKCompactBoundaryMessage` in TypeScript; `SystemMessage` with subtype `"compact_boundary"` in Python).

## Stream tool calls

Tool calls also stream incrementally. You can track when tools start, receive their input as it's generated, and see when they complete. The example below tracks the current tool being called and accumulates the JSON input as it streams in. It uses three event types:

* `content_block_start`: tool begins
* `content_block_delta` with `input_json_delta`: input chunks arrive
* `content_block_stop`: tool call complete

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions
  from claude_agent_sdk.types import StreamEvent
  import asyncio

  async def stream_tool_calls():
      options = ClaudeAgentOptions(
          include_partial_messages=True,
          allowed_tools=["Read", "Bash"],
      )

      # Track the current tool and accumulate its input JSON
      current_tool = None
      tool_input = ""

      async for message in query(prompt="Read the README.md file", options=options):
          if isinstance(message, StreamEvent):
              event = message.event
              event_type = event.get("type")

              if event_type == "content_block_start":
                  # New tool call is starting
                  content_block = event.get("content_block", {})
                  if content_block.get("type") == "tool_use":
                      current_tool = content_block.get("name")
                      tool_input = ""
                      print(f"Starting tool: {current_tool}")

              elif event_type == "content_block_delta":
                  delta = event.get("delta", {})
                  if delta.get("type") == "input_json_delta":
                      # Accumulate JSON input as it streams in
                      chunk = delta.get("partial_json", "")
                      tool_input += chunk
                      print(f"  Input chunk: {chunk}")

              elif event_type == "content_block_stop":
                  # Tool call complete - show final input
                  if current_tool:
                      print(f"Tool {current_tool} called with: {tool_input}")
                      current_tool = None

  asyncio.run(stream_tool_calls())
  ```

  ```typescript TypeScript theme={null}

  // Track the current tool and accumulate its input JSON
  let currentTool: string | null = null;
  let toolInput = "";

  for await (const message of query({
    prompt: "Read the README.md file",
    options: {
      includePartialMessages: true,
      allowedTools: ["Read", "Bash"]
    }
  })) {
    if (message.type === "stream_event") {
      const event = message.event;

      if (event.type === "content_block_start") {
        // New tool call is starting
        if (event.content_block.type === "tool_use") {
          currentTool = event.content_block.name;
          toolInput = "";
          console.log(`Starting tool: ${currentTool}`);
        }
      } else if (event.type === "content_block_delta") {
        if (event.delta.type === "input_json_delta") {
          // Accumulate JSON input as it streams in
          const chunk = event.delta.partial_json;
          toolInput += chunk;
          console.log(`  Input chunk: ${chunk}`);
        }
      } else if (event.type === "content_block_stop") {
        // Tool call complete - show final input
        if (currentTool) {
          console.log(`Tool ${currentTool} called with: ${toolInput}`);
          currentTool = null;
        }
      }
    }
  }
  ```
</CodeGroup>

## Build a streaming UI

This example combines text and tool streaming into a cohesive UI. It tracks whether the agent is currently executing a tool (using an `in_tool` flag) to show status indicators like `[Using Read...]` while tools run. Text streams normally when not in a tool, and tool completion triggers a "done" message. This pattern is useful for chat interfaces that need to show progress during multi-step agent tasks.

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
  from claude_agent_sdk.types import StreamEvent
  import asyncio
  import sys

  async def streaming_ui():
      options = ClaudeAgentOptions(
          include_partial_messages=True,
          allowed_tools=["Read", "Bash", "Grep"],
      )

      # Track whether we're currently in a tool call
      in_tool = False

      async for message in query(
          prompt="Find all TODO comments in the codebase", options=options
      ):
          if isinstance(message, StreamEvent):
              event = message.event
              event_type = event.get("type")

              if event_type == "content_block_start":
                  content_block = event.get("content_block", {})
                  if content_block.get("type") == "tool_use":
                      # Tool call is starting - show status indicator
                      tool_name = content_block.get("name")
                      print(f"\n[Using {tool_name}...]", end="", flush=True)
                      in_tool = True

              elif event_type == "content_block_delta":
                  delta = event.get("delta", {})
                  # Only stream text when not executing a tool
                  if delta.get("type") == "text_delta" and not in_tool:
                      sys.stdout.write(delta.get("text", ""))
                      sys.stdout.flush()

              elif event_type == "content_block_stop":
                  if in_tool:
                      # Tool call finished
                      print(" done", flush=True)
                      in_tool = False

          elif isinstance(message, ResultMessage):
              # Agent finished all work
              print(f"\n\n--- Complete ---")

  asyncio.run(streaming_ui())
  ```

  ```typescript TypeScript theme={null}

  // Track whether we're currently in a tool call
  let inTool = false;

  for await (const message of query({
    prompt: "Find all TODO comments in the codebase",
    options: {
      includePartialMessages: true,
      allowedTools: ["Read", "Bash", "Grep"]
    }
  })) {
    if (message.type === "stream_event") {
      const event = message.event;

      if (event.type === "content_block_start") {
        if (event.content_block.type === "tool_use") {
          // Tool call is starting - show status indicator
          process.stdout.write(`\n[Using ${event.content_block.name}...]`);
          inTool = true;
        }
      } else if (event.type === "content_block_delta") {
        // Only stream text when not executing a tool
        if (event.delta.type === "text_delta" && !inTool) {
          process.stdout.write(event.delta.text);
        }
      } else if (event.type === "content_block_stop") {
        if (inTool) {
          // Tool call finished
          console.log(" done");
          inTool = false;
        }
      }
    } else if (message.type === "result") {
      // Agent finished all work
      console.log("\n\n--- Complete ---");
    }
  }
  ```
</CodeGroup>

## Known limitations

* **Structured output**: the JSON result appears only in the final `ResultMessage.structured_output`, not as streaming deltas. See [structured outputs](/docs/en/agent-sdk/structured-outputs) for details.

## Next steps

Now that you can stream text and tool calls in real-time, explore these related topics:

* [Interactive vs one-shot queries](/docs/en/agent-sdk/streaming-vs-single-mode): choose between input modes for your use case
* [Structured outputs](/docs/en/agent-sdk/structured-outputs): get typed JSON responses from the agent
* [Permissions](/docs/en/agent-sdk/permissions): control which tools the agent can use

---

## Streaming Input

- 官方原文：https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-streaming-vs-single-mode.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Streaming Input

> Understanding the two input modes for Claude Agent SDK and when to use each

## Overview

The Claude Agent SDK supports two distinct input modes for interacting with agents:

* **Streaming Input Mode**: a persistent, interactive session
* **Single Message Input**: one-shot queries that use session state and resuming

## Streaming Input Mode (Recommended)

Streaming input mode is the **preferred** way to use the Claude Agent SDK. It provides full access to the agent's capabilities and enables rich, interactive experiences.

It allows the agent to operate as a long lived process that takes in user input, handles interruptions, surfaces permission requests, and handles session management.

### Benefits

In streaming input mode, you work in a persistent session with these capabilities:

* **Image uploads**: attach images directly to messages for visual analysis and understanding
* **Queued messages**: send multiple messages that process sequentially, with ability to interrupt
* **Tool integration**: full access to all tools and custom MCP servers during the session
* **Real-time feedback**: see responses as they're generated, not just final results
* **Context persistence**: maintain conversation context across multiple turns naturally

### Implementation Example

These examples read an image named `diagram.png` from the working directory. Create one there first, or change the filename to point at your own image.

<CodeGroup>
  ```typescript TypeScript theme={null}

  async function* generateMessages(): AsyncGenerator<SDKUserMessage> {
    // First message
    yield {
      type: "user",
      message: {
        role: "user",
        content: "Analyze this codebase for security issues"
      },
      parent_tool_use_id: null
    };

    // Wait for conditions or user input
    await new Promise((resolve) => setTimeout(resolve, 2000));

    // Follow-up with image
    yield {
      type: "user",
      message: {
        role: "user",
        content: [
          {
            type: "text",
            text: "Review this architecture diagram"
          },
          {
            type: "image",
            source: {
              type: "base64",
              media_type: "image/png",
              data: await readFile("diagram.png", "base64")
            }
          }
        ]
      },
      parent_tool_use_id: null
    };
  }

  // Process streaming responses
  for await (const message of query({
    prompt: generateMessages(),
    options: {
      maxTurns: 10,
      allowedTools: ["Read", "Grep"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import (
      ClaudeSDKClient,
      ClaudeAgentOptions,
      AssistantMessage,
      TextBlock,
  )
  import asyncio
  import base64

  async def streaming_analysis():
      async def message_generator():
          # First message
          yield {
              "type": "user",
              "message": {
                  "role": "user",
                  "content": "Analyze this codebase for security issues",
              },
          }

          # Wait for conditions
          await asyncio.sleep(2)

          # Follow-up with image
          with open("diagram.png", "rb") as f:
              image_data = base64.b64encode(f.read()).decode()

          yield {
              "type": "user",
              "message": {
                  "role": "user",
                  "content": [
                      {"type": "text", "text": "Review this architecture diagram"},
                      {
                          "type": "image",
                          "source": {
                              "type": "base64",
                              "media_type": "image/png",
                              "data": image_data,
                          },
                      },
                  ],
              },
          }

      # Use ClaudeSDKClient for streaming input
      options = ClaudeAgentOptions(max_turns=10, allowed_tools=["Read", "Grep"])

      async with ClaudeSDKClient(options) as client:
          # Send streaming input
          await client.query(message_generator())

          # Process responses
          async for message in client.receive_response():
              if isinstance(message, AssistantMessage):
                  for block in message.content:
                      if isinstance(block, TextBlock):
                          print(block.text)

  asyncio.run(streaming_analysis())
  ```
</CodeGroup>

When you run the example, the TypeScript version prints each response as it completes. The Python version's `receive_response()` loop ends at the first result message, so it prints the security analysis; to read both responses, use one `query()` and `receive_response()` pair per message as shown in the [Python reference's example of continuing a conversation](/docs/en/agent-sdk/python#example-continuing-a-conversation).

<Note>
  In the TypeScript SDK, if your message generator throws, for example when a file it reads is missing, the stream ends with an error that reads `Claude Code process aborted by user` instead of the original error, so check the code inside your generator first when you see that message. The error may also be preceded by a long minified line of bundled SDK source, so read to the end of the output for the error text.

  In the Python SDK, a generator exception is logged at debug level and the session stalls without raising, so if a streaming session hangs with no output, enable debug logging and check your generator.
</Note>

## Single Message Input

Single message input is simpler but more limited.

### When to Use Single Message Input

Use single message input when:

* You need a one-shot response
* You do not need image attachments or mid-session control methods
* You need to operate in a stateless environment, such as a lambda function

### Limitations

<Warning>
  Single message input mode does **not** support:

  * Direct image attachments in messages
  * Dynamic message queueing
  * Real-time interruption
  * Natural multi-turn conversations
</Warning>

If a query ends with an error result, such as `error_max_turns`, a single message `query()` call raises an error that includes the failure text after yielding the final result message, so wrap the loop in a try block if your code needs to continue. See [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result) for the result subtypes.

### Implementation Example

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Simple one-shot query
  // query() throws after an error result, such as error_max_turns
  try {
    for await (const message of query({
      prompt: "Explain the authentication flow",
      options: {
        maxTurns: 5,
        allowedTools: ["Read", "Grep"]
      }
    })) {
      if (message.type === "result" && message.subtype === "success") {
        console.log(message.result);
      }
    }
  } catch (error) {
    console.error(`Query failed: ${error}`);
  }

  // Continue conversation with session management
  try {
    for await (const message of query({
      prompt: "Now explain the authorization process",
      options: {
        continue: true,
        maxTurns: 5
      }
    })) {
      if (message.type === "result" && message.subtype === "success") {
        console.log(message.result);
      }
    }
  } catch (error) {
    console.error(`Query failed: ${error}`);
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage
  import asyncio

  async def single_message_example():
      # Simple one-shot query using query() function
      # query() raises ResultError after an error result, such as error_max_turns
      try:
          async for message in query(
              prompt="Explain the authentication flow",
              options=ClaudeAgentOptions(max_turns=5, allowed_tools=["Read", "Grep"]),
          ):
              if isinstance(message, ResultMessage) and message.subtype == "success":
                  print(message.result)
      except Exception as e:
          print(f"Query failed: {e}")

      # Continue conversation with session management
      try:
          async for message in query(
              prompt="Now explain the authorization process",
              options=ClaudeAgentOptions(continue_conversation=True, max_turns=5),
          ):
              if isinstance(message, ResultMessage) and message.subtype == "success":
                  print(message.result)
      except Exception as e:
          print(f"Query failed: {e}")

  asyncio.run(single_message_example())
  ```
</CodeGroup>

When you run the example, each query prints its final result text: first the authentication explanation, then the authorization explanation.

---

## Get structured output from agents

- 官方原文：https://code.claude.com/docs/en/agent-sdk/structured-outputs.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-structured-outputs.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get structured output from agents

> Return validated JSON from agent workflows using JSON Schema, Zod, or Pydantic. Get type-safe, structured data after multi-turn tool use.

Structured outputs let you define the exact shape of data you want back from an agent. The agent can use any tools it needs to complete the task, and you still get validated JSON matching your schema at the end. Define a [JSON Schema](https://json-schema.org/understanding-json-schema/about) for the structure you need, and the SDK validates the output against it, re-prompting on mismatch. If validation does not succeed within the retry limit, the result is an error instead of structured data; see [Error handling](#error-handling).

For full type safety, use [Zod](#type-safe-schemas-with-zod-and-pydantic) (TypeScript) or [Pydantic](#type-safe-schemas-with-zod-and-pydantic) (Python) to define your schema and get strongly-typed objects back.

## Why structured outputs?

Agents return free-form text by default, which works for chat but not when you need to use the output programmatically. Structured outputs give you typed data you can pass directly to your application logic, database, or UI components.

Consider a recipe app where an agent searches the web and brings back recipes. Without structured outputs, you get free-form text that you'd need to parse yourself. With structured outputs, you define the shape you want and get typed data you can use directly in your app.

<AccordionGroup>
  <Accordion title="Without structured outputs">
    ```text theme={null}
    Here's a classic chocolate chip cookie recipe!

    **Chocolate Chip Cookies**
    Prep time: 15 minutes | Cook time: 10 minutes

    Ingredients:
    - 2 1/4 cups all-purpose flour
    - 1 cup butter, softened
    ...
    ```

    To use this in your app, you'd need to parse out the title, convert "15 minutes" to a number, separate ingredients from instructions, and handle inconsistent formatting across responses.
  </Accordion>

  <Accordion title="With structured outputs">
    ```jsonc theme={null}
    {
      "name": "Chocolate Chip Cookies",
      "prep_time_minutes": 15,
      "cook_time_minutes": 10,
      "ingredients": [
        { "item": "all-purpose flour", "amount": 2.25, "unit": "cups" },
        { "item": "butter, softened", "amount": 1, "unit": "cup" }
        // ...
      ],
      "steps": ["Preheat oven to 375°F", "Cream butter and sugar" /* ... */]
    }
    ```

    Typed data you can use directly in your UI.
  </Accordion>
</AccordionGroup>

## Quick start

To use structured outputs, define a [JSON Schema](https://json-schema.org/understanding-json-schema/about) describing the shape of data you want, then pass it to `query()` via the `outputFormat` option (TypeScript) or `output_format` option (Python). When the agent finishes, the result message includes a `structured_output` field with validated data matching your schema.

The example below asks the agent to research Anthropic and return the company name, year founded, and headquarters as structured output.

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Define the shape of data you want back
  const schema = {
    type: "object",
    properties: {
      company_name: { type: "string" },
      founded_year: { type: "number" },
      headquarters: { type: "string" }
    },
    required: ["company_name"]
  };

  try {
    for await (const message of query({
      prompt: "Research Anthropic and provide key company information",
      options: {
        outputFormat: {
          type: "json_schema",
          schema: schema
        }
      }
    })) {
      // The result message contains structured_output with validated data
      if (message.type === "result" && message.subtype === "success" && message.structured_output) {
        console.log(message.structured_output);
        // { company_name: "Anthropic", founded_year: 2021, headquarters: "San Francisco, CA" }
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result, such as
    // error_max_structured_output_retries; see the Error handling section.
    console.error(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  # Define the shape of data you want back
  schema = {
      "type": "object",
      "properties": {
          "company_name": {"type": "string"},
          "founded_year": {"type": "number"},
          "headquarters": {"type": "string"},
      },
      "required": ["company_name"],
  }

  async def main():
      try:
          async for message in query(
              prompt="Research Anthropic and provide key company information",
              options=ClaudeAgentOptions(
                  output_format={"type": "json_schema", "schema": schema}
              ),
          ):
              # The result message contains structured_output with validated data
              if isinstance(message, ResultMessage) and message.structured_output:
                  print(message.structured_output)
                  # {'company_name': 'Anthropic', 'founded_year': 2021, 'headquarters': 'San Francisco, CA'}
      except Exception as error:
          # A single-shot query() raises after yielding an error result, such as
          # error_max_structured_output_retries; see the Error handling section.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

## Type-safe schemas with Zod and Pydantic

Instead of writing JSON Schema by hand, you can use [Zod](https://zod.dev/) (TypeScript) or [Pydantic](https://docs.pydantic.dev/latest/) (Python) to define your schema. These libraries generate the JSON Schema for you and let you parse the response into a fully-typed object you can use throughout your codebase with autocomplete and type checking.

The example below defines a schema for a feature implementation plan with a summary, list of steps (each with complexity level), and potential risks. The agent plans the feature and returns a typed `FeaturePlan` object. You can then access properties like `plan.summary` and iterate over `plan.steps` with full type safety.

The SDK validates schemas with JSON Schema draft-07, so schemas that declare a newer version are rejected. Zod targets draft 2020-12 by default, so pass `target: "draft-7"` when converting your schema.

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Define schema with Zod
  const FeaturePlan = z.object({
    feature_name: z.string(),
    summary: z.string(),
    steps: z.array(
      z.object({
        step_number: z.number(),
        description: z.string(),
        estimated_complexity: z.enum(["low", "medium", "high"])
      })
    ),
    risks: z.array(z.string())
  });

  type FeaturePlan = z.infer<typeof FeaturePlan>;

  // Convert to JSON Schema using the draft-07 target the SDK expects
  const schema = z.toJSONSchema(FeaturePlan, { target: "draft-7" });

  // Use in query
  try {
    for await (const message of query({
      prompt:
        "Plan how to add dark mode support to a React app. Break it into implementation steps.",
      options: {
        outputFormat: {
          type: "json_schema",
          schema: schema
        }
      }
    })) {
      if (message.type === "result" && message.subtype === "success" && message.structured_output) {
        // Validate and get fully typed result
        const parsed = FeaturePlan.safeParse(message.structured_output);
        if (parsed.success) {
          const plan: FeaturePlan = parsed.data;
          console.log(`Feature: ${plan.feature_name}`);
          console.log(`Summary: ${plan.summary}`);
          plan.steps.forEach((step) => {
            console.log(`${step.step_number}. [${step.estimated_complexity}] ${step.description}`);
          });
        }
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result, such as
    // error_max_structured_output_retries; see the Error handling section.
    console.error(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio
  from pydantic import BaseModel
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  class Step(BaseModel):
      step_number: int
      description: str
      estimated_complexity: str  # 'low', 'medium', 'high'

  class FeaturePlan(BaseModel):
      feature_name: str
      summary: str
      steps: list[Step]
      risks: list[str]

  async def main():
      try:
          async for message in query(
              prompt="Plan how to add dark mode support to a React app. Break it into implementation steps.",
              options=ClaudeAgentOptions(
                  output_format={
                      "type": "json_schema",
                      "schema": FeaturePlan.model_json_schema(),
                  }
              ),
          ):
              if isinstance(message, ResultMessage) and message.structured_output:
                  # Validate and get fully typed result
                  plan = FeaturePlan.model_validate(message.structured_output)
                  print(f"Feature: {plan.feature_name}")
                  print(f"Summary: {plan.summary}")
                  for step in plan.steps:
                      print(
                          f"{step.step_number}. [{step.estimated_complexity}] {step.description}"
                      )
      except Exception as error:
          # A single-shot query() raises after yielding an error result, such as
          # error_max_structured_output_retries; see the Error handling section.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

## Output format configuration

The `outputFormat` (TypeScript) or `output_format` (Python) option accepts an object with:

* `type`: Set to `"json_schema"` for structured outputs
* `schema`: A [JSON Schema](https://json-schema.org/understanding-json-schema/about) object defining your output structure. You can generate this from a Zod schema with `z.toJSONSchema(schema, { target: "draft-7" })` or a Pydantic model with `.model_json_schema()`

The SDK supports standard JSON Schema features including all basic types (object, array, string, number, boolean, null), `enum`, `const`, `required`, nested objects, and `$ref` definitions. For the full list of supported features and limitations, see [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations).

A schema that isn't valid JSON Schema fails the run at startup with an error naming the problem. Before v2.1.205, an invalid schema was silently ignored and the agent returned unstructured text.

The `format` keyword, such as `"format": "email"`, is accepted as an annotation and isn't enforced by the SDK's validator. Before v2.1.205, any schema containing `format` was treated as invalid.

## Example: TODO tracking agent

This example demonstrates how structured outputs work with multi-step tool use. The agent needs to find TODO comments in the codebase, then look up git blame information for each one. It autonomously decides which tools to use (Grep to search, Bash to run git commands) and combines the results into a single structured response.

The schema includes optional fields (`author` and `date`) since git blame information might not be available for all files. The agent fills in what it can find and omits the rest.

<CodeGroup>
  ```typescript TypeScript theme={null}

  // Define structure for TODO extraction
  const todoSchema = {
    type: "object",
    properties: {
      todos: {
        type: "array",
        items: {
          type: "object",
          properties: {
            text: { type: "string" },
            file: { type: "string" },
            line: { type: "number" },
            author: { type: "string" },
            date: { type: "string" }
          },
          required: ["text", "file", "line"]
        }
      },
      total_count: { type: "number" }
    },
    required: ["todos", "total_count"]
  };

  // Agent uses Grep to find TODOs, Bash to get git blame info
  try {
    for await (const message of query({
      prompt: "Find all TODO comments in this codebase and identify who added them",
      options: {
        outputFormat: {
          type: "json_schema",
          schema: todoSchema
        }
      }
    })) {
      if (message.type === "result" && message.subtype === "success" && message.structured_output) {
        const data = message.structured_output as { total_count: number; todos: Array<{ file: string; line: number; text: string; author?: string; date?: string }> };
        console.log(`Found ${data.total_count} TODOs`);
        data.todos.forEach((todo) => {
          console.log(`${todo.file}:${todo.line} - ${todo.text}`);
          if (todo.author) {
            console.log(`  Added by ${todo.author} on ${todo.date}`);
          }
        });
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result, such as
    // error_max_structured_output_retries; see the Error handling section.
    console.error(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  # Define structure for TODO extraction
  todo_schema = {
      "type": "object",
      "properties": {
          "todos": {
              "type": "array",
              "items": {
                  "type": "object",
                  "properties": {
                      "text": {"type": "string"},
                      "file": {"type": "string"},
                      "line": {"type": "number"},
                      "author": {"type": "string"},
                      "date": {"type": "string"},
                  },
                  "required": ["text", "file", "line"],
              },
          },
          "total_count": {"type": "number"},
      },
      "required": ["todos", "total_count"],
  }

  async def main():
      # Agent uses Grep to find TODOs, Bash to get git blame info
      try:
          async for message in query(
              prompt="Find all TODO comments in this codebase and identify who added them",
              options=ClaudeAgentOptions(
                  output_format={"type": "json_schema", "schema": todo_schema}
              ),
          ):
              if isinstance(message, ResultMessage) and message.structured_output:
                  data = message.structured_output
                  print(f"Found {data['total_count']} TODOs")
                  for todo in data["todos"]:
                      print(f"{todo['file']}:{todo['line']} - {todo['text']}")
                      if "author" in todo:
                          print(f"  Added by {todo['author']} on {todo['date']}")
      except Exception as error:
          # A single-shot query() raises after yielding an error result, such as
          # error_max_structured_output_retries; see the Error handling section.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

## Error handling

Structured output generation can fail when the agent cannot produce valid JSON matching your schema. This typically happens when the schema is too complex for the task, the task itself is ambiguous, or the agent hits its retry limit trying to fix validation errors. It can also happen without any validation failure: a [model fallback](/docs/en/model-config#automatic-model-fallback) can retract an already-completed output mid-stream, and if no retry replaces it the run ends with the same error. Check the `errors` list on the result message to tell the two causes apart before debugging your schema.

When an error occurs, the result message has a `subtype` indicating what went wrong:

| Subtype                               | Meaning                                                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `success`                             | Output was generated and validated successfully                                                                                 |
| `error_max_structured_output_retries` | No valid output remained after multiple attempts (validation failures, or a model-fallback retraction with no successful retry) |

A result can also end with subtype `success` but no `structured_output` value, for example when the run completes without the agent producing a structured output. Treat that case as a failure as well. The troubleshooting entry [structured\_output is None but the result says success](/docs/en/agent-sdk/troubleshooting#structured_output-is-none-but-the-result-says-success) covers this case. The example below treats a result as successful only when the `subtype` is `success` and `structured_output` is present, and handles every other result as a failure:

<CodeGroup>
  ```typescript TypeScript theme={null}

  const contactSchema = {
    type: "object",
    properties: {
      name: { type: "string" },
      email: { type: "string" }
    },
    required: ["name"]
  };

  try {
    for await (const msg of query({
      prompt: "Extract contact info from the document",
      options: {
        outputFormat: {
          type: "json_schema",
          schema: contactSchema
        }
      }
    })) {
      if (msg.type === "result") {
        if (msg.subtype === "success" && msg.structured_output) {
          // Use the validated output
          console.log(msg.structured_output);
        } else if (msg.subtype === "error_max_structured_output_retries") {
          console.error("Could not produce valid output");
        } else {
          console.error("Run ended without a structured output");
        }
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result. If the
    // failure was an error result, the error subtype branches above have
    // already run; connection or process failures yield no result message.
    console.log(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  contact_schema = {
      "type": "object",
      "properties": {
          "name": {"type": "string"},
          "email": {"type": "string"},
      },
      "required": ["name"],
  }

  async def main():
      try:
          async for message in query(
              prompt="Extract contact info from the document",
              options=ClaudeAgentOptions(
                  output_format={"type": "json_schema", "schema": contact_schema}
              ),
          ):
              if isinstance(message, ResultMessage):
                  if message.subtype == "success" and message.structured_output:
                      # Use the validated output
                      print(message.structured_output)
                  elif message.subtype == "error_max_structured_output_retries":
                      print("Could not produce valid output")
                  else:
                      print("Run ended without a structured output")
      except Exception as error:
          # A single-shot query() raises after yielding an error result. If the
          # failure was an error result, the error subtype branches above have
          # already run; connection or process failures yield no result message.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

**Tips for avoiding errors:**

* **Keep schemas focused.** Deeply nested schemas with many required fields are harder to satisfy. Start simple and add complexity as needed.
* **Match schema to task.** If the task might not have all the information your schema requires, make those fields optional.
* **Use clear prompts.** Ambiguous prompts make it harder for the agent to know what output to produce.

## Related resources

* [JSON Schema documentation](https://json-schema.org/): learn JSON Schema syntax for defining complex schemas with nested objects, arrays, enums, and validation constraints
* [API Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs): use structured outputs with the Claude API directly for single-turn requests without tool use
* [Custom tools](/docs/en/agent-sdk/custom-tools): give your agent custom tools to call during execution before returning structured output

---

## Subagents in the SDK

- 官方原文：https://code.claude.com/docs/en/agent-sdk/subagents.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-subagents.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subagents in the SDK

> Define and invoke subagents to isolate context, run tasks in parallel, and apply specialized instructions in your Claude Agent SDK applications.

Subagents are separate agent instances that your main agent can spawn to handle focused subtasks.
Use them to isolate context, run multiple analyses in parallel, and apply specialized instructions without adding to the main agent's prompt.

## Overview

You can create subagents in three ways:

* **Programmatically**: use the `agents` parameter in your `query()` options. See the [TypeScript](/docs/en/agent-sdk/typescript#agentdefinition) and [Python](/docs/en/agent-sdk/python#agentdefinition) references
* **Filesystem-based**: define agents as markdown files in `.claude/agents/` directories. See [defining subagents as files](/docs/en/sub-agents)
* **Built-in general-purpose**: Claude can invoke the built-in `general-purpose` subagent at any time via the Agent tool without you defining anything

This guide focuses on the programmatic approach, which is recommended for SDK applications.

## Benefits of using subagents

Because subagents are separate agent instances, delegating work to them gives you four benefits:

* **Context isolation**: each subagent runs in its own conversation, which starts fresh unless the subagent is a [fork](/docs/en/sub-agents#fork-the-current-conversation). Either way, intermediate tool calls and results stay inside the subagent; only its final message returns to the parent. A `research-assistant` subagent can explore dozens of files without any of that content accumulating in the main conversation. The parent receives a concise summary, not every file the subagent read. See [What subagents inherit](#what-subagents-inherit) for exactly what's in the subagent's context.
* **Parallelization**: multiple subagents can run concurrently, so independent subtasks finish in the time of the slowest one rather than the sum of all of them. During a code review, you can run `style-checker`, `security-scanner`, and `test-coverage` subagents simultaneously instead of sequentially.
* **Specialized instructions and knowledge**: each subagent can have a tailored system prompt with specific expertise, best practices, and constraints. A `database-migration` subagent can have detailed knowledge about SQL best practices, rollback strategies, and data integrity checks that would be unnecessary noise in the main agent's instructions.
* **Tool restrictions**: subagents can be limited to specific tools, reducing the risk of unintended actions. A `doc-reviewer` subagent might only have access to Read and Grep tools, ensuring it can analyze but never accidentally modify your documentation files.

## Create subagents

### Programmatic definition (recommended)

Define subagents directly in your code using the `agents` parameter. Claude invokes subagents through the `Agent` tool.

Most examples on this page print only the final result. To confirm that Claude delegated to a subagent rather than answering directly, see [Detect subagent invocation](#detect-subagent-invocation).

This example creates two subagents: a code reviewer with read-only access and a test runner that can execute commands.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

  async def main():
      async for message in query(
          prompt="Review the authentication module for security issues",
          options=ClaudeAgentOptions(
              # Auto-approve these tools
              allowed_tools=["Read", "Grep", "Glob", "Agent"],
              agents={
                  "code-reviewer": AgentDefinition(
                      # description tells Claude when to use this subagent
                      description="Expert code review specialist. Use for quality, security, and maintainability reviews.",
                      # prompt defines the subagent's behavior and expertise
                      prompt="""You are a code review specialist with expertise in security, performance, and best practices.

  When reviewing code:
  - Identify security vulnerabilities
  - Check for performance issues
  - Verify adherence to coding standards
  - Suggest specific improvements

  Be thorough but concise in your feedback.""",
                      # tools restricts what the subagent can do (read-only here)
                      tools=["Read", "Grep", "Glob"],
                      # model overrides the default model for this subagent
                      model="sonnet",
                  ),
                  "test-runner": AgentDefinition(
                      description="Runs and analyzes test suites. Use for test execution and coverage analysis.",
                      prompt="""You are a test execution specialist. Run tests and provide clear analysis of results.

  Focus on:
  - Running test commands
  - Analyzing test output
  - Identifying failing tests
  - Suggesting fixes for failures""",
                      # Bash access lets this subagent run test commands
                      tools=["Bash", "Read", "Grep"],
                  ),
              },
          ),
      ):
          if hasattr(message, "result"):
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Review the authentication module for security issues",
    options: {
      // Auto-approve these tools
      allowedTools: ["Read", "Grep", "Glob", "Agent"],
      agents: {
        "code-reviewer": {
          // description tells Claude when to use this subagent
          description:
            "Expert code review specialist. Use for quality, security, and maintainability reviews.",
          // prompt defines the subagent's behavior and expertise
          prompt: `You are a code review specialist with expertise in security, performance, and best practices.

  When reviewing code:
  - Identify security vulnerabilities
  - Check for performance issues
  - Verify adherence to coding standards
  - Suggest specific improvements

  Be thorough but concise in your feedback.`,
          // tools restricts what the subagent can do (read-only here)
          tools: ["Read", "Grep", "Glob"],
          // model overrides the default model for this subagent
          model: "sonnet"
        },
        "test-runner": {
          description:
            "Runs and analyzes test suites. Use for test execution and coverage analysis.",
          prompt: `You are a test execution specialist. Run tests and provide clear analysis of results.

  Focus on:
  - Running test commands
  - Analyzing test output
  - Identifying failing tests
  - Suggesting fixes for failures`,
          // Bash access lets this subagent run test commands
          tools: ["Bash", "Read", "Grep"]
        }
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

### AgentDefinition configuration

| Field             | Type                                                        | Required | Description                                                                                                                                                                                                                                                                                                                                |
| :---------------- | :---------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`     | `string`                                                    | Yes      | Natural language description of when to use this agent                                                                                                                                                                                                                                                                                     |
| `prompt`          | `string`                                                    | Yes      | The agent's system prompt defining its role and behavior                                                                                                                                                                                                                                                                                   |
| `tools`           | `string[]`                                                  | No       | Array of allowed tool names. If omitted, inherits every [tool available to subagents](/docs/en/sub-agents#available-tools)                                                                                                                                                                                                                      |
| `disallowedTools` | `string[]`                                                  | No       | Array of tool names to remove from the agent's tool set. MCP server-level patterns are also accepted: `mcp__server` or `mcp__server__*` removes every tool from that server, and `mcp__*` removes every MCP tool from any server                                                                                                           |
| `model`           | `string`                                                    | No       | Model override for this agent. Accepts an alias such as `'fable'`, `'opus'`, `'sonnet'`, `'haiku'`, `'inherit'`, or a full model ID. `'inherit'` uses the main model. When you omit it, Claude Code picks the model in the [subagent model order](/docs/en/sub-agents#choose-a-model)                                                           |
| `skills`          | `string[]`                                                  | No       | List of skill names to preload into the agent's context at startup. Unlisted skills remain invocable through the Skill tool                                                                                                                                                                                                                |
| `memory`          | `'user' \| 'project' \| 'local'`                            | No       | Memory source for this agent                                                                                                                                                                                                                                                                                                               |
| `mcpServers`      | `(string \| object)[]`                                      | No       | MCP servers available to this agent, by name or inline config                                                                                                                                                                                                                                                                              |
| `initialPrompt`   | `string`                                                    | No       | Auto-submitted as the first user turn when this agent runs as the main thread agent. Ignored when the agent is invoked as a subagent                                                                                                                                                                                                       |
| `maxTurns`        | `number`                                                    | No       | Maximum number of agentic turns before the agent stops. When the agent reaches the limit, Claude Code returns its output marked as partial, and you can [resume the agent](#resume-subagents) to continue. The partial marking requires Claude Code v2.1.246 or later                                                                      |
| `background`      | `boolean`                                                   | No       | Run this agent as a non-blocking background task when invoked                                                                                                                                                                                                                                                                              |
| `omitClaudeMd`    | `boolean`                                                   | No       | Run this agent without the user, project, and local CLAUDE.md files when it runs as a subagent; managed policy files still load. Ignored when the agent runs as the main thread agent. Requires TypeScript Agent SDK v0.3.271 or later. The Python SDK's [`AgentDefinition`](/docs/en/agent-sdk/python#agentdefinition) doesn't have this field |
| `effort`          | `'low' \| 'medium' \| 'high' \| 'xhigh' \| 'max' \| number` | No       | Reasoning effort level for this agent                                                                                                                                                                                                                                                                                                      |
| `permissionMode`  | `PermissionMode`                                            | No       | Permission mode for tool execution within this agent. The [subagent inheritance rules](/docs/en/agent-sdk/permissions#available-modes) decide when it applies                                                                                                                                                                                   |

In the Python SDK, multi-word field names such as `disallowedTools` and `mcpServers` keep their camelCase spelling to match the wire format rather than following Python's snake\_case convention. See the [`AgentDefinition` reference](/docs/en/agent-sdk/python#agentdefinition) for details.

Subagents run in the background by default. An Agent tool call that omits the [`run_in_background`](/docs/en/sub-agents#run-subagents-in-foreground-or-background) input launches a background subagent, and Claude sets `run_in_background: false` when it needs the result before continuing. Set the `background` field to `true` to force background execution for a specific agent regardless of what Claude requests. Before Claude Code v2.1.198, the background default was rolling out gradually, and an Agent tool call that omitted `run_in_background` could run the subagent synchronously.

Subagents can also spawn subagents of their own. To limit how deep that nesting goes, how many subagents run at once, and how much a query spends, see [Cap subagent depth, concurrency, and spend](#cap-subagent-depth-concurrency-and-spend).

### Filesystem-based definition (alternative)

You can also define subagents as markdown files in `.claude/agents/` directories. See the [Claude Code subagents documentation](/docs/en/sub-agents) for details on this approach. Programmatically defined agents take precedence over filesystem-based agents with the same name.

<Note>
  When Claude calls the Agent tool without a `subagent_type`, it gets the built-in `general-purpose` subagent, which Claude can spawn even when you define no agents of your own. Setting [`CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1`](/docs/en/env-vars) removes that default, and such a call fails with [`subagent_type is required`](/docs/en/errors#subagent-type-is-required).
</Note>

## What subagents inherit

Unless the subagent is a [fork](/docs/en/sub-agents#fork-the-current-conversation), its context window starts fresh, with no parent conversation, but isn't empty. The only content you pass from parent to subagent is the Agent tool's prompt string, so include any file paths, error messages, or decisions the subagent needs directly in that prompt.

A subagent that has the [`SendMessage`](/docs/en/tools-reference) tool starts with a list of the other named agents running in the session, so it knows which names it can send messages to. Claude Code adds the list to the subagent's first turn automatically. A [fork](/docs/en/sub-agents#fork-the-current-conversation) doesn't get the list because it inherits the parent conversation instead.

A subagent also inherits the main session's extended thinking configuration.

The table below lists what a non-fork subagent's context contains and what it leaves out.

| The subagent receives                                                                                                                                                                                         | The subagent doesn't receive                                       |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------- |
| Its own system prompt (`AgentDefinition.prompt`) and the Agent tool's prompt                                                                                                                                  | The parent's conversation history or tool results                  |
| Project CLAUDE.md (loaded via [`settingSources`](/docs/en/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources)), unless the agent sets [`omitClaudeMd`](#agentdefinition-configuration) | Preloaded skill content, unless listed in `AgentDefinition.skills` |
| Tool definitions (inherited from parent or the subset in `tools`, [filtered for background runs](/docs/en/sub-agents#available-tools))                                                                             | The parent's system prompt                                         |

<Note>
  The parent receives the subagent's final message as the Agent tool result, but may summarize it in its own response. To preserve subagent output verbatim in the user-facing response, include an instruction to do so in the prompt or `systemPrompt` option you pass to the main `query()` call.

  In v2.1.210 and later, Claude Code [scans the final message for instruction-shaped patterns](/docs/en/sub-agents#subagent-output-scanning) before the parent reads it. The scan treats three kinds of pattern differently:

  * **Control-tag imitation**: Claude Code neutralizes a tag that only the harness emits, such as a `<system-reminder>` block, in place. It inserts a backslash after the opening angle bracket and deletes nothing.
  * **Permission-configuration mentions**: Claude Code keeps references to the permission configuration, such as `.claude/settings.json`, `bypassPermissions`, or `--dangerously-skip-permissions`, as written.
  * **Turn markers**: a line that starts with `Human:` or `Assistant:` gets a backslash before the colon, so the message can't imitate a conversation turn boundary.

  For a control-tag or permission-configuration match, Claude Code prepends a `[harness: ...]` marker line naming the matched patterns; a turn-marker match doesn't add the marker line. Those are the only modifications the scan makes: it never removes or rewords the subagent's text.
</Note>

An API error that ends the subagent early, such as a rate limit, is never delivered as its result. See [API errors in subagents](/docs/en/sub-agents#api-errors-in-subagents) for the foreground and background behavior.

## Invoke subagents

### Automatic invocation

Claude automatically decides when to invoke subagents based on the task and each subagent's `description`. For example, if you define a `performance-optimizer` subagent with the description "Performance optimization specialist for query tuning", Claude will invoke it when your prompt mentions optimizing queries.

Write clear, specific descriptions so Claude can match tasks to the right subagent.

### Explicit invocation

To guarantee Claude uses a specific subagent, mention it by name in your prompt:

```text theme={null}
"Use the code-reviewer agent to check the authentication module"
```

This bypasses automatic matching and directly invokes the named subagent.

### Dynamic agent configuration

You can create agent definitions dynamically based on runtime conditions. This example creates a security reviewer with different strictness levels, using a more capable model for strict reviews.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

  # Factory function that returns an AgentDefinition
  # This pattern lets you customize agents based on runtime conditions
  def create_security_agent(security_level: str) -> AgentDefinition:
      is_strict = security_level == "strict"
      return AgentDefinition(
          description="Security code reviewer",
          # Customize the prompt based on strictness level
          prompt=f"You are a {'strict' if is_strict else 'balanced'} security reviewer...",
          tools=["Read", "Grep", "Glob"],
          # Key insight: use a more capable model for high-stakes reviews
          model="opus" if is_strict else "sonnet",
      )

  async def main():
      # The agent is created at query time, so each request can use different settings
      async for message in query(
          prompt="Review this PR for security issues",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Grep", "Glob", "Agent"],
              agents={
                  # Call the factory with your desired configuration
                  "security-reviewer": create_security_agent("strict")
              },
          ),
      ):
          if hasattr(message, "result"):
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Factory function that returns an AgentDefinition
  // This pattern lets you customize agents based on runtime conditions
  function createSecurityAgent(securityLevel: "basic" | "strict"): AgentDefinition {
    const isStrict = securityLevel === "strict";
    return {
      description: "Security code reviewer",
      // Customize the prompt based on strictness level
      prompt: `You are a ${isStrict ? "strict" : "balanced"} security reviewer...`,
      tools: ["Read", "Grep", "Glob"],
      // Key insight: use a more capable model for high-stakes reviews
      model: isStrict ? "opus" : "sonnet"
    };
  }

  // The agent is created at query time, so each request can use different settings
  for await (const message of query({
    prompt: "Review this PR for security issues",
    options: {
      allowedTools: ["Read", "Grep", "Glob", "Agent"],
      agents: {
        // Call the factory with your desired configuration
        "security-reviewer": createSecurityAgent("strict")
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

## Detect subagent invocation

Claude invokes subagents through the Agent tool. To detect when a subagent is invoked, check for `tool_use` blocks where `name` is `"Agent"`. Messages from within a subagent's context include a `parent_tool_use_id` field.

<Note>
  The tool appears as `"Agent"` in `tool_use` blocks but as `"Task"` in the `system:init` tools list. Before Claude Code v2.1.63, `tool_use` blocks also named it `"Task"`. To keep detection working across SDK versions, match both values in `block.name`.
</Note>

The message structure differs between SDKs. In Python, you access content blocks directly via `message.content`. In TypeScript, `SDKAssistantMessage` wraps the Claude API message, so you access content via `message.message.content`.

This example iterates through streamed messages, logging when a subagent is invoked and when subsequent messages originate from within that subagent's execution context.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, ToolUseBlock

  async def main():
      async for message in query(
          prompt="Use the code-reviewer agent to review this codebase",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Glob", "Grep", "Agent"],
              agents={
                  "code-reviewer": AgentDefinition(
                      description="Expert code reviewer.",
                      prompt="Analyze code quality and suggest improvements.",
                      tools=["Read", "Glob", "Grep"],
                  )
              },
          ),
      ):
          # Check for subagent invocation. Match both names: older SDK
          # versions emitted "Task", current versions emit "Agent".
          if hasattr(message, "content") and message.content:
              for block in message.content:
                  if isinstance(block, ToolUseBlock) and block.name in (
                      "Task",
                      "Agent",
                  ):
                      print(f"Subagent invoked: {block.input.get('subagent_type')}")

          # Check if this message is from within a subagent's context
          if hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id:
              print("  (running inside subagent)")

          if hasattr(message, "result"):
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Use the code-reviewer agent to review this codebase",
    options: {
      allowedTools: ["Read", "Glob", "Grep", "Agent"],
      agents: {
        "code-reviewer": {
          description: "Expert code reviewer.",
          prompt: "Analyze code quality and suggest improvements.",
          tools: ["Read", "Glob", "Grep"]
        }
      }
    }
  })) {
    const msg = message as any;

    // Check for subagent invocation. Match both names: older SDK versions
    // emitted "Task", current versions emit "Agent".
    for (const block of msg.message?.content ?? []) {
      if (block.type === "tool_use" && (block.name === "Task" || block.name === "Agent")) {
        console.log(`Subagent invoked: ${block.input.subagent_type}`);
      }
    }

    // Check if this message is from within a subagent's context
    if (msg.parent_tool_use_id) {
      console.log("  (running inside subagent)");
    }

    if ("result" in message) {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

## Resume subagents

You can resume a subagent to continue where it left off rather than starting fresh. A resumed subagent retains its full conversation history, including all previous tool calls, results, and reasoning.

When a subagent stops at its [`maxTurns`](#agentdefinition-configuration) limit, Claude Code marks the output in the Agent tool result as partial, so Claude knows the run is unfinished.

When a subagent completes, the Agent tool result includes a text block containing `agentId: <id>`. The built-in [`Explore` and `Plan` agents](/docs/en/sub-agents#built-in-subagents) are one-shot and don't return an `agentId`, so use a custom agent or `general-purpose` when you need to resume. To resume a subagent programmatically:

1. **Capture the session ID**: extract `session_id` from messages during the first query
2. **Extract the agent ID**: parse `agentId` from the Agent tool result text
3. **Resume the session**: pass `resume: sessionId` in the second query's options, and include the agent ID in your prompt. Each `query()` call starts a new session by default, and you must resume the same session to access the subagent's transcript.

<Note>
  When using a custom agent, pass the same agent definition in the `agents` parameter for both queries.
</Note>

The example below defines a custom `endpoint-finder` agent. The first query runs it and captures the session ID and agent ID from the Agent tool result, then the second query resumes the session to ask a follow-up question that requires context from the first analysis.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import re
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition, ToolResultBlock

  AGENTS = {
      "endpoint-finder": AgentDefinition(
          description="Locates and catalogs API endpoints in a codebase.",
          prompt="You find and document API endpoints. Report each endpoint's path, method, and handler.",
          tools=["Read", "Grep", "Glob"],
      )
  }

  def extract_agent_id(block: ToolResultBlock) -> str | None:
      """Extract agentId from an Agent tool result's text content."""
      parts = block.content if isinstance(block.content, list) else [{"text": block.content}]
      for part in parts:
          if match := re.search(r"agentId:\s*([\w-]+)", part.get("text") or ""):
              return match.group(1)
      return None

  async def main():
      agent_id = None
      session_id = None

      # First invocation - run the endpoint-finder subagent
      try:
          async for message in query(
              prompt="Use the endpoint-finder agent to find all API endpoints in this codebase",
              options=ClaudeAgentOptions(allowed_tools=["Read", "Grep", "Glob", "Agent"], agents=AGENTS),
          ):
              # Capture session_id from ResultMessage (needed to resume this session)
              if hasattr(message, "session_id"):
                  session_id = message.session_id
              # Search tool results for the agentId trailer
              for block in getattr(message, "content", None) or []:
                  if isinstance(block, ToolResultBlock):
                      agent_id = extract_agent_id(block) or agent_id
              # Print the final result
              if hasattr(message, "result"):
                  print(message.result)
      except Exception as error:
          # A single-shot query() raises after yielding an error result,
          # so session_id and agent_id have already been captured by the loop above.
          print(f"Session ended with an error: {error}")

      # Second invocation - resume and ask follow-up
      if agent_id and session_id:
          async for message in query(
              prompt=f"Resume agent {agent_id} and list the top 3 most complex endpoints",
              options=ClaudeAgentOptions(
                  allowed_tools=["Read", "Grep", "Glob", "Agent"], agents=AGENTS, resume=session_id
              ),
          ):
              if hasattr(message, "result"):
                  print(message.result)
      else:
          print("No agentId found in the first query, so there is no subagent to resume.")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  const agents = {
    "endpoint-finder": {
      description: "Locates and catalogs API endpoints in a codebase.",
      prompt: "You find and document API endpoints. Report each endpoint's path, method, and handler.",
      tools: ["Read", "Grep", "Glob"]
    }
  };

  // Stringify content to search for agentId without traversing nested block types
  function extractAgentId(message: SDKMessage): string | undefined {
    if (message.type !== "assistant" && message.type !== "user") return undefined;
    const content = JSON.stringify(message.message.content);
    const match = content.match(/agentId:\s*([\w-]+)/);
    return match?.[1];
  }

  let agentId: string | undefined;
  let sessionId: string | undefined;

  // First invocation - run the endpoint-finder subagent
  try {
    for await (const message of query({
      prompt: "Use the endpoint-finder agent to find all API endpoints in this codebase",
      options: { allowedTools: ["Read", "Grep", "Glob", "Agent"], agents }
    })) {
      // Capture session_id from ResultMessage (needed to resume this session)
      if ("session_id" in message) sessionId = message.session_id;
      // Search message content for the agentId (appears in Agent tool results)
      const extractedId = extractAgentId(message);
      if (extractedId) agentId = extractedId;
      // Print the final result
      if ("result" in message) console.log(message.result);
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result,
    // so sessionId and agentId have already been captured by the loop above.
    console.error(`Session ended with an error: ${error}`);
  }

  // Second invocation - resume and ask follow-up
  if (agentId && sessionId) {
    for await (const message of query({
      prompt: `Resume agent ${agentId} and list the top 3 most complex endpoints`,
      options: { allowedTools: ["Read", "Grep", "Glob", "Agent"], agents, resume: sessionId }
    })) {
      if ("result" in message) console.log(message.result);
    }
  } else {
    console.log("No agentId found in the first query, so there is no subagent to resume.");
  }
  ```
</CodeGroup>

Subagent transcripts are stored in separate files and persist independently of the main conversation. See [resume subagents in Claude Code](/docs/en/sub-agents#resume-subagents) for compaction behavior and the `cleanupPeriodDays` cleanup period.

## Tool restrictions

Use the `tools` field to limit what a subagent can do:

* **Omit `tools`**: the subagent gets every [tool available to subagents](/docs/en/sub-agents#available-tools)
* **List tools**: the subagent gets only those. A code reviewer that should never edit files, for example, gets `["Read", "Grep", "Glob"]`

A tool you leave out isn't in the subagent's session at all: Claude works without it, with no permission prompt or error.

This example creates a read-only analysis agent that can examine code but can't modify files or run commands.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

  async def main():
      async for message in query(
          prompt="Analyze the architecture of this codebase",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Grep", "Glob", "Agent"],
              agents={
                  "code-analyzer": AgentDefinition(
                      description="Static code analysis and architecture review",
                      prompt="""You are a code architecture analyst. Analyze code structure,
  identify patterns, and suggest improvements without making changes.""",
                      # Read-only tools: no Edit, Write, or Bash access
                      tools=["Read", "Grep", "Glob"],
                  )
              },
          ),
      ):
          if hasattr(message, "result"):
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  for await (const message of query({
    prompt: "Analyze the architecture of this codebase",
    options: {
      allowedTools: ["Read", "Grep", "Glob", "Agent"],
      agents: {
        "code-analyzer": {
          description: "Static code analysis and architecture review",
          prompt: `You are a code architecture analyst. Analyze code structure,
  identify patterns, and suggest improvements without making changes.`,
          // Read-only tools: no Edit, Write, or Bash access
          tools: ["Read", "Grep", "Glob"]
        }
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

### Common tool combinations

| Use case           | Tools                                   | Description                                                        |
| :----------------- | :-------------------------------------- | :----------------------------------------------------------------- |
| Read-only analysis | `Read`, `Grep`, `Glob`                  | Can examine code but not modify or execute                         |
| Test execution     | `Bash`, `Read`, `Grep`                  | Can run commands and analyze output                                |
| Code modification  | `Read`, `Edit`, `Write`, `Grep`, `Glob` | Full read/write access without command execution                   |
| Full access        | All tools                               | Inherits the tools available to subagents (omit the `tools` field) |

## Cap subagent depth, concurrency, and spend

<Note>
  This section describes TypeScript SDK v0.3.219 and Python SDK v0.2.127 and later, the releases that bundle Claude Code v2.1.219 or later. On earlier releases, some of these limits are missing or default differently, so upgrade before you rely on them to bound a run. The [environment variable reference](/docs/en/env-vars) and [turns and budget](/docs/en/agent-sdk/agent-loop#turns-and-budget) record the Claude Code version that added each variable and the spend cap's subagent enforcement.
</Note>

Claude decides on its own when to spawn a subagent and how many to spawn. Each subagent makes its own API requests, which count toward the query's `total_cost_usd`, and a subagent can spawn subagents of its own, so one prompt can grow into a tree of agents.

You can cap that growth in three ways: how deeply subagents nest, how many run at once, and how much the whole query spends. Set the depth and concurrency limits as environment variables through the [`env`](/docs/en/agent-sdk/typescript#options) option, and the spend limit as a query option:

| Limit       | Set it with                                              | Default                                                                                                | What Claude Code does at the limit                                                                                                                                                                                                                                                                                                   |
| :---------- | :------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Depth       | [`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`](/docs/en/env-vars)   | `3` layers of subagents below your main agent. `1` stops your subagents from spawning any of their own | Leaves a subagent at the bottom layer unable to spawn, so it does its delegated work itself. See [nested subagents](/docs/en/sub-agents#let-subagents-spawn-their-own-subagents)                                                                                                                                                          |
| Concurrency | [`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`](/docs/en/env-vars)   | `20` subagents running at once, counting every subagent Claude spawns with the Agent tool              | Refuses to spawn another subagent, returning `Concurrent subagent limit reached`, until the running count drops below the limit. Sessions with [ultracode](/docs/en/model-config#adjust-effort-level) active are never refused. See the [concurrent subagent limit](/docs/en/sub-agents#concurrent-subagent-limit)                             |
| Spend       | `maxBudgetUsd` in TypeScript, `max_budget_usd` in Python | No limit. Counts the call's own spend, subagent requests included                                      | Enforces the cap in three ways: refuses to spawn more subagents, returning `Budget limit reached`, stops background subagents that are still running, and ends the query with the `error_max_budget_usd` result subtype. For how the caps behave across a session, see [turns and budget](/docs/en/agent-sdk/agent-loop#turns-and-budget) |

The two SDKs treat the `env` option differently: the TypeScript SDK replaces the subprocess environment with it, so spread `process.env` into it to keep variables like `PATH`, while the Python SDK merges it into the inherited environment. This example turns nesting off, allows at most five subagents at a time, and stops the query once the estimated spend reaches \$5:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      try:
          async for message in query(
              prompt="Audit every service in this repo for unhandled promise rejections",
              options=ClaudeAgentOptions(
                  allowed_tools=["Read", "Grep", "Glob", "Agent"],
                  # env is merged on top of the inherited environment
                  env={
                      "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "1",
                      "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "5",
                  },
                  max_budget_usd=5.0,
              ),
          ):
              if isinstance(message, ResultMessage):
                  print(f"{message.subtype}: ${message.total_cost_usd}")
      except Exception as error:
          # A single-shot query() raises after yielding an error result,
          # so the budget-capped result has already been printed above.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  try {
    for await (const message of query({
      prompt: "Audit every service in this repo for unhandled promise rejections",
      options: {
        allowedTools: ["Read", "Grep", "Glob", "Agent"],
        // env replaces the subprocess environment, so spread process.env to keep PATH
        env: {
          ...process.env,
          CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH: "1",
          CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS: "5",
        },
        maxBudgetUsd: 5,
      },
    })) {
      if (message.type === "result") {
        console.log(`${message.subtype}: $${message.total_cost_usd}`);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result,
    // so the budget-capped result has already been logged above.
    console.error(`Session ended with an error: ${error}`);
  }
  ```
</CodeGroup>

What you see depends on which limit, if any, the query reaches:

* **Under the spend cap**: you see `success` and the estimated cost.
* **At the spend cap**: you see `error_max_budget_usd` with a cost at or above `5`, and then your error handler runs.
* **At the concurrency limit**: you see a `tool_result` block in the message stream carrying `Concurrent subagent limit reached`. Claude receives the same block as the Agent tool's result.

### Run Opus 5 with subagents

Claude Opus 5 delegates to subagents more readily than earlier models, so the [depth, concurrency, and spend limits](#cap-subagent-depth-concurrency-and-spend) matter most on queries that run Opus 5. The [Opus 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#controlling-subagent-spawning) has a delegation instruction you can add to any prompt. Whether Claude Code adds an instruction of its own depends on which [system prompt](/docs/en/agent-sdk/modifying-system-prompts#how-system-prompts-work) you use:

* **`claude_code` preset**: when the model is Opus 5, Claude Code adds a line to its system prompt telling Claude not to call the Agent tool unless it's asked to. The Agent tool stays available.
* **A custom prompt, or no `systemPrompt`**: Claude Code doesn't build its system prompt, so that line is absent. Add the prompting guide's delegation instruction to your own prompt.

Either instruction only steers Claude, so set the limits as well. Claude Code enforces them however Claude decides to delegate.

## Scale up with dynamic workflows

Subagents work well for a few delegated tasks per turn. For runs that coordinate dozens to hundreds of agents, use the `Workflow` tool, which moves the orchestration into a script the runtime executes outside the conversation context. See [dynamic workflows](/docs/en/workflows) for how workflows differ from turn-by-turn subagent delegation.

The `Workflow` tool is available in the TypeScript Agent SDK v0.3.149 and later. Include `Workflow` in `allowedTools` to auto-approve workflow runs. The tool input and output schemas are listed in the [TypeScript reference](/docs/en/agent-sdk/typescript#workflow).

## Troubleshooting

### Claude not delegating to subagents

If Claude completes tasks directly instead of delegating to your subagent:

* **Use explicit prompting**: mention the subagent by name in your prompt, for example "Use the code-reviewer agent to check the authentication module"
* **Write a clear description**: explain exactly when to use the subagent so Claude can match tasks appropriately

### Filesystem-based agents not loading

Claude Code watches `~/.claude/agents/` and `.claude/agents/` and picks up a new or edited agent file within a few seconds, with no restart needed. If a definition never appears, work through these causes:

* **New `agents` directory**: the watcher covers only directories that existed when the session started, so the first file in a new directory needs a session restart. This is the most common cause.
* **Invalid frontmatter or a duplicate `name`**: check the file's YAML, and whether an existing agent already uses the `name`.
* **`--disable-slash-commands`**: sessions started with this flag don't watch these directories and always need a restart to load new files.
* **A file under an added directory**: Claude Code loads `.claude/agents/` from directories added with the `add_dirs` (Python) or `additionalDirectories` (TypeScript) option, or the CLI's `--add-dir` or `/add-dir`, but doesn't watch them, so a new or edited file there needs a session restart.
* **A programmatic agent with the same name**: `agents` passed to `query()` override a filesystem agent with the same name.

For the file format, see [how to write subagent files](/docs/en/sub-agents#write-subagent-files).

## Related documentation

* [Claude Code subagents](/docs/en/sub-agents): comprehensive subagent documentation including filesystem-based definitions
* [Dynamic workflows](/docs/en/workflows): orchestrate many subagents from a script for jobs too large for one conversation
* [SDK overview](/docs/en/agent-sdk/overview): getting started with the Claude Agent SDK

---

## Track todos

- 官方原文：https://code.claude.com/docs/en/agent-sdk/todo-tracking.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-todo-tracking.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Track todos

> Track todos in Agent SDK sessions and render Claude's progress in your application from structured tool calls

Claude Code provides the [task-tracking tools](/docs/en/tools-reference#task-tool-availability) by default only on the models listed under [Model availability](#model-availability). Newer models track multi-step work without a written todo list, so on those you don't need anything on this page for Claude to work through multi-step tasks.

In a session that has the task-tracking tools, Claude keeps a written todo list, updating each item's status as it works. You see each change in the message stream as a structured tool call. Opt a session in only when your application reads those tool calls, whether to log task activity or to render its own progress display.

## Model availability

<Note>
  The following tools are available by default only on Claude 3.x models, Opus 4 through 4.7, Sonnet 4 through 4.6, and Haiku 4.5. On every other model, including model IDs Claude Code doesn't recognize, they aren't available unless you opt in:

  * `TodoWrite`
  * `TaskCreate`
  * `TaskGet`
  * `TaskUpdate`
  * `TaskList`

  Wherever the tools are available, Claude Code provides the four Task tools, or `TodoWrite` instead when you set `CLAUDE_CODE_ENABLE_TASKS=0`.

  This default set applies in Claude Code v2.1.268 and later, which the TypeScript Agent SDK bundles from v0.3.268.
</Note>

On a model that doesn't have the tools by default, unless you opt a session in, you see no `tool_use` blocks for them in the message stream. The Agent SDK applies these defaults through the Claude Code binary that it bundles. If you point `pathToClaudeCodeExecutable` (TypeScript) or `cli_path` (Python) at your own Claude Code install, you get whichever tools that install provides, under its own defaults. To see the exact set in a running session, [check which tools are available](/docs/en/tools-reference#check-which-tools-are-available). To opt a session in, do one of the following:

* Name one of the tools in the [`allowedTools`](/docs/en/agent-sdk/permissions#allow-and-deny-rules) (TypeScript) or `allowed_tools` (Python) option
* List the tools in the `tools` option, which restricts the session's built-in tools to the ones it names. Include the tools you want alongside the other built-in tools you use
* Set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` in the `env` option, as the examples on this page do. In TypeScript, `env` replaces the subprocess environment, so spread `...process.env` to keep inherited variables. In Python, `env` is merged on top of the inherited environment

## Todo lifecycle

Claude moves each todo through a predictable lifecycle:

1. **Created**: Claude adds the todo as `pending` when it identifies a task
2. **Activated**: Claude sets the todo to `in_progress` when it starts the work
3. **Completed**: Claude marks it completed when the task finishes successfully
4. **Removed**: Claude deletes a todo it no longer needs by setting `status: "deleted"` in a `TaskUpdate` call

## When Claude creates todos

In a [session that has the task-tracking tools](#model-availability), Claude creates todos for most multi-step work, such as:

* **Complex multi-step tasks** requiring three or more distinct actions
* **User-provided task lists** when multiple items are mentioned
* **Longer operations** that benefit from progress tracking
* **Explicit requests** when users ask for todo organization

Claude may skip todos for very short or single-step requests.

## Examples

Before running these examples, install the Claude Agent SDK by following the [quickstart](/docs/en/agent-sdk/quickstart). Every example on this page shares the same permission setup and exit behavior:

* **Permission mode**: the example prompts ask Claude to do real work on a project, so each example sets `permissionMode: "acceptEdits"` (TypeScript) or `permission_mode="acceptEdits"` (Python) to auto-approve the file edits that work produces. See [Permission modes](/docs/en/agent-sdk/permissions#permission-modes) for the alternatives.
* **Turn limit**: each example runs until the agent finishes and yields its final result message. If a session reaches its turn limit first, that result message has the `error_max_turns` subtype. Check `subtype` to detect that ending.
* **Error handling**: these examples use single-shot `query()` calls. After yielding an `error_max_turns` result, `query()` raises an error that includes `Reached maximum number of turns`. Each example wraps its loop in a try block to exit cleanly when that happens. See [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result) for the result subtypes.

<Note>
  The task system messages, [`SDKTaskNotificationMessage`](/docs/en/agent-sdk/typescript#sdktasknotificationmessage) (TypeScript) or [`TaskNotificationMessage`](/docs/en/agent-sdk/python#tasknotificationmessage) (Python) among them, report background tasks such as backgrounded commands and subagents. In the message stream, you see todo activity as `tool_use` blocks in the assistant messages.
</Note>

### Monitor todo changes

The following example watches the assistant stream for `TaskCreate` and `TaskUpdate` `tool_use` blocks and prints a `+` line with each new task's subject and an update line with each status change's task ID and new status. Use this shape when you want a log of task activity rather than a rendered display. The `+` lines don't include the assigned IDs, so this log can't match updates back to their creates. To keep that correlation, capture the IDs as [Display progress in real time](#display-progress-in-real-time) does.

The streamed `tool_use` input is the raw shape the model emitted. Claude Code repairs some close-but-incorrect key names before execution, mapping `id` or `task_id` to `taskId` and `active_form` to `activeForm`, but that repair is not reflected in the stream. Read `TaskUpdate` input fields defensively, as both examples on this page do, rather than assuming the canonical name is always present.

<CodeGroup>
  ```typescript TypeScript theme={null}

  try {
    for await (const message of query({
      prompt: "Create a static website with a home page, an about page, and a shared stylesheet, and track progress with todos",
      // Keeps the Task tools on models where Claude Code otherwise doesn't provide them.
      options: { maxTurns: 15, permissionMode: "acceptEdits", env: { ...process.env, CLAUDE_CODE_ENABLE_TODO_TOOLS: "1" } },
    })) {
      if (message.type !== "assistant") continue;
      for (const block of message.message.content) {
        if (block.type !== "tool_use") continue;
        if (block.name === "TaskCreate") {
          const input = block.input as { subject: string };
          console.log(`+ ${input.subject}`);
        } else if (block.name === "TaskUpdate") {
          const input = block.input as {
            taskId?: string;
            id?: string;
            task_id?: string;
            status?: string;
          };
          const taskId = input.taskId ?? input.id ?? input.task_id;
          if (taskId && input.status) console.log(`  ${taskId} -> ${input.status}`);
        }
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result.
    console.log(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock

  async def main():
      try:
          async for message in query(
              prompt="Create a static website with a home page, an about page, and a shared stylesheet, and track progress with todos",
              # Keeps the Task tools on models where Claude Code otherwise doesn't provide them.
              options=ClaudeAgentOptions(max_turns=15, permission_mode="acceptEdits", env={"CLAUDE_CODE_ENABLE_TODO_TOOLS": "1"}),
          ):
              if not isinstance(message, AssistantMessage):
                  continue
              for block in message.content:
                  if not isinstance(block, ToolUseBlock):
                      continue
                  if block.name == "TaskCreate":
                      print(f"+ {block.input.get('subject', '')}")
                  elif block.name == "TaskUpdate" and block.input.get("status"):
                      task_id = (
                          block.input.get("taskId")
                          or block.input.get("id")
                          or block.input.get("task_id")
                      )
                      if task_id:
                          print(f"  {task_id} -> {block.input['status']}")
      except Exception as error:
          # A single-shot query() raises after yielding an error result.
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

### Display progress in real time

The following example watches the assistant stream for `TaskCreate` and `TaskUpdate` `tool_use` blocks and keeps a map of tasks keyed by task ID in a `TaskTracker` class, rerendering a progress summary on every change. The summary counts completed and in-progress tasks and shows each active item's `activeForm` label in place of its `subject`. Use this shape when your application maintains a progress display instead of logging each event.

The assigned task ID isn't in the `TaskCreate` input. Claude Code delivers each tool's structured output on the user message that carries its `tool_result` block, in the `tool_use_result` field. For `TaskCreate`, that object is documented for TypeScript as `TaskCreateOutput` under [Tool Output Types](/docs/en/agent-sdk/typescript#tool-output-types), and in Python the field is a plain dict of the same shape. The tracker pairs each `tool_result` block with its `tool_use` call by `tool_use_id` and reads `task.id` from the paired message's `tool_use_result`. Claude can read the list back with `TaskList` and one task's full details with `TaskGet`.

<CodeGroup>
  ```typescript TypeScript theme={null}

  type Task = { subject: string; activeForm?: string; status: string };

  class TaskTracker {
    private tasks = new Map<string, Task>();
    private pendingCreates = new Map<string, { subject: string; activeForm?: string }>();

    displayProgress() {
      if (this.tasks.size === 0) {
        console.log("\nProgress: no open tasks\n");
        return;
      }

      const items = [...this.tasks.values()];
      const completed = items.filter((t) => t.status === "completed").length;
      const inProgress = items.filter((t) => t.status === "in_progress").length;

      console.log(`\nProgress: ${completed}/${this.tasks.size} completed`);
      console.log(`Currently working on: ${inProgress} task(s)\n`);

      for (const [id, task] of this.tasks) {
        const icon =
          task.status === "completed" ? "✅" : task.status === "in_progress" ? "🔧" : "❌";
        const text = task.status === "in_progress" && task.activeForm ? task.activeForm : task.subject;
        console.log(`${id}. ${icon} ${text}`);
      }
    }

    handleToolUse(block: { id: string; name: string; input: unknown }) {
      if (block.name === "TaskCreate") {
        const input = block.input as { subject: string; activeForm?: string; active_form?: string };
        this.pendingCreates.set(block.id, {
          subject: input.subject,
          activeForm: input.activeForm ?? input.active_form,
        });
      } else if (block.name === "TaskUpdate") {
        const input = block.input as {
          taskId?: string;
          id?: string;
          task_id?: string;
          status?: string;
          activeForm?: string;
          active_form?: string;
        };
        const taskId = input.taskId ?? input.id ?? input.task_id;
        if (!taskId) return;
        if (input.status === "deleted") {
          this.tasks.delete(taskId);
          this.displayProgress();
          return;
        }
        const task = this.tasks.get(taskId);
        if (!task) return;
        if (input.status) task.status = input.status;
        const active = input.activeForm ?? input.active_form;
        if (active) task.activeForm = active;
        this.displayProgress();
      }
    }

    handleToolResult(block: { tool_use_id: string; is_error?: boolean }, result: unknown) {
      const create = this.pendingCreates.get(block.tool_use_id);
      if (!create) return;
      this.pendingCreates.delete(block.tool_use_id);
      if (block.is_error) return;
      // The result's user message carries the tool's structured output as
      // tool_use_result; for TaskCreate that's TaskCreateOutput,
      // { task: { id, subject } }.
      const out = result as { task?: { id: string } };
      if (!out?.task?.id) return;
      this.tasks.set(out.task.id, { ...create, status: "pending" });
      this.displayProgress();
    }

    async trackQuery(prompt: string) {
      try {
        for await (const message of query({
          prompt,
          options: { maxTurns: 20, permissionMode: "acceptEdits", env: { ...process.env, CLAUDE_CODE_ENABLE_TODO_TOOLS: "1" } },
        })) {
          if (message.type === "assistant") {
            for (const block of message.message.content) {
              if (block.type === "tool_use") this.handleToolUse(block);
            }
          }
          if (message.type === "user" && Array.isArray(message.message.content)) {
            for (const block of message.message.content) {
              if (block.type === "tool_result") this.handleToolResult(block, message.tool_use_result);
            }
          }
        }
      } catch (error) {
        // A single-shot query() throws after yielding an error result,
        // such as when the maxTurns limit is hit.
        console.log(`Session ended with an error: ${error}`);
      }
    }
  }

  // Usage
  const tracker = new TaskTracker();
  await tracker.trackQuery("Build a complete authentication system with todos");
  ```

  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import (
      query,
      ClaudeAgentOptions,
      AssistantMessage,
      UserMessage,
      ToolUseBlock,
      ToolResultBlock,
  )

  class TaskTracker:
      def __init__(self):
          self.tasks: dict[str, dict] = {}
          self.pending_creates: dict[str, dict] = {}

      def display_progress(self):
          if not self.tasks:
              print("\nProgress: no open tasks\n")
              return

          completed = len([t for t in self.tasks.values() if t["status"] == "completed"])
          in_progress = len([t for t in self.tasks.values() if t["status"] == "in_progress"])

          print(f"\nProgress: {completed}/{len(self.tasks)} completed")
          print(f"Currently working on: {in_progress} task(s)\n")

          for task_id, task in self.tasks.items():
              icon = (
                  "✅"
                  if task["status"] == "completed"
                  else "🔧"
                  if task["status"] == "in_progress"
                  else "❌"
              )
              text = (
                  task["activeForm"]
                  if task["status"] == "in_progress" and task.get("activeForm")
                  else task["subject"]
              )
              print(f"{task_id}. {icon} {text}")

      def handle_tool_use(self, block: ToolUseBlock):
          if block.name == "TaskCreate":
              self.pending_creates[block.id] = {
                  "subject": block.input.get("subject", ""),
                  "activeForm": block.input.get("activeForm") or block.input.get("active_form"),
              }
          elif block.name == "TaskUpdate":
              task_id = (
                  block.input.get("taskId")
                  or block.input.get("id")
                  or block.input.get("task_id")
              )
              if not task_id:
                  return
              if block.input.get("status") == "deleted":
                  self.tasks.pop(task_id, None)
                  self.display_progress()
                  return
              task = self.tasks.get(task_id)
              if not task:
                  return
              if block.input.get("status"):
                  task["status"] = block.input["status"]
              active = block.input.get("activeForm") or block.input.get("active_form")
              if active:
                  task["activeForm"] = active
              self.display_progress()

      def handle_tool_result(self, block: ToolResultBlock, tool_use_result):
          create = self.pending_creates.pop(block.tool_use_id, None)
          if create is None or block.is_error:
              return
          # The result's user message carries the tool's structured output as
          # tool_use_result; for TaskCreate that's {"task": {"id": ..., "subject": ...}}.
          task = (tool_use_result or {}).get("task") or {}
          if not task.get("id"):
              return
          self.tasks[task["id"]] = {**create, "status": "pending"}
          self.display_progress()

      async def track_query(self, prompt: str):
          try:
              async for message in query(
                  prompt=prompt,
                  options=ClaudeAgentOptions(
                      max_turns=20,
                      permission_mode="acceptEdits",
                      env={"CLAUDE_CODE_ENABLE_TODO_TOOLS": "1"},
                  ),
              ):
                  if isinstance(message, AssistantMessage):
                      for block in message.content:
                          if isinstance(block, ToolUseBlock):
                              self.handle_tool_use(block)
                  if isinstance(message, UserMessage) and isinstance(message.content, list):
                      for block in message.content:
                          if isinstance(block, ToolResultBlock):
                              self.handle_tool_result(block, message.tool_use_result)
          except Exception as error:
              # A single-shot query() raises after yielding an error result,
              # such as when the max_turns limit is hit.
              print(f"Session ended with an error: {error}")

  # Usage
  async def main():
      tracker = TaskTracker()
      await tracker.track_query("Build a complete authentication system with todos")

  asyncio.run(main())
  ```
</CodeGroup>

## Related documentation

* [Agent SDK reference - TypeScript](/docs/en/agent-sdk/typescript): the options, types, and tool schemas for the TypeScript SDK, including the Task tool input and output types
* [Agent SDK reference - Python](/docs/en/agent-sdk/python): the options, types, and tool documentation for the Python SDK
* [Streaming Input](/docs/en/agent-sdk/streaming-vs-single-mode): the two input modes, and when to use streaming input instead of the single-shot calls these examples use
* [Give Claude custom tools](/docs/en/agent-sdk/custom-tools): define your own tools with the SDK's in-process MCP server

---

## Scale to many tools with tool search

- 官方原文：https://code.claude.com/docs/en/agent-sdk/tool-search.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-tool-search.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scale to many tools with tool search

> Scale your agent to thousands of tools by discovering and loading only what's needed, on demand.

Tool search enables your agent to work with hundreds or thousands of tools by dynamically discovering and loading them on demand. Instead of loading all tool definitions into the context window upfront, the agent searches your tool catalog and loads only the tools it needs.

This approach solves two challenges as tool libraries scale:

* **Context efficiency:** Tool definitions can consume large portions of the context window (50 tools can use 10-20K tokens), leaving less room for actual work.
* **Tool selection accuracy:** Tool selection accuracy degrades with more than 30-50 tools loaded at once.

## How tool search works

Tool search is on by default, with the exceptions listed in [Configure tool search](#configure-tool-search).

When it is active, tool definitions are withheld from the context window. The agent receives a summary of available tools and searches for relevant ones when the task requires a capability not already loaded. Up to five of the most relevant tools are loaded into context by default, where they stay available for subsequent turns until the SDK compacts the messages where the agent discovered them. After that compaction, the agent searches for those tools again when it next needs them.

Tool search adds one extra round-trip each time Claude searches for tools, but for large tool sets this is offset by smaller context on every turn. With fewer than \~10 tools whose definitions fit comfortably in the context window, loading everything upfront is typically faster.

For details on the underlying API mechanism, see [Tool search in the API](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool).

<Note>
  Tool search isn't supported on Microsoft Foundry [deployments hosted on Azure](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options), which reject it server-side: the SDK detects the rejection and loads tool definitions upfront for that deployment instead. [`ENABLE_TOOL_SEARCH`](#configure-tool-search) can't override this, since the rejection comes from the deployment itself.
</Note>

## Configure tool search

Tool search is on by default. For models on the SDK's unsupported-model list, the SDK loads tool definitions upfront instead, and no `ENABLE_TOOL_SEARCH` value overrides that. On Google Cloud's Agent Platform, the SDK decides by model generation:

* **Claude Opus 4.5, Sonnet 4.5, Haiku 4.5, and later**: tool search is on by default.
* **Earlier Agent Platform models**: the SDK loads tool definitions upfront, because their serving stacks reject the required beta header. `ENABLE_TOOL_SEARCH` can't override this.

Before Claude Code v2.1.221, the SDK disabled tool search for all models on Google Cloud's Agent Platform unless you set `ENABLE_TOOL_SEARCH`.

The SDK also disables tool search when `ANTHROPIC_BASE_URL` points to a non-first-party host, since most proxies don't forward `tool_reference` blocks. You can override that default with the `ENABLE_TOOL_SEARCH` environment variable:

| Value    | Behavior                                                                                                                                                                                                                                                                                                                                                                                                            |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| (unset)  | Tool search is on. Tool definitions are deferred and discovered on demand. Falls back to loading upfront on Google Cloud's Agent Platform models earlier than the Claude 4.5 generation, a non-first-party `ANTHROPIC_BASE_URL`, or a Microsoft Foundry deployment hosted on Azure.                                                                                                                                 |
| `true`   | Tool search is always on, except on a Microsoft Foundry deployment hosted on Azure, where the server-side rejection still forces upfront loading, and on Google Cloud's Agent Platform models earlier than the Claude 4.5 generation, where the SDK keeps loading tool definitions upfront. The SDK sends the beta header through proxies, and requests fail on proxies that don't support `tool_reference` blocks. |
| `auto`   | Counts the tokens in the tool definitions that tool search can defer and compares the total against the model's context window. When the total reaches 10% of the window, tool search activates. Below that, the SDK loads every tool definition into context upfront.                                                                                                                                              |
| `auto:N` | Same as `auto` with a custom percentage. `auto:5` activates when those definitions reach 5% of the context window. Lower values activate sooner.                                                                                                                                                                                                                                                                    |
| `false`  | Tool search is off. All tool definitions are loaded into context on every turn.                                                                                                                                                                                                                                                                                                                                     |

Setting [`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`](/docs/en/env-vars) keeps tool search off. You can't override it by setting `ENABLE_TOOL_SEARCH` yourself. Your organization can keep tool search on through [managed settings](/docs/en/managed-settings), on Claude Code v2.1.227 or later. [Disable pre-release capabilities](/docs/en/llm-gateway-protocol#disable-pre-release-capabilities) covers where the override applies and what the variable strips.

Tool search applies to all registered tools, whether they come from remote MCP servers or [custom SDK MCP servers](/docs/en/agent-sdk/custom-tools). When you use `auto`, the SDK counts every definition that tool search can defer toward one combined threshold: each MCP tool that isn't marked [`alwaysLoad`](/docs/en/mcp#exempt-a-server-from-deferral), from any server, plus the built-in tools that load on demand. The SDK always loads core built-in tools such as Bash, Read, and Edit upfront and doesn't count them toward the threshold.

Set the value in the `env` option on `query()`. In TypeScript, `env` replaces the subprocess environment, so spread `...process.env` to keep inherited variables. In Python, `env` is merged on top of the inherited environment. This example connects to a remote MCP server that exposes many tools, pre-approves all of them with a wildcard, and uses `auto:5` so tool search activates when the definitions it can defer reach 5% of the context window:

<CodeGroup>
  ```typescript TypeScript theme={null}

  try {
    for await (const message of query({
      prompt: "Find and run the appropriate database query",
      options: {
        mcpServers: {
          "enterprise-tools": {
            // Connect to a remote MCP server
            type: "http",
            url: "https://tools.example.com/mcp"
          }
        },
        allowedTools: ["mcp__enterprise-tools__*"], // Wildcard pre-approves all tools from this server
        env: {
          ...process.env, // env replaces the subprocess environment, so keep inherited variables
          ENABLE_TOOL_SEARCH: "auto:5" // Activate tool search when deferrable definitions reach 5% of context
        }
      }
    })) {
      if (message.type === "result" && message.subtype === "success") {
        console.log(message.result);
      }
    }
  } catch (error) {
    // A single-shot query() throws after yielding an error result
    console.log(`Session ended with an error: ${error}`);
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  async def main():
      options = ClaudeAgentOptions(
          mcp_servers={
              "enterprise-tools": {
                  "type": "http",
                  "url": "https://tools.example.com/mcp",
              }
          },
          allowed_tools=[
              "mcp__enterprise-tools__*"
          ],  # Wildcard pre-approves all tools from this server
          env={
              "ENABLE_TOOL_SEARCH": "auto:5"  # Activate tool search when deferrable definitions reach 5% of context
          },
      )

      try:
          async for message in query(
              prompt="Find and run the appropriate database query",
              options=options,
          ):
              if isinstance(message, ResultMessage) and message.subtype == "success":
                  print(message.result)
      except Exception as error:
          # A single-shot query() raises after yielding an error result
          print(f"Session ended with an error: {error}")

  asyncio.run(main())
  ```
</CodeGroup>

To run this example, replace `https://tools.example.com/mcp` with the URL of your own MCP server. On success the result text prints to the console.

Because this is a single-shot `query()` call, the SDK raises after yielding an error result, so the example wraps the loop in a try block. To see why a run failed, check the result message's `subtype`, such as `error_during_execution`, inside the loop. For more on result messages, see [Handle the result](/docs/en/agent-sdk/agent-loop#handle-the-result).

## Optimize tool discovery

The search mechanism matches queries against tool names and descriptions. Names like `search_slack_messages` surface for a wider range of requests than `query_slack`. Descriptions with specific keywords ("Search Slack messages by keyword, channel, or date range") match more queries than generic ones ("Query Slack").

You can also add a system prompt section listing available tool categories. This gives the agent context about what kinds of tools are available to search for. Pass the text through the `systemPrompt` option in TypeScript or `system_prompt` in Python, using the `claude_code` preset with `append`, which adds your text to the preset's prompt instead of replacing it:

<CodeGroup>
  ```typescript TypeScript theme={null}
  options: {
    systemPrompt: {
      type: "preset",
      preset: "claude_code",
      append: "You can search for tools to interact with Slack, GitHub, and Jira."
    }
  }
  ```

  ```python Python theme={null}
  options = ClaudeAgentOptions(
      system_prompt={
          "type": "preset",
          "preset": "claude_code",
          "append": "You can search for tools to interact with Slack, GitHub, and Jira.",
      }
  )
  ```
</CodeGroup>

For the full set of system prompt options, see [Modifying system prompts](/docs/en/agent-sdk/modifying-system-prompts).

## Limits

* **Maximum tools:** 10,000 tools in your catalog
* **Search results:** returns up to five most relevant tools per search by default
* **Model support:** Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.5, and later models; see [model compatibility in the API docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#model-compatibility) for the current list. The same minimums apply on Google Cloud's Agent Platform.

## Related documentation

* [Tool search in the API](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool): Full API documentation for tool search, including custom implementations
* [Connect MCP servers](/docs/en/agent-sdk/mcp): Connect to external tools via MCP servers
* [Custom tools](/docs/en/agent-sdk/custom-tools): Build your own tools with SDK MCP servers
* [TypeScript SDK reference](/docs/en/agent-sdk/typescript): Full API reference
* [Python SDK reference](/docs/en/agent-sdk/python): Full API reference

---

## Troubleshoot the Agent SDK

- 官方原文：https://code.claude.com/docs/en/agent-sdk/troubleshooting.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-troubleshooting.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshoot the Agent SDK

> Fix Agent SDK errors by the exact message you see, with the cause and fix for each error in the TypeScript and Python SDKs.

Entries on this page are keyed to the error you see. Each names the cause and what to do.

## CLI startup

### CLINotFoundError: Claude Code not found

The Python SDK launches the Claude Code CLI as a subprocess. When it can't find a `claude` executable, connecting fails with a `CLINotFoundError`:

```
Claude Code not found at: /your/configured/path
```

The message includes the configured path when you set `ClaudeAgentOptions(cli_path=...)` and it points at a missing file. Without `cli_path`, the SDK searches your `PATH` and common install locations, and the message includes install instructions for your platform.

To fix it:

* Install Claude Code if it isn't installed. See [Install Claude Code](/docs/en/setup#install-claude-code) for the command on your platform.
* If you set `cli_path`, confirm the file exists and is the `claude` executable.
* If you rely on `PATH` resolution, confirm `claude --version` works in the same environment your application runs in. Processes you launch outside your shell, such as from an IDE or a service manager, often run with a different `PATH`.

The TypeScript SDK looks for the CLI in its bundled platform package and the path you set in `pathToClaudeCodeExecutable`. Match the message you see:

* `Native CLI binary for <platform>-<arch> not found`: the bundled platform package is missing, most often because the install skipped optional dependencies. Reinstall `@anthropic-ai/claude-agent-sdk` without skipping optional dependencies, or point `pathToClaudeCodeExecutable` at a [native install](/docs/en/setup#install-claude-code). In a single-file executable built with `bun build --compile`, the same message has a different cause and fix. See [Compile to a single executable](/docs/en/agent-sdk/typescript#compile-to-a-single-executable).
* `Claude Code native binary not found at <path>` or `Claude Code executable not found at <path>. Is options.pathToClaudeCodeExecutable set?`: the file at the resolved path is missing, or the process can't access it. Confirm the file exists at that path and that the process can access it.

### CLIConnectionError: Refusing to execute batch script

On Windows, connecting fails with a `CLIConnectionError` when the CLI path the Python SDK uses is a `.bat` or `.cmd` batch script, including the `claude.cmd` shim that an npm install creates:

```
Refusing to execute batch script 'C:\\Users\\you\\AppData\\Roaming\\npm\\claude.cmd': Windows runs .bat/.cmd files via cmd.exe, which can execute commands injected through CLI arguments, and no reliable escaping for cmd.exe exists. Use a native claude executable instead: install Claude Code natively (irm https://claude.ai/install.ps1 | iex), point ClaudeAgentOptions(cli_path=...) at a claude.exe, or install the claude-agent-sdk wheel for a platform that bundles claude.exe (e.g. Windows x64).
```

The refusal is deliberate security hardening, not a broken install. Windows runs batch scripts by rewriting the spawn into a `cmd.exe /c` invocation, and `cmd.exe` re-parses the whole command line at execution time, so an argument value can execute injected commands.

Most Windows installs never reach this error. The Windows x64 wheel of `claude-agent-sdk` bundles a `claude.exe`, and the SDK prefers the bundled CLI, then any native `claude.exe` it can discover, before falling back to a batch shim. You see the refusal in two cases:

* You set `ClaudeAgentOptions(cli_path=...)` to a `.bat` or `.cmd` file, such as npm's `claude.cmd` shim.
* Your install has no bundled or native `claude.exe`, for example a source install on ARM64 Windows where the only `claude` on your `PATH` is the npm shim.

To fix it, give the SDK a native executable instead of a batch script:

* If you set `ClaudeAgentOptions(cli_path=...)`, point it at a `claude.exe` or remove the option. The SDK skips discovery while `cli_path` is set, so a native install alone can't take effect.
* Install Claude Code natively in PowerShell: `irm https://claude.ai/install.ps1 | iex`
* On x64 Windows, install the `claude-agent-sdk` wheel, which bundles `claude.exe`.

Before `claude-agent-sdk` 0.2.124, the Python SDK spawned batch scripts through `cmd.exe` without this check.

### CLIConnectionError: Failed to start Claude Code

The SDK found a file at the resolved path but couldn't launch it. Python raises these failures as a `CLIConnectionError`. TypeScript rejects the message iteration with an error carrying no SDK class. The table below maps each message to what it tells you. Match the message you see:

| Message                                                           | SDK        | What it tells you                                                    |
| ----------------------------------------------------------------- | ---------- | -------------------------------------------------------------------- |
| `Failed to start Claude Code: <detail>`                           | Python     | The rest of the message is the operating system's own error          |
| `Claude Code executable at <path> exists but failed to launch`    | TypeScript | The script at the configured path can't run                          |
| `Claude Code native binary at <path> exists but failed to launch` | TypeScript | The binary can't run, with a libc suggestion appended to the message |
| `Failed to spawn Claude Code process: <detail>`                   | TypeScript | Any other launch failure                                             |

In both SDKs, the usual cause is a resolved path that points at something that can't run, such as a text file, a directory, or a file without execute permission. Read the native-binary message's libc suggestion as one possible cause.

To fix it in either SDK:

* Confirm the configured path points at the `claude` executable itself and that the file has execute permission.
* If you don't need a custom path, remove `cli_path` in Python or `pathToClaudeCodeExecutable` in TypeScript so the SDK finds a CLI on its own, preferring its bundled copy.
* When the failing binary is the SDK's bundled copy in a container image, reinstall the SDK during the image build so the bundled binary matches the container's platform, or rebuild the image for the architecture it runs on. The usual cause is a binary that doesn't match the container's architecture or libc, or one that lost its execute permission in the image build.

### CLIConnectionError: Not connected

Calling a `ClaudeSDKClient` method in Python before the client has connected, or after it has disconnected, raises a `CLIConnectionError` with this message:

```
Not connected. Call connect() first.
```

Do what the message says. Either call `await client.connect()` before any other client method, or open the client with `async with ClaudeSDKClient() as client:`, which connects on entry.

## CLI process exit

The entries in this section mean the Claude Code process ended while your application was using it. Which error you see depends on the SDK language and on whether the CLI reported an error result before it exited.

### ProcessError: Command failed with exit code

The Python SDK raises a `ProcessError` when the Claude Code process exits with a nonzero code:

```
Command failed with exit code 1 (exit code: 1)
Error output: Check stderr output for details
```

The message states the exit code twice, and the `Error output` line is fixed text rather than your process's error output. The same fixed text fills the exception's `stderr` attribute. The exception's `exit_code` attribute carries the code. To capture what the CLI actually wrote to stderr, pass a `stderr` callback in `ClaudeAgentOptions` and log what it receives.

A bare `ProcessError` means the CLI exited without reporting an error result. When the CLI did report one, the SDK raises [`ResultError`](/docs/en/agent-sdk/python#resulterror) instead, covered in [Claude Code returned an error result](#claude-code-returned-an-error-result). `ResultError` subclasses `ProcessError`, so `except ProcessError` catches both. To handle them differently, put the `except ResultError` clause first.

Before `claude-agent-sdk` 0.2.140, the Python SDK raised error-result exits as a plain `Exception` rather than a `ResultError`.

### Claude Code process exited with code N

IDE wrappers print this message too, and the [error reference](/docs/en/errors#claude-code-process-exited-with-code-n) covers it for VS Code and other launchers. This entry covers what your TypeScript SDK code receives. The SDK surfaces a nonzero CLI exit as a plain `Error` that rejects the `for await` loop over `query()`'s messages. There's no SDK error class to catch, so wrap the loop in `try`/`catch` and match on the message:

```
Claude Code process exited with code 1. stderr: <tail of the CLI's stderr>
```

When the CLI wrote to stderr, the message ends with the tail of it. To capture the full stream, pass a `stderr` callback in the query options. A process killed by a signal reports `Claude Code process terminated by signal <name>` in the same form.

### Claude Code returned an error result

Both SDKs replace the process-exit error with this message when the CLI reported an error result before exiting:

```
Claude Code returned an error result: <the CLI's own error report>
```

The text after the colon is the CLI's report of what went wrong, so start there rather than with the exit itself. Python raises this as a [`ResultError`](/docs/en/agent-sdk/python#resulterror), whose `data` attribute carries the full error result. TypeScript rejects the message loop with a plain `Error` carrying the same message shape.

## Structured outputs

### structured\_output is None but the result says success

A result message can end with `subtype: "success"` while `structured_output` is `None` in Python or `undefined` in TypeScript. The run completes, but no validated output exists. One way to hit this is a schema no output can satisfy, for example conflicting length constraints. The run ends without a validation error, and the only signal is the missing `structured_output`.

Treat this result as a failure in application code. Check both that `subtype` is `success` and that `structured_output` is present before using it. The [Error handling](/docs/en/agent-sdk/structured-outputs#error-handling) section shows this pattern for both SDKs.

If it happens repeatedly with a schema you believe is correct, verify the schema is satisfiable, then simplify it until outputs validate, and reintroduce constraints one at a time.

## Report a new issue

If your error isn't covered here, check the open issues or file a new one in the SDK repositories: [claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript/issues) or [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python/issues). Include the full error text and your SDK version.

---

## TypeScript SDK V2 session API (removed)

- 官方原文：https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-typescript-v2-preview.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TypeScript SDK V2 session API (removed)

> Reference for the removed V2 TypeScript Agent SDK session API, with session-based send/stream patterns for multi-turn conversations.

<Warning>
  The V2 session API is no longer supported. TypeScript Agent SDK 0.3.142 removes `unstable_v2_createSession`, `unstable_v2_resumeSession`, `unstable_v2_prompt`, and the `SDKSession` and `SDKSessionOptions` types.

  To migrate, use the [`query()` API](/docs/en/agent-sdk/typescript) and the [session options](/docs/en/agent-sdk/sessions) it accepts. Pass an `AsyncIterable<SDKUserMessage>` for multi-turn conversations, or `options.resume` to continue a saved session. This page is kept for reference if you maintain code on Agent SDK 0.2.x or earlier.
</Warning>

V2 was an experimental session API that removed the need for async generators and yield coordination. Instead of managing generator state across turns, each turn was a separate `send()`/`stream()` cycle. The API surface reduced to creating a session, sending a message, and streaming the response:

* `createSession()` / `resumeSession()`: Start or continue a conversation
* `session.send()`: Send a message
* `session.stream()`: Get the response

## Installation

Agent SDK 0.2.x is the last version that includes the V2 interface. The package version jumped from 0.2.x directly to 0.3.142, so the removal version above and the install pin below describe the same boundary. To install the last V2-compatible release, pin the major and minor version:

```bash theme={null}
npm install @anthropic-ai/claude-agent-sdk@0.2
```

<Note>
  The SDK bundles a native Claude Code binary for your platform as an optional dependency, so most installs need no separate Claude Code install. See the [quickstart's install note](/docs/en/agent-sdk/quickstart) for the installs that need one.
</Note>

## Quick start

### One-shot prompt

For simple single-turn queries where you don't need to maintain a session, use `unstable_v2_prompt()`. This example sends a math question and logs the answer:

```typescript theme={null}

const result = await unstable_v2_prompt("What is 2 + 2?", {
  model: "claude-opus-4-7"
});
if (result.subtype === "success") {
  console.log(result.result);
}
```

<details>
  <summary>See the same operation in V1</summary>

  ```typescript theme={null}

  const q = query({
    prompt: "What is 2 + 2?",
    options: { model: "claude-opus-4-7" }
  });

  for await (const msg of q) {
    if (msg.type === "result" && msg.subtype === "success") {
      console.log(msg.result);
    }
  }
  ```
</details>

### Basic session

For interactions beyond a single prompt, create a session. V2 separates sending and streaming into distinct steps:

* `send()` dispatches your message
* `stream()` streams back the response

This explicit separation makes it easier to add logic between turns (like processing responses before sending follow-ups).

The example below creates a session, sends "Hello!" to Claude, and prints the text response. It uses [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management) (TypeScript 5.2+) to automatically close the session when the block exits. You can also call `session.close()` manually.

```typescript theme={null}

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

await session.send("Hello!");
for await (const msg of session.stream()) {
  // Filter for assistant messages to get human-readable output
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}
```

<details>
  <summary>See the same operation in V1</summary>

  In V1, both input and output flow through a single async generator. For a basic prompt this looks similar, but adding multi-turn logic requires restructuring to use an input generator.

  ```typescript theme={null}

  const q = query({
    prompt: "Hello!",
    options: { model: "claude-opus-4-7" }
  });

  for await (const msg of q) {
    if (msg.type === "assistant") {
      const text = msg.message.content
        .filter((block) => block.type === "text")
        .map((block) => block.text)
        .join("");
      console.log(text);
    }
  }
  ```
</details>

### Multi-turn conversation

Sessions persist context across multiple exchanges. To continue a conversation, call `send()` again on the same session. Claude remembers the previous turns.

This example asks a math question, then asks a follow-up that references the previous answer:

```typescript theme={null}

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

// Turn 1
await session.send("What is 5 + 3?");
for await (const msg of session.stream()) {
  // Filter for assistant messages to get human-readable output
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}

// Turn 2
await session.send("Multiply that by 2");
for await (const msg of session.stream()) {
  if (msg.type === "assistant") {
    const text = msg.message.content
      .filter((block) => block.type === "text")
      .map((block) => block.text)
      .join("");
    console.log(text);
  }
}
```

<details>
  <summary>See the same operation in V1</summary>

  ```typescript theme={null}

  // Must create an async iterable to feed messages
  async function* createInputStream() {
    yield {
      type: "user",
      session_id: "",
      message: { role: "user", content: [{ type: "text", text: "What is 5 + 3?" }] },
      parent_tool_use_id: null
    };
    // Must coordinate when to yield next message
    yield {
      type: "user",
      session_id: "",
      message: { role: "user", content: [{ type: "text", text: "Multiply by 2" }] },
      parent_tool_use_id: null
    };
  }

  const q = query({
    prompt: createInputStream(),
    options: { model: "claude-opus-4-7" }
  });

  for await (const msg of q) {
    if (msg.type === "assistant") {
      const text = msg.message.content
        .filter((block) => block.type === "text")
        .map((block) => block.text)
        .join("");
      console.log(text);
    }
  }
  ```
</details>

### Session resume

If you have a session ID from a previous interaction, you can resume it later. This is useful for long-running workflows or when you need to persist conversations across application restarts.

This example creates a session, stores its ID, closes it, then resumes the conversation:

```typescript theme={null}
import {
  unstable_v2_createSession,
  unstable_v2_resumeSession,
  type SDKMessage
} from "@anthropic-ai/claude-agent-sdk";

// Helper to extract text from assistant messages
function getAssistantText(msg: SDKMessage): string | null {
  if (msg.type !== "assistant") return null;
  return msg.message.content
    .filter((block) => block.type === "text")
    .map((block) => block.text)
    .join("");
}

// Create initial session and have a conversation
const session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});

await session.send("Remember this number: 42");

// Get the session ID from any received message
let sessionId: string | undefined;
for await (const msg of session.stream()) {
  sessionId = msg.session_id;
  const text = getAssistantText(msg);
  if (text) console.log("Initial response:", text);
}

console.log("Session ID:", sessionId);
session.close();

// Later: resume the session using the stored ID
await using resumedSession = unstable_v2_resumeSession(sessionId!, {
  model: "claude-opus-4-7"
});

await resumedSession.send("What number did I ask you to remember?");
for await (const msg of resumedSession.stream()) {
  const text = getAssistantText(msg);
  if (text) console.log("Resumed response:", text);
}
```

<details>
  <summary>See the same operation in V1</summary>

  ```typescript theme={null}

  // Create initial session
  const initialQuery = query({
    prompt: "Remember this number: 42",
    options: { model: "claude-opus-4-7" }
  });

  // Get session ID from any message
  let sessionId: string | undefined;
  for await (const msg of initialQuery) {
    sessionId = msg.session_id;
    if (msg.type === "assistant") {
      const text = msg.message.content
        .filter((block) => block.type === "text")
        .map((block) => block.text)
        .join("");
      console.log("Initial response:", text);
    }
  }

  console.log("Session ID:", sessionId);

  // Later: resume the session
  const resumedQuery = query({
    prompt: "What number did I ask you to remember?",
    options: {
      model: "claude-opus-4-7",
      resume: sessionId
    }
  });

  for await (const msg of resumedQuery) {
    if (msg.type === "assistant") {
      const text = msg.message.content
        .filter((block) => block.type === "text")
        .map((block) => block.text)
        .join("");
      console.log("Resumed response:", text);
    }
  }
  ```
</details>

### Cleanup

Sessions can be closed manually or automatically using [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management), a TypeScript 5.2+ feature for automatic resource cleanup. If you're using an older TypeScript version or encounter compatibility issues, use manual cleanup instead.

The examples below show only the cleanup pattern and don't send any messages, so running them produces no output.

**Automatic cleanup (TypeScript 5.2+):**

```typescript theme={null}

await using session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});
// Session closes automatically when the block exits
```

**Manual cleanup:**

```typescript theme={null}

const session = unstable_v2_createSession({
  model: "claude-opus-4-7"
});
// ... use the session ...
session.close();
```

## API reference

### `unstable_v2_createSession()`

Creates a new session for multi-turn conversations.

```typescript theme={null}
function unstable_v2_createSession(options: {
  model: string;
  // Additional options supported
}): SDKSession;
```

### `unstable_v2_resumeSession()`

Resumes an existing session by ID.

```typescript theme={null}
function unstable_v2_resumeSession(
  sessionId: string,
  options: {
    model: string;
    // Additional options supported
  }
): SDKSession;
```

### `unstable_v2_prompt()`

One-shot convenience function for single-turn queries.

```typescript theme={null}
function unstable_v2_prompt(
  prompt: string,
  options: {
    model: string;
    // Additional options supported
  }
): Promise<SDKResultMessage>;
```

### SDKSession interface

```typescript theme={null}
interface SDKSession {
  readonly sessionId: string;
  send(message: string | SDKUserMessage): Promise<void>;
  stream(): AsyncGenerator<SDKMessage, void>;
  close(): void;
}
```

## Feature availability

The V2 session API does not support every V1 feature. The following require the [V1 SDK](/docs/en/agent-sdk/typescript):

* Session forking (`forkSession` option)
* Some advanced streaming input patterns

## See also

* [TypeScript SDK reference (V1)](/docs/en/agent-sdk/typescript) - Full V1 SDK documentation
* [SDK overview](/docs/en/agent-sdk/overview) - General SDK concepts
* [V2 examples on GitHub](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world-v2) - Working code examples

---

## Handle approvals and user input

- 官方原文：https://code.claude.com/docs/en/agent-sdk/user-input.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-agent-sdk-user-input.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Handle approvals and user input

> Surface Claude's approval requests and clarifying questions to users, then return their decisions to the SDK.

While working on a task, Claude sometimes needs to check in with users. It might need permission before deleting files, or need to ask which database to use for a new project. Your application needs to surface these requests to users so Claude can continue with their input.

Claude requests user input in two situations: when it needs **permission to use a tool** (like deleting files or running commands), and when it has **clarifying questions** (via the `AskUserQuestion` tool). Both trigger your `canUseTool` callback, which pauses execution until you return a response. This is different from normal conversation turns where Claude finishes and waits for your next message.

For clarifying questions, Claude generates the questions and options. Your role is to present them to users and return their selections. You can't add your own questions to this flow; if you need to ask users something yourself, do that separately in your application logic.

The callback can stay pending indefinitely. Execution remains paused until your callback returns. If a user might take longer to respond than your process can reasonably stay running, register a [`PreToolUse` hook](/docs/en/agent-sdk/hooks) that returns the [`defer` decision](/docs/en/hooks#defer-a-tool-call-for-later) instead of waiting in the callback, so the process can exit and resume later from the persisted session.

This guide shows you how to detect each type of request and respond appropriately.

## Detect when Claude needs input

Pass a `canUseTool` callback in your query options. The callback fires whenever Claude needs user input, receiving the tool name and input as arguments:

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import ClaudeAgentOptions

  async def handle_tool_request(tool_name, input_data, context):
      # Prompt user and return allow or deny
      ...

  options = ClaudeAgentOptions(can_use_tool=handle_tool_request)
  ```

  ```typescript TypeScript theme={null}
  async function handleToolRequest(toolName, input, options) {
    // options includes { signal: AbortSignal, suggestions?: PermissionUpdate[] }
    // Prompt user and return allow or deny
  }

  const options = { canUseTool: handleToolRequest };
  ```
</CodeGroup>

The callback fires in two cases:

1. **Tool needs approval**: Claude wants to use a tool that isn't auto-approved by a [permission rule](/docs/en/agent-sdk/permissions) or permission mode. Check `tool_name` for the tool (e.g., `"Bash"`, `"Write"`).
2. **Claude asks a question**: Claude calls the `AskUserQuestion` tool. Check if `tool_name == "AskUserQuestion"` to handle it differently. If you specify a `tools` array, include `AskUserQuestion` for this to work. See [Handle clarifying questions](#handle-clarifying-questions) for details.

<Warning>
  **The callback never fires for auto-approved tools.** Any approval earlier in the [permission evaluation flow](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated), an allow rule or a mode like `acceptEdits` or `bypassPermissions`, resolves the call before `canUseTool` is consulted. If you list a tool bare in `allowed_tools`, a `canUseTool` check for that tool runs only when the [evaluation flow](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) routes the call back to a prompt, such as an ask rule or `plan` mode. For logic that must apply to every tool call, use a [`PreToolUse` hook](/docs/en/agent-sdk/hooks), which executes before the rest of the flow and can allow, deny, or modify requests.

  An allow rule doesn't pre-approve the [actions no mode auto-approves](/docs/en/permission-modes#actions-no-mode-auto-approves); see [How permissions are evaluated](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) for which of them reach the callback and what happens in `dontAsk` and `auto` mode.
</Warning>

You can also use the [`PermissionRequest` hook](/docs/en/agent-sdk/hooks#available-hooks) to send external notifications (Slack, email, push) when Claude is waiting for approval.

## Handle tool approval requests

Once you've passed a `canUseTool` callback in your query options, it fires when Claude wants to use a tool that nothing earlier in the permission flow has approved. In some configurations, such as `dontAsk` mode, Claude Code doesn't call it; the last step of [How permissions are evaluated](/docs/en/agent-sdk/permissions#how-permissions-are-evaluated) lists them and says what happens to the call instead.

Your callback receives three arguments:

| Argument                            | Description                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `toolName`                          | The name of the tool Claude wants to use (for example, `"Bash"`, `"Write"`, `"Edit"`)                                                                                                                                                                                                                                                 |
| `input`                             | The parameters Claude is passing to the tool. Contents vary by tool.                                                                                                                                                                                                                                                                  |
| `options` (TS) / `context` (Python) | Additional context including optional `suggestions` (proposed `PermissionUpdate` entries to avoid re-prompting) and a cancellation signal. In TypeScript, `signal` is an `AbortSignal`; in Python, the signal field is reserved for future use. See [`ToolPermissionContext`](/docs/en/agent-sdk/python#toolpermissioncontext) for Python. |

The `input` object contains tool-specific parameters. Common examples:

| Tool    | Input fields                            |
| ------- | --------------------------------------- |
| `Bash`  | `command`, `description`, `timeout`     |
| `Write` | `file_path`, `content`                  |
| `Edit`  | `file_path`, `old_string`, `new_string` |
| `Read`  | `file_path`, `offset`, `limit`          |

See the SDK reference for complete input schemas: [Python](/docs/en/agent-sdk/python#tool-input%2Foutput-types) | [TypeScript](/docs/en/agent-sdk/typescript#tool-input-types).

You can display this information to the user so they can decide whether to allow or reject the action, then return the appropriate response.

The following example asks Claude to create and delete a test file. When Claude attempts each operation, the callback prints the tool request to the terminal and prompts for y/n approval.

<CodeGroup>
  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
  from claude_agent_sdk.types import (
      HookMatcher,
      PermissionResultAllow,
      PermissionResultDeny,
      ToolPermissionContext,
  )

  async def can_use_tool(
      tool_name: str, input_data: dict, context: ToolPermissionContext
  ) -> PermissionResultAllow | PermissionResultDeny:
      # Display the tool request
      print(f"\nTool: {tool_name}")
      if tool_name == "Bash":
          print(f"Command: {input_data.get('command')}")
          if input_data.get("description"):
              print(f"Description: {input_data.get('description')}")
      else:
          print(f"Input: {input_data}")

      # Get user approval
      response = input("Allow this action? (y/n): ")

      # Return allow or deny based on user's response
      if response.lower() == "y":
          # Allow: tool executes with the original (or modified) input
          return PermissionResultAllow(updated_input=input_data)
      else:
          # Deny: tool doesn't execute, Claude sees the message
          return PermissionResultDeny(message="User denied this action")

  # Required workaround: dummy hook keeps the stream open for can_use_tool
  async def dummy_hook(input_data, tool_use_id, context):
      return {"continue_": True}

  async def prompt_stream():
      yield {
          "type": "user",
          "message": {
              "role": "user",
              "content": "Create a test file in /tmp and then delete it",
          },
      }

  async def main():
      async for message in query(
          prompt=prompt_stream(),
          options=ClaudeAgentOptions(
              can_use_tool=can_use_tool,
              hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[dummy_hook])]},
          ),
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Helper to prompt user for input in the terminal
  function prompt(question: string): Promise<string> {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    return new Promise((resolve) =>
      rl.question(question, (answer) => {
        rl.close();
        resolve(answer);
      })
    );
  }

  for await (const message of query({
    prompt: "Create a test file in /tmp and then delete it",
    options: {
      canUseTool: async (toolName, input) => {
        // Display the tool request
        console.log(`\nTool: ${toolName}`);
        if (toolName === "Bash") {
          console.log(`Command: ${input.command}`);
          if (input.description) console.log(`Description: ${input.description}`);
        } else {
          console.log(`Input: ${JSON.stringify(input, null, 2)}`);
        }

        // Get user approval
        const response = await prompt("Allow this action? (y/n): ");

        // Return allow or deny based on user's response
        if (response.toLowerCase() === "y") {
          // Allow: tool executes with the original (or modified) input
          return { behavior: "allow", updatedInput: input };
        } else {
          // Deny: tool doesn't execute, Claude sees the message
          return { behavior: "deny", message: "User denied this action" };
        }
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

This example uses a `y/n` flow where any input other than `y` is treated as a denial. In practice, you might build a richer UI that lets users modify the request, provide feedback, or redirect Claude entirely. See [Respond to tool requests](#respond-to-tool-requests) for all the ways you can respond.

### Respond to tool requests

Your callback returns one of two response types:

| Response  | Python                                     | TypeScript                            |
| --------- | ------------------------------------------ | ------------------------------------- |
| **Allow** | `PermissionResultAllow(updated_input=...)` | `{ behavior: "allow", updatedInput }` |
| **Deny**  | `PermissionResultDeny(message=...)`        | `{ behavior: "deny", message }`       |

When allowing, the tool runs with the input Claude requested unless you return a modified input, `updatedInput` in TypeScript or `updated_input` in Python. Before v2.1.207, Claude Code rejected an allow result that omitted `updatedInput` and denied the tool call with a validation error.

When denying, provide a message explaining why. Claude sees this message and may adjust its approach.

Beyond allowing or denying, you can modify the tool's input or provide context that helps Claude adjust its approach:

* **Approve**: let the tool execute as Claude requested
* **Approve with changes**: modify the input before execution (for example, sanitize paths, add constraints)
* **Approve and remember**: echo a suggested permission rule back so matching calls skip the prompt next time
* **Reject**: block the tool and tell Claude why
* **Suggest alternative**: block but guide Claude toward what the user wants instead
* **Redirect entirely**: use [streaming input](/docs/en/agent-sdk/streaming-vs-single-mode) to send Claude a completely new instruction

The `ask_user` and `askUser` helpers in the following snippets stand in for your application's own prompt UI.

  <Tab title="Approve">
    The user approves the action as-is. Pass through the `input` from your callback unchanged and the tool executes exactly as Claude requested.

    <CodeGroup>
      ```python Python theme={null}
      async def can_use_tool(tool_name, input_data, context):
          print(f"Claude wants to use {tool_name}")
          approved = await ask_user("Allow this action?")

          if approved:
              return PermissionResultAllow(updated_input=input_data)
          return PermissionResultDeny(message="User declined")
      ```

      ```typescript TypeScript theme={null}
      canUseTool: async (toolName, input) => {
        console.log(`Claude wants to use ${toolName}`);
        const approved = await askUser("Allow this action?");

        if (approved) {
          return { behavior: "allow", updatedInput: input };
        }
        return { behavior: "deny", message: "User declined" };
      };
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Approve with changes">
    The user approves but wants to modify the request first. You can change the input before the tool executes. Claude sees the result but isn't told you changed anything. Useful for sanitizing parameters, adding constraints, or scoping access.

    <CodeGroup>
      ```python Python theme={null}
      async def can_use_tool(tool_name, input_data, context):
          if tool_name == "Bash":
              # User approved, but scope all commands to sandbox
              sandboxed_input = {**input_data}
              sandboxed_input["command"] = input_data["command"].replace(
                  "/tmp", "/tmp/sandbox"
              )
              return PermissionResultAllow(updated_input=sandboxed_input)
          return PermissionResultAllow(updated_input=input_data)
      ```

      ```typescript TypeScript theme={null}
      canUseTool: async (toolName, input) => {
        if (toolName === "Bash") {
          // User approved, but scope all commands to sandbox
          const sandboxedInput = {
            ...input,
            command: input.command.replace("/tmp", "/tmp/sandbox")
          };
          return { behavior: "allow", updatedInput: sandboxedInput };
        }
        return { behavior: "allow", updatedInput: input };
      };
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Approve and remember">
    The user approves and doesn't want to be asked again for this kind of call. The third callback argument carries `suggestions`, an array of ready-made [`PermissionUpdate`](/docs/en/agent-sdk/typescript#permissionupdate) entries. Echo one back in `updatedPermissions` to apply it. A suggestion with the `localSettings` destination writes the rule to `.claude/settings.local.json` so future sessions skip the prompt for matching calls.

    The Python example requires `claude-agent-sdk` 0.1.80 or later.

    <CodeGroup>
      ```python Python theme={null}
      async def can_use_tool(tool_name, input_data, context):
          choice = await ask_user(f"Allow {tool_name}?", ["once", "always", "no"])

          if choice == "always":
              persist = [
                  s for s in context.suggestions if s.destination == "localSettings"
              ]
              return PermissionResultAllow(
                  updated_input=input_data, updated_permissions=persist
              )
          if choice == "once":
              return PermissionResultAllow(updated_input=input_data)
          return PermissionResultDeny(message="User declined")
      ```

      ```typescript TypeScript theme={null}
      canUseTool: async (toolName, input, { suggestions = [] }) => {
        const choice = await askUser(`Allow ${toolName}?`, ["once", "always", "no"]);

        if (choice === "always") {
          const persist = suggestions.filter(
            (s) => s.destination === "localSettings"
          );
          return {
            behavior: "allow",
            updatedInput: input,
            updatedPermissions: persist
          };
        }
        if (choice === "once") {
          return { behavior: "allow", updatedInput: input };
        }
        return { behavior: "deny", message: "User declined" };
      };
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Reject">
    The user doesn't want this action to happen. Block the tool and provide a message explaining why. Claude sees this message and may try a different approach.

    <CodeGroup>
      ```python Python theme={null}
      async def can_use_tool(tool_name, input_data, context):
          approved = await ask_user(f"Allow {tool_name}?")

          if not approved:
              return PermissionResultDeny(message="User rejected this action")
          return PermissionResultAllow(updated_input=input_data)
      ```

      ```typescript TypeScript theme={null}
      canUseTool: async (toolName, input) => {
        const approved = await askUser(`Allow ${toolName}?`);

        if (!approved) {
          return {
            behavior: "deny",
            message: "User rejected this action"
          };
        }
        return { behavior: "allow", updatedInput: input };
      };
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Suggest alternative">
    The user doesn't want this specific action, but has a different idea. Block the tool and include guidance in your message. Claude will read this and decide how to proceed based on your feedback.

    <CodeGroup>
      ```python Python theme={null}
      async def can_use_tool(tool_name, input_data, context):
          if tool_name == "Bash" and "rm" in input_data.get("command", ""):
              # User doesn't want to delete, suggest archiving instead
              return PermissionResultDeny(
                  message="User doesn't want to delete files. They asked if you could compress them into an archive instead."
              )
          return PermissionResultAllow(updated_input=input_data)
      ```

      ```typescript TypeScript theme={null}
      canUseTool: async (toolName, input) => {
        if (toolName === "Bash" && input.command.includes("rm")) {
          // User doesn't want to delete, suggest archiving instead
          return {
            behavior: "deny",
            message:
              "User doesn't want to delete files. They asked if you could compress them into an archive instead."
          };
        }
        return { behavior: "allow", updatedInput: input };
      };
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Redirect entirely">
    For a complete change of direction (not just a nudge), use [streaming input](/docs/en/agent-sdk/streaming-vs-single-mode) to send Claude a new instruction directly. This bypasses the current tool request and gives Claude entirely new instructions to follow.
  </Tab>

## Handle clarifying questions

When Claude needs more direction on a task with multiple valid approaches, it calls the `AskUserQuestion` tool. This triggers your `canUseTool` callback with `toolName` set to `AskUserQuestion`. The input contains Claude's questions as multiple-choice options, which you display to the user and return their selections.

<Tip>
  Clarifying questions are especially common in [`plan` mode](/docs/en/agent-sdk/permissions#plan-mode-plan), where Claude explores the codebase and asks questions before proposing a plan. This makes plan mode ideal for interactive workflows where you want Claude to gather requirements before making changes.
</Tip>

The following steps show how to handle clarifying questions:

    Pass a `canUseTool` callback in your query options. By default, `AskUserQuestion` is available. If you specify a `tools` array to restrict Claude's capabilities (for example, a read-only agent with only `Read`, `Glob`, and `Grep`), include `AskUserQuestion` in that array. Otherwise, Claude won't be able to ask clarifying questions:

    <CodeGroup>
      ```python Python theme={null}
      async for message in query(
          prompt="Analyze this codebase",
          options=ClaudeAgentOptions(
              # Include AskUserQuestion in your tools list
              tools=["Read", "Glob", "Grep", "AskUserQuestion"],
              can_use_tool=can_use_tool,
          ),
      ):
          print(message)
      ```

      ```typescript TypeScript theme={null}
      for await (const message of query({
        prompt: "Analyze this codebase",
        options: {
          // Include AskUserQuestion in your tools list
          tools: ["Read", "Glob", "Grep", "AskUserQuestion"],
          canUseTool: async (toolName, input) => {
            // Handle clarifying questions here
          }
        }
      })) {
        console.log(message);
      }
      ```
    </CodeGroup>

    In your callback, check if `toolName` equals `AskUserQuestion` to handle it differently from other tools:

    <CodeGroup>
      ```python Python theme={null}
      async def can_use_tool(tool_name: str, input_data: dict, context):
          if tool_name == "AskUserQuestion":
              # Your implementation to collect answers from the user
              return await handle_clarifying_questions(input_data)
          # Handle other tools normally
          return await prompt_for_approval(tool_name, input_data)
      ```

      ```typescript TypeScript theme={null}
      canUseTool: async (toolName, input) => {
        if (toolName === "AskUserQuestion") {
          // Your implementation to collect answers from the user
          return handleClarifyingQuestions(input);
        }
        // Handle other tools normally
        return promptForApproval(toolName, input);
      };
      ```
    </CodeGroup>

    The input contains Claude's questions in a `questions` array. Each question has a `question` (the text to display), `options` (the choices), and `multiSelect` (whether multiple selections are allowed):

    ```json theme={null}
    {
      "questions": [
        {
          "question": "How should I format the output?",
          "header": "Format",
          "options": [
            { "label": "Summary", "description": "Brief overview" },
            { "label": "Detailed", "description": "Full explanation" }
          ],
          "multiSelect": false
        },
        {
          "question": "Which sections should I include?",
          "header": "Sections",
          "options": [
            { "label": "Introduction", "description": "Opening context" },
            { "label": "Conclusion", "description": "Final summary" }
          ],
          "multiSelect": true
        }
      ]
    }
    ```

    See [Question format](#question-format) for full field descriptions.

    Present the questions to the user and collect their selections. How you do this depends on your application: a terminal prompt, a web form, a mobile dialog, etc.

    Build the `answers` object as a record where each key is the `question` text and each value is the selected option's `label`:

    | From the question object                                            | Use as |
    | ------------------------------------------------------------------- | ------ |
    | `question` field (for example, `"How should I format the output?"`) | Key    |
    | Selected option's `label` field (for example, `"Summary"`)          | Value  |

    For multi-select questions, pass an array of labels or join them with `", "`. If you [support free-text input](#support-free-text-input), use the user's custom text as the value.

    <CodeGroup>
      ```python Python theme={null}
      return PermissionResultAllow(
          updated_input={
              "questions": input_data.get("questions", []),
              "answers": {
                  "How should I format the output?": "Summary",
                  "Which sections should I include?": ["Introduction", "Conclusion"],
              },
          }
      )
      ```

      ```typescript TypeScript theme={null}
      return {
        behavior: "allow",
        updatedInput: {
          questions: input.questions,
          answers: {
            "How should I format the output?": "Summary",
            "Which sections should I include?": "Introduction, Conclusion"
          }
        }
      };
      ```
    </CodeGroup>

### Question format

The input contains Claude's generated questions in a `questions` array. Each question has these fields:

| Field         | Description                                                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `question`    | The full question text to display                                                                                                                |
| `header`      | Short label for the question (max 12 characters)                                                                                                 |
| `options`     | Array of 2-4 choices, each with `label` and `description`. TypeScript: optionally `preview`. See [Option previews](#option-previews-typescript). |
| `multiSelect` | If `true`, users can select multiple options                                                                                                     |

The structure your callback receives:

```json theme={null}
{
  "questions": [
    {
      "question": "How should I format the output?",
      "header": "Format",
      "options": [
        { "label": "Summary", "description": "Brief overview of key points" },
        { "label": "Detailed", "description": "Full explanation with examples" }
      ],
      "multiSelect": false
    }
  ]
}
```

#### Option previews (TypeScript)

`toolConfig.askUserQuestion.previewFormat` adds a `preview` field to each option so your app can show a visual mockup alongside the label. Without this setting, Claude does not generate previews and the field is absent.

| `previewFormat` | `preview` contains                                                                                            |
| :-------------- | :------------------------------------------------------------------------------------------------------------ |
| unset (default) | Field is absent. Claude does not generate previews.                                                           |
| `"markdown"`    | ASCII art and fenced code blocks                                                                              |
| `"html"`        | A styled `<div>` fragment (the SDK rejects `<script>`, `<style>`, and `<!DOCTYPE>` before your callback runs) |

The format applies to all questions in the session. Claude includes `preview` on options where a visual comparison helps (layout choices, color schemes) and omits it where one wouldn't (yes/no confirmations, text-only choices). Check for `undefined` before rendering.

```typescript theme={null}

for await (const message of query({
  prompt: "Help me choose a card layout",
  options: {
    toolConfig: {
      askUserQuestion: { previewFormat: "html" }
    },
    canUseTool: async (toolName, input) => {
      // input.questions[].options[].preview is an HTML string or undefined
      return { behavior: "allow", updatedInput: input };
    }
  }
})) {
  // ...
}
```

An option with an HTML preview:

```json theme={null}
{
  "label": "Compact",
  "description": "Title and metric value only",
  "preview": "<div style=\"padding:12px;border:1px solid #ddd;border-radius:8px\"><div style=\"font-size:12px;color:#666\">Active users</div><div style=\"font-size:28px;font-weight:600\">1,284</div></div>"
}
```

### Response format

Return an `answers` object mapping each question's `question` field to the selected option's `label`:

| Field       | Description                                                                          |
| ----------- | ------------------------------------------------------------------------------------ |
| `questions` | Pass through the original questions array (required for tool processing)             |
| `answers`   | Object where keys are question text and values are selected labels                   |
| `response`  | Optional freeform reply the user typed instead of answering the structured questions |

For multi-select questions, pass an array of labels or join them with `", "`. For per-question free text such as an "Other" option, put the user's text in `answers[question]` as shown in [Support free-text input](#support-free-text-input). Set `response` only when your UI lets the user dismiss the question card and type a general reply that isn't an answer to any specific question. When `response` is set, Claude receives "The user responded: …" instead of the per-question answer list.

```jsonc theme={null}
{
  "questions": [
    // ...
  ],
  "answers": {
    "How should I format the output?": "Summary",
    "Which sections should I include?": ["Introduction", "Conclusion"]
  }
}
```

#### Support free-text input

Claude's predefined options won't always cover what users want. To let users type their own answer:

* Display an additional "Other" choice after Claude's options that accepts text input
* Use the user's custom text as the answer value (not the word "Other")

See the [complete example](#complete-example) below for a full implementation.

### Complete example

Claude asks clarifying questions when it needs user input to proceed. For example, when asked to help decide on a tech stack for a mobile app, Claude might ask about cross-platform vs native, backend preferences, or target platforms. These questions help Claude make decisions that match the user's preferences rather than guessing.

This example handles those questions in a terminal application. Here's what happens at each step:

1. **Route the request**: The `canUseTool` callback checks if the tool name is `"AskUserQuestion"` and routes to a dedicated handler
2. **Display questions**: The handler loops through the `questions` array and prints each question with numbered options
3. **Collect input**: The user can enter a number to select an option, or type free text directly (for example, "jquery", "i don't know")
4. **Map answers**: The code checks if input is numeric (uses the option's label) or free text (uses the text directly)
5. **Return to Claude**: The response includes both the original `questions` array and the `answers` mapping

Save the TypeScript version as `ask.ts` and run it with `npx tsx ask.ts`, or save the Python version as `ask.py` and run it with `python ask.py`.

<CodeGroup>
  ```python Python theme={null}
  import asyncio

  from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query
  from claude_agent_sdk.types import HookMatcher, PermissionResultAllow

  def parse_response(response: str, options: list) -> str:
      """Parse user input as option number(s) or free text."""
      try:
          indices = [int(s.strip()) - 1 for s in response.split(",")]
          labels = [options[i]["label"] for i in indices if 0 <= i < len(options)]
          return ", ".join(labels) if labels else response
      except ValueError:
          return response

  async def handle_ask_user_question(input_data: dict) -> PermissionResultAllow:
      """Display Claude's questions and collect user answers."""
      answers = {}

      for q in input_data.get("questions", []):
          print(f"\n{q['header']}: {q['question']}")

          options = q["options"]
          for i, opt in enumerate(options):
              print(f"  {i + 1}. {opt['label']} - {opt['description']}")
          if q.get("multiSelect"):
              print("  (Enter numbers separated by commas, or type your own answer)")
          else:
              print("  (Enter a number, or type your own answer)")

          response = input("Your choice: ").strip()
          answers[q["question"]] = parse_response(response, options)

      return PermissionResultAllow(
          updated_input={
              "questions": input_data.get("questions", []),
              "answers": answers,
          }
      )

  async def can_use_tool(
      tool_name: str, input_data: dict, context
  ) -> PermissionResultAllow:
      # Route AskUserQuestion to our question handler
      if tool_name == "AskUserQuestion":
          return await handle_ask_user_question(input_data)
      # Auto-approve other tools for this example
      return PermissionResultAllow(updated_input=input_data)

  async def prompt_stream():
      yield {
          "type": "user",
          "message": {
              "role": "user",
              "content": "Help me decide on the tech stack for a new mobile app",
          },
      }

  # Required workaround: dummy hook keeps the stream open for can_use_tool
  async def dummy_hook(input_data, tool_use_id, context):
      return {"continue_": True}

  async def main():
      async for message in query(
          prompt=prompt_stream(),
          options=ClaudeAgentOptions(
              can_use_tool=can_use_tool,
              hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[dummy_hook])]},
          ),
      ):
          if isinstance(message, ResultMessage) and message.subtype == "success":
              print(message.result)

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}

  // Helper to prompt user for input in the terminal
  async function prompt(question: string): Promise<string> {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    const answer = await rl.question(question);
    rl.close();
    return answer;
  }

  // Parse user input as option number(s) or free text
  function parseResponse(response: string, options: any[]): string {
    const indices = response.split(",").map((s) => parseInt(s.trim()) - 1);
    const labels = indices
      .filter((i) => !isNaN(i) && i >= 0 && i < options.length)
      .map((i) => options[i].label);
    return labels.length > 0 ? labels.join(", ") : response;
  }

  // Display Claude's questions and collect user answers
  async function handleAskUserQuestion(input: any) {
    const answers: Record<string, string> = {};

    for (const q of input.questions) {
      console.log(`\n${q.header}: ${q.question}`);

      const options = q.options;
      options.forEach((opt: any, i: number) => {
        console.log(`  ${i + 1}. ${opt.label} - ${opt.description}`);
      });
      if (q.multiSelect) {
        console.log("  (Enter numbers separated by commas, or type your own answer)");
      } else {
        console.log("  (Enter a number, or type your own answer)");
      }

      const response = (await prompt("Your choice: ")).trim();
      answers[q.question] = parseResponse(response, options);
    }

    // Return the answers to Claude (must include original questions)
    return {
      behavior: "allow",
      updatedInput: { questions: input.questions, answers }
    };
  }

  async function main() {
    for await (const message of query({
      prompt: "Help me decide on the tech stack for a new mobile app",
      options: {
        canUseTool: async (toolName, input) => {
          // Route AskUserQuestion to our question handler
          if (toolName === "AskUserQuestion") {
            return handleAskUserQuestion(input);
          }
          // Auto-approve other tools for this example
          return { behavior: "allow", updatedInput: input };
        }
      }
    })) {
      if ("result" in message) console.log(message.result);
    }
  }

  main();
  ```
</CodeGroup>

## Limitations

* **Subagents**: `AskUserQuestion` is not currently available in subagents spawned via the Agent tool
* **Question limits**: each `AskUserQuestion` call supports 1-4 questions with 2-4 options each

## Other ways to get user input

The `canUseTool` callback and `AskUserQuestion` tool cover most approval and clarification scenarios, but the SDK offers other ways to get input from users:

### Streaming input

Use [streaming input](/docs/en/agent-sdk/streaming-vs-single-mode) when you need to:

* **Interrupt the agent mid-task**: send a cancel signal or change direction while Claude is working
* **Provide additional context**: add information Claude needs without waiting for it to ask
* **Build chat interfaces**: let users send follow-up messages during long-running operations

Streaming input is ideal for conversational UIs where users interact with the agent throughout execution, not just at approval checkpoints.

### Custom tools

Use [custom tools](/docs/en/agent-sdk/custom-tools) when you need to:

* **Collect structured input**: build forms, wizards, or multi-step workflows that go beyond `AskUserQuestion`'s multiple-choice format
* **Integrate external approval systems**: connect to existing ticketing, workflow, or approval platforms
* **Implement domain-specific interactions**: create tools tailored to your application's needs, like code review interfaces or deployment checklists

Custom tools give you full control over the interaction, but require more implementation work than using the built-in `canUseTool` callback.

## Related resources

* [Configure permissions](/docs/en/agent-sdk/permissions): set up permission modes and rules
* [Control execution with hooks](/docs/en/agent-sdk/hooks): run custom code at key points in the agent lifecycle
* [TypeScript SDK reference](/docs/en/agent-sdk/typescript#canusetool): full canUseTool API documentation
