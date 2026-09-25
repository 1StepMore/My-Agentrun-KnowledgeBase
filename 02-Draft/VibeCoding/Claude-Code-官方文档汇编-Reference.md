---
title: Claude Code 官方文档汇编 · Reference
source: Claude Code 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/claude-code/claude-code-en-channels-reference.md
- VibeCoding/claude-code/claude-code-en-checkpointing.md
- VibeCoding/claude-code/claude-code-en-cli-reference.md
- VibeCoding/claude-code/claude-code-en-glossary.md
- VibeCoding/claude-code/claude-code-en-interactive-mode.md
- VibeCoding/claude-code/claude-code-en-plugins-reference.md
- VibeCoding/claude-code/claude-code-en-tools-reference.md
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

> **汇编性质**：Claude Code 官方文档 官方原文 7 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## Channels reference

- 官方原文：https://code.claude.com/docs/en/channels-reference.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-channels-reference.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Channels reference

> Build an MCP server that pushes webhooks, alerts, and chat messages into a Claude Code session. Reference for the channel contract: capability declaration, notification events, reply tools, sender gating, and permission relay.

<Note>
  Channels are in [research preview](/docs/en/channels#research-preview). Team and Enterprise organizations must [explicitly enable them](/docs/en/channels#enterprise-controls).
</Note>

A channel is an MCP server that pushes events into a Claude Code session so Claude can react to things happening outside the terminal.

You can build a one-way or two-way channel. One-way channels forward alerts, webhooks, or monitoring events for Claude to act on. Two-way channels like chat bridges also [expose a reply tool](#expose-a-reply-tool) so Claude can send messages back. A channel with a trusted sender path can also opt in to [relay permission prompts](#relay-permission-prompts) so you can approve or deny tool use remotely.

This page covers:

* [Overview](#overview): how channels work
* [What you need](#what-you-need): requirements and general steps
* [Example: build a webhook receiver](#example-build-a-webhook-receiver): a minimal one-way walkthrough
* [Server options](#server-options): the constructor fields
* [Notification format](#notification-format): the event payload and delivery behavior
* [Expose a reply tool](#expose-a-reply-tool): let Claude send messages back
* [Gate inbound messages](#gate-inbound-messages): sender checks to prevent prompt injection
* [Relay permission prompts](#relay-permission-prompts): forward tool approval prompts to remote channels

To use an existing channel instead of building one, see [Channels](/docs/en/channels). Telegram, Discord, iMessage, and fakechat are included in the research preview.

## Overview

A channel is an [MCP](https://modelcontextprotocol.io) server that runs on the same machine as Claude Code. Claude Code spawns it as a subprocess and communicates over stdio. Your channel server is the bridge between external systems and the Claude Code session:

* **Chat platforms** (Telegram, Discord): your plugin runs locally and polls the platform's API for new messages. When someone DMs your bot, the plugin receives the message and forwards it to Claude. No URL to expose.
* **Webhooks** (CI, monitoring): your server listens on a local HTTP port. External systems POST to that port, and your server pushes the payload to Claude.

<img src="https://mintcdn.com/claude-code/9FG0ZKj9uKYiHmbi/images/channel-architecture.svg?fit=max&auto=format&n=9FG0ZKj9uKYiHmbi&q=85&s=9a037b7da80184ae49015c0256b21a1f" className="dark:hidden" alt="Architecture diagram showing external systems connecting to your local channel server, which communicates with Claude Code over stdio" width="600" height="220" data-path="images/channel-architecture.svg" />

<img src="https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/channel-architecture-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=ae1e494440806a6a5d74a1279e22e162" className="hidden dark:block" alt="Architecture diagram showing external systems connecting to your local channel server, which communicates with Claude Code over stdio" width="600" height="220" data-path="images/channel-architecture-dark.svg" />

## What you need

The only hard requirement is the [`@modelcontextprotocol/sdk`](https://www.npmjs.com/package/@modelcontextprotocol/sdk) package and a Node.js-compatible runtime. [Bun](https://bun.sh), [Node](https://nodejs.org), and [Deno](https://deno.com) all work. The pre-built plugins in the research preview use Bun, but your channel doesn't have to.

Your server needs to:

1. Declare the `claude/channel` capability so Claude Code registers a notification listener
2. Emit `notifications/claude/channel` events when something happens
3. Connect over [stdio transport](https://modelcontextprotocol.io/docs/concepts/transports#standard-io)

The [Server options](#server-options) and [Notification format](#notification-format) sections cover each of these in detail. See [Example: build a webhook receiver](#example-build-a-webhook-receiver) for a full walkthrough.

During the research preview, custom channels aren't on the [approved allowlist](/docs/en/channels#supported-channels). Use `--dangerously-load-development-channels` to test locally. See [Test during the research preview](#test-during-the-research-preview) for details.

## Example: build a webhook receiver

This walkthrough builds a single-file server that listens for HTTP requests and forwards them into your Claude Code session. By the end, anything that can send an HTTP POST, like a CI pipeline, a monitoring alert, or a `curl` command, can push events to Claude.

This example uses [Bun](https://bun.sh) as the runtime for its built-in HTTP server and TypeScript support. You can use [Node](https://nodejs.org) or [Deno](https://deno.com) instead; the only requirement is the [MCP SDK](https://www.npmjs.com/package/@modelcontextprotocol/sdk).

    The [permission relay](#relay-permission-prompts) examples import `zod` directly, so it installs alongside the MCP SDK. Create a new directory and install both:

    ```bash theme={null}
    mkdir webhook-channel && cd webhook-channel
    bun add @modelcontextprotocol/sdk zod
    ```

    Create a file called `webhook.ts`. This is your entire channel server: it connects to Claude Code over stdio, and it listens for HTTP POSTs on port 8788. When a request arrives, it pushes the body to Claude as a channel event.

    ```ts title="webhook.ts" theme={null}
    #!/usr/bin/env bun

    // Create the MCP server and declare it as a channel
    const mcp = new Server(
      { name: 'webhook', version: '0.0.1' },
      {
        // this key is what makes it a channel — Claude Code registers a listener for it
        capabilities: { experimental: { 'claude/channel': {} } },
        // Claude Code delivers this to Claude as context when the server connects, so it knows how to handle these events
        instructions: 'Events from the webhook channel arrive as <channel source="webhook" ...>. They are one-way: read them and act, no reply expected.',
      },
    )

    // Connect to Claude Code over stdio (Claude Code spawns this process)
    await mcp.connect(new StdioServerTransport())

    // Start an HTTP server that forwards every POST to Claude
    Bun.serve({
      port: 8788,  // any open port works
      // localhost-only: nothing outside this machine can POST
      hostname: '127.0.0.1',
      async fetch(req) {
        const body = await req.text()
        await mcp.notification({
          method: 'notifications/claude/channel',
          params: {
            content: body,  // becomes the body of the <channel> tag
            // each key becomes a tag attribute, e.g. <channel path="/" method="POST">
            meta: { path: new URL(req.url).pathname, method: req.method },
          },
        })
        return new Response('ok')
      },
    })
    ```

    The file configures the server, connects over stdio, and starts an HTTP listener, in that order:

    * **Server configuration**: creates the MCP server with `claude/channel` in its capabilities, which is what tells Claude Code this is a channel. Claude Code delivers the [`instructions`](#server-options) string to Claude as context when the server connects: tell Claude what events to expect, whether to reply, and how to route replies if it should.
    * **Stdio connection**: connects to Claude Code over stdin/stdout. This is standard for any [MCP server](https://modelcontextprotocol.io/docs/concepts/transports#standard-io).
    * **HTTP listener**: starts a local web server on port 8788. Every POST body gets forwarded to Claude as a channel event via `mcp.notification()`. The `content` becomes the event body, and each `meta` entry becomes an attribute on the `<channel>` tag. The listener needs access to the `mcp` instance, so it runs in the same process. You could split it into separate modules for a larger project.

    Add the server to your MCP config so Claude Code knows how to start it. For a project-level `.mcp.json` in the same directory, use a relative path. For user-level config in `~/.claude.json`, use the full absolute path so the server can be found from any project:

    ```json title=".mcp.json" theme={null}
    {
      "mcpServers": {
        "webhook": { "command": "bun", "args": ["./webhook.ts"] }
      }
    }
    ```

    Claude Code reads your MCP config at startup and spawns each server as a subprocess.

    During the research preview, custom channels aren't on the allowlist, so start Claude Code with the development flag:

    ```bash theme={null}
    claude --dangerously-load-development-channels server:webhook
    ```

    Claude Code first shows a full-screen warning dialog listing the development channels you're loading. Select **I am using this for local development** to continue, or **Exit** to quit.

    The first time you start a session in this project, Claude Code also asks for consent before using the new server from `.mcp.json`. The dialog reports "New MCP server found in this project: webhook". Select **Use this MCP server** to continue.

    After you accept, Claude Code spawns your `webhook.ts` as a subprocess, and the HTTP listener starts automatically on the port you configured, 8788 in this example. You don't need to run the server yourself.

    A dim notice below the startup banner confirms the channel is registered: `Channels (experimental) messages from server:webhook inject directly in this session · restart without --dangerously-load-development-channels to stop`.

    If you see "blocked by org policy," your organization admin needs to [enable channels](/docs/en/channels#enterprise-controls) first.

    In a separate terminal, simulate a webhook by sending an HTTP POST with a message to your server. This example sends a CI failure alert to port 8788 (or whichever port you configured):

    ```bash theme={null}
    curl -X POST localhost:8788 -d "build failed on main: https://ci.example.com/run/1234"
    ```

    The payload arrives in Claude's context as a `<channel>` tag:

    ```text theme={null}
    <channel source="webhook" path="/" method="POST">build failed on main: https://ci.example.com/run/1234</channel>
    ```

    Your terminal renders the event as a one-line summary, `← webhook: build failed on main: https://ci.example.com/run/1234`, rather than the raw tag. You'll then see Claude start responding: reading files, running commands, or whatever the message calls for. This is a one-way channel, so Claude acts in your session but doesn't send anything back through the webhook. To add replies, see [Expose a reply tool](#expose-a-reply-tool).

    If the event doesn't arrive, the diagnosis depends on what `curl` returned:

    * **`curl` succeeds but nothing reaches Claude**: run `/mcp` in your session to check the server's status. A `failed` status usually means a dependency or import error in your server file. To see the stderr trace, restart with `claude --debug --dangerously-load-development-channels server:webhook` and check the debug log at `~/.claude/debug/<session-id>.txt`.
    * **`curl` fails with "connection refused"**: the port is either not bound yet or a stale process from an earlier run is holding it. `lsof -i :<port>` shows what's listening; `kill` the stale process before restarting your session.

The [fakechat server](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/fakechat) extends this pattern with a web UI, file attachments, and a reply tool for two-way chat.

## Test during the research preview

During the research preview, every channel must be on the [approved allowlist](/docs/en/channels#research-preview) to register. The development flag bypasses the allowlist for specific entries after a confirmation prompt. This example shows both entry types:

```bash theme={null}
# Testing a plugin you're developing
claude --dangerously-load-development-channels plugin:yourplugin@yourmarketplace

# Testing a bare .mcp.json server (no plugin wrapper yet)
claude --dangerously-load-development-channels server:webhook
```

The bypass is per-entry. Combining this flag with `--channels` doesn't extend the bypass to the `--channels` entries. During the research preview, the approved allowlist is Anthropic-curated, so your channel stays on the development flag while you build and test.

<Note>
  This flag skips the allowlist only. The `channelsEnabled` organization policy still applies. Don't use it to run channels from untrusted sources.
</Note>

## Server options

A channel sets these options in the [`Server`](https://modelcontextprotocol.io/docs/learn/server-concepts) constructor. The `instructions` and `capabilities.tools` fields are [standard MCP](https://modelcontextprotocol.io/docs/learn/server-concepts); `capabilities.experimental['claude/channel']` and `capabilities.experimental['claude/channel/permission']` are the channel-specific additions:

| Field                                                    | Type                | Description                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------- | :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `capabilities.experimental['claude/channel']`            | `object`            | Required. Always `{}`. Presence registers the notification listener.                                                                                                                                                                                                                                                                                                                 |
| `capabilities.experimental['claude/channel/permission']` | `object` or `false` | Optional. Set it to `{}` to declare that this channel can receive permission relay requests. When declared, Claude Code forwards tool approval prompts to your channel so you can approve or deny them remotely. To opt out, omit the key or set it to `false`. Before v2.1.234, Claude Code treated `false` as declared. See [Relay permission prompts](#relay-permission-prompts). |
| `capabilities.tools`                                     | `object`            | Two-way only. Always `{}`. Standard MCP tool capability. See [Expose a reply tool](#expose-a-reply-tool).                                                                                                                                                                                                                                                                            |
| `instructions`                                           | `string`            | Recommended. Claude Code delivers it to Claude as context when the server connects. Tell Claude what events to expect, what the `<channel>` tag attributes mean, whether to reply, and if so which tool to use and which attribute to pass back (like `chat_id`).                                                                                                                    |

To create a one-way channel, omit `capabilities.tools`. This example shows a two-way setup with the channel capability, tools, and instructions set:

```ts theme={null}

const mcp = new Server(
  { name: 'your-channel', version: '0.0.1' },
  {
    capabilities: {
      experimental: { 'claude/channel': {} },  // registers the channel listener
      tools: {},  // omit for one-way channels
    },
    // Claude Code delivers this to Claude as context when the server connects, so it knows how to handle your events
    instructions: 'Messages arrive as <channel source="your-channel" ...>. Reply with the reply tool.',
  },
)
```

## Notification format

Your server emits `notifications/claude/channel` with two params:

| Field     | Type                     | Description                                                                                                                                                                                                                                                           |
| :-------- | :----------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content` | `string`                 | The event body. Delivered as the body of the `<channel>` tag.                                                                                                                                                                                                         |
| `meta`    | `Record<string, string>` | Optional. Each entry becomes an attribute on the `<channel>` tag for routing context like chat ID, sender name, or alert severity. Keys must be identifiers: letters, digits, and underscores only. Keys containing hyphens or other characters are silently dropped. |

Your server pushes events by calling `mcp.notification()` on the `Server` instance. This example pushes a CI failure alert with two meta keys:

```ts theme={null}
await mcp.notification({
  method: 'notifications/claude/channel',
  params: {
    content: 'build failed on main: https://ci.example.com/run/1234',
    meta: { severity: 'high', run_id: '1234' },
  },
})
```

The event arrives in Claude's context wrapped in a `<channel>` tag. The `source` attribute is set automatically from your server's configured name:

```text theme={null}
<channel source="your-channel" severity="high" run_id="1234">
build failed on main: https://ci.example.com/run/1234
</channel>
```

Claude Code doesn't acknowledge notifications. The `await` on `mcp.notification()` resolves when the message is written to the transport, not when Claude has processed it. If the session hasn't loaded your server as a channel, or the organization policy blocks it, Claude Code drops the events silently and returns no error to your server.

If you need delivery confirmation, track event state in your server and expose a [reply tool](#expose-a-reply-tool) that Claude can call to report status back.

Events queue into the session and are processed in order. If several notifications arrive while Claude is busy, they're delivered together on the next turn and Claude handles them as a group. To process independent event streams concurrently, run separate sessions.

## Expose a reply tool

If your channel is two-way, like a chat bridge rather than an alert forwarder, expose a standard [MCP tool](https://modelcontextprotocol.io/docs/concepts/tools) that Claude can call to send messages back. Nothing about the tool registration is channel-specific. A reply tool has three components:

1. A `tools: {}` entry in your `Server` constructor capabilities so Claude Code discovers the tool
2. Tool handlers that define the tool's schema and implement the send logic
3. An `instructions` string in your `Server` constructor that tells Claude when and how to call the tool

To add these to the [webhook receiver above](#example-build-a-webhook-receiver):

    In your `Server` constructor in `webhook.ts`, add `tools: {}` to the capabilities so Claude Code knows your server offers tools:

    ```ts theme={null}
    capabilities: {
      experimental: { 'claude/channel': {} },
      tools: {},  // enables tool discovery
    },
    ```

    Add the following to `webhook.ts`. The `import` goes at the top of the file with your other imports; the two handlers go between the `Server` constructor and `mcp.connect()`. This registers a `reply` tool that Claude can call with a `chat_id` and `text`:

    ```ts theme={null}
    // Add this import at the top of webhook.ts

    // Claude queries this at startup to discover what tools your server offers
    mcp.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [{
        name: 'reply',
        description: 'Send a message back over this channel',
        // inputSchema tells Claude what arguments to pass
        inputSchema: {
          type: 'object',
          properties: {
            chat_id: { type: 'string', description: 'The conversation to reply in' },
            text: { type: 'string', description: 'The message to send' },
          },
          required: ['chat_id', 'text'],
        },
      }],
    }))

    // Claude calls this when it wants to invoke a tool
    mcp.setRequestHandler(CallToolRequestSchema, async req => {
      if (req.params.name === 'reply') {
        const { chat_id, text } = req.params.arguments as { chat_id: string; text: string }
        // send() is your outbound: POST to your chat platform, or for local
        // testing the SSE broadcast shown in the full example below.
        send(`Reply to ${chat_id}: ${text}`)
        return { content: [{ type: 'text', text: 'sent' }] }
      }
      throw new Error(`unknown tool: ${req.params.name}`)
    })
    ```

    Update the `instructions` string in your `Server` constructor so Claude knows to route replies back through the tool. This example tells Claude to pass `chat_id` from the inbound tag:

    ```ts theme={null}
    instructions: 'Messages arrive as <channel source="webhook" chat_id="...">. Reply with the reply tool, passing the chat_id from the tag.'
    ```

Here's the complete `webhook.ts` with two-way support. Outbound replies stream over `GET /events` using [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) (SSE), so `curl -N localhost:8788/events` can watch them live; inbound chat arrives on `POST /`:

```ts title="Full webhook.ts with reply tool" expandable theme={null}
#!/usr/bin/env bun

// --- Outbound: write to any curl -N listeners on /events --------------------
// A real bridge would POST to your chat platform instead.
const listeners = new Set<(chunk: string) => void>()
function send(text: string) {
  const chunk = text.split('\n').map(l => `data: ${l}\n`).join('') + '\n'
  for (const emit of listeners) emit(chunk)
}

const mcp = new Server(
  { name: 'webhook', version: '0.0.1' },
  {
    capabilities: {
      experimental: { 'claude/channel': {} },
      tools: {},
    },
    instructions: 'Messages arrive as <channel source="webhook" chat_id="...">. Reply with the reply tool, passing the chat_id from the tag.',
  },
)

mcp.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: 'reply',
    description: 'Send a message back over this channel',
    inputSchema: {
      type: 'object',
      properties: {
        chat_id: { type: 'string', description: 'The conversation to reply in' },
        text: { type: 'string', description: 'The message to send' },
      },
      required: ['chat_id', 'text'],
    },
  }],
}))

mcp.setRequestHandler(CallToolRequestSchema, async req => {
  if (req.params.name === 'reply') {
    const { chat_id, text } = req.params.arguments as { chat_id: string; text: string }
    send(`Reply to ${chat_id}: ${text}`)
    return { content: [{ type: 'text', text: 'sent' }] }
  }
  throw new Error(`unknown tool: ${req.params.name}`)
})

await mcp.connect(new StdioServerTransport())

let nextId = 1
Bun.serve({
  port: 8788,
  hostname: '127.0.0.1',
  idleTimeout: 0,  // don't close idle SSE streams
  async fetch(req) {
    const url = new URL(req.url)

    // GET /events: SSE stream so curl -N can watch Claude's replies live
    if (req.method === 'GET' && url.pathname === '/events') {
      const stream = new ReadableStream({
        start(ctrl) {
          ctrl.enqueue(': connected\n\n')  // so curl shows something immediately
          const emit = (chunk: string) => ctrl.enqueue(chunk)
          listeners.add(emit)
          req.signal.addEventListener('abort', () => listeners.delete(emit))
        },
      })
      return new Response(stream, {
        headers: { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' },
      })
    }

    // POST: forward to Claude as a channel event
    const body = await req.text()
    const chat_id = String(nextId++)
    await mcp.notification({
      method: 'notifications/claude/channel',
      params: {
        content: body,
        meta: { chat_id, path: url.pathname, method: req.method },
      },
    })
    return new Response('ok')
  },
})
```

The [fakechat server](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/fakechat) shows a more complete example with file attachments and message editing.

## Gate inbound messages

An ungated channel is a prompt injection vector. Anyone who can reach your endpoint can put text in front of Claude. A channel listening to a chat platform or a public endpoint needs a real sender check before it emits anything.

Check the sender against an allowlist before calling `mcp.notification()`. This example drops any message from a sender not in the set:

```ts theme={null}
const allowed = new Set(loadAllowlist())  // from your access.json or equivalent

// inside your message handler, before emitting:
if (!allowed.has(message.from.id)) {  // sender, not room
  return  // drop silently
}
await mcp.notification({ ... })
```

Gate on the sender's identity, not the chat or room identity: `message.from.id` in the example, not `message.chat.id`. In group chats, these differ, and gating on the room would let anyone in an allowlisted group inject messages into the session.

The [Telegram](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/telegram) and [Discord](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/discord) channels gate on a sender allowlist the same way. They bootstrap the list by [pairing](/docs/en/channels#security). See either implementation for the full pairing flow. The [iMessage](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/imessage) channel takes a different approach: it detects the user's own addresses from the Messages database at startup and lets them through automatically, with other senders added by handle.

## Relay permission prompts

When Claude calls a tool that needs approval, the local terminal dialog opens and the session waits. A two-way channel can opt in to receive the same prompt in parallel and relay it to you on another device. Both stay live: you can answer in the terminal or on your phone, and Claude Code applies whichever answer arrives first and closes the other.

Relay covers tool-use approvals like `Bash`, `Write`, and `Edit`. Project trust and MCP server consent dialogs don't relay; those only appear in the local terminal.

Claude Code v2.1.234 and later sends permission requests only to servers it registered as channels for the session, so relay sits behind the same [session opt-in and organization controls](/docs/en/channels#security) as message delivery. Relay also requires you to opt the server in with `--channels` or the development flag, and requires the server to declare the permission capability.

### How relay works

When a permission prompt opens, the relay loop has four steps:

1. Claude Code generates a short request ID and notifies your server
2. Your server forwards the prompt and ID to your chat app
3. The remote user replies with a yes or no and that ID
4. Your inbound handler parses the reply into a verdict, and Claude Code applies it only if the ID matches an open request

The local terminal dialog stays open through all of this. If someone at the terminal answers before the remote verdict arrives, that answer is applied instead and the pending remote request is dropped.

<img src="https://mintcdn.com/claude-code/9FG0ZKj9uKYiHmbi/images/channel-permission-relay.svg?fit=max&auto=format&n=9FG0ZKj9uKYiHmbi&q=85&s=97d57f128f0da55f105ab1e3a7e10240" className="dark:hidden" alt="Sequence diagram: Claude Code sends a permission_request notification to the channel server, the server formats and sends the prompt to the chat app, the human replies with a verdict, and the server parses that reply into a permission notification back to Claude Code" width="600" height="230" data-path="images/channel-permission-relay.svg" />

<img src="https://mintcdn.com/claude-code/_xqph1dUOslCOwsj/images/channel-permission-relay-dark.svg?fit=max&auto=format&n=_xqph1dUOslCOwsj&q=85&s=368c8d9119a9a9cff5d826d806724842" className="hidden dark:block" alt="Sequence diagram: Claude Code sends a permission_request notification to the channel server, the server formats and sends the prompt to the chat app, the human replies with a verdict, and the server parses that reply into a permission notification back to Claude Code" width="600" height="230" data-path="images/channel-permission-relay-dark.svg" />

### Permission request fields

The outbound notification from Claude Code is `notifications/claude/channel/permission_request`. Like the [channel notification](#notification-format), the transport is standard MCP but the method and schema are Claude Code extensions. The `params` object has four string fields your server formats into the outgoing prompt:

| Field           | Description                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_id`    | Five lowercase letters drawn from `a`-`z` without `l`, so it never reads as a `1` or `I` when typed on a phone. Include it in your outgoing prompt so it can be echoed in the reply. Claude Code only accepts a verdict that carries an ID it issued. The local terminal dialog doesn't display this ID, so your outbound handler is the only way to learn it. |
| `tool_name`     | Name of the tool Claude wants to use, for example `Bash` or `Write`.                                                                                                                                                                                                                                                                                           |
| `description`   | Human-readable summary of what this specific tool call does, never the command itself. For a Bash call this is Claude's description of the command; when the model gives no description, the field is the constant `Run shell command` and carries zero command detail. Render `input_preview` when you have room.                                             |
| `input_preview` | The tool's arguments as JSON-shaped display text, keyed per top-level field. For Bash this is the command; for Write, the file path and the content. Omit it from your prompt if you only have room for a one-line message. Your server decides what to show.                                                                                                  |

Clients on Claude Code v2.1.211 or later sanitize `description` and `input_preview` before relaying them. Expect three changes in the text you receive:

* Claude Code neutralizes direction-override characters, invisible characters, and quote and angle-bracket lookalikes.
* Claude Code folds each run of whitespace to a single space.
* Claude Code relays text whole up to 3,500 code points. For a longer value, you receive its start and its end around a counted `⋯ N code points elided ⋯` marker. The end of a long command still reaches the approver.

For `input_preview`, Claude Code applies the 3,500 limit to each top-level field of the arguments separately and keeps the JSON's own structural quotes. Clients before v2.1.211 relay `description` raw and cut `input_preview` to 200 UTF-16 units with a trailing ellipsis.

Clients on Claude Code v2.1.234 or later relay the marker `(value unserializable)` in place of an `input_preview` field value they can't serialize safely, such as a circular structure or an extremely large array. You still receive the field's key, and the preview's other fields are unchanged.

Clients on Claude Code v2.1.234 or later also mask credentials in `description` and `input_preview`. You receive `[REDACTED]` in place of a recognizable provider credential token, such as an API key or a personal access token. Expect three effects of the masking when you render the fields:

* Claude Code masks key names inside `input_preview` as well as their values. A key name you display may not match the key name in the input.
* Claude Code never masks a span that contains shell syntax, path characters, or URL characters. A mask can't hide the command, file path, or destination being approved.
* Claude Code doesn't mask a secret that lacks a recognizable prefix, or a secret that spans whitespace, such as a private-key block. Both reach your server unmasked.

Masking doesn't change who receives the fields. Whatever stays unmasked goes only to servers you opted in with `--channels` or the development flag. Treat both fields as untrusted unless you control the client fleet.

The verdict your server sends back is `notifications/claude/channel/permission` with two fields: `request_id` echoing the ID above, and `behavior` set to `'allow'` or `'deny'`. Allow lets the tool call proceed; deny rejects it. Neither verdict affects future calls.

### Add relay to a chat bridge

Adding permission relay to a two-way channel takes three components:

1. A `claude/channel/permission: {}` entry under `experimental` capabilities in your `Server` constructor so Claude Code knows to forward prompts
2. A notification handler for `notifications/claude/channel/permission_request` that formats the prompt and sends it out through your platform API
3. A check in your inbound message handler that recognizes `yes <id>` or `no <id>` and emits a `notifications/claude/channel/permission` verdict instead of forwarding the text to Claude

Only declare the capability if your channel [authenticates the sender](#gate-inbound-messages), because anyone who can reply through your channel can approve or deny tool use in your session.

To add these to a two-way chat bridge like the one assembled in [Expose a reply tool](#expose-a-reply-tool):

    In your `Server` constructor, add `claude/channel/permission: {}` alongside `claude/channel` under `experimental`:

    ```ts theme={null}
    capabilities: {
      experimental: {
        'claude/channel': {},
        'claude/channel/permission': {},  // opt in to permission relay
      },
      tools: {},
    },
    ```

    Register a notification handler between your `Server` constructor and `mcp.connect()`. Claude Code calls it with the [four request fields](#permission-request-fields) when a permission dialog opens. Your handler formats the prompt for your platform and includes instructions for replying with the ID:

    ```ts theme={null}

    // setNotificationHandler routes by z.literal on the method field,
    // so this schema is both the validator and the dispatch key
    const PermissionRequestSchema = z.object({
      method: z.literal('notifications/claude/channel/permission_request'),
      params: z.object({
        request_id: z.string(),     // five lowercase letters, include verbatim in your prompt
        tool_name: z.string(),      // e.g. "Bash", "Write"
        description: z.string(),    // summary of this call. Treat as untrusted.
        input_preview: z.string(),  // tool args as JSON-shaped text. Treat as untrusted.
      }),
    })

    mcp.setNotificationHandler(PermissionRequestSchema, async ({ params }) => {
      // send() is your outbound: POST to your chat platform, or for local
      // testing the SSE broadcast shown in the full example below.
      send(
        `Claude wants to run ${params.tool_name}: ${params.description}\n` +
        // input_preview carries the actual arguments; render it when you
        // have room: for Bash the description alone may be just
        // "Run shell command" with zero command detail
        `${params.input_preview}\n\n` +
        // the ID in the instruction is what your inbound handler parses in Step 3
        `Reply "yes ${params.request_id}" or "no ${params.request_id}"`,
      )
    })
    ```

    Your inbound handler is the loop or callback that receives messages from your platform: the same place you [gate on sender](#gate-inbound-messages) and emit `notifications/claude/channel` to forward chat to Claude. Add a check before the chat-forwarding call that recognizes the verdict format and emits the permission notification instead.

    The regex matches the ID format Claude Code generates: five letters, never `l`. The `/i` flag tolerates phone autocorrect capitalizing the reply; lowercase the captured ID before sending it back.

    ```ts theme={null}
    // matches "y abcde", "yes abcde", "n abcde", "no abcde"
    // [a-km-z] is the ID alphabet Claude Code uses (lowercase, skips 'l')
    // /i tolerates phone autocorrect; lowercase the capture before sending
    const PERMISSION_REPLY_RE = /^\s*(y|yes|n|no)\s+([a-km-z]{5})\s*$/i

    async function onInbound(message: PlatformMessage) {
      if (!allowed.has(message.from.id)) return  // gate on sender first

      const m = PERMISSION_REPLY_RE.exec(message.text)
      if (m) {
        // m[1] is the verdict word, m[2] is the request ID
        // emit the verdict notification back to Claude Code instead of chat
        await mcp.notification({
          method: 'notifications/claude/channel/permission',
          params: {
            request_id: m[2].toLowerCase(),  // normalize in case of autocorrect caps
            behavior: m[1].toLowerCase().startsWith('y') ? 'allow' : 'deny',
          },
        })
        return  // handled as verdict, don't also forward as chat
      }

      // didn't match verdict format: fall through to the normal chat path
      await mcp.notification({
        method: 'notifications/claude/channel',
        params: { content: message.text, meta: { chat_id: String(message.chat.id) } },
      })
    }
    ```

A remote reply that doesn't exactly match the expected format fails in one of two ways, and in both cases the local terminal dialog stays open:

* **Different format**: your inbound handler's regex fails to match, so text like `approve it` or `yes` without an ID falls through as a normal message to Claude.
* **Right format, wrong ID**: your server emits a verdict, but Claude Code finds no open request with that ID and drops it silently.

### Full example

The assembled `webhook.ts` below combines all three extensions from this page: the reply tool, sender gating, and permission relay. If you're starting here, you'll also need the [project setup and `.mcp.json` entry](#example-build-a-webhook-receiver) from the initial walkthrough.

To make both directions testable from curl, the HTTP listener serves two paths:

* **`GET /events`**: holds an SSE stream open and pushes each outbound message as a `data:` line, so `curl -N` can watch Claude's replies and permission prompts arrive live.
* **`POST /`**: the inbound side, the same handler as earlier, now with the verdict-format check inserted before the chat-forward branch.

```ts title="Full webhook.ts with permission relay" expandable theme={null}
#!/usr/bin/env bun

// --- Outbound: write to any curl -N listeners on /events --------------------
// A real bridge would POST to your chat platform instead.
const listeners = new Set<(chunk: string) => void>()
function send(text: string) {
  const chunk = text.split('\n').map(l => `data: ${l}\n`).join('') + '\n'
  for (const emit of listeners) emit(chunk)
}

// Sender allowlist. For the local walkthrough we trust the single X-Sender
// header value "dev"; a real bridge would check the platform's user ID.
const allowed = new Set(['dev'])

const mcp = new Server(
  { name: 'webhook', version: '0.0.1' },
  {
    capabilities: {
      experimental: {
        'claude/channel': {},
        'claude/channel/permission': {},  // opt in to permission relay
      },
      tools: {},
    },
    instructions:
      'Messages arrive as <channel source="webhook" chat_id="...">. ' +
      'Reply with the reply tool, passing the chat_id from the tag.',
  },
)

// --- reply tool: Claude calls this to send a message back -------------------
mcp.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: 'reply',
    description: 'Send a message back over this channel',
    inputSchema: {
      type: 'object',
      properties: {
        chat_id: { type: 'string', description: 'The conversation to reply in' },
        text: { type: 'string', description: 'The message to send' },
      },
      required: ['chat_id', 'text'],
    },
  }],
}))

mcp.setRequestHandler(CallToolRequestSchema, async req => {
  if (req.params.name === 'reply') {
    const { chat_id, text } = req.params.arguments as { chat_id: string; text: string }
    send(`Reply to ${chat_id}: ${text}`)
    return { content: [{ type: 'text', text: 'sent' }] }
  }
  throw new Error(`unknown tool: ${req.params.name}`)
})

// --- permission relay: Claude Code (not Claude) calls this when a dialog opens
const PermissionRequestSchema = z.object({
  method: z.literal('notifications/claude/channel/permission_request'),
  params: z.object({
    request_id: z.string(),
    tool_name: z.string(),
    description: z.string(),
    input_preview: z.string(),
  }),
})

mcp.setNotificationHandler(PermissionRequestSchema, async ({ params }) => {
  send(
    `Claude wants to run ${params.tool_name}: ${params.description}\n` +
    `${params.input_preview}\n\n` +
    `Reply "yes ${params.request_id}" or "no ${params.request_id}"`,
  )
})

await mcp.connect(new StdioServerTransport())

// --- HTTP on :8788: GET /events streams outbound, POST routes inbound -------
const PERMISSION_REPLY_RE = /^\s*(y|yes|n|no)\s+([a-km-z]{5})\s*$/i
let nextId = 1

Bun.serve({
  port: 8788,
  hostname: '127.0.0.1',
  idleTimeout: 0,  // don't close idle SSE streams
  async fetch(req) {
    const url = new URL(req.url)

    // GET /events: SSE stream so curl -N can watch replies and prompts live
    if (req.method === 'GET' && url.pathname === '/events') {
      const stream = new ReadableStream({
        start(ctrl) {
          ctrl.enqueue(': connected\n\n')  // so curl shows something immediately
          const emit = (chunk: string) => ctrl.enqueue(chunk)
          listeners.add(emit)
          req.signal.addEventListener('abort', () => listeners.delete(emit))
        },
      })
      return new Response(stream, {
        headers: { 'Content-Type': 'text/event-stream', 'Cache-Control': 'no-cache' },
      })
    }

    // everything else is inbound: gate on sender first
    const body = await req.text()
    const sender = req.headers.get('X-Sender') ?? ''
    if (!allowed.has(sender)) return new Response('forbidden', { status: 403 })

    // check for verdict format before treating as chat
    const m = PERMISSION_REPLY_RE.exec(body)
    if (m) {
      await mcp.notification({
        method: 'notifications/claude/channel/permission',
        params: {
          request_id: m[2].toLowerCase(),
          behavior: m[1].toLowerCase().startsWith('y') ? 'allow' : 'deny',
        },
      })
      return new Response('verdict recorded')
    }

    // normal chat: forward to Claude as a channel event
    const chat_id = String(nextId++)
    await mcp.notification({
      method: 'notifications/claude/channel',
      params: { content: body, meta: { chat_id, path: url.pathname } },
    })
    return new Response('ok')
  },
})
```

Test the verdict path in three terminals. The first is your Claude Code session, started with the [development flag](#test-during-the-research-preview) so it spawns `webhook.ts`:

```bash theme={null}
claude --dangerously-load-development-channels server:webhook
```

This walkthrough tests the permission dialog itself, so once the session is open, press `Shift+Tab` until the status bar shows `⏸ manual mode on`. In auto mode the classifier would decide the `reply` call instead of you, and no dialog would open for the remote side to answer.

In the second, stream the outbound side so you can see Claude's replies and any permission prompts as they fire:

```bash theme={null}
curl -N localhost:8788/events
```

In the third, send a message that will make Claude try to run a command:

```bash theme={null}
curl -d "list the files in this directory" -H "X-Sender: dev" localhost:8788
```

Listing files is read-only, so Claude runs it without approval. The permission dialog opens when Claude calls the `reply` tool to send its answer back. The local dialog opens in your Claude Code terminal, and a moment later the prompt for `mcp__webhook__reply` appears in the `/events` stream, including the five-letter ID. Approve it from the remote side:

```bash theme={null}
curl -d "yes <id>" -H "X-Sender: dev" localhost:8788
```

The local dialog closes, the `reply` tool runs, and Claude's reply appears in the stream.

The three channel-specific pieces in this file:

* **Capabilities** in the `Server` constructor: `claude/channel` registers the notification listener, `claude/channel/permission` opts in to permission relay, `tools` lets Claude discover the reply tool.
* **Outbound paths**: the `reply` tool handler is what Claude calls for conversational responses; the `PermissionRequestSchema` notification handler is what Claude Code calls when a permission dialog opens. Both call `send()` to broadcast over `/events`, but they're triggered by different parts of the system.
* **HTTP handler**: `GET /events` holds an SSE stream open so curl can watch outbound live; `POST` is inbound, gated on the `X-Sender` header. A `yes <id>` or `no <id>` body goes to Claude Code as a verdict notification and never reaches Claude; anything else is forwarded to Claude as a channel event.

## Package as a plugin

To make your channel installable and shareable, wrap it in a [plugin](/docs/en/plugins) and publish it to a [marketplace](/docs/en/plugin-marketplaces). Users install it with `/plugin install`, then enable it per session with `--channels plugin:<name>@<marketplace>`.

A channel published to your own marketplace still needs `--dangerously-load-development-channels` to run, since it isn't on the [approved allowlist](/docs/en/channels#supported-channels). The default allowlist is the channel plugins in `claude-plugins-official`, which Anthropic curates at its discretion. The [in-app submission forms](/docs/en/plugins#submit-your-plugin-to-the-community-marketplace) add plugins to the community marketplace, which is not on the channel allowlist.

If you are working with an Anthropic partner contact, reach out to them to coordinate an official-marketplace listing. On Team and Enterprise plans, an admin can instead include your plugin in the organization's own [`allowedChannelPlugins`](/docs/en/channels#restrict-which-channel-plugins-can-run) list, which replaces the default Anthropic allowlist.

## See also

* [Channels](/docs/en/channels) to install and use Telegram, Discord, iMessage, or the fakechat demo, and to enable channels for a Team or Enterprise org
* [Working channel implementations](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins) for complete server code with pairing flows, reply tools, and file attachments
* [MCP](/docs/en/mcp) for the underlying protocol that channel servers implement
* [Plugins](/docs/en/plugins) to package your channel so users can install it with `/plugin install`

---

## Checkpointing

- 官方原文：https://code.claude.com/docs/en/checkpointing.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-checkpointing.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Checkpointing

> Track, rewind, and summarize Claude's edits and conversation to manage session state.

Claude Code automatically tracks Claude's file edits as you work, allowing you to quickly undo changes and rewind to previous states if anything gets off track.

## How checkpoints work

As you work with Claude, checkpointing automatically captures the state of your code before each prompt you send that starts a turn.

### Automatic tracking

Claude Code tracks all changes made by its file editing tools:

* Every prompt you send that starts a turn creates a new checkpoint
* Claude Code keeps file snapshots for the 100 most recent checkpoints in a session. Discarding an older checkpoint deletes the snapshot files that no remaining checkpoint references, except each file's first snapshot, which the VS Code extension uses as the baseline for its session diffs.
* Claude Code saves checkpoints with the conversation, so you can still run `/rewind` after you resume a session
* Claude Code deletes a session's file snapshots in the [retention sweep](/docs/en/claude-directory#cleaned-up-automatically), by default about 30 days after the session last saved one. Rewinding to a checkpoint whose snapshots are gone can fail with [`No files were restored`](/docs/en/errors#no-files-were-restored). To keep snapshots longer, set [`cleanupPeriodDays`](/docs/en/settings-reference#cleanupperioddays).

### Rewind and summarize

Run `/rewind`, or press `Esc` twice when the prompt input is empty, to open the rewind menu.

<Note>
  If the prompt input contains text, double `Esc` clears it instead of opening the menu. The cleared text is saved to your input history, so press `Up` to recall it after you finish in the rewind menu.
</Note>

The rewind menu lists each prompt you sent during the session, except [messages that joined a running turn](#messages-sent-mid-turn-not-checkpointed). Select the point you want to act on, then choose an action:

* **Restore code and conversation**: revert both code and conversation to that point
* **Restore conversation**: rewind to that message while keeping current code
* **Restore code**: revert file changes while keeping the conversation
* **Summarize from here**: compress the conversation from this point forward into a summary, freeing context window space
* **Summarize up to here**: compress the conversation before this point into a summary, keeping later messages intact
* **Never mind**: return to the message list without making changes

The two code restore options appear only when the selected checkpoint has tracked file changes to revert. If no file edits were captured after that point, the menu offers only **Restore conversation**, the summarize options, and **Never mind**.

After restoring the conversation or choosing Summarize from here, the original prompt from the selected message is restored into the input field so you can re-send or edit it.

Choosing Summarize up to here leaves you at the end of the conversation with the input empty. With either summarize option, a **Summarized conversation** marker appears in the conversation where the compressed messages were.

#### Rewind past a cleared conversation

If you ran `/clear` earlier in the same Claude Code process, the rewind menu shows an additional entry at the top of the list labeled `/resume <session-id> (previous session)`. Select it to resume the conversation that was active before `/clear` ran. The entry is available until you exit Claude Code or resume a different session, and requires Claude Code v2.1.191 or later. On earlier versions, run `/resume` and pick the previous session from the list instead.

#### Guide a summary

Summarizing doesn't change files on disk, and the original messages stay in the session transcript, so Claude can still reference the details. To guide what the summary focuses on, highlight a **Summarize** option with the arrow keys and type instructions where the row reads **add context (optional)**, then press `Enter`. Selecting the option with its number key summarizes immediately without instructions.

<Note>
  Summarize keeps you in the same session and compresses context, like a targeted `/compact`. To branch off and try a different approach while preserving the original session intact, use [`/branch`](/docs/en/sessions#branch-a-session) or `claude --continue --fork-session` instead.
</Note>

## Common use cases

Checkpoints are particularly useful when:

* **Exploring alternatives**: try different implementation approaches without losing your starting point
* **Recovering from mistakes**: quickly undo changes that introduced bugs or broke functionality
* **Iterating on features**: experiment with variations knowing you can revert to working states
* **Freeing context space**: summarize a verbose debugging session from the midpoint forward, keeping your initial instructions intact

## Limitations

### Bash command changes not tracked

Checkpointing does not track files modified by Bash commands. For example, if Claude Code runs:

```bash theme={null}
rm file.txt
mv old.txt new.txt
cp source.txt dest.txt
```

These file modifications cannot be undone through rewind. Only direct file edits made through Claude's file editing tools are tracked.

### Subagent edits not restored

A [subagent](/docs/en/sub-agents) makes edits with Claude's file editing tools, but Claude Code usually doesn't capture those edits in your session's checkpoints. Whether rewinding restores them depends on how the subagent runs:

* **Foreground forked skill**: a [skill with `context: fork`](/docs/en/skills#run-skills-in-a-subagent) that runs in the foreground edits your working tree during your own turn, so rewinding restores its edits as usual. Set `background: false` to run a fork in the foreground; a few situations, [listed on the skills page](/docs/en/skills#run-skills-in-a-subagent), run it there regardless of the setting.
* **Any other subagent**: rewinding doesn't restore the edits. Use git to revert them. This includes a forked skill that runs in the background, the default, and a background [`/code-review --fix`](/docs/en/code-review) run.

### External changes not tracked

Checkpointing only tracks files that have been edited within the current session. Manual changes you make to files outside of Claude Code and edits from other concurrent sessions are normally not captured, unless they happen to modify the same files as the current session.

### Messages sent mid-turn not checkpointed

When a message you [queue while Claude works](/docs/en/interactive-mode#queue-messages-while-claude-works) reaches Claude within the running turn, it joins that turn instead of starting a new one. The message appears in the conversation, but Claude Code doesn't create a checkpoint for it, and the rewind menu doesn't list it. A queued message that Claude Code sends as its own turn gets a checkpoint as usual.

To remove such a message, or undo the edits Claude made after it, rewind to the prompt that started the turn. That rewinds the whole turn, including the work Claude did before your message arrived.

### Symlinked and hard-linked paths not restored

Checkpointing doesn't rewind symlinked or hard-linked files. When you pick **Restore code** or **Restore code and conversation** from the `/rewind` menu, Claude Code skips any tracked path that is a symlink or hard link and shows a `Restored the code, but skipped N files` warning. The skipped files keep their current contents. To undo the session's changes to one of them, ask Claude to reverse the edit or edit the file yourself. Config files a dotfile manager symlinks into your project and files pnpm hard-links into place both fall into this category.

To see which paths a restore skips, turn on debug logging with `/debug` before you restore: the debug log at `~/.claude/debug/<session-id>.txt` names each skipped path. For every skip reason and the recovery steps, see [the skipped-files entry in the error reference](/docs/en/errors#restored-the-code-but-skipped-files).

### Not a replacement for version control

Checkpoints are designed for quick, session-level recovery. For permanent version history and collaboration, continue using version control, such as Git, for commits, branches, and long-term history.

## See also

* [Interactive mode](/docs/en/interactive-mode) - Keyboard shortcuts and session controls
* [Commands](/docs/en/commands) - Accessing checkpoints using `/rewind`
* [CLI reference](/docs/en/cli-reference) - Command-line options

---

## CLI reference

- 官方原文：https://code.claude.com/docs/en/cli-reference.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-cli-reference.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI reference

> Complete reference for Claude Code command-line interface, including commands and flags.

## CLI commands

You can start sessions, pipe content, resume conversations, and manage updates with these commands:

| Command                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Example                                                     |
| :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `claude`                        | Start interactive session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude`                                                    |
| `claude "query"`                | Start interactive session with initial prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `claude "explain this project"`                             |
| `claude -p "query"`             | Query via SDK, then exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `claude -p "explain this function"`                         |
| `cat file \| claude -p "query"` | Process piped content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `cat logs.txt \| claude -p "explain"`                       |
| `claude -c`                     | Continue most recent conversation in current directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `claude -c`                                                 |
| `claude -c -p "query"`          | Continue via SDK                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude -c -p "Check for type errors"`                      |
| `claude -r "<session>" "query"` | Resume session by ID or name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude -r "auth-refactor" "Finish this PR"`                |
| `claude update`                 | Update to latest version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `claude update`                                             |
| `claude gateway`                | Start the self-hosted [Claude apps gateway](/docs/en/claude-apps-gateway) server, for administrators deploying SSO and policy in front of Claude Code on Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry. Requires `--config` pointing at a [`gateway.yaml`](/docs/en/claude-apps-gateway-config). Available in Claude Code v2.1.195 and later.                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude gateway --config gateway.yaml`                      |
| `claude install [version]`      | Install or reinstall the native binary. Accepts a version like `2.1.118`, or `stable` or `latest`. See [Install a specific version](/docs/en/setup#install-a-specific-version)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude install stable`                                     |
| `claude auth login`             | Sign in to your Anthropic account. Use `--email` to pre-fill your email address, `--sso` to force SSO authentication, and `--console` to sign in with Anthropic Console for API usage billing instead of a Claude subscription                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude auth login --console`                               |
| `claude auth logout`            | Log out from your Anthropic account                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `claude auth logout`                                        |
| `claude auth status`            | Show authentication status as JSON. Use `--text` for human-readable output. Exits with code 0 if logged in, 1 if not                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `claude auth status`                                        |
| `claude agents`                 | Open [agent view](/docs/en/agent-view) to monitor and dispatch parallel background sessions. Use `--cwd <path>` to show only sessions started under that directory, or `--json` to print active sessions as a JSON array for scripting (`--json --all` also includes completed background sessions). Pass `--permission-mode`, `--model`, `--effort`, or `--agent` to set [defaults for dispatched sessions](/docs/en/agent-view#permission-mode-model-and-effort). Accepts `--settings`, `--add-dir`, `--plugin-dir`, and `--mcp-config` like the top-level `claude` command. Opening agent view requires an interactive terminal                                                                                                                                                    | `claude agents --json`                                      |
| `claude attach <id>`            | Attach to a [background session](/docs/en/agent-view#manage-sessions-from-the-shell) in this terminal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude attach 7c5dcf5d`                                    |
| `claude auto-mode defaults`     | Print the built-in [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) classifier rules as JSON. Use `claude auto-mode config` to see your effective config with settings applied. `--label <prefix>` prints only the rules whose label starts with that prefix, matched case-insensitively. Requires Claude Code v2.1.208 or later                                                                                                                                                                                                                                                                                                                                                                                                                          | `claude auto-mode defaults --label 'Git Destructive'`       |
| `claude auto-mode reset`        | Restore the default [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) configuration by removing the `autoMode` section from your user settings file. Prompts for confirmation before writing; pass `-y`/`--yes` to skip the prompt. Rules from [managed settings](/docs/en/server-managed-settings) or the `--settings` flag still apply. Requires Claude Code v2.1.212 or later. See [Inspect the defaults and your effective config](/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config)                                                                                                                                                                                                                                                     | `claude auto-mode reset --yes`                              |
| `claude daemon status`          | Print the background-session [supervisor's](/docs/en/agent-view#the-supervisor-process) state, version, socket directory, and worker count for diagnostics. Exits 1 if the supervisor isn't running                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude daemon status`                                      |
| `claude daemon stop --any`      | Stop the background-session [supervisor](/docs/en/agent-view#the-supervisor-process) and the sessions it hosts. Pass `--keep-workers` to leave background sessions running so the next supervisor reconnects to them. `--any` confirms stopping an on-demand supervisor, which is the default. Use this to recover from an [unresponsive supervisor](/docs/en/agent-view#agent-view-says-the-background-service-did-not-respond)                                                                                                                                                                                                                                                                                                                                                      | `claude daemon stop --any --keep-workers`                   |
| `claude doctor`                 | Print read-only installation and settings diagnostics from the terminal without starting a session, including install health, settings-file validation errors, and Remote Control eligibility. For the in-session setup checkup that can also apply fixes, run [`/doctor`](/docs/en/commands#all-commands)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `claude doctor`                                             |
| `claude import [source]`        | Start an interactive session that runs [`/import`](/docs/en/commands#all-commands) to bring configuration from other coding agents into Claude Code. Accepts the same `--dry-run` and `--yes` options as the command. Not available on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or Claude Platform on AWS. Also unavailable when you turn off [feature-flag fetching](/docs/en/env-vars#features-that-need-feature-flag-fetching). Requires Claude Code v2.1.213 or later                                                                                                                                                                                                                                                                                    | `claude import codex --dry-run`                             |
| `claude logs <id>`              | Print recent output from a [background session](/docs/en/agent-view#manage-sessions-from-the-shell)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude logs 7c5dcf5d`                                      |
| `claude mcp`                    | Configure Model Context Protocol (MCP) servers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | See the [Claude Code MCP documentation](/docs/en/mcp).           |
| `claude mcp login <name>`       | Run a configured MCP server's OAuth flow without opening the interactive `/mcp` panel. Works for HTTP, SSE, and claude.ai connector servers. Add `--no-browser` over SSH to print the authorization URL instead of opening a browser, then paste the redirect URL back at the prompt. Requires Claude Code v2.1.186 or later. See [Authenticate from the command line](/docs/en/mcp#authenticate-from-the-command-line)                                                                                                                                                                                                                                                                                                                                                          | `claude mcp login sentry`                                   |
| `claude mcp logout <name>`      | Clear stored OAuth credentials for an MCP server. Requires Claude Code v2.1.186 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `claude mcp logout sentry`                                  |
| `claude plugin`                 | Manage Claude Code [plugins](/docs/en/plugins). Alias: `claude plugins`. See [plugin reference](/docs/en/plugins-reference#cli-commands-reference) for subcommands                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `claude plugin install code-review@claude-plugins-official` |
| `claude project purge [path]`   | Delete all local Claude Code state for a project: transcripts, task lists, debug logs, file-edit history, prompt history lines, and the project's entry in `~/.claude.json`. Omit `[path]` to pick from an interactive list. Flags: `--dry-run` to preview, `-y`/`--yes` to skip confirmation, `-i`/`--interactive` to confirm each item, `--all` for every project. See [Clear local data](/docs/en/claude-directory#clear-local-data)                                                                                                                                                                                                                                                                                                                                          | `claude project purge ~/work/repo --dry-run`                |
| `claude remote-control`         | Start a [Remote Control](/docs/en/remote-control) server to control Claude Code from Claude.ai or the Claude app. Runs in server mode (no local interactive session). See [Server mode flags](/docs/en/remote-control#start-a-remote-control-session). After you stop the server, you can bring back the sessions it was serving. See [Resume sessions after stopping the server](/docs/en/remote-control#resume-sessions-after-stopping-the-server)                                                                                                                                                                                                                                                                                                                                       | `claude remote-control --name "My Project"`                 |
| `claude respawn <id>`           | Restart a [background session](/docs/en/agent-view#manage-sessions-from-the-shell), running or stopped, with its conversation intact. Use `--all` to restart every running session, e.g. to pick up an updated Claude Code binary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude respawn 7c5dcf5d`                                   |
| `claude rm <id>`                | Remove a [background session](/docs/en/agent-view#manage-sessions-from-the-shell) from the list. When the removal is [refused over the session's worktree](/docs/en/agent-view#what-deleting-a-session-removes) and a second `claude rm` can resolve it, the refusal prints the exact flag and value to pass: `--discard-unpushed <commit>@<worktree-id>` discards a worktree that has unpushed commits along with those commits, and `--force-remove-worktree <worktree-id>` deletes a worktree directory that git or the `WorktreeRemove` hook couldn't remove. `--discard-unpushed` requires Claude Code v2.1.260 or later, and `--force-remove-worktree` requires v2.1.268 or later. The conversation transcript stays on your local machine, available through `claude --resume` | `claude rm 7c5dcf5d`                                        |
| `claude self-hosted-runner`     | Start a runner process that registers this machine or container with a [self-hosted environment](/docs/en/self-hosted-environments) and hosts Claude Code cloud sessions on your infrastructure. Run `claude self-hosted-runner setup` for a guided operator walkthrough, `claude self-hosted-runner doctor` to [diagnose a deployed runner](/docs/en/self-hosted-environments-deploy#troubleshooting), and `claude self-hosted-runner orchestrator` to spawn [on-demand runners](/docs/en/self-hosted-environments-configuration#on-demand-runners). Requires Claude Code v2.1.224 or later                                                                                                                                                                                               | `claude self-hosted-runner setup`                           |
| `claude setup-token`            | Generate a long-lived OAuth token for CI and scripts. Prints the token to the terminal without saving it. Requires a Claude subscription. See [Generate a long-lived token](/docs/en/authentication#generate-a-long-lived-token)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `claude setup-token`                                        |
| `claude stop <id>`              | Stop a [background session](/docs/en/agent-view#manage-sessions-from-the-shell). Also accepts `claude kill`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `claude stop 7c5dcf5d`                                      |
| `claude ultrareview [target]`   | Run [ultrareview](/docs/en/ultrareview#run-ultrareview-non-interactively) non-interactively. Prints findings to stdout and exits 0 on success or 1 on failure. Use `--json` for the raw payload and `--timeout <minutes>` to override the 45-minute default. Use `--post` on a `github.com` pull request target to post the finished findings to the PR as one plain comment from your GitHub account. `--no-post` is the default. `--post` and `--no-post` require Claude Code v2.1.227 or later. See [Post findings to the pull request](/docs/en/ultrareview#post-findings-to-the-pull-request)                                                                                                                                                                                    | `claude ultrareview 1234 --json`                            |

If you mistype a subcommand, Claude Code suggests the closest match and exits without starting a session. For example, `claude udpate` prints `Did you mean claude update?`.

As of v2.1.199, `claude --dangerously-skip-permissions daemon <subcommand>` runs the `daemon` subcommand. Earlier versions treated `daemon <subcommand>` as the prompt for a new interactive session, so the subcommand never ran when the flag came first, a common setup when `claude` is aliased to include the flag. Only a leading `--dangerously-skip-permissions` or `--allow-dangerously-skip-permissions` routes to `daemon` this way; any other leading flag still starts an interactive session.

## CLI flags

Customize Claude Code's behavior with these command-line flags. `claude --help` does not list every flag, so a flag's absence from `--help` does not mean it is unavailable.

| Flag                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                             |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------- |
| `--add-dir`                                     | Add additional working directories for Claude to read and edit files. Grants file access; Claude Code [doesn't discover](/docs/en/permissions#additional-directories-grant-file-access-not-configuration) most `.claude/` configuration from these directories. Validates that each path exists as a directory. You can't add most [network paths](/docs/en/errors#working-directory-is-a-network-path), such as `\\server\share`. To persist these directories across sessions, set [`permissions.additionalDirectories`](/docs/en/settings-reference#permissions-additionaldirectories) in settings                                                                                                                                                                                                                                                                                                                                                                        | `claude --add-dir ../apps ../lib`                                                                   |
| `--advisor <model>`                             | Enable the server-side [advisor tool](/docs/en/advisor) for this session with a model alias, `fable`, `opus`, or `sonnet`, or a full model ID. Takes precedence over the `advisorModel` setting for the session. `fable` requires [Fable access](/docs/en/advisor#choose-an-advisor-model)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude --advisor opus`                                                                             |
| `--agent`                                       | Specify an agent for the current session (overrides the `agent` setting)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `claude --agent my-custom-agent`                                                                    |
| `--agents`                                      | Define custom subagents dynamically via JSON. Accepts the [fields listed for CLI-defined subagents](/docs/en/sub-agents#choose-the-subagent-scope). Claude Code validates the JSON at startup and exits on an invalid value; see [`Invalid --agents configuration`](/docs/en/errors#invalid-agents-configuration) for the message and for the flags and environment variable that skip the validation. Validation requires Claude Code v2.1.242 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude --agents '{"reviewer":{"description":"Reviews code","prompt":"You are a code reviewer"}}'`  |
| `--allow-dangerously-skip-permissions`          | Add `bypassPermissions` to the `Shift+Tab` mode cycle without starting in it. Lets you begin in a different mode like `plan` and switch to `bypassPermissions` later. See [permission modes](/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude --permission-mode plan --allow-dangerously-skip-permissions`                                |
| `--allowedTools`, `--allowed-tools`             | Tools that execute without prompting for permission. See [permission rule syntax](/docs/en/settings-reference#permission-rule-syntax) for pattern matching. To restrict which tools are available, use `--tools` instead. If you name one of the [task-tracking tools](/docs/en/tools-reference#task-tool-availability) here, Claude Code also opts the session in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `"Bash(git log *)" "Bash(git diff *)" "Read"`                                                       |
| `--append-subagent-system-prompt`               | Append custom text to the end of every [subagent](/docs/en/sub-agents)'s system prompt, nested subagents included, apart from a [forked subagent](/docs/en/sub-agents#fork-the-current-conversation), which reuses the conversation's own prompt. Only applies in non-interactive mode with `-p`. Requires Claude Code v2.1.205 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude -p --append-subagent-system-prompt "Cite file paths in every answer" "query"`               |
| `--append-subagent-system-prompt-file`          | Load text from a file and append it to [subagent](/docs/en/sub-agents) system prompts. An alternative to `--append-subagent-system-prompt` for text too long to pass on the command line. The two flags can't be combined. Only applies in non-interactive mode with `-p`. Requires Claude Code v2.1.261 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude -p --append-subagent-system-prompt-file ./subagent-rules.txt "query"`                       |
| `--append-system-prompt`                        | Append custom text to the end of the default system prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `claude --append-system-prompt "Always use TypeScript"`                                             |
| `--append-system-prompt-file`                   | Load additional system prompt text from a file and append to the default prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `claude --append-system-prompt-file ./extra-rules.txt`                                              |
| `--autocompact <auto\|tokens>`                  | Set the [auto-compact window](/docs/en/model-config#set-the-auto-compact-window) for this session without changing your saved settings. Accepts the same values as `/autocompact`; that section covers the value forms and what overrides the flag. Requires Claude Code v2.1.221 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `claude --autocompact 500k`                                                                         |
| `--ax-screen-reader`                            | Render screen-reader friendly output: flat text without decorative borders or animations. Forces the classic renderer, so the [`tui`](/docs/en/settings-reference#tui) setting has no effect; attached [background sessions](/docs/en/agent-view) still render fullscreen. Takes precedence over [`CLAUDE_AX_SCREEN_READER`](/docs/en/env-vars) and the [`axScreenReader`](/docs/en/settings-reference#axscreenreader) setting. Requires Claude Code v2.1.181 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude --ax-screen-reader`                                                                         |
| `--bare`                                        | Minimal mode: skip auto-discovery of hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory, and CLAUDE.md so scripted calls start faster. Skills in a directory you pass with `--add-dir` still load. Claude has access to Bash, file read, and file edit tools. Sets [`CLAUDE_CODE_SIMPLE`](/docs/en/env-vars). See [bare mode](/docs/en/headless#start-faster-with-bare-mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --bare -p "query"`                                                                          |
| `--betas`                                       | Beta headers to include in API requests (API key users only)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --betas interleaved-thinking`                                                               |
| `--bg`, `--background`                          | Start the session as a [background agent](/docs/en/agent-view) and return immediately. Prints the session ID and management commands. Combine with `--exec` to run a shell command as a background job instead of a Claude session, or with `--agent` to run a specific subagent. Can't be combined with `-p`/`--print`; see the [error reference](/docs/en/errors#command-line-errors)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `claude --bg "investigate the flaky test"`                                                          |
| `--channels`                                    | (Research preview) MCP servers whose [channel](/docs/en/channels) notifications Claude should listen for in this session. Space-separated list of `plugin:<name>@<marketplace>` entries. Requires Anthropic authentication through claude.ai or a Console API key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --channels plugin:my-notifier@my-marketplace`                                               |
| `--chrome`                                      | Enable [Chrome browser integration](/docs/en/chrome) for web automation and testing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude --chrome`                                                                                   |
| `--cloud`                                       | With a task description, create a new [cloud session](/docs/en/claude-code-on-the-web). With a session ID (`session_...` or `cse_...`) or a claude.ai/code URL, queue a message into that existing session instead, with `-p`. See [send a follow-up message](/docs/en/claude-code-on-the-web#send-follow-ups-from-the-cli).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude --cloud "Fix the login bug"`                                                                |
| `--continue`, `-c`                              | Load the most recent conversation in the current directory, including a [background session that has finished](/docs/en/sessions#resume-a-session); opening finished background sessions requires Claude Code v2.1.257 or later. Skips sessions created with `claude -p` or the Agent SDK, and sessions whose first prompt was `/loop`. `claude -p --continue` includes `-p`, SDK, and `/loop` sessions. Includes sessions that added this directory with `/add-dir`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `claude --continue`                                                                                 |
| `--dangerously-load-development-channels`       | Enable [channels](/docs/en/channels-reference#test-during-the-research-preview) that are not on the approved allowlist, for local development. Accepts `plugin:<name>@<marketplace>` and `server:<name>` entries. Prompts for confirmation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `claude --dangerously-load-development-channels server:webhook`                                     |
| `--dangerously-skip-permissions`                | Skip permission prompts. Equivalent to `--permission-mode bypassPermissions`. See [permission modes](/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode) for what this does and does not skip. For sessions started with `--bg`, the mode [persists when the supervisor restarts the session](/docs/en/agent-view#permission-mode-model-and-effort)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --dangerously-skip-permissions`                                                             |
| `--debug`                                       | Enable debug mode with optional category filtering, such as `--debug='mcp,startup'` or `--debug='!1p'`. The filter binds only in the `=` form; a space-separated filter enables debug mode without filtering                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --debug='mcp,startup'`                                                                      |
| `--debug-file <path>`                           | Write debug logs to a specific file path. Implicitly enables debug mode. Takes precedence over `CLAUDE_CODE_DEBUG_LOGS_DIR`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude --debug-file /tmp/claude-debug.log`                                                         |
| `--disable-slash-commands`                      | Disable all skills and commands for this session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude --disable-slash-commands`                                                                   |
| `--disallowedTools`, `--disallowed-tools`       | Deny rules. A bare tool name removes the matching tools from Claude's context: `"Edit"` removes Edit, `"*"` removes every tool, and `"mcp__*"` removes every MCP tool. A scoped rule such as `Bash(rm *)` leaves the tool available and denies only calls that match [as written](/docs/en/permissions#bash-rule-limits). A rule naming [`EndConversation`](/docs/en/tools-reference#endconversation-tool-behavior) can't remove it while any other tool remains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `"Bash(git log *)" "Bash(git diff *)" "Edit"`                                                       |
| `--effort`                                      | Set the [effort level](/docs/en/model-config#adjust-effort-level) for the current session. Options: `low`, `medium`, `high`, `xhigh`, `max`, or `ultracode`. Available levels depend on the model. `ultracode` requests `xhigh` effort with [ultracode](/docs/en/workflows#let-claude-decide-with-ultracode) turned on, and requires Claude Code v2.1.203 or later. Overrides the [`modelSettings`](/docs/en/settings-reference#modelsettings) and [`effortLevel`](/docs/en/settings-reference#effortlevel) settings for this session and does not persist                                                                                                                                                                                                                                                                                                                                                                                                                        | `claude --effort high`                                                                              |
| `--enable-auto-mode`                            | Removed in v2.1.111. Auto mode is now in the `Shift+Tab` cycle by default; use `--permission-mode auto` to start in it                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `claude --permission-mode auto`                                                                     |
| `--environment <environment-id>`                | Create a new cloud session that runs on the [self-hosted environment](/docs/en/self-hosted-environments) with the given ID. Environment IDs start with `ccpool_`. See [`--environment` dispatch behavior](/docs/en/self-hosted-environments-testing#environment-dispatch-behavior) for dispatch behavior and the flag combinations it rejects. Requires Claude Code v2.1.224 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude -p "Fix the login bug" --environment ccpool_abc123`                                         |
| `--exclude-dynamic-system-prompt-sections`      | Move per-machine sections from the system prompt (working directory, environment info, memory paths, git-repo flag) into the first user message. Improves prompt-cache reuse across different users and machines running the same task. Only applies with the default system prompt; ignored when `--system-prompt` or `--system-prompt-file` is set. Use with `-p` for scripted, multi-user workloads                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `claude -p --exclude-dynamic-system-prompt-sections "query"`                                        |
| `--exec`                                        | Run a shell command as a PTY-backed background job instead of starting a Claude session. Use with `--bg` to launch from the shell                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `claude --bg --exec 'pytest -x'`                                                                    |
| `--fallback-model`                              | Enable automatic fallback to the specified model(s) when the primary model is overloaded or not available, for example a retired model. Accepts a comma-separated list tried in order. See [Fallback model chains](/docs/en/model-config#fallback-model-chains). To persist a chain across sessions, use the [`fallbackModel` setting](/docs/en/settings-reference#fallbackmodel), which this flag overrides                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude --fallback-model sonnet,haiku`                                                              |
| `--fork-session`                                | When resuming, create a new session ID instead of reusing the original (use with `--resume` or `--continue`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --resume abc123 --fork-session`                                                             |
| `--forward-subagent-text`                       | Emit [subagent](/docs/en/sub-agents) text and thinking blocks in the output stream as `assistant` and `user` messages with `parent_tool_use_id` set, so you can reconstruct each subagent's transcript. Without this flag, Claude Code omits the text and thinking blocks of a subagent that runs in the [foreground](/docs/en/sub-agents#run-subagents-in-foreground-or-background). Requires `--print` and `--output-format stream-json`. Claude Code also forwards messages from [nested subagents](/docs/en/sub-agents#let-subagents-spawn-their-own-subagents), setting `parent_tool_use_id` to the ID of the Agent or Skill tool call that started each one; this requires Claude Code v2.1.219 or later, and messages of subagents that a forked skill spawns, and of nested forked skills, require v2.1.275 or later. The [`CLAUDE_CODE_FORWARD_SUBAGENT_TEXT`](/docs/en/env-vars) environment variable enables the same behavior. Requires Claude Code v2.1.211 or later | `claude -p --output-format stream-json --verbose --forward-subagent-text "query"`                   |
| `--from-pr`                                     | Open the session picker filtered to sessions linked to a specific pull request. Accepts a PR number, a GitHub or GitHub Enterprise PR URL, a GitLab merge request URL, or a Bitbucket pull request URL. Sessions are linked automatically when Claude creates the pull request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude --from-pr 123`                                                                              |
| `--ide`                                         | Automatically connect to IDE on startup if exactly one valid IDE is available                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `claude --ide`                                                                                      |
| `--init`                                        | Run [Setup hooks](/docs/en/hooks#setup) with the `init` matcher before the session (print mode only)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `claude -p --init "query"`                                                                          |
| `--init-only`                                   | Run [Setup](/docs/en/hooks#setup) and `SessionStart` hooks, then exit without starting a conversation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude --init-only`                                                                                |
| `--include-hook-events`                         | Include hook lifecycle events in the output stream. `SessionStart` and `Setup` hook events are always included and don't need this flag. Some hook events, such as `Notification`, `SessionEnd`, `PreCompact`, and `PostCompact`, never produce a `hook_started` event, even with this flag. For those events, Claude Code still emits `hook_progress` while a command hook that runs for more than a second produces output, and emits `hook_response` only when a [hook that runs in the background](/docs/en/hooks#run-hooks-in-the-background) finishes. Requires `--output-format stream-json`                                                                                                                                                                                                                                                                                                                                                                | `claude -p --output-format stream-json --verbose --include-hook-events "query"`                     |
| `--include-partial-messages`                    | Include partial streaming events in output. Requires `--print` and `--output-format stream-json`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude -p --output-format stream-json --verbose --include-partial-messages "query"`                |
| `--input-format`                                | Specify input format for print mode (options: `text`, `stream-json`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `claude -p --output-format json --input-format stream-json`                                         |
| `--json-schema`                                 | Get validated JSON output matching a JSON Schema after the agent completes its workflow (print mode only). See [structured outputs](/docs/en/agent-sdk/structured-outputs). Claude Code exits with an error on an invalid schema and accepts the `format` keyword as an annotation without client-side validation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude -p --json-schema '{"type":"object","properties":{...}}' "query"`                            |
| `--maintenance`                                 | Run [Setup hooks](/docs/en/hooks#setup) with the `maintenance` matcher before the session (print mode only)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `claude -p --maintenance "query"`                                                                   |
| `--max-budget-usd`                              | Maximum dollar amount to spend on API calls before stopping (print mode only). Spend from [subagents](/docs/en/sub-agents) counts toward the cap. When you return to a conversation with `--continue` or `--resume`, totals [restored from earlier runs](/docs/en/agent-sdk/cost-tracking#accumulate-costs-across-multiple-calls) don't count toward it. Once spend reaches the cap, spawning another subagent fails with `Budget limit reached`, and Claude Code stops background subagents that are still running; the cap-enforcement behaviors require Claude Code v2.1.217 or later                                                                                                                                                                                                                                                                                                                                                                                | `claude -p --max-budget-usd 5.00 "query"`                                                           |
| `--max-turns`                                   | Limit the number of agentic turns (print mode only). Exits with an error when the limit is reached. No limit by default. With `--input-format stream-json`, a message still queued when the limit ends a turn stays queued and starts a new turn with its own limit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `claude -p --max-turns 3 "query"`                                                                   |
| `--mcp-config`                                  | Load MCP servers from JSON files or strings (space-separated). When you pass this flag with `-p`, Claude Code waits for still-pending servers to connect before running the first turn, up to the [`MCP_TIMEOUT`](/docs/en/env-vars) startup timeout, 30 seconds by default; a server with a [cached tool list](/docs/en/mcp#managing-your-servers) skips the wait and connects on first use. The wait requires Claude Code v2.1.221 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `claude --mcp-config ./mcp.json`                                                                    |
| `--model`                                       | Sets the model for the current session with a [model alias](/docs/en/model-config#model-aliases) such as `sonnet`, `opus`, `haiku`, or `fable`, or a model's full name. Overrides the [`model`](/docs/en/settings-reference#model) setting and [`ANTHROPIC_MODEL`](/docs/en/model-config#environment-variables)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `claude --model claude-sonnet-5`                                                                    |
| `--name`, `-n`                                  | Set a display name for the session, shown in `/resume` and the terminal title. You can resume a named session with `claude --resume <name>`. In an interactive session, if another live session on this machine already uses the name, Claude Code applies [a variant of it](/docs/en/sessions#name-your-sessions) instead. <br /><br />[`/rename`](/docs/en/commands) changes the name mid-session and also shows it on the prompt bar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `claude -n "my-feature-work"`                                                                       |
| `--no-chrome`                                   | Disable [Chrome browser integration](/docs/en/chrome) for this session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `claude --no-chrome`                                                                                |
| `--no-session-persistence`                      | Disable session persistence so sessions are not saved to disk and cannot be resumed. Print mode only. The [`CLAUDE_CODE_SKIP_PROMPT_HISTORY`](/docs/en/env-vars) environment variable does the same in any mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `claude -p --no-session-persistence "query"`                                                        |
| `--output-format`                               | Specify output format for print mode (options: `text`, `json`, `stream-json`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `claude -p "query" --output-format json`                                                            |
| `--permission-mode`                             | Begin in a specified [permission mode](/docs/en/permission-modes). Accepts `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`, or `manual` as an alias for `default`. The `manual` alias selects the permission mode the UI labels Manual and requires Claude Code v2.1.200 or later; `claude --help` lists it in place of `default`, and both values work. Overrides `defaultMode` from settings files. Without this flag or `--dangerously-skip-permissions`, a new session starts in the permission mode described in [which permission mode a session starts in](/docs/en/permission-modes#which-mode-a-session-starts-in). For `-p`, that's `default` when nothing is configured                                                                                                                                                                                                                                                             | `claude --permission-mode plan`                                                                     |
| `--permission-prompt-tool`                      | Specify an MCP tool to handle permission prompts in non-interactive mode. Claude Code waits for that tool's MCP server to connect before running the first turn, up to the [`MCP_TIMEOUT`](/docs/en/env-vars) startup timeout, 30 seconds by default. <br /><br />The prompt tool can't approve an MCP tool marked as [requiring user interaction](/docs/en/mcp#require-approval-for-a-specific-tool): Claude Code converts an `allow` result for one to a deny. This restriction requires Claude Code v2.1.199 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude -p --permission-prompt-tool mcp_auth_tool "query"`                                          |
| `--permission-prompts`                          | Set who answers permission prompts in print mode. With the default `host`, Claude Code sends them to the Agent SDK host or the `--permission-prompt-tool` tool. Pass `none` when nobody can answer, and Claude Code denies them instead. See [Turn off permission prompts in unattended runs](/docs/en/headless#turn-off-permission-prompts-in-unattended-runs). Requires Claude Code v2.1.259 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude -p --permission-prompts none "query"`                                                       |
| `--plugin-dir`                                  | Load a plugin from a directory or `.zip` archive, or several from a [folder of plugins](/docs/en/plugins#test-your-plugins-locally), for this session only. Each flag takes one path. Repeat the flag for more paths: `--plugin-dir A --plugin-dir B.zip`. Passing a folder of plugins requires Claude Code v2.1.265 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `claude --plugin-dir ./my-plugin`                                                                   |
| `--plugin-url`                                  | Fetch a plugin `.zip` archive from a URL for this session only. Repeat the flag for multiple plugins, or pass space-separated URLs in a single quoted value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude --plugin-url https://example.com/plugin.zip`                                                |
| `--print`, `-p`                                 | Print response without interactive mode (see [Agent SDK documentation](/docs/en/agent-sdk/overview) for programmatic usage details)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude -p "query"`                                                                                 |
| `--prompt-suggestions`                          | Emit a `prompt_suggestion` message with a predicted next user prompt after each turn that generates one; very short conversations can produce none. Requires `--print`, `--output-format stream-json`, and `--verbose`. See [Prompt suggestions](/docs/en/interactive-mode#prompt-suggestions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `claude -p --prompt-suggestions --output-format stream-json --verbose "query"`                      |
| `--ref <branch>`                                | With `--environment`, base the new session's checkout on a named ref instead of local `HEAD`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude -p "Run the smoke test" --environment ccpool_abc123 --ref main`                             |
| `--remote`                                      | Deprecated alias for `--cloud`, including the existing-session form                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `claude --remote "Fix the login bug"`                                                               |
| `--remote-control`, `--rc`                      | Start an interactive session with [Remote Control](/docs/en/remote-control#start-a-remote-control-session) enabled so you can also control it from claude.ai or the Claude app. Optionally pass a name for the session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `claude --remote-control "My Project"`                                                              |
| `--remote-control-session-name-prefix <prefix>` | Prefix for auto-generated [Remote Control](/docs/en/remote-control) session names when no explicit name is set. Defaults to your machine's hostname, producing names like `myhost-graceful-unicorn`. Set `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX` for the same effect                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `claude remote-control --remote-control-session-name-prefix dev-box`                                |
| `--replay-user-messages`                        | Re-emit user messages from stdin back on stdout for acknowledgment. Requires `--input-format stream-json` and `--output-format stream-json`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude -p --input-format stream-json --output-format stream-json --verbose --replay-user-messages` |
| `--restricted`                                  | Start in restricted mode. Use it when an evaluation harness drives `claude` on a shared machine and Claude Code must not run commands or read that machine's user and project settings. Claude Code removes the built-in tools that run commands or code, and WebFetch, unless you name them individually in `--tools`, not through the `default` preset. It also confines the built-in file tools to the [working directories](/docs/en/permissions#working-directories), loads only [managed settings](/docs/en/managed-settings) and `--settings`, refuses [`bypassPermissions`](/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode), and [refuses to create cloud sessions](/docs/en/errors#cloud-sessions-cannot-be-created-from-a-restricted-session). Requires Claude Code v2.1.248 or later                                                                                                                                                            | `claude --restricted -p "query"`                                                                    |
| `--resume`, `-r`                                | Resume a specific session by ID or name, or show an interactive picker to choose a session. In place of an ID, you can pass the absolute path to a session's `.jsonl` [transcript file](/docs/en/sessions#where-transcripts-are-stored). The picker and name search include sessions that added this directory with `/add-dir`. When you pass a session ID, Claude Code searches the current project directory and its git worktrees, then every other project on this machine. Before v2.1.223, the ID search covered only the current project directory and its git worktrees. [Background sessions](/docs/en/agent-view) appear in the picker marked with `bg`                                                                                                                                                                                                                                                                                                       | `claude --resume auth-refactor`                                                                     |
| `--safe-mode`                                   | Start with all customizations disabled to troubleshoot a broken configuration: CLAUDE.md, skills, plugins, hooks, MCP servers, custom commands and agents, output styles, workflows, custom themes, custom keybindings, status line and file-suggestion commands, LSP servers, and auto memory do not load. Authentication, model selection, built-in tools, and permissions work normally, which differs from [`--bare`](/docs/en/headless#start-faster-with-bare-mode). Managed settings policy still applies, including policy-configured hooks, status line, and file-suggestion commands; managed plugins, managed skills, managed CLAUDE.md, and policy-configured MCP servers do not. Useful for checking whether a customization is what triggers [automatic model fallback](/docs/en/model-config#automatic-model-fallback). Sets [`CLAUDE_CODE_SAFE_MODE`](/docs/en/env-vars)                                                                                      | `claude --safe-mode`                                                                                |
| `--session-id`                                  | Use a specific session ID for the conversation (must be a valid UUID)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `claude --session-id "550e8400-e29b-41d4-a716-446655440000"`                                        |
| `--setting-sources`                             | Comma-separated list of setting sources to load (`user`, `project`, `local`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --setting-sources user,project`                                                             |
| `--settings`                                    | Path to a settings JSON file or an inline JSON string. Values you set here override the same keys in your `settings.json` files for this session. Keys you omit keep their file-based values. The file must be a regular file no larger than 2 MiB. See [settings precedence](/docs/en/settings#settings-precedence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `claude --settings ./settings.json`                                                                 |
| `--strict-mcp-config`                           | Only use MCP servers from `--mcp-config`, ignoring all other MCP configurations. See [Exclusive control with managed-mcp.json](/docs/en/managed-mcp#exclusive-control-with-managed-mcp-json) for what the flag does under a managed MCP file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `claude --strict-mcp-config --mcp-config ./mcp.json`                                                |
| `--system-prompt`                               | Replace the entire system prompt with custom text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `claude --system-prompt "You are a Python expert"`                                                  |
| `--system-prompt-file`                          | Load system prompt from a file, replacing the default prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --system-prompt-file ./custom-prompt.txt`                                                   |
| `--system-prompt-snapshot`                      | Pass `off` to rebuild the system prompt on every request instead of reusing the prompt [recorded on the conversation's first request](#system-prompt-flags-in-resumed-conversations), for example while you iterate on `--append-system-prompt` text across `--continue` runs. Requires Claude Code v2.1.257 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `claude --system-prompt-snapshot off`                                                               |
| `--teleport`                                    | Resume a [cloud session](/docs/en/claude-code-on-the-web) in your local terminal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `claude --teleport`                                                                                 |
| `--teammate-mode`                               | Set how [agent team](/docs/en/agent-teams) teammates display: `in-process` (default), `auto`, `tmux`, or `iterm2` (added in v2.1.186). Overrides the [`teammateMode`](/docs/en/settings-reference#teammatemode) setting for this session. See [Choose a display mode](/docs/en/agent-teams#choose-a-display-mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude --teammate-mode auto`                                                                       |
| `--tmux`                                        | Create a tmux session for the worktree. Requires `--worktree`. Uses iTerm2 native panes when available; pass `--tmux=classic` for traditional tmux                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `claude -w feature-auth --tmux`                                                                     |
| `--tools`                                       | Restrict which built-in tools Claude can use. Use `""` to disable all, `"default"` for the default set, or tool names like `"Bash,Edit,Read"`. On macOS, Linux, and WSL, the default set leaves out `Glob` and `Grep`, as described under [Glob tool behavior](/docs/en/tools-reference#glob-tool-behavior). If you name one of the [task-tracking tools](/docs/en/tools-reference#task-tool-availability) here, Claude Code also opts the session in. The flag doesn't affect MCP tools; to deny those too, use `--disallowedTools "mcp__*"`. A list that omits [`EndConversation`](/docs/en/tools-reference#endconversation-tool-behavior) doesn't remove it; `""` removes it only when no MCP tools remain                                                                                                                                                                                                                                                                | `claude --tools "Bash,Edit,Read"`                                                                   |
| `--verbose`                                     | Enable verbose logging, shows full turn-by-turn output. Overrides the [`viewMode`](/docs/en/settings-reference#viewmode) setting for this session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `claude --verbose`                                                                                  |
| `--version`, `-v`                               | Output the version number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `claude -v`                                                                                         |
| `--worktree`, `-w`                              | Start Claude in an isolated [git worktree](/docs/en/worktrees) at `<repo>/.claude/worktrees/<name>`. If you don't give a name, Claude Code generates one. Pass `#<number>`, a GitHub pull request URL, or a GitLab merge request URL to [fetch that PR or MR from `origin` and branch the worktree from it](/docs/en/worktrees#branch-from-a-pull-request). Branching from a GitLab merge request requires Claude Code v2.1.233 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `claude -w feature-auth`                                                                            |

### System prompt flags

Claude Code provides five flags for customizing the system prompt. Four set its text, and with `--system-prompt-snapshot` you control whether a conversation keeps the text it started with. All five work in both interactive and non-interactive modes.

| Flag                          | Behavior                                                                                                                                                                    | Example                                                                    |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| `--system-prompt`             | Replaces the entire default prompt                                                                                                                                          | `claude --system-prompt "You are a Python expert"`                         |
| `--system-prompt-file`        | Replaces with file contents                                                                                                                                                 | `claude --system-prompt-file ./prompts/review.txt`                         |
| `--append-system-prompt`      | Appends to the default prompt                                                                                                                                               | `claude --append-system-prompt "Always use TypeScript"`                    |
| `--append-system-prompt-file` | Appends file contents to the default prompt                                                                                                                                 | `claude --append-system-prompt-file ./style-rules.txt`                     |
| `--system-prompt-snapshot`    | With `off`, rebuilds the prompt on every request. With `on`, the default, reuses a recorded prompt where [recording applies](#system-prompt-flags-in-resumed-conversations) | `claude --append-system-prompt "Draft rules" --system-prompt-snapshot off` |

`--system-prompt` and `--system-prompt-file` are mutually exclusive. The append flags can be combined with either replacement flag.

When the replacement text combines instructions that are the same on every run with context that changes per run, add a line containing only `__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` between the instructions and the context. Claude Code splits the prompt at the first such line and removes that line, so the part above it stays cached while the part below changes. Requires Claude Code v2.1.275 or later. [Cache the static part of a custom prompt](/docs/en/agent-sdk/modifying-system-prompts#cache-the-static-part-of-a-custom-prompt) lists the configurations where the split applies.

Choose based on whether Claude Code's default identity still fits your task. Use an append flag when Claude should remain a coding assistant that also follows your extra rules: per-invocation instructions, output formatting, or domain context for a `-p` script. Appending preserves the default tool guidance, safety instructions, and coding conventions, so you only supply what differs. Use a replacement flag when the surface, identity, or permission model differs from Claude Code's, like a non-coding agent in a pipeline that no human watches. Replacing drops all of the default prompt, including tool guidance and safety instructions, so you take responsibility for whatever your task still needs.

For persistent personas you can switch between and share across a project, use [output styles](/docs/en/output-styles). For project conventions Claude should always follow, use [CLAUDE.md](/docs/en/memory). The [Agent SDK guide on system prompts](/docs/en/agent-sdk/modifying-system-prompts#decide-on-a-starting-point) covers the same decision in more depth.

#### System prompt flags in resumed conversations

By default, Claude Code builds the system prompt once, on a conversation's first request, with the text from any system prompt flags applied, and records it in the session. Until the conversation is compacted, every later request uses that recorded prompt, including after you return to the conversation with `--resume` or `--continue`. If you pass different system prompt flag text, or none, on that later launch, it takes effect once the conversation is compacted or when you start a new conversation.

Outside of [cloud sessions](/docs/en/cloud-environments), if you start Claude Code in [bare mode](/docs/en/headless#start-faster-with-bare-mode) by passing `--bare` or setting `CLAUDE_CODE_SIMPLE=1`, recording stays off unless you pass `--system-prompt-snapshot on`. Before v2.1.268, sessions that don't [fetch feature flags](/docs/en/env-vars#features-that-need-feature-flag-fetching), including sessions on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry, rebuilt the prompt on every request and `--system-prompt-snapshot` had no effect.

To rebuild the prompt on every request instead, for example while you iterate on its wording across `--continue` runs, pass `--system-prompt-snapshot off`. Before v2.1.265, passing any of the system prompt flags also turned recording off unless you passed `--system-prompt-snapshot on`.

## See also

* [Chrome extension](/docs/en/chrome) - Browser automation and web testing
* [Interactive mode](/docs/en/interactive-mode) - Shortcuts, input modes, and interactive features
* [Quickstart guide](/docs/en/quickstart) - Getting started with Claude Code
* [Common workflows](/docs/en/common-workflows) - Advanced workflows and patterns
* [Settings](/docs/en/settings) - Configuration options
* [Agent SDK documentation](/docs/en/agent-sdk/overview) - Programmatic usage and integrations

---

## Glossary

- 官方原文：https://code.claude.com/docs/en/glossary.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-glossary.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> Definitions for Claude Code terminology. Learn what agentic loop, compaction, CLAUDE.md, hooks, subagents, MCP, and other core concepts mean.

This glossary defines Claude Code terminology. Each entry links to the page where the concept is covered in depth. For model-level concepts like tokens, temperature, and RAG, see the [platform glossary](https://platform.claude.com/docs/en/about-claude/glossary). For Claude Desktop terms such as desktop extension, MCPB, and DXT, see the [Claude Help Center](https://support.claude.com/).

## A

### AGENTS.md

A markdown file of project instructions you write for AI coding agents. If your repository has one and no [CLAUDE.md](#claude-md), Claude reads it as your project instructions without you adding a second file. You can change the **Project instructions** setting in `/config` to have Claude read both files or only `CLAUDE.md`. Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later in a session that fetches feature flags; on other versions, import it from a CLAUDE.md.

Learn more: [AGENTS.md](/docs/en/memory#agents-md)

### Agent teams

Multiple independent Claude Code sessions coordinated by a team lead, with a shared task list and peer-to-peer messaging. Unlike [subagents](#subagent), which run within a single session and report only to the parent, teammates each have their own context window and you can interact with any of them directly. Agent teams are experimental and disabled by default; see [Enable agent teams](/docs/en/agent-teams#enable-agent-teams).

Learn more: [Run agent teams](/docs/en/agent-teams)

### Agentic coding

A workflow where the AI can read files, run commands, and make changes autonomously while you watch, redirect, or step away, as opposed to chat-based assistants that only respond with text you must apply yourself. Claude Code is agentic because it has [tools](#tool) that let it act, not just advise.

Learn more: [How Claude Code works](/docs/en/how-claude-code-works)

### Agentic harness

The tools, context management, and execution environment that turn a language model into a capable coding agent. Claude Code is the harness; Claude is the model inside it. The harness supplies file access, shell execution, permission gating, memory loading, and the loop that chains actions together.

Learn more: [How Claude Code works](/docs/en/how-claude-code-works)

### Agentic loop

The cycle Claude works through for every task: gather context, take action, verify results, and repeat until done. Each tool use returns information that informs the next step. You can interrupt the loop at any point to redirect. Most extension points, including [hooks](#hook), [skills](#skill), and [MCP](#mcp-model-context-protocol), plug into specific phases of this loop.

Learn more: [How Claude Code works](/docs/en/how-claude-code-works#the-agentic-loop)

### Artifact

A live, interactive web page Claude Code publishes from your session to a private URL on claude.ai, so you can see output visually or share it instead of reading terminal text. The page updates in place when the session republishes. Artifacts you create from Claude Code appear in the same gallery as artifacts created in claude.ai conversations. Sharing depends on your plan: on Pro and Max, a public link that anyone can open; on Team and Enterprise, sharing within your organization, plus public links once an Owner enables them.

Learn more: [Share session output as artifacts](/docs/en/artifacts)

### Auto memory

Notes Claude writes for itself based on your corrections and preferences, stored per git repository under `~/.claude/projects/`. All worktrees of the same repository share one auto memory directory. The first 200 lines or 25 KB of the `MEMORY.md` index loads at the start of every session. Auto memory is the Claude-written counterpart to [CLAUDE.md](#claude-md), which you write.

Learn more: [Auto memory](/docs/en/memory#auto-memory)

### Auto mode

A [permission mode](#permission-mode) where a separate classifier model reviews actions instead of you, so Claude Code runs most of them without asking you. Claude Code still asks you before actions your explicit ask rules match. On Pro, Max, and Team plans, auto mode is the [built-in starting permission mode](/docs/en/permission-modes#which-mode-a-session-starts-in) for interactive terminal and VS Code sessions. The classifier blocks scope escalation, untrusted infrastructure, and [prompt injection](#prompt-injection). Tool results are stripped from what it sees, so hostile content in a file or web page can't manipulate it directly.

Learn more: [Eliminate prompts with auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode)

## B

### Bare mode

With `--bare`, Claude Code starts without loading hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory, or CLAUDE.md, apart from skills in a directory you pass with `--add-dir`. Recommended for CI and scripted calls where you need the same result on every machine.

Learn more: [Start faster with bare mode](/docs/en/headless#start-faster-with-bare-mode)

### Bundled skills

Prompt-based playbooks included with Claude Code, such as `/batch`, `/code-review`, `/debug`, and `/loop`. Unlike built-in commands, which execute fixed logic, bundled skills give Claude a detailed prompt and let it orchestrate the work, so they can spawn agents, read files, and adapt to your codebase.

Learn more: [Bundled skills](/docs/en/skills#bundled-skills)

## C

### Channel

An [MCP server](#mcp-model-context-protocol) that pushes events into your running session so Claude can react to things that happen while you're away from the terminal. Channels can be two-way: Claude reads an inbound event and replies back through the same channel. Telegram, Discord, and iMessage are included in the research preview.

Learn more: [Channels](/docs/en/channels)

### Checkpoint

A restore point created at each prompt you send that starts a turn. Claude Code snapshots files before every edit so a checkpoint can revert them. Press `Esc` twice or run `/rewind` to restore code, conversation, or both to an earlier point, or to summarize part of the conversation from a selected message. Checkpoints are saved with the conversation, so a resumed session can still `/rewind` to them. They're separate from git and don't track changes made through the Bash tool.

Learn more: [Checkpointing](/docs/en/checkpointing)

### `.claude` directory

The directory where Claude Code reads project-scoped configuration: settings, hooks, skills, subagents, rules, and auto memory. A project has `.claude/` at its root; your user-level defaults are at `~/.claude/`.

Learn more: [The `.claude` directory](/docs/en/claude-directory)

### CLAUDE.md

A markdown file of persistent instructions you write for Claude, loaded at the start of every session as a user message after the system prompt. Put project conventions, architecture notes, and "always do X" rules here. Project-root CLAUDE.md survives [compaction](#compaction) and is re-read fresh from disk afterward.

You can place CLAUDE.md at project scope in `./CLAUDE.md` or `./.claude/CLAUDE.md`, at user scope in `~/.claude/CLAUDE.md`, or as [managed policy](#managed-settings) for your organization. All discovered files are concatenated into context rather than overriding each other, ordered from broadest scope to most specific. Claude Code can also load a project's [AGENTS.md](#agents-md) files, on their own or alongside CLAUDE.md.

Learn more: [CLAUDE.md files](/docs/en/memory#claude-md-files)

### Cloud session

A Claude Code session that keeps running after you close your laptop, because it runs on cloud infrastructure instead of your machine: Anthropic-managed by default, or a [self-hosted environment](/docs/en/self-hosted-environments) your organization operates. You start one from claude.ai/code, the Claude mobile app, the Desktop app with **Cloud** selected, `claude --cloud`, or a [routine](/docs/en/routines). A session in your terminal, IDE, or the Desktop app with **Local** selected is a local session; to reach a local session from another device, use [Remote Control](#remote-control).

Learn more: [Use Claude Code in the cloud](/docs/en/claude-code-on-the-web)

### Command

A reusable instruction you invoke by typing `/name` in the prompt. Built-in commands such as `/clear`, `/model`, and `/compact` control the session. You can define your own commands as files in `.claude/commands/`, or install them from a [plugin](#plugin). [Skills](#skill) are the recommended way to package multi-step commands.

Two other uses of the word are unrelated: `claude` CLI subcommands such as `claude mcp add`, listed in the [CLI reference](/docs/en/cli-reference#cli-commands), and the `command` field of a stdio [MCP server](#mcp-server) entry, which specifies the executable Claude Code launches to start the server.

Learn more: [Commands](/docs/en/commands) · [Skills](/docs/en/skills)

### Compaction

Automatic summarization of your conversation when the [context window](#context-window) approaches its limit. Older tool outputs are cleared first, then the conversation is summarized. Project-root CLAUDE.md and auto memory survive compaction and reload from disk; instructions given only in conversation may be lost. Run `/compact` to trigger manually, optionally with a focus like `/compact focus on the API changes`.

Learn more: [What survives compaction](/docs/en/context-window#what-survives-compaction) · [When context fills up](/docs/en/how-claude-code-works#when-context-fills-up)

### Connector

An [MCP server](#mcp-server) added to your claude.ai account rather than configured in Claude Code. When you sign in to Claude Code with that account, your connectors appear in `/mcp` alongside the servers you added locally. Organizations can also provision connectors and set per-tool controls on them.

Learn more: [Use MCP servers from claude.ai](/docs/en/mcp#use-mcp-servers-from-claude-ai)

### Context window

The working memory for a session, holding conversation history, file contents, command outputs, CLAUDE.md, auto memory, loaded skills, and system instructions. As you work, context fills up until [compaction](#compaction) summarizes it. Run `/context` to see what's using space. For the underlying model concept, see the [platform glossary](https://platform.claude.com/docs/en/about-claude/glossary#context-window).

Learn more: [Explore the context window](/docs/en/context-window)

## D

### Dispatch

A phone-initiated task router that spawns a Claude Code session in the Desktop app when you send a coding task from the Claude mobile app. Your prompt routes to the right tool automatically. Available on Pro and Max plans.

Learn more: [Sessions from Dispatch](/docs/en/desktop#sessions-from-dispatch)

## E

### Effort level

A setting that controls adaptive reasoning, which lets the model decide whether and how much to think on each step. Higher effort means more thinking tokens and deeper reasoning; lower effort is faster and cheaper. Effort is supported on Fable models, on Opus 4.6 and later, and on Sonnet 4.6 and later.

Learn more: [Adjust effort level](/docs/en/model-config#adjust-effort-level)

### Extended thinking

Visible step-by-step reasoning the model performs before responding. You can adjust it with the [effort level](#effort-level), or cap thinking tokens with `MAX_THINKING_TOKENS` on models with a fixed thinking budget. Thinking appears in gray italic text in the terminal.

Learn more: [Use extended thinking](/docs/en/model-config#extended-thinking)

## F

### Frontmatter

A block of YAML settings at the very top of a Markdown file, between an opening `---` line and a closing `---` line. Skills, subagents, output styles, and rules each read their configuration from frontmatter, such as a skill's `description` or a subagent's `tools`, and treat everything after the closing `---` as the instructions. The opening `---` must be the file's first line. Each file type accepts its own set of fields.

Learn more: [Skill frontmatter](/docs/en/skills#frontmatter-reference), [Subagent frontmatter](/docs/en/sub-agents#supported-frontmatter-fields), [Output style frontmatter](/docs/en/output-styles#frontmatter), [Rule frontmatter](/docs/en/memory#rules-frontmatter-reference)

## H

### Hook

A user-defined handler that executes automatically at a specific point in Claude Code's lifecycle, such as before a tool runs, after a file edit, or at session start. Handlers can be a shell command, HTTP endpoint, MCP tool, LLM prompt, or subagent. Hooks are deterministic: they fire at fixed lifecycle points rather than at the model's discretion.

A hook configuration has three levels:

* **Hook event**: the lifecycle point
* **Matcher**: filters which events fire it
* **Hook handler**: what runs

Learn more: [Get started with hooks](/docs/en/hooks-guide) · [Hooks reference](/docs/en/hooks)

## M

### Managed settings

Settings enforced org-wide by IT or DevOps, delivered from Anthropic's servers through the admin console or deployed to devices at an OS-level path outside `~/.claude`. User and project settings cannot override managed settings. Server-managed delivery applies on [eligible configurations](/docs/en/server-managed-settings#platform-availability); see [Security considerations](/docs/en/server-managed-settings#security-considerations). Use this for security policies, compliance requirements, or standardized tooling across a fleet.

Learn more: [Server-managed settings](/docs/en/server-managed-settings) · [Settings files](/docs/en/settings#where-settings-live)

### MCP (Model Context Protocol)

An open standard for connecting AI tools to external data sources and services. MCP servers give Claude new tools for Slack, Jira, databases, browsers, and hundreds of other integrations. You connect servers via `/mcp` or by adding them to `.mcp.json`. For the protocol itself, see the [platform glossary](https://platform.claude.com/docs/en/about-claude/glossary#mcp-model-context-protocol).

Learn more: [Model Context Protocol](/docs/en/mcp)

### MCP server

A program that gives Claude tools, prompts, or resources over [MCP](#mcp-model-context-protocol). You add servers with `claude mcp add`, in `.mcp.json`, through a [plugin](#plugin), or as a claude.ai [connector](#connector). A local stdio server runs as a process Claude Code starts from the `command` and `args` fields of its configuration, which have nothing to do with the [commands](#command) you type at the prompt.

Learn more: [Model Context Protocol](/docs/en/mcp)

### MCP Tool Search

A context-saving mechanism that defers MCP tool schemas until needed. Only tool names and server instructions load at startup; Claude fetches the full schema on demand when it decides to use a specific tool. This keeps idle MCP servers from consuming much context.

Learn more: [Scale with MCP Tool Search](/docs/en/mcp#scale-with-mcp-tool-search)

## N

### Non-interactive mode

A mode that executes a single prompt and exits without an interactive prompt, invoked with `-p` or `--print`. Used for CI, scripts, and piping. The run is still saved as a resumable session unless you pass `--no-session-persistence`. The [Agent SDK](/docs/en/agent-sdk/overview) is the Python and TypeScript equivalent. Formerly called headless mode.

Learn more: [Run Claude Code programmatically](/docs/en/headless)

## O

### Output style

A configuration that changes the instructions Claude Code gives Claude, to set response behavior, tone, or format. Unlike [CLAUDE.md](#claude-md), which adds project context alongside Claude Code's default instructions, a custom output style can replace the default software engineering instructions.

Learn more: [Output styles](/docs/en/output-styles)

## P

### Permission mode

The baseline approval behavior for the session. Cycle with `Shift+Tab` in the CLI or use the mode selector in VS Code, Desktop, and claude.ai. Available modes are `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, and `bypassPermissions`.

The `default` mode is labeled Manual in the CLI, in the VS Code and JetBrains extensions, and in the desktop app, and Claude Code accepts `manual` as an alias for the value.

Learn more: [Choose a permission mode](/docs/en/permission-modes)

### Permission rule

A settings entry that allows, asks about, or denies a tool invocation based on the tool name and argument pattern. Rules are evaluated deny→ask→allow, first match wins. Permission rules are fine-grained controls layered on top of the broader [permission mode](#permission-mode).

Learn more: [Configure permissions](/docs/en/permissions)

### Plan mode

A [permission mode](#permission-mode) where Claude researches and proposes changes without editing your source files. It can read, search, and run exploration commands, then presents a plan for approval before touching anything. Enter plan mode with `/plan` or by pressing `Shift+Tab`.

Learn more: [Analyze before you edit with plan mode](/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)

### Plugin

A bundle of skills, hooks, subagents, and MCP servers packaged as a single installable unit. Plugin skills are namespaced as `plugin-name:skill-name` so multiple plugins coexist. Distribute plugins across teams via a [marketplace](/docs/en/plugin-marketplaces).

Learn more: [Plugins](/docs/en/plugins)

### Project trust

A dialog accepting a directory before Claude Code loads its configuration. Acceptance is saved per project directory, except your home directory, where trust is held for the current session only and the prompt reappears on each launch. Until you trust a directory, Claude Code holds back some of the content its repository supplies, such as project allow rules and marketplaces from `.claude/settings.json`. [What runs before you trust a folder](/docs/en/permissions#what-runs-before-you-trust-a-folder) lists each kind of content, including what a `-p` session runs without a dialog.

Learn more: [The `.claude` directory](/docs/en/claude-directory)

### Prompt injection

Hostile instructions embedded in a file, web page, or tool result that attempt to redirect Claude toward actions you never asked for. Claude Code's defenses include the permission system, command injection detection, and trust verification. [Auto mode](#auto-mode) adds a server-side probe that scans tool results for suspicious content and a classifier that reviews actions with tool results stripped, so injected text can't manipulate it directly.

Learn more: [Protect against prompt injection](/docs/en/security#protect-against-prompt-injection)

## R

### Remote Control

A way to continue a local Claude Code session from your phone or browser via claude.ai. Your code execution and files stay on your machine; the interface is remote. Different from a [cloud session](/docs/en/claude-code-on-the-web), which runs in a cloud sandbox.

Learn more: [Remote Control](/docs/en/remote-control)

### Rules

Modular instruction files in `.claude/rules/` that load alongside CLAUDE.md. A rule can be path-scoped with YAML `paths:` frontmatter so it only loads when Claude reads a matching file, keeping context lean until it's relevant.

Learn more: [Organize rules with `.claude/rules/`](/docs/en/memory#organize-rules-with-claude/rules/)

## S

### Sandboxing

OS-level filesystem and network isolation for the Bash tool. Commands run inside a boundary you define upfront, so Claude can work freely within it without per-command approval prompts. Sandboxing is a separate layer from [permission rules](#permission-rule).

Learn more: [Sandboxing](/docs/en/sandboxing)

### Session

A conversation tied to your current directory, with its own independent [context window](#context-window). Sessions can be resumed with `claude -c`, forked with `--fork-session` to preserve history under a new session ID, or run in parallel across terminals. Running `/clear` starts a new session; the previous one stays stored and is available via `/resume`. Each session's transcript is stored under `~/.claude/projects/`.

Learn more: [Work with sessions](/docs/en/how-claude-code-works#work-with-sessions)

### Settings layers

The hierarchy Claude Code reads configuration from, in precedence order from highest to lowest: [managed policy](#managed-settings), command-line arguments, local settings at `.claude/settings.local.json`, project settings at `.claude/settings.json`, then user settings at `~/.claude/settings.json`. Arrays merge across layers; scalars at a higher layer override lower ones. See [Settings precedence](/docs/en/settings#settings-precedence).

Learn more: [Settings files](/docs/en/settings#where-settings-live)

### Skill

A `SKILL.md` file containing instructions, knowledge, or a workflow that Claude adds to its toolkit. Claude loads a skill automatically when relevant, or you invoke it directly with `/skill-name`. Skills follow the Agent Skills open standard; Claude Code extends it with invocation control and subagent execution.

Skills are the recommended successor to custom commands. A file at `.claude/commands/deploy.md` and one at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way; existing command files continue to work.

Learn more: [Extend Claude with skills](/docs/en/skills)

### Subagent

A specialized AI assistant that runs in its own context window with a custom system prompt, specific tool access, and independent permissions. It works on a delegated task and returns a summary to the main conversation. Use subagents to keep large explorations out of your primary context or to run parallel research. A subagent stays inside the session that spawned it. To pass findings between separate sessions you run yourself, use [cross-session messaging](/docs/en/cross-session-messaging).

Built-in subagents include Explore, Plan, and general-purpose.

Learn more: [Create custom subagents](/docs/en/sub-agents)

### Surface

Any place you access Claude Code: the CLI, VS Code, JetBrains, Desktop, or claude.ai. All surfaces share the same engine. Sessions on your machine read your local CLAUDE.md, settings, and skills; [cloud sessions](/docs/en/cloud-environments#what-carries-over-from-your-setup) start from a fresh clone of your repository and don't read `~/.claude/` on your machine. Slack and the Chrome extension are integrations that connect to a surface rather than surfaces themselves.

Learn more: [Platforms and integrations](/docs/en/platforms)

## T

### Teleport

A command, `/teleport`, that pulls a cloud Claude Code session into your local terminal. Claude fetches the branch, loads the conversation history, and resumes from the cloud session's last state. The reverse direction is `--cloud`, which sends a local task to run in the cloud.

Learn more: [From cloud to terminal](/docs/en/claude-code-on-the-web#from-cloud-to-terminal)

### Tool

An action Claude can take: read a file, edit code, run a shell command, search the web, spawn a subagent. Tools are what make Claude Code agentic. Without them, Claude can only respond with text. Each tool use returns a result that informs Claude's next decision in the [agentic loop](#agentic-loop).

Learn more: [Tools available to Claude](/docs/en/tools-reference)

### Turn

One complete response from Claude within a [session](#session). A turn begins when you send a message and ends when Claude finishes responding, with any number of [tool](#tool) calls in between. [Stop hooks](#hook) fire at the end of each turn. A session consists of many turns, and the [agentic loop](#agentic-loop) describes what happens inside one.

Learn more: [How Claude Code works](/docs/en/how-claude-code-works#the-agentic-loop)

## V

### Verification loop

How a session knows the work is actually done rather than just plausible. You give Claude a check it can run, such as a test suite, a build, or a screenshot comparison, and Claude iterates until the check passes instead of stopping after one attempt. A verification loop is the prerequisite for [`/goal`](/docs/en/goal), unattended runs, and [dynamic workflows](/docs/en/workflows): without one, the only thing deciding the agent is finished is the agent itself.

Learn more: [Give Claude a way to verify its work](/docs/en/best-practices#give-claude-a-way-to-verify-its-work)

## W

### Worktree isolation

An isolation mode that runs Claude in a separate git worktree under `.claude/worktrees/`, enabled with the `-w` flag or `isolation: worktree` in subagent config. Changes stay on a separate branch in a separate directory, so parallel agents don't overwrite each other's files.

Learn more: [Run parallel sessions with git worktrees](/docs/en/worktrees)

***

## Deprecated and renamed terms

These terms appear in older docs, blog posts, and community content. Use the current name when searching this site.

| Old term                                                                | Now called                                    | Notes                                                                         |
| ----------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------- |
| Headless mode                                                           | [Non-interactive mode](#non-interactive-mode) | Same `-p` flag, same behavior                                                 |
| Web session; "Claude Code on the web" as the name for any cloud session | [Cloud session](#cloud-session)               | "Claude Code on the web" now names only the browser surface at claude.ai/code |
| Custom commands                                                         | [Skills](#skill)                              | `.claude/commands/` files still work                                          |
| Slash commands                                                          | Commands                                      | "Slash" dropped from product copy                                             |

---

## Interactive mode

- 官方原文：https://code.claude.com/docs/en/interactive-mode.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-interactive-mode.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Interactive mode

> Complete reference for keyboard shortcuts, input modes, and interactive features in Claude Code sessions.

## Keyboard shortcuts

<Note>
  Keyboard shortcuts may vary by platform and terminal. In [fullscreen rendering](/docs/en/fullscreen), press `?` in the transcript viewer to see available shortcuts there.

  **macOS users**: Option/Alt key shortcuts (`Alt+B`, `Alt+F`, `Alt+D`, `Alt+Y`, `Alt+P`) require configuring Option as Meta in your terminal. See [Enable Option key shortcuts on macOS](/docs/en/terminal-config#enable-option-key-shortcuts-on-macos) for the setting in each terminal.
</Note>

### General controls

| Shortcut                                                                                     | Description                                                                                                                                                                                                                                                                | Context                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Ctrl+C`                                                                                     | Interrupt, or clear input                                                                                                                                                                                                                                                  | Interrupts a running operation. If nothing is running, the first press clears the prompt input and a second press exits Claude Code                                                                                                                                                                                                                                                                                                                                                                                              |
| `Ctrl+X Ctrl+K`                                                                              | Stop all running [background subagents](/docs/en/sub-agents#run-subagents-in-foreground-or-background) in this session, and turn off [artifact auto-replies](/docs/en/artifacts#let-claude-reply-to-comments-on-its-own) for the rest of it. Press twice within 3 seconds to confirm | Subagent control                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Ctrl+D`                                                                                     | Exit Claude Code session                                                                                                                                                                                                                                                   | The first press shows a confirmation hint and a second press within 800ms exits. When the prompt has text, `Ctrl+D` deletes the character after the cursor instead                                                                                                                                                                                                                                                                                                                                                               |
| `Ctrl+G` or `Ctrl+X Ctrl+E`                                                                  | Open in default text editor                                                                                                                                                                                                                                                | Edit your prompt or custom response in your default text editor. `Ctrl+X Ctrl+E` is the readline-native binding. Turn on **Show last response in external editor** in `/config` to prepend Claude's previous reply as `#`-commented context above your prompt; Claude Code strips the comment block when you save                                                                                                                                                                                                                |
| `Ctrl+L`                                                                                     | Redraw the screen                                                                                                                                                                                                                                                          | Forces a full terminal redraw, keeping input and conversation history. Use this to recover if the display becomes garbled or partially blank. See [Clear the conversation](/docs/en/fullscreen#clear-the-conversation) for fullscreen rendering                                                                                                                                                                                                                                                                                       |
| `Ctrl+O`                                                                                     | Toggle transcript viewer                                                                                                                                                                                                                                                   | Shows detailed tool usage and execution, with a timestamp and the model used on each assistant message. Also expands lines that collapse by default, such as MCP calls, shown as a single `Called slack 3 times` line, and [messages from your other sessions](/docs/en/cross-session-messaging#what-a-message-looks-like), shown as a one-line `Message from @<sender>` preview                                                                                                                                                      |
| `Ctrl+R`                                                                                     | Reverse search command history                                                                                                                                                                                                                                             | Search through previous commands interactively                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Ctrl+V` or `Cmd+V` (iTerm2) or `Alt+V` (Windows and WSL)                                    | Paste image from clipboard                                                                                                                                                                                                                                                 | Inserts an `[Image #N]` chip at the cursor so you can reference it positionally in your prompt. On WSL, both `Ctrl+V` and `Alt+V` are bound; use `Alt+V` if your terminal intercepts `Ctrl+V`                                                                                                                                                                                                                                                                                                                                    |
| `Ctrl+B`                                                                                     | Background running tasks                                                                                                                                                                                                                                                   | Backgrounds Bash commands and agents. Tmux users press twice                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Ctrl+T`                                                                                     | Toggle Claude's task checklist                                                                                                                                                                                                                                             | Show or hide [Claude's to-do checklist](#task-list) in the status area. This is not the background-task view; use [`/tasks`](/docs/en/commands) to see running shells and subagents                                                                                                                                                                                                                                                                                                                                                   |
| `Ctrl+S`                                                                                     | Stash or restore prompt                                                                                                                                                                                                                                                    | With text in the input, stashes it and clears the prompt. Pressed again on an empty prompt, restores the stashed text, cursor position, and pasted content                                                                                                                                                                                                                                                                                                                                                                       |
| `Ctrl+Z`                                                                                     | Suspend Claude Code                                                                                                                                                                                                                                                        | Unix only. Suspends the process to your shell; run `fg` to resume                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `Left/Right arrows`                                                                          | Cycle through dialog tabs                                                                                                                                                                                                                                                  | Navigate between tabs in permission dialogs and menus                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Tab`                                                                                        | Accept an autocomplete suggestion, or add a comment to a permission answer                                                                                                                                                                                                 | While autocomplete suggestions are showing in the prompt input, accepts the selected suggestion. On most permission prompts, with **Yes** or **No** focused, opens a comment field on that option, and pressing it again closes the field. See [add a comment when you answer a permission prompt](/docs/en/permissions#add-a-comment-when-you-answer-a-permission-prompt)                                                                                                                                                            |
| `Up/Down arrows` or `Ctrl+P`/`Ctrl+N`                                                        | Move cursor or navigate command history                                                                                                                                                                                                                                    | When the input spans more than one visual row, whether wrapped or multiline, first moves the cursor within the prompt. Once the cursor is on the first or last visual row, pressing again navigates command history. While you have messages queued, `Up` from the first row instead [takes them back](#take-back-what-you-queued)                                                                                                                                                                                               |
| `Esc`                                                                                        | Interrupt Claude, or close a dialog                                                                                                                                                                                                                                        | Stop the current response or tool call mid-turn so you can redirect. Claude keeps the work done so far. If you have [messages queued](#queue-messages-while-claude-works), Claude Code sends them next. When a dialog is open, `Esc` closes the dialog. On a permission prompt, `Esc` declines the action, the same as [**No** without a comment](/docs/en/permissions#add-a-comment-when-you-answer-a-permission-prompt)                                                                                                             |
| `Esc` + `Esc`                                                                                | Clear input draft, or rewind                                                                                                                                                                                                                                               | When the prompt input contains text, double `Esc` clears it and saves the draft to history so `Up` recalls it. When the input is empty, double `Esc` opens the [rewind menu](/docs/en/checkpointing) to restore or summarize code and conversation from a previous point                                                                                                                                                                                                                                                              |
| `Ctrl+Enter` or `Ctrl+X Ctrl+S`                                                              | Send queued messages now                                                                                                                                                                                                                                                   | Interrupts the current turn so your [queued messages](#queue-messages-while-claude-works), and your draft with them, go out right away instead of when the turn ends. In [shell mode](#shell-mode-with-prefix), the key queues your command without interrupting. In terminals that don't report extended keys, `Ctrl+Enter` arrives as plain `Enter`; `Ctrl+X Ctrl+S` works in any terminal. Requires Claude Code v2.1.275 or later                                                                                             |
| `Shift+Tab`, or `Alt+M` on Windows when the Node or Bun runtime doesn't enable VT input mode | Cycle permission modes                                                                                                                                                                                                                                                     | Cycle through `default` (labeled Manual in the mode indicator), `acceptEdits`, `plan`, and, when available, `bypassPermissions` and then `auto`. From `auto`, the first press switches to `default`. See [permission modes](/docs/en/permission-modes). On a file permission prompt, the same key closes an open [comment field](/docs/en/permissions#add-a-comment-when-you-answer-a-permission-prompt). With no field open, it selects the option that allows the action for the rest of the session, when the prompt offers that option |
| `Option+P` (macOS) or `Alt+P` (Windows/Linux)                                                | Switch model                                                                                                                                                                                                                                                               | Switch models without clearing your prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `Option+T` (macOS) or `Alt+T` (Windows/Linux)                                                | Toggle extended thinking                                                                                                                                                                                                                                                   | Enable or disable extended thinking mode. Has no effect on Opus 5.5 or the Fable models, which always use extended thinking. Works on macOS without configuring Option as Meta                                                                                                                                                                                                                                                                                                                                                   |
| `Option+O` (macOS) or `Alt+O` (Windows/Linux)                                                | Toggle fast mode                                                                                                                                                                                                                                                           | Enable or disable [fast mode](/docs/en/fast-mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Text editing

| Shortcut                   | Description                          | Context                                                                                                                                                                                           |
| :------------------------- | :----------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Ctrl+A`                   | Move cursor to start of current line | In multiline input, moves to the start of the current logical line                                                                                                                                |
| `Ctrl+E`                   | Move cursor to end of current line   | In multiline input, moves to the end of the current logical line                                                                                                                                  |
| `Ctrl+K`                   | Delete to end of line                | Stores deleted text for pasting                                                                                                                                                                   |
| `Ctrl+U`                   | Delete from cursor to line start     | Stores deleted text for pasting. Repeat to clear across lines in multiline input. On macOS, terminal emulators including iTerm2 and Terminal.app map `Cmd+Backspace` to this shortcut             |
| `Ctrl+W`                   | Delete back to previous whitespace   | Stores deleted text for pasting. One press removes a whole path or `--flag=value`. To delete only the previous word, press `Option+Delete` on macOS or `Ctrl+Backspace` on Windows                |
| `Ctrl+Y`                   | Paste deleted text                   | Pastes the text you last deleted with one of the word or line deletion shortcuts, such as `Ctrl+K`, `Ctrl+U`, or `Ctrl+W`                                                                         |
| `Alt+Y` (after `Ctrl+Y`)   | Cycle paste history                  | After pasting, cycle through previously deleted text. Requires [Option as Meta](#keyboard-shortcuts) on macOS                                                                                     |
| `Alt+B`                    | Move cursor back one word            | Word navigation. Requires [Option as Meta](#keyboard-shortcuts) on macOS                                                                                                                          |
| `Alt+F`                    | Move cursor forward one word         | Moves to the end of the current word, or to the end of the next word when the cursor is between words. Requires [Option as Meta](#keyboard-shortcuts) on macOS                                    |
| `Alt+D`                    | Delete to end of word                | Deletes to the end of the current word, or to the end of the next word when the cursor is between words. Stores deleted text for pasting. Requires [Option as Meta](#keyboard-shortcuts) on macOS |
| `Ctrl+_` or `Ctrl+Shift+-` | Undo last input edit                 | Restores the previous input text and cursor position                                                                                                                                              |

<h3 id="make-ctrl-w-delete-back-to-whitespace">
  Word boundaries in editing shortcuts
</h3>

The word shortcuts `Alt+B`, `Alt+F`, `Alt+D`, `Option+Delete`, and `Ctrl+Backspace` treat a word as a run of letters and digits, so punctuation such as `_`, `.`, and `/` separates words. With `src/utils/foo.ts` in the prompt, repeated presses of `Alt+B` stop at the start of `ts`, `foo`, `utils`, and `src`.

`Ctrl+W` is different: it ignores punctuation and deletes back to the previous whitespace, so one press removes all of `src/utils/foo.ts`.

In text written without spaces, such as Chinese or Japanese, the word shortcuts still move or delete one word at a time.

These readline conventions apply in Claude Code v2.1.261 and later. The [`keybindingFlavor`](/docs/en/settings-reference#keybindingflavor) setting that turned them on in earlier versions is deprecated and has no effect.

You can't remap these shortcuts in the [keybindings configuration file](/docs/en/keybindings), which has no actions for them.

### Theme and display

| Shortcut | Description                                | Context                                                                                                      |
| :------- | :----------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `Ctrl+T` | Toggle syntax highlighting for code blocks | Only works inside the `/theme` picker menu. Controls whether code in Claude's responses uses syntax coloring |

### Multiline input

| Method           | Shortcut       | Context                                                                                                                                                                            |
| :--------------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quick escape     | `\` + `Enter`  | Works in all terminals                                                                                                                                                             |
| Option key       | `Option+Enter` | After enabling [Option as Meta](/docs/en/terminal-config#enable-option-key-shortcuts-on-macos) on macOS                                                                                 |
| Shift+Enter      | `Shift+Enter`  | Native in iTerm2, WezTerm, Ghostty, Kitty, Warp, Apple Terminal, Windows Terminal. For other terminals, see [Enter multiline prompts](/docs/en/terminal-config#enter-multiline-prompts) |
| Control sequence | `Ctrl+J`       | Works in any terminal without configuration                                                                                                                                        |
| Paste mode       | Paste directly | For code blocks, logs                                                                                                                                                              |

### Quick commands

| Shortcut           | Description                    | Notes                                                                                                                                                                                                                                                                                                                                            |
| :----------------- | :----------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/` at start       | Command or skill               | See [commands](#commands) and [skills](/docs/en/skills)                                                                                                                                                                                                                                                                                               |
| `!` at start       | Shell mode                     | Run a command directly, add its output to the session, and have Claude respond to it                                                                                                                                                                                                                                                             |
| `@`                | File path mention              | Trigger file path autocomplete. In sessions with [cross-session messaging](/docs/en/cross-session-messaging#message-another-session), when you type at least one letter after the `@`, Claude Code also suggests your other live sessions on this machine, so you can tell Claude to message the one you pick. Requires Claude Code v2.1.232 or later |
| `:`                | Emoji shortcode                | Type a full `:name:` to insert the emoji, or two or more characters for suggestions. See [Emoji shortcodes](#emoji-shortcodes). Requires Claude Code v2.1.217 or later                                                                                                                                                                           |
| `?` on empty input | Toggle the shortcut help panel | Typing `?` when the input already contains text inserts the character                                                                                                                                                                                                                                                                            |

### Transcript viewer

When the transcript viewer is open (toggled with `Ctrl+O`), these shortcuts are available. Run `/tui` with no argument to check which renderer is active. `Ctrl+E` can be rebound via [`transcript:toggleShowAll`](/docs/en/keybindings).

| Shortcut             | Description                                                                                                                                                                                                           |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `?`                  | Toggle the keyboard shortcut help panel. Requires [fullscreen rendering](/docs/en/fullscreen)                                                                                                                              |
| `{` / `}`            | Jump to the previous or next user prompt, like vim paragraph motion. Requires [fullscreen rendering](/docs/en/fullscreen)                                                                                                  |
| `Ctrl+E`             | Toggle show all content. Available in the classic renderer only, not in [fullscreen rendering](/docs/en/fullscreen)                                                                                                        |
| `[`                  | Write the full conversation to your terminal's native scrollback so `Cmd+F`, tmux copy mode, and other native tools can search it. Requires [fullscreen rendering](/docs/en/fullscreen#search-and-review-the-conversation) |
| `v`                  | Write the conversation to a temporary file and open it in `$VISUAL` or `$EDITOR`. Requires [fullscreen rendering](/docs/en/fullscreen)                                                                                     |
| `q`, `Ctrl+C`, `Esc` | Exit transcript view. All three can be rebound via [`transcript:exit`](/docs/en/keybindings)                                                                                                                               |

### Voice input

| Shortcut            | Description     | Notes                                                                                                                                                                            |
| :------------------ | :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hold or tap `Space` | Voice dictation | Requires [voice dictation](/docs/en/voice-dictation) to be enabled. Hold to record, or run `/voice tap` for tap-to-toggle. [Rebindable](/docs/en/voice-dictation#rebind-the-dictation-key) |

## Commands

Type `/` in Claude Code to see the commands available to you, or type `/` followed by any letters to filter. The `/` menu lists built-in commands, bundled and user-authored [skills](/docs/en/skills), and commands contributed by [plugins](/docs/en/plugins) and [MCP servers](/docs/en/mcp#use-mcp-prompts-as-commands). Not all built-in commands are visible to every user since some depend on your platform or plan, and [a few available commands are hidden from the menu by design](/docs/en/commands#how-the-command-menu-matches-what-you-type) and run when you type their full name.

In [fullscreen rendering](/docs/en/fullscreen#use-the-mouse), the `/` command and `@` file suggestion lists also respond to the mouse: hovering highlights a row and clicking accepts it.

See the [commands reference](/docs/en/commands) for the full list of commands included in Claude Code.

### Complete a command mid-prompt

Command completion also works partway through a prompt: type `/` after a space, then the first letters of a name, as in `run the tests, then /com`. Only commands whose names start with those letters match, so a file path such as `/tmp/notes.md` doesn't keep a list open. Claude Code runs a command itself only when the command [starts your message](/docs/en/commands).

* **In [fullscreen rendering](/docs/en/fullscreen)**: the matches open as a list while you type, with no row highlighted, so `Enter` still sends your prompt as typed. Press `Tab` to insert the top match, or pick a row with the arrow keys and `Enter`.
* **Outside fullscreen**: the rest of the top match appears as ghost text at your cursor, with a count such as `+2` when more commands match. Press `Tab` to insert the only match, or to open the list when several match, then pick a row with the arrow keys and `Enter`.

In both renderers, press `Tab` on a bare mid-prompt `/` to list every command.

A plugin skill matches on its bare name too, so `/deploy` finds a skill named `myplugin:deploy-app`. When you insert the match, Claude Code writes the full `/myplugin:deploy-app`.

## Vim editor mode

Enable vim-style editing via `/config` → Editor mode.

Claude Code keeps your vim mode and cursor position when you toggle the [transcript viewer](#transcript-viewer) with `Ctrl+O` or open and close a panel such as `/config`. If you leave the prompt in NORMAL mode, it's still in NORMAL mode when you return, with the cursor where you left it.

### Mode switching

| Command           | Action                                                                                                    | From mode      |
| :---------------- | :-------------------------------------------------------------------------------------------------------- | :------------- |
| `Esc` or `Ctrl+[` | Enter NORMAL mode. In terminals that use the Kitty keyboard protocol, `Ctrl+[` requires v2.1.242 or later | INSERT, VISUAL |
| `i`               | Insert before cursor                                                                                      | NORMAL         |
| `I`               | Insert at beginning of line                                                                               | NORMAL         |
| `a`               | Insert after cursor                                                                                       | NORMAL         |
| `A`               | Insert at end of line                                                                                     | NORMAL         |
| `o`               | Open line below                                                                                           | NORMAL         |
| `O`               | Open line above                                                                                           | NORMAL         |
| `v`               | Start character-wise visual selection                                                                     | NORMAL         |
| `V`               | Start line-wise visual selection                                                                          | NORMAL         |

### Remap INSERT-mode key sequences

The [`vimInsertModeRemaps`](/docs/en/settings-reference#viminsertmoderemaps) setting maps a two-key INSERT-mode sequence to Escape, so a mapping like `jj` returns you to NORMAL mode. Requires Claude Code v2.1.208 or later.

The following `~/.claude/settings.json` example turns on vim mode and maps `jj` to Escape:

```json theme={null}
{
  "editorMode": "vim",
  "vimInsertModeRemaps": { "jj": "<Esc>" }
}
```

Each key is exactly two printable characters typed in sequence, and `"<Esc>"` is the only supported target. Entries with a different length or target are ignored.

Typing the first character of a sequence inserts it normally. Pressing the second character within one second removes that pending character and switches to NORMAL mode, leaving neither character in your input. After the one-second window, or if a different key follows, both characters stay as literal text, so you can still type a word containing the sequence by pausing between the two keys.

Claude Code reads this setting from your user settings file, the `--settings` flag, and [managed settings](/docs/en/managed-settings) only. Entries in a project's `.claude/settings.json` or `.claude/settings.local.json` are ignored, so a checked-out repository can't remap your keystrokes.

### Navigation (NORMAL mode)

| Command         | Action                                                                                                                                              |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| `h`/`j`/`k`/`l` | Move left/down/up/right                                                                                                                             |
| `Space`         | Move right                                                                                                                                          |
| `w`             | Next word                                                                                                                                           |
| `e`             | End of word                                                                                                                                         |
| `b`             | Previous word                                                                                                                                       |
| `0`             | Beginning of line                                                                                                                                   |
| `$`             | End of line                                                                                                                                         |
| `^`             | First non-blank character                                                                                                                           |
| `gg`            | Beginning of input                                                                                                                                  |
| `G`             | End of input                                                                                                                                        |
| `f{char}`       | Jump to next occurrence of character                                                                                                                |
| `F{char}`       | Jump to previous occurrence of character                                                                                                            |
| `t{char}`       | Jump to just before next occurrence of character                                                                                                    |
| `T{char}`       | Jump to just after previous occurrence of character                                                                                                 |
| `;`             | Repeat last f/F/t/T motion                                                                                                                          |
| `,`             | Repeat last f/F/t/T motion in reverse                                                                                                               |
| `/`             | Open reverse history search, same as `Ctrl+R`. The empty search prompt shows a hint: press `Esc` then `i` then `/` to open the command menu instead |

<Note>
  In vim NORMAL mode, if the cursor is at the beginning or end of input and can't move further, `j`/`k` and `↑`/`↓` navigate command history instead. `←` on an empty prompt opens [agent view](/docs/en/agent-view) from NORMAL mode as well as INSERT; before v2.1.219, `←` on an empty prompt did nothing in NORMAL mode.
</Note>

### Editing (NORMAL mode)

| Command               | Action                                                                                                                    |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| `x`                   | Delete character                                                                                                          |
| `dd`                  | Delete line                                                                                                               |
| `D`                   | Delete to end of line                                                                                                     |
| `dw`/`de`/`db`        | Delete word/to end/back                                                                                                   |
| `df{char}`/`dt{char}` | Delete to and including, or up to, the next occurrence of a character                                                     |
| `cc`                  | Change line                                                                                                               |
| `C`                   | Change to end of line                                                                                                     |
| `cw`/`ce`/`cb`        | Change word/to end/back                                                                                                   |
| `s`                   | Substitute character: delete the character under the cursor and enter INSERT mode. Requires Claude Code v2.1.211 or later |
| `S`                   | Substitute line: clear the line and enter INSERT mode. Requires Claude Code v2.1.211 or later                             |
| `yy`/`Y`              | Yank (copy) line                                                                                                          |
| `yw`/`ye`/`yb`        | Yank word/to end/back                                                                                                     |
| `p`                   | Paste after cursor                                                                                                        |
| `P`                   | Paste before cursor                                                                                                       |
| `>>`                  | Indent line                                                                                                               |
| `<<`                  | Dedent line                                                                                                               |
| `J`                   | Join lines                                                                                                                |
| `u`                   | Undo                                                                                                                      |
| `.`                   | Repeat last change                                                                                                        |

### Text objects (NORMAL mode)

Text objects work with operators like `d`, `c`, and `y`:

| Command   | Action                                   |
| :-------- | :--------------------------------------- |
| `iw`/`aw` | Inner/around word                        |
| `iW`/`aW` | Inner/around WORD (whitespace-delimited) |
| `i"`/`a"` | Inner/around double quotes               |
| `i'`/`a'` | Inner/around single quotes               |
| `i(`/`a(` | Inner/around parentheses                 |
| `i[`/`a[` | Inner/around brackets                    |
| `i{`/`a{` | Inner/around braces                      |

### Visual mode

Press `v` for character-wise selection or `V` for line-wise selection. Motions extend the selection, and operators act on it directly.

| Command          | Action                                               |
| :--------------- | :--------------------------------------------------- |
| `d`/`x`          | Delete selection                                     |
| `y`              | Yank selection                                       |
| `c`/`s`          | Change selection                                     |
| `p`              | Replace selection with register contents             |
| `r{char}`        | Replace every selected character with `{char}`       |
| `~`/`u`/`U`      | Toggle, lowercase, or uppercase selection            |
| `>`/`<`          | Indent or dedent selected lines                      |
| `J`              | Join selected lines                                  |
| `o`              | Swap cursor and anchor                               |
| `iw`/`aw`/`i"`/… | Select a text object                                 |
| `v`/`V`          | Toggle between character-wise and line-wise, or exit |

Block-wise visual mode with `Ctrl+V` is not supported.

## Command history

Claude Code keeps a history of the prompts you type, and Up-arrow recall reaches prompts from past sessions of the same project:

* Input history is stored per working directory
* Running `/clear` starts a new session: recall then lists the new session's prompts first, with earlier sessions' prompts after them. The previous session's conversation is preserved and can be resumed.
* Submitting the same prompt twice in a row records one history entry, so pressing Up steps to the previous distinct prompt
* When you recall a prompt that included pasted text, Claude Code sends the full pasted content again when you resubmit. If the content has since been [cleaned up](/docs/en/claude-directory#cleaned-up-automatically), Claude Code doesn't send the literal `[Pasted text #N]` string; see [Paste large content](/docs/en/terminal-config#paste-large-content) for what happens to the prompt
* History expansion with `!` is disabled by default

### Reverse search with Ctrl+R

Press `Ctrl+R` to interactively search through your command history. In [fullscreen rendering](/docs/en/fullscreen), `Ctrl+R` opens a search dialog instead: type to filter, press `Up` and `Down` to move through matches, and press `Ctrl+S` to cycle the scope through this session, this project, and all projects. Press `Enter` or `Tab` to place a match in the prompt input, or `Esc` to cancel. The steps below describe the classic renderer's inline search:

1. **Start search**: press `Ctrl+R` to activate reverse history search
2. **Type query**: enter text to search for in previous commands. The search term is highlighted in matching results
3. **Navigate matches**: press `Ctrl+R` again to cycle through older matches
4. **Search scope**: the inline search always searches prompts from all projects
5. **Accept match**:
   * Press `Tab` or `Esc` to accept the current match and continue editing
   * Press `Enter` to accept and execute the command immediately
6. **Cancel search**:
   * Press `Ctrl+C` to cancel and restore your original input
   * Press `Backspace` on empty search to cancel

The inline search scans your full prompt history, newest first, with duplicates collapsed to the newest occurrence. The fullscreen dialog searches your whole prompt history in the selected scope, newest first, with duplicates collapsed to the newest occurrence: the most recent prompts appear immediately, and matches from older prompts fill in as Claude Code loads the rest. Matching prompts display with the search term highlighted, so you can find and reuse previous inputs.

Accepting a match or canceling the search takes effect immediately, even while Claude Code is still loading the history.

## Background Bash commands

Claude Code supports running Bash commands in the background, allowing you to continue working while long-running processes execute.

### How backgrounding works

When Claude Code runs a command in the background, it runs the command asynchronously and immediately returns a background task ID. Claude Code can respond to new prompts while the command continues executing in the background.

To run commands in the background, you can either:

* Prompt Claude Code to run a command in the background
* Press `Ctrl+B` to move a regular Bash tool invocation to the background. Tmux users must press `Ctrl+B` twice due to tmux's prefix key.

**Key features:**

* Output is written to a file and Claude can retrieve it using the Read tool
* Background tasks have unique IDs for tracking and output retrieval
* Background tasks are automatically cleaned up when Claude Code exits. On macOS and Linux, when you stop a background task from [`/tasks`](/docs/en/commands) or Claude Code stops it at exit, processes that detached from the task's shell, such as ones started under `setsid` or `timeout`, stop too
* If you background the session instead of exiting it, your background tasks keep running in the background session. See [background a running session](/docs/en/agent-view#from-inside-a-session)
* Background tasks are automatically terminated if output exceeds 5GB, with a note in stderr explaining why
* On macOS and Linux, Claude Code stops your running background tasks when the operating system reports critical memory pressure, provided the session has been idle for at least 30 minutes and no turn or subagent is running. Requires Claude Code v2.1.193 or later
  * The [debug log](/docs/en/debug-your-config) says why tasks were stopped, or why a pressure event left them running
  * Set [`CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP`](/docs/en/env-vars) to `1` to turn off memory-pressure stops
* Background commands owned by a [subagent](/docs/en/sub-agents) have no time limit, except that a command owned by a subagent running in the foreground ends when that subagent gives its final response; see [Background commands](/docs/en/tools-reference#background-commands) in the tools reference. Before v2.1.218, neither the memory-pressure reap nor the former 60-minute limit on subagent commands covered commands moved to the background with `Ctrl+B`

To disable all background task functionality, set the `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to `1`. See [Environment variables](/docs/en/env-vars) for details.

**Common backgrounded commands:**

* Build tools (webpack, vite, make)
* Package managers (npm, yarn, pnpm)
* Test runners (jest, pytest)
* Development servers
* Long-running processes (docker, terraform)

### Shell mode with `!` prefix

Run shell commands directly without going through Claude by prefixing your input with `!`:

```bash theme={null}
! npm test
! git status
! ls -la
```

Shell mode:

* Adds the command and its output to the conversation context
* Shows real-time progress and output
* Supports the same `Ctrl+B` backgrounding for long-running commands
* Doesn't require Claude to interpret or approve the command
* Supports history-based autocomplete: type a partial command and press `Tab` to complete from previous `!` commands in the current project
* Supports live file path autocomplete as of v2.1.193 on all platforms: type a token containing a forward slash, such as `./src/` or `~/`, to see a dropdown of matching files and directories, then press `Tab` to accept. Use forward slashes on Windows too; the dropdown is triggered by `/`, not `\`
* Exit with `Escape`, `Backspace`, or `Ctrl+U` on an empty prompt
* Pasting text that starts with `!` into an empty prompt enters shell mode automatically, matching typed `!` behavior

Unless your session is one of those listed under [strict sandbox mode](/docs/en/sandboxing#the-unsandboxed-retry-escape-hatch), commands you type in shell mode run outside the [sandbox](/docs/en/sandboxing) even when you've enabled sandboxing, because the sandbox applies to the commands Claude runs.

Claude responds to the command output automatically once it lands in the transcript, so you can run `! npm test` and get an explanation of the failures without a second prompt. The response costs the same as sending a normal prompt. To restore the earlier behavior where the output is added to context without a response, set [`respondToBashCommands`](/docs/en/settings-reference#respondtobashcommands) to `false` in `settings.json`. Before v2.1.186, shell mode always added output to context without a response.

## Queue messages while Claude works

Type a message and press `Enter` while Claude is working. Claude Code queues the message instead of interrupting the turn, and lists the queued entries above the input box until it sends them. You can queue `!` [shell commands](#shell-mode-with-prefix) and most [commands](/docs/en/commands) the same way, apart from the commands, such as `/status`, that Claude Code runs as soon as you send them.

Sent and queued messages show in gray until Claude starts responding to them, so you can tell which messages Claude hasn't started on yet.

### When Claude Code sends what you queued

When a queued entry reaches Claude depends on what you queued.

* Messages: if you queue a message while Claude is running tool calls, Claude Code passes it to Claude as soon as those tool calls finish, within the same turn. When the turn ends with messages still queued, they go out without another key press, in the order you typed them
* Commands and shell commands: Claude Code holds them until the turn ends, then runs them one at a time, keeping the order you queued them in

To send what you queued without waiting for the turn to finish, press `Ctrl+Enter`. Claude Code interrupts the turn, and your queued messages go out right away, with your draft queued behind them if you had typed one. In [shell mode](#shell-mode-with-prefix), the key queues your command without interrupting the turn. Requires Claude Code v2.1.275 or later.

In terminals that don't report extended keys, `Ctrl+Enter` arrives as plain `Enter` and queues the draft instead; `Ctrl+X Ctrl+S` works in any terminal. Both keys are bindings of the [`chat:sendNow` action](/docs/en/keybindings#chat-actions).

Press `Esc` to interrupt the turn without submitting your draft. Claude Code keeps what you queued and sends it right away.

Claude Code runs some commands as soon as you send them instead of queueing them, among them `/model`, `/effort`, and `/fast`. Each of the three changes a setting: the model, the effort level, or fast mode. Whether Claude Code applies the new setting to the turn Claude is already working on, or only from your next turn, differs by command:

* [`/model`](/docs/en/model-config#setting-your-model): once you confirm the [cache warning](/docs/en/prompt-caching#switching-models), if Claude Code shows one, Claude Code applies your change to the next request it makes in that turn
* [`/effort`](/docs/en/model-config#adjust-effort-level): once you confirm the [cache warning](/docs/en/prompt-caching#changing-effort-level), if Claude Code shows one, Claude Code applies your change to the next request it makes in that turn
* [`/fast`](/docs/en/fast-mode#toggle-fast-mode): Claude Code keeps the fast mode setting that was active when the turn started, so your speed change applies from your next turn. If your current model doesn't support fast mode, turning it on also [switches your model](/docs/en/prompt-caching#turning-on-fast-mode), and Claude Code uses the new model from its next request in that turn

### Take back what you queued

Press `Up` from the first line of the input box to take back the queued messages and commands. Claude Code removes them from the queue and puts them in the input box, one per line, ahead of any text you had typed. Edit the text and press `Enter` to queue it again as one entry, or clear the input box to drop it.

Claude Code takes back queued shell commands only when the input box is empty and you have nothing else queued, and it switches the input box to shell mode when it does. Otherwise it leaves them in the queue, listed with their `!` prefix, and runs them after the turn ends.

## Prompt suggestions

When you first open a session, Claude Code shows a grayed-out example command in the prompt input to help you get started. It picks this from your project's git history, so the example reflects files you've been working on recently.

After Claude responds, Claude Code can suggest your next prompt based on your conversation history, such as a follow-up step from a multi-part request or a natural continuation of your workflow.

* Press `Tab` or `Right arrow` to place the suggestion in the prompt input, then `Enter` to submit
* Start typing to dismiss it

Claude Code generates each of these next-prompt suggestions with a background request that reuses the conversation's prompt cache, so the additional cost is minimal.

### When Claude Code skips suggestions

In interactive mode, Claude Code leaves prompt suggestions off by default and hides the **Prompt suggestions** toggle in `/config` in a [session that doesn't fetch feature flags](/docs/en/env-vars#features-that-need-feature-flag-fetching), such as one on a third-party provider or through a Claude apps gateway, and in a [first session after an install or upgrade](/docs/en/env-vars#first-session-after-an-install-or-upgrade) whose flags haven't arrived yet.

Claude Code also skips individual suggestions in several situations, including:

* The prompt cache is cold, to avoid unnecessary cost
* After the first turn of a conversation, in some sessions
* The previous response ended in an error
* While you're in plan mode
* Your account is close to or at its usage limit. To keep suggestions on until you reach the limit, set [`CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION`](/docs/en/env-vars) to `true`. Before v2.1.238, Claude Code skipped them near the limit even with the variable set to `true`
* In an [agent team](/docs/en/agent-teams), in teammates' sessions by default. The lead's session shows suggestions

In print mode, Claude Code doesn't generate suggestions by default. Pass [`--prompt-suggestions`](/docs/en/cli-reference#cli-flags) with `-p "<prompt>" --output-format stream-json --verbose` to have Claude Code emit a `prompt_suggestion` message after each turn that generates one. The generator skips very short conversations and cold prompt caches here too, so a single short `-p` query can emit none.

### Turn prompt suggestions off

To disable prompt suggestions entirely, use any of the following:

* Turn off **Prompt suggestions** in `/config`
* Set [`promptSuggestionEnabled`](/docs/en/settings-reference#promptsuggestionenabled) to `false` in your settings file
* Set the [`CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION`](/docs/en/env-vars) environment variable to `false`, which takes precedence over the setting:
  ```bash theme={null}
  export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
  ```

To turn prompt suggestions off across an organization, set `promptSuggestionEnabled` to `false` in [managed settings](/docs/en/managed-settings). Also set `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` to `false` under the managed [`env`](/docs/en/settings-reference#env) key so that users can't re-enable them with their own environment variable.

## Emoji shortcodes

Type a `:` followed by an emoji shortcode in the prompt input to insert the emoji. Requires Claude Code v2.1.217 or later.

* Type a complete shortcode such as `:heart:` and Claude Code replaces it with ❤️ as soon as you type the closing `:`
* Type `:` plus at least two characters of a name, such as `:hea`, to open a suggestion popup, then press `Tab` or `Enter` to insert the highlighted emoji

The shortcode must start the input or follow a space, so a `:` inside a word or URL doesn't open suggestions.

To turn the feature off, set [`emojiCompletionEnabled`](/docs/en/settings-reference#emojicompletionenabled) to `false` in `settings.json`. This disables both the suggestion popup and the inline replacement.

## Check spelling as you type

Claude Code can underline misspelled words in the prompt input while you type. It checks only the text in the input box, never Claude's replies or your files. It also checks nothing while the input box is in [shell mode](#shell-mode-with-prefix), `Ctrl+R` history search, or [voice dictation](/docs/en/voice-dictation).

Spell checking is off by default, and Claude Code checks nothing in [screen reader mode](/docs/en/accessibility). Requires Claude Code v2.1.235 or later.

### Prerequisites

* Install [aspell](https://github.com/GNUAspell/aspell), [hunspell](https://github.com/hunspell/hunspell), or [ispell](https://en.wikipedia.org/wiki/Ispell) and make sure it's on your `PATH`. Claude Code runs the first of the three it finds, in that order, on every platform, including a `.cmd` shim a package manager installs on Windows.
* To check that the program is on your `PATH`, run `aspell --version`, `hunspell --version`, or `ispell -v` in your terminal. A "command not found" error means it isn't on your `PATH` yet.

### Turn spell checking on or off

Claude Code reads the [`spellcheck`](/docs/en/settings-reference#spellcheck) setting from three places, and ignores it in a project's `.claude/settings.json` and `.claude/settings.local.json`. Turn it on from whichever one you use:

  <Tab title="User settings">
    Add `spellcheck` to `~/.claude/settings.json`. It applies in every project you open, like the rest of your [user settings](/docs/en/settings#where-settings-live):

    ```json theme={null}
    {
      "spellcheck": { "enabled": true }
    }
    ```
  </Tab>

  <Tab title="Command line">
    Save `spellcheck` in a JSON file, such as `spellcheck.json`:

    ```json theme={null}
    {
      "spellcheck": { "enabled": true }
    }
    ```

    Then pass the file to `--settings`. It applies to that session only:

    ```bash theme={null}
    claude --settings spellcheck.json
    ```
  </Tab>

  <Tab title="Managed settings">
    Add `spellcheck` to one of your organization's [managed settings sources](/docs/en/permissions#managed-settings). It applies to every user who receives those settings, and they can't turn it off:

    ```json theme={null}
    {
      "spellcheck": { "enabled": true }
    }
    ```
  </Tab>

To check that spell checking is on, type a misspelled word and a space. Claude Code underlines the word. If it doesn't, see [When Claude Code underlines nothing](#when-claude-code-underlines-nothing). To turn spell checking off again, set `enabled` to `false` in the same place, or remove `spellcheck`.

To choose which of the three programs Claude Code runs, which dictionary it uses, or the underline color, add any of these fields next to `enabled`, in the same place:

* `checker`: `aspell`, `hunspell`, or `ispell`. Claude Code doesn't fall back from a checker you name, and treats any other value as `auto`.
* `language`: a dictionary name in your checker's form, such as `en_GB`. Claude Code ignores any value that isn't a plain dictionary name, such as a path or a name with spaces, and the checker uses its default dictionary.
* `color`: a color name such as `yellow`, or a `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `ansi256(n)`, or `ansi:<name>` value. Claude Code uses your theme's error color by default and for any value it doesn't recognize.

For example, this `spellcheck` setting runs hunspell with its `en_GB` dictionary and underlines words in yellow. It works the same in `~/.claude/settings.json`, in the file you pass to `--settings`, and in managed settings:

```json theme={null}
{
  "spellcheck": {
    "enabled": true,
    "checker": "hunspell",
    "language": "en_GB",
    "color": "yellow"
  }
}
```

If more than one of the three places has a `spellcheck` setting, Claude Code uses only one of them: managed settings first, then `--settings`, then user settings. It doesn't combine fields from two places. For example, when `--settings` sets `spellcheck`, a `language` in your user settings has no effect.

### What Claude Code underlines

Shortly after you pause typing, Claude Code underlines the words the dictionary doesn't know. It leaves the word you're still typing alone until you move past it, and it never changes your text. It also skips text that looks like code:

* Commands such as `/help`, `@` mentions, URLs, file paths, and flags such as `--verbose`
* Words with digits, underscores, or a capital letter after the first, and text in backticks

Claude Code also skips Chinese, Japanese, Korean, Thai, Lao, Khmer, and Myanmar text.

Claude Code has no word list of its own: a word is misspelled when your checker says so. To stop Claude Code from underlining a word, add the word to your checker's personal dictionary, following the checker's own documentation. Claude Code picks up the new word after you restart it.

### When Claude Code underlines nothing

Claude Code underlines nothing when it can't keep a checker running:

* No checker is installed, or the one you named in `checker` is missing
* The checker fails twice in a row, at startup or later in the session. Claude Code restarts it after the first failure and stops checking after the second, until you restart Claude Code
* The checker takes more than 15 seconds to answer, three times. Each time, Claude Code leaves the words it was waiting on unmarked; after the third, it stops checking until you restart Claude Code

To find out which of these happened, start `claude --debug` with spell checking on and type a word. Then look for the `[spellcheck]` lines in the debug log at `~/.claude/debug/<session-id>.txt`. One line names the program Claude Code started, or lists the ones it looked for and didn't find. Later lines say why it stopped. A missing-dictionary error there means the checker has no dictionary for your `language` value, or no default one when `language` is unset. Install one, or set `language` to a dictionary you have.

## Invisible characters in prompts

Pasted text can carry Unicode characters that a terminal draws as nothing at all, such as tag characters, bidirectional controls, and zero-width spaces, so a prompt can contain text you never see. To keep copied text from carrying instructions your terminal doesn't draw, Claude Code removes those characters when you press Enter, before sending anything. It cleans both the prompt and the contents of any collapsed [pasted-text reference](/docs/en/terminal-config#paste-large-content) the prompt includes. Claude Code keeps the joiners that Persian and Indic scripts write and the selectors inside emoji sequences.

If Claude Code removed anything, that Enter sends nothing. The cleaned prompt goes back into the input box with a notice such as `Removed 3 invisible characters · review and press Enter to send`, and pressing Enter again sends the text as shown.

When you pass a prompt on the command line, as in `claude "fix the login bug"`, or pipe one into an interactive session, Claude Code doesn't wait for a second Enter. It removes the characters, shows a notice, and sends the cleaned prompt. If the cleaned prompt would begin with `/`, Claude Code puts it in the input box for you to review and send instead.

## Review changes with /diff

Run `/diff` to look over the changes in your working tree without leaving Claude Code. You see the edits Claude has made so far alongside anything else you haven't committed.

In the changes `/diff` reads from git, a submodule appears as a single entry, and only when the commit it points to changes; edits to files inside the submodule don't appear there.

In [fullscreen rendering](/docs/en/fullscreen), `/diff` opens the [diff panel](#diff-panel) beside the conversation, which stays open and updates while you keep working. In the classic renderer, `/diff` opens the [diff viewer](#diff-viewer) in place of the prompt, and you close it when you're done reading.

### Diff panel

The diff panel lists the changed files with their added and removed line counts, and shows each file's diff under the list. Claude Code refreshes it each time Claude edits a file or runs a shell command. To close it, run `/diff` again or click the `✕` in its header.

To use the panel you need:

* [Fullscreen rendering](/docs/en/fullscreen)
* A git repository
* A terminal at least 110 columns wide
* Claude Code v2.1.260 or later

When the panel can't open, `/diff` opens the diff viewer instead or tells you why.

The panel also opens on its own once Claude starts editing files, if your terminal is at least 144 columns wide. After you've opened it yourself with `/diff`, later sessions open it as soon as Claude edits a file in any terminal wide enough to fit it. Close the panel and it stays closed, in this session and later ones, until you run `/diff` again.

While the panel is open, you can:

* **Jump to a file**: click its row in the list. Scroll the panel with the mouse wheel. When the file list itself is too long to fit, scroll it with `Alt+Up` and `Alt+Down`, or `Ctrl+Up` and `Ctrl+Down`.
* **Ask Claude about specific lines**: select them in the panel with the mouse. Claude Code attaches the selection to your next prompt and shows a line count in the input until you send it.
  * To send the prompt without the selection, move the cursor to just after the line-count indicator and press `Backspace` to delete it. Requires Claude Code v2.1.271 or later.
* **Show the files the panel leaves out**: the list skips test files and generated files, and collapses changes from before this session into one line at the bottom. Click either count line to expand it.
* **Change what the panel compares against**: press `Ctrl+X B` to cycle from this session's changes, to your uncommitted changes as one list, to everything since your branch split from the default branch. Claude Code remembers the choice for each project.

To bind keys to these actions, see [Diff panel actions](/docs/en/keybindings#diff-panel-actions).

### Diff viewer

The diff viewer takes the place of the prompt until you close it. Its **Current** view shows your uncommitted changes from git, or, when there are none, what your branch adds on top of the default branch. The viewer also has a turn view for each prompt after which Claude edited files, showing just those edits. Claude Code builds the turn views from Claude's file edits rather than from git, so a change Claude makes through a shell command appears only under Current.

Use these keys in the viewer:

* **Left and Right**: move between Current and the turn views.
* **Up and Down**: select a file.
* **Enter**: open the selected file's diff. Scroll it with Up and Down, or PageUp and PageDown.
* **Esc**: return from a file's diff to the list, or close the viewer from the list.

To rebind these keys, see [Diff actions](/docs/en/keybindings#diff-actions).

## Side questions with /btw

Use `/btw` to ask a question about your current work without adding to the conversation history.

```
/btw what was the name of that config file again?
```

Claude answers a side question from what's already in the conversation: your messages, its replies, and the tool results it has gathered. You can ask about code Claude has already read, decisions it made earlier, or anything else from the session. A later side question also sees your earlier side questions: Claude Code replays the newest 20 exchanges with each ask, until you clear them. The question and answer never enter the conversation history. In the terminal, they appear in a dismissible overlay. The terminal keeps the thread in memory: press `x` to clear the earlier exchanges, and it's gone when you exit Claude Code.

In the [VS Code extension](/docs/en/vs-code#use-the-prompt-box)'s chat panel, `/btw` opens a panel rather than the overlay this section describes, and you ask follow-up questions right in the panel. The panel's thread survives window reloads, on the retention schedule that page describes. You need the extension at v2.1.227 or later. Earlier extension versions don't offer `/btw`.

* **Available while Claude is working**: you can run `/btw` even while Claude is processing a response. The side question runs independently and doesn't interrupt the main turn. It sees everything in the conversation so far, except the reply Claude is still writing.
* **No tool access**: side questions answer only from what is already in context. Claude can't read files, run commands, or search when answering a side question. If Claude writes out tool calls as text anyway, the answer ends with a note that nothing was executed.
* **Single response**: there are no follow-up turns in the overlay. To continue the thread, ask another `/btw` question. To continue with full tool access in a local session, press `f` to fork this question and answer into a [background subagent](/docs/en/sub-agents#fork-the-current-conversation).
* **Low cost**: while the conversation's [prompt cache](/docs/en/prompt-caching) is warm, a side question costs little beyond the answer itself.

Your five newest earlier side questions appear as a dimmed list above the current answer, with a count of any older ones. They stay out of the conversation history.

To return to the overlay after dismissing it, run `/btw` with no question. The overlay reopens on your most recent exchange. Before v2.1.212, `/btw` without a question printed a usage message instead.

Once the answer appears, the overlay accepts these keys.

| Key                          | Action                                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Space`, `Enter`, `Escape`   | Dismiss the answer and return to the prompt                                                                                                                                                                                                                                                                                                                                                       |
| `Up` / `Down`                | Scroll the answer                                                                                                                                                                                                                                                                                                                                                                                 |
| `Shift+Left` / `Shift+Right` | Step between this answer and your earlier `/btw` answers. `Shift+Left` moves to older answers and `Shift+Right` returns toward the current one. `[` and `]` do the same, for terminals that don't report `Shift` with arrow keys. `Tab` / `Shift+Tab` cycle through the same answers. Requires Claude Code v2.1.257 or later. Between v2.1.187 and v2.1.256, the keys were plain `Left` / `Right` |
| `c`                          | Copy the answer to your clipboard as raw Markdown. Use this instead of mouse selection, which captures the hard-wrapped terminal rendering rather than the source text                                                                                                                                                                                                                            |
| `f`                          | Start a [forked subagent](/docs/en/sub-agents#fork-the-current-conversation) that inherits the parent conversation plus this question and answer, so it can continue with full tool access. You stay in the current session and find the fork in the [panel below your prompt](/docs/en/sub-agents#observe-and-steer-running-forks). Available in local sessions only                                       |
| `x`                          | Clear the list of earlier `/btw` exchanges shown above the current answer                                                                                                                                                                                                                                                                                                                         |

In an attached [background session](/docs/en/agent-view#attach-to-a-session), `Left` detaches and returns you to agent view, even while the answer is still arriving. The side question keeps running while you're away. The next time you attach to the session, the overlay reopens with the side question, or with its answer. Before v2.1.257, `Left` didn't detach there.

`/btw` sees your full conversation but has no tools. A [subagent](/docs/en/sub-agents) has tools and starts from the prompt it receives, or, for a [fork](/docs/en/sub-agents#fork-the-current-conversation), from a copy of this conversation. Use `/btw` to ask about what Claude already knows from this session; use a subagent to go find out something new.

## Task list

The task list is Claude's to-do checklist: items Claude created to plan multi-step work, with indicators showing what's pending, in progress, or complete. It's separate from the background-task view. To see running shells and subagents, use [`/tasks`](/docs/en/commands) instead.

The list fills only in sessions that have the task-tracking tools, which Claude Code provides by default on [Claude 3.x models, Opus 4 through 4.7, Sonnet 4 through 4.6, and Haiku 4.5](/docs/en/tools-reference#task-tool-availability). On any other model, including a model ID Claude Code doesn't recognize, the list stays empty unless you opt in with `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` or one of the other ways under [Task tool availability](/docs/en/tools-reference#task-tool-availability). When the session has the tools, the task list works as follows:

* Press `Ctrl+T` to toggle the task list view. The display shows up to five tasks at a time. When Claude hasn't created any checklist items yet, the toggle has no visible effect because there's nothing to display
* If you leave the list expanded, Claude Code restores the expanded view the next time you launch into a session that still has tasks, such as with `--resume` or `--continue`. When the task list is empty, Claude Code starts it collapsed
* To see all tasks or clear them, ask Claude directly: "show me all tasks" or "clear all tasks"
* Tasks persist across context compactions, helping Claude stay organized on larger projects
* To share a task list across sessions, set `CLAUDE_CODE_TASK_LIST_ID` to use a named directory in `~/.claude/tasks/`: `CLAUDE_CODE_TASK_LIST_ID=my-project claude`

## Session recap

When you return to the terminal after stepping away, Claude Code shows a one-line recap of what happened in the session so far. The recap generates in the background once at least three minutes have passed since the last completed turn and the terminal is unfocused, so it's ready when you switch back. Recaps only appear once the session has at least three turns, and never twice in a row.

Run `/recap` to generate a summary on demand. Claude Code caps both automatic recaps and `/recap` output at 400 characters. To turn automatic recaps off, open `/config` and turn off **Session recap**.

Session recap is on by default for every plan and provider. The recap is always skipped in non-interactive mode.

## Wait for a usage limit to reset

When a claude.ai [usage limit](/docs/en/errors#youve-hit-your-session-limit) stops Claude mid-task, Claude Code waits in the open session and continues the task on its own after the limit resets. Automatic continue is on by default in interactive sessions signed in with a claude.ai subscription. Requires Claude Code v2.1.234 or later.

While Claude Code waits, a line at the bottom of the session shows when it will continue:

```text theme={null}
Usage limit reached · continuing automatically at 3:45pm · esc to cancel
```

Keep the session open. What happens next depends on how the wait ends:

* **At the reset**: the line reads `continuing shortly`, then `Usage limit reset · continuing automatically`, and Claude Code sends Claude a fixed prompt to pick the task up where it stopped. It doesn't resend your last message.
* **After your computer slept**: if it slept for more than about 30 minutes and the limit reset while it slept, the line reads `Your usage limit has reset · press enter to continue`. Press `Enter` to continue. After a shorter sleep, Claude Code continues on its own.
* **Early**: when you finish adding [usage credits](/docs/en/costs#add-usage-credits-to-your-subscription) with `/usage-credits`, sign back in after `/upgrade`, or switch models with `/model` during the wait, Claude Code checks whether usage is available again and continues right away if it is. It doesn't check after an upgrade or purchase you make in a browser on your own. Under [`opusplan`](/docs/en/model-config#opusplan-model-setting) and other model settings that run plan mode on a different model, Claude Code waits for the reset instead.

The continued task runs like any other turn. Claude Code still asks for [permissions](/docs/en/permissions) as usual, so the task can stop on a prompt while you're away. If it hits the limit again, Claude Code re-arms the wait on its own at most twice in a row, then stops and shows `Automatic continue stopped after repeated usage-limit hits · /rate-limit-options to try again`.

### Cancel the wait

Press `Esc` at an empty prompt, or `Ctrl+C`, while the line shows, or run [`/rate-limit-options`](/docs/en/commands#all-commands) and pick **Don't continue automatically**. Claude Code confirms with a line that starts `Automatic continue cancelled`.

After a cancel, nothing continues until you send a prompt or pick the row that starts **Wait here, then continue automatically** from `/rate-limit-options` again. Claude Code doesn't start a wait on its own again for that reset window; the next reset window starts fresh.

The wait also ends without continuing the task in these cases:

* **You send a prompt**: Claude Code runs your prompt instead of waiting.
* **You exit Claude Code**: the wait doesn't restart when you resume the session.
* **The conversation changes hands**: you switch accounts with `/login`, clear or rewind the conversation, `/resume` another session, pull one with `/teleport`, relaunch with `/tui`, or hand the session to Claude Desktop, a background session, or the cloud.
* **The setting turns off, or the reset moves past 24 hours**: this ends only a wait Claude Code started on its own. A wait you picked from `/rate-limit-options` keeps counting down.
* **The continuation is blocked**: a [`UserPromptSubmit` hook](/docs/en/hooks#userpromptsubmit) that blocks the continuation prompt, or a failure before it reaches the model, ends the wait. Claude Code tells you the continuation didn't run. Send a prompt to continue.

### Start a wait yourself

Claude Code doesn't start the wait on its own in these cases:

* **Remote Control and agent team teammate sessions**: a person at that terminal can still start one.
* **A reset more than 24 hours away**: a weekly limit can reset days out.
* **An Opus or Sonnet limit while you run a model outside that family**: your next turn may not hit that limit. [`opusplan`](/docs/en/model-config#opusplan-model-setting) and other model settings that run plan mode on the limited family don't get this exception.

In those cases, and whenever automatic continue is off, Claude Code opens the usage-limit options menu once per reset window when you hit a limit at your own terminal. Pick the row that starts **Wait here, then continue automatically** to start the wait. In a [Remote Control](/docs/en/remote-control) or [agent team](/docs/en/agent-teams) teammate session, run `/rate-limit-options` yourself to open the menu.

Claude Code doesn't offer the wait at all in these cases:

* **Background sessions and `-p` runs**: the menu row isn't available.
* **API keys, cloud providers, and usage-based billing**: usage there is metered per request, so there is no reset to wait for.
* **An [LLM gateway](/docs/en/llm-gateway#subscriptions-and-gateways) without a saved claude.ai login**: Claude Code offers the wait only while a saved claude.ai login is the active credential.

### Turn automatic continue off

In `/config`, turn off **Continue automatically at usage limit**, or set [`autoContinueAtUsageLimit`](/docs/en/settings-reference#autocontinueatusagelimit) to `false` in your user settings. `/config autoContinueAtUsageLimit=false` also works, including with `-p`, but the `key=value` form can't turn it back on, because the setting grants unattended execution. Which settings files Claude Code reads for this key is in the [settings reference](/docs/en/settings-reference#autocontinueatusagelimit).

## PR review status

When working on a branch with an open pull request, Claude Code displays a clickable PR link in the footer, such as "PR #446". The link has a colored underline indicating the review state:

* Green: approved
* Yellow: pending review
* Red: changes requested
* Gray: draft

The badge disappears once the pull request merges or closes.

`Cmd+click` (macOS) or `Ctrl+click` (Windows/Linux) the link to open the pull request in your browser.

The status refreshes as soon as a `git push`, or a `gh pr` command that changes the pull request, such as `gh pr create` or `gh pr merge`, succeeds in the session.

Claude Code renders the badge as a hyperlink even when it can't detect hyperlink support in your terminal, which commonly happens over SSH or in tmux. Set [`FORCE_HYPERLINK=0`](/docs/en/env-vars) to render the badge as plain text.

When you set [`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`](/docs/en/env-vars), Claude Code doesn't check pull request or merge request status.

<Note>
  PR status for GitHub repositories needs a GitHub token. Claude Code finds one based on the remote's host:

  * **github.com**: `GH_TOKEN` or `GITHUB_TOKEN`, or the token saved by `gh auth login`. Without one, the footer shows `install gh for PR status` when the `gh` CLI isn't installed, or `gh auth login for PR status` when it is
  * **A GitHub Enterprise host set as `GH_HOST`**: `GH_ENTERPRISE_TOKEN` or `GITHUB_ENTERPRISE_TOKEN`, or the token saved by `gh auth login --hostname <host>`. Without one, the footer shows the same hints
  * **Any other GitHub host**: the token saved by `gh auth login --hostname <host>`. Without one, Claude Code shows no badge and no hint
</Note>

### GitLab merge requests

When you work on a branch with an open GitLab merge request, Claude Code shows a clickable `MR !N` badge in the footer slot that otherwise holds the GitHub PR link. `!N` is GitLab's own reference syntax for merge request number N. The colored underline shows the merge request's state:

* Green: GitLab reports the merge request as mergeable
* Yellow: any other open state
* Gray: draft

The badge disappears once the merge request merges or closes.

It refreshes as soon as a `git push`, or a `glab mr` command that changes the merge request, such as `glab mr create` or `glab mr merge`, succeeds in the session.

To get the badge, you need:

* Claude Code v2.1.234 or later
* A repository remote that points at your GitLab host, either gitlab.com or a self-managed instance
* The [`glab` CLI](https://gitlab.com/gitlab-org/cli) on your `PATH`, authenticated with `glab auth login`

Claude Code ignores `glab`'s token environment variables, such as `GITLAB_TOKEN`, when it checks status, so you get no badge from an exported token alone. Claude Code also looks for `glab` and for its login once per session, so restart Claude Code after you install `glab` or run `glab auth login`.

## Issue reference links

When Claude mentions an issue as `owner/repo#123`, you can click the reference to open it, as long as your terminal supports hyperlinks. If Claude Code doesn't detect hyperlink support in your terminal, set [`FORCE_HYPERLINK`](/docs/en/env-vars) to `1` to turn the links on, or to `0` to keep references as plain text.

You get a link only for the two-part `owner/repo#123` form. These stay plain text:

* A bare `#123`
* A nested GitLab path such as `group/subgroup/project#123`
* Any reference inside a code span or code block

Claude Code builds the link for the host of the repository it identifies from your git remote, not for the repository the reference names:

| Your repository's host                                             | Where `owner/repo#123` links                 |
| :----------------------------------------------------------------- | :------------------------------------------- |
| github.com, a GitHub Enterprise host, or any host not listed below | `https://<host>/owner/repo/issues/123`       |
| gitlab.com                                                         | `https://gitlab.com/owner/repo/-/issues/123` |
| bitbucket.org, codeberg.org, or gitea.com                          | No link; the reference stays plain text      |

## See also

* [Skills](/docs/en/skills) - Custom prompts and workflows
* [Checkpointing](/docs/en/checkpointing) - Rewind Claude's edits and restore previous states
* [CLI reference](/docs/en/cli-reference) - Command-line flags and options
* [Settings](/docs/en/settings) - Configuration options
* [Memory management](/docs/en/memory) - Managing CLAUDE.md files

---

## Plugins reference

- 官方原文：https://code.claude.com/docs/en/plugins-reference.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-plugins-reference.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins reference

> Complete technical reference for Claude Code plugin system, including schemas, CLI commands, and component specifications.

<Tip>
  Looking to install plugins? See [Discover and install plugins](/docs/en/discover-plugins). For creating plugins, see [Plugins](/docs/en/plugins). For distributing plugins, see [Plugin marketplaces](/docs/en/plugin-marketplaces).
</Tip>

A **plugin** is a self-contained directory of components that extends Claude Code with custom functionality. Plugin components include skills, agents, hooks, MCP servers, LSP servers, and monitors.

## Plugin components reference

### Skills

Plugins add skills to Claude Code, creating `/name` shortcuts that you or Claude can invoke.

**Location**: `skills/` or `commands/` directory in plugin root, or a single `SKILL.md` file at the plugin root

**File format**: Skills are directories with `SKILL.md`; commands are simple markdown files

**Skill structure**:

```text theme={null}
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (optional)
│   └── scripts/ (optional)
└── code-reviewer/
    └── SKILL.md
```

Skills and commands are automatically discovered when the plugin is installed.

If a plugin has no `skills/` directory and no `skills` manifest field, a `SKILL.md` at the plugin root is loaded as a single skill. Set the frontmatter `name` field to control the skill's invocation name. Without it, Claude Code falls back to the install directory name. For a plugin [copied into the cache](#plugin-caching-and-file-resolution), that name is a version string that changes on every update. For plugins that ship more than one skill, use the `skills/` directory layout shown above.

In plugin skills and commands, Boolean frontmatter fields such as `disable-model-invocation` accept `yes`, `no`, `on`, `off`, `1`, and `0` in any letter case, in addition to `true` and `false`. Before v2.1.218, Claude Code recognized only `true` and `false`.

For complete details, see [Skills](/docs/en/skills).

### Agents

Plugins can provide specialized subagents for specific tasks that Claude can invoke automatically when appropriate.

**Location**: `agents/` directory in plugin root

**File format**: Markdown files describing agent capabilities

**Agent structure**:

```markdown theme={null}
---
name: agent-name
description: What this agent specializes in and when Claude should invoke it
model: sonnet
effort: medium
maxTurns: 20
disallowedTools: Write, Edit
---

Detailed system prompt for the agent describing its role, expertise, and behavior.
```

#### Plugin agent frontmatter

A plugin agent file uses the same [frontmatter fields as a subagent file](/docs/en/sub-agents#supported-frontmatter-fields), except that Claude Code honors only some of them when the agent comes from a plugin:

* **Supported**: `name`, `description`, `model`, `effort`, `maxTurns`, `tools`, `disallowedTools`, `skills`, `memory`, `background`, `omitClaudeMd`, `isolation`, `color`, and `experimental`. The only valid `isolation` value is `"worktree"`.
* **Not supported, for security reasons**: `hooks`, `mcpServers`, and `permissionMode`. Claude Code ignores these when loading an agent from a plugin. To use them, copy the agent file into `.claude/agents/` or `~/.claude/agents/`.
* **Not supported**: `initialPrompt`.

You can put plugin agent files in subfolders of `agents/`. Claude Code [loads them recursively](/docs/en/sub-agents#choose-the-subagent-scope) and joins the plugin name, each subfolder name, and the file name with colons to form the agent's scoped name. For example, `agents/review/security.md` in a plugin named `my-plugin` loads as `my-plugin:review:security`. Two settings change that name:

* Frontmatter `name`: it replaces only the file name, so `name: audit` in `agents/review/security.md` loads as `my-plugin:review:audit`
* Manifest [`agents`](#component-path-fields) field: a file you list there loads without subfolder names, so `"agents": "./custom/review/security.md"` loads as `my-plugin:security`

Claude Code loads a plugin agent even when its frontmatter has no `name` or doesn't parse:

* No `name`: Claude Code names the agent after the file, so `agents/reviewer.md` in a plugin named `my-plugin` loads as `my-plugin:reviewer`
* Frontmatter that doesn't parse: Claude Code names the agent after the file, uses `Agent from my-plugin plugin` as its description, and ignores every field in the file

By contrast, Claude Code skips a project, user, or managed agent file whose frontmatter has no `name` or doesn't parse.

To find files in a plugin's default `agents/` directory whose frontmatter doesn't parse, run `claude plugin validate`. The path you pass depends on whether the plugin has a manifest, and both examples use `./my-plugin` as the plugin directory:

* A plugin with a manifest: `claude plugin validate ./my-plugin`
* A plugin without a manifest: `claude plugin validate ./my-plugin/agents`. Requires Claude Code v2.1.233 or later.

Agents appear in the [@-mention typeahead](/docs/en/sub-agents#invoke-subagents-explicitly) under their scoped name, such as `my-plugin:code-reviewer`, once the plugin is enabled.

For complete details, see [Subagents](/docs/en/sub-agents).

### Hooks

Plugins can provide event handlers that respond to Claude Code events automatically.

**Location**: `hooks/hooks.json` in plugin root, or inline in plugin.json

**Format**: JSON configuration with event matchers and actions

`hooks/hooks.json` can carry a top-level `$schema` key that names a JSON Schema URL for editor autocomplete and validation. Claude Code ignores the key at load time.

**Hook configuration**:

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

Plugin hooks respond to the same lifecycle events as [user-defined hooks](/docs/en/hooks):

| Event                 | When it fires                                                                                                                                                                                                                                         |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SessionStart`        | When a session begins or resumes                                                                                                                                                                                                                      |
| `Setup`               | When you start Claude Code with `--init-only`, or with `--init` or `--maintenance` in `-p` mode. For one-time preparation in CI or scripts                                                                                                            |
| `UserPromptSubmit`    | When you submit a prompt, before Claude processes it                                                                                                                                                                                                  |
| `UserPromptExpansion` | When a user-typed command expands into a prompt, before it reaches Claude. Can block the expansion                                                                                                                                                    |
| `PreToolUse`          | Before a tool call executes. Can block it                                                                                                                                                                                                             |
| `PermissionRequest`   | When a tool call needs a permission decision                                                                                                                                                                                                          |
| `PermissionDenied`    | When auto mode denies a tool call, including denials without a classifier verdict. Use JSON `hookSpecificOutput.retry: true` to tell the model it may retry the denied tool call. Claude Code ignores `retry` when the classifier produced no verdict |
| `PostToolUse`         | After a tool call succeeds                                                                                                                                                                                                                            |
| `PostToolUseFailure`  | After a tool call fails                                                                                                                                                                                                                               |
| `PostToolBatch`       | After a full batch of parallel tool calls resolves, before the next model call                                                                                                                                                                        |
| `Notification`        | When Claude Code sends a notification                                                                                                                                                                                                                 |
| `MessageDisplay`      | While assistant message text is displayed                                                                                                                                                                                                             |
| `SubagentStart`       | When a subagent is spawned                                                                                                                                                                                                                            |
| `SubagentStop`        | When a subagent finishes                                                                                                                                                                                                                              |
| `TaskCreated`         | When a task is being created via `TaskCreate`                                                                                                                                                                                                         |
| `TaskCompleted`       | When a task is being marked as completed                                                                                                                                                                                                              |
| `Stop`                | When Claude finishes responding                                                                                                                                                                                                                       |
| `StopFailure`         | When the turn ends due to an API error                                                                                                                                                                                                                |
| `TeammateIdle`        | When an [agent team](/docs/en/agent-teams) teammate is about to go idle                                                                                                                                                                                    |
| `InstructionsLoaded`  | When a CLAUDE.md or `.claude/rules/*.md` file is loaded into context. Fires at session start and when files are lazily loaded during a session                                                                                                        |
| `ConfigChange`        | When a configuration file changes during a session                                                                                                                                                                                                    |
| `CwdChanged`          | When the working directory changes, for example when Claude executes a `cd` command. Useful for reactive environment management with tools like direnv                                                                                                |
| `DirectoryAdded`      | When a working directory is added mid-session via `/add-dir` or the SDK `register_repo_root` control request                                                                                                                                          |
| `FileChanged`         | When a watched file changes on disk. The `matcher` field specifies which filenames to watch                                                                                                                                                           |
| `WorktreeCreate`      | When a worktree is being created via `--worktree`, `isolation: "worktree"`, or for a background session. Replaces default git behavior                                                                                                                |
| `WorktreeRemove`      | When a worktree is being removed at session exit, when a subagent finishes, or when you delete a background session                                                                                                                                   |
| `PreCompact`          | Before context compaction                                                                                                                                                                                                                             |
| `PostCompact`         | After context compaction completes                                                                                                                                                                                                                    |
| `PreModelSwitch`      | Before Claude Code applies a model switch that you or a client requested. Can block the switch                                                                                                                                                        |
| `PostModelSwitch`     | After the session's model changes, including changes Claude Code makes on its own, such as restoring the model when you resume a session                                                                                                              |
| `Elicitation`         | When an MCP server requests user input during a tool call                                                                                                                                                                                             |
| `ElicitationResult`   | After a user responds to an MCP elicitation, before the response is sent back to the server                                                                                                                                                           |
| `SessionEnd`          | When a session terminates                                                                                                                                                                                                                             |

**Hook types**:

* `command`: execute shell commands or scripts
* `http`: send the event JSON as a POST request to a URL
* `mcp_tool`: call a tool on a configured [MCP server](/docs/en/mcp)
* `prompt`: evaluate a prompt with an LLM (uses `$ARGUMENTS` placeholder for context)
* `agent`: run an agentic verifier with tools for complex verification tasks

Hooks that target the plugin's own [bundled MCP server](#mcp-servers) must use its scoped names. Tool matchers and `if` fields take the scoped tool name `mcp__plugin_<plugin-name>_<server-name>__<tool>`, and an `mcp_tool` hook's `server` field takes `plugin:<plugin-name>:<server-name>`. A matcher written against the bare server key never fires. See [Match MCP tools](/docs/en/hooks#match-mcp-tools) and [Plugin-provided MCP servers](/docs/en/mcp#plugin-provided-mcp-servers).

### MCP servers

Plugins can bundle Model Context Protocol (MCP) servers to connect Claude Code with external tools and services.

**Location**: `.mcp.json` in plugin root, or inline in plugin.json

**Format**: Standard MCP server configuration

**MCP server configuration**:

```json theme={null}
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"]
    }
  }
}
```

**Integration behavior**:

* Plugin MCP servers start automatically when the plugin is enabled
* Servers appear as standard MCP tools in Claude's toolkit
* Plugin servers can be configured independently of user MCP servers
* If you run [`/reload-plugins`](/docs/en/discover-plugins#apply-plugin-changes-without-restarting) mid-session, Claude Code keeps the live connections of servers whose configuration is unchanged

### LSP servers

<Tip>
  Looking to use LSP plugins? Install them from the official marketplace: search for "lsp" in the `/plugin` Discover tab. This section documents how to create LSP plugins for languages not covered by the official marketplace.
</Tip>

Plugins can provide [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP) servers to give Claude [real-time code intelligence](/docs/en/discover-plugins#code-intelligence) while working on your codebase.

**Location**: `.lsp.json` in plugin root, or inline in `plugin.json`

**Format**: JSON configuration mapping language server names to their configurations

**`.lsp.json` file format**:

```json theme={null}
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**Inline in `plugin.json`**:

```json theme={null}
{
  "name": "my-plugin",
  "lspServers": {
    "go": {
      "command": "gopls",
      "args": ["serve"],
      "extensionToLanguage": {
        ".go": "go"
      }
    }
  }
}
```

**Required fields:**

| Field                 | Description                                  |
| :-------------------- | :------------------------------------------- |
| `command`             | The LSP binary to execute (must be in PATH)  |
| `extensionToLanguage` | Maps file extensions to language identifiers |

**Optional fields:**

| Field                   | Description                                                                                                                                                              |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `args`                  | Command-line arguments for the LSP server                                                                                                                                |
| `transport`             | Communication transport: `stdio` (default) or `socket`. Claude Code accepts `socket` but runs every server over stdio, so the stdout protocol rules apply to all servers |
| `env`                   | Environment variables to set when starting the server                                                                                                                    |
| `initializationOptions` | Options passed to the server during initialization                                                                                                                       |
| `settings`              | Settings passed via `workspace/didChangeConfiguration`                                                                                                                   |
| `workspaceFolder`       | Workspace folder path for the server                                                                                                                                     |
| `startupTimeout`        | Max time to wait for server startup (milliseconds)                                                                                                                       |
| `shutdownTimeout`       | Max time to wait for graceful shutdown (milliseconds). When the timeout elapses, Claude Code terminates the server process. When unset, no timeout applies               |
| `restartOnCrash`        | Whether to restart the server after it crashes. Defaults to `true`. Set to `false` to leave a crashed server stopped instead of restarting it                            |
| `maxRestarts`           | Maximum number of restart attempts before giving up                                                                                                                      |
| `diagnostics`           | Whether to push diagnostics into Claude's context after edits (default `true`). Set to `false` to keep code navigation but suppress automatic diagnostic injection.      |

`restartOnCrash` and `shutdownTimeout` require Claude Code v2.1.205 or later. Before v2.1.205, the config schema accepted both options but setting either one caused Claude Code to skip that LSP server entirely at startup, with the reason visible only in `claude --debug` output.

**Multiple servers for the same extension**: when more than one enabled LSP server declares the same file extension in `extensionToLanguage`, whether the servers come from one plugin or from different plugins, the first server registered handles files with that extension and the others never start. The `/plugin` interface shows a warning naming the plugin whose server is active.

**Servers that fail to initialize**: Claude Code skips a server whose configuration is invalid, for example one missing `command` or `extensionToLanguage`, and the other configured servers still start. Run `claude --debug` to see why a server was skipped.

A skipped server doesn't claim its file extensions, so another valid server that declares the same extension, from the same or a different plugin, still handles those files.

**Send log output to stderr, not stdout**: Claude Code reads a server's stdout as protocol messages only, and accepts message headers up to 64 KiB and a message body up to 32 MiB. Claude Code disconnects a server that exceeds either limit or writes non-protocol output to stdout, and counts the disconnect as a crash for `restartOnCrash` and `maxRestarts`. When you run with `--debug`, Claude Code writes an error naming the cause to the debug log.

<Warning>
  **You must install the language server binary separately.** LSP plugins configure how Claude Code connects to a language server, but they don't include the server itself. If you see `Executable not found in $PATH` in the `/plugin` Errors tab, install the required binary for your language.
</Warning>

**Available LSP plugins:**

| Plugin              | Language server            | Install command                                                                            |
| :------------------ | :------------------------- | :----------------------------------------------------------------------------------------- |
| `pyright-lsp`       | Pyright (Python)           | `pip install pyright` or `npm install -g pyright`                                          |
| `typescript-lsp`    | TypeScript Language Server | `npm install -g typescript-language-server typescript`                                     |
| `rust-analyzer-lsp` | rust-analyzer              | [See rust-analyzer installation](https://rust-analyzer.github.io/manual.html#installation) |

Install the language server first, then install the plugin from the marketplace.

### Monitors

Plugins can declare background monitors that Claude Code starts automatically when the plugin is active. Each monitor runs a shell command for the lifetime of the session and delivers every stdout line to Claude as a notification, so Claude can react to log entries, status changes, or polled events without being asked to start the watch itself.

Plugin monitors use the same mechanism as the [Monitor tool](/docs/en/tools-reference#monitor-tool) and share its availability constraints. They run only in interactive CLI sessions, run unsandboxed at the same trust level as [hooks](#hooks), and are skipped on hosts where the Monitor tool is unavailable.

**Location**: `monitors/monitors.json` in the plugin root, or inline in `plugin.json`

**Format**: JSON array of monitor entries

The following `monitors/monitors.json` watches a deployment status endpoint and a local error log:

```json theme={null}
[
  {
    "name": "deploy-status",
    "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/poll-deploy.sh",
    "description": "Deployment status changes"
  },
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log",
    "when": "on-skill-invoke:debug"
  }
]
```

To declare monitors inline, set `experimental.monitors` in `plugin.json` to the same array. To load from a non-default path, set `experimental.monitors` to a relative path string such as `"./config/monitors.json"`. Monitors are an [experimental component](#experimental-components).

**Required fields:**

| Field         | Description                                                                                                           |
| :------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `name`        | Identifier unique within the plugin. Prevents duplicate processes when the plugin reloads or a skill is invoked again |
| `command`     | Shell command run as a persistent background process in the session working directory                                 |
| `description` | Short summary of what is being watched. Shown in the task panel and in notification summaries                         |

**Optional fields:**

| Field  | Description                                                                                                                                                                                                              |
| :----- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `when` | Controls when the monitor starts. `"always"` starts it at session start and on plugin reload, and is the default. `"on-skill-invoke:<skill-name>"` starts it the first time the named skill in this plugin is dispatched |

The `command` value supports the [path substitutions](#environment-variables) `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, and `${CLAUDE_PROJECT_DIR}`, plus any `${ENV_VAR}` from the environment. Prefix the command with `cd "${CLAUDE_PLUGIN_ROOT}" && ` if the script needs to run from the plugin's own directory.

A monitor `command` can't reference [`${user_config.*}`](#user-configuration) values. The command runs through a shell, so Claude Code rejects the monitor with an [error](/docs/en/errors#plugin-command-references-user-config) instead of substituting the value. Monitor processes don't receive `CLAUDE_PLUGIN_OPTION_<KEY>` environment variables, so have the monitor script read the value from a config file it owns.

If you disable a plugin mid-session, Claude Code doesn't stop monitors that are already running; they stop when the session ends.

### Themes

Plugins can ship color themes that appear in `/theme` alongside the built-in presets and the user's local themes. A theme is a JSON file in `themes/` with a `base` preset and a sparse `overrides` map of color tokens. Themes are an [experimental component](#experimental-components).

```json theme={null}
{
  "name": "Dracula",
  "base": "dark",
  "overrides": {
    "claude": "#bd93f9",
    "error": "#ff5555",
    "success": "#50fa7b"
  }
}
```

When a user selects a plugin theme, Claude Code saves `custom:<plugin-name>:<slug>` in their config. Plugin themes are read-only: when a user presses `Ctrl+E` on one in `/theme`, Claude Code copies it into `~/.claude/themes/` so they can edit the copy.

***

## Plugin installation scopes

When you install a plugin, you choose a **scope** that determines where the plugin is available and who else can use it:

| Scope     | Settings file                            | Use case                                                                    |
| :-------- | :--------------------------------------- | :-------------------------------------------------------------------------- |
| `user`    | `~/.claude/settings.json`                | Personal plugins available across all projects (default)                    |
| `project` | `.claude/settings.json`                  | Team plugins shared via version control                                     |
| `local`   | `.claude/settings.local.json`            | Project-specific plugins, gitignored when Claude Code saves a setting to it |
| `managed` | [Managed settings](/docs/en/managed-settings) | Managed plugins (read-only, update only)                                    |

Plugins use the same scope system as other Claude Code configurations. For installation instructions and scope flags, see [Install plugins](/docs/en/discover-plugins#install-plugins). For a complete explanation of scopes, see [Configuration scopes](/docs/en/settings#where-settings-live).

***

## Skills-directory plugins

Any folder under a skills directory that contains a `.claude-plugin/plugin.json` manifest is loaded as a plugin named `<name>@skills-dir` on the next session, with no marketplace and no install step. Scaffold one with [`plugin init`](#plugin-init). Unlike a copied marketplace install, the plugin is discovered in place rather than copied into the plugin cache.

A skills directory tree supports three distinct things:

| What you have                                 | What it is                                                                          |
| :-------------------------------------------- | :---------------------------------------------------------------------------------- |
| `<skills-dir>/foo/SKILL.md` with no manifest  | A plain [skill](/docs/en/skills) named `foo`                                             |
| `<skills-dir>/foo/.claude-plugin/plugin.json` | A plugin `foo@skills-dir`, which can bundle its own skills, agents, hooks, and more |
| `<plugin>/skills/bar/SKILL.md`                | A skill `bar` packaged inside a plugin                                              |

### Choose where the plugin loads from

| Skills directory        | Scope    | Loads                                                                                                                   |
| :---------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| `~/.claude/skills/`     | personal | In every project, since the location is yours alone                                                                     |
| `<cwd>/.claude/skills/` | project  | Only after you accept the workspace [trust dialog](/docs/en/permissions#what-runs-before-you-trust-a-folder) for that folder |

A project-scope plugin is checked into the repository and reaches every collaborator who clones it. Because that content comes from the repository rather than from you, it loads only after the same trust gate that governs project allow rules in `.claude/settings.json`, so trusting a parent folder or running with `-p` isn't enough, and components that run code are restricted further:

* MCP servers it declares go through the [same per-server approval](/docs/en/mcp) as a project `.mcp.json`
* LSP servers start only after you trust the workspace
* [Background monitors](#monitors) do not load

Personal-scope plugins have none of these restrictions.

<Warning>
  Project-scope `@skills-dir` plugins load only from the `.claude/skills/` of the session's [primary working directory](/docs/en/permissions#working-directories). They don't [walk up to the repository root](/docs/en/skills#discovery-from-parent-and-nested-directories) the way plain skills and commands do, so launching from a subdirectory misses a plugin that lives at the repo root. Launch from the repository root, or [move the session there with `/cd`](/docs/en/permissions#move-the-session-to-another-directory) on v2.1.246 or later.
</Warning>

### Edit, reload, and disable a skills-directory plugin

Changes you make to a skill's `SKILL.md` take effect immediately in the current session. Changes to the plugin's other components, such as `hooks/`, `.mcp.json`, `agents/`, and `output-styles/`, do not. Run `/reload-plugins` or restart Claude Code to pick those up. See [Live change detection](/docs/en/skills#live-change-detection).

To stop loading a skills-directory plugin, delete its folder or disable it by name. There is no `uninstall` step because nothing was installed from a marketplace.

```bash theme={null}
claude plugin disable my-tool@skills-dir
```

***

<h2 id="synced-plugins">
  Plugins synced from claude.ai
</h2>

Claude Code loads the plugins enabled for your claude.ai account, including plugins your organization turns on for its members, alongside the plugins you install from marketplaces. It downloads each one into `~/.claude/plugins/synced/` and loads it as `<name>@synced`, with no marketplace and no install record. A synced plugin runs with the same trust as a marketplace plugin you installed: its skills, agents, hooks, MCP servers, and LSP servers all load.

Where Claude Code syncs these plugins depends on the session:

* In [Cowork](https://claude.com/product/cowork) and [cloud sessions](/docs/en/cloud-environments#what-carries-over-from-your-setup), Claude Code downloads them into the session's own environment when the session starts. Before v2.1.239, Claude Code loaded these plugins as `<name>@inline`, the identity that `--plugin-dir` plugins use.
* In terminal sessions where you sign in with your claude.ai account, Claude Code checks your account once each time it starts, then downloads new and updated plugins and removes the ones that you or your organization turned off, all in the background. Syncing in terminal sessions requires Claude Code v2.1.273 or later.

The launch check runs in the background, so it can finish after your session has started. When it adds, updates, or removes a synced plugin in an interactive session, Claude Code shows `Plugins changed. Run /reload-plugins to activate.` Run [`/reload-plugins`](/docs/en/discover-plugins#apply-plugin-changes-without-restarting) to load the change in that session, or leave it for the next time you start Claude Code. If you enable a plugin on claude.ai while a session is running, Claude Code downloads it the next time it starts.

Plugin sync in terminal sessions runs under the same sign-in conditions as [skills synced from claude.ai](/docs/en/skills#where-synced-skills-load). It also needs a sign-in that grants Claude Code access to your account's plugins.

A sign-in from an earlier version of Claude Code picks up plugin access the next time Claude Code renews that sign-in in the background, within a few hours, or right away if you run `/login` again. Plugin sync starts the next time you start Claude Code after that.

`claude plugin list` shows synced plugins under a `Synced from claude.ai` heading, and the `/plugin` **Installed** tab lists them with `synced` as their source. Manage a synced plugin by the `<name>@synced` ID that `claude plugin list` prints:

* **Turn one off**: run `claude plugin disable <name>@synced`, or disable it from the `/plugin` **Installed** tab. Claude Code saves the choice as `"<name>@synced": false` in your user-level [`enabledPlugins`](/docs/en/settings-reference#enabledplugins). To turn the plugin back on, run `claude plugin enable <name>@synced`.
* **Keep one out everywhere**: [turn the plugin off for your claude.ai account](/docs/en/desktop#extend-claude-code). To keep it out of one project in every environment, set `"<name>@synced": false` under `enabledPlugins` in that project's committed `.claude/settings.json`.
* **Manage the plugin itself on claude.ai**: `claude plugin install`, `update`, and `uninstall` don't apply to a synced plugin. Claude Code downloads a plugin's updates at the next sync. To remove one, turn the plugin off for your claude.ai account, and Claude Code removes it at the next sync.
* **Stop syncing on a machine**: set [`syncClaudeAiPlugins`](/docs/en/settings-reference#syncclaudeaiplugins) to `false` in your user settings. Claude Code stops downloading, and the next time it starts it moves the plugins it already synced to `~/.claude/plugins/.trash/` and no longer loads them. Your organization can set the same key in [managed settings](/docs/en/managed-settings), or turn off Skills on claude.ai, which stops plugins from syncing too.

You can't turn off a plugin that your organization marks as required on claude.ai. Claude Code loads it even if you disabled it earlier, and `claude plugin disable` refuses with `Plugin "<name>@synced" is required by your organization and can't be disabled here. Contact your admin to change it.` In `claude plugin list`, these plugins are marked `required by your org`.

When an enabled plugin from any other source matches a synced plugin's name, Claude Code loads that plugin and reports the synced copy as not loaded. Other sources include marketplace installs, [skills-directory plugins](#skills-directory-plugins), `--plugin-dir` plugins, and plugins built into Claude Code. To use the claude.ai copy instead, disable your own copy. Before v2.1.239, Claude Code loaded the synced copy instead of a same-named marketplace install.

***

## Plugin manifest schema

The `.claude-plugin/plugin.json` file defines your plugin's metadata and configuration.

The manifest is optional. If omitted, Claude Code auto-discovers components in [default locations](#file-locations-reference) and derives the plugin name from the directory name. Use a manifest when you need to provide metadata or custom component paths.

### Complete schema

```json theme={null}
{
  "name": "plugin-name",
  "displayName": "Plugin Name",
  "version": "1.2.0",
  "description": "Brief plugin description",
  "author": {
    "name": "Author Name",
    "email": "author@example.com",
    "url": "https://github.com/author"
  },
  "homepage": "https://docs.example.com/plugin",
  "repository": "https://github.com/author/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "metadata": { "catalogId": "cat-123", "tier": "pro" },
  "skills": "./custom/skills/",
  "commands": ["./custom/commands/special.md"],
  "agents": ["./custom/agents/reviewer.md"],
  "hooks": "./config/hooks.json",
  "mcpServers": "./mcp-config.json",
  "outputStyles": "./styles/",
  "lspServers": "./.lsp.json",
  "experimental": {
    "themes": "./themes/",
    "monitors": "./monitors.json",
    "evals": "quality/evals"
  },
  "dependencies": [
    "helper-lib",
    { "name": "secrets-vault", "version": "~2.1.0" }
  ]
}
```

### Required fields

If you include a manifest, `name` is the only required field.

| Field  | Type   | Description                                                                                                                                                                                                                                                                                         | Example              |
| :----- | :----- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- |
| `name` | string | Unique identifier in kebab-case, with no spaces, control characters, or bidirectional-formatting characters. When a [marketplace entry](/docs/en/plugin-marketplaces#plugin-entries) lists the plugin under a different name, the marketplace entry name is what `enabledPlugins` keys and `/plugin` use | `"deployment-tools"` |

This name is used for namespacing components. For example, in the UI, the
agent `agent-creator` for the plugin with name `plugin-dev` will appear as
`plugin-dev:agent-creator`.

### Unrecognized fields

Claude Code ignores top-level fields it does not recognize. You can keep
metadata from another ecosystem in `plugin.json` and the plugin still loads.
This makes it practical to maintain one manifest that doubles as a VS Code or
Cursor extension manifest, an npm `package.json`, or an MCPB/DXT bundle
manifest.

`claude plugin validate` reports unrecognized fields as warnings, not errors.
If a field is one or two characters off from a recognized one, the warning
suggests the likely intended name. A plugin with only unrecognized-field
warnings still passes validation and loads at runtime.

How Claude Code handles a recognized field whose value has the wrong type depends on the field:

* **Most fields**: the plugin fails to load. For example, a `keywords` value that is a string instead of an array is a load error, and `claude plugin validate` reports it as one.
* **`experimental` and `metadata`**: Claude Code ignores a non-object value, and `claude plugin validate` reports a warning.

Pass `--strict` to treat warnings as errors. Use it in CI to catch a misspelled
field name or a field left over from another tool's manifest before publishing,
even though the plugin would load at runtime.

```bash theme={null}
claude plugin validate ./my-plugin --strict
```

### Metadata fields

| Field            | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Example                                                           |
| :--------------- | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| `$schema`        | string  | JSON Schema URL for editor autocomplete and validation. Claude Code ignores this field at load time.                                                                                                                                                                                                                                                                                                                                                                                    | `"https://json.schemastore.org/claude-code-plugin-manifest.json"` |
| `displayName`    | string  | Human-readable name shown in the `/plugin` picker and other UI surfaces. For a marketplace-installed plugin, a `displayName` on the [marketplace entry](/docs/en/plugin-marketplaces#optional-plugin-fields) takes precedence over this value. When no display name is set in either place, users see `name`. Unlike `name`, may contain spaces and any casing. Not used for namespacing or lookup.                                                                                          | `"Deployment Tools"`                                              |
| `version`        | string  | Optional. Semantic version. Setting this pins the plugin to that version string, so users only receive updates when you bump it, except for a [`command` source](/docs/en/plugin-marketplaces#command-sources) or a plugin [loaded in place](#plugin-caching-and-file-resolution); see [Version management](#version-management). If also set in the marketplace entry, `plugin.json` wins. If omitted, the version comes from the next source in [Version management](#version-management). | `"2.1.0"`                                                         |
| `description`    | string  | Brief explanation of plugin purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `"Deployment automation tools"`                                   |
| `author`         | object  | Author information                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `{"name": "Dev Team", "email": "dev@company.com"}`                |
| `homepage`       | string  | Documentation URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `"https://docs.example.com"`                                      |
| `repository`     | string  | Source code URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `"https://github.com/user/plugin"`                                |
| `license`        | string  | License identifier                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `"MIT"`, `"Apache-2.0"`                                           |
| `keywords`       | array   | Discovery tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `["deployment", "ci-cd"]`                                         |
| `metadata`       | object  | Free-form object for your own data, such as entitlement or catalog fields. Claude Code doesn't read it, so the values never affect plugin behavior. Claude Code ignores a non-object value, and `claude plugin validate` reports it as a warning. Before v2.1.222, Claude Code treated the key as an [unrecognized field](#unrecognized-fields).                                                                                                                                        | `{"catalogId": "cat-123"}`                                        |
| `defaultEnabled` | boolean | Whether the plugin starts in an enabled state when the user has not set one. Defaults to `true`. See [Default enablement](#default-enablement).                                                                                                                                                                                                                                                                                                                                         | `false`                                                           |

### Default enablement

Set `defaultEnabled: false` in `plugin.json` to ship a plugin that installs disabled. The user turns it on with `claude plugin enable <plugin>` or the `/plugin` interface. Use this for plugins that add cost or scope a user should opt into, such as one that connects to an external service.

`defaultEnabled` is the fallback when nothing else has decided the plugin's state. The user's setting and a dependency requirement take precedence over it:

* **The user's setting**: an entry for the plugin in `enabledPlugins` at any settings scope. Once written, it persists across plugin updates and reinstalls, so changing `defaultEnabled` in a later release does not flip an existing user.
* **A dependency requirement**: when a plugin is required by another one that is active, Claude Code writes `true` for it at install or enable time. That gives it an explicit setting, so its own default no longer applies. See [Enable or disable a plugin with dependencies](/docs/en/plugin-dependencies#enable-or-disable-a-plugin-with-dependencies).

The same field can appear in a plugin's marketplace entry, where it takes precedence over the value in `plugin.json`. See [Optional plugin fields](/docs/en/plugin-marketplaces#optional-plugin-fields).

### Component path fields

| Field                   | Type                  | Description                                                                                                                                                                                             | Example                                              |
| :---------------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------- |
| `skills`                | string\|array         | Custom skill directories containing `<name>/SKILL.md`. Adds to the default `skills/` scan. See [Path behavior rules](#path-behavior-rules) for the marketplace-root exception                           | `"./custom/skills/"`                                 |
| `commands`              | string\|array         | Custom flat `.md` skill files or directories (replaces default `commands/`)                                                                                                                             | `"./custom/cmd.md"` or `["./cmd1.md"]`               |
| `agents`                | string\|array         | Custom agent files (replaces default `agents/`)                                                                                                                                                         | `"./custom/agents/reviewer.md"`                      |
| `workflows`             | string\|array         | Custom [workflow](/docs/en/workflows) script files or directories (replaces default `workflows/`)                                                                                                            | `"./custom/workflows/"`                              |
| `hooks`                 | string\|array\|object | Hook config paths or inline config                                                                                                                                                                      | `"./my-extra-hooks.json"`                            |
| `mcpServers`            | string\|array\|object | MCP config paths or inline config                                                                                                                                                                       | `"./my-extra-mcp-config.json"`                       |
| `outputStyles`          | string\|array         | Custom output style files/directories (replaces default `output-styles/`)                                                                                                                               | `"./styles/"`                                        |
| `lspServers`            | string\|array\|object | [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) configs for code intelligence (go to definition, find references, etc.)                                               | `"./.lsp.json"`                                      |
| `experimental.themes`   | string\|array         | Color theme files/directories (replaces default `themes/`). See [Themes](#themes)                                                                                                                       | `"./themes/"`                                        |
| `experimental.monitors` | string\|array         | Background [Monitor](/docs/en/tools-reference#monitor-tool) configurations that start automatically when the plugin is active. See [Monitors](#monitors)                                                     | `"./monitors.json"`                                  |
| `experimental.evals`    | string\|array         | Directory below the plugin root that holds the plugin's [eval cases](/docs/en/plugin-evals#use-a-different-eval-directory), when it isn't the default `evals/`. `claude plugin eval --eval-dir` overrides it | `"quality/evals"`                                    |
| `userConfig`            | object                | User-configurable values prompted at enable time. See [User configuration](#user-configuration)                                                                                                         |                                                      |
| `channels`              | array                 | Channel declarations for message injection (Telegram, Slack, Discord style). See [Channels](#channels)                                                                                                  |                                                      |
| `dependencies`          | array                 | Other plugins this plugin requires, optionally with semver version constraints. See [Constrain plugin dependency versions](/docs/en/plugin-dependencies)                                                     | `[{ "name": "secrets-vault", "version": "~2.1.0" }]` |

### Experimental components

Components under the `experimental` key, `themes` and `monitors`, have a manifest schema that may change between releases while they stabilize. Where you declare them is a separate migration: the top level still works, `claude plugin validate` warns, and a future release will require `experimental.*`.

### User configuration

The `userConfig` field declares values that Claude Code prompts the user for when the plugin is enabled. Use this instead of requiring users to hand-edit `settings.json`.

```json theme={null}
{
  "userConfig": {
    "api_endpoint": {
      "type": "string",
      "title": "API endpoint",
      "description": "Your team's API endpoint"
    },
    "api_token": {
      "type": "string",
      "title": "API token",
      "description": "API authentication token",
      "sensitive": true
    }
  }
}
```

Keys must be valid identifiers. Each option supports these fields:

| Field         | Required | Description                                                                                                                                                                                              |
| :------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`        | Yes      | One of `string`, `number`, `boolean`, `directory`, or `file`                                                                                                                                             |
| `title`       | Yes      | Label shown in the configuration dialog                                                                                                                                                                  |
| `description` | Yes      | Help text shown beneath the field                                                                                                                                                                        |
| `sensitive`   | No       | If `true`, masks input and stores the value in secure storage instead of `settings.json`                                                                                                                 |
| `required`    | No       | If `true`, validation fails when the field is empty                                                                                                                                                      |
| `default`     | No       | Value used when the user provides nothing                                                                                                                                                                |
| `options`     | No       | For `string` type, the values the field accepts, shown in `/config` as a picker over them. See [Limit a field to fixed options](#limit-a-field-to-fixed-options). Requires Claude Code v2.1.271 or later |
| `multiple`    | No       | For `string` type, allow an array of strings                                                                                                                                                             |
| `min` / `max` | No       | Bounds for `number` type                                                                                                                                                                                 |

Except `sensitive` fields and `multiple` lists, each field of each enabled plugin also appears as a row in the `/config` panel. The rows require Claude Code v2.1.269 or later.

Each value is available for substitution as `${user_config.KEY}` in MCP and LSP server configs and hook commands. Non-sensitive values can also be substituted in skill and agent content. All values are exported to hook processes as `CLAUDE_PLUGIN_OPTION_<KEY>` environment variables, where `<KEY>` is the option key uppercased.

Fields that run in a shell reject `${user_config.*}`: substituting a configured value into a shell command would let the shell run whatever that value contains, so the component fails with an [error](/docs/en/errors#plugin-command-references-user-config) instead. Each rejected field has an alternative way to pass the value:

| Rejected field                                                               | How to pass the value                                                                                                             |
| :--------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| Shell-form hook commands                                                     | Use [exec form](/docs/en/hooks#exec-form-and-shell-form) with `args`, or read `CLAUDE_PLUGIN_OPTION_<KEY>` from the hook's environment |
| [Monitor](#monitors) commands                                                | Read the value from a config file in the script                                                                                   |
| MCP [`headersHelper`](/docs/en/mcp#use-dynamic-headers-for-custom-authentication) | Read the value from a config file in the script                                                                                   |

Before v2.1.207, these fields substituted `${user_config.KEY}` values; update plugins that relied on this.

Non-sensitive values are stored under the [`pluginConfigs`](/docs/en/settings-reference#pluginconfigs) key in your user `settings.json` as `pluginConfigs[<plugin-id>].options`.

On macOS, Claude Code stores sensitive values in the macOS Keychain, falling back to `~/.claude/.credentials.json` when the Keychain rejects the write. On platforms without a supported keychain, it stores them in `~/.claude/.credentials.json`. Keychain storage is shared with OAuth tokens and has an approximately 2 KB total limit, so keep sensitive values small.

Claude Code reads all `pluginConfigs` values from only three settings sources:

* **User settings**: `~/.claude/settings.json`, the file the enable-time prompt writes to
* **`--settings`**: the CLI flag or SDK inline settings
* **Managed settings**: [organization-controlled policy](/docs/en/permissions#managed-settings)

When more than one source sets the same key, managed settings take precedence, then `--settings`, then user settings. The only source you can remove from this list is user settings: pass [`--setting-sources`](/docs/en/cli-reference#cli-flags) without `user` and Claude Code skips them. Managed settings and `--settings` stay whatever you pass. The SDK's [`settingSources`](/docs/en/agent-sdk/claude-code-features#what-settingsources-does-not-control) option sets the same list.

Entries in a project's `.claude/settings.json` or `.claude/settings.local.json` are ignored. Both files live in the workspace, so a cloned repository could supply values there, and those values would flow into plugin hook commands, MCP server configs, LSP commands, and monitor commands. Before v2.1.207, these entries were read. The restriction is specific to `pluginConfigs`: [`enabledPlugins`](/docs/en/settings-reference#enabledplugins) still honors project and local settings.

#### Limit a field to fixed options

Set `options` on a `userConfig` field to make users pick its value from a fixed list.

To limit a `tone` field to three options, list them in `options` and set `default` to one of them:

```json theme={null}
{
  "userConfig": {
    "tone": {
      "type": "string",
      "title": "Tone",
      "description": "Voice for generated replies",
      "options": ["neutral", "warm", "formal"],
      "default": "neutral"
    }
  }
}
```

If you declare `options` on any field, users on Claude Code versions before v2.1.271 can't load the plugin.

When you set `options` on a field, follow these rules:

* Set `type` to `string`
* Don't set `multiple` or `sensitive` to `true`
* Set `default` to one of the options
* If you leave `default` unset, set `required` to `true`
* List at least one option, each 1 to 64 characters long
* Don't start or end an option with a space
* Don't use control characters, invisible characters, characters that change text direction, or spaces other than a regular space in an option
* Don't list the same option twice, even in a different letter case

If you break any of these rules, the plugin fails to load. Run `claude plugin validate` to see which field breaks which rule.

### Channels

The `channels` field lets a plugin declare one or more message channels that inject content into the conversation. Each channel binds to an MCP server that the plugin provides.

```json theme={null}
{
  "channels": [
    {
      "server": "telegram",
      "userConfig": {
        "bot_token": {
          "type": "string",
          "title": "Bot token",
          "description": "Telegram bot token",
          "sensitive": true
        },
        "owner_id": {
          "type": "string",
          "title": "Owner ID",
          "description": "Your Telegram user ID"
        }
      }
    }
  ]
}
```

The `server` field is required and must match a key in the plugin's `mcpServers`. The optional per-channel `userConfig` uses the same schema as the top-level field, letting the plugin prompt for bot tokens or owner IDs when the plugin is enabled.

### Path behavior rules

Whether a custom path replaces or extends the plugin's default directory depends on the field:

* **Replaces the default**: `commands`, `agents`, `workflows`, `outputStyles`, `experimental.themes`, `experimental.monitors`. For example, when the manifest specifies `commands`, the default `commands/` directory is not scanned. To keep the default and add more, list it explicitly: `"commands": ["./commands/", "./extras/"]`
* **Adds to the default**: `skills`. The default `skills/` directory is always scanned, and directories listed in `skills` are loaded alongside it. Exception: for a [marketplace entry whose `source` resolves to the marketplace root](/docs/en/plugin-marketplaces#advanced-plugin-entries), declaring specific subdirectories replaces the default `skills/` scan
* **Own merge rules**: [hooks](#hooks), [MCP servers](#mcp-servers), and [LSP servers](#lsp-servers). See each section for how multiple sources combine

When a plugin has both a default folder and the matching manifest key, Claude Code warns about the ignored folder in `claude plugin list` and the `/plugin` detail view. The plugin still loads using the manifest paths. Claude Code doesn't warn when the manifest key points into the default folder, for example `"commands": ["./commands/deploy.md"]`, because that path names the folder explicitly.

For all path fields:

* All paths must be relative to the plugin root and start with `./`, except that the `skills` field also accepts `"."`
  * Both `"."` and `"./"` denote the plugin root itself
  * Before v2.1.221, `"."` failed manifest validation and the plugin didn't load, so use `"./"` to support earlier versions
* Components from custom paths use the same naming and namespacing rules, except agent files. See [Agents](#agents) for how agent names work
* Multiple paths can be specified as arrays
* A skill path can point to a directory that contains a `SKILL.md` directly, for example `"skills": ["."]` for the plugin root
  * Claude Code takes the skill's invocation name from the frontmatter `name` field in `SKILL.md`, so the name stays stable whatever the install directory is named
  * If `name` isn't set in the frontmatter, Claude Code falls back to the directory basename

A plugin that has a `SKILL.md` at its root, no `skills/` subdirectory, and no `skills` manifest field is automatically loaded as a single-skill plugin. You do not need to set `"skills": ["./"]` in `plugin.json` for this layout.

**Path examples**:

```json theme={null}
{
  "commands": [
    "./specialized/deploy.md",
    "./utilities/batch-process.md"
  ],
  "agents": [
    "./custom-agents/reviewer.md",
    "./custom-agents/tester.md"
  ]
}
```

### Environment variables

Claude Code provides three variables for referencing paths:

| Variable                | Resolves to                                                                                                 | Use it for                                                                                               |
| :---------------------- | :---------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| `${CLAUDE_PLUGIN_ROOT}` | Absolute path to the plugin's installation directory                                                        | Scripts, binaries, and config files bundled with the plugin                                              |
| `${CLAUDE_PLUGIN_DATA}` | [Persistent directory](#persistent-data-directory) that survives plugin updates, created on first reference | Installed dependencies such as `node_modules` or Python virtual environments, generated code, and caches |
| `${CLAUDE_PROJECT_DIR}` | The project root                                                                                            | Project-local scripts and config files                                                                   |

All three are exported as environment variables to hook processes and to MCP and LSP server subprocesses. They aren't present in the environment of commands Claude runs through the Bash tool, in the main session or in a subagent. In plugin content, write the placeholder instead, and Claude Code substitutes the path inline when it loads the content. Which fields substitute them inline depends on the plugin component:

| Plugin component                | Fields where placeholders resolve           |
| :------------------------------ | :------------------------------------------ |
| Skill and agent content         | Anywhere the placeholder appears            |
| Hook and monitor commands       | Anywhere the placeholder appears            |
| MCP `stdio` servers             | `command`, `args`, `env`                    |
| MCP `http`, `sse`, `ws` servers | `url`, `headers`, `headersHelper`           |
| LSP servers                     | `command`, `args`, `env`, `workspaceFolder` |

In hook commands, use [exec form](/docs/en/hooks#exec-form-and-shell-form) with `args` so each path is passed as one argument with no quoting. In shell-form hooks and monitor commands, wrap the variables in double quotes, as in `"${CLAUDE_PROJECT_DIR}/scripts/server.sh"`. This shell-form hook runs a script bundled with a plugin:

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/process.sh"
          }
        ]
      }
    ]
  }
}
```

For a copied plugin, `${CLAUDE_PLUGIN_ROOT}` changes when the plugin updates. The previous version's directory remains on disk for a grace period after an update, but treat it as ephemeral and don't write state there. For a plugin loaded in place from a local-directory marketplace, the variable points at the stable source directory. See [plugin caching](#plugin-caching-and-file-resolution) for which plugins are copied and for cleanup semantics.

When a copied plugin updates mid-session, hook commands, monitors, MCP servers, and LSP servers keep using the previous version's path. Run `/reload-plugins` to switch hooks, MCP servers, and LSP servers to the new path; monitors require a session restart. In a session without an interactive terminal, the reload leaves plugin MCP servers on the old path until the next session.

For a plugin with a `command` source, Claude Code [can reload the plugin itself](/docs/en/plugin-marketplaces#when-claude-code-re-runs-the-command).

MCP servers can also call the `roots/list` request to read the session's working directories at runtime. See [what `roots/list` returns and when Claude Code notifies the server of changes](/docs/en/mcp#option-3-add-a-local-stdio-server).

#### Persistent data directory

The `${CLAUDE_PLUGIN_DATA}` directory resolves to `~/.claude/plugins/data/{id}/`, where `{id}` is the plugin identifier with characters outside `a-z`, `A-Z`, `0-9`, `_`, and `-` replaced by `-`. For a plugin installed as `formatter@my-marketplace`, the directory is `~/.claude/plugins/data/formatter-my-marketplace/`.

A common use is installing language dependencies once and reusing them across sessions and plugin updates. Use it for Python dependencies, dependencies locked with Yarn or pnpm, and packages whose lifecycle scripts must run. For a marketplace-installed plugin, you may not need it at all: Claude Code installs eligible [Node.js package dependencies](#node-js-package-dependencies) automatically when it caches the plugin.

Because the data directory outlives any single plugin version, a check for directory existence alone cannot detect when an update changes the plugin's dependency manifest. The recommended pattern compares the bundled manifest against a copy in the data directory and reinstalls when they differ.

This `SessionStart` hook installs `node_modules` on the first run and again whenever a plugin update includes a changed `package.json`:

```json theme={null}
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "diff -q \"${CLAUDE_PLUGIN_ROOT}/package.json\" \"${CLAUDE_PLUGIN_DATA}/package.json\" >/dev/null 2>&1 || (cd \"${CLAUDE_PLUGIN_DATA}\" && cp \"${CLAUDE_PLUGIN_ROOT}/package.json\" . && npm install) || rm -f \"${CLAUDE_PLUGIN_DATA}/package.json\""
          }
        ]
      }
    ]
  }
}
```

The `diff` exits nonzero when the stored copy is missing or differs from the bundled one, covering both first run and dependency-changing updates. If `npm install` fails, the trailing `rm` removes the copied manifest so the next session retries.

Scripts bundled in `${CLAUDE_PLUGIN_ROOT}` can then run against the persisted `node_modules`:

```json theme={null}
{
  "mcpServers": {
    "routines": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/server.js"],
      "env": {
        "NODE_PATH": "${CLAUDE_PLUGIN_DATA}/node_modules"
      }
    }
  }
}
```

The data directory is deleted automatically when you uninstall the plugin from the last scope where it is installed. The `/plugin` interface shows the directory size and prompts before deleting. The CLI deletes by default; pass [`--keep-data`](#plugin-uninstall) to preserve it.

***

## Plugin caching and file resolution

Plugins are specified in one of three ways:

* Through `claude --plugin-dir` or `claude --plugin-url`, for the duration of a session.
* Through a marketplace, installed for future sessions.
* Through your claude.ai account, [synced](#synced-plugins) into `~/.claude/plugins/synced/`.

For security and verification purposes, Claude Code copies *marketplace* plugins to the user's local **plugin cache** (`~/.claude/plugins/cache`), unless the plugin loads in place. A [`command` source in link mode](/docs/en/plugin-marketplaces#copy-mode-and-link-mode) loads in place through links in the cache entry. A [relative path source](/docs/en/plugin-marketplaces#relative-paths) in a marketplace added from a local directory loads in place from the marketplace folder.

For a plugin loaded in place from a local-directory marketplace, your edits to the source directory take effect at the next session start or `/reload-plugins`. You don't need a version bump. The plugin's hook processes and MCP and LSP servers receive a `CLAUDE_PLUGIN_ROOT` that points at the source directory. Claude Code doesn't install the plugin's [Node.js package dependencies](#node-js-package-dependencies) into the source directory. Install them there yourself, or from a hook into the [persistent data directory](#persistent-data-directory).

For copied plugins, each installed version is a separate directory in the cache, grouped by marketplace and plugin and named for the resolved version, with its own copy of the plugin's files and [Node.js package dependencies](#node-js-package-dependencies). A dependency resolved from a [release tag](/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution) gets a directory name with a commit-SHA suffix.

When you update or uninstall a plugin, Claude Code marks the previous version directory as orphaned and removes it in a background sweep roughly 14 days later. The grace period lets concurrent Claude Code sessions that already loaded the old version keep running without errors. Claude Code runs the sweep only while at least one plugin is installed; after you uninstall your last plugin, orphaned directories stay on disk until you install a plugin again.

Claude Code removes a plugin or marketplace folder from the cache only when it no longer contains any directory or symlink. If you symlink a development checkout into the cache as a plugin's version entry, Claude Code never marks the link as orphaned and never removes it or the folders that hold it. Claude Code also never writes its version-tracking files inside the linked checkout.

Claude's Glob and Grep tools skip orphaned version directories during searches, so file results don't include outdated plugin code.

### Node.js package dependencies

When Claude Code copies a plugin into the cache, it also installs the plugin's Node.js package dependencies there, so the plugin's hooks and MCP servers can load them. This section covers the npm and Bun packages a plugin declares in its own `package.json`. For plugins that depend on other plugins, see [plugin dependency versions](/docs/en/plugin-dependencies).

Claude Code runs the install inside the copied version directory each time it creates one: when you install a plugin, when Claude Code updates a plugin to a new version, and at session start when an enabled plugin isn't cached yet, such as on a new machine. The install runs only when the plugin's root directory contains both a `package.json` and a supported lockfile:

| Lockfile                                     | Command                                          |
| :------------------------------------------- | :----------------------------------------------- |
| `bun.lock` or `bun.lockb`                    | `bun install --frozen-lockfile --ignore-scripts` |
| `npm-shrinkwrap.json` or `package-lock.json` | `npm ci --ignore-scripts`                        |

If a plugin contains more than one of these lockfiles, Claude Code uses the first match, checking in order: `bun.lock`, `bun.lockb`, `npm-shrinkwrap.json`, `package-lock.json`.

Claude Code skips the install in two cases, each with its own fix:

* If your plugin ships only a `yarn.lock` or `pnpm-lock.yaml`, replace it with an npm lockfile.
* If a `bunfig.toml` sits beside the bun lockfile, remove the `bunfig.toml`, or replace the bun lockfile with an npm lockfile.

Ship an npm lockfile for the widest reach. Claude Code runs the matched lockfile's package manager from the user's PATH and doesn't fall back to the other lockfile if it's missing. For a plugin distributed through an npm source, use `npm-shrinkwrap.json`; npm excludes `package-lock.json` from published packages.

Claude Code constrains this dependency install so that no code from the plugin or its packages executes during it, and bounds how long it can run:

* **Frozen resolution:** Bun and npm install exactly what the lockfile pins, and fail rather than re-resolve versions when `package.json` and the lockfile disagree.
* **No lifecycle scripts:** `--ignore-scripts` keeps `preinstall`, `install`, and `postinstall` scripts from running, so dependencies that build native modules in those scripts download but don't compile during this install.
* **60-second timeout:** Claude Code stops an install that runs longer and treats it as failed.

Claude Code fetches an npm-source plugin before this dependency install, and none of the package's own install scripts run during the fetch. See [npm packages](/docs/en/plugin-marketplaces#npm-packages).

A failed or skipped install never blocks the plugin. When the install fails, or Claude Code skips it because of a yarn or pnpm lockfile or a `bunfig.toml`, it records the reason as a warning in [debug output](#debugging-commands). A plugin with a `package.json` and no lockfile is skipped without a log entry. A timed-out install can leave a partial `node_modules` tree in the cached copy.

You can't turn the automatic install off; no setting or environment variable disables it. In restricted networks, see the [network access requirements](/docs/en/network-config#network-access-requirements) for the hosts to allow.

For dependencies the automatic install can't provide, such as packages that need their lifecycle scripts to build, Python dependencies, or a plugin locked with Yarn or pnpm, install them from a hook into the [persistent data directory](#persistent-data-directory).

### Path traversal limitations

Claude Code doesn't let a plugin reference files outside its own directory. It rejects a component path that resolves outside the plugin root, whether the path is declared in `plugin.json` or in a [marketplace entry](/docs/en/plugin-marketplaces#plugin-entries). That covers a path that points outside the plugin as written, such as `../shared-utils`, and a symlink that leads outside the plugin, other than [links within one marketplace](#share-files-within-a-marketplace-with-symlinks).

On macOS and Linux, Claude Code also rejects a component path that contains a backslash anywhere in it, even when the path stays inside the plugin. Components declared with backslash paths therefore load on Windows only. Write component paths with forward slashes, such as `./commands/deploy.md`.

When Claude Code rejects a path, it reports a [`path escapes plugin directory`](/docs/en/errors#path-escapes-plugin-directory) error and loads the plugin without that component.

Claude Code also doesn't copy files outside the plugin directory into the cache when it installs the plugin, so when a script inside a copied plugin reads a path above the plugin root, it doesn't find those files either.

### Share files within a marketplace with symlinks

If your plugin needs to share files with other parts of the same marketplace, you can create symbolic links inside your plugin directory. How a symlink is handled when the plugin is copied into the cache depends on where its target resolves:

* **Within the plugin's own directory:** the symlink is preserved as a relative symlink in the cache, so it keeps resolving to the copied target at runtime.
* **Elsewhere within the same marketplace:** the symlink is dereferenced. The target's content is copied into the cache in its place. This lets a meta-plugin's `skills/` directory link to skills defined by other plugins in the marketplace.
* **Outside the marketplace:** the symlink is skipped for security. This prevents plugins from pulling arbitrary host files such as system paths into the cache.

For plugins installed with `--plugin-dir`, from a local path, or from a [`command` source](/docs/en/plugin-marketplaces#copy-mode-and-link-mode) in copy mode, only symlinks that resolve within the plugin's own directory are preserved. All others are skipped.

The following command creates a link from inside a marketplace plugin to a shared skill defined by a sibling plugin. On Windows, use `mklink /D` from an elevated Command Prompt or enable Developer Mode:

```bash theme={null}
ln -s ../../shared-plugin/skills/foo ./skills/foo
```

***

## Plugin directory structure

### Standard plugin layout

A complete plugin follows this structure:

```text theme={null}
enterprise-plugin/
├── .claude-plugin/           # Metadata directory (optional)
│   └── plugin.json             # plugin manifest
├── skills/                   # Skills
│   ├── code-reviewer/
│   │   └── SKILL.md
│   └── pdf-processor/
│       ├── SKILL.md
│       └── scripts/
├── commands/                 # Skills as flat .md files
│   ├── status.md
│   └── logs.md
├── agents/                   # Subagent definitions
│   ├── security-reviewer.md
│   ├── performance-tester.md
│   ├── compliance-checker.md
│   └── review/               # Agents here load as enterprise-plugin:review:<name>
│       └── accessibility.md
├── workflows/                # Workflow scripts
│   └── release-audit.js
├── output-styles/            # Output style definitions
│   └── terse.md
├── themes/                   # Color theme definitions
│   └── dracula.json
├── monitors/                 # Background monitor configurations
│   └── monitors.json
├── hooks/                    # Hook configurations
│   ├── hooks.json           # Main hook config
│   └── security-hooks.json  # Additional hooks
├── bin/                      # Plugin executables added to PATH
│   └── my-tool               # Invokable as bare command in Bash tool
├── settings.json            # Default settings for the plugin
├── .mcp.json                # MCP server definitions
├── .lsp.json                # LSP server configurations
├── scripts/                 # Hook and utility scripts
│   ├── security-scan.sh
│   ├── format-code.py
│   └── deploy.js
├── LICENSE                  # License file
└── CHANGELOG.md             # Version history
```

<Warning>
  The `.claude-plugin/` directory contains the `plugin.json` file. All other directories (commands/, agents/, skills/, workflows/, output-styles/, themes/, monitors/, hooks/) must be at the plugin root, not inside `.claude-plugin/`.
</Warning>

A `CLAUDE.md` file at the plugin root is not loaded as project context. Plugins contribute context through skills, agents, and hooks rather than CLAUDE.md. To ship instructions that load into Claude's context, put them in a [skill](#skills).

### File locations reference

| Component         | Default Location             | Purpose                                                                                                                                                                                                                                                                                    |
| :---------------- | :--------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manifest**      | `.claude-plugin/plugin.json` | Plugin metadata and configuration (optional)                                                                                                                                                                                                                                               |
| **Skills**        | `skills/`                    | Skills with `<name>/SKILL.md` structure                                                                                                                                                                                                                                                    |
| **Commands**      | `commands/`                  | Skills as flat Markdown files. Use `skills/` for new plugins                                                                                                                                                                                                                               |
| **Agents**        | `agents/`                    | Subagent Markdown files. Subfolders are part of the [agent name](#agents)                                                                                                                                                                                                                  |
| **Workflows**     | `workflows/`                 | [Workflow](/docs/en/workflows) script files                                                                                                                                                                                                                                                     |
| **Output styles** | `output-styles/`             | Output style definitions                                                                                                                                                                                                                                                                   |
| **Themes**        | `themes/`                    | Color theme definitions                                                                                                                                                                                                                                                                    |
| **Hooks**         | `hooks/hooks.json`           | Hook configuration                                                                                                                                                                                                                                                                         |
| **MCP servers**   | `.mcp.json`                  | MCP server definitions                                                                                                                                                                                                                                                                     |
| **LSP servers**   | `.lsp.json`                  | Language server configurations                                                                                                                                                                                                                                                             |
| **Monitors**      | `monitors/monitors.json`     | Background monitor configurations                                                                                                                                                                                                                                                          |
| **Executables**   | `bin/`                       | Executables added to the Bash tool's `PATH` and invokable as bare commands while the plugin is enabled. You can't include this directory in a plugin you [distribute through claude.ai organization settings](/docs/en/plugin-marketplaces#keep-executables-out-of-the-top-level-bin-directory) |
| **Settings**      | `settings.json`              | Default configuration applied when the plugin is enabled. Only the [`agent`](/docs/en/sub-agents) and [`subagentStatusLine`](/docs/en/statusline#subagent-status-lines) keys are supported                                                                                                           |

***

## CLI commands reference

Claude Code provides CLI commands for non-interactive plugin management, useful for scripting and automation.

### plugin init

Scaffold a new plugin at `~/.claude/skills/<name>/`. On the next Claude Code session it loads automatically as `<name>@skills-dir` and appears in `/plugin` and `claude plugin list` with no install step.

See [Skills-directory plugins](#skills-directory-plugins) for scope and trust requirements.

```bash theme={null}
claude plugin init <name> [options]
```

The command takes these arguments:

* `<name>`: Plugin name. Becomes the skill namespace and the directory name under `~/.claude/skills/`, so it cannot contain spaces or path separators.

The command accepts these options:

| Option                   | Description                                                                                                         | Default                 |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------ | :---------------------- |
| `--description <text>`   | Manifest description                                                                                                |                         |
| `--author <name>`        | Author name                                                                                                         | `git config user.name`  |
| `--author-email <email>` | Author email                                                                                                        | `git config user.email` |
| `--with <components...>` | Also scaffold component folders. Valid values: `skills`, `agents`, `hooks`, `mcp`, `lsp`, `output-style`, `channel` |                         |
| `-f, --force`            | Overwrite an existing `.claude-plugin/` at the target                                                               |                         |
| `-h, --help`             | Display help for command                                                                                            |                         |

`claude plugin new` is an alias for this command.

Each `--with` value adds a starter file for that component, ready to edit:

| Component      | What it scaffolds                                                                                         |
| :------------- | :-------------------------------------------------------------------------------------------------------- |
| `skills`       | An extra namespaced `<name>:example` skill alongside the default one                                      |
| `agents`       | An `agents/` subagent definition                                                                          |
| `hooks`        | A `hooks/hooks.json` with a sample event handler                                                          |
| `mcp`          | A `.mcp.json` with HTTP and stdio server examples                                                         |
| `lsp`          | A `.lsp.json` language-server example                                                                     |
| `output-style` | An `output-styles/<name>.md` that applies automatically while the plugin is enabled                       |
| `channel`      | An MCP-based [channel](/docs/en/channels): a stdio server (`server.ts`), its `.mcp.json`, and a `package.json` |

The scaffolded plugin uses the `@skills-dir` source rather than a marketplace. Admins can block this source with `strictKnownMarketplaces` or by adding `{"source": "skills-dir"}` to `blockedMarketplaces` in [managed settings](/docs/en/plugin-marketplaces#managed-marketplace-restrictions). When blocked, `plugin init` fails before writing.

These examples show common invocations:

```bash theme={null}
# Scaffold a minimal plugin
claude plugin init my-helper

# Scaffold with skill and hook folders
claude plugin init my-helper --with skills hooks

# Overwrite an existing scaffold
claude plugin init my-helper --force
```

### plugin install

Install a plugin from available marketplaces.

```bash theme={null}
claude plugin install <plugin> [options]
```

The command takes these arguments:

* `<plugin>`: Plugin name or `plugin-name@marketplace-name` for a specific marketplace

The command accepts these options:

| Option                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Default |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `-s, --scope <scope>`       | Installation scope: `user`, `project`, or `local`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `user`  |
| `--config <key=value>`      | Set a [`userConfig`](#user-configuration) option declared in the plugin's manifest. Repeat the flag to set multiple options                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         |
| `-y, --yes`                 | Accept a command the plugin's marketplace declares, without the confirmation prompt: the command that produces a plugin with a [`command` source](/docs/en/plugin-marketplaces#command-sources), or the [`headersHelper`](/docs/en/plugin-marketplaces#authenticate-archive-downloads) that authenticates an archive download. Accepting a `headersHelper` requires Claude Code v2.1.238 or later. Claude Code still prints the command first. Required when stdin or stdout isn't a TTY, unless you pass `--accept-command`. Has no effect inside a Claude Code session, so run the command from your own terminal |         |
| `--accept-command <sha256>` | Accept the marketplace-declared command whose `sha256` a previous [`--json` run](#plugin-json-result) reported in `shownCommand`, in place of `-y`. The acceptance counts for exactly that command, plugin, and marketplace catalog. If any of them changed since the command was displayed, including through the run's own marketplace refresh, Claude Code doesn't accept the digest and shows the command again. Can't be combined with `-y`. Has no effect inside a Claude Code session, so run the command from your own terminal. Requires Claude Code v2.1.271 or later                           |         |
| `--json`                    | Print the result as one JSON object on the last line of stdout instead of the human-readable message, for use in scripts. See [JSON result format](#plugin-json-result). Requires Claude Code v2.1.268 or later                                                                                                                                                                                                                                                                                                                                                                                           |         |
| `-h, --help`                | Display help for command                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |

Scope determines which settings file the installed plugin is added to. For example, `--scope project` writes to `enabledPlugins` in .claude/settings.json, making the plugin available to everyone who clones the project repository.

<span id="plugin-json-result" />With `--json`, the last line of stdout is one JSON object. Parse only that line, because Claude Code prints any command the marketplace declares ahead of it. Three fields are always present:

* `command`: the subcommand that ran, such as `install`
* `outcome`: `ok` or `failed`
* `message`: a human-readable description of the result

Other fields, such as `pluginId`, `scope`, and `failureCode`, appear only when they apply. The `--json` option on `plugin uninstall`, `plugin update`, `plugin enable`, and `plugin disable` prints the same object with that subcommand's own fields. A usage error, such as an invalid `--scope`, prints no result line and exits 1 with the reason on stderr.

When a run displays a marketplace-declared command and doesn't run it, the `failed` result also carries a `shownCommand` object whose fields include the command as displayed, the plugin it belongs to, and the command's `sha256`. To accept exactly that command, re-run with that `sha256` as `--accept-command`. Requires Claude Code v2.1.271 or later.

If `shownCommand.acceptCommandMatched` is `false`, the digest you passed doesn't match the command now displayed. Show that command to a person before passing its `sha256`.

These examples show common invocations:

```bash theme={null}
# Install to user scope (default)
claude plugin install formatter@my-marketplace

# Install to project scope (shared with team)
claude plugin install formatter@my-marketplace --scope project

# Install to local scope (not shared with team)
claude plugin install formatter@my-marketplace --scope local
```

### plugin uninstall

Remove an installed plugin.

```bash theme={null}
claude plugin uninstall <plugin> [options]
```

The command takes these arguments:

* `<plugin>`: Plugin name or `plugin-name@marketplace-name`

The command accepts these options:

| Option                | Description                                                                                                                                                                                                    | Default |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `-s, --scope <scope>` | Uninstall from scope: `user`, `project`, or `local`                                                                                                                                                            | `user`  |
| `--keep-data`         | Preserve the plugin's [persistent data directory](#persistent-data-directory)                                                                                                                                  |         |
| `--prune`             | Also remove auto-installed dependencies that no other plugin requires. See [plugin prune](#plugin-prune)                                                                                                       |         |
| `-y, --yes`           | Skip the `--prune` confirmation prompt. Required when stdin or stdout is not a TTY                                                                                                                             |         |
| `--json`              | Print the result as one JSON object on the last line of stdout, in the [same format as `plugin install --json`](#plugin-json-result). Can't be combined with `--prune`. Requires Claude Code v2.1.268 or later |         |
| `-h, --help`          | Display help for command                                                                                                                                                                                       |         |

`claude plugin remove` and `claude plugin rm` are aliases for this command.

By default, uninstalling from the last remaining scope also deletes the plugin's `${CLAUDE_PLUGIN_DATA}` directory. Use `--keep-data` to preserve it, for example when reinstalling after testing a new version.

<Note>
  When installed plugins from different marketplaces share a name, the `plugin-name@marketplace-name` form uninstalls only the plugin from the named marketplace. Before v2.1.212, the qualified form could match and uninstall the same-named plugin from a different marketplace.
</Note>

### plugin prune

Remove auto-installed plugin dependencies that are no longer required by any installed plugin. Dependencies that Claude Code pulled in to satisfy another plugin's [`dependencies`](/docs/en/plugin-dependencies) field are removed; plugins you installed directly are never touched.

```bash theme={null}
claude plugin prune [options]
```

The command accepts these options:

| Option                | Description                                                              | Default |
| :-------------------- | :----------------------------------------------------------------------- | :------ |
| `-s, --scope <scope>` | Prune at scope: `user`, `project`, or `local`                            | `user`  |
| `--dry-run`           | List what would be removed without removing anything                     |         |
| `-y, --yes`           | Skip the confirmation prompt. Required when stdin or stdout is not a TTY |         |
| `-h, --help`          | Display help for command                                                 |         |

`claude plugin autoremove` is an alias for this command.

The command lists orphaned dependencies and asks for confirmation before removing them. To remove a plugin and clean up its dependencies in one step, run `claude plugin uninstall <plugin> --prune`.

### plugin enable

Enable a disabled plugin. When the target is installed from a marketplace and declares [dependencies](/docs/en/plugin-dependencies), Claude Code enables them transitively at the same scope. The command fails under the conditions that [Enable or disable a plugin with dependencies](/docs/en/plugin-dependencies#enable-or-disable-a-plugin-with-dependencies) lists.

```bash theme={null}
claude plugin enable <plugin> [options]
```

The command takes these arguments:

* `<plugin>`: Plugin name, `plugin-name@marketplace-name`, or `plugin-name@synced` for a [plugin synced from claude.ai](#synced-plugins)

The command accepts these options:

| Option                | Description                                                                                                                                                                  | Default     |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| `-s, --scope <scope>` | Scope to enable: `user`, `project`, or `local`. When omitted, Claude Code detects the scope where the plugin is installed                                                    | Auto-detect |
| `--json`              | Print the result as one JSON object on the last line of stdout, in the [same format as `plugin install --json`](#plugin-json-result). Requires Claude Code v2.1.268 or later |             |
| `-h, --help`          | Display help for command                                                                                                                                                     |             |

### plugin disable

Disable a plugin without uninstalling it.

When the target is installed from a marketplace, the command fails if another enabled plugin [depends on](/docs/en/plugin-dependencies#enable-or-disable-a-plugin-with-dependencies) it. The error message includes a chained command that disables every dependent first.

For a [synced plugin](#synced-plugins) that your organization requires, the command fails and saves nothing.

```bash theme={null}
claude plugin disable [plugin] [options]
```

The command takes these arguments:

* `[plugin]`: Plugin name, `plugin-name@marketplace-name`, or `plugin-name@synced` for a [plugin synced from claude.ai](#synced-plugins). Optional when using `--all`

The command accepts these options:

| Option                | Description                                                                                                                                                                  | Default     |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| `-a, --all`           | Disable all enabled plugins. Can't be combined with `--scope`                                                                                                                |             |
| `-s, --scope <scope>` | Scope to disable: `user`, `project`, or `local`. When omitted, Claude Code detects the scope where the plugin is installed                                                   | Auto-detect |
| `--json`              | Print the result as one JSON object on the last line of stdout, in the [same format as `plugin install --json`](#plugin-json-result). Requires Claude Code v2.1.268 or later |             |
| `-h, --help`          | Display help for command                                                                                                                                                     |             |

### plugin update

Update a plugin to the latest version.

```bash theme={null}
claude plugin update <plugin> [options]
```

The command takes these arguments:

* `<plugin>`: Plugin name or `plugin-name@marketplace-name`

The command accepts these options:

| Option                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Default |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `-s, --scope <scope>`       | Scope to update: `user`, `project`, `local`, or `managed`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `user`  |
| `-y, --yes`                 | Accept a command the plugin's marketplace declares, without the confirmation prompt: the command that produces a plugin with a [`command` source](/docs/en/plugin-marketplaces#command-sources), or the [`headersHelper`](/docs/en/plugin-marketplaces#authenticate-archive-downloads) that authenticates an archive download. Accepting a `headersHelper` requires Claude Code v2.1.238 or later. Claude Code still prints the command first. Required when stdin or stdout isn't a TTY, unless you pass `--accept-command`. Has no effect inside a Claude Code session, so run the command from your own terminal |         |
| `--accept-command <sha256>` | Accept the marketplace-declared command whose `sha256` a previous [`--json` run](#plugin-json-result) reported in `shownCommand`, in place of `-y`. The acceptance counts for exactly that command, plugin, and marketplace catalog. If any of them changed since the command was displayed, including through the run's own marketplace refresh, Claude Code doesn't accept the digest and shows the command again. Can't be combined with `-y`. Has no effect inside a Claude Code session, so run the command from your own terminal. Requires Claude Code v2.1.271 or later                           |         |
| `--json`                    | Print the result as one JSON object on the last line of stdout, in the [same format as `plugin install --json`](#plugin-json-result). Requires Claude Code v2.1.268 or later                                                                                                                                                                                                                                                                                                                                                                                                                              |         |
| `-h, --help`                | Display help for command                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |

<Note>
  Claude Code resolves a bare plugin name against your installed plugins. When installed plugins from different marketplaces share the name, Claude Code refuses the update and lists the qualified `plugin-name@marketplace-name` commands to run instead. Before v2.1.246, Claude Code accepted only the qualified form and rejected a bare name as not found.
</Note>

***

### plugin list

List installed plugins with their version, source marketplace, and enable status.

```bash theme={null}
claude plugin list [options]
```

The command accepts these options:

| Option        | Description                                                                                                                                                                                                                                                                                                          | Default |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `--json`      | Output as JSON. A plugin row with load problems or authoring warnings carries `errors` or `notes` string arrays. On Claude Code v2.1.268 or later, parallel `errorDetails` and `noteDetails` arrays give each entry's diagnostic `type` and the names it refers to, such as the plugin, marketplace, server, or file |         |
| `--available` | Include available plugins from marketplaces. Requires `--json`                                                                                                                                                                                                                                                       |         |
| `-h, --help`  | Display help for command                                                                                                                                                                                                                                                                                             |         |

Within an interactive session, `/plugin list` prints a similar listing inline, but it covers marketplace-installed plugins only:

* Plugins loaded from skills directories appear in the `/plugin` interface and in `claude plugin list`, but not in the inline `/plugin list` output.
* [Plugins synced from claude.ai](#synced-plugins) appear in `claude plugin list` on Claude Code v2.1.239 or later and in the `/plugin` interface, but not in the inline `/plugin list` output.
* Plugins loaded for the session with `--plugin-dir` or `--plugin-url` appear in the `/plugin` interface, and in `claude plugin list` only when the same flag precedes the subcommand, as in `claude --plugin-dir <dir> plugin list`. Only the flag names their location, so a bare `claude plugin list` can't find them, unlike synced plugins and skills-directory plugins, whose fixed directories Claude Code scans.

The interactive form accepts `--enabled` or `--disabled` to show only plugins in that state, and `ls` as a shorthand for `list`.

### plugin details

Show a plugin's component inventory and projected token cost. The output lists all components the plugin contributes, grouped as Skills, Agents, Hooks, MCP servers, and LSP servers, along with an estimate of how many tokens it adds to each session. The Skills group includes both `skills/` and `commands/` entries.

```bash theme={null}
claude plugin details <name>
```

The command takes these arguments:

* `<name>`: Plugin name or `plugin-name@marketplace-name`

The command accepts these options:

| Option       | Description              | Default |
| :----------- | :----------------------- | :------ |
| `-h, --help` | Display help for command |         |

The output shows two cost figures for each component:

* **Always-on:** tokens added to every session by the plugin's listing text, such as skill descriptions, agent descriptions, and command names, regardless of whether any component fires.
* **On-invoke:** tokens a component costs when it fires. Shown per component, not as a plugin total, because a typical session invokes only a subset of components.

This example shows what the output looks like for a plugin with two skills:

```
dependency-guard 1.2.0
  Dependency analysis for Claude Code sessions
  Source: dependency-guard@example-marketplace

Component inventory
  Skills (2)  scan-dependencies, review-changes
  Agents (0)
  Hooks (1)  SessionStart  (harness-only — no model context cost)
  MCP servers (0)
  LSP servers (0)

Projected token cost
  Always-on:   ~180 tok   added to every session

Per-component (rounded)
  component            always-on  on-invoke
  scan-dependencies        ~100      ~2400
  review-changes            ~80      ~1800

  On-invoke cost is paid each time a skill or agent fires.
  Token counts are estimates and may differ from actual usage.
```

The always-on total is computed via the `count_tokens` API for your active model. Per-component numbers are proportionally scaled from that total. If the API is unreachable, the command falls back to a character-based estimate.

### plugin validate

Check a plugin or a marketplace for syntax and schema errors before publishing.

The command exits 0 when validation passes, 1 when it fails, and 2 when the validation run itself fails, such as when the path you pass is unreadable.

```bash theme={null}
claude plugin validate <path> [options]
```

The command takes these arguments:

* `<path>`: Path to a plugin directory or a marketplace directory. See [Validate a plugin or a directory without a manifest](/docs/en/plugin-marketplaces#validate-a-plugin-or-a-directory-without-a-manifest) for which files a plugin run covers.

The command accepts these options:

| Option       | Description                                                                                                                                       | Default |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :------ |
| `--strict`   | Treat warnings as errors and exit 1 on them. Use in CI to catch issues the runtime tolerates, such as [unrecognized fields](#unrecognized-fields) |         |
| `--json`     | Output the validation report as one JSON object with the same exit codes. Requires Claude Code v2.1.259 or later                                  |         |
| `-h, --help` | Display help for command                                                                                                                          |         |

With `--json`, Claude Code writes the report to stdout as one JSON object with these top-level fields:

* `success`: the same verdict the exit code gives
* `strict`: whether the run treated warnings as errors
* `target`: the resolved path Claude Code validated
* `manifest`: the manifest's own result, or `null` for a [run without a manifest](/docs/en/plugin-marketplaces#validate-a-plugin-or-a-directory-without-a-manifest)
* `contents`: per-file results, each naming its `file` and carrying `errors`, `warnings`, and `notes` arrays

On exit 2, the command writes nothing to stdout; the error message goes to stderr.

Within an interactive session, `/plugin validate <path>` runs the same checks inline.

### plugin eval

Run a plugin's [eval cases](/docs/en/plugin-evals) and report scored results. Requires Claude Code v2.1.269 or later. Each case is a prompt plus graders; Claude Code runs it several times in an isolated session with only the target plugin loaded, and by default also without the plugin so the report shows the difference. See [Test plugins with evals](/docs/en/plugin-evals) for the case format, graders, results, and CI usage.

```bash theme={null}
claude plugin eval [target] [options]
```

The optional `target` is a plugin directory, a single `prompt.md` or `case.yaml` file, an installed plugin as `name` or `name@marketplace`, or `name@skills-dir`, and defaults to the current directory. Put it before `--tag`, `--allow-tools`, and `--json`.

This table lists the options most runs use. Run `claude plugin eval --help` for the complete set, including `--case`, `--tag`, `--output-dir`, `--report`, `--allow-real-servers`, `--keep-temp`, and `--verbose`.

| Option                     | Description                                                                                                                                                     | Default                                                                        |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| `--runs <n>`               | Runs per case per arm                                                                                                                                           | Each case's `runs`, else 3                                                     |
| `-j, --concurrency <n>`    | Agent sessions to run at once, 1 to 8. They share your rate limit                                                                                               | `1`                                                                            |
| `--model <model>`          | Model for the agent under test                                                                                                                                  | Each case's `model`, else `ANTHROPIC_MODEL` if set, else Claude Code's default |
| `--judge-model <model>`    | Model for `llm` and `baseline` graders                                                                                                                          | A small fast model                                                             |
| `--ablation <mode>`        | `none` or `with-without`. See [Compare against a no-plugin baseline](/docs/en/plugin-evals#compare-against-a-no-plugin-baseline)                                     | `with-without` when a plugin resolves, else `none`                             |
| `--threshold <0..1>`       | Exit 1 if any case scores below this                                                                                                                            | `1.0`                                                                          |
| `--max-cost-usd <usd>`     | Stop before the next run once spend reaches this, exit 2, and report partial results                                                                            | No ceiling                                                                     |
| `--allow-tools <tools...>` | Grant tools beyond the read-only set, such as `Bash`, `Write`, `Edit`, or `"mcp__plugin_<plugin>_<server>__*"`. See [Grant tools](/docs/en/plugin-evals#grant-tools) |                                                                                |
| `--scaffold`               | Run each case's [`scaffold_script`](/docs/en/plugin-evals#add-setup-or-history-with-case-yaml)                                                                       | Off                                                                            |
| `--trust-plugin`           | Skip the first-run trust prompt, for CI. See [What a run can access](/docs/en/plugin-evals#security)                                                                 | Off                                                                            |
| `--mocks <mode>`           | `record` or `off`. See [Mock MCP servers](/docs/en/plugin-evals#mock-mcp-servers)                                                                                    | `record`                                                                       |
| `--eval-dir <dir>`         | Directory below the plugin that holds the cases                                                                                                                 | The manifest's `experimental.evals`, else `evals`                              |
| `--json [path]`            | Print the [result document](/docs/en/plugin-evals#json-result) to stdout, or write it to a `.json` path                                                              |                                                                                |
| `--no-publish`             | Keep the HTML report local                                                                                                                                      |                                                                                |
| `-h, --help`               | Display help for command                                                                                                                                        |                                                                                |

The command exits 0 when every case meets the threshold, 1 on a failing case, a load error, or an untrusted plugin directory, 2 on a partial run, 130 when interrupted, and 143 when terminated. See [Run evals in CI](/docs/en/plugin-evals#run-evals-in-ci).

### plugin eval init

Create an eval suite for the plugin in the current directory. Requires Claude Code v2.1.269 or later. In a terminal this starts an authoring interview that reads the plugin, proposes cases and graders, pilots them, and writes the files. With `--bare`, or without a terminal, it writes a blank single-case template instead. Run from inside an interactive Claude Code session, it prints the interview instructions for that session to follow rather than writing a template. See [Create your first eval suite](/docs/en/plugin-evals#create-your-first-eval-suite).

```bash theme={null}
claude plugin eval init [name] [options]
```

The optional `name` is a case name: the interview doesn't need one, while `--bare` and the no-terminal template path require it. It accepts these options:

| Option              | Description                                                                                       | Default                                           |
| :------------------ | :------------------------------------------------------------------------------------------------ | :------------------------------------------------ |
| `--bare`            | Write a blank `prompt.md` and `graders/criteria.md` for `<name>` instead of running the interview |                                                   |
| `-i, --interactive` | Require the interview. Fails without a terminal instead of writing a template                     |                                                   |
| `--eval-dir <dir>`  | Directory below the current directory to write cases into                                         | The manifest's `experimental.evals`, else `evals` |
| `-h, --help`        | Display help for command                                                                          |                                                   |

### plugin tag

Create a release git tag for a plugin. By default the command tags the plugin in the current directory; pass a path to tag a plugin elsewhere. See [Tag plugin releases](/docs/en/plugin-dependencies#tag-plugin-releases-for-version-resolution).

```bash theme={null}
claude plugin tag [path] [options]
```

The command takes these arguments:

* `[path]`: Path to the plugin directory. Defaults to the current directory.

The command accepts these options:

| Option                | Description                                                                | Default  |
| :-------------------- | :------------------------------------------------------------------------- | :------- |
| `--push`              | Push the tag to the remote after creating it                               |          |
| `--dry-run`           | Print what would be tagged without creating the tag                        |          |
| `-f, --force`         | Create the tag even if the working tree is dirty or the tag already exists |          |
| `-m, --message <msg>` | Tag annotation message. Use `%s` as a placeholder for the version          |          |
| `--remote <name>`     | Remote to push to with `--push`                                            | `origin` |
| `-h, --help`          | Display help for command                                                   |          |

***

## Debugging and development tools

### Debugging commands

Use `claude --debug` to see plugin loading details:

This shows:

* Which plugins are being loaded
* Any errors in plugin manifests
* Skill, agent, and hook registration
* MCP server initialization

### Common issues

| Issue                               | Cause                           | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :---------------------------------- | :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Plugin not loading                  | Invalid `plugin.json`           | Run `claude plugin validate ./my-plugin` or `/plugin validate ./my-plugin`, where `./my-plugin` is your plugin directory, to check `plugin.json`, `hooks/hooks.json`, and the frontmatter of the skills, agents, and commands in the plugin's default directories for syntax and schema errors. See [Validate a plugin or a directory without a manifest](/docs/en/plugin-marketplaces#validate-a-plugin-or-a-directory-without-a-manifest) for what a run covers |
| Skills not appearing                | Wrong directory structure       | Ensure `skills/` or `commands/` is at the plugin root, not inside `.claude-plugin/`                                                                                                                                                                                                                                                                                                                                                                          |
| Hooks not firing                    | Script not executable           | Run `chmod +x script.sh`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MCP server fails                    | Missing `${CLAUDE_PLUGIN_ROOT}` | Use variable for all plugin paths                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Path errors                         | Absolute paths used             | Make paths relative, starting with `./`; see [Path behavior rules](#path-behavior-rules), which cover the `skills` field's `"."` exception                                                                                                                                                                                                                                                                                                                   |
| LSP `Executable not found in $PATH` | Language server not installed   | Install the binary (for example, `npm install -g typescript-language-server typescript`)                                                                                                                                                                                                                                                                                                                                                                     |

### Example error messages

**Manifest validation errors**:

* `Invalid JSON syntax: Unexpected token } in JSON at position 142`: check for missing commas, extra commas, or unquoted strings
* `Plugin <name> has an invalid manifest file at .claude-plugin/plugin.json. Validation errors: name: Invalid input: expected string, received undefined`: a required field is missing
* `Plugin <name> has a corrupt manifest file at .claude-plugin/plugin.json. JSON parse error: ...`: JSON syntax error. Before v2.1.246, Claude Code also produced this error for a `plugin.json` saved as UTF-8 with a leading byte-order mark (BOM), even when the JSON was otherwise valid.

**Plugin loading errors**:

* `Warning: No commands found in plugin my-plugin custom directory: ./cmds. Expected .md files or SKILL.md in subdirectories.`: command path exists but contains no valid command files
* `Plugin directory not found at path: ./plugins/my-plugin. Check that the marketplace entry has the correct path.`: the `source` path in marketplace.json points to a non-existent directory
* `Plugin my-plugin has conflicting manifests: both plugin.json and marketplace entry specify components.`: remove duplicate component definitions or remove `strict: false` in marketplace entry

### Hook troubleshooting

**Hook script not executing**:

1. Check the script is executable: `chmod +x ./scripts/your-script.sh`
2. Verify the shebang line: First line should be `#!/bin/bash` or `#!/usr/bin/env bash`
3. Check the path uses `${CLAUDE_PLUGIN_ROOT}`: `"command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/your-script.sh"`
4. Test the script manually: `./scripts/your-script.sh`

**Hook not triggering on expected events**:

1. Verify the event name is correct (case-sensitive): `PostToolUse`, not `postToolUse`
2. Check the matcher pattern matches your tools: `"matcher": "Write|Edit"` for file operations
3. Confirm the hook type is valid: `command`, `http`, `mcp_tool`, `prompt`, or `agent`

### MCP server troubleshooting

**Server not starting**:

1. Check the command exists and is executable
2. Verify all paths use `${CLAUDE_PLUGIN_ROOT}` variable
3. Check the MCP server logs: `claude --debug` shows initialization errors
4. Test the server manually outside of Claude Code

**Server tools not appearing**:

1. Ensure the server is properly configured in `.mcp.json` or `plugin.json`
2. Verify the server implements the MCP protocol correctly
3. Check for connection timeouts in debug output

### Directory structure mistakes

**Symptoms**: Plugin loads but components (skills, agents, hooks) are missing.

**Correct structure**: Components must be at the plugin root, not inside `.claude-plugin/`. Only `plugin.json` belongs in `.claude-plugin/`.

**Debug checklist**:

1. Run `claude --debug` and look for "loading plugin" messages
2. Check that each component directory is listed in the debug output
3. Verify file permissions allow reading the plugin files

***

## Distribution and versioning reference

### Version management

Claude Code uses the plugin's version as the cache key that determines whether an update is available. When you run `/plugin update` or auto-update fires, Claude Code computes the current version and skips the update if it matches what's already installed. A plugin [loaded in place](#plugin-caching-and-file-resolution) from a local-directory marketplace loads its current source files at every session start, whatever its version string says.

For every source type except `command`, Claude Code resolves the version from the first of these that is set:

1. The `version` field in the plugin's `plugin.json`
2. The `version` field in the plugin's marketplace entry in `marketplace.json`
3. The git commit SHA of the plugin's source, for `github`, `url`, `git-subdir`, and relative-path sources in a git-hosted marketplace
4. The SHA-256 digest, for [`archive` sources](/docs/en/plugin-marketplaces#zip-archives): the `sha256` pin in the marketplace entry, or the digest of the downloaded file when you set no pin. Claude Code shortens it to the first 12 characters
5. `unknown`, for `npm` sources, or for local directories when neither the plugin directory nor its marketplace is a git repository. Claude Code doesn't take the version from a repository that encloses the install path, such as a git-managed `~/.claude`

For a [`command` source](/docs/en/plugin-marketplaces#command-sources), Claude Code always derives the version from what the command produced: a 12-character content hash on its own, or appended to the `plugin.json` version as `<version>-<hash>` when one is set. Claude Code ignores the marketplace entry's `version` field for command sources. A command whose hashed output changes therefore produces a new version, even when the authored version string stays the same. In [link mode](/docs/en/plugin-marketplaces#copy-mode-and-link-mode), the hash covers the printed directory's real path and its top-level entries rather than the file contents.

For those source types, this gives you three ways to version a plugin:

| Approach               | How                                                                                                                                  | Update behavior                                                                                                                                                                                                                                                         | Best for                                                                 |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| **Explicit version**   | Set `"version": "2.1.0"` in `plugin.json`                                                                                            | Users get updates only when you bump this field. Pushing new commits without bumping it has no effect, and `/plugin update` reports "already at the latest version". For a plugin [loaded in place](#plugin-caching-and-file-resolution), the new content loads anyway. | Published plugins with stable release cycles                             |
| **Commit-SHA version** | Omit `version` from both `plugin.json` and the marketplace entry                                                                     | Users get updates whenever the source's resolved commit changes                                                                                                                                                                                                         | Internal or team plugins under active development                        |
| **Digest version**     | Use an [`archive` source](/docs/en/plugin-marketplaces#zip-archives) and omit `version` from both `plugin.json` and the marketplace entry | With a `sha256` pin, users get updates when you change the pin. Without one, users get updates whenever the hosted zip file's bytes change                                                                                                                              | Plugins published as zip files to a static server or artifact repository |

If you use explicit versions, follow [semantic versioning](https://semver.org) (`MAJOR.MINOR.PATCH`): bump MAJOR for breaking changes, MINOR for new features, PATCH for bug fixes. Document changes in a `CHANGELOG.md`.

***

## See also

* [Plugins](/docs/en/plugins) - Tutorials and practical usage
* [Plugin marketplaces](/docs/en/plugin-marketplaces) - Creating and managing marketplaces
* [Skills](/docs/en/skills) - Skill development details
* [Subagents](/docs/en/sub-agents) - Agent configuration and capabilities
* [Hooks](/docs/en/hooks) - Event handling and automation
* [MCP](/docs/en/mcp) - External tool integration
* [Settings](/docs/en/settings) - Configuration options for plugins

---

## Tools reference

- 官方原文：https://code.claude.com/docs/en/tools-reference.md
- 存档：`01-Raw/VibeCoding/claude-code/claude-code-en-tools-reference.md`

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools reference

> Complete reference for the tools Claude Code can use, including permission requirements and per-tool behavior.

Claude Code has access to a set of built-in tools that help it understand and modify your codebase. The tool names are the exact strings you use in [permission rules](/docs/en/permissions#tool-specific-permission-rules), [subagent tool lists](/docs/en/sub-agents), and [hook matchers](/docs/en/hooks).

To control which tools Claude can use and when it asks first, configure [permission rules](/docs/en/permissions#tool-specific-permission-rules) in your settings, [hooks](/docs/en/hooks), or a [subagent's tool list](/docs/en/sub-agents#supported-frontmatter-fields). See [Configure tools with permission rules and hooks](#configure-tools-with-permission-rules-and-hooks) for each place that accepts a tool name.

To add custom tools, connect an [MCP server](/docs/en/mcp). To extend Claude with reusable prompt-based workflows, write a [skill](/docs/en/skills), which runs through the existing `Skill` tool rather than adding a new tool entry.

<Info>
  On Pro, Max, and Team plans, Claude Code starts sessions in [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode), where a classifier decides most of these prompts instead of you. The `Permission required` column shows whether the tool prompts in [Manual mode](/docs/en/permission-modes) for paths inside the working directory. File-access tools marked No, including `Read`, `Grep`, and `Glob`, still prompt for paths outside the [working directory and additional directories](/docs/en/permissions#working-directories). `Bash` is marked Yes but runs a built-in set of [read-only commands](/docs/en/permissions#read-only-commands) without prompting.
</Info>

| Tool                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Permission required |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------ |
| `Agent`                | Spawns a [subagent](/docs/en/sub-agents) with its own context window to handle a task. With [agent teams](/docs/en/agent-teams) enabled, a call that carries a `name` can launch a [teammate](/docs/en/agent-teams#how-claude-starts-agent-teams) instead. See [Agent tool behavior](#agent-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No                  |
| `Artifact`             | Publishes an HTML or Markdown file as an [artifact](/docs/en/artifacts): a private, interactive page on claude.ai. You can share it with a public link, or inside your organization on Team and Enterprise plans, where public sharing requires an Owner to [enable it](/docs/en/artifacts#control-public-sharing). Requires a Pro, Max, Team, or Enterprise plan and `/login` authentication; see [Availability](/docs/en/artifacts#availability)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes                 |
| `AskUserQuestion`      | Asks multiple-choice questions to gather requirements or clarify ambiguity. Questions stay open until you answer them by default. See [AskUserQuestion tool behavior](#askuserquestion-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No                  |
| `Bash`                 | Executes shell commands in your environment. See [Bash tool behavior](#bash-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes                 |
| `CronCreate`           | Schedules a recurring or one-shot prompt within the current session. Tasks are session-scoped and restored on `--resume` or `--continue` if unexpired. See [scheduled tasks](/docs/en/scheduled-tasks)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No                  |
| `CronDelete`           | Cancels a scheduled task by ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No                  |
| `CronList`             | Lists all scheduled tasks in the session                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                  |
| `Edit`                 | Makes targeted edits to specific files. See [Edit tool behavior](#edit-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes                 |
| `EndConversation`      | Ends the session, in rare cases of sustained abusive input or when you ask Claude to demonstrate the tool. Requires Claude Code v2.1.213 or later. See [EndConversation tool behavior](#endconversation-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No                  |
| `EnterPlanMode`        | Switches to plan mode to design an approach before coding                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                  |
| `EnterWorktree`        | Creates an isolated [git worktree](/docs/en/worktrees) and switches into it. Pass a `path` to switch into an existing worktree instead of creating a new one. On first entry the target may be a worktree of the current repository or, in a multi-repo workspace, of a repository nested inside it. Before v2.1.203, a nested repository's worktree was rejected. A `path` outside `.claude/worktrees/` prompts for your approval before entering, since it moves the session's working directory and write access to that location. New-worktree creation and paths under `.claude/worktrees/` don't prompt. Before v2.1.206, Claude entered paths outside `.claude/worktrees/` without a prompt. From within a worktree session, or from a subagent with a pinned working directory such as [`isolation: worktree`](/docs/en/sub-agents#supported-frontmatter-fields), only the `path` form is available and the target must be under `.claude/worktrees/` of the session's repository                         | Yes                 |
| `ExitPlanMode`         | Presents a plan for approval and exits plan mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes                 |
| `ExitWorktree`         | Exits a worktree session and returns to the original directory. Not available to subagents that already run in their own working directory, such as with [`isolation: worktree`](/docs/en/sub-agents#supported-frontmatter-fields)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                  |
| `Glob`                 | Finds files based on pattern matching. Absent by default on macOS, Linux, and WSL. See [Glob tool behavior](#glob-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                  |
| `Grep`                 | Searches for patterns in file contents. Absent by default on macOS, Linux, and WSL. See [Grep tool behavior](#grep-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No                  |
| `ListAgents`           | Lists the agents Claude can message with `SendMessage`: subagents in the session, [agent team](/docs/en/agent-teams) teammates, your other local Claude Code sessions, and, while this session is connected to [Remote Control](/docs/en/remote-control), your [cloud sessions](/docs/en/claude-code-on-the-web) and your Remote Control sessions on other machines. Backs the `/list-agents` command. See [cross-session messaging](/docs/en/cross-session-messaging). Requires Claude Code v2.1.224 or later, and appears only in sessions where [cross-session messaging is enabled](/docs/en/cross-session-messaging#availability). Teammate rows and the first line showing this session's own name require v2.1.239 or later                                                                                                                                                                                                                                                                                               | No                  |
| `ListMcpResourcesTool` | Lists resources exposed by connected [MCP servers](/docs/en/mcp)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No                  |
| `LSP`                  | Code intelligence via language servers: jump to definitions, find references, report type errors and warnings. See [LSP tool behavior](#lsp-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No                  |
| `Monitor`              | Runs a command in the background and feeds each output line back to Claude, so it can react to log entries, file changes, or polled status mid-conversation. Can also open a WebSocket and treat each incoming message as an event. See [Monitor tool](#monitor-tool)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes                 |
| `NotebookEdit`         | Modifies Jupyter notebook cells. See [NotebookEdit tool behavior](#notebookedit-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes                 |
| `PowerShell`           | Executes PowerShell commands natively. See [PowerShell tool](#powershell-tool) for availability                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes                 |
| `PushNotification`     | Sends a desktop notification, and a phone push when [Remote Control](/docs/en/remote-control) is connected, so a long-running task or [scheduled task](/docs/en/scheduled-tasks) can reach you when you step away. Push delivery runs through Anthropic-hosted infrastructure, which is not accessible from Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, or Microsoft Foundry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                  |
| `Read`                 | Reads the contents of files. See [Read tool behavior](#read-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No                  |
| `ReadMcpResourceTool`  | Reads a specific MCP resource by URI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No                  |
| `RemoteTrigger`        | Creates, updates, runs, and lists [Routines](/docs/en/routines) on claude.ai. Backs the `/schedule` command. The [`RemoteTrigger` input reference](/docs/en/agent-sdk/typescript#remotetrigger) documents every action and the organization policies that remove the tool. Routines live on claude.ai and require a Pro, Max, Team, or Enterprise plan, so this tool is not accessible from Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, or Microsoft Foundry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                  |
| `ReportFindings`       | Reports code-review findings as a structured list, with a file, summary, and failure scenario per finding, so Claude Code can render them instead of printing them as text. Claude calls it when active code-review instructions tell it to. Requires Claude Code v2.1.196 or later. As of v2.1.199, a finding can also carry an optional `category` slug, such as `correctness` or `test-coverage`, shown next to the file location in the rendered list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                  |
| `ScheduleWakeup`       | Reschedules the next iteration of a [self-paced `/loop`](/docs/en/scheduled-tasks#let-claude-choose-the-interval). Claude calls this at the end of each iteration to pick when the next one runs, between one minute and one hour out; you don't call it directly. To end the loop instead, Claude calls it with `stop: true`, which cancels the pending wakeup. The `stop` field requires Claude Code v2.1.202 or later. The pending wakeup appears in `session_crons` in [Stop hook input](/docs/en/hooks#stop-input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                  |
| `SendFeedback`         | Drafts a feedback report about Claude Code, covering a product problem or Claude's own behavior in the session, and queues it on your machine for you to review. Claude Code sends nothing until you choose to send the draft. See [SendFeedback tool behavior](#sendfeedback-tool-behavior). Requires Claude Code v2.1.238 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No                  |
| `SendMessage`          | Sends a message to another agent: an [agent team](/docs/en/agent-teams) teammate, a [subagent it resumes](/docs/en/sub-agents#resume-subagents) by agent ID or name, or one of your other Claude Code sessions, on this machine or beyond it. Messaging other sessions requires Claude Code v2.1.224 or later. [Cross-session messaging](/docs/en/cross-session-messaging) covers which sessions Claude can reach, [what a message looks like when it arrives](/docs/en/cross-session-messaging#what-a-message-looks-like), and [how Claude gets a notice when another session goes idle](/docs/en/cross-session-messaging#get-a-notice-when-another-session-goes-idle). Claude can include an optional `summary` input, typically 5-10 words, that Claude Code shows as a one-line preview. When Claude omits it on a [plain-text message](/docs/en/cross-session-messaging#limitations), Claude Code uses the first line of the message as the summary. Claude Code truncates a summary longer than 200 characters with an ellipsis | No                  |
| `SendUserFile`         | Sends files from the session to you with an optional caption, so a generated report, diagram, screenshot, or built artifact reaches your device instead of only being mentioned in the transcript. As of v2.1.196, the optional `display` input controls presentation: `render` opens the file inline in the client, `attach` shows a download card only, and when unset the client decides by file type. Available when a [Remote Control](/docs/en/remote-control) client is connected or in a [cloud session](/docs/en/claude-code-on-the-web). Delivery runs through Anthropic-hosted infrastructure, so the tool is not available on Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry                                                                                                                                                                                                                                                                                                     | No                  |
| `ShareOnboardingGuide` | Uploads `ONBOARDING.md` and returns a share link teammates can open in Claude Code. Called from `/team-onboarding` after the guide is written. Available to claude.ai subscribers on Pro, Max, Team, and Enterprise plans                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes                 |
| `Skill`                | Executes a [skill](/docs/en/skills#control-who-invokes-a-skill) within the main conversation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes                 |
| `SubagentHandback`     | Delivers a subagent's final report to whichever conversation receives that subagent's result. Provided only in [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode), to subagents that the Agent tool runs locally other than [forks](/docs/en/sub-agents#fork-the-current-conversation), and available in the terminal CLI, IDE extensions, cloud sessions, and the Agent SDK; the classifier reviews the report before it's delivered. Requires Claude Code v2.1.271 or later                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                  |
| `TaskCreate`           | Creates a new task in the task list. Provided by default only on the models listed under [Task tool availability](#task-tool-availability), and on other models when you opt in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No                  |
| `TaskGet`              | Retrieves full details for a specific task. Provided by default only on the models listed under [Task tool availability](#task-tool-availability), and on other models when you opt in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No                  |
| `TaskList`             | Lists all tasks with their current status. Provided by default only on the models listed under [Task tool availability](#task-tool-availability), and on other models when you opt in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No                  |
| `TaskOutput`           | Retrieves output from a background task. Deprecated in favor of `Read` on the task's output file path. When no task matches the ID, the error lists the running background agents by ID and description. Before v2.1.203, the error named only the missing ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                  |
| `TaskStop`             | Stops a running background task by ID. It also accepts an [agent-team teammate](/docs/en/agent-teams) or a named background agent by agent ID or name. Before v2.1.198, it accepted only a background task ID. When no task matches the ID, the error lists the running background agents by ID and description, including agents that another agent spawned. Before v2.1.203, the error listed running teammates and named agents but not background agents another agent spawned, so those couldn't be identified or stopped from the main conversation                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No                  |
| `TaskUpdate`           | Updates task status, dependencies, details, or deletes tasks. Provided by default only on the models listed under [Task tool availability](#task-tool-availability), and on other models when you opt in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                  |
| `TodoWrite`            | Manages the session task checklist. Disabled by default in favor of `TaskCreate`, `TaskGet`, `TaskList`, and `TaskUpdate`. Set `CLAUDE_CODE_ENABLE_TASKS=0` to re-enable it in [sessions that have the task-tracking tools](#task-tool-availability)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No                  |
| `ToolSearch`           | Searches for and loads deferred tools when [tool search](/docs/en/mcp#scale-with-mcp-tool-search) is enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No                  |
| `WaitForMcpServers`    | Waits for one or more [MCP servers](/docs/en/mcp) that are still connecting in the background, so a request can use their tools without restarting the session. Claude calls it when a needed server isn't connected yet. Only appears when [tool search](/docs/en/mcp#scale-with-mcp-tool-search) is disabled, since `ToolSearch` handles the wait when it's enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No                  |
| `WebFetch`             | Fetches content from a specified URL. See [WebFetch tool behavior](#webfetch-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes                 |
| `WebSearch`            | Performs web searches. See [WebSearch tool behavior](#websearch-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes                 |
| `Workflow`             | Runs a [dynamic workflow](/docs/en/workflows): a script that orchestrates many subagents in the background and returns one consolidated result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes                 |
| `Write`                | Creates or overwrites files. See [Write tool behavior](#write-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes                 |

## Configure tools with permission rules and hooks

For the most part, Claude decides when to use these tools and you don't need to name them yourself when interacting with Claude. You reference tool names directly when defining permissions and other configuration:

* in [`permissions.allow`](/docs/en/settings-reference#permissions-allow) and [`permissions.deny`](/docs/en/settings-reference#permissions-deny) in settings, and the `/permissions` interface
* in the `--allowedTools` and `--disallowedTools` [CLI flags](/docs/en/cli-reference)
* in the Agent SDK's [`allowedTools` and `disallowedTools`](/docs/en/agent-sdk/permissions#allow-and-deny-rules) options
* in a [skill's `allowed-tools`](/docs/en/skills#frontmatter-reference) frontmatter
* in a hook's [`if` condition](/docs/en/hooks-guide#filter-by-tool-name-and-arguments-with-the-if-field)

All of these accept the same rule format, `ToolName(specifier)`. The specifier depends on the tool, and several tools share a format:

| Rule format                    | Applies to                | Details                                                          |
| :----------------------------- | :------------------------ | :--------------------------------------------------------------- |
| `Bash(npm run *)`              | Bash, Monitor             | [Command pattern matching](/docs/en/permissions#bash)                 |
| `PowerShell(Get-ChildItem *)`  | PowerShell                | [Command pattern matching](/docs/en/permissions#powershell)           |
| `Read(~/secrets/**)`           | Read, Grep, Glob, LSP     | [Path pattern matching](/docs/en/permissions#read-and-edit)           |
| `Edit(/src/**)`                | Edit, Write, NotebookEdit | [Path pattern matching](/docs/en/permissions#read-and-edit)           |
| `Skill(deploy *)`              | Skill                     | [Skill name matching](/docs/en/skills#restrict-claude’s-skill-access) |
| `Agent(Explore)`               | Agent                     | [Subagent type matching](/docs/en/permissions#agent-subagents)        |
| `WebFetch(domain:example.com)` | WebFetch                  | [Domain matching](/docs/en/permissions#webfetch)                      |
| `WebSearch`                    | WebSearch                 | No specifier; allow or deny the tool as a whole                  |

Tools not listed here, such as `ExitPlanMode` or `ShareOnboardingGuide`, accept only the bare tool name with no specifier.

An `Edit(...)` allow rule also grants read access to the same path, so you don't need a matching `Read(...)` rule. A `Read(...)` deny rule also blocks the Edit and Write tools on the same path, including creating a new file there, because both tools change content Claude has to be able to read back. The `Read` deny check requires Claude Code v2.1.208 or later on edits, and v2.1.228 or later on writes.

Hook `matcher` fields use bare tool names, not the parenthesized rule format. See [matcher patterns](/docs/en/hooks#matcher-patterns) for the matching rules. For the field names each tool passes to `tool_input` in hooks, see the [PreToolUse input reference](/docs/en/hooks#pretooluse-input).

## Agent tool behavior

The Agent tool spawns a subagent in a separate context window. The subagent works through its task autonomously, then returns its result to the parent conversation. The parent doesn't see the subagent's intermediate tool calls or outputs, only that final result. With [agent teams](/docs/en/agent-teams) enabled, a call that carries a `name` can launch a [teammate](/docs/en/agent-teams#how-claude-starts-agent-teams) instead, which reports back through team messages rather than by returning a result.

To cap how many turns a subagent runs, set `maxTurns` in the [subagent definition](/docs/en/sub-agents#supported-frontmatter-fields). When the subagent reaches the limit, Claude Code marks the returned result as partial output, and Claude can [resume the subagent](/docs/en/sub-agents#resume-subagents) to continue.

The same Agent tool also launches [forked subagents](/docs/en/sub-agents#fork-the-current-conversation) wherever [fork mode](/docs/en/sub-agents#turn-fork-mode-on-or-off) is on. A fork inherits the full parent conversation instead of starting fresh, runs in the background apart from the [cases that stay in the foreground](/docs/en/sub-agents#run-subagents-in-foreground-or-background), and still surfaces permission prompts in your terminal. The rest of this section describes non-fork subagents.

Which tools a non-fork subagent can use depends on the `tools` and `disallowedTools` fields in the [subagent definition](/docs/en/sub-agents):

* **Neither field set**: the subagent inherits every [tool available to subagents](/docs/en/sub-agents#available-tools).
* **`tools` only**: the subagent gets only the listed tools.
* **`disallowedTools` only**: the subagent gets every parent tool except the listed ones.
* **Both set**: `disallowedTools` takes precedence. A tool listed in both is removed.

In every case, the resolved set is limited to the [tools available to subagents](/docs/en/sub-agents#available-tools): a tool that isn't available to subagents is never granted, even when listed in `tools`. Where the conditions in the `SubagentHandback` tools-table entry hold, Claude Code also gives the subagent that tool, even if you leave it out of `tools` or list it in `disallowedTools`.

If every entry in a subagent's `tools` list fails to match a usable tool, the Agent tool usually returns an error naming the entries instead of launching the subagent; see [Agent would be spawned with zero tools](/docs/en/errors#agent-would-be-spawned-with-zero-tools) for the message and how to fix each entry.

Launching the subagent doesn't itself prompt for permission. Claude Code checks the subagent's own tool calls against your permission rules as it runs.

Where you see a subagent's permission prompts depends on whether it runs in the foreground or the background. Claude Code runs subagents in the background by default, apart from the [cases that run in the foreground](/docs/en/sub-agents#run-subagents-in-foreground-or-background).

* **Foreground subagents** show the same permission prompts you would see in the main conversation, at the moment each tool call happens.
* **Background subagents** surface permission prompts in your main session as of v2.1.186. The prompt names which subagent is asking, and pressing Esc denies that one tool call without stopping the subagent. Before v2.1.186, background subagents auto-denied any tool call that would otherwise prompt and continued without that tool.

To [limit what a subagent can reach](/docs/en/sub-agents#control-subagent-capabilities) in the first place, narrow its `tools` field, for example by leaving Bash off the list, or set deny rules in your settings.

## AskUserQuestion tool behavior

Claude uses `AskUserQuestion` to ask you multiple-choice questions when it needs a decision or a clarification. Answer by picking an option, or type your own text through the `Other` row or the notes field.

When you answer by typing your own text, Claude Code relays the answer with neutral wording so Claude follows what you wrote, including a request to wait or explain first.

### Question auto-continue timeout

Questions stay open until you answer them. If you want a question you leave unanswered to eventually close and let Claude continue without you, set the [`askUserQuestionTimeout`](/docs/en/settings-reference#askuserquestiontimeout) setting to `60s`, `5m`, or `10m`, either in your user `settings.json` or from the **Question auto-continue timeout** row in `/config`.

After a question sits that long with no input, the dialog closes on its own: it submits any options you'd already selected and tells Claude you may be away from your keyboard, so Claude proceeds on its own judgment and can re-ask later. You see a countdown for the last 20 seconds. Press any key to restart the timer; on terminals that report focus, switching to the window restarts it too.

The timeout applies only to `AskUserQuestion`'s multiple-choice questions; permission prompts, including plan approval, never auto-resolve on idle.

## Bash tool behavior

The Bash tool runs each command in a separate process.

### What persists between commands

* When Claude runs `cd` in the main session, the new working directory carries over to later Bash commands as long as it stays inside the project directory or an [additional working directory](/docs/en/permissions#working-directories) you added with `--add-dir`, `/add-dir`, or `additionalDirectories` in settings. This includes commands Claude runs in response to your later messages.
  * Subagent sessions never carry over working directory changes.
  * If `cd` lands outside those directories, Claude Code resets to the project directory and appends `Shell cwd was reset to <dir>` to the tool result.
  * To disable this carry-over so every Bash command starts in the project directory, set `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1`.
* Environment variables don't persist. An `export` in one command won't be available in the next.
* Aliases and shell functions defined in your shell startup file are available. At session start, Claude Code sources `~/.zshrc`, `~/.bashrc`, or `~/.profile` depending on your shell, captures the resulting aliases, functions, and shell options, and applies them to every Bash command.

Activate your virtualenv or conda environment before launching Claude Code. To make environment variables persist across Bash commands, set [`CLAUDE_ENV_FILE`](/docs/en/env-vars) to a shell script before launching Claude Code, or use a [SessionStart hook](/docs/en/hooks#persist-environment-variables) to populate it dynamically.

### Timeout and output limits

Each command runs under a timeout, and Claude manages it: when it wants longer than the default for a command, it passes the `timeout` parameter with that call — you never set a per-command timeout. Two [environment variables](/docs/en/env-vars) bound what Claude gets:

* `BASH_DEFAULT_TIMEOUT_MS` — the default when Claude passes no timeout; two minutes out of the box
* `BASH_MAX_TIMEOUT_MS` — with the default, sets the ceiling that caps whatever Claude requests: the effective ceiling is the larger of the two, ten minutes out of the box

#### Output limits

Claude Code streams a command's output to a working file as the command runs; a command whose output passes 5 GB is killed. When the command finishes, Claude Code reads the output back from that file, up to the read-back window described below. How much of the output reaches Claude inline depends on whether Claude Code treats the result as a failure:

| Result  | What Claude gets                                                                                                                                                                                                                                            |
| :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Valid   | Inline up to roughly 30,000 characters by default; past that, the path of a file saved to the session directory and truncated past 64 MiB, plus a preview of up to the first 2,000 characters, and Claude reads or searches the file when it needs the rest |
| Failure | Inline up to roughly 10,000 characters; past that, a head-and-tail excerpt of that size cut from the read-back window, with no file path                                                                                                                    |

A command that exits 1 counts as a valid result for the Bash tool only when Claude Code recognizes exit code 1 as a benign outcome for that command: `grep`, `rg`, `egrep`, `fgrep`, `find`, `diff`, `test`, and `[`, plus `git diff` and `git grep`. Every other command that exits 1 counts as a failure, even when exit 1 is a benign informational outcome: no matches for `pgrep` and `jq -e`, files that differ for `cmp`.

[`BASH_MAX_OUTPUT_LENGTH`](/docs/en/env-vars) sets how many characters of output Claude Code reads back from the working file into a command's result: 30,000 by default, up to a hard ceiling of 150,000. Raise it when your commands routinely overflow that window, such as a verbose build or a full test-suite log. Raising it enlarges the read-back window, which is also the window a failing command's excerpt is cut from. It doesn't raise the inline ceilings: a valid result over the inline ceiling arrives as a file path plus preview regardless of this variable.

To change how much of a valid result Claude receives inline, set the [`bashOutputMaxChars`](/docs/en/settings-reference#bashoutputmaxchars) setting instead, up to 128,000 characters. It sizes the inline ceiling and the read-back window together, and Claude Code then ignores `BASH_MAX_OUTPUT_LENGTH`. Requires Claude Code v2.1.261 or later.

### Background commands

For long-running processes such as dev servers or watch builds, Claude can set `run_in_background: true` to start the command as a background task and continue working while it runs. List and stop background tasks with `/tasks`. After you stop one there, or from a connected client such as the desktop app, Claude moves on instead of waiting for it. If a subagent started the command, it's that subagent that moves on.

A command that a [foreground subagent](/docs/en/sub-agents#run-subagents-in-foreground-or-background) started stops when that subagent gives its final response. A command that the main conversation or a background subagent started keeps running after a final response. In non-interactive mode with the `-p` flag, [background commands end shortly after the run's final result](/docs/en/headless#background-tasks-at-exit).

When a command reaches its timeout without finishing, Claude Code moves it to the background instead of stopping it, unless the command starts with `sleep`. Claude keeps working while the command continues. Claude Code applies the same lifetime rules to a moved command as to any other background command, so it still ends a foreground subagent's command at that subagent's final response. Setting [`CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`](/docs/en/env-vars#variables) disables auto-backgrounding along with the rest of the background task functionality.

The result of a command moved to the background states what happened:

* When the timeout triggers the move, the result reports it explicitly: `Command did not complete within its 120s timeout and was moved to the background`, with the seconds matching the timeout that applied, followed by the task ID and the path of the file the output is being written to.
* A `cd`, `pushd`, `popd`, or `chdir` inside a command that is moved to the background never carries over: the result states `Session cwd remains <dir>; directory changes made by the backgrounded command do not apply to subsequent commands.`, so Claude doesn't act on a directory change that didn't happen.

### Memory limit on Linux and WSL

On Linux and WSL, set [`CLAUDE_CODE_TOOL_MEMORY_LIMIT`](/docs/en/env-vars#variables) to a size such as `4G` to cap the memory that Bash, PowerShell, and [Monitor](#monitor-tool) tool commands can use, so one runaway build can't take the memory the rest of the session needs. Requires Claude Code v2.1.233 or later. Before v2.1.246, Monitor tool commands ran outside the cap.

* Write the size as a number of bytes or with a `K`, `M`, `G`, or `T` suffix. Set `0`, `off`, `false`, `no`, or `none` to turn the cap off. Claude Code ignores any other value it can't read as a size, such as `4e9`.
* Claude Code counts all of a session's Bash, PowerShell, and Monitor commands against the one cap, not each command on its own.
* Claude Code applies the cap with a memory cgroup. When it can't set the cgroup up, commands run without a cap, and the debug log from `claude --debug` says why.
* After the first process Claude Code starts has turned the cap on, or has turned it off because of an off value or a failed cgroup setup, Claude Code holds that result until you relaunch. To apply a changed or removed value, or a fixed setup, launch `claude` again.
* When commands can't stay under the cap, the kernel kills a command, and nothing in its result names the cap.

Claude Code can also count other kinds of processes it starts against the same limit. Set [`CLAUDE_CODE_TOOL_MEMORY_CGROUP_EXCLUDE`](/docs/en/env-vars#variables) to a comma-separated list of the kinds to exempt from the cap; Claude Code applies the cap to every kind not on your list. Set it to `none` to cap every kind, or to `all-new` to cap only Bash, PowerShell, and Monitor tool commands. Requires Claude Code v2.1.246 or later. The kinds you can name:

* `mcp`: local [MCP servers](/docs/en/mcp)
* `lsp`: [language servers](#lsp-tool-behavior)
* `hooks`: [hook](/docs/en/hooks) commands
* `plugin`: commands that [plugins](/docs/en/plugins) run
* `helper`: Claude Code's own helper commands, such as `git`
* `agent`: child Claude Code processes, such as [agent teammates](/docs/en/agent-teams)

Whatever you list, these rules apply:

* **Unknown names**: Claude Code ignores names it doesn't recognize
* **Bash, PowerShell, and Monitor**: Claude Code keeps Bash, PowerShell, and Monitor tool commands under the cap whatever you list
* **Variable unset**: Claude Code takes the set of other capped kinds from configuration Anthropic delivers from the server, and that set can change over time, so set the variable when you need a set that doesn't change
* **Permission-gating hooks**: even with every kind capped, Claude Code excludes from the cap a hook that can block or change the outcome of an action, and any MCP server that such a hook calls, so the kernel killing a permission-gating hook can't allow the action it was blocking

## Edit tool behavior

The Edit tool performs exact string replacement. It takes an `old_string` and a `new_string` and replaces the first with the second. It doesn't use regex or fuzzy matching.

Three checks must pass for an edit to apply. Before any of them, a path matched by a [`Read` deny rule](/docs/en/permissions#tool-specific-permission-rules) is refused, including creating a new file there. The refusal requires Claude Code v2.1.208 or later.

* **Read-before-edit**: Claude reads the file in the current conversation before editing it, and a read cut short with a [`PARTIAL view` notice](#read-tool-behavior) doesn't count. Claude Opus 4.6, Claude Haiku 4.5, and older models always require the read. Newer models can edit an unread file when reading it wouldn't need a permission prompt and the Read tool is available.
* **Match**: `old_string` must appear in the file exactly as written. A single character of whitespace or indentation difference is enough to miss.
* **Uniqueness**: `old_string` must appear exactly once. When it appears more than once, Claude either supplies a longer string with enough surrounding context to pin down one occurrence, or sets `replace_all: true` to replace them all.

A file that changed on disk after Claude last read it can still be edited when `old_string` matches the current content exactly and unambiguously and Claude Code can read the file without prompting. Matching against the file's current content keeps this safe, and the result notes that the file carries other changes so Claude re-reads it before edits that depend on surrounding content. In any other case, such as a stale `old_string` or one that matches more than once without `replace_all`, Claude reads the file again before editing. The relaxed handling of unread and changed files requires Claude Code v2.1.208 or later; before that, Claude Code refused any edit to a file it hadn't read in the conversation or that changed on disk after the read.

Viewing a file with Bash also satisfies the read-before-edit requirement when the command is `cat`, `nl`, `bat`, `batcat`, `head`, `tail`, `sed -n 'X,Yp'`, `grep`, `egrep`, `fgrep`, or `rg` on a single file with no pipes or redirects. Piped output and other Bash commands don't count toward the read-before-edit check.

Viewing a file with Bash affects edit eligibility only, not permissions. See [Read and Edit permission rules](/docs/en/permissions#read-and-edit) for which Bash commands your `Read` and `Edit` deny rules cover.

## EndConversation tool behavior

The EndConversation tool ends the current session. Claude uses it only in two situations:

* as a last resort against sustained abusive input, after attempts to redirect the conversation have failed and after a clear warning in an earlier message
* when you explicitly ask to see the tool demonstrated and confirm that you want the session to end

General frustration, profanity, or a task going badly don't qualify, and neither do requests for harmful content, which Claude declines instead of ending the session. Claude Code follows the same approach as claude.ai, which can [end a rare subset of chats](https://www.anthropic.com/research/end-subset-conversations).

After Claude ends an interactive session, the session locks. New prompts and most commands return `Claude ended this conversation. Start a new session (or /clear) to continue.`, and only `/clear`, `/resume`, `/help`, `/exit`, and `/feedback` still run. Claude Code records the end in the session's transcript, so resuming an ended session restores the lock; the session's history isn't deleted.

Resuming an ended session in [non-interactive mode](/docs/en/headless) with the `-p` flag errors and exits with code 1, so a script doesn't read the ended run as a success.

The tool never prompts for permission, and [PreToolUse hooks](/docs/en/hooks#pretooluse) don't run for it. While any other tool remains, you can't block it either: [deny and ask rules](/docs/en/permissions#tool-specific-permission-rules) naming `EndConversation` have no effect, and neither `--disallowedTools` nor a `--tools` list can remove it. The exemption is deliberate: the tool does nothing except end the conversation, never reading or modifying files or data, and a safeguard of this kind holds only if the session it applies to can't turn it off. When your deny rules remove every other tool and also match `EndConversation`, as `"*"` does, Claude Code removes it too rather than leaving it as the only tool, unless an allow rule names `EndConversation` explicitly. A deny list that removes every other tool without matching `EndConversation` leaves it in place.

[Subagents](/docs/en/sub-agents) never get the tool. Background tasks that share the main conversation's tool list see it, but calling it there ends nothing.

The tool appears only when all of the following are true:

* **Version**: Claude Code v2.1.213 or later.
* **Model**: the session's model is Claude Opus 4.8, Claude Sonnet 5, Claude Fable 5, or a later version of one of those families.
* **Surface**: an interactive terminal session, including a `claude` session in an IDE's integrated terminal, which is how the [JetBrains plugin](/docs/en/jetbrains) runs it. Other surfaces don't include the tool, such as:
  * non-interactive `-p` runs
  * sessions through the [Agent SDK](/docs/en/agent-sdk/overview) TypeScript and Python packages
  * the [VS Code extension](/docs/en/vs-code) panel, which bundles its own CLI
  * [GitHub Actions](/docs/en/github-actions)
  * [cloud sessions](/docs/en/claude-code-on-the-web)
* **Startup mode**: not a [`--bare`](/docs/en/headless#start-faster-with-bare-mode) session. Bare mode loads only shell and file tools, so the tool is never registered there.
* **Provider**: not available on [Amazon Bedrock](/docs/en/amazon-bedrock), [Claude Platform on AWS](/docs/en/claude-platform-on-aws), [Google Cloud's Agent Platform](/docs/en/google-vertex-ai), or [Microsoft Foundry](/docs/en/microsoft-foundry), or on sessions signed in through a [cloud gateway](/docs/en/claude-apps-gateway).

## Glob tool behavior

The Glob tool finds files by name pattern. On Windows, it's part of the default tool set. On macOS, Linux, and WSL, Claude Code leaves Glob and [Grep](#grep-tool-behavior) out of the default tool set, and Claude searches with `find` and `grep` through the Bash tool instead. In Claude's shell those two commands run embedded versions of `bfs` and `ugrep`, and the searches reach your hooks and permission rules as `Bash` calls.

On macOS, Linux, and WSL, you get the Glob and Grep tools back in these cases:

* You name `Glob` or `Grep` in [`--tools` or `--allowedTools`](/docs/en/cli-reference#cli-flags) when you start the session, or in the equivalent [Agent SDK](/docs/en/agent-sdk/overview) options. With `--tools` you get the ones you list, and naming either tool in `--allowedTools` restores both. An allow rule in a settings file doesn't have this effect.
* A permissions [deny rule](/docs/en/permissions#match-all-uses-of-a-tool), the `--disallowedTools` flag, or [`--restricted`](/docs/en/cli-reference#cli-flags) removes `Bash` from the session.
* A [subagent](/docs/en/sub-agents#available-tools) lists `Glob` or `Grep` in its `tools` field and leaves out `Bash`. The listed tools come back for that subagent only, or for the whole session when it runs as the main session agent through [`--agent`](/docs/en/sub-agents#invoke-subagents-explicitly) or the `agent` setting.

Glob supports standard glob syntax including `**` for recursive directory matching:

* `**/*.js` matches all `.js` files at any depth
* `src/**/*.ts` matches all `.ts` files under `src/`
* `*.{json,yaml}` matches `.json` and `.yaml` files in the current directory

Results are sorted by modification time and capped at 100 files. If the cap is hit, Claude sees a truncation flag in the result and can narrow the pattern.

Glob doesn't respect `.gitignore` by default, so it finds gitignored files alongside tracked ones. This differs from [Grep](#grep-tool-behavior), which skips gitignored files. To make Glob respect `.gitignore`, set `CLAUDE_CODE_GLOB_NO_IGNORE=false` before launching Claude Code.

Claude Code decides permission for a Glob call before it checks whether the search directory exists. It still runs the read-permission check for a missing `path` outside the [working directories](/docs/en/permissions#working-directories), so a permission prompt for a path doesn't mean the path exists.

A `pattern` or `path` value that contains a null byte returns an error asking Claude to remove it.&#x20;

## Grep tool behavior

The Grep tool searches file contents for patterns. Where [Glob](#glob-tool-behavior) finds files by name, Grep finds lines inside them. On macOS, Linux, and WSL, Grep is absent by default under the same conditions as Glob. See [Glob tool behavior](#glob-tool-behavior) for when both tools are available.

Grep is built on [ripgrep](https://github.com/BurntSushi/ripgrep) and uses ripgrep's regex syntax, not POSIX grep. Patterns that include regex metacharacters need escaping. For example, finding `interface{}` in Go code takes the pattern `interface\{\}`.

A pattern, glob, or file type that ripgrep rejects returns an error that includes ripgrep's diagnostic, so Claude can correct the input and search again. Before v2.1.208, Claude Code reported a rejected input as `No files found` instead of an error, even when the searched-for text existed in the target files.

Three output modes control what comes back:

* `files_with_matches`: file paths only, no line content. This is the default.
* `content`: matching lines with file and line number. When the tool's `offset` parameter points past the last match for a pattern that has matches, Grep returns `No entries at this offset`, so Claude widens or resets the offset instead of concluding the pattern doesn't match.
* `count`: match count per file, followed by a total across all matching files. The total covers every match even when the tool's `head_limit` or `offset` parameters truncate the listed per-file entries. Before v2.1.208, the total only summed the listed entries.

Claude can scope results by file with the `glob` parameter, such as `**/*.tsx`, or by language with the `type` parameter, such as `py` or `rust`. By default, patterns match within a single line. Claude can set `multiline: true` to match across line boundaries.

Grep respects `.gitignore`, so gitignored files are skipped. To search a gitignored file, Claude passes its path directly.

Claude Code decides permission for a Grep call before it checks whether the search `path` exists. It still runs the read-permission check for a missing `path` outside the [working directories](/docs/en/permissions#working-directories), so a permission prompt for a path doesn't mean the path exists.

## LSP tool behavior

The LSP tool gives Claude code intelligence from a running language server. After each file edit, it automatically reports type errors and warnings so Claude can fix issues without a separate build step. Claude can also call it directly to navigate code:

* Jump to a symbol's definition
* Find all references to a symbol
* Get type information at a position
* List symbols in a file
* Search for a symbol by name across the workspace
* Find implementations of an interface
* Trace call hierarchies

Claude Code keeps the tool inactive until you install a [code intelligence plugin](/docs/en/discover-plugins#code-intelligence) for your language. In [cloud sessions](/docs/en/claude-code-on-the-web), Claude Code doesn't start plugin language servers, so the LSP tool stays inactive there. Claude Code takes the language server's configuration from the plugin, and you install the server binary yourself.

Claude Code returns an error result for each LSP call on a file whose language server it can't start.

## Monitor tool

The Monitor tool lets Claude watch something in the background and react when it changes, without pausing the conversation. Ask Claude to:

* Tail a log file and flag errors as they appear
* Poll a PR or CI job and report when its status changes
* Watch a directory for file changes
* Track output from any long-running script you point it at
* Connect to a WebSocket feed and report each message as it arrives

For most watches, Claude writes a small script, runs it in the background, and receives each output line as it arrives. For a server that already pushes events, Claude can open a [WebSocket](#websocket-source) instead of running a script.

You keep working in the same session and Claude interjects when an event arrives.

Every watch Claude starts has a deadline: 5 minutes by default, at most 30 minutes, and at most 10 minutes in a [non-interactive](/docs/en/headless) run given a single prompt with `-p`.

At the deadline the watch ends. Claude gets one notice, so it can start the watch again if it's still needed.

Stop a monitor by asking Claude to cancel it or by ending the session. When you stop a [subagent](/docs/en/sub-agents) that started monitors, for example from `/tasks`, those monitors stop with it.

When Monitor runs a command, it uses the same [permission rules as Bash](/docs/en/permissions#tool-specific-permission-rules), so `allow` and `deny` patterns you have set for Bash apply here too. While [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) is active, Claude Code sets aside allow rules that name `Monitor` itself, along with the other [broad allow rules it drops](/docs/en/permission-modes#how-the-classifier-evaluates-actions), so the classifier reviews Monitor commands the same way it reviews Bash commands.

The [WebSocket source](#websocket-source) has its own approval prompt, which the classifier also decides in auto mode.

The tool is not available on Amazon Bedrock, Google Cloud's Agent Platform, or Microsoft Foundry. It is also not available when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set.

Plugins can declare monitors that start automatically when the plugin is active, instead of asking Claude to start them. See [plugin monitors](/docs/en/plugins-reference#monitors).

### WebSocket source

<Note>
  The WebSocket source requires Claude Code v2.1.195 or later.
</Note>

When a server already pushes events over a WebSocket, Claude can connect to it directly instead of writing a polling script. Each kind of socket activity either becomes an event or ends the watch:

* **Text messages**: each one becomes one event, even when the message spans multiple lines.
* **Binary messages**: not passed through. Claude receives a placeholder line such as `[binary frame, 512 bytes]` instead.
* **Messages larger than 1 MiB**: the watch ends, so subscribe to a filtered feed where one exists.
* **Socket close**: the watch ends and Claude receives the close code.

A WebSocket watch takes a `ws` input in place of `command`, and a single Monitor call can't combine the two. The `ws` input has two fields:

| Field       | Required | Description                                                                                                                                    |
| :---------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`       | Yes      | The endpoint to connect to. Must be a `ws://` or `wss://` URL with no embedded credentials or whitespace, using ASCII characters only          |
| `protocols` | No       | WebSocket subprotocol names to offer during the handshake. Each entry must be a valid subprotocol token, and the list can't contain duplicates |

The `timeout_ms` deadline applies to a WebSocket watch too: the watch ends at the deadline, and `TaskStop` cancels it early.

Opening a WebSocket prompts for approval; in [auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) the classifier decides instead. The prompt doesn't offer an option to skip future prompts for the same host.

Claude Code denies URLs that point at a private, link-local, or cloud-metadata address, including hostnames that resolve to one. It also denies hosts in `sandbox.network.deniedDomains`, and when [`allowManagedDomainsOnly`](/docs/en/settings-reference#sandbox-network-allowmanageddomainsonly) is set in managed settings, any host outside the managed allowlist.

## NotebookEdit tool behavior

NotebookEdit modifies a Jupyter notebook one cell at a time, targeting cells by their `cell_id`. It doesn't perform string replacement across the notebook the way [Edit](#edit-tool-behavior) does on plain files.

Three edit modes control what happens to the target cell:

* `replace`: overwrite the cell's source. This is the default.
* `insert`: add a new cell after the target. With no `cell_id`, the new cell goes at the start of the notebook. Requires `cell_type` set to `code` or `markdown`.
* `delete`: remove the target cell.

Permission rules use the `Edit(...)` path format. A rule like `Edit(notebooks/**)` covers NotebookEdit calls on files in that directory.

## PowerShell tool

The PowerShell tool lets Claude run PowerShell commands natively. On Windows, this means commands run in PowerShell instead of routing through Git Bash. How the tool becomes available depends on your platform:

* **Windows without Git Bash**: the tool is enabled automatically.
* **Windows with Git Bash installed**: the tool is on by default for claude.ai and Console accounts; set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` to enable it in Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry sessions, or `0` to turn it off.
* **Linux, macOS, and WSL**: the tool is opt-in.

Your [PreToolUse hooks](/docs/en/hooks#powershell) receive the tool's command string in `tool_input.command`, with the same fields as the Bash tool.

Match `Bash|PowerShell` in hooks that inspect shell commands; the [PowerShell hook input section](/docs/en/hooks#powershell) explains why matching `Bash` alone is not enough.

### Enable the PowerShell tool

Set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` in your environment or in `settings.json`:

```json theme={null}
{
  "env": {
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"
  }
}
```

On Windows, set the variable to `0` to turn the tool off. On Linux, macOS, and WSL, the tool requires PowerShell 7 or later: install `pwsh` and ensure it is on your `PATH`.

On Windows, Claude Code auto-detects `pwsh.exe` for PowerShell 7+ with a fallback to `powershell.exe` for PowerShell 5.1. When the tool is enabled, Claude treats PowerShell as the primary shell. The Bash tool remains available for POSIX scripts when Git Bash is installed.

Claude Code spawns PowerShell with `-ExecutionPolicy Bypass` at process scope only, so `.ps1` scripts and module imports work on default Windows installs without changing the machine's policy. Process-scope bypass doesn't override Group Policy `MachinePolicy` or `UserPolicy`, so enterprise policies still apply. To respect the machine's effective execution policy instead, set `CLAUDE_CODE_POWERSHELL_RESPECT_EXECUTION_POLICY=1`.

### Shell selection in settings, hooks, and skills

Three additional settings control where PowerShell is used:

* `"defaultShell": "powershell"` in [`settings.json`](/docs/en/settings-reference#all-settings): routes interactive `!` commands through PowerShell. Requires the PowerShell tool to be enabled.
* `"shell": "powershell"` on individual [command hooks](/docs/en/hooks#command-hook-fields): runs that hook in PowerShell. Hooks spawn PowerShell directly, so this works regardless of `CLAUDE_CODE_USE_POWERSHELL_TOOL`.
* `shell: powershell` in [skill frontmatter](/docs/en/skills#frontmatter-reference): runs `` !`command` `` blocks in PowerShell. Requires the PowerShell tool to be enabled.

The same main-session working-directory reset behavior described under the Bash tool section applies to PowerShell commands, including the `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` environment variable.

As of v2.1.196, exit code 1 from `grep`, `rg`, `egrep`, `fgrep`, `findstr`, and `git grep` means no matches. Exit code 1 from `git diff` means differences exist. Neither result is reported to Claude as a command failure. For `robocopy`, exit codes 0 through 7 are informational results, such as files copied or extra files detected. Exit codes of 8 or higher count as failures.

### Windows encoding and exit codes

On Windows, the following PowerShell encoding and exit-code behaviors require Claude Code v2.1.214 or later:

* Redirection with `>` and `>>` writes UTF-8 files on PowerShell 5.1
* Claude Code encodes text piped to a native command's standard input as UTF-8
* Claude Code captures error output without ANSI escape sequences
* A command whose child process waits on standard input receives end-of-file instead of hanging
* Exit code 1 from `where.exe` means no match, and from `fc.exe` and `diff.exe` it means the files differ, so when the command produces output, Claude Code treats that exit code as a valid negative answer rather than a command error. Claude Code still reports a silenced form, such as `where.exe /Q` or a redirect to `$null`, as a failure on exit code 1

Before v2.1.214, `>` on PowerShell 5.1 wrote UTF-16LE files, non-ASCII piped input arrived as `?`, and Python scripts could crash with a `UnicodeEncodeError` when printing non-ASCII characters.

### Preview limitations

The PowerShell tool has the following known limitations during the preview:

* PowerShell profiles are not loaded
* On Windows, sandboxing is not supported

## Read tool behavior

The Read tool takes a file path and returns the contents with line numbers. Claude is instructed to always pass absolute paths.

By default, Read returns the file from the start. When a whole-file read exceeds the token limit, Read returns the first page with a `PARTIAL view` notice that tells Claude how much of the file it received and how to read more with `offset` and `limit`. A read that passes an explicit `offset` or `limit` and still exceeds the token limit returns an error.

A read with an explicit `limit` stops as soon as the selected lines exceed what the token limit could ever fit and returns an error without loading the rest of the range. The error tells Claude to use a smaller `limit`, or to search for specific content with [Grep](#grep-tool-behavior) instead when a single line is that large. Before v2.1.208, Claude Code loaded the whole range into memory before rejecting it, so reading a file with an extremely long single line could run it out of memory.

Reading an empty file returns a notice that the file exists but its contents are empty, and an `offset` past the last line returns a notice giving the file's line count. Before v2.1.208, reading an empty file returned the past-the-end notice instead.

Read handles several file types beyond plain text:

* **Images**: PNG, JPG, and other image formats are returned as visual content that Claude can see, not as raw bytes. Claude Code resizes and recompresses large images to fit the model's image size limits before sending them, so Claude may see a downscaled version of a large screenshot. As of v2.1.196, an image that is still larger than 500KB after that resize is re-encoded as a JPEG at reduced quality with its pixel dimensions unchanged. If Claude misses fine pixel-level detail in a large image, ask it to crop the region of interest first, for example with ImageMagick via Bash.
* **PDFs**: Claude reads short `.pdf` files whole. For PDFs longer than 10 pages, it reads in ranges with a `pages` parameter, such as `"1-5"`, up to 20 pages at a time.
* **Jupyter notebooks**: `.ipynb` files return all cells with their outputs, including code, markdown, and visualizations. Claude Code refuses to read a notebook file over 100 MB; the error tells Claude how to read a portion of the notebook instead, such as a slice of cells, with a shell command.

Read only reads files, not directories. Claude lists directory contents with a shell command such as `ls`.

## SendFeedback tool behavior

Claude-drafted feedback is a feedback report about Claude Code that Claude writes for you. It requires Claude Code v2.1.238 or later. Claude Code saves each draft on your machine under `~/.claude/feedback/drafts/`, and nothing reaches Anthropic until you send it. Claude drafts one with the SendFeedback tool when:

* A tool or command keeps failing
* It can't help with something you asked for
* You point out a mistake it made, or it notices one
* You ask it to file feedback

### What you see when Claude drafts

After Claude queues a draft, you see a card above your prompt with the draft's title. Press `1` to review the draft, press `2` twice to send it as written, or press `0` to dismiss it. A dismissed draft stays in your queue. After you dismiss a card, Claude Code asks whether to turn Claude-drafted feedback off. It stops asking once you've declined twice.

By default, you see at most three cards in a session; Anthropic can adjust that limit from the server without a release. After the limit, and whenever you set [`feedbackDrafts`](/docs/en/settings-reference#feedbackdrafts) to `quiet`, you see only a count of queued drafts in the prompt footer.

### Review and edit a draft

Run `/feedback` with no argument to open your queue. It lists every queued draft from all your sessions, including drafts whose cards you dismissed or never saw. Select a draft to open it for review, where you can:

* Edit the title, area, and details
* Set **Send transcript** to `yes` or `no`. When the transcript from the session where Claude queued the draft is still available, it starts at `yes`, which sends that conversation to Anthropic; `no` sends the report only
* Send the draft, discard it, or leave it in the queue for later

To write a report yourself instead, press `w` for the standard feedback dialog. `/feedback` with text after it, and `/bug`, open that dialog directly.

### Send a draft

When you send a draft, Claude Code submits it the same way as a `/feedback` report, with the same [retention](/docs/en/data-usage#feedback-using-the-%2Ffeedback-command), and deletes the draft from your machine. When you send from the card, it shows `✓ Sent`; when you send from the queue, it closes with a receipt ID.

The report carries:

* Your title, area, and details
* Environment info, such as your Claude Code version, operating system, and model
* The IDs of recent API requests
* The conversation transcript, when you left **Send transcript** at `yes` in the review screen. Sending from the card never includes the transcript

Claude Code keeps your working directory in the local draft so it can find the transcript, and doesn't send the directory.

In [organizations with zero data retention](/docs/en/zero-data-retention#features-disabled-under-zdr), Claude Code leaves the tool out, as it does for `/feedback`. If a session in such an organization still offers the tool, drafts stay on your machine, and sending fails with `Feedback collection is not available for organizations with custom data retention policies.`

### Discard or keep a draft

When you discard a draft, Claude Code deletes it from your machine. A draft you leave in the queue expires after 30 days, or after [`cleanupPeriodDays`](/docs/en/settings-reference#cleanupperioddays) when that's shorter. The queue holds 10 drafts across all your sessions, and when Claude queues an eleventh, Claude Code deletes the oldest. When you run `/exit` with drafts from the session still in the queue, Claude Code asks whether to review them or discard them before exiting.

### Turn Claude-drafted feedback off

Set **Claude-drafted feedback** to `off` in `/config`, which writes the [`feedbackDrafts`](/docs/en/settings-reference#feedbackdrafts) setting, or set [`CLAUDE_CODE_SEND_FEEDBACK=0`](/docs/en/env-vars) for one session. With either, Claude can't queue drafts. To keep drafting on without cards, set `feedbackDrafts` to `quiet` instead. Administrators can set `feedbackDrafts` in [managed settings](/docs/en/managed-settings), which takes precedence over your own setting.

### Sessions without Claude-drafted feedback

Claude Code includes the tool in interactive terminal sessions on your own machine that use the Claude API rather than a cloud provider. It leaves the tool out of:

* Non-interactive `-p` runs and [Agent SDK](/docs/en/agent-sdk/overview) sessions, which have no screen to review the queue on
* [Cloud sessions](/docs/en/claude-code-on-the-web), which can't write to the queue on your machine
* Sessions on [Amazon Bedrock](/docs/en/amazon-bedrock), [Claude Platform on AWS](/docs/en/claude-platform-on-aws), [Google Cloud's Agent Platform](/docs/en/google-vertex-ai), or [Microsoft Foundry](/docs/en/microsoft-foundry)
* Sessions where you set [`CLAUDE_CODE_SEND_FEEDBACK=0`](/docs/en/env-vars) or [`DISABLE_FEEDBACK_COMMAND=1`](/docs/en/env-vars), set `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` to any non-empty value, or turned off [feature-flag fetching](/docs/en/env-vars#features-that-need-feature-flag-fetching)
* Organizations that have turned off product feedback, and [organizations with zero data retention](/docs/en/zero-data-retention#features-disabled-under-zdr)

## Task tool availability

The task-tracking tools, `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`, and `TodoWrite`, are available by default only on Claude 3.x models, Opus 4 through 4.7, Sonnet 4 through 4.6, and Haiku 4.5. Wherever the tools are available, you get the four Task tools, or `TodoWrite` instead when you set [`CLAUDE_CODE_ENABLE_TASKS=0`](/docs/en/env-vars).

On every other model, Claude Code leaves the tools out unless you opt in. The same applies to a model ID Claude Code doesn't recognize, such as a custom model name served through an [LLM gateway](/docs/en/llm-gateway). On newer models, Claude keeps track of multi-step work without a written checklist, and the tools' definitions and reminders take up context. Without the tools, Claude adds nothing to the [task list](/docs/en/interactive-mode#task-list) while it works.

If you'd like to use these tools on a model that doesn't have them by default, do one of the following:

* Export [`CLAUDE_CODE_ENABLE_TODO_TOOLS=1`](/docs/en/env-vars) before you start Claude Code, for example `CLAUDE_CODE_ENABLE_TODO_TOOLS=1 claude`. Claude Code then provides the same tools on every model and every provider
* Name one of the tools in [`--allowedTools`](/docs/en/cli-reference#cli-flags), for example `claude --allowedTools TaskCreate`
* List the tools in [`--tools`](/docs/en/cli-reference#cli-flags), which restricts the session's built-in tools to the ones it names. Include the tools you want alongside the other built-in tools you use
* In the Agent SDK, the [`allowedTools` and `tools` options](/docs/en/agent-sdk/todo-tracking#model-availability) work the same way as the two flags

In [background sessions](/docs/en/agent-view) and in [cloud sessions](/docs/en/claude-code-on-the-web), Claude Code provides the same tools on every model, listed or not.

Claude Code gives a subagent the tools only when your session has them, even when the subagent runs a different model. An in-process [agent team](/docs/en/agent-teams) teammate follows your session the same way, while a teammate in its own [split pane](/docs/en/agent-teams#choose-a-display-mode) runs as a separate Claude Code process, so its own model decides. Without the Task tools, an agent coordinates with its team through messages instead of the [shared task list](/docs/en/agent-teams#assign-and-claim-tasks).

The default set described here applies in Claude Code v2.1.268 and later.

## WebFetch tool behavior

WebFetch takes a URL and a prompt describing what to extract. It fetches the page, converts the response to Markdown when the server returns HTML, and runs the prompt against the content using a small, fast model. For most fetches, Claude receives that model's answer, not the raw page. The conversion step is not configurable.

This makes WebFetch lossy by design. The extraction prompt determines what reaches Claude, so a result that says a page doesn't mention something may only mean the prompt didn't ask about it. Ask Claude to fetch again with a more specific prompt, or use `curl` via Bash for the unprocessed page.

A few behaviors shape the response Claude receives:

* WebFetch refuses `localhost` and any other hostname without a dot, such as a bare intranet name, before making a request. The [error it returns](/docs/en/errors#webfetch-cannot-fetch-localhost) tells Claude to reach local servers with `curl` through Bash instead.
* HTTP URLs are automatically upgraded to HTTPS.
* Large pages are truncated to a fixed character limit before processing.
* WebFetch caches each response for 15 minutes by default, so repeated fetches of the same URL return quickly. On Claude Code v2.1.233 or later, set [`CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS`](/docs/en/env-vars#variables) to change how long WebFetch keeps each response.
* A page that hasn't finished downloading within five minutes, including any redirects WebFetch follows, fails with a deadline error. On Claude Code v2.1.268 or later, set [`CLAUDE_CODE_WEBFETCH_DEADLINE_MS`](/docs/en/env-vars#variables) to change the limit, or to `0` to remove it.
* When a URL redirects to a different host, WebFetch returns a text result that names the original URL and the redirect target instead of following it. Claude then fetches the new URL with a second WebFetch call.
* When the extraction step hits an overloaded API, Claude Code retries it with backoff; a fetch that still fails returns an error result. Before v2.1.212, the API error text could reach Claude as if it were the extracted page content.

In Manual and `acceptEdits` [permission modes](/docs/en/permission-modes), WebFetch prompts before fetching, except for domains your [permission rules](/docs/en/permissions#manage-permissions) already allow or deny and a built-in set of preapproved documentation domains that fetch without a prompt. Whatever your rules allow, a fetch also passes the [WebFetch domain safety check](/docs/en/data-usage#webfetch-domain-safety-check) first; that section covers what the check sends and the setting that skips it. The prompt offers three options:

* **Yes**: approves this fetch only. The next WebFetch call prompts again, even for the same domain.
* **Yes, and don't ask again for `<domain>`**: approves the fetch and saves a `WebFetch(domain:...)` allow rule for that domain to `.claude/settings.local.json` for that repository. See [how saved approvals persist](/docs/en/permissions#permission-system). When your organization sets [`allowManagedPermissionRulesOnly`](/docs/en/permissions#managed-only-settings), Claude Code hides this option.
* **No, and tell Claude what to do differently**: rejects the fetch.

To allow a domain in advance without a prompt, add an allow rule like `WebFetch(domain:example.com)`; `WebFetch(domain:*)` allows every domain. The `auto` and `bypassPermissions` [permission modes](/docs/en/permissions#permission-modes) skip the prompt, except for a domain an explicit `ask` rule matches.

An explicit `WebFetch(domain:...)` rule in `deny`, `ask`, or `allow` takes precedence over the preapproved set, so you can block a preapproved domain or require a prompt for it.

WebFetch sets a `User-Agent` header beginning with `Claude-User`, and an `Accept` header that prefers Markdown over HTML so servers that support content negotiation can return Markdown directly.

Sandboxed commands don't inherit WebFetch's built-in set of preapproved documentation domains. To let a sandboxed command reach a domain without a prompt, add the domain to [`allowedDomains`](/docs/en/settings-reference#sandbox-network-alloweddomains) or allow it with a `WebFetch(domain:...)` rule, which the [sandbox also honors](/docs/en/sandboxing#network-isolation). WebFetch never reads the sandbox allowlist in return, so adding a domain to a sandbox or organization network allowlist doesn't stop WebFetch from prompting for it.

## WebSearch tool behavior

WebSearch runs a query against Anthropic's [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) backend and returns result titles and URLs. It doesn't fetch the result pages. To read a page Claude finds in search results, it follows up with [WebFetch](#webfetch-tool-behavior).

The tool may issue up to eight backend searches per call, refining the search internally before returning results. Claude can scope results with `allowed_domains` to include only certain hosts, or `blocked_domains` to exclude them. The two lists can't be combined in a single call.

When the search request hits an overloaded API, Claude Code retries it with backoff; a call that still fails returns an error result. Before v2.1.212, the API error text could reach Claude as if it were search results.

WebSearch permission rules take no specifier. A bare `WebSearch` entry in `allow` or `deny` is the only form.

The search backend is not configurable. To search with a different provider, add an [MCP server](/docs/en/mcp) that exposes a search tool.

<Note>
  WebSearch is available on the Claude API and [Claude Platform on AWS](/docs/en/claude-platform-on-aws). On Microsoft Foundry it requires a [deployment hosted on Anthropic](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry#hosting-options): deployments hosted on Azure don't support server-side tools, so the WebSearch call fails. On Google Cloud's Agent Platform it works with Claude 4 and later models, including Opus, Sonnet, and Haiku. Amazon Bedrock doesn't expose the server-side web search tool.
</Note>

### Session search limit

A session can make at most 200 WebSearch calls, counted across the main conversation and every [subagent](/docs/en/sub-agents) it spawns, so searches made by parallel research fan-outs count against the same limit. The limit requires Claude Code v2.1.212 or later. When Claude reaches the limit, further calls return a notice telling Claude to continue with the information it already gathered, rather than an error that would invite a retry. You don't see the notice: a capped call appears in the conversation as a search that did nothing, and if Claude needs more searches, the notice tells it to ask you to raise the limit.

Set the [`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`](/docs/en/env-vars) environment variable to change the cap; it accepts a positive whole number, so the cap can be raised but not turned off. Running [`/clear`](/docs/en/commands#all-commands) resets the count. If work that can still spawn [subagents](/docs/en/sub-agents) survives the clear, such as a running workflow, the count carries over instead.

## Write tool behavior

The Write tool creates a new file or overwrites an existing one with the full content provided. It doesn't append or merge.

Whether Claude must read an existing file in the current conversation before overwriting it depends on the model and the file:

* Claude Opus 4.6, Claude Haiku 4.5, and older models always require the read, so a Write to an unread existing file fails with an error.
* Newer models can overwrite a file they never read this session under the same conditions as [read-before-edit](#edit-tool-behavior): reading it wouldn't need a permission prompt and the Read tool is available.
* Jupyter notebooks, and files Claude has read only partially with a [`PARTIAL view` notice](#read-tool-behavior), require the read on every model.

This constraint doesn't apply to new files. Before v2.1.228, every model required the read before overwriting an existing file.

Viewing the file with Bash also satisfies this requirement under the same rules described in [Edit tool behavior](#edit-tool-behavior).

For partial changes to an existing file, Claude uses Edit instead of Write.

## Check which tools are available

Your exact tool set depends on your provider, platform, and settings. To check what's loaded in a running session, ask Claude directly:

```text theme={null}
What tools do you have access to?
```

Claude gives a conversational summary. For exact MCP tool names, run `/mcp`.

<Note>
  The [advisor tool](/docs/en/advisor) is a [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) that the API runs, rather than a tool that Claude Code implements. It has no name you can reference in permission rules or hook matchers.
</Note>

## See also

* [MCP servers](/docs/en/mcp): add custom tools by connecting external servers
* [Permissions](/docs/en/permissions): permission system, rule syntax, and tool-specific patterns
* [Subagents](/docs/en/sub-agents): configure tool access for subagents
* [Hooks](/docs/en/hooks-guide): run custom commands before or after tool execution
