---
title: OpenAI 官方文档汇编 · 01-Agents SDK 官方文档
source: OpenAI 官方仓库（openai-agents-python / openai-cookbook）（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/openai/openai-agents-sdk-docs-agents-md.md
- VibeCoding/openai/openai-agents-sdk-docs-config-md.md
- VibeCoding/openai/openai-agents-sdk-docs-context-md.md
- VibeCoding/openai/openai-agents-sdk-docs-guardrails-md.md
- VibeCoding/openai/openai-agents-sdk-docs-handoffs-md.md
- VibeCoding/openai/openai-agents-sdk-docs-human-in-the-loop-md.md
- VibeCoding/openai/openai-agents-sdk-docs-index-md.md
- VibeCoding/openai/openai-agents-sdk-docs-llms-full-txt.md
- VibeCoding/openai/openai-agents-sdk-docs-llms-txt.md
- VibeCoding/openai/openai-agents-sdk-docs-mcp-md.md
- VibeCoding/openai/openai-agents-sdk-docs-multi-agent-md.md
- VibeCoding/openai/openai-agents-sdk-docs-quickstart-md.md
- VibeCoding/openai/openai-agents-sdk-docs-results-md.md
- VibeCoding/openai/openai-agents-sdk-docs-running-agents-md.md
- VibeCoding/openai/openai-agents-sdk-docs-sandbox-agents-md.md
evidence: E1
domain: VibeCoding
keywords:
- openai
- codex
- AI-Agent
- vibe-coding
state:
  phase: draft
  time_raw: 2026-09-23 06:25:00+08:00
  time_draft: 2026-09-23 03:37:43+08:00
  time_wiki: '2026-09-23T10:40:21+08:00'
wiki_ref: 03-Wiki/氛围编程/_MOC-氛围编程.md
---

> **汇编性质**：OpenAI 官方仓库（openai-agents-python / openai-cookbook） 官方原文 15 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:37:43+08:00

---

## agents

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/agents.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-agents-md.md`

# Agents

Agents are the core building block in your apps. An agent is a large language model (LLM) configured with instructions, tools, and optional runtime behavior such as handoffs, guardrails, and structured outputs.

Use this page when you want to define or customize a single base `Agent` rather than a `SandboxAgent`. If you are deciding how multiple agents should collaborate, read [Agent orchestration](multi_agent.md). If the agent should run inside an isolated workspace with manifest-defined files and sandbox-native capabilities, read [Sandbox agent concepts](sandbox/guide.md).

The SDK uses the Responses API by default for OpenAI models, but the distinction here is orchestration: `Agent` plus `Runner` lets the SDK manage turns, tools, guardrails, handoffs, and sessions for you. If you want to own that loop yourself, use the Responses API directly instead.

## Choose the next guide

Use this page as the hub for agent definition. Jump to the adjacent guide that matches the next decision you need to make.

| If you want to... | Read next |
| --- | --- |
| Choose a model or provider setup | [Models](models/index.md) |
| Add capabilities to the agent | [Tools](tools.md) |
| Run an agent against a real repo, document bundle, or isolated workspace | [Sandbox agents quickstart](sandbox_agents.md) |
| Decide between manager-style orchestration and handoffs | [Agent orchestration](multi_agent.md) |
| Configure handoff behavior | [Handoffs](handoffs.md) |
| Run turns, stream events, or manage conversation state | [Running agents](running_agents.md) |
| Inspect final output, run items, or resumable state | [Results](results.md) |
| Share local dependencies and runtime state | [Context management](context.md) |

## Basic configuration

The most common properties of an agent are:

| Property | Required | Description |
| --- | --- | --- |
| `name` | yes | Human-readable agent name. |
| `instructions` | no | System prompt or dynamic instructions callback. Strongly recommended. See [Dynamic instructions](#dynamic-instructions). |
| `prompt` | no | OpenAI Responses API prompt configuration. Accepts a static prompt object or a function. See [Prompt templates](#prompt-templates). |
| `handoff_description` | no | Short description exposed when this agent is offered as a handoff target. |
| `handoffs` | no | Delegate the conversation to specialist agents. See [handoffs](handoffs.md). |
| `model` | no | Which LLM to use. See [Models](models/index.md). |
| `model_settings` | no | Model tuning parameters such as `temperature`, `top_p`, and `tool_choice`. |
| `tools` | no | Tools the agent can call. See [Tools](tools.md). |
| `mcp_servers` | no | MCP servers that provide MCP-backed tools to the agent. See the [MCP guide](mcp.md). |
| `mcp_config` | no | Fine-tune how MCP tools are prepared, such as converting their schemas to strict mode and formatting MCP failures. See the [MCP guide](mcp.md#agent-level-mcp-configuration). |
| `input_guardrails` | no | Guardrails that run on the first user input for this agent chain. See [Guardrails](guardrails.md). |
| `output_guardrails` | no | Guardrails that run on the final output for this agent. See [Guardrails](guardrails.md). |
| `output_type` | no | Structured output type instead of plain text. See [Output types](#output-types). |
| `hooks` | no | Agent-scoped lifecycle callbacks. See [Lifecycle events (hooks)](#lifecycle-events-hooks). |
| `tool_use_behavior` | no | Control whether tool results loop back to the model or end the run. See [Tool use behavior](#tool-use-behavior). |
| `reset_tool_choice` | no | Reset `tool_choice` after a tool call (default: `True`) to avoid tool-use loops. See [Forcing tool use](#forcing-tool-use). |

```python
from agents import Agent
from agents.decorators import tool

@tool
def get_weather(city: str) -> str:
    """returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Haiku agent",
    instructions="Always respond in haiku form",
    model="gpt-5-nano",
    tools=[get_weather],
)
```

Everything in this section applies to `Agent`. `SandboxAgent` builds on the same ideas, then adds `default_manifest`, `base_instructions`, `capabilities`, and `run_as` for workspace-scoped runs. See [Sandbox agent concepts](sandbox/guide.md).

## Prompt templates

You can reference a prompt template created in the OpenAI platform by setting `prompt`. This works when OpenAI models are accessed through the Responses API.

To use it, please:

1. Go to https://platform.openai.com/playground/prompts
2. Create a new prompt variable, `poem_style`.
3. Create a system prompt with the content:

    ```
    Write a poem in {{poem_style}}
    ```

4. Run the example with the `--prompt-id` flag.

```python
from agents import Agent

agent = Agent(
    name="Prompted assistant",
    prompt={
        "id": "pmpt_123",
        "version": "1",
        "variables": {"poem_style": "haiku"},
    },
)
```

You can also generate the prompt dynamically at run time:

```python
from dataclasses import dataclass

from agents import Agent, GenerateDynamicPromptData, Runner

@dataclass
class PromptContext:
    prompt_id: str
    poem_style: str

async def build_prompt(data: GenerateDynamicPromptData):
    ctx: PromptContext = data.context.context
    return {
        "id": ctx.prompt_id,
        "version": "1",
        "variables": {"poem_style": ctx.poem_style},
    }

agent = Agent(name="Prompted assistant", prompt=build_prompt)
result = await Runner.run(
    agent,
    "Say hello",
    context=PromptContext(prompt_id="pmpt_123", poem_style="limerick"),
)
```

## Context

Agents are generic on their `context` type. Context is a dependency-injection tool: it's an object you create and pass to `Runner.run()`, that is passed to every agent, tool, handoff etc, and it serves as a grab bag of dependencies and state for the agent run. You can provide any Python object as the context.

Read the [context guide](context.md) for the full `RunContextWrapper` surface, shared usage tracking, nested `tool_input`, and serialization caveats.

```python
from dataclasses import dataclass

@dataclass
class Purchase:
    id: str

@dataclass
class UserContext:
    name: str
    uid: str
    is_pro_user: bool

    async def fetch_purchases(self) -> list[Purchase]:
        # implement your logic here
        return []

agent = Agent[UserContext](
    ...,
)
```

## Output types

By default, agents produce plain text (i.e. `str`) outputs. If you want the agent to produce a particular type of output, you can use the `output_type` parameter. A common choice is to use [Pydantic](https://docs.pydantic.dev/) objects, but we support any type that can be wrapped in a Pydantic [TypeAdapter](https://docs.pydantic.dev/latest/api/type_adapter/) - dataclasses, lists, TypedDict, etc.

```python
from pydantic import BaseModel
from agents import Agent

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

agent = Agent(
    name="Calendar extractor",
    instructions="Extract calendar events from text",
    output_type=CalendarEvent,
)
```

!!! note

    When you pass an `output_type`, that tells the model to use [structured outputs](https://platform.openai.com/docs/guides/structured-outputs) instead of regular plain text responses.

## Multi-agent system design patterns

There are many ways to design multi‑agent systems, but we commonly see two broadly applicable patterns:

1. Manager (agents as tools): A central manager/orchestrator invokes specialized sub‑agents as tools and retains control of the conversation.
2. Handoffs: Peer agents hand off control to a specialized agent that takes over the conversation. This is decentralized.

See [our practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) for more details.

### Manager (agents as tools)

The `customer_facing_agent` handles all user interaction and invokes specialized sub‑agents exposed as tools. Read more in the [tools](tools.md#agents-as-tools) documentation.

```python
from agents import Agent

booking_agent = Agent(...)
refund_agent = Agent(...)

customer_facing_agent = Agent(
    name="Customer-facing agent",
    instructions=(
        "Handle all direct user communication. "
        "Call the relevant tools when specialized expertise is needed."
    ),
    tools=[
        booking_agent.as_tool(
            tool_name="booking_expert",
            tool_description="Handles booking questions and requests.",
        ),
        refund_agent.as_tool(
            tool_name="refund_expert",
            tool_description="Handles refund questions and requests.",
        )
    ],
)
```

### Handoffs

Configured handoff targets are sub‑agents to which the agent can delegate. When a handoff occurs, the delegated agent receives the conversation history and takes over the conversation. This pattern enables modular, specialized agents that excel at a single task. Read more in the [handoffs](handoffs.md) documentation.

```python
from agents import Agent

booking_agent = Agent(...)
refund_agent = Agent(...)

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions. "
        "If they ask about booking, hand off to the booking agent. "
        "If they ask about refunds, hand off to the refund agent."
    ),
    handoffs=[booking_agent, refund_agent],
)
```

## Dynamic instructions

In most cases, you can provide instructions when you create the agent. However, you can also provide dynamic instructions via a function. The function will receive the agent and context, and must return the prompt. Both regular and `async` functions are accepted.

```python
from agents import Agent, RunContextWrapper

def dynamic_instructions(
    context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    return f"The user's name is {context.context.name}. Help them with their questions."

agent = Agent[UserContext](
    name="Triage agent",
    instructions=dynamic_instructions,
)
```

## Lifecycle events (hooks)

Sometimes, you want to observe the lifecycle of an agent. For example, you may want to log events, pre-fetch data, or record usage when certain events occur.

There are two hook scopes:

-   [`RunHooks`][agents.lifecycle.RunHooks] observe the entire `Runner.run(...)` invocation, including handoffs to other agents.
-   [`AgentHooks`][agents.lifecycle.AgentHooks] are attached to a specific agent instance via `agent.hooks`.

The callback context also changes depending on the event:

-   Agent start/end hooks receive [`AgentHookContext`][agents.run_context.AgentHookContext], which wraps your original context and carries the shared run usage state.
-   LLM, tool, and handoff hooks receive [`RunContextWrapper`][agents.run_context.RunContextWrapper].

Typical hook timing:

-   `on_agent_start`: when a specific agent begins running; `on_agent_end`: when that agent finishes producing a final output.
-   `on_llm_start` / `on_llm_end`: immediately around each model call.
- `on_tool_start` / `on_tool_end`: around each local tool invocation. For function tools, the hook `context` is typically a `ToolContext`, so you can inspect tool-call metadata such as `tool_call_id`.
-   `on_handoff`: when control moves from one agent to another.

Use `RunHooks` when you want a single observer for the whole workflow, and `AgentHooks` when you want lifecycle callbacks scoped to a specific agent.

```python
from agents import Agent, RunHooks, Runner

class LoggingHooks(RunHooks):
    async def on_agent_start(self, context, agent):
        print(f"Starting {agent.name}")

    async def on_llm_end(self, context, agent, response):
        print(f"{agent.name} produced {len(response.output)} output items")

    async def on_agent_end(self, context, agent, output):
        print(f"{agent.name} finished with usage: {context.usage}")

agent = Agent(name="Assistant", instructions="Be concise.")
result = await Runner.run(agent, "Explain quines", hooks=LoggingHooks())
print(result.final_output)
```

For the full callback surface, see the [Lifecycle API reference](ref/lifecycle.md).

## Guardrails

Guardrails allow you to run checks/validations on user input in parallel to the agent running, and on the agent's output once it is produced. For example, you could screen the user's input and agent's output for relevance. Read more in the [guardrails](guardrails.md) documentation.

## Cloning/copying agents

By using the `clone()` method on an agent, you can duplicate an Agent, and optionally change any properties you like.

```python
pirate_agent = Agent(
    name="Pirate",
    instructions="Write like a pirate",
    model="gpt-5.6-sol",
)

robot_agent = pirate_agent.clone(
    name="Robot",
    instructions="Write like a robot",
)
```

`clone()` uses `dataclasses.replace`, so it performs a shallow copy. A list attribute that you do not override, such as `tools`, `handoffs`, `mcp_servers`, `input_guardrails`, or `output_guardrails`, remains the exact list held by the original agent. Mutating that list through either agent therefore affects both agents. To give the clone an independent list container, pass a new list, for example `pirate_agent.clone(tools=[*pirate_agent.tools, extra_tool])`. The entries copied into that new list remain the same tool or handoff objects unless you replace those entries too.

## Forcing tool use

Supplying a list of tools doesn't always mean the LLM will use a tool. You can force tool use by setting [`ModelSettings.tool_choice`][agents.model_settings.ModelSettings.tool_choice]. Valid values are:

1. `auto`, which allows the LLM to decide whether or not to use a tool.
2. `required`, which requires the LLM to use a tool (but it can intelligently decide which tool).
3. `none`, which requires the LLM to _not_ use a tool.
4. Setting a specific string e.g. `my_tool`, which requires the LLM to use that specific tool.

When you are using OpenAI Responses tool search, named tool choices are more limited: you cannot target bare namespace names or deferred-only tools with `tool_choice`, and `tool_choice="tool_search"` does not target [`ToolSearchTool`][agents.tool.ToolSearchTool]. In those cases, prefer `auto` or `required`. See [Hosted tool search](tools.md#hosted-tool-search) for the Responses-specific constraints.

```python
from agents import Agent, ModelSettings
from agents.decorators import tool

@tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Weather Agent",
    instructions="Retrieve weather details.",
    tools=[get_weather],
    model_settings=ModelSettings(tool_choice="get_weather")
)
```

## Tool use behavior

The `tool_use_behavior` parameter in the `Agent` configuration controls how tool outputs are handled:

- `"run_llm_again"`: The default. Tools are run, and the LLM processes the results to produce a final response.
- `"stop_on_first_tool"`: The output of the first tool call is used as the final response, without further LLM processing.

```python
from agents import Agent
from agents.decorators import tool

@tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

agent = Agent(
    name="Weather Agent",
    instructions="Retrieve weather details.",
    tools=[get_weather],
    tool_use_behavior="stop_on_first_tool"
)
```

- `StopAtTools(stop_at_tool_names=[...])`: Stops if any specified tool is called, using its output as the final response.

```python
from agents import Agent
from agents.agent import StopAtTools
from agents.decorators import tool

@tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

@tool
def sum_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

agent = Agent(
    name="Stop At Stock Agent",
    instructions="Get weather or sum numbers.",
    tools=[get_weather, sum_numbers],
    tool_use_behavior=StopAtTools(stop_at_tool_names=["get_weather"])
)
```

- `ToolsToFinalOutputFunction`: A custom function that processes tool results and decides whether to end the run with a final output or continue processing with the LLM.

```python
from agents import Agent, FunctionToolResult, RunContextWrapper
from agents.agent import ToolsToFinalOutputResult
from agents.decorators import tool
from typing import List, Any

@tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

def custom_tool_handler(
    context: RunContextWrapper[Any],
    tool_results: List[FunctionToolResult]
) -> ToolsToFinalOutputResult:
    """Processes tool results to decide final output."""
    for result in tool_results:
        if result.output and "sunny" in result.output:
            return ToolsToFinalOutputResult(
                is_final_output=True,
                final_output=f"Final weather: {result.output}"
            )
    return ToolsToFinalOutputResult(
        is_final_output=False,
        final_output=None
    )

agent = Agent(
    name="Weather Agent",
    instructions="Retrieve weather details.",
    tools=[get_weather],
    tool_use_behavior=custom_tool_handler
)
```

!!! note

    To prevent infinite loops, the framework automatically resets `tool_choice` to "auto" after a tool call. This behavior is configurable via [`agent.reset_tool_choice`][agents.agent.Agent.reset_tool_choice]. The infinite loop is because tool results are sent to the LLM, which then generates another tool call because of `tool_choice`, ad infinitum.

---

## config

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/config.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-config-md.md`

# Configuration

This page covers SDK-wide defaults that you usually set once during application startup, such as the default OpenAI key or client, the default OpenAI API shape, tracing export defaults, and logging behavior.

These defaults still apply to sandbox-based workflows, but sandbox workspaces, sandbox clients, and session reuse are configured separately.

If you need to configure a specific agent or run instead, start with:

-   [Agents](agents.md) for instructions, tools, output types, handoffs, and guardrails on a plain `Agent`.
-   [Running agents](running_agents.md) for `RunConfig`, sessions, and conversation-state options.
-   [Sandbox agents](sandbox/guide.md) for `SandboxRunConfig`, manifests, capabilities, and sandbox-client-specific workspace setup.
-   [Models](models/index.md) for model selection and provider configuration.
-   [Tracing](tracing.md) for per-run tracing metadata and custom trace processors.

## Configuration objects and dictionaries

Configuration parameters defined by the SDK generally accept either their typed settings object or a dictionary containing the same fields. This applies across agent, run, model, session, sandbox, and voice configuration boundaries whose type annotations include a dictionary. Nested settings types defined by the SDK can also use dictionaries.

```python
from agents import Agent

agent = Agent(
    name="Assistant",
    model="gpt-5.6-sol",
    model_settings={
        "reasoning": {"effort": "high"},
        "verbosity": "low",
    },
)
```

The SDK normalizes these dictionaries into the corresponding settings objects. Unknown fields in dataclass configuration types defined by the SDK raise `TypeError`, which helps catch misspelled option names early. Check the parameter's type annotation or API reference to confirm whether a specific boundary accepts a dictionary.

## API keys and clients

By default, the SDK uses the `OPENAI_API_KEY` environment variable for LLM requests and tracing. The key is resolved when the SDK first creates an OpenAI client (lazy initialization), so set the environment variable before your first model call. If you are unable to set that environment variable before your app starts, you can use the [set_default_openai_key()][agents.set_default_openai_key] function to set the key.

```python
from agents import set_default_openai_key

set_default_openai_key("sk-...")
```

Alternatively, you can also configure an OpenAI client to be used. By default, the SDK creates an `AsyncOpenAI` instance, using the API key from the environment variable or the default key set above. You can change this by using the [set_default_openai_client()][agents.set_default_openai_client] function.

```python
from openai import AsyncOpenAI
from agents import set_default_openai_client

custom_client = AsyncOpenAI(base_url="...", api_key="...")
set_default_openai_client(custom_client)
```

When you pass an explicit client to [`OpenAIProvider`][agents.models.openai_provider.OpenAIProvider], that client owns its connection and account settings. Do not also pass `api_key`, `base_url`, `websocket_base_url`, `organization`, or `project` to `OpenAIProvider`; combining `openai_client` with any of those arguments raises [`UserError`][agents.exceptions.UserError] instead of silently ignoring the duplicate value. Set the intended values when constructing `AsyncOpenAI`.

When `openai_client` is omitted, `OpenAIProvider` reuses the SDK-wide default client only if `api_key`, `base_url`, `websocket_base_url`, `organization`, and `project` are all `None`. Passing any of those options, including an empty string, makes the provider create its own client and gives the provider option precedence over the SDK-wide default client. Leave every provider option as `None` when the provider should inherit the client installed by `set_default_openai_client()`.

[`OpenAIVoiceModelProvider`][agents.voice.models.openai_model_provider.OpenAIVoiceModelProvider] uses the same ownership and precedence rules for `api_key`, `base_url`, `organization`, and `project`. Its explicit `openai_client` cannot be combined with any of those four options.

### Custom HTTP clients with `openai` v3

Version 0.21.0 requires `openai>=3.0.0,<4`. The default OpenAI provider uses HTTPX2, so most applications do not need to configure an HTTP client directly. If your application passes `http_client=` to `AsyncOpenAI`, use HTTPX2 types for the custom client and its transport-facing options:

```python
import httpx2
from openai import AsyncOpenAI, DefaultAsyncHttpx2Client

from agents import set_default_openai_client

http_client = DefaultAsyncHttpx2Client(
    timeout=httpx2.Timeout(30.0, connect=5.0),
)
custom_client = AsyncOpenAI(
    api_key="...",
    http_client=http_client,
)
set_default_openai_client(custom_client)
```

The same migration applies to custom transports, authentication, event hooks, mock transports, URLs, requests, responses, and transport exception handling. Use their `httpx2` equivalents. The Agents SDK does not convert arbitrary legacy `httpx` objects to HTTPX2. The OpenAI Python SDK provides a temporary compatibility path for legacy clients when the application installs `httpx` explicitly, but new and migrated code should use HTTPX2.

This OpenAI client boundary is separate from local MCP transport customization. MCP Python SDK v1 uses its own legacy `httpx` dependency, while MCP Python SDK v2 uses `httpx2`; see [MCP Python SDK v1 and v2](mcp.md#mcp-python-sdk-v1-and-v2).

If you prefer environment-based endpoint configuration, the default OpenAI provider also reads `OPENAI_BASE_URL`. When you enable Responses websocket transport, it also reads `OPENAI_WEBSOCKET_BASE_URL` for the websocket `/responses` endpoint.

```bash
export OPENAI_BASE_URL="https://your-openai-compatible-endpoint.example/v1"
export OPENAI_WEBSOCKET_BASE_URL="wss://your-openai-compatible-endpoint.example/v1"
```

Finally, you can also customize the OpenAI API that is used. By default, we use the OpenAI Responses API. You can override this to use the Chat Completions API by using the [set_default_openai_api()][agents.set_default_openai_api] function.

```python
from agents import set_default_openai_api

set_default_openai_api("chat_completions")
```

## OpenAI provider defaults

Providers that use the SDK's OpenAI backend also read SDK-wide defaults when they map model-name strings to models. Use [`set_default_openai_responses_transport()`][agents.set_default_openai_responses_transport] to make OpenAI Responses models use websocket transport by default:

```python
from agents import set_default_openai_responses_transport

set_default_openai_responses_transport("websocket")
```

This affects OpenAI Responses models that result when the default OpenAI provider resolves a model name. For provider-level setup, connection reuse, keepalive options, and custom websocket endpoints, see [Responses WebSocket transport](models/index.md#responses-websocket-transport).

If your OpenAI setup expects provider-level agent registration metadata, configure a default harness ID once at startup:

```python
from agents import set_default_openai_harness

set_default_openai_harness("your-harness-id")
```

You can also pass the full registration object:

```python
from agents import OpenAIAgentRegistrationConfig, set_default_openai_agent_registration

set_default_openai_agent_registration(
    OpenAIAgentRegistrationConfig(harness_id="your-harness-id")
)
```

If no SDK default is set, providers that use the SDK's OpenAI backend fall back to the `OPENAI_AGENT_HARNESS_ID` environment variable. When a harness ID is configured, the SDK adds it to trace metadata as `agent_harness_id` unless that key is already present in `RunConfig.trace_metadata`.

## Tracing

Tracing is enabled by default. By default it uses the same OpenAI API key as your model requests from the section above (that is, the environment variable or the default key you set). You can specifically set the API key used for tracing by using the [`set_tracing_export_api_key`][agents.set_tracing_export_api_key] function.

```python
from agents import set_tracing_export_api_key

set_tracing_export_api_key("sk-...")
```

If your model traffic uses one key or client but tracing should use a different OpenAI key, pass `use_for_tracing=False` when setting the default key or client, then configure tracing separately. The same pattern works with [`set_default_openai_key()`][agents.set_default_openai_key] if you are not using a custom client.

```python
from openai import AsyncOpenAI
from agents import (
    set_default_openai_client,
    set_tracing_export_api_key,
)

custom_client = AsyncOpenAI(base_url="https://your-openai-compatible-endpoint.example/v1", api_key="provider-key")
set_default_openai_client(custom_client, use_for_tracing=False)

set_tracing_export_api_key("sk-tracing")
```

If you need to attribute traces to a specific organization or project when using the default exporter, set these environment variables before your app starts:

```bash
export OPENAI_ORG_ID="org_..."
export OPENAI_PROJECT_ID="proj_..."
```

You can also set a tracing API key per run without changing the global exporter.

```python
from agents import Runner, RunConfig

await Runner.run(
    agent,
    input="Hello",
    run_config=RunConfig(tracing={"api_key": "sk-tracing-123"}),
)
```

You can also disable tracing entirely by using the [`set_tracing_disabled()`][agents.set_tracing_disabled] function.

```python
from agents import set_tracing_disabled

set_tracing_disabled(True)
```

If you want to keep tracing enabled but exclude potentially sensitive inputs/outputs from trace payloads, set [`RunConfig.trace_include_sensitive_data`][agents.run.RunConfig.trace_include_sensitive_data] to `False`:

```python
from agents import Runner, RunConfig

await Runner.run(
    agent,
    input="Hello",
    run_config=RunConfig(trace_include_sensitive_data=False),
)
```

You can also change the default without code by setting this environment variable before your app starts:

```bash
export OPENAI_AGENTS_TRACE_INCLUDE_SENSITIVE_DATA=0
```

For full tracing controls, see the [tracing guide](tracing.md).

## Debug logging

The SDK defines two Python loggers (`openai.agents` and `openai.agents.tracing`) and does not attach handlers by default. Logs follow your application's Python logging configuration.

To enable verbose logging, use the [`enable_verbose_stdout_logging()`][agents.enable_verbose_stdout_logging] function.

```python
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()
```

Alternatively, you can customize the logs by adding handlers, filters, formatters, etc. You can read more in the [Python logging guide](https://docs.python.org/3/howto/logging.html).

```python
import logging

logger = logging.getLogger("openai.agents") # or openai.agents.tracing for the Tracing logger

# To make all logs show up
logger.setLevel(logging.DEBUG)
# To make info and above show up
logger.setLevel(logging.INFO)
# To make warning and above show up
logger.setLevel(logging.WARNING)
# etc

# You can customize this as needed, but this will output to `stderr` by default
logger.addHandler(logging.StreamHandler())
```

### Sensitive data in logs and diagnostics

Certain logs and diagnostic exceptions may contain sensitive data (for example, model or tool inputs and outputs).

By default, the SDK does **not** log LLM inputs/outputs or tool inputs/outputs. These protections are controlled by:

```bash
OPENAI_AGENTS_DONT_LOG_MODEL_DATA=1
OPENAI_AGENTS_DONT_LOG_TOOL_DATA=1
```

If you need to include this data temporarily for debugging, set either variable to `0` (or `false`) before your app starts:

```bash
export OPENAI_AGENTS_DONT_LOG_MODEL_DATA=0
export OPENAI_AGENTS_DONT_LOG_TOOL_DATA=0
```

These flags also control whether affected failures retain payload-bearing diagnostic details. For example, with tool-data redaction enabled, invalid arguments for a `FunctionTool` raise a generic `ModelBehaviorError` without chaining the underlying validation error. Setting either variable to `0` can expose raw model or tool data in logs, exception messages, exception chains, and other diagnostic context, so enable it only in a controlled development environment.

---

## context

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/context.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-context-md.md`

# Context management

Context is an overloaded term. There are two main classes of context you might care about:

1. Context available locally to your code: this is data and dependencies you might need when tool functions run, during callbacks like `on_handoff`, in lifecycle hooks, etc.
2. Context available to LLMs: this is data the LLM sees when generating a response.

## Local context

This is represented via the [`RunContextWrapper`][agents.run_context.RunContextWrapper] class and the [`context`][agents.run_context.RunContextWrapper.context] property within it. The way this works is:

1. You create any Python object you want. A common pattern is to use a dataclass or a Pydantic object.
2. You pass that object to the various run methods (e.g. `Runner.run(..., context=whatever)`).
3. All your tool calls, lifecycle hooks etc will be passed a wrapper object, `RunContextWrapper[T]`, where `T` represents the type of your context object; the object itself is available via `wrapper.context`.

For some runtime-specific callbacks, the SDK may pass a more specialized subclass of `RunContextWrapper[T]`. For example, lifecycle hooks for `FunctionTool` instances typically receive `ToolContext`, which also exposes tool-call metadata like `tool_call_id`, `tool_name`, and `tool_arguments`.

The **most important** thing to be aware of: every agent, tool function, lifecycle etc for a given agent run must use the same _type_ of context.

You can use the context for things like:

-   Contextual data for your run (e.g. things like a username/uid or other information about the user)
-   Dependencies (e.g. logger objects, data fetchers, etc)
-   Helper functions

!!! danger "Note"

    The context object is **not** sent to the LLM. It is purely a local object that you can read from, write to and call methods on it.

Within a single run, derived wrappers share the same underlying app context, approval state, and usage tracking. Nested [`Agent.as_tool()`][agents.agent.Agent.as_tool] runs may attach a different `tool_input`, but they do not get an isolated copy of your app state by default.

### Use local context for capability visibility

When function tools, MCP tools, and handoffs depend on the same request policy, keep the policy inputs or helper on your application context. Each SDK surface exposes the current run context through its own callback:

-   [`FunctionTool.is_enabled`][agents.tool.FunctionTool.is_enabled] receives a `RunContextWrapper`.
-   [`Handoff.is_enabled`][agents.handoffs.Handoff.is_enabled] receives a `RunContextWrapper`.
-   An MCP [`tool_filter`](mcp.md#dynamic-tool-filtering) receives a [`ToolFilterContext`][agents.mcp.ToolFilterContext], whose `run_context` property contains the current `RunContextWrapper`.

Adapt the shared application policy to these callbacks instead of maintaining separate capability lists. The callbacks control which capabilities the SDK exposes for the current run; they cannot authorize a model-generated argument or resource selection. For function tools, enforce those decisions inside the tool implementation or with [tool input guardrails](guardrails.md#tool-guardrails) and [approvals](human_in_the_loop.md) when appropriate. MCP servers must authorize their own protected operations. For a handoff with `input_type`, check the parsed input at the start of `on_handoff`, before application side effects, and raise instead of returning when authorization fails. Tool input guardrails do not run for handoffs. See [handoff inputs](handoffs.md#handoff-inputs) for the callback lifecycle.

### What `RunContextWrapper` exposes

[`RunContextWrapper`][agents.run_context.RunContextWrapper] is a wrapper around your app-defined context object. In practice you will most often use:

-   [`wrapper.context`][agents.run_context.RunContextWrapper.context] for your own mutable app state and dependencies.
-   [`wrapper.usage`][agents.run_context.RunContextWrapper.usage] for aggregated request and token usage across the current run.
-   [`wrapper.tool_input`][agents.run_context.RunContextWrapper.tool_input] for structured input when the current run is executing inside [`Agent.as_tool()`][agents.agent.Agent.as_tool].
-   [`wrapper.approve_tool(...)`][agents.run_context.RunContextWrapper.approve_tool] / [`wrapper.reject_tool(...)`][agents.run_context.RunContextWrapper.reject_tool] when you need to update approval state programmatically.

Only `wrapper.context` is your app-defined object. The other fields are runtime metadata managed by the SDK.

If you later serialize a [`RunState`][agents.run_state.RunState] for human-in-the-loop or durable job workflows, that runtime metadata is saved with the state. Avoid putting secrets in [`RunContextWrapper.context`][agents.run_context.RunContextWrapper.context] if you intend to persist or transmit serialized state.

Conversation state is a separate concern. Use `result.to_input_list()`, `session`, `conversation_id`, or `previous_response_id` depending on how you want to carry turns forward. See [results](results.md), [running agents](running_agents.md), and [sessions](sessions/index.md) for that decision.

```python
import asyncio
from dataclasses import dataclass

from agents import Agent, RunContextWrapper, Runner
from agents.decorators import tool

@dataclass
class UserInfo:  # (1)!
    name: str
    uid: int

@tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:  # (2)!
    """Fetch the age of the user. Call this function to get user's age information."""
    return f"The user {wrapper.context.name} is 47 years old"

async def main():
    user_info = UserInfo(name="John", uid=123)

    agent = Agent[UserInfo](  # (3)!
        name="Assistant",
        tools=[fetch_user_age],
    )

    result = await Runner.run(  # (4)!
        starting_agent=agent,
        input="What is the age of the user?",
        context=user_info,
    )

    print(result.final_output)  # (5)!
    # The user John is 47 years old.

if __name__ == "__main__":
    asyncio.run(main())
```

1. This is the context object. We've used a dataclass here, but you can use any type.
2. This is a tool. You can see it takes a `RunContextWrapper[UserInfo]`. The tool implementation reads from the context.
3. We mark the agent with the generic `UserInfo`, so that the typechecker can catch errors (for example, if we tried to pass a tool that took a different context type).
4. The context is passed to the `run` function.
5. The agent correctly calls the tool and gets the age.

---

### Advanced: `ToolContext`

In some cases, you might want to access extra metadata about the tool being executed — such as its name, call ID, or raw argument string.  
For this, you can use the [`ToolContext`][agents.tool_context.ToolContext] class, which extends `RunContextWrapper`.

```python
from typing import Annotated
from pydantic import BaseModel, Field
from agents import Agent
from agents.decorators import tool
from agents.tool_context import ToolContext

class WeatherContext(BaseModel):
    user_id: str

class Weather(BaseModel):
    city: str = Field(description="The city name")
    temperature_range: str = Field(description="The temperature range in Celsius")
    conditions: str = Field(description="The weather conditions")

@tool
def get_weather(ctx: ToolContext[WeatherContext], city: Annotated[str, "The city to get the weather for"]) -> Weather:
    print(f"[debug] Tool context: (name: {ctx.tool_name}, call_id: {ctx.tool_call_id}, args: {ctx.tool_arguments})")
    return Weather(city=city, temperature_range="14-20C", conditions="Sunny with wind.")

agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful agent that can tell the weather of a given city.",
    tools=[get_weather],
)
```

`ToolContext` provides the same `.context` property as `RunContextWrapper`,  
plus additional fields specific to the current tool call:

- `tool_name` – the name of the tool being invoked  
- `tool_call_id` – a unique identifier for this tool call  
- `tool_arguments` – the raw argument string passed to the tool  
- `tool_namespace` – the Responses namespace for the tool call, when the tool was loaded through `tool_namespace()` or another namespaced surface  
- `qualified_tool_name` – the tool name qualified with the namespace when one is available  

Use `ToolContext` when you need tool-level metadata during execution.  
For general context sharing between agents and tools, `RunContextWrapper` remains sufficient. Because `ToolContext` extends `RunContextWrapper`, it can also expose `.tool_input` when a nested `Agent.as_tool()` run supplied structured input.

---

## Agent/LLM context

When an LLM is called, the **only** data it can see is from the conversation history. This means that if you want to make some new data available to the LLM, you must do it in a way that makes it available in that history. There are a few ways to do this:

1. You can add it to the Agent `instructions`. This is also known as a "system prompt" or "developer message". System prompts can be static strings, or they can be dynamic functions that receive the context and output a string. This is a common tactic for information that is always useful (for example, the user's name or the current date).
2. Add it to the `input` when calling the `Runner.run` functions. This is similar to the `instructions` tactic, but allows you to have messages that are lower in the [chain of command](https://cdn.openai.com/spec/model-spec-2024-05-08.html#follow-the-chain-of-command).
3. Expose it through `FunctionTool` instances. This is useful for _on-demand_ context - the LLM decides when it needs some data, and can call the tool to fetch that data.
4. Use retrieval or web search. These are special tools that are able to fetch relevant data from files or databases (retrieval), or from the web (web search). This is useful for "grounding" the response in relevant contextual data.

---

## guardrails

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-guardrails-md.md`

# Guardrails

Guardrails enable you to do checks and validations of user input and agent output. For example, imagine you have an agent that uses a very smart (and hence slow/expensive) model to help with customer requests. You wouldn't want malicious users to ask the model to help them with their math homework. So, you can run a guardrail with a fast/cheap model. If the guardrail detects malicious usage, it can immediately raise an error, saving time and money. Blocking execution guarantees that the expensive model does not start; with parallel execution, the expensive model may already have started before the guardrail completes. See "Execution modes" below for details.

There are two kinds of guardrails:

1. Input guardrails run on the initial user input
2. Output guardrails run on the final agent output

## Workflow boundaries

Guardrails are attached to agents and tools, but they do not all run at the same points in a workflow:

-   **Input guardrails** run only for the first agent in the chain.
-   **Output guardrails** run only for the agent that produces the final output.
-   **Tool guardrails** run on every guarded function-tool invocation, including local MCP tools when their server configures guardrails, with input guardrails before execution and output guardrails after execution.

If you need checks before and/or after each custom function-tool call in a workflow that includes managers, handoffs, or delegated specialists, use tool guardrails instead of relying only on agent-level input/output guardrails.

## Input guardrails

Input guardrails run in 3 steps:

1. First, the guardrail receives the same input passed to the agent.
2. Next, the guardrail function runs to produce a [`GuardrailFunctionOutput`][agents.guardrail.GuardrailFunctionOutput], which is then wrapped in an [`InputGuardrailResult`][agents.guardrail.InputGuardrailResult]
3. Finally, we check if [`.tripwire_triggered`][agents.guardrail.GuardrailFunctionOutput.tripwire_triggered] is true. If true, an [`InputGuardrailTripwireTriggered`][agents.exceptions.InputGuardrailTripwireTriggered] exception is raised, so you can appropriately respond to the user or handle the exception.

!!! Note

    Input guardrails are intended to run on user input, so an agent's guardrails only run if the agent is the *first* agent. You might wonder, why is the `guardrails` property on the agent instead of passed to `Runner.run`? It's because guardrails tend to be related to the actual Agent - you'd run different guardrails for different agents, so colocating the code is useful for readability.

### Execution modes

Input guardrails support two execution modes:

- **Parallel execution** (default, `run_in_parallel=True`): The guardrail runs concurrently with the agent's execution. This provides the best latency since both start at the same time. However, if the guardrail's tripwire is triggered, the agent may have already consumed tokens and executed tools before being cancelled.

- **Blocking execution** (`run_in_parallel=False`): The guardrail runs and completes *before* the agent starts. If the guardrail tripwire is triggered, the agent never executes, preventing token consumption and tool execution. This is ideal for cost optimization and when you want to avoid potential side effects from tool calls.

## Output guardrails

Output guardrails run in 3 steps:

1. First, the guardrail receives the output produced by the agent.
2. Next, the guardrail function runs to produce a [`GuardrailFunctionOutput`][agents.guardrail.GuardrailFunctionOutput], which is then wrapped in an [`OutputGuardrailResult`][agents.guardrail.OutputGuardrailResult]
3. Finally, we check if [`.tripwire_triggered`][agents.guardrail.GuardrailFunctionOutput.tripwire_triggered] is true. If true, an [`OutputGuardrailTripwireTriggered`][agents.exceptions.OutputGuardrailTripwireTriggered] exception is raised, so you can appropriately respond to the user or handle the exception.

!!! Note

    Output guardrails are intended to run on the final agent output, so an agent's guardrails only run if the agent is the *last* agent. Similar to the input guardrails, we do this because guardrails tend to be related to the actual Agent - you'd run different guardrails for different agents, so colocating the code is useful for readability.

    Output guardrails always run after the agent completes, so they don't support the `run_in_parallel` parameter.

An output tripwire and an exception raised by the guardrail function have different session behavior. A tripwire rejects the candidate final output. When a tripwire fires, the runner asks the configured session to persist already-completed tool call and tool output items, together with any reasoning context required to replay those calls, while excluding the rejected candidate final output. The runner applies this tripwire rule to both streaming and non-streaming runs. When the guardrail function raises an exception instead of returning a tripwire result, the runner treats the verdict as unknown and asks the configured session to persist the completed final-turn items before surfacing the guardrail exception. If that session write also fails, the session write error takes precedence. Streaming runs use the same persistence ordering as non-streaming runs and raise the terminal exception from `stream_events()`. An immediate [`RunResultStreaming.cancel()`][agents.result.RunResultStreaming.cancel] call while the output guardrail is running cancels the in-flight guardrail and does not start a final-turn session write.

Terminal function-tool output needs additional handling because the tool has already run before the agent-level output guardrail checks the value. When [`Agent.tool_use_behavior`][agents.agent.Agent.tool_use_behavior] makes that tool result the final output and an output tripwire rejects it, the SDK retains a replay-valid function call/output pair only when it can rebuild the pair from validated fields. The retained `function_call_output` payload is replaced with the default text `"Output withheld by an output guardrail."`; the original tool-output payload is not retained in the session, `RunState`, streamed result state, or sandbox memory input. The SDK does retain validated function-call metadata required for replay, including the function arguments, so that metadata can contain data that also appeared in the rejected output. Current-response [`OutputGuardrailResult`][agents.guardrail.OutputGuardrailResult] objects also replace `agent_output` with the resolved placeholder and clear `output_info`. Current-response [`ToolOutputGuardrailResult`][agents.tool_guardrails.ToolOutputGuardrailResult] objects preserve the allow/reject behavior type but replace payload-bearing `output_info` and rejection messages with the same placeholder. Earlier accepted turns and guardrail results remain unchanged. If the response contains reasoning or another shape that the SDK cannot sanitize safely, the SDK discards the complete current-response suffix instead of retaining the rejected output payload. A guardrail function that raises an exception has not returned a rejection verdict, so the completed terminal-tool turn follows the exception persistence behavior described above.

Set [`RunConfig.output_guardrail_blocked_message`][agents.run.RunConfig.output_guardrail_blocked_message] to a non-empty string or a synchronous formatter when your application needs a different data-free placeholder. The formatter receives [`OutputGuardrailBlockedMessageArgs`][agents.run.OutputGuardrailBlockedMessageArgs] with the SDK default, the guardrail name, the agent, and the active run context. It never receives the rejected tool output or guardrail `output_info`. The returned text is persisted and replayed wherever the SDK retains the sanitized terminal-tool turn, so keep it free of sensitive data and do not copy secrets from the run context. If the formatter raises, returns `None`, returns an empty or non-string value, or produces an awaitable, the SDK uses the default placeholder. Async formatter functions are rejected when `RunConfig` is constructed.

```python
from agents import OutputGuardrailBlockedMessageArgs, RunConfig

def blocked_message(args: OutputGuardrailBlockedMessageArgs[dict[str, str]]) -> str:
    return f"Output blocked by policy: {args.guardrail_name}."

run_config = RunConfig(output_guardrail_blocked_message=blocked_message)
```

## Tool guardrails

Tool guardrails wrap **`FunctionTool` instances** and let you validate or block calls to those tools before and after execution. They are configured on the tool itself and run every time that tool is invoked.

- Input tool guardrails run before the tool executes and can skip the call, replace the output with a message, or raise a tripwire.
- Output tool guardrails run after the tool executes and can replace the output or raise a tripwire.
- If a function tool requires approval, input tool guardrails normally run after approval and immediately before execution. Set [`RunConfig.tool_execution`][agents.run.RunConfig.tool_execution] to [`ToolExecutionConfig(pre_approval_tool_input_guardrails=True)`][agents.run.ToolExecutionConfig] when you want those input checks to run before the pending approval interruption is emitted. Calls that pass this pre-approval check are still checked again after approval before the tool executes.
- Tool guardrails use the `FunctionTool` execution pipeline. You can attach them directly to a custom tool created with `tool` or [`function_tool`][agents.tool.function_tool]. You can also set `tool_input_guardrails` and `tool_output_guardrails` on a local MCP server; the SDK attaches those lists to every tool exposed by that server. Handoffs run through the SDK's handoff pipeline rather than the function-tool pipeline, so tool guardrails do not apply to the handoff call itself. Hosted tools (`WebSearchTool`, `FileSearchTool`, `HostedMCPTool`, `CodeInterpreterTool`, `ImageGenerationTool`) and built-in execution tools (`ComputerTool`, `ShellTool`, `ApplyPatchTool`, `LocalShellTool`) do not use this guardrail pipeline, and [`Agent.as_tool()`][agents.agent.Agent.as_tool] does not currently expose tool-guardrail options directly. See [MCP server tool guardrails](mcp.md#tool-guardrails) for the local MCP configuration.

See the code snippet below for details.

## Tripwires

If an agent input or output fails a guardrail, the guardrail can signal this with a tripwire. The runner immediately raises an `InputGuardrailTripwireTriggered` or `OutputGuardrailTripwireTriggered` exception and halts agent execution. Tool guardrails use the corresponding `ToolInputGuardrailTripwireTriggered` and `ToolOutputGuardrailTripwireTriggered` exceptions.

For agent-level tripwires, the exception's `guardrail_result` identifies the guardrail that triggered the tripwire. For an input tripwire raised by the runner, `exception.run_data.input_guardrail_results` contains every input guardrail result completed before the run stopped, including the result that triggered the tripwire. Output tripwires provide the equivalent accumulated results through `exception.run_data.output_guardrail_results`.

Tool tripwire exceptions instead expose the triggering `guardrail` and `output` directly. Their `run_data.tool_input_guardrail_results` and `run_data.tool_output_guardrail_results` lists preserve results accumulated from completed turns before the failure; the triggering result is available through the exception's `output`. Other runner-managed failures, such as `MaxTurnsExceeded`, also preserve completed tool guardrail results in these lists. After `stream_events()` raises an exception, the streamed result exposes the same accumulated agent and tool guardrail result lists. `run_data` can be `None` when an exception is raised outside a runner-managed execution path.

## Implementing a guardrail

You need to provide a function that receives input, and returns a [`GuardrailFunctionOutput`][agents.guardrail.GuardrailFunctionOutput]. In this example, we'll do this by running an Agent under the hood.

```python
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
)
from agents.decorators import input_guardrail

class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

guardrail_agent = Agent( # (1)!
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
)

@input_guardrail
async def math_guardrail( # (2)!
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output, # (3)!
        tripwire_triggered=result.final_output.is_math_homework,
    )

agent = Agent(  # (4)!
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail],
)

async def main():
    # This should trip the guardrail
    try:
        await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
        print("Guardrail didn't trip - this is unexpected")

    except InputGuardrailTripwireTriggered:
        print("Math homework guardrail tripped")
```

1. We'll use this agent in our guardrail function.
2. This is the guardrail function that receives the agent's input/context, and returns the result.
3. We can include extra information in the guardrail result.
4. This is the actual agent that defines the workflow.

Output guardrails are similar.

```python
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
)
from agents.decorators import output_guardrail
class MessageOutput(BaseModel): # (1)!
    response: str

class MathOutput(BaseModel): # (2)!
    reasoning: str
    is_math: bool

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the output includes any math.",
    output_type=MathOutput,
)

@output_guardrail
async def math_guardrail(  # (3)!
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math,
    )

agent = Agent( # (4)!
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    output_guardrails=[math_guardrail],
    output_type=MessageOutput,
)

async def main():
    # This should trip the guardrail
    try:
        await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?")
        print("Guardrail didn't trip - this is unexpected")

    except OutputGuardrailTripwireTriggered:
        print("Math output guardrail tripped")
```

1. This is the actual agent's output type.
2. This is the guardrail's output type.
3. This is the guardrail function that receives the agent's output, and returns the result.
4. This is the actual agent that defines the workflow.

Lastly, here are examples of tool guardrails.

```python
import json
from agents import (
    Agent,
    Runner,
    ToolGuardrailFunctionOutput,
)
from agents.decorators import tool, tool_input_guardrail, tool_output_guardrail

@tool_input_guardrail
def block_secrets(data):
    args = json.loads(data.context.tool_arguments or "{}")
    if "sk-" in json.dumps(args):
        return ToolGuardrailFunctionOutput.reject_content(
            "Remove secrets before calling this tool."
        )
    return ToolGuardrailFunctionOutput.allow()

@tool_output_guardrail
def redact_output(data):
    text = str(data.output or "")
    if "sk-" in text:
        return ToolGuardrailFunctionOutput.reject_content("Output contained sensitive data.")
    return ToolGuardrailFunctionOutput.allow()

@tool(
    tool_input_guardrails=[block_secrets],
    tool_output_guardrails=[redact_output],
)
def classify_text(text: str) -> str:
    """Classify text for internal routing."""
    return f"length:{len(text)}"

agent = Agent(name="Classifier", tools=[classify_text])
result = Runner.run_sync(agent, "hello world")
print(result.final_output)
```

---

## handoffs

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/handoffs.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-handoffs-md.md`

# Handoffs

Handoffs allow an agent to delegate tasks to another agent. This is particularly useful in scenarios where different agents specialize in distinct areas. For example, a customer support app might have agents that each specifically handle tasks like order status, refunds, FAQs, etc.

Handoffs are represented as tools to the LLM. So if there's a handoff to an agent named `Refund Agent`, the tool would be named `transfer_to_refund_agent`.

## Creating a handoff

All agents have a [`handoffs`][agents.agent.Agent.handoffs] param, which can either take an `Agent` directly, or a `Handoff` object that customizes the Handoff.

If you pass plain `Agent` instances, their [`handoff_description`][agents.agent.Agent.handoff_description] (when set) is appended to the default tool description. Use it to hint when the model should pick that handoff without writing a full `handoff()` object.

You can create a handoff using the [`handoff()`][agents.handoffs.handoff] function provided by the Agents SDK. This function allows you to specify the agent to hand off to, along with optional overrides and input filters.

### Basic usage

Here's how you can create a simple handoff:

```python
from agents import Agent, handoff

billing_agent = Agent(name="Billing agent")
refund_agent = Agent(name="Refund agent")

# (1)!
triage_agent = Agent(name="Triage agent", handoffs=[billing_agent, handoff(refund_agent)])
```

1. You can use the agent directly (as in `billing_agent`), or you can use the `handoff()` function.

### Customizing handoffs via the `handoff()` function

The [`handoff()`][agents.handoffs.handoff] function lets you customize things.

-   `agent`: This is the agent to which things will be handed off.
-   `tool_name_override`: By default, the `Handoff.default_tool_name()` function is used, which resolves to `transfer_to_<agent_name>`. You can override this.
-   `tool_description_override`: Override the default tool description from `Handoff.default_tool_description()`
-   `on_handoff`: A callback function executed when the handoff is invoked. This is useful for things like kicking off some data fetching as soon as you know a handoff is being invoked. This function receives the agent context, and can optionally also receive LLM generated input. The input data is controlled by the `input_type` param.
-   `input_type`: The schema for the handoff tool-call arguments. When set, the parsed payload is passed to `on_handoff`.
-   `input_filter`: This lets you filter the input received by the next agent. See below for more.
-   `is_enabled`: Whether the handoff is enabled. This can be a boolean or a function that returns a boolean, allowing you to dynamically enable or disable the handoff at runtime.
-   `nest_handoff_history`: Optional per-handoff override for the RunConfig-level `nest_handoff_history` setting. If `None`, the value defined in the active run configuration is used instead.

The [`handoff()`][agents.handoffs.handoff] helper always transfers control to the specific `agent` you passed in. If you have multiple possible destinations, register one handoff per destination and let the model choose among them. Use a custom [`Handoff`][agents.handoffs.Handoff] only when your own handoff code must decide which agent to return at invocation time.

```python
from agents import Agent, handoff, RunContextWrapper

def on_handoff(ctx: RunContextWrapper[None]):
    print("Handoff called")

agent = Agent(name="My agent")

handoff_obj = handoff(
    agent=agent,
    on_handoff=on_handoff,
    tool_name_override="custom_handoff_tool",
    tool_description_override="Custom description",
)
```

## Handoff inputs

In certain situations, you want the LLM to provide some data when it calls a handoff. For example, imagine a handoff to an "Escalation agent". You might want the model to provide a reason so you can log it.

```python
from pydantic import BaseModel

from agents import Agent, handoff, RunContextWrapper

class EscalationData(BaseModel):
    reason: str

async def on_handoff(ctx: RunContextWrapper[None], input_data: EscalationData):
    print(f"Escalation agent called with reason: {input_data.reason}")

agent = Agent(name="Escalation agent")

handoff_obj = handoff(
    agent=agent,
    on_handoff=on_handoff,
    input_type=EscalationData,
)
```

`input_type` describes the arguments for the handoff tool call itself. The SDK exposes that schema to the model as the handoff tool's `parameters`, validates the returned JSON locally, and passes the parsed value to `on_handoff`.

`is_enabled` is evaluated while the SDK prepares the available handoffs, before the model returns handoff arguments, so it cannot authorize values inside an argument-bearing handoff. When authorization depends on the parsed fields, perform the check at the start of `on_handoff`, before any application side effects. If authorization fails, raise instead of returning; the SDK continues the transfer after `on_handoff` returns successfully. Tool input guardrails apply to function tools, not handoffs.

It does not replace the next agent's main input, and it does not choose a different destination. The [`handoff()`][agents.handoffs.handoff] helper still transfers to the specific agent you wrapped, and the receiving agent still sees the conversation history unless you change it with an [`input_filter`][agents.handoffs.Handoff.input_filter] or nested handoff history settings.

`input_type` is also separate from [`RunContextWrapper.context`][agents.run_context.RunContextWrapper.context]. Use `input_type` for metadata the model decides at handoff time, not for application state or dependencies you already have locally.

### When to use `input_type`

Use `input_type` when the handoff needs a small piece of model-generated metadata such as `reason`, `language`, `priority`, or `summary`. For example, a triage agent can hand off to a refund agent with `{ "reason": "duplicate_charge", "priority": "high" }`, and `on_handoff` can log or persist that metadata before the refund agent takes over.

Choose a different mechanism when the goal is different:

-   Put existing application state and dependencies in [`RunContextWrapper.context`][agents.run_context.RunContextWrapper.context]. See the [context guide](context.md).
-   Use [`input_filter`][agents.handoffs.Handoff.input_filter], [`RunConfig.nest_handoff_history`][agents.run.RunConfig.nest_handoff_history], or [`RunConfig.handoff_history_mapper`][agents.run.RunConfig.handoff_history_mapper] if you want to change what history the receiving agent sees.
-   Register one handoff per destination if there are multiple possible specialists. `input_type` can add metadata to the chosen handoff, but it does not dispatch between destinations.
-   If you want structured input for a nested specialist without transferring the conversation, prefer [`Agent.as_tool(parameters=...)`][agents.agent.Agent.as_tool]. See [tools](tools.md#structured-input-for-tool-agents).

## Input filters

When a handoff occurs, it's as though the new agent takes over the conversation, and gets to see the entire previous conversation history. If you want to change this, you can set an [`input_filter`][agents.handoffs.Handoff.input_filter]. An input filter is a function that receives the existing input via a [`HandoffInputData`][agents.handoffs.HandoffInputData], and must return a new `HandoffInputData`.

[`HandoffInputData`][agents.handoffs.HandoffInputData] includes:

-   `input_history`: the input history before `Runner.run(...)` started.
-   `pre_handoff_items`: items generated before the agent turn where the handoff was invoked.
-   `new_items`: items generated during the current turn, including the handoff call and handoff output items.
-   `input_items`: optional items to forward to the next agent instead of `new_items`, allowing you to filter model input while keeping `new_items` intact for session history.
-   `run_context`: the active [`RunContextWrapper`][agents.run_context.RunContextWrapper] at the time the handoff was invoked.

Nested handoff history is available as an opt-in beta and is disabled by default while we stabilize it. When you enable [`RunConfig.nest_handoff_history`][agents.run.RunConfig.nest_handoff_history], the runner compacts summarizable history into ordered assistant summary segments while preserving lossless message items in their original positions. Each generated summary segment uses the `<CONVERSATION HISTORY>` wrapper, and later handoffs flatten earlier generated segments before rebuilding the ordered transcript. Sessions, `RunState`, and `RunResult.to_input_list()` track exact message occurrences moved into this SDK-default history so those occurrences are not appended twice; separate identical messages are still preserved. You can provide your own mapping function via [`RunConfig.handoff_history_mapper`][agents.run.RunConfig.handoff_history_mapper] to return the exact list of input items for the next agent instead of using the built-in segmentation. The opt-in applies only when neither the handoff's `input_filter` nor the active run's `RunConfig.handoff_input_filter` is set, so existing code that already customizes the payload (including the examples in this repository) keeps its current behavior without changes. You can override the nesting behaviour for a single handoff by passing `nest_handoff_history=True` or `False` to [`handoff(...)`][agents.handoffs.handoff], which sets [`Handoff.nest_handoff_history`][agents.handoffs.Handoff.nest_handoff_history]. If you just need to change the wrapper text for generated summary segments, call [`set_conversation_history_wrappers`][agents.handoffs.set_conversation_history_wrappers] before running your agents. Call [`reset_conversation_history_wrappers`][agents.handoffs.reset_conversation_history_wrappers] before a later run when you need to restore the default wrappers.

Nested handoff history changes how the transcript is represented; it does not redact sensitive data. Tool-call arguments and tool outputs can remain in the generated assistant summary even when the corresponding structured tool items are no longer forwarded separately. Treat the receiving agent and its model provider as recipients of the forwarded history.

For client-managed history, use an explicit [`input_filter`][agents.handoffs.Handoff.input_filter] or [`RunConfig.handoff_input_filter`][agents.run.RunConfig.handoff_input_filter] to select or redact the content that the receiving agent may see. If a custom filter also calls `nest_handoff_history`, sanitize `input_history`, `pre_handoff_items`, and `new_items` before that call. The helper builds nested history from those three fields and ignores any existing `input_items` override. Filtering only `input_items` can therefore leave excluded tool content in the generated summary.

If the filter must preserve the original `new_items` for session history, the filter can instead call `nest_handoff_history` and sanitize the returned `input_history` before returning the nested result. Clearing or replacing only `input_items` after nesting does not remove content already included in `input_history`.

Server-managed conversations (`conversation_id`, `previous_response_id`, or `auto_previous_response_id`) do not support handoff input filters; use a separate run with explicitly selected input when the receiving agent must not inherit that server-managed history. Do not reuse the original `conversation_id` or `previous_response_id` in that separate run.

If both the handoff and the active [`RunConfig.handoff_input_filter`][agents.run.RunConfig.handoff_input_filter] define a filter, the per-handoff [`input_filter`][agents.handoffs.Handoff.input_filter] takes precedence for that specific handoff.

!!! note

    Handoffs stay within a single run. Input guardrails still apply only to the first agent in the chain, and output guardrails only to the agent that produces the final output. Use tool guardrails when you need checks around each custom function-tool call inside the workflow.

There are some common patterns (for example removing all tool calls from the history), which are implemented for you in [`agents.extensions.handoff_filters`][]

```python
from agents import Agent, handoff
from agents.extensions import handoff_filters

agent = Agent(name="FAQ agent")

handoff_obj = handoff(
    agent=agent,
    input_filter=handoff_filters.remove_all_tools, # (1)!
)
```

1. This will automatically remove all tool-related items from the history when `FAQ agent` is called.

`remove_all_tools` removes structured tool items. It does not redact tool arguments or results already copied into ordinary messages or nested-history summaries. Use a custom input filter to remove or redact those message contents when needed.

## Recommended prompts

To make sure that LLMs understand handoffs properly, we recommend including information about handoffs in your agents. We have a suggested prefix in [`agents.extensions.handoff_prompt.RECOMMENDED_PROMPT_PREFIX`][], or you can call [`agents.extensions.handoff_prompt.prompt_with_handoff_instructions`][] to automatically add recommended data to your prompts.

```python
from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

billing_agent = Agent(
    name="Billing agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    <Fill in the rest of your prompt here>.""",
)
```

---

## human_in_the_loop

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/human_in_the_loop.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-human-in-the-loop-md.md`

# Human-in-the-loop

Use the human-in-the-loop (HITL) flow to pause agent execution until a person approves or rejects sensitive tool calls. Tools declare when they need approval, run results surface pending approvals as interruptions, and `RunState` lets you serialize paused runs and resume them after decisions are made.

That approval surface is run-wide, not limited to the current top-level agent. The same pattern applies when the tool belongs to the current agent, to an agent reached through a handoff, or to a nested [`Agent.as_tool()`][agents.agent.Agent.as_tool] execution. In the nested `Agent.as_tool()` case, the interruption still surfaces on the outer run, so you approve or reject it on the outer `RunState` and resume the original top-level run.

With `Agent.as_tool()`, approvals can happen at two different layers: the agent tool itself can require approval via `Agent.as_tool(..., needs_approval=...)`, and tools inside the nested agent can later raise their own approvals after the nested run starts. Both are handled through the same outer-run interruption flow.

This page focuses on the manual approval flow via `interruptions`. If your app can decide in code, some tool types also support programmatic approval callbacks so the run can continue without pausing.

## Marking tools that need approval

Set `needs_approval` to `True` to always require approval or provide an async function that decides per call. The callable receives the run context, parsed tool parameters, and the tool call ID.

Callable approval rules fail closed when the SDK cannot safely inspect the arguments. If the arguments are missing, empty, contain only whitespace, are malformed JSON, are valid JSON but not an object (for example, `null` or a list), or contain non-standard constants such as `NaN`, `Infinity`, or `-Infinity`, the callable is not invoked and the call requires manual approval. This behavior is the same for Runner and Realtime tool calls.

```python
from agents import Agent
from agents.decorators import tool

@tool(needs_approval=True)
async def cancel_order(order_id: int) -> str:
    return f"Cancelled order {order_id}"

async def requires_review(_ctx, params, _call_id) -> bool:
    return "refund" in params.get("subject", "").lower()

@tool(needs_approval=requires_review)
async def send_email(subject: str, body: str) -> str:
    return f"Sent '{subject}'"

agent = Agent(
    name="Support agent",
    instructions="Handle tickets and ask for approval when needed.",
    tools=[cancel_order, send_email],
)
```

`needs_approval` is available on [`function_tool`][agents.tool.function_tool], [`Agent.as_tool`][agents.agent.Agent.as_tool], [`ShellTool`][agents.tool.ShellTool], and [`ApplyPatchTool`][agents.tool.ApplyPatchTool]. Local MCP servers also support approvals through `require_approval` on [`MCPServerStdio`][agents.mcp.server.MCPServerStdio], [`MCPServerSse`][agents.mcp.server.MCPServerSse], and [`MCPServerStreamableHttp`][agents.mcp.server.MCPServerStreamableHttp]. Hosted MCP servers support approvals via [`HostedMCPTool`][agents.tool.HostedMCPTool] with `tool_config={"require_approval": "always"}` and an optional `on_approval_request` callback. Shell and apply_patch tools accept an `on_approval` callback if you want to auto-approve or auto-reject without surfacing an interruption.

## How the approval flow works

1. When the model emits a tool call, the runner evaluates its approval rule (`needs_approval`, `require_approval`, or the hosted MCP equivalent).
2. If an approval decision for that tool call is already stored in the [`RunContextWrapper`][agents.run_context.RunContextWrapper], the runner proceeds without prompting. Per-call approvals are scoped to the specific call ID; pass `always_approve=True` or `always_reject=True` to persist the same decision for future calls to the same tool identity during the rest of the run.
3. If the approval rule requires approval and no decision for that tool call is stored, execution pauses, and `RunResult.interruptions` (or `RunResultStreaming.interruptions`) contains [`ToolApprovalItem`][agents.items.ToolApprovalItem] entries with details such as `agent.name`, `tool_name`, and `arguments`. This includes approvals raised after a handoff or inside nested `Agent.as_tool()` executions.
4. Convert the result to a `RunState` with `result.to_state()`, call `state.approve(...)` or `state.reject(...)`, and then resume with `Runner.run(agent, state)` or `Runner.run_streamed(agent, state)`, where `agent` is the original top-level agent for the run.
5. The resumed run continues where it left off and will re-enter this flow if new approvals are needed.

Sticky decisions created with `always_approve=True` or `always_reject=True` are stored in the run state, so they survive `state.to_string()` / `RunState.from_string(...)` and `state.to_json()` / `RunState.from_json(...)` when you resume the same paused run later.

For approval requests from [`HostedMCPTool`][agents.tool.HostedMCPTool], the Agents SDK identifies a sticky tool decision by the combination of `server_label` and tool name. An always-approve decision for `lookup_account` on one hosted MCP server does not approve a tool with the same name on another server. The Agents SDK persists an always-approve or always-reject decision only when the hosted MCP approval request includes both non-empty identity fields.

You do not need to resolve every pending approval in the same pass. `interruptions` can contain a mix of regular function tools, hosted MCP approvals, and nested `Agent.as_tool()` approvals. If you rerun after approving or rejecting only some items, those resolved calls can continue while unresolved ones remain in `interruptions` and pause the run again.

## Custom rejection messages

By default, a rejected tool call returns the SDK's standard rejection text back into the run. You can customize that message in two layers:

-   Run-wide fallback: set [`RunConfig.tool_error_formatter`][agents.run.RunConfig.tool_error_formatter] to control the default model-visible message for approval rejections across the whole run.
-   Per-call override: pass `rejection_message=...` to `state.reject(...)` when you want one specific rejected tool call to surface a different message.

If both are provided, the per-call `rejection_message` takes precedence over the run-wide formatter.

```python
from agents import RunConfig, ToolErrorFormatterArgs

def format_rejection(args: ToolErrorFormatterArgs[None]) -> str | None:
    if args.kind != "approval_rejected":
        return None
    return "Publish action was canceled because approval was rejected."

run_config = RunConfig(tool_error_formatter=format_rejection)

# Later, while resolving a specific interruption:
state.reject(
    interruption,
    rejection_message="Publish action was canceled because the reviewer denied approval.",
)
```

See [`examples/agent_patterns/human_in_the_loop_custom_rejection.py`](https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns/human_in_the_loop_custom_rejection.py) for a complete example that shows both layers together.

## Automatic approval decisions

Manual `interruptions` are the most general pattern, but they are not the only one:

-   Local [`ShellTool`][agents.tool.ShellTool] and [`ApplyPatchTool`][agents.tool.ApplyPatchTool] can use `on_approval` to approve or reject immediately in code.
-   [`HostedMCPTool`][agents.tool.HostedMCPTool] can use `tool_config={"require_approval": "always"}` together with `on_approval_request` for the same kind of programmatic decision.
-   Plain [`function_tool`][agents.tool.function_tool] tools and [`Agent.as_tool()`][agents.agent.Agent.as_tool] use the manual interruption flow on this page.

When these callbacks return a decision, the run continues without pausing for a human response. For Realtime and voice session APIs, see the approval flow in the [Realtime guide](realtime/guide.md).

## Streaming and sessions

The same interruption flow works in streaming runs. After a streamed run pauses, keep consuming [`RunResultStreaming.stream_events()`][agents.result.RunResultStreaming.stream_events] until the iterator finishes, inspect [`RunResultStreaming.interruptions`][agents.result.RunResultStreaming.interruptions], resolve them, and resume with [`Runner.run_streamed(...)`][agents.run.Runner.run_streamed] if you want the resumed output to keep streaming. See [Streaming](streaming.md) for the streamed version of this pattern.

If you are also using a session, keep passing the same session instance when you resume from `RunState`, or pass another session object configured for the same session ID and backing store. The resumed turn is then appended to the same stored conversation history. See [Sessions](sessions/index.md) for the session lifecycle details.

## Example: pause, approve, resume

The snippet below mirrors the JavaScript HITL guide: it pauses when a tool needs approval, persists state to disk, reloads it, and resumes after collecting a decision.

```python
import asyncio
import json
from pathlib import Path

from agents import Agent, Runner, RunState
from agents.decorators import tool

async def needs_oakland_approval(_ctx, params, _call_id) -> bool:
    return "Oakland" in params.get("city", "")

@tool(needs_approval=needs_oakland_approval)
async def get_temperature(city: str) -> str:
    return f"The temperature in {city} is 20° Celsius"

agent = Agent(
    name="Weather assistant",
    instructions="Answer weather questions with the provided tools.",
    tools=[get_temperature],
)

STATE_PATH = Path(".cache/hitl_state.json")

def prompt_approval(tool_name: str, arguments: str | None) -> bool:
    answer = input(f"Approve {tool_name} with {arguments}? [y/N]: ").strip().lower()
    return answer in {"y", "yes"}

async def main() -> None:
    result = await Runner.run(agent, "What is the temperature in Oakland?")

    while result.interruptions:
        # Persist the paused state.
        state = result.to_state()
        STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
        STATE_PATH.write_text(state.to_string())

        # Load the state later (could be a different process).
        stored = json.loads(STATE_PATH.read_text())
        state = await RunState.from_json(agent, stored)

        for interruption in result.interruptions:
            approved = await asyncio.get_running_loop().run_in_executor(
                None, prompt_approval, interruption.name or "unknown_tool", interruption.arguments
            )
            if approved:
                state.approve(interruption, always_approve=False)
            else:
                state.reject(interruption)

        result = await Runner.run(agent, state)

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

In this example, `prompt_approval` is synchronous because it uses `input()` and is executed with `run_in_executor(...)`. If your approval source is already asynchronous (for example, an HTTP request or async database query), you can use an `async def` function and `await` it directly instead.

To use streaming in a run that may pause for approvals, call `Runner.run_streamed`, consume `result.stream_events()` until it completes, and then follow the same `result.to_state()` and resume steps shown above.

## Repository patterns and examples

- **Streaming approvals**: `examples/agent_patterns/human_in_the_loop_stream.py` shows how to drain `stream_events()` and then approve pending tool calls before resuming with `Runner.run_streamed(agent, state)`.
- **Custom rejection text**: `examples/agent_patterns/human_in_the_loop_custom_rejection.py` shows how to combine run-level `tool_error_formatter` with per-call `rejection_message` overrides when approvals are rejected.
- **Agent as tool approvals**: `Agent.as_tool(..., needs_approval=...)` applies the same interruption flow when delegated agent tasks need review. Nested interruptions still surface on the outer run, so resume the original top-level agent rather than the nested one.
- **Local shell and apply_patch tools**: `ShellTool` and `ApplyPatchTool` also support `needs_approval`. Use `state.approve(interruption, always_approve=True)` or `state.reject(..., always_reject=True)` to cache the decision for future calls to that tool during the rest of the run. To resolve approval inside a callback, provide `on_approval`; `examples/tools/shell.py` demonstrates an interactive callback that prompts the operator by default. For an automatic policy that rejects every shell call, set `needs_approval=True` and `on_approval=lambda _context, _item: {"approve": False, "reason": "Disabled by policy"}` on `ShellTool`. To let the application review a paused run instead, handle interruptions (see `examples/tools/shell_human_in_the_loop.py`). Hosted shell environments do not support `needs_approval` or `on_approval`; see the [tools guide](tools.md).
- **Local MCP servers**: Use `require_approval` on `MCPServerStdio` / `MCPServerSse` / `MCPServerStreamableHttp` to gate MCP tool calls (see `examples/mcp/get_all_mcp_tools_example/main.py` and `examples/mcp/tool_filter_example/main.py`).
- **Hosted MCP servers**: Set `tool_config={"require_approval": "always"}` on `HostedMCPTool` to force HITL, optionally providing `on_approval_request` to auto-approve or reject (see `examples/hosted_mcp/human_in_the_loop.py` and `examples/hosted_mcp/on_approval.py`). Use `"never"` for trusted servers (`examples/hosted_mcp/simple.py`).
- **Sessions and memory**: Pass a session to `Runner.run` so approvals and conversation history survive multiple turns. SQLite and OpenAI Conversations session variants are in `examples/memory/memory_session_hitl_example.py` and `examples/memory/openai_session_hitl_example.py`.
- **Realtime agents**: The realtime demo exposes WebSocket messages that approve or reject tool calls via `approve_tool_call` / `reject_tool_call` on the `RealtimeSession` (see `examples/realtime/app/server.py` for the server-side handlers and [Realtime guide](realtime/guide.md#tool-approvals) for the API surface).

## Long-running approvals

`RunState` is designed to be durable. Use `state.to_json()` or `state.to_string()` to store pending work in a database or queue and recreate it later with `RunState.from_json(...)` or `RunState.from_string(...)`.

### Keep approval state on the server

Serialized `RunState` contains execution state, including approval decisions, pending tool calls, and tool arguments. The SDK restores this state; `RunState.from_json()` and `RunState.from_string()` do not authenticate the snapshot or the person submitting it. Only deserialize snapshots from trusted storage, or snapshots whose complete integrity and ownership the application has verified. A schema check or a tool-call fingerprint does not authenticate a snapshot.

For browser or mobile approval interfaces, keep the complete snapshot in application-controlled server storage. Send the reviewer only the tool details that the reviewer is authorized to see and opaque identifiers for the pending decisions. Treat tool names and arguments as untrusted display content and escape them when rendering HTML.

When a decision arrives, the server must:

1. Authenticate the reviewer using the application's session or authentication middleware. Do not take the reviewer's identity from the approval request body.
2. Authorize that reviewer to act on the stored run and the selected pending calls. Possession of a run ID or decision ID is not authorization.
3. Validate the submitted decision identifiers and boolean decisions against the pending requests stored on the server. Load the server-owned snapshot and obtain the pending items with `state.get_interruptions()`; do not accept replacement tool calls, arguments, approval records, or serialized state from the client.
4. Apply `state.approve(...)` or `state.reject(...)` to those server-owned items, then resume the run. Coordinate consumption of each pending request with storage so concurrent or replayed submissions cannot resume the same snapshot twice. In shared storage, use an atomic owner-checked transition before starting resumed execution.

The [server-side approval example](https://github.com/openai/openai-agents-python/blob/main/examples/agent_patterns/human_in_the_loop_server.py) demonstrates this pattern with a CLI client simulation and a store confined to one event loop in one process. It requires one decision for every pending call in a batch. The example consumes a request before deserialization and resumed execution, so failures and cancellations also consume the request. A production application must provide authentication, request protections, storage retention, and recovery that reconciles tool side effects before retrying; this example is not a deployable HTTP service.

Replacing `context` with `context_override`, setting `strict_context=True`, or removing only the serialized approval records does not make an untrusted snapshot safe. Other fields still control resumed execution. If an application transports the complete snapshot through a client, the application must verify its integrity, bind it to the authorized user and run, and prevent replay before deserialization. Such verification does not encrypt the snapshot or hide its contents from the client.

### Serialization options

Useful serialization options:

-   `context_serializer`: Customize how non-mapping context objects are serialized.
-   `context_deserializer`: Rebuild non-mapping context objects when loading state with `RunState.from_json(...)` or `RunState.from_string(...)`.
- `strict_context=True`: Fail serialization unless the context is already a mapping or you provide `context_serializer`; fail deserialization unless the context is already a mapping or you provide `context_deserializer`.
- `context_override`: Replace the serialized context when loading state. This is useful when you do not want to restore the original context object, but it does not remove that context from an already serialized payload.
- `include_tracing_api_key=True`: Include the tracing API key in the serialized trace payload when you need resumed work to keep exporting traces with the same credentials.

Serialized run state includes your app context plus SDK-managed runtime metadata such as approvals, usage, serialized `tool_input`, nested agent-as-tool resumptions, trace metadata, and server-managed conversation settings. If you plan to store or transmit serialized state, treat `RunContextWrapper.context` as persisted data and avoid placing secrets there unless you intentionally want them to travel with the state.

## Versioning pending tasks

If approvals may sit for a while, store a version marker for your agent definitions or SDK alongside the serialized state. You can then route deserialization to the matching code path to avoid incompatibilities when models, prompts, or tool definitions change.

---

## index

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/index.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-index-md.md`

# OpenAI Agents SDK

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, [Swarm](https://github.com/openai/swarm/tree/main). The Agents SDK has a very small set of primitives:

-   **Agents**, which are LLMs equipped with instructions and tools
-   **Agents as tools / Handoffs**, which allow agents to delegate to other agents for specific tasks
-   **Guardrails**, which enable validation of agent inputs and outputs

In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in **tracing** that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

## Why use the Agents SDK

The SDK has two driving design principles:

1. Enough features to be worth using, but few enough primitives to make it quick to learn.
2. Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

-   **Agents**: Build agents with instructions, tools, guardrails, handoffs, and a built-in loop that continues until the task is complete.
-   **Sandbox agents**: Run specialists inside real isolated workspaces. Sandbox agents support manifest-defined files, sandbox client selection, and resumable sandbox sessions.
-   **Realtime agents**: Build powerful voice agents with `gpt-realtime-2.1`, automatic interruption detection, context management, guardrails, and more.
-   **Voice agents**: Build voice pipelines that combine speech-to-text, an agent workflow, and text-to-speech.
-   **Python-first**: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
-   **Agents as tools / Handoffs**: A powerful mechanism for coordinating and delegating work across multiple agents.
-   **Guardrails**: Run input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass.
-   **Function tools**: Turn any Python function into a tool with automatic schema generation and Pydantic-powered validation.
-   **MCP server tool calling**: Built-in integration that exposes remote MCP tools to agents alongside function tools.
-   **Sessions**: A persistent memory layer for maintaining working context within an agent loop.
-   **Human in the loop**: Built-in mechanisms for involving humans during agent runs.
-   **Tracing**: Built-in tracing for visualizing, debugging, and monitoring workflows, with support for the OpenAI suite of evaluation, fine-tuning, and distillation tools.

## Agents SDK or Responses API?

The SDK uses the Responses API by default for OpenAI models, but it wraps model calls in a higher-level runtime.

Use the Responses API directly when:

-   you want to own the loop, tool dispatch, and state handling yourself
-   your workflow is short-lived and mainly about returning the model's response

Use the Agents SDK when:

-   you want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions
-   your agent should produce artifacts or operate across multiple coordinated steps
-   you need a real workspace or resumable execution through [Sandbox agents](sandbox_agents.md)

You do not need to choose one globally. Many applications use the SDK for managed workflows and call the Responses API directly for lower-level paths.

## Installation

```bash
pip install openai-agents
```

## Hello world example

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

(_If running this, ensure you set the `OPENAI_API_KEY` environment variable_)

```bash
export OPENAI_API_KEY=sk-...
```

## Start here

-   Build your first text-based agent with the [Quickstart](quickstart.md).
-   Then decide how you want to carry state across turns in [Running agents](running_agents.md#choose-a-memory-strategy).
-   If the task depends on real files, repos, or isolated per-agent workspace state, read the [Sandbox agents quickstart](sandbox_agents.md).
-   If you are deciding between handoffs and manager-style orchestration, read [Agent orchestration](multi_agent.md).

## Choose your path

Use this table when you know the job you want to do, but not which page explains it.

| Goal | Start here |
| --- | --- |
| Build the first text agent and see one complete run | [Quickstart](quickstart.md) |
| Add function tools, hosted tools, or agents as tools | [Tools](tools.md) |
| Run a coding, review, or document agent inside a real isolated workspace | [Sandbox agents quickstart](sandbox_agents.md) and [Sandbox clients](sandbox/clients.md) |
| Decide between handoffs and manager-style orchestration | [Agent orchestration](multi_agent.md) |
| Keep memory across turns | [Running agents](running_agents.md#choose-a-memory-strategy) and [Sessions](sessions/index.md) |
| Use OpenAI models, websocket transport, or non-OpenAI providers | [Models](models/index.md) |
| Review outputs, run items, interruptions, and resume state | [Results](results.md) |
| Build a low-latency voice agent with `gpt-realtime-2.1` | [Realtime agents quickstart](realtime/quickstart.md) and [Realtime transport](realtime/transport.md) |
| Build a speech-to-text / agent / text-to-speech pipeline | [Voice pipeline quickstart](voice/quickstart.md) |

---

## llms-full.txt

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/llms-full.txt
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-llms-full-txt.md`

# OpenAI Agents SDK Documentation (Full Context)

> Extended reference map for the OpenAI Agents SDK documentation site. Use these curated links when assembling prompts that need authoritative guidance on building, operating, and extending agentic applications with the SDK.

The Agents SDK delivers a focused set of Python primitives—agents, tools, guardrails, handoffs, sessions, and tracing—plus voice and realtime interfaces. The pages below provide detailed walkthroughs, architectural patterns, and API-level documentation for integrating those capabilities into production systems.

## Getting Started and Orientation
- [Overview](https://openai.github.io/openai-agents-python/): Conceptual tour of the SDK, covering the core agent loop, motivation, installation snippet, and a runnable hello-world.
- [Quickstart](https://openai.github.io/openai-agents-python/quickstart/): Guided setup from environment preparation through running and monitoring your first agent, including troubleshooting tips.
- [Example Gallery](https://openai.github.io/openai-agents-python/examples/): Realistic Python samples that demonstrate tool orchestration, guardrails, streaming, and integrations with external systems.
- [Release notes](https://openai.github.io/openai-agents-python/release/): Version-by-version change log with migration notes for breaking updates.
- [Usage and pricing](https://openai.github.io/openai-agents-python/usage/): Explains how token usage is tracked, how to retrieve usage metadata, and how to forecast cost for different deployment patterns.
- [Configuration](https://openai.github.io/openai-agents-python/config/): Centralized reference for tuning model settings, retries, rate limits, timeouts, logging, and runner behavior.

## Core Agent Workflows
- [Agents](https://openai.github.io/openai-agents-python/agents/): Defines agent objects, instruction design, tool registration, guardrail attachment, streaming options, and lifecycle hooks.
- [Running agents](https://openai.github.io/openai-agents-python/running_agents/): Covers synchronous and asynchronous execution, concurrency controls, background tasks, cancellation, and handling failures.
- [Sessions](https://openai.github.io/openai-agents-python/sessions/): Describes persistent session state, conversation threading, history pruning, and custom session storage backends.
- [Context strategies](https://openai.github.io/openai-agents-python/context/): Techniques for tailoring prompts, managing attachments, trimming history, and injecting auxiliary context into runs.
- [Results](https://openai.github.io/openai-agents-python/results/): Breaks down the result object, including final output, tool call transcripts, intermediate messages, and metadata fields.
- [Streaming](https://openai.github.io/openai-agents-python/streaming/): Shows how to subscribe to incremental events, stream tool progress, and render partial model outputs in real time.
- [REPL](https://openai.github.io/openai-agents-python/repl/): Interactive runner for exploring agent behavior, step-by-step execution, and debugging tool calls.
- [Visualization](https://openai.github.io/openai-agents-python/visualization/): Demonstrates embeddable visualizations for session timelines, message flows, and tool interactions.
- [Testing](https://openai.github.io/openai-agents-python/testing/): Build deterministic, provider-neutral tests for Agent, Sandbox, Realtime, and Voice workflows.

## Coordination, Safety, and Tooling
- [Handoffs](https://openai.github.io/openai-agents-python/handoffs/): Implements delegation between agents, argument passing, completion handling, and error recovery across agent boundaries.
- [Multi-agent patterns](https://openai.github.io/openai-agents-python/multi_agent/): Architecture playbook for designing specialist teams, escalation workflows, and role-based collaboration strategies.
- [Guardrails](https://openai.github.io/openai-agents-python/guardrails/): Create synchronous or asynchronous checks, short-circuit runs, and emit structured validation reports.
- [Tools](https://openai.github.io/openai-agents-python/tools/): Turn Python callables into structured tools, manage schemas, compose tool contexts, and test tool execution paths.
- [Model Context Protocol](https://openai.github.io/openai-agents-python/mcp/): Integrate MCP servers so agents can dynamically request data or actions from external providers via a standard protocol.

## Modality-Specific Guides
- [Voice quickstart](https://openai.github.io/openai-agents-python/voice/quickstart/): Build an end-to-end voice assistant with streaming transcription, text-to-speech, and event-driven responses.
- [Voice pipeline](https://openai.github.io/openai-agents-python/voice/pipeline/): Customize audio capture, buffering, model invocation, and playback in voice-first experiences.
- [Voice tracing](https://openai.github.io/openai-agents-python/voice/tracing/): Inspect voice session traces, latency breakdowns, and audio event timelines.
- [Realtime quickstart](https://openai.github.io/openai-agents-python/realtime/quickstart/): Launch realtime agents over websockets (WebRTC is not available in the Python SDK), subscribe to events, and manage low-latency execution.
- [Realtime transport](https://openai.github.io/openai-agents-python/realtime/transport/): Choose between the default server-side WebSocket path and SIP attach flows, with the browser WebRTC boundary called out explicitly.
- [Realtime guide](https://openai.github.io/openai-agents-python/realtime/guide/): Deep dive into realtime session lifecycle, structured input, approvals, interruptions, and low-level transport control.

## Models and Provider Integrations
- [Model catalog](https://openai.github.io/openai-agents-python/models/): Covers OpenAI model selection, non-OpenAI provider patterns, websocket transport, and third-party adapter guidance in one place.

## API Reference – Agents SDK Core
- [API index](https://openai.github.io/openai-agents-python/ref/index/): Directory of all documented modules, classes, and functions in the SDK.
- [agents.Agent](https://openai.github.io/openai-agents-python/ref/agent/): Constructor arguments, behaviors, guardrail hooks, and serialization helpers.
- [runs and runners](https://openai.github.io/openai-agents-python/ref/run/): Runner interfaces for launching agents, streaming events, handling cancellations, and background execution.
- [memory interfaces](https://openai.github.io/openai-agents-python/ref/memory/): Session memory primitives, storage adapters, and utilities for retrieving historical context.
- [repl utilities](https://openai.github.io/openai-agents-python/ref/repl/): Programmatic access to the interactive REPL loop and inspection helpers.
- [tool base classes](https://openai.github.io/openai-agents-python/ref/tool/): Tool registration, invocation, and structured argument parsing.
- [testing utilities](https://openai.github.io/openai-agents-python/ref/testing/): Deterministic utilities for Agent model calls and Sandbox workflows.
- [tool context helpers](https://openai.github.io/openai-agents-python/ref/tool_context/): Manage shared resources, dependency injection, and cleanup for tool execution.
- [result objects](https://openai.github.io/openai-agents-python/ref/result/): Fields exposed on run results, including final content, tool call summaries, and attachments.
- [stream events](https://openai.github.io/openai-agents-python/ref/stream_events/): Event models emitted during streaming runs and their payload schemas.
- [handoffs module](https://openai.github.io/openai-agents-python/ref/handoffs/): Programmatic API for defining, routing, and resolving handoffs between agents.
- [lifecycle callbacks](https://openai.github.io/openai-agents-python/ref/lifecycle/): Hooks for intercepting agent stages, customizing evaluation, and logging intermediate data.
- [items API](https://openai.github.io/openai-agents-python/ref/items/): Low-level primitives that represent agent messages, tool calls, and attachments.
- [run context utilities](https://openai.github.io/openai-agents-python/ref/run_context/): Context managers and helpers for passing metadata through nested tool executions.
- [usage tracking](https://openai.github.io/openai-agents-python/ref/usage/): Inspect token usage, durations, and cost metrics from completed runs.
- [exceptions](https://openai.github.io/openai-agents-python/ref/exceptions/): Exception hierarchy raised by the SDK and recommendations for resilient error handling.
- [guardrail APIs](https://openai.github.io/openai-agents-python/ref/guardrail/): Build custom guardrails, interpret validation outcomes, and integrate enforcement logic.
- [model settings](https://openai.github.io/openai-agents-python/ref/model_settings/): Shared configuration objects for model parameters, temperature, and tool invocation settings.
- [agent output models](https://openai.github.io/openai-agents-python/ref/agent_output/): Typed models describing message content, tool calls, and aggregated agent responses.
- [function schema utilities](https://openai.github.io/openai-agents-python/ref/function_schema/): Helpers for generating JSON schemas from Python functions and Pydantic models.
- [model interfaces](https://openai.github.io/openai-agents-python/ref/models/interface/): Abstractions for pluggable model providers.
- [OpenAI chat completions provider](https://openai.github.io/openai-agents-python/ref/models/openai_chatcompletions/): Implementation details for the chat-completions-based model adapter.
- [OpenAI responses provider](https://openai.github.io/openai-agents-python/ref/models/openai_responses/): Implementation details for the responses API adapter.
- [MCP server helpers](https://openai.github.io/openai-agents-python/ref/mcp/server/): Utilities for building MCP servers that expose tools to agents.
- [MCP client utilities](https://openai.github.io/openai-agents-python/ref/mcp/util/): Helpers for consuming MCP servers from within agents.

## API Reference – Tracing
- [Tracing overview](https://openai.github.io/openai-agents-python/ref/tracing/index/): End-to-end API documentation for tracing components.
- [Creating traces](https://openai.github.io/openai-agents-python/ref/tracing/create/): Programmatic APIs for instantiating traces and attaching metadata.
- [Trace model](https://openai.github.io/openai-agents-python/ref/tracing/traces/): Data models representing traces and their relationships.
- [Span model](https://openai.github.io/openai-agents-python/ref/tracing/spans/): Span structure, timing data, and message attribution.
- [Processor interface](https://openai.github.io/openai-agents-python/ref/tracing/processor_interface/): Contract for custom processors that consume trace events.
- [Bundled processors](https://openai.github.io/openai-agents-python/ref/tracing/processors/): Built-in processors for exporting traces to external systems.
- [Tracing scope](https://openai.github.io/openai-agents-python/ref/tracing/scope/): Context managers that manage active traces and spans.
- [Tracing setup](https://openai.github.io/openai-agents-python/ref/tracing/setup/): Configuration helpers for initializing tracing in applications and tests.
- [Span data utilities](https://openai.github.io/openai-agents-python/ref/tracing/span_data/): Helper models for span payloads and events.
- [Tracing utility helpers](https://openai.github.io/openai-agents-python/ref/tracing/util/): Miscellaneous tracing utilities, exporters, and logging helpers.

## API Reference – Realtime
- [Realtime agent API](https://openai.github.io/openai-agents-python/ref/realtime/agent/): Programmatic interface for realtime agents.
- [Realtime runner](https://openai.github.io/openai-agents-python/ref/realtime/runner/): Manage realtime execution loops, concurrency, and cleanup.
- [Realtime session](https://openai.github.io/openai-agents-python/ref/realtime/session/): Lifecycle and state management for realtime sessions.
- [Realtime events](https://openai.github.io/openai-agents-python/ref/realtime/events/): Event payload types delivered over realtime channels.
- [Realtime config](https://openai.github.io/openai-agents-python/ref/realtime/config/): Configuration models for realtime transports and behaviors.
- [Realtime model interface](https://openai.github.io/openai-agents-python/ref/realtime/model/): Interfaces for plugging in realtime-capable models.
- [Realtime testing](https://openai.github.io/openai-agents-python/ref/realtime/testing/): Scripted model utilities for Realtime session and tool workflow tests.

## API Reference – Voice
- [Voice pipeline API](https://openai.github.io/openai-agents-python/ref/voice/pipeline/): Programmatic control over the voice pipeline and event flow.
- [Voice workflow helpers](https://openai.github.io/openai-agents-python/ref/voice/workflow/): Orchestrate conversational voice workflows.
- [Voice input models](https://openai.github.io/openai-agents-python/ref/voice/input/): Structured representations of microphone and streaming audio input.
- [Voice result models](https://openai.github.io/openai-agents-python/ref/voice/result/): Output schema for voice responses, transcripts, and tool invocations.
- [Voice pipeline config](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/): Configuration options for buffer sizes, concurrency, and model routing.
- [Voice events](https://openai.github.io/openai-agents-python/ref/voice/events/): Event payloads describing voice session updates.
- [Voice exceptions](https://openai.github.io/openai-agents-python/ref/voice/exceptions/): Exception types for voice pipelines and error handling guidance.
- [Voice model adapters](https://openai.github.io/openai-agents-python/ref/voice/model/): Interfaces for voice-enabled models and synthesis engines.
- [Voice utility helpers](https://openai.github.io/openai-agents-python/ref/voice/utils/): Audio conversion, streaming helpers, and testing utilities.
- [Voice testing](https://openai.github.io/openai-agents-python/ref/voice/testing/): Scripted STT, TTS, transcription, and workflow test utilities.
- [OpenAI voice provider](https://openai.github.io/openai-agents-python/ref/voice/models/openai_provider/): Adapter for OpenAI voice models.
- [OpenAI speech-to-text provider](https://openai.github.io/openai-agents-python/ref/voice/models/openai_stt/): Integration for STT models used in the pipeline.
- [OpenAI text-to-speech provider](https://openai.github.io/openai-agents-python/ref/voice/models/openai_tts/): Adapter for OpenAI TTS output.

## API Reference – Extensions
- [Handoff filters extension](https://openai.github.io/openai-agents-python/ref/extensions/handoff_filters/): Build filters that decide whether to trigger a handoff.
- [Handoff prompt extension](https://openai.github.io/openai-agents-python/ref/extensions/handoff_prompt/): Customize prompt templates used when transferring control.
- [Third-party adapters API reference](https://openai.github.io/openai-agents-python/ref/extensions/): API reference entry point for Any-LLM and LiteLLM model adapters and providers.
- [SQLAlchemy session memory](https://openai.github.io/openai-agents-python/ref/extensions/memory/sqlalchemy_session/): Persist agent session history to SQL databases.

## Optional
- [Japanese documentation](https://openai.github.io/openai-agents-python/ja/): Localized guides mirroring the core English documentation.
- [GitHub repository](https://github.com/openai/openai-agents-python): Source code, issues, and contribution resources.
- [Agents SDK package on PyPI](https://pypi.org/project/openai-agents/): Distribution page with installation command and release history.

---

## llms.txt

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/llms.txt
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-llms-txt.md`

# OpenAI Agents SDK Documentation

> Official documentation for building production-ready agentic applications with the OpenAI Agents SDK, a Python toolkit that equips LLM-powered assistants with tools, guardrails, handoffs, sessions, tracing, voice, and realtime capabilities.

The SDK focuses on a concise set of primitives so you can orchestrate multi-agent workflows without heavy abstractions. These pages explain how to install the library, design agents, coordinate tools, handle results, and extend the platform to new modalities.

## Start Here
- [Overview](https://openai.github.io/openai-agents-python/): Learn the core primitives—agents, handoffs, guardrails, sessions, and tracing—and see a minimal hello-world example.
- [Quickstart](https://openai.github.io/openai-agents-python/quickstart/): Step-by-step setup for installing the package, configuring API keys, and running your first agent locally.
- [Example Gallery](https://openai.github.io/openai-agents-python/examples/): Task-oriented examples that demonstrate agent loops, tool usage, guardrails, and integration patterns.

## Core Concepts
- [Agents](https://openai.github.io/openai-agents-python/agents/): Configure agent instructions, tools, guardrails, memory, and streaming behavior.
- [Running agents](https://openai.github.io/openai-agents-python/running_agents/): Learn synchronous, asynchronous, and batched execution, plus cancellation and error handling.
- [Sessions](https://openai.github.io/openai-agents-python/sessions/): Manage stateful conversations with automatic history persistence and memory controls.
- [Results](https://openai.github.io/openai-agents-python/results/): Inspect agent outputs, tool calls, follow-up actions, and metadata returned by the runner.
- [Streaming](https://openai.github.io/openai-agents-python/streaming/): Stream intermediate tool usage and LLM responses for responsive UIs.
- [REPL](https://openai.github.io/openai-agents-python/repl/): Use the interactive runner to prototype agents and inspect execution step by step.
- [Context strategies](https://openai.github.io/openai-agents-python/context/): Control what past messages, attachments, and tool runs are injected into prompts.
- [Testing](https://openai.github.io/openai-agents-python/testing/): Test Agent, Sandbox, Realtime, and Voice workflows deterministically without provider requests.

## Coordination and Safety
- [Handoffs](https://openai.github.io/openai-agents-python/handoffs/): Delegate tasks between agents with intent classification, argument passing, and return values.
- [Multi-agent patterns](https://openai.github.io/openai-agents-python/multi_agent/): Architect teams of agents that collaborate, escalate, or specialize by capability.
- [Guardrails](https://openai.github.io/openai-agents-python/guardrails/): Define validators that run alongside the agent loop to enforce business and safety rules.
- [Tools](https://openai.github.io/openai-agents-python/tools/): Register Python callables as structured tools, manage schemas, and work with tool contexts.
- [Model Context Protocol](https://openai.github.io/openai-agents-python/mcp/): Connect MCP servers so agents can request external data or actions through standardized tool APIs.

## Operations and Configuration
- [Usage and pricing](https://openai.github.io/openai-agents-python/usage/): Understand token accounting, usage metrics, and cost estimation.
- [Configuration](https://openai.github.io/openai-agents-python/config/): Tune model selection, retry logic, rate limits, and runner policies for production workloads.
- [Visualization](https://openai.github.io/openai-agents-python/visualization/): Embed tracing dashboards and visualize agent runs directly in notebooks and web apps.

## Observability and Tracing
- [Tracing](https://openai.github.io/openai-agents-python/tracing/): Capture spans for every agent step, emit data to OpenAI traces, and integrate third-party processors.

## Modalities and Interfaces
- [Voice quickstart](https://openai.github.io/openai-agents-python/voice/quickstart/): Build speech-enabled agents with streaming transcription and TTS.
- [Voice pipeline](https://openai.github.io/openai-agents-python/voice/pipeline/): Customize audio ingestion, tool execution, and response rendering.
- [Realtime quickstart](https://openai.github.io/openai-agents-python/realtime/quickstart/): Stand up low-latency realtime agents with websocket transport (WebRTC is not available in the Python SDK).
- [Realtime transport](https://openai.github.io/openai-agents-python/realtime/transport/): Decide between the default server-side WebSocket path and SIP attach flows, with the browser WebRTC boundary called out explicitly.
- [Realtime guide](https://openai.github.io/openai-agents-python/realtime/guide/): Deep dive into session lifecycle, structured input, approvals, interruptions, and low-level transport control.

## API Reference Highlights
- [Agents API index](https://openai.github.io/openai-agents-python/ref/index/): Entry point for class and function documentation throughout the SDK.
- [Agent lifecycle](https://openai.github.io/openai-agents-python/ref/lifecycle/): Understand the runner, evaluation phases, and callbacks triggered during execution.
- [Runs and sessions](https://openai.github.io/openai-agents-python/ref/run/): API for launching runs, streaming updates, and handling cancellations.
- [Results objects](https://openai.github.io/openai-agents-python/ref/result/): Data structures returned from agent runs, including final output and tool calls.
- [Tool interfaces](https://openai.github.io/openai-agents-python/ref/tool/): Create tools, parse arguments, and manage tool execution contexts.
- [Testing APIs](https://openai.github.io/openai-agents-python/ref/testing/): Reference provider-neutral testing utilities for Agent model calls and Sandbox workflows.
- [Tracing APIs](https://openai.github.io/openai-agents-python/ref/tracing/index/): Programmatic interfaces for creating traces, spans, and integrating custom processors.
- [Realtime APIs](https://openai.github.io/openai-agents-python/ref/realtime/agent/): Classes for realtime agents, runners, sessions, and event payloads.
- [Voice APIs](https://openai.github.io/openai-agents-python/ref/voice/pipeline/): Configure voice pipelines, inputs, events, and model adapters.
- [Extensions](https://openai.github.io/openai-agents-python/ref/extensions/handoff_filters/): Extend the SDK with custom handoff filters, prompts, third-party adapters, and SQLAlchemy session memory.

## Models and Providers
- [Model catalog](https://openai.github.io/openai-agents-python/models/): Overview of OpenAI models, non-OpenAI provider patterns, websocket transport, and third-party adapter guidance.

## Optional
- [Release notes](https://openai.github.io/openai-agents-python/release/): Track SDK changes, migration notes, and deprecations.
- [Japanese documentation](https://openai.github.io/openai-agents-python/ja/): Localized overview and quickstart for Japanese-speaking developers.
- [Repository on GitHub](https://github.com/openai/openai-agents-python): Source code, issues, and contribution guidelines for the SDK.

---

## mcp

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/mcp.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-mcp-md.md`

# Model context protocol (MCP)

The [Model context protocol](https://modelcontextprotocol.io/introduction) (MCP) standardises how applications expose tools and
context to language models. From the official documentation:

> MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI
> applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP
> provides a standardized way to connect AI models to different data sources and tools.

The Agents Python SDK understands multiple MCP transports. This lets you reuse existing MCP servers or build your own to expose filesystem, HTTP, or connector backed tools to an agent.

!!! warning "Trust MCP servers before connecting"

    MCP tools can expose data from the model context and perform actions with the credentials you provide. Connect only to servers you trust, use least-privilege credentials, keep access tokens in authorization fields or headers rather than URLs, and require approval for sensitive operations. See the [OpenAI MCP security guidance](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#risks-and-safety).

## Choosing an MCP integration

Before wiring an MCP server into an agent decide where the tool calls should execute and which transports you can reach. The matrix below summarises the options that the Python SDK supports.

| What you need                                                                        | Recommended option                                    |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| Let OpenAI's Responses API call a publicly reachable MCP server on the model's behalf| **Hosted MCP server tools** via [`HostedMCPTool`][agents.tool.HostedMCPTool] |
| Connect to Streamable HTTP servers that you run locally or remotely                  | **Streamable HTTP MCP servers** via [`MCPServerStreamableHttp`][agents.mcp.server.MCPServerStreamableHttp] |
| Talk to servers that implement HTTP with Server-Sent Events                          | **HTTP with SSE MCP servers** via [`MCPServerSse`][agents.mcp.server.MCPServerSse] |
| Launch a local process and communicate over stdin/stdout                             | **stdio MCP servers** via [`MCPServerStdio`][agents.mcp.server.MCPServerStdio] |

The sections below walk through each option, how to configure it, and when to prefer one transport over another.

## MCP Python SDK v1 and v2

The Agents SDK supports both major versions of the `mcp` Python package through the dependency range `mcp>=1.19.0,<3`. The installed `mcp` package version is separate from the MCP protocol version negotiated with a server. The Agents SDK detects the installed package major version and adapts stdio, SSE, and Streamable HTTP connections automatically, so ordinary server configuration does not need a version switch.

When MCP Python SDK v2 is installed, the Agents SDK creates the v2 `mcp.Client` with `mode="auto"` around the configured local transport. The client first sends a `server/discover` probe at the newest protocol version supported by the installed MCP SDK. A modern server answers the probe, and the client adopts the result. If an older server does not support `server/discover`, the client falls back to the legacy `initialize` handshake and uses the protocol version negotiated there. Installing MCP Python SDK v2 therefore does not force every connection to use the newest MCP protocol version. See the MCP Python SDK's [protocol version negotiation guide](https://py.sdk.modelcontextprotocol.io/protocol-versions/).

Most applications should let their dependency resolver select a compatible version. If your application must stay on one major version, add an explicit constraint alongside `openai-agents`:

```bash
# MCP Python SDK v1
pip install "mcp>=1.19.0,<2"

# MCP Python SDK v2
pip install "mcp>=2,<3"
```

HTTP transport customization must use the HTTP stack owned by the installed MCP package:

| Customization | MCP Python SDK v1 | MCP Python SDK v2 |
| --- | --- | --- |
| `params["auth"]` | `httpx.Auth` | `httpx2.Auth` |
| `params["httpx_client_factory"]` return value | `httpx.AsyncClient` | `httpx2.AsyncClient` |
| `MCPServerStreamableHttp` `params["ignore_initialized_notification_failure"] = True` | Supported | Not supported; rejected before connecting |

Use an `Authorization` header when possible, as shown in the Streamable HTTP example below; an `Authorization` header works unchanged with both package versions. When an application supplies `params["auth"]` or `params["httpx_client_factory"]`, those values must use the HTTP types for the installed `mcp` package major version. When an application sets `MCPServerStreamableHttp`'s `params["ignore_initialized_notification_failure"] = True`, the application must keep `mcp<2` or disable the option before upgrading.

These local `mcp` dependency requirements do not apply to [`HostedMCPTool`][agents.tool.HostedMCPTool] because the OpenAI Responses API owns the remote MCP connection.

## Agent-level MCP configuration

In addition to choosing a transport, you can tune how MCP tools are prepared by setting `Agent.mcp_config`.

```python
from agents import Agent

agent = Agent(
    name="Assistant",
    mcp_servers=[server],
    mcp_config={
        # Try to convert MCP tool schemas to strict JSON schema.
        "convert_schemas_to_strict": True,
        # If None, MCP tool failures are raised as exceptions instead of
        # returning model-visible error text.
        "failure_error_function": None,
        # Prefix local MCP tool names with their server name.
        "include_server_in_tool_names": True,
    },
)
```

Notes:

- `convert_schemas_to_strict` is best-effort. If a schema cannot be converted, the original schema is used.
- `failure_error_function` controls how MCP tool call failures are surfaced to the model.
- When `failure_error_function` is unset, the SDK uses the default tool error formatter.
- Server-level `failure_error_function` overrides `Agent.mcp_config["failure_error_function"]` for that server.
- `include_server_in_tool_names` is opt-in. When enabled, each local MCP tool is exposed to the model with a deterministic server-prefixed name, which helps avoid collisions when multiple MCP servers publish tools with the same name. Generated names are ASCII-safe, stay within the name-length limit for `FunctionTool` instances, and do not collide with the configured names of local `FunctionTool` instances or enabled handoffs on the same agent. The SDK still invokes the original MCP tool name on the original server.

## Shared patterns across transports

After you choose a transport, most integrations need the same follow-up decisions:

- How to expose only a subset of tools ([Tool filtering](#tool-filtering)).
- Whether the server also provides reusable prompts ([Prompts](#prompts)).
- Whether `list_tools()` should be cached ([Caching](#caching)).
- How MCP activity appears in traces ([Tracing](#tracing)).

For local MCP servers (`MCPServerStdio`, `MCPServerSse`, `MCPServerStreamableHttp`), approval policies and per-call `_meta` payloads are also shared concepts. The Streamable HTTP section shows the most complete examples, and the same patterns apply to the other local transports.

## 1. Hosted MCP server tools

Hosted tools push the entire tool round-trip into OpenAI's infrastructure. Instead of your code listing and calling tools, the [`HostedMCPTool`][agents.tool.HostedMCPTool] forwards a server label (and optional connector metadata) to the Responses API. The model lists the remote server's tools and invokes them without an extra callback to your Python process. Hosted tools currently work with OpenAI models that support the Responses API's hosted MCP integration.

### Basic hosted MCP tool

Create a hosted tool by adding a [`HostedMCPTool`][agents.tool.HostedMCPTool] to the agent's `tools` list. The `tool_config`
dict mirrors the JSON you would send to the REST API:

```python
import asyncio

from agents import Agent, HostedMCPTool, Runner

async def main() -> None:
    agent = Agent(
        name="Assistant",
        instructions="Use the DeepWiki hosted MCP server to inspect openai/openai-agents-python.",
        tools=[
            HostedMCPTool(
                tool_config={
                    "type": "mcp",
                    "server_label": "deepwiki",
                    "server_url": "https://mcp.deepwiki.com/mcp",
                    "require_approval": "never",
                }
            )
        ],
    )

    result = await Runner.run(
        agent,
        "Which language is the repository openai/openai-agents-python written in?",
    )
    print(result.final_output)

asyncio.run(main())
```

The hosted server exposes its tools automatically; you do not add it to `mcp_servers`.

If you want hosted tool search to load a hosted MCP server lazily, set `tool_config["defer_loading"] = True` and add [`ToolSearchTool`][agents.tool.ToolSearchTool] to the agent. This is supported only on OpenAI Responses models. See [Tools](tools.md#hosted-tool-search) for the complete tool-search setup and constraints.

### Streaming hosted MCP results

Hosted tools support streaming results in exactly the same way as function tools. Use `Runner.run_streamed` to
consume incremental MCP output while the model is still working:

```python
result = Runner.run_streamed(agent, "Summarise this repository's top languages")
async for event in result.stream_events():
    if event.type == "run_item_stream_event":
        print(f"Received: {event.item}")
print(result.final_output)
```

### Optional approval flows

If a server can perform sensitive operations you can require human or programmatic approval before each tool execution. Configure `require_approval` in the `tool_config` with either a single policy (`"always"`, `"never"`) or a dict mapping tool names to policies. To make the decision inside Python, provide an `on_approval_request` callback.

```python
from agents import MCPToolApprovalFunctionResult, MCPToolApprovalRequest

SAFE_TOOLS = {"read_wiki_structure", "read_wiki_contents", "ask_question"}

def approve_tool(request: MCPToolApprovalRequest) -> MCPToolApprovalFunctionResult:
    if request.data.name in SAFE_TOOLS:
        return {"approve": True}
    return {"approve": False, "reason": "Escalate to a human reviewer"}

agent = Agent(
    name="Assistant",
    tools=[
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "deepwiki",
                "server_url": "https://mcp.deepwiki.com/mcp",
                "require_approval": "always",
            },
            on_approval_request=approve_tool,
        )
    ],
)
```

The callback can be synchronous or asynchronous and is invoked whenever the model needs approval data to keep running.

### Connector-backed hosted servers

Hosted MCP also supports OpenAI connectors. Instead of specifying a `server_url`, supply a `connector_id` and an access token. The Responses API handles authentication and the hosted server exposes the connector's tools.

```python
import os

HostedMCPTool(
    tool_config={
        "type": "mcp",
        "server_label": "google_calendar",
        "connector_id": "connector_googlecalendar",
        "authorization": os.environ["GOOGLE_CALENDAR_AUTHORIZATION"],
        "require_approval": "never",
    }
)
```

Fully working hosted tool samples—including streaming, approvals, and connectors—live in [`examples/hosted_mcp`](https://github.com/openai/openai-agents-python/tree/main/examples/hosted_mcp).

## 2. Streamable HTTP MCP servers

When you want to manage the network connection yourself, use [`MCPServerStreamableHttp`][agents.mcp.server.MCPServerStreamableHttp]. Streamable HTTP servers are ideal when you control the transport or want to run the server inside your own infrastructure while keeping latency low.

```python
import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp
from agents.model_settings import ModelSettings

async def main() -> None:
    token = os.environ["MCP_SERVER_TOKEN"]
    async with MCPServerStreamableHttp(
        name="Streamable HTTP Python Server",
        params={
            "url": "http://localhost:8000/mcp",
            "headers": {"Authorization": f"Bearer {token}"},
            "timeout": 10,
        },
        cache_tools_list=True,
        max_retry_attempts=3,
    ) as server:
        agent = Agent(
            name="Assistant",
            instructions="Use the MCP tools to answer the questions.",
            mcp_servers=[server],
            model_settings=ModelSettings(tool_choice="required"),
        )

        result = await Runner.run(agent, "Add 7 and 22.")
        print(result.final_output)

asyncio.run(main())
```

The constructor accepts additional options:

- `client_session_timeout_seconds` controls MCP ClientSession read timeouts. Positive finite values representable by `datetime.timedelta` and at least one microsecond set a finite timeout; `None` and `0` disable it. Other values are rejected when the server is constructed.
- `use_structured_content` toggles whether `tool_result.structured_content` is preferred over textual output.
- `max_retry_attempts` and `retry_backoff_seconds_base` add automatic retries for `list_tools()` and `call_tool()`.
- `tool_filter` lets you expose only a subset of tools (see [Tool filtering](#tool-filtering)).
- `require_approval` enables human-in-the-loop approval policies on local MCP tools.
- `failure_error_function` customizes model-visible MCP tool failure messages; set it to `None` to raise errors instead.
- `tool_meta_resolver` injects per-call MCP `_meta` payloads before `call_tool()`.

### Approval policies for local MCP servers

`MCPServerStdio`, `MCPServerSse`, and `MCPServerStreamableHttp` all accept `require_approval`.

Supported forms:

- `"always"` or `"never"` for all tools.
- `True` requires approval for all tools, and `False` requires approval for none (equivalent to `"always"` and `"never"`, respectively).
- A per-tool map, for example `{"delete_file": "always", "read_file": "never"}`.
- A grouped object: `{"always": {"tool_names": [...]}, "never": {"tool_names": [...]}}`.

```python
async with MCPServerStreamableHttp(
    name="Filesystem MCP",
    params={"url": "http://localhost:8000/mcp"},
    require_approval={"always": {"tool_names": ["delete_file"]}},
) as server:
    ...
```

For a full pause/resume flow, see [Human-in-the-loop](human_in_the_loop.md) and `examples/mcp/get_all_mcp_tools_example/main.py`.

### Per-call metadata with `tool_meta_resolver`

Use `tool_meta_resolver` when your MCP server expects request metadata in `_meta` (for example, tenant IDs or trace context). The example below assumes you pass a `dict` as `context` to `Runner.run(...)`.

```python
from agents.mcp import MCPServerStreamableHttp, MCPToolMetaContext

def resolve_meta(context: MCPToolMetaContext) -> dict[str, str] | None:
    run_context_data = context.run_context.context or {}
    tenant_id = run_context_data.get("tenant_id")
    if tenant_id is None:
        return None
    return {"tenant_id": str(tenant_id), "source": "agents-sdk"}

server = MCPServerStreamableHttp(
    name="Metadata-aware MCP",
    params={"url": "http://localhost:8000/mcp"},
    tool_meta_resolver=resolve_meta,
)
```

If your run context is a Pydantic model, dataclass, or custom class, read the tenant ID with attribute access instead.

### MCP tool outputs: text, images, and other content

When an MCP result uses its content blocks, the SDK forwards text content as text output and maps image content to image-type entries in the tool output. For other MCP content block types, including audio and resource blocks, the SDK forwards a text output whose value is the block's valid JSON serialization. Responses that contain multiple content blocks are forwarded as a list of output items. If `use_structured_content=True` selects a non-empty, non-error `structuredContent` payload, that structured payload takes precedence over these content blocks. Missing or empty structured content falls back to the content blocks.

## 3. HTTP with SSE MCP servers

!!! warning

    The MCP project has deprecated the Server-Sent Events transport. Prefer Streamable HTTP or stdio for new integrations and keep SSE only for legacy servers.

If the MCP server implements the HTTP with SSE transport, instantiate [`MCPServerSse`][agents.mcp.server.MCPServerSse]. Apart from the transport, the API is identical to the Streamable HTTP server.

```python

from agents import Agent, Runner
from agents.model_settings import ModelSettings
from agents.mcp import MCPServerSse

workspace_id = "demo-workspace"

async with MCPServerSse(
    name="SSE Python Server",
    params={
        "url": "http://localhost:8000/sse",
        "headers": {"X-Workspace": workspace_id},
    },
    cache_tools_list=True,
) as server:
    agent = Agent(
        name="Assistant",
        mcp_servers=[server],
        model_settings=ModelSettings(tool_choice="required"),
    )
    result = await Runner.run(agent, "What's the weather in Tokyo?")
    print(result.final_output)
```

## 4. stdio MCP servers

For MCP servers that run as local subprocesses, use [`MCPServerStdio`][agents.mcp.server.MCPServerStdio]. The SDK spawns the process, keeps the pipes open, and closes them automatically when the context manager exits. This option is helpful for quick proofs of concept or when the server only exposes a command line entry point.

```python
from pathlib import Path
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

current_dir = Path(__file__).parent
samples_dir = current_dir / "sample_files"

async with MCPServerStdio(
    name="Filesystem Server via npx",
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir)],
    },
) as server:
    agent = Agent(
        name="Assistant",
        instructions="Use the files in the sample directory to answer questions.",
        mcp_servers=[server],
    )
    result = await Runner.run(agent, "List the files available to you.")
    print(result.final_output)
```

## 5. MCP server manager

When you have multiple MCP servers, use `MCPServerManager` to connect them up front and expose the successfully connected subset of those servers to your agents. See the [MCPServerManager API reference](ref/mcp/manager.md) for constructor options and reconnect behavior.

```python
from agents import Agent, Runner
from agents.mcp import MCPServerManager, MCPServerStreamableHttp

servers = [
    MCPServerStreamableHttp(name="calendar", params={"url": "http://localhost:8000/mcp"}),
    MCPServerStreamableHttp(name="docs", params={"url": "http://localhost:8001/mcp"}),
]

async with MCPServerManager(servers) as manager:
    agent = Agent(
        name="Assistant",
        instructions="Use MCP tools when they help.",
        mcp_servers=manager.active_servers,
    )
    result = await Runner.run(agent, "Which MCP tools are available?")
    print(result.final_output)
```

Key behaviors:

- `active_servers` includes only successfully connected servers when `drop_failed_servers=True` (the default).
- If the input iterable repeats the same server object, the manager owns that server once: `all_servers` and `active_servers` contain one entry, and connection and cleanup run once for that server.
- Failures are tracked in `failed_servers` and `errors`.
- Set `strict=True` to raise on the first connection failure.
- Call `reconnect(failed_only=True)` to retry failed servers, or `reconnect(failed_only=False)` to restart all servers.
- Calls to `connect_all()`, `reconnect()`, and `cleanup_all()` are serialized. If one lifecycle operation is already running, another lifecycle operation waits for it to finish instead of connecting or cleaning up the same servers concurrently.
- Set `connect_timeout_seconds`, `cleanup_timeout_seconds`, and `connect_in_parallel` to tune lifecycle behavior. Both lifecycle timeouts default to 10 seconds. They accept positive finite seconds, or `None` to disable them, and are validated both during construction and assignment; zero is rejected because it would create an immediate deadline.

## Common server capabilities

The sections below apply across MCP server transports (with the exact API surface depending on the server class).

## Tool filtering

Each MCP server supports tool filters so that you can expose only the functions that your agent needs. Filtering can happen at construction time or dynamically per run.

### Static tool filtering

Use [`create_static_tool_filter`][agents.mcp.create_static_tool_filter] to configure simple allow/block lists:

```python
from pathlib import Path

from agents.mcp import MCPServerStdio, create_static_tool_filter

samples_dir = Path("/path/to/files")

filesystem_server = MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir)],
    },
    tool_filter=create_static_tool_filter(allowed_tool_names=["read_file", "write_file"]),
)
```

When both `allowed_tool_names` and `blocked_tool_names` are supplied the SDK applies the allow-list first and then removes any blocked tools from the remaining set.

### Dynamic tool filtering

For more elaborate logic pass a callable that receives a [`ToolFilterContext`][agents.mcp.ToolFilterContext]. The callable can be synchronous or asynchronous and returns `True` when the tool should be exposed.

```python
from pathlib import Path

from agents.mcp import MCPServerStdio, ToolFilterContext

samples_dir = Path("/path/to/files")

async def context_aware_filter(context: ToolFilterContext, tool) -> bool:
    if context.agent.name == "Code Reviewer" and tool.name.startswith("danger_"):
        return False
    return True

async with MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir)],
    },
    tool_filter=context_aware_filter,
) as server:
    ...
```

The filter context exposes the active `run_context`, the `agent` requesting the tools, and the `server_name`.

## Tool guardrails

Local MCP server classes accept `tool_input_guardrails` and `tool_output_guardrails`. The SDK attaches these server-wide guardrails to every MCP tool that remains after filtering. Input guardrails can prevent the MCP server call and supply replacement content, while output guardrails inspect the converted MCP result before the SDK sends that result back to the model. These guardrails use the same function-tool execution pipeline, approval ordering, result tracking, and tripwire exceptions described in [Tool guardrails](guardrails.md#tool-guardrails).

```python
import json

from agents import ToolGuardrailFunctionOutput
from agents.decorators import tool_input_guardrail
from agents.mcp import MCPServerStdio

@tool_input_guardrail
def block_secret_arguments(data):
    arguments = json.loads(data.context.tool_arguments or "{}")
    if "secret" in arguments:
        return ToolGuardrailFunctionOutput.reject_content(
            "Remove secrets before calling this MCP tool."
        )
    return ToolGuardrailFunctionOutput.allow()

filesystem_server = MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
    },
    tool_input_guardrails=[block_secret_arguments],
)
```

This configuration applies only to tools exposed by local MCP server objects such as `MCPServerStdio`, `MCPServerSse`, and `MCPServerStreamableHttp`. It does not add client-side tool guardrails to [`HostedMCPTool`][agents.tool.HostedMCPTool], which the Responses API executes as a hosted tool.

## Prompts

MCP servers can also provide prompts that dynamically generate agent instructions. Servers that support prompts expose two
methods:

- `list_prompts()` enumerates the available prompt templates.
- `get_prompt(name, arguments)` fetches a concrete prompt, optionally with parameters.

```python
from agents import Agent

prompt_result = await server.get_prompt(
    "generate_code_review_instructions",
    {"focus": "security vulnerabilities", "language": "python"},
)
instructions = prompt_result.messages[0].content.text

agent = Agent(
    name="Code Reviewer",
    instructions=instructions,
    mcp_servers=[server],
)
```

## Pagination

The built-in local MCP server classes automatically follow `nextCursor` when listing tools and prompts. `list_tools()` collects the complete tool list before applying filters or populating its cache, and `list_prompts()` returns one combined result with `nextCursor=None`. If a later page fails or a server repeats a cursor, the operation raises an error instead of exposing or caching partial results.

Resources remain explicitly paginated. Pass the `nextCursor` from `list_resources()` or `list_resource_templates()` back as the `cursor` argument to retrieve the next page.

## Caching

Every agent run calls `list_tools()` on each MCP server. Remote servers can introduce noticeable latency, so all of the MCP server classes expose a `cache_tools_list` option. Set it to `True` only if you are confident that the tool definitions do not change frequently. To force a fresh list later, call `invalidate_tools_cache()` on the server instance.

When caching is enabled, each `list_tools()` result contains detached copies of the cached tool definitions, including nested input schemas. Dynamic tool-filter callbacks also inspect detached copies. Mutating a returned tool or a tool received by a filter therefore does not change the server's cached schema or later `list_tools()` results.

## Tracing

[Tracing](./tracing.md) automatically captures MCP activity, including:

1. Calls to the MCP server to list tools.
2. MCP-related information on tool calls.

## Further reading

- [Model Context Protocol](https://modelcontextprotocol.io/) – the specification and design guides.
- [examples/mcp](https://github.com/openai/openai-agents-python/tree/main/examples/mcp) – runnable stdio, SSE, and Streamable HTTP samples.
- [examples/hosted_mcp](https://github.com/openai/openai-agents-python/tree/main/examples/hosted_mcp) – complete hosted MCP demonstrations including approvals and connectors.

---

## multi_agent

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/multi_agent.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-multi-agent-md.md`

# Agent orchestration

Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how is the next step decided? There are two main ways to orchestrate agents:

1. Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that.
2. Orchestrating via code: determining the flow of agents via your code.

You can mix and match these patterns. Each has their own tradeoffs, described below.

## Orchestrating via LLM

An agent is an LLM equipped with instructions, tools and handoffs. This means that given an open-ended task, the LLM can autonomously plan how it will tackle the task, using tools to take actions and acquire data, and using handoffs to delegate tasks to sub-agents. For example, a research agent could be equipped with capabilities like:

-   Web search to find information online
-   File search and retrieval to search through proprietary data and connected data sources
-   Computer use to take actions on a computer
-   Code execution to do data analysis
-   Handoffs to specialized agents that are great at planning, report writing and more.

### Core SDK patterns

In the Python SDK, two orchestration patterns come up most often:

| Pattern | How it works | Best when |
| --- | --- | --- |
| Agents as tools | A manager agent keeps control of the conversation and calls specialist agents through `Agent.as_tool()`. | You want one agent to own the final answer, combine outputs from multiple specialists, or enforce shared SDK guardrails in one place. |
| Handoffs | A triage agent routes the conversation to a specialist, and that specialist becomes the active agent for the rest of the turn. | You want the specialist to respond directly, keep prompts focused, or have the handoff switch the active instructions without requiring the manager to narrate the result. |

Use **agents as tools** when a specialist should help with a bounded subtask but should not take over the user-facing conversation. Use **handoffs** when routing itself is part of the workflow and you want the chosen specialist to own the remainder of the current turn.

You can also combine the two. A triage agent might hand off to a specialist, and that specialist can still call other agents as tools for narrow subtasks.

This pattern is great when the task is open-ended and you want to rely on the intelligence of an LLM. The most important tactics here are:

1. Invest in good prompts. Make it clear what tools are available, how to use them, and what constraints the agent must follow.
2. Monitor your app and iterate on it. See where things go wrong, and iterate on your prompts.
3. Allow the agent to introspect and improve. For example, run it in a loop, and let it critique itself; or, provide error messages and let it improve.
4. Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything.
5. Invest in [evals](https://platform.openai.com/docs/guides/evals). This lets you train your agents to improve and get better at tasks.

If you want the core SDK primitives behind this style of orchestration, start with [tools](tools.md), [handoffs](handoffs.md), and [running agents](running_agents.md).

## Orchestrating via code

While orchestrating via LLM is powerful, orchestrating via code makes tasks more deterministic and predictable, in terms of speed, cost and performance. Common patterns here are:

-   Using [structured outputs](https://platform.openai.com/docs/guides/structured-outputs) to generate well formed data that you can inspect with your code. For example, you might ask an agent to classify the task into a few categories, and then pick the next agent based on the category.
-   Chaining multiple agents by transforming the output of one into the input of the next. You can decompose a task like writing a blog post into a series of steps - do research, write an outline, write the blog post, critique it, and then improve it.
-   In each iteration of a `while` loop, run the task agent to produce an output, then run an evaluator agent to assess that output and provide feedback; stop when the evaluator says the output passes the required criteria.
-   Running multiple agents in parallel, e.g. via Python primitives like `asyncio.gather`. This is useful for speed when you have multiple tasks that don't depend on each other.

We have a number of examples in [`examples/agent_patterns`](https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns).

## Related guides

-   [Agents](agents.md) for composition patterns and agent configuration.
-   [Tools](tools.md#agents-as-tools) for `Agent.as_tool()` and manager-style orchestration.
-   [Handoffs](handoffs.md) for delegation between specialist agents.
-   [Running agents](running_agents.md) for per-run orchestration controls and conversation state.
-   [Quickstart](quickstart.md) for a minimal end-to-end handoff example.

---

## quickstart

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/quickstart.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-quickstart-md.md`

# Quickstart

## Create a project and virtual environment

You'll only need to do this once.

```bash
mkdir my_project
cd my_project
python -m venv .venv
```

### Activate the virtual environment

Do this every time you start a new terminal session.

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```cmd
.venv\Scripts\activate
```

### Install the Agents SDK

```bash
pip install openai-agents # or `uv add openai-agents`, etc
```

### Set an OpenAI API key

If you don't have one, follow [these instructions](https://platform.openai.com/docs/quickstart#create-and-export-an-api-key) to create an OpenAI API key.

These commands set the key for your current terminal session.

On macOS or Linux:

```bash
export OPENAI_API_KEY=sk-...
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY = "sk-..."
```

On Windows Command Prompt:

```cmd
set "OPENAI_API_KEY=sk-..."
```

## Create your first agent

Agents are defined with instructions, a name, and optional configuration such as a specific model.

```python
from agents import Agent

agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
)
```

## Run your first agent

Use [`Runner`][agents.run.Runner] to execute the agent and get a [`RunResult`][agents.result.RunResult] back.

```python
import asyncio
from agents import Agent, Runner

agent = Agent(
    name="History Tutor",
    instructions="You answer history questions clearly and concisely.",
)

async def main():
    result = await Runner.run(agent, "When did the Roman Empire fall?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

For a second turn, you can either pass `result.to_input_list()` back into `Runner.run(...)`, attach a [session](sessions/index.md), or reuse OpenAI server-managed state with `conversation_id` / `previous_response_id`. The [running agents](running_agents.md) guide compares these approaches.

Use this rule of thumb:

| If you want... | Start with... |
| --- | --- |
| Full manual control and provider-agnostic history | `result.to_input_list()` |
| The SDK to load and save history for you | [`session=...`](sessions/index.md) |
| OpenAI-managed server-side continuation | `previous_response_id` or `conversation_id` |

For the tradeoffs and exact behaviors, see [Running agents](running_agents.md#choose-a-memory-strategy).

Use a plain `Agent` plus `Runner` when the task mainly lives in prompts, tools, and conversation state. If the agent should inspect or modify real files in an isolated workspace, jump to the [Sandbox agents quickstart](sandbox_agents.md).

## Give your agent tools

You can give an agent tools to look up information or perform actions.

```python
import asyncio
from agents import Agent, Runner
from agents.decorators import tool

@tool
def history_fun_fact() -> str:
    """Return a short history fact."""
    return "Sharks are older than trees."

agent = Agent(
    name="History Tutor",
    instructions="Answer history questions clearly. Use history_fun_fact when it helps.",
    tools=[history_fun_fact],
)

async def main():
    result = await Runner.run(
        agent,
        "Tell me something surprising about ancient life on Earth.",
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

## Add a few more agents

Before you choose a multi-agent pattern, decide who should own the final answer:

-   **Handoffs**: a specialist takes over the conversation for that part of the turn.
-   **Agents as tools**: an orchestrator stays in control and calls specialists as tools.

This quickstart continues with **handoffs** because it is the shortest first example. For the manager-style pattern, see [Agent orchestration](multi_agent.md) and [Tools: agents as tools](tools.md#agents-as-tools).

Additional agents can be defined in the same way. `handoff_description` gives the routing agent extra context about when to delegate.

```python
from agents import Agent

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You answer history questions clearly and concisely.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You explain math step by step and include worked examples.",
)
```

## Define your handoffs

On an agent, you can define an inventory of outgoing handoff options that it can choose from while solving the task.

```python
triage_agent = Agent(
    name="Triage Agent",
    instructions="Route each homework question to the right specialist.",
    handoffs=[history_tutor_agent, math_tutor_agent],
)
```

## Run the agent orchestration

The runner handles executing individual agents, any handoffs, and any tool calls.

```python
import asyncio
from agents import Runner

async def main():
    result = await Runner.run(
        triage_agent,
        "Who was the first president of the United States?",
    )
    print(result.final_output)
    print(f"Answered by: {result.last_agent.name}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Reference examples

The repository includes full scripts for the same core patterns:

-   [`examples/basic/hello_world.py`](https://github.com/openai/openai-agents-python/tree/main/examples/basic/hello_world.py) for the first run.
-   [`examples/basic/tools.py`](https://github.com/openai/openai-agents-python/tree/main/examples/basic/tools.py) for function tools.
-   [`examples/agent_patterns/routing.py`](https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns/routing.py) for multi-agent routing.

## View your traces

To review what happened during your agent run, navigate to the [Trace viewer in the OpenAI Dashboard](https://platform.openai.com/traces) to view traces of your agent runs.

## Next steps

Learn how to build more complex agentic flows:

-   Learn about how to configure [Agents](agents.md).
-   Learn about [running agents](running_agents.md) and [sessions](sessions/index.md).
-   Learn about [Sandbox agents](sandbox_agents.md) if the work should happen inside a real workspace.
-   Learn about [tools](tools.md), [guardrails](guardrails.md) and [models](models/index.md).

---

## results

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/results.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-results-md.md`

# Results

When you call the `Runner.run` methods, you receive one of two result types:

-   [`RunResult`][agents.result.RunResult] from `Runner.run(...)` or `Runner.run_sync(...)`
-   [`RunResultStreaming`][agents.result.RunResultStreaming] from `Runner.run_streamed(...)`

Both inherit from [`RunResultBase`][agents.result.RunResultBase], which exposes the shared result surfaces such as `final_output`, `new_items`, `last_agent`, `raw_responses`, and `to_state()`.

`RunResultStreaming` adds streaming-specific controls such as [`stream_events()`][agents.result.RunResultStreaming.stream_events], [`current_agent`][agents.result.RunResultStreaming.current_agent], [`is_complete`][agents.result.RunResultStreaming.is_complete], and [`cancel(...)`][agents.result.RunResultStreaming.cancel].

## Choose the right result surface

Most applications only need a few result properties or helpers:

| If you need... | Use |
| --- | --- |
| The final answer to show the user | `final_output` |
| A replay-ready next-turn input list with the full local transcript | `to_input_list()` |
| Rich run items with agent, tool, handoff, and approval metadata | `new_items` |
| The agent that should usually handle the next user turn | `last_agent` |
| OpenAI Responses API chaining with `previous_response_id` | `last_response_id` |
| Pending approvals and a resumable snapshot | `interruptions` and `to_state()` |
| Metadata about the current nested `Agent.as_tool()` invocation | `agent_tool_invocation` |
| Raw model calls or guardrail diagnostics | `raw_responses` and the guardrail result arrays |

## Final output

The [`final_output`][agents.result.RunResultBase.final_output] property contains the final output of the last agent that ran. This is either:

-   a `str`, if the last agent did not have an `output_type` defined
-   an object of type `last_agent.output_type`, if the last agent had an output type defined
-   `None`, if the run stopped before a final output was produced, for example because it paused on an approval interruption

!!! note

    `final_output` is typed as `Any`. Handoffs can change which agent finishes the run, so the SDK cannot statically know the full set of possible output types.

In streaming mode, `final_output` stays `None` until the stream has finished processing. See [Streaming](streaming.md) for the event-by-event flow.

## Input, next-turn history, and new items

These surfaces answer different questions:

| Property or helper | What it contains | Best for |
| --- | --- | --- |
| [`input`][agents.result.RunResultBase.input] | The base input for this run segment. If a handoff input filter rewrote the history, this reflects the filtered input the run continued with. | Auditing what this run actually used as input |
| [`to_input_list()`][agents.result.RunResultBase.to_input_list] | An input-item view of the run. The default `mode="preserve_all"` keeps the converted history from `new_items`, except it does not append an exact session item occurrence already moved into SDK-default nested handoff history a second time; `mode="normalized"` prefers canonical continuation input when handoff filtering rewrites model history. | Manual chat loops, client-managed conversation state, and plain-item history inspection |
| [`new_items`][agents.result.RunResultBase.new_items] | Rich [`RunItem`][agents.items.RunItem] wrappers with agent, tool, handoff, and approval metadata. | Logs, UIs, audits, and debugging |
| [`raw_responses`][agents.result.RunResultBase.raw_responses] | Raw [`ModelResponse`][agents.items.ModelResponse] objects from each model call in the run. | Provider-level diagnostics or raw response inspection |

In practice:

-   Use `to_input_list()` when you want a plain input-item view of the run.
-   Use `to_input_list(mode="normalized")` when you want the canonical local input for the next `Runner.run(..., input=...)` call after handoff filtering or nested handoff history rewrites.
-   Use [`session=...`](sessions/index.md) when you want the SDK to load and save history for you.
-   If you are using OpenAI server-managed state with `conversation_id` or `previous_response_id`, usually pass only the new user input and reuse the stored ID instead of resending `to_input_list()`.
-   Use the default `to_input_list()` mode or `new_items` when you need the full converted history for logs, UIs, or audits.

When SDK-default nested handoff history preserves a message item verbatim, Sessions, `RunState`, and `to_input_list()` track the exact owned occurrence rather than deduplicating by content. Identical messages that occurred separately remain separate; only the already-owned occurrence is kept from being appended a second time.

When model output is converted into replayable input, `to_input_list()`, [`ModelResponse.to_input_items()`][agents.items.ModelResponse.to_input_items], and each [`RunItemBase.to_input_item()`][agents.items.RunItemBase.to_input_item] call remove provider output-only `created_by` metadata. This includes `created_by` on nested `shell_call_output` chunks. The conversion rebuilds the affected mappings and does not mutate the original raw item.

Unlike the JavaScript SDK, Python does not expose a separate `output` property containing only the model-format items newly generated during the run. Use `new_items` when you need SDK metadata, or inspect `raw_responses` when you need the raw model payloads.

Resubmitting computer-tool items as conversation input uses the raw Responses payload shape. Preview-model `computer_call` items preserve a single `action`, while `gpt-5.5` computer calls can preserve batched `actions[]`. [`to_input_list()`][agents.result.RunResultBase.to_input_list] and [`RunState`][agents.run_state.RunState] keep whichever shape the model produced, so manually resubmitting those items as conversation input, pause/resume flows, and stored transcripts continue to work across both preview and GA computer-tool calls. Local execution results still appear as `computer_call_output` items in `new_items`.

### New items

[`new_items`][agents.result.RunResultBase.new_items] gives you the richest view of what happened during the run. Common item types are:

-   [`InputItem`][agents.items.InputItem] for input admitted from `RunState.pending_input` immediately before a resumed model call
-   [`MessageOutputItem`][agents.items.MessageOutputItem] for assistant messages
-   [`ReasoningItem`][agents.items.ReasoningItem] for reasoning items
-   [`ToolSearchCallItem`][agents.items.ToolSearchCallItem] and [`ToolSearchOutputItem`][agents.items.ToolSearchOutputItem] for Responses tool search requests and loaded tool-search results
-   [`ToolCallItem`][agents.items.ToolCallItem] and [`ToolCallOutputItem`][agents.items.ToolCallOutputItem] for tool calls and their results
-   [`ToolApprovalItem`][agents.items.ToolApprovalItem] for tool calls that paused for approval
-   [`MCPApprovalRequestItem`][agents.items.MCPApprovalRequestItem], [`MCPApprovalResponseItem`][agents.items.MCPApprovalResponseItem], and [`MCPListToolsItem`][agents.items.MCPListToolsItem] for hosted MCP approvals and tool catalogs
-   [`HandoffCallItem`][agents.items.HandoffCallItem] and [`HandoffOutputItem`][agents.items.HandoffOutputItem] for handoff requests and completed transfers

Choose `new_items` over `to_input_list()` whenever you need agent associations, tool outputs, handoff boundaries, or approval boundaries.

When you use hosted tool search, inspect `ToolSearchCallItem.raw_item` to see the search request the model emitted, and `ToolSearchOutputItem.raw_item` to see which namespaces, functions, or hosted MCP servers were loaded for that turn.

With Programmatic Tool Calling, the generated `program` is a `ToolCallItem`, ordinary child tool calls owned by that program are also `ToolCallItem` entries, and the matching `program_output` is a `ToolCallOutputItem`. Program-owned hosted MCP `mcp_approval_request` and `mcp_list_tools` items are exceptions: they become `MCPApprovalRequestItem` and `MCPListToolsItem` entries.

Raw items can be typed Responses objects or mappings. In particular, program-owned shell and apply-patch calls use mappings. Use a mapping-safe inspection pattern:

```python
from collections.abc import Mapping

def raw_field(item, name):
    raw_item = item.raw_item
    if isinstance(raw_item, Mapping):
        return raw_item.get(name)
    return getattr(raw_item, name, None)

raw_type = raw_field(item, "type")
caller = raw_field(item, "caller")
caller_id = (
    caller.get("caller_id")
    if isinstance(caller, Mapping)
    else getattr(caller, "caller_id", None)
)
```

For a program-owned child call, the `type` field of `caller` is `program`, and `caller_id` identifies the parent program call.

## Continue or resume the conversation

### Next-turn agent

[`last_agent`][agents.result.RunResultBase.last_agent] contains the last agent that ran. This is often the best agent to reuse for the next user turn after handoffs.

In streaming mode, [`RunResultStreaming.current_agent`][agents.result.RunResultStreaming.current_agent] updates as the run progresses, so you can observe handoffs before the stream finishes.

### Interruptions and run state

If a tool needs approval, pending approvals are exposed in [`RunResult.interruptions`][agents.result.RunResult.interruptions] or [`RunResultStreaming.interruptions`][agents.result.RunResultStreaming.interruptions]. This can include approvals raised by direct tools, by tools reached after a handoff, or by nested [`Agent.as_tool()`][agents.agent.Agent.as_tool] runs.

Call [`to_state()`][agents.result.RunResult.to_state] to capture a resumable [`RunState`][agents.run_state.RunState], approve or reject the pending items, and then resume with `Runner.run(...)` or `Runner.run_streamed(...)`.

When a [`ToolCallOutputItem`][agents.items.ToolCallOutputItem] output is a Pydantic model or dataclass, `RunState` serializes that output as structured data. `RunState` also traverses dictionaries, lists, and tuples and converts Pydantic models or dataclasses that it encounters in those containers; tuples are restored as lists after a JSON round trip. Other non-JSON-compatible values can fall back to their string representation, so return explicitly JSON-compatible data when an exact custom type must survive serialization.

```python
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="Use tools when needed.")
result = await Runner.run(agent, "Delete temp files that are no longer needed.")

if result.interruptions:
    state = result.to_state()
    for interruption in result.interruptions:
        state.approve(interruption)
    result = await Runner.run(agent, state)
```

#### Recover a failed resumed Session write

A resumed run can complete approved tool work that still leads to another model call, including a handoff in the same model response, and then fail while writing the completed tool calls and outputs to a client-managed [`Session`][agents.memory.session.Session]. Keep the same [`RunState`][agents.run_state.RunState], or serialize and restore it, and retry `Runner.run(...)` or `Runner.run_streamed(...)` with the original Session backend and `session_id`. Before any later model call, the SDK reconciles the pending batch with the Session history. If the Session committed the complete batch but its acknowledgment failed, the SDK recognizes the exact history tail and does not append the batch again. If the write did not commit, the SDK retries the append. The SDK does not execute completed tools, tool guardrails, hooks, or handoffs again. The resumed run continues with the agent selected by the completed handoff.

Recovery fails closed when the Session history is not an exact match. Use the original Session backend and `session_id`, and give the resumed run exclusive access to that history. If another writer changes the history tail, only part of the pending batch is present, or the history is otherwise ambiguous, the SDK raises [`UserError`][agents.exceptions.UserError] before another model call. Repair the original Session history before resuming; do not rerun the completed work. The pending batch, selected agent, and accumulated tool guardrail results survive `RunState` JSON and string round trips, including a later approval interruption before recovery finishes. After [`stream_events()`][agents.result.RunResultStreaming.stream_events] raises the Session write error, [`RunResultStreaming.to_state()`][agents.result.RunResultStreaming.to_state] also returns a detached state that retains the same recovery data.

This recovery does not apply after the run has accepted a final output, completed its output guardrails and terminal hooks, and then failed to persist that final turn. Replaying that state could repeat terminal lifecycle effects, so the SDK marks the `RunState` as unrecoverable. Every later `Runner.run(...)` or `Runner.run_streamed(...)` attempt with that state raises [`UserError`][agents.exceptions.UserError] before Session reconciliation, sandbox preparation, model calls, tools, guardrails, or hooks. The marker survives `RunState` serialization. Start a new run instead of retrying that state. This boundary also applies to a terminal function-tool output and to a `max_turns` handler output that was accepted for history.

#### Add input before resuming

Use [`RunState.add_input()`][agents.run_state.RunState.add_input] when new user input arrives after a run pauses or stops after a completed turn, but before the unfinished run reaches its next model call. A string becomes a user message, and multiple calls preserve insertion order. The staged input is part of serialized `RunState`, so it survives `to_json()` / `from_json()` and `to_string()` / `from_string()` round trips.

```python
state = result.to_state()
state.add_input("Also keep the generated report in the project folder.")

for interruption in state.get_interruptions():
    state.approve(interruption)

result = await Runner.run(agent, state)
```

On resume, the runner applies both the current agent's input guardrails and the input guardrails from [`RunConfig`][agents.run.RunConfig] only to the staged input. When a client-managed [`Session`][agents.memory.session.Session] is configured, the runner converts the accepted staged input into a durable [`InputItem`][agents.items.InputItem] and awaits the session write before issuing the model request. Without a client-managed session or server-managed conversation, the runner converts the accepted staged input into an `InputItem` before issuing the model request. For a server-managed conversation, the input remains pending until the server request accepts it. Across serialization, resume, and replay-safe retries, the SDK preserves one durable `InputItem` occurrence. This SDK occurrence guarantee is not a provider-delivery guarantee: if a retry policy returns `RetryDecision(approve_unsafe_replay=True)` after a request may have reached the provider, the runner can resend the staged input and provider-side work can repeat. Successfully admitted input appears in `new_items` as an `InputItem`. Read [`RunState.pending_input`][agents.run_state.RunState.pending_input] for a detached copy, or call [`RunState.clear_pending_input()`][agents.run_state.RunState.clear_pending_input] to discard all staged input before resuming.

`RunState.add_input()` rejects a terminal state, a state with no remaining model turns, a state in which an accepted model response is awaiting local processing, and an interrupted state whose pending tool result may end the run before another model call. In those cases, finish the current run and start a new user turn instead.

For streaming runs, finish consuming [`stream_events()`][agents.result.RunResultStreaming.stream_events] first, then inspect `result.interruptions` and resume from `result.to_state()`. For the full approval flow, see [Human-in-the-loop](human_in_the_loop.md).

### Server-managed continuation

[`last_response_id`][agents.result.RunResultBase.last_response_id] is the latest model response ID from the run. Pass it back as `previous_response_id` on the next turn when you want to continue an OpenAI Responses API chain.

If you already continue the conversation with `to_input_list()`, `session`, or `conversation_id`, you usually do not need `last_response_id`. If you need every model response from a multi-step run, inspect `raw_responses` instead.

## Agent-as-tool metadata

When a result comes from a nested [`Agent.as_tool()`][agents.agent.Agent.as_tool] run, [`agent_tool_invocation`][agents.result.RunResultBase.agent_tool_invocation] exposes immutable metadata about the enclosing `Agent.as_tool()` call:

-   `tool_name`
-   `tool_call_id`
-   `tool_arguments`

For ordinary top-level runs, `agent_tool_invocation` is `None`.

This is especially useful inside `custom_output_extractor`, where you may need the enclosing `Agent.as_tool()` call's tool name, call ID, or raw arguments while post-processing the nested result. See [Tools](tools.md) for the surrounding `Agent.as_tool()` patterns.

If you also need the parsed structured input for that nested run, read `context_wrapper.tool_input`. That is the field [`RunState`][agents.run_state.RunState] serializes generically for nested tool input, while `agent_tool_invocation` exposes metadata for the current nested invocation directly on the result.

## Streaming lifecycle and diagnostics

[`RunResultStreaming`][agents.result.RunResultStreaming] inherits the same result surfaces above, but adds streaming-specific controls:

-   [`stream_events()`][agents.result.RunResultStreaming.stream_events] to consume semantic stream events
-   [`current_agent`][agents.result.RunResultStreaming.current_agent] to track the active agent mid-run
-   [`is_complete`][agents.result.RunResultStreaming.is_complete] to see whether the streamed run has fully finished
-   [`cancel(...)`][agents.result.RunResultStreaming.cancel] to stop the run immediately or after the current turn

Keep consuming `stream_events()` until the async iterator finishes. A streaming run is not complete until that iterator ends, and summary properties such as `final_output`, `interruptions`, `raw_responses`, and session-persistence side effects may still be settling after the last visible token arrives.

If you call `cancel()`, continue consuming `stream_events()` so cancellation and cleanup can finish correctly.

Python does not expose a separate streamed `completed` promise or `error` property. Streaming failures that terminate the run are raised by `stream_events()`, and `is_complete` reflects whether the run has reached its terminal state.

### Raw responses

[`raw_responses`][agents.result.RunResultBase.raw_responses] contains the raw model responses collected during the run. Multi-step runs can produce more than one response, for example across handoffs or repeated model/tool/model cycles.

[`last_response_id`][agents.result.RunResultBase.last_response_id] is just the ID from the last entry in `raw_responses`.

Each [`ModelResponse`][agents.items.ModelResponse] also exposes two diagnostics that apply to that individual model call:

-   [`request_id`][agents.items.ModelResponse.request_id] is the transport request ID when the model adapter and transport propagate one. The built-in `OpenAIResponsesModel` and `OpenAIChatCompletionsModel` propagate an available server-generated `x-request-id` on their HTTP and SSE transport paths. When the configured endpoint is the OpenAI API, log a non-`None` value in production so you can correlate failures with OpenAI support; for an OpenAI-compatible provider or proxy, use that service's support channel instead. `OpenAIResponsesWSModel` currently leaves `request_id` as `None`. Third-party adapters do not guarantee request ID propagation. The AnyLLM Chat Completions adapter and `LitellmModel` currently leave `request_id` as `None`. The Agents SDK AnyLLM Responses adapter may also leave `request_id` as `None` when it normalizes a provider response without preserving the transport request ID.
-   [`raw_usage`][agents.items.ModelResponse.raw_usage] is an opt-in, JSON-compatible snapshot of the provider's usage payload before the Agents SDK normalizes the payload. Enable `raw_usage` with `ModelSettings(preserve_raw_usage=True)`; see [Preserving provider usage payloads](usage.md#preserving-provider-usage-payloads).

`ModelResponse.request_id` and `ModelResponse.raw_usage` can each be `None`, so handle these values as optional diagnostics rather than conversation state.

### Guardrail results

Agent-level guardrails are exposed as [`input_guardrail_results`][agents.result.RunResultBase.input_guardrail_results] and [`output_guardrail_results`][agents.result.RunResultBase.output_guardrail_results].

Tool guardrails are exposed separately as [`tool_input_guardrail_results`][agents.result.RunResultBase.tool_input_guardrail_results] and [`tool_output_guardrail_results`][agents.result.RunResultBase.tool_output_guardrail_results].

These arrays accumulate across the run, so they are useful for logging decisions, storing extra guardrail metadata, or debugging why a run was blocked.

One redaction rule applies when an agent-level output guardrail blocks final output produced directly by a terminal function tool. For the blocked current response, `output_guardrail_results` replaces the rejected agent output and clears payload-bearing output metadata, while `tool_output_guardrail_results` replaces payload-bearing tool metadata. Earlier accepted results remain unchanged. The sanitized output-guardrail result is exposed as `guardrail_result` on [`OutputGuardrailTripwireTriggered`][agents.exceptions.OutputGuardrailTripwireTriggered]. Sanitized output-guardrail and tool-output-guardrail results are also exposed through streamed result state and `RunState`; see [Output guardrails](guardrails.md#output-guardrails).

### Context and usage

[`context_wrapper`][agents.result.RunResultBase.context_wrapper] exposes your app context together with SDK-managed runtime metadata such as approvals, usage, and nested `tool_input`.

Usage is tracked on `context_wrapper.usage`. For streamed runs, the usage totals can lag until the stream's final chunks have been processed. See [Context management](context.md) for the full wrapper shape and persistence caveats.

---

## running_agents

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/running_agents.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-running-agents-md.md`

# Running agents

You can run agents via the [`Runner`][agents.run.Runner] class. You have 3 options:

1. [`Runner.run()`][agents.run.Runner.run], which runs async and returns a [`RunResult`][agents.result.RunResult].
2. [`Runner.run_sync()`][agents.run.Runner.run_sync], which is a sync method and just runs `.run()` under the hood.
3. [`Runner.run_streamed()`][agents.run.Runner.run_streamed], which runs async and returns a [`RunResultStreaming`][agents.result.RunResultStreaming]. It calls the LLM in streaming mode, and streams those events to you as they are received.

```python
from agents import Agent, Runner

async def main():
    agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = await Runner.run(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)
    # Code within the code,
    # Functions calling themselves,
    # Infinite loop's dance
```

Read more in the [results guide](results.md).

## Runner lifecycle and configuration

### The agent loop

When you call any of the three `Runner` methods above, you pass in a starting agent and input. The input can be:

-   a string (treated as a user message),
-   a list of input items in the OpenAI Responses API format, or
-   a [`RunState`][agents.run_state.RunState] when resuming a paused run or a run stopped with `cancel(mode="after_turn")`. The state can also carry [input staged for the next resumed model call](results.md#add-input-before-resuming).

The runner then runs a loop:

1. We call the LLM for the current agent, with the current input.
2. The LLM produces its output.
    1. If the runner classifies the LLM's output as final output, the loop ends and we return the result.
    2. If the LLM requests a handoff, we update the current agent and input, and re-run the loop.
    3. If the LLM produces tool calls, we run those tool calls, append the results, and re-run the loop.
3. If we exceed the `max_turns` passed, we raise a [`MaxTurnsExceeded`][agents.exceptions.MaxTurnsExceeded] exception. Pass `max_turns=None` to disable this turn limit.

!!! note

    The rule for whether the LLM output is considered as a "final output" is that it produces text output with the desired type, and there are no tool calls.

### Streaming

Streaming allows you to additionally receive streaming events as the LLM runs. Once the stream is done, the [`RunResultStreaming`][agents.result.RunResultStreaming] will contain the complete information about the run, including all the new outputs produced. You can call `.stream_events()` for the streaming events. Read more in the [streaming guide](streaming.md).

#### Responses WebSocket transport (optional helper)

If you enable the OpenAI Responses websocket transport, you can keep using the normal `Runner` APIs. The websocket session helper is recommended for connection reuse, but it is not required.

This is the Responses API over websocket transport, not the [Realtime API](realtime/guide.md).

For transport-selection rules and caveats around concrete model objects or custom providers, see [Models](models/index.md#responses-websocket-transport).

##### Pattern 1: No session helper (works)

Use this when you just want websocket transport and do not need the SDK to manage a shared provider/session for you.

```python
import asyncio

from agents import Agent, Runner, set_default_openai_responses_transport

async def main():
    set_default_openai_responses_transport("websocket")

    agent = Agent(name="Assistant", instructions="Be concise.")
    result = Runner.run_streamed(agent, "Summarize recursion in one sentence.")

    async for event in result.stream_events():
        if event.type == "raw_response_event":
            continue
        print(event.type)

asyncio.run(main())
```

This pattern is fine for single runs. If you call `Runner.run()` / `Runner.run_streamed()` repeatedly, each run may reconnect unless you manually reuse the same `RunConfig` / provider instance.

The Runner owns the model provider only when `run_config` is omitted or when a `dict`-based config omits `model_provider`. The Runner closes that implicitly created provider after a non-streaming run returns or after a streamed run settles, including error and cancellation paths. If you pass a `RunConfig` instance or a `dict` that contains `model_provider`, your application owns that provider; the Runner leaves it open so you can reuse it, and your application must eventually call its `aclose()` method.

##### Pattern 2: Use `responses_websocket_session()` (recommended for multi-turn reuse)

Use [`responses_websocket_session()`][agents.responses_websocket_session] when you want a shared websocket-capable provider and `RunConfig` across multiple runs (including nested agent-as-tool calls that inherit the same `run_config`).

```python
import asyncio

from agents import Agent, responses_websocket_session

async def main():
    agent = Agent(name="Assistant", instructions="Be concise.")

    async with responses_websocket_session(
        responses_websocket_options={"ping_interval": 20.0, "ping_timeout": 60.0},
    ) as ws:
        first = ws.run_streamed(agent, "Say hello in one short sentence.")
        async for _event in first.stream_events():
            pass

        second = ws.run_streamed(
            agent,
            "Now say goodbye.",
            previous_response_id=first.last_response_id,
        )
        async for _event in second.stream_events():
            pass

asyncio.run(main())
```

Finish consuming streamed results before the context exits. Exiting the context while a websocket request is still in flight may force-close the shared connection.

The service processes one response at a time on each websocket connection and limits a connection to 60 minutes. The helper reuses the connection but does not remove those constraints. After a reconnect, `store=False` and ZDR flows cannot recover an uncached `previous_response_id`; start a new chain with full input context or rebuild it from locally managed session state. See the [Responses WebSocket transport notes](models/index.md#responses-websocket-transport) for the full recovery behavior.

If long reasoning turns hit websocket keepalive timeouts, increase `ping_timeout` or set `ping_timeout=None` to disable heartbeat timeouts. Use HTTP/SSE transport for runs where reliability matters more than websocket latency.

### Run config

The `run_config` parameter lets you configure some global settings for the agent run:

#### Common run config categories

Use `RunConfig` to override behavior for a single run without changing each agent definition.

##### Model, provider, and session defaults

-   [`model`][agents.run.RunConfig.model]: Allows setting a global LLM model to use, irrespective of what `model` each Agent has.
-   [`model_provider`][agents.run.RunConfig.model_provider]: A model provider for looking up model names, which defaults to OpenAI.
-   [`model_settings`][agents.run.RunConfig.model_settings]: Overrides agent-specific settings. For example, you can set a global `temperature` or `top_p`.
-   [`session_settings`][agents.run.RunConfig.session_settings]: Overrides session-level defaults (for example, `SessionSettings(limit=...)`) when retrieving history during a run.
-   [`session_input_callback`][agents.run.RunConfig.session_input_callback]: Customize how new user input is merged with session history before each `Runner` run when using Sessions. The callback can be sync or async.

##### Guardrails, handoffs, and model input shaping

-   [`input_guardrails`][agents.run.RunConfig.input_guardrails], [`output_guardrails`][agents.run.RunConfig.output_guardrails]: A list of input or output guardrails to include on all runs.
-   [`handoff_input_filter`][agents.run.RunConfig.handoff_input_filter]: A global input filter to apply to all handoffs, if the handoff doesn't already have one. The input filter allows you to edit the inputs that are sent to the new agent. See the documentation in [`Handoff.input_filter`][agents.handoffs.Handoff.input_filter] for more details.
-   [`nest_handoff_history`][agents.run.RunConfig.nest_handoff_history]: Opt-in beta that compacts summarizable history into ordered assistant summary segments while preserving lossless message items in their original positions before invoking the next agent. This is disabled by default while we stabilize nested handoffs; set to `True` to enable or leave `False` to pass through the raw transcript. Sessions, `RunState`, and `RunResult.to_input_list()` avoid appending an exact message occurrence twice when the SDK-default nested history already owns it, while preserving separate identical messages. All [Runner methods][agents.run.Runner] automatically create a `RunConfig` when you do not pass one, so the quickstarts and examples keep the default off, and any explicit [`Handoff.input_filter`][agents.handoffs.Handoff.input_filter] callbacks continue to override it. Individual handoffs can override this setting via [`Handoff.nest_handoff_history`][agents.handoffs.Handoff.nest_handoff_history].
-   [`handoff_history_mapper`][agents.run.RunConfig.handoff_history_mapper]: Optional callable that receives the normalized transcript (history + handoff items) whenever you opt in to `nest_handoff_history`. It must return the exact list of input items to forward to the next agent, replacing the built-in ordered summary segments without writing a full handoff filter.
-   [`call_model_input_filter`][agents.run.RunConfig.call_model_input_filter]: Hook to edit the fully prepared model input (instructions and input items) immediately before the model call, e.g., to trim history or inject a system prompt.
-   [`reasoning_item_id_policy`][agents.run.RunConfig.reasoning_item_id_policy]: Control whether reasoning item IDs are preserved or omitted when the runner converts prior outputs into next-turn model input.

##### Tracing and observability

-   [`tracing_disabled`][agents.run.RunConfig.tracing_disabled]: Allows you to disable [tracing](tracing.md) for the entire run.
-   [`tracing`][agents.run.RunConfig.tracing]: Pass a [`TracingConfig`][agents.tracing.TracingConfig] to override trace export settings such as the per-run tracing API key.
-   [`trace_include_sensitive_data`][agents.run.RunConfig.trace_include_sensitive_data]: Configures whether traces will include potentially sensitive data, such as LLM and tool call inputs/outputs.
-   [`workflow_name`][agents.run.RunConfig.workflow_name], [`trace_id`][agents.run.RunConfig.trace_id], [`group_id`][agents.run.RunConfig.group_id]: Sets the tracing workflow name, trace ID and trace group ID for the run. We recommend at least setting `workflow_name`. The group ID is an optional field that lets you link traces across multiple runs.
-   [`trace_metadata`][agents.run.RunConfig.trace_metadata]: Metadata to include on all traces.

##### Tool execution, approval, and tool error behavior

-   [`tool_execution`][agents.run.RunConfig.tool_execution]: Configure SDK-side execution behavior for local tool calls, such as limiting how many local function tool calls run at once.
-   [`tool_not_found_behavior`][agents.run.RunConfig.tool_not_found_behavior]: Configure how the runner handles model-emitted function tool calls whose tool name does not match any function tool available to the current agent. The default raises `ModelBehaviorError`; opt in to return a model-visible error output instead.
-   [`tool_name_collision_policy`][agents.run.RunConfig.tool_name_collision_policy]: Configure how the runner handles unnamespaced function-tool and handoff names that collide. The default, `"warn"`, logs an actionable warning and exposes only the current dispatch winner; `"error"` raises `UserError` before the model is called. Strict validation for namespaced and deferred-loading tools is unchanged.
-   [`tool_error_formatter`][agents.run.RunConfig.tool_error_formatter]: Customize model-visible tool error messages, such as approval rejections and opt-in tool-not-found outputs.

Nested handoffs are available as an opt-in beta. Enable ordered transcript compaction by passing `RunConfig(nest_handoff_history=True)` or set `handoff(..., nest_handoff_history=True)` to turn it on for a specific handoff. The built-in mapper places generated assistant summary segments around lossless message items instead of collapsing the whole transcript into one message. If you prefer to keep the raw transcript (the default), leave the flag unset or provide a `handoff_input_filter` (or `handoff_history_mapper`) that forwards the conversation exactly as you need. To change the wrapper text used in generated summary segments without writing a custom mapper, call [`set_conversation_history_wrappers`][agents.handoffs.set_conversation_history_wrappers] (and [`reset_conversation_history_wrappers`][agents.handoffs.reset_conversation_history_wrappers] to restore the defaults).

#### Run config details

##### `tool_execution`

Use `tool_execution` when you want to configure SDK-side behavior for local function tools, such as limiting local function-tool concurrency for a run.

```python
from agents import Agent, RunConfig, Runner, ToolExecutionConfig

agent = Agent(name="Assistant", tools=[...])

result = await Runner.run(
    agent,
    "Run the required tool calls.",
    run_config=RunConfig(
        tool_execution=ToolExecutionConfig(
            max_function_tool_concurrency=2,
            pre_approval_tool_input_guardrails=True,
        ),
    ),
)
```

`max_function_tool_concurrency=None` preserves the default behavior: when a model emits multiple function tool calls in a turn, the SDK starts all emitted local function tool calls. Set an integer value to cap how many of those local function tool calls run at once.

This is separate from provider-side [`ModelSettings.parallel_tool_calls`][agents.model_settings.ModelSettings.parallel_tool_calls]. `parallel_tool_calls` controls whether the model is allowed to emit multiple tool calls in a single response. `tool_execution.max_function_tool_concurrency` controls how the SDK executes local function tool calls after the model has emitted them.

`pre_approval_tool_input_guardrails=False` preserves the default approval flow: if a function tool needs approval, the run pauses first and the tool input guardrails run only after approval, immediately before execution. Set it to `True` when you want function-tool input guardrails to run before the pending approval interruption is emitted. Calls that pass this pre-approval check still run the same input guardrails again after approval, so time-sensitive checks are revalidated before execution.

##### `tool_not_found_behavior`

By default, if the model emits a function tool call that does not match any function tool available to the current agent, the runner raises `ModelBehaviorError`.

Set `tool_not_found_behavior="return_error_to_model"` when you want the run to remain recoverable. In that mode, the SDK appends a `function_call_output` for the unresolved tool call and runs the model again, so the model can choose an available tool or answer without using that tool.

```python
from agents import Agent, RunConfig, Runner

agent = Agent(name="Assistant", tools=[...])

result = await Runner.run(
    agent,
    "Handle this request with the available tools.",
    run_config=RunConfig(tool_not_found_behavior="return_error_to_model"),
)
```

This option currently applies only to function tool calls that fail tool-name lookup. Other invalid tool payloads continue to use their existing error behavior.

##### `tool_error_formatter`

Use `tool_error_formatter` to customize the message that is returned to the model when the SDK creates a model-visible tool error output.

The formatter receives [`ToolErrorFormatterArgs`][agents.run_config.ToolErrorFormatterArgs] with:

-   `kind`: The error category, such as `"approval_rejected"` or `"tool_not_found"`.
-   `tool_type`: The tool runtime (`"function"`, `"computer"`, `"shell"`, `"apply_patch"`, or `"custom"`).
-   `tool_name`: The tool name.
-   `call_id`: The tool call ID.
-   `default_message`: The SDK's default model-visible message.
-   `run_context`: The active run context wrapper.

Return a string to replace the message, or `None` to use the SDK default.

```python
from agents import Agent, RunConfig, Runner, ToolErrorFormatterArgs

def format_rejection(args: ToolErrorFormatterArgs[None]) -> str | None:
    if args.kind == "approval_rejected":
        return (
            f"Tool call '{args.tool_name}' was rejected by a human reviewer. "
            "Ask for confirmation or propose a safer alternative."
        )
    if args.kind == "tool_not_found":
        return f"Tool '{args.tool_name}' is not available. Choose one of the listed tools."
    return None

agent = Agent(name="Assistant")
result = Runner.run_sync(
    agent,
    "Please delete the production database.",
    run_config=RunConfig(tool_error_formatter=format_rejection),
)
```

##### `reasoning_item_id_policy`

`reasoning_item_id_policy` controls how reasoning items are converted into next-turn model input when the runner carries history forward (for example, when using `RunResult.to_input_list()` or session-backed runs).

-   `None` or `"preserve"` (default): Keep reasoning item IDs.
-   `"omit"`: Strip reasoning item IDs from the generated next-turn input.

Use `"omit"` primarily as an opt-in mitigation for a class of Responses API 400 errors where a reasoning item is sent with an `id` but without the required following item (for example, `Item 'rs_...' of type 'reasoning' was provided without its required following item.`).

This can happen in multi-turn agent runs when the SDK constructs follow-up input from prior outputs (including session persistence, server-managed conversation deltas, streamed/non-streamed follow-up turns, and resume paths) and a reasoning item ID is preserved but the provider requires that ID to remain paired with its corresponding following item.

Setting `reasoning_item_id_policy="omit"` keeps the reasoning content but strips the reasoning item `id`, which avoids triggering that API invariant in SDK-generated follow-up inputs.

Scope notes:

-   This only changes reasoning items generated/forwarded by the SDK when it builds follow-up input.
-   It does not rewrite user-supplied initial input items.
-   `call_model_input_filter` can still intentionally reintroduce reasoning IDs after this policy is applied.

## State and conversation management

### Choose a memory strategy

There are four common ways to carry state into the next turn:

| Strategy | Where state lives | Best for | What you pass on the next turn |
| --- | --- | --- | --- |
| `result.to_input_list()` | Your app memory | Small chat loops, full manual control, any provider | The list from `result.to_input_list()` plus the next user message |
| `session` | Your storage plus the SDK | Persistent chat state, resumable runs, custom stores | The same `session` instance or another instance pointed at the same store |
| `conversation_id` | OpenAI Conversations API | A named server-side conversation you want to share across workers or services | The same `conversation_id` plus only the new user turn |
| `previous_response_id` | OpenAI Responses API | Lightweight server-managed continuation without creating a conversation resource | `result.last_response_id` plus only the new user turn |

`result.to_input_list()` and `session` are client-managed. `conversation_id` and `previous_response_id` are OpenAI-managed and only apply when you are using the OpenAI Responses API. In most applications, pick one persistence strategy per conversation. Mixing client-managed history with OpenAI-managed state can duplicate context unless you are deliberately reconciling both layers.

!!! note

    Session persistence cannot be combined with server-managed conversation settings
    (`conversation_id`, `previous_response_id`, or `auto_previous_response_id`) in the
    same run. Choose one approach per call.

### Conversations/chat threads

Calling any of the run methods can result in one or more agents running (and hence one or more LLM calls), but it represents a single logical turn in a chat conversation. For example:

1. User turn: user enters text
2. Runner run: first agent calls LLM, runs tools, does a handoff to a second agent, second agent runs more tools, and then produces an output.

At the end of the agent run, you can choose what to show to the user. For example, you might show the user every new item generated by the agents, or just the final output. Either way, the user might then ask a followup question, in which case you can call the run method again.

#### Manual conversation management

You can manually manage conversation history using the [`RunResultBase.to_input_list()`][agents.result.RunResultBase.to_input_list] method to get the inputs for the next turn:

```python
from agents import Agent, Runner, trace

async def main():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    thread_id = "thread_123"  # Example thread ID
    with trace(workflow_name="Conversation", group_id=thread_id):
        # First turn
        result = await Runner.run(agent, "What city is the Golden Gate Bridge in?")
        print(result.final_output)
        # San Francisco

        # Second turn
        new_input = result.to_input_list() + [{"role": "user", "content": "What state is it in?"}]
        result = await Runner.run(agent, new_input)
        print(result.final_output)
        # California
```

#### Automatic conversation management with sessions

For a simpler approach, you can use [Sessions](sessions/index.md) to automatically handle conversation history without manually calling `.to_input_list()`:

```python
from agents import Agent, Runner, SQLiteSession, trace

async def main():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create session instance
    session = SQLiteSession("conversation_123")

    thread_id = "thread_123"  # Example thread ID
    with trace(workflow_name="Conversation", group_id=thread_id):
        # First turn
        result = await Runner.run(agent, "What city is the Golden Gate Bridge in?", session=session)
        print(result.final_output)
        # San Francisco

        # Second turn - agent automatically remembers previous context
        result = await Runner.run(agent, "What state is it in?", session=session)
        print(result.final_output)
        # California
```

Sessions automatically:

-   Retrieves conversation history before each run
-   Stores new messages after each run
-   Maintains separate conversations for different session IDs

See the [Sessions documentation](sessions/index.md) for more details.

#### Server-managed conversations

You can also let the OpenAI conversation state feature manage conversation state on the server side, instead of handling it locally with `to_input_list()` or `Sessions`. This allows you to preserve conversation history without manually resending all past messages. With either server-managed approach below, pass only the new turn's input on each request and reuse the saved ID. See the [OpenAI Conversation state guide](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses) for more details.

OpenAI provides two ways to track state across turns:

##### 1. Using `conversation_id`

You first create a conversation using the OpenAI Conversations API and then reuse its ID for every subsequent call:

```python
from agents import Agent, Runner
from openai import AsyncOpenAI

client = AsyncOpenAI()

async def main():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    # Create a server-managed conversation
    conversation = await client.conversations.create()
    conv_id = conversation.id

    while True:
        user_input = input("You: ")
        result = await Runner.run(agent, user_input, conversation_id=conv_id)
        print(f"Assistant: {result.final_output}")
```

##### 2. Using `previous_response_id`

Another option is **response chaining**, where each turn links explicitly to the response ID from the previous turn.

```python
from agents import Agent, Runner

async def main():
    agent = Agent(name="Assistant", instructions="Reply very concisely.")

    previous_response_id = None

    while True:
        user_input = input("You: ")

        # Setting auto_previous_response_id=True enables response chaining automatically
        # for the first turn, even when there's no actual previous response ID yet.
        result = await Runner.run(
            agent,
            user_input,
            previous_response_id=previous_response_id,
            auto_previous_response_id=True,
        )
        previous_response_id = result.last_response_id
        print(f"Assistant: {result.final_output}")
```

If a run pauses for approval and you resume from a [`RunState`][agents.run_state.RunState], the SDK keeps the saved `conversation_id` / `previous_response_id` / `auto_previous_response_id` settings so the resumed turn continues in the same server-managed conversation.

`conversation_id` and `previous_response_id` are mutually exclusive. Use `conversation_id` when you want a named conversation resource that can be shared across systems. Use `previous_response_id` when you want the lightest Responses API continuation primitive from one turn to the next.

!!! note

    The SDK automatically retries `conversation_locked` errors with backoff. In server-managed
    conversation runs, it rewinds the internal conversation-tracker input before retrying so the
    same prepared items can be resent cleanly.

    In local session-based runs (which cannot be combined with `conversation_id`,
    `previous_response_id`, or `auto_previous_response_id`), the SDK also performs a best-effort
    rollback of recently persisted input items to reduce duplicate history entries after a retry.

    This compatibility retry happens even if you do not configure `ModelSettings.retry`. For
    broader opt-in retry behavior on model requests, see [Runner-managed retries](models/index.md#runner-managed-retries).

## Hooks and customization

### Call model input filter

Use `call_model_input_filter` to edit the model input right before the model call. The hook receives the current agent, context, and the combined input items (including session history when present) and returns a new `ModelInputData`.

The return value must be a [`ModelInputData`][agents.run.ModelInputData] object. Its `input` field is required and must be a list of input items. Returning any other shape raises a `UserError`.

```python
from agents import Agent, Runner, RunConfig
from agents.run import CallModelData, ModelInputData

def drop_old_messages(data: CallModelData[None]) -> ModelInputData:
    # Keep only the last 5 items and preserve existing instructions.
    trimmed = data.model_data.input[-5:]
    return ModelInputData(input=trimmed, instructions=data.model_data.instructions)

agent = Agent(name="Assistant", instructions="Answer concisely.")
result = Runner.run_sync(
    agent,
    "Explain quines",
    run_config=RunConfig(call_model_input_filter=drop_old_messages),
)
```

The runner passes a copy of the prepared input list to the hook, so you can trim, replace, or reorder it without mutating the caller's original list in place.

If you are using a session, `call_model_input_filter` runs after session history has already been loaded and merged with the current turn. Use [`session_input_callback`][agents.run.RunConfig.session_input_callback] when you want to customize that earlier merge step itself.

If you are using OpenAI server-managed conversation state with `conversation_id`, `previous_response_id`, or `auto_previous_response_id`, the hook runs on the prepared payload for the next Responses API call. That payload may already represent only the new-turn delta rather than a full replay of earlier history. Only the items you return are marked as sent for that server-managed continuation.

Set the hook per run via `run_config` to redact sensitive data, trim long histories, or inject additional system guidance.

## Errors and recovery

### Error handlers

All `Runner` entry points accept `error_handlers`, a dict keyed by error kind. The supported keys are `"max_turns"`, `"model_refusal"`, and `"invalid_final_output"`. Use them when you want to return a controlled final output instead of ending the run with the corresponding error.

```python
from agents import (
    Agent,
    RunErrorHandlerInput,
    RunErrorHandlerResult,
    Runner,
)

agent = Agent(name="Assistant", instructions="Be concise.")

def on_max_turns(_data: RunErrorHandlerInput[None]) -> RunErrorHandlerResult:
    return RunErrorHandlerResult(
        final_output="I couldn't finish within the turn limit. Please narrow the request.",
        include_in_history=False,
    )

result = Runner.run_sync(
    agent,
    "Analyze this long transcript",
    max_turns=3,
    error_handlers={"max_turns": on_max_turns},
)
print(result.final_output)
```

Use `"invalid_final_output"` when a model message does not validate against the agent's structured `output_type`, or when the model returns no structured final message. The handler can return an application-specific fallback, which the SDK validates against the same `output_type`. It does not retry the model call or replay any tool side effects. Returning `None` declines recovery. Without a fallback, non-empty validation failures continue to raise `ModelBehaviorError`, and empty structured responses retain the existing next-turn behavior.

```python
from pydantic import BaseModel

from agents import Agent, ModelBehaviorError, RunErrorHandlerInput, Runner

class Recipe(BaseModel):
    ingredients: list[str]
    recovered_from_invalid_output: bool = False

def on_invalid_final_output(data: RunErrorHandlerInput[None]) -> Recipe:
    assert isinstance(data.error, ModelBehaviorError)
    return Recipe(ingredients=[], recovered_from_invalid_output=True)

agent = Agent(
    name="Recipe assistant",
    instructions="Return a structured recipe.",
    output_type=Recipe,
)

result = Runner.run_sync(
    agent,
    "Plan tonight's dinner.",
    error_handlers={"invalid_final_output": on_invalid_final_output},
)
print(result.final_output)
```

`RunErrorHandlerResult.include_in_history` defaults to `True`. For a max-turns handler, this appends the synthesized fallback output to conversation history and persists it to the configured session. Set `include_in_history=False` when you want the fallback returned to the caller without adding it to result history or session storage.

Use `"model_refusal"` when a model refusal should produce an application-specific fallback instead of ending the run with `ModelRefusalError`.

```python
from pydantic import BaseModel

from agents import Agent, ModelRefusalError, RunErrorHandlerInput, Runner

class Recipe(BaseModel):
    ingredients: list[str]
    refusal_reason: str | None = None

def on_model_refusal(data: RunErrorHandlerInput[None]) -> Recipe:
    assert isinstance(data.error, ModelRefusalError)
    return Recipe(ingredients=[], refusal_reason=data.error.refusal)

agent = Agent(
    name="Recipe assistant",
    instructions="Return a structured recipe.",
    output_type=Recipe,
)

result = Runner.run_sync(
    agent,
    "Make me something unsafe.",
    error_handlers={"model_refusal": on_model_refusal},
)
print(result.final_output)
```

## Durable execution integrations and human-in-the-loop

For tool approval pause/resume patterns, start with the dedicated [Human-in-the-loop guide](human_in_the_loop.md). The integrations below are for durable orchestration when runs may span long waits, retries, or process restarts.

### Dapr

You can use the Agents SDK [Dapr](https://dapr.io) Diagrid integration to run durable, long-running agents that automatically recover from failures and support human-in-the-loop workflows. Dapr is a vendor-neutral, [CNCF](https://cncf.io) workflow orchestrator. Get started with Dapr and OpenAI agents [here](https://docs.diagrid.io/getting-started/quickstarts/ai-agents/?agentframework=openai).

### Temporal

You can use the Agents SDK [Temporal](https://temporal.io/) integration to run durable, long-running workflows, including human-in-the-loop tasks. View a demo of Temporal and the Agents SDK working in action to complete long-running tasks [in this video](https://www.youtube.com/watch?v=fFBZqzT4DD8), and [view docs here](https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib/openai_agents). 

### Restate

You can use the Agents SDK [Restate](https://restate.dev/) integration for lightweight, durable agents, including human approval, handoffs, and session management. The integration requires Restate's single-binary runtime as a dependency, and supports running agents as processes/containers or serverless functions. Read the [overview](https://www.restate.dev/blog/durable-orchestration-for-ai-agents-with-restate-and-openai-sdk) or view the [docs](https://docs.restate.dev/ai) for more details.

### DBOS

You can use the Agents SDK [DBOS](https://dbos.dev/) integration to run reliable agents that preserve progress across failures and restarts. It supports long-running agents, human-in-the-loop workflows, and handoffs. It supports both sync and async methods. The integration requires only a SQLite or Postgres database. View the integration [repo](https://github.com/dbos-inc/dbos-openai-agents) and the [docs](https://docs.dbos.dev/integrations/openai-agents) for more details.

## Exceptions

The SDK raises exceptions in certain cases. The full list is in [`agents.exceptions`][]. As an overview:

-   [`AgentsException`][agents.exceptions.AgentsException]: This is the base class for all exceptions that the SDK raises. It serves as a generic type from which all other specific exceptions are derived.
-   [`MaxTurnsExceeded`][agents.exceptions.MaxTurnsExceeded]: This exception is raised when the agent's run exceeds the `max_turns` limit passed to the `Runner.run`, `Runner.run_sync`, or `Runner.run_streamed` methods. It indicates that the agent could not complete its task within the specified number of agent-loop turns (LLM calls). Set `max_turns=None` to disable the limit.
-   [`ModelTimeoutError`][agents.exceptions.ModelTimeoutError]: This exception is raised when a model-call attempt exceeds [`ModelSettings.timeout`][agents.model_settings.ModelSettings.timeout]. See [Model-call timeouts](models/index.md#model-call-timeouts) for scope and retry behavior.
-   [`ModelBehaviorError`][agents.exceptions.ModelBehaviorError]: This exception occurs when the underlying model (LLM) produces unexpected or invalid outputs. This can include:
    -   Malformed JSON: When the model provides a malformed JSON structure for tool calls or in its direct output, especially if a specific `output_type` is defined.
    -   Unexpected tool-related failures: When the model fails to use tools in an expected manner
    -   Failed or incomplete non-streaming Responses calls: `OpenAIResponsesModel` and the Responses path in `AnyLLMModel` raise this exception when the returned response has terminal status `failed` or `incomplete`. The exception identifies the terminal status and includes available error or incomplete details from the response.
-   [`ToolTimeoutError`][agents.exceptions.ToolTimeoutError]: This exception is raised when a function tool call exceeds its configured timeout and the tool uses `timeout_behavior="raise_exception"`.
-   [`UserError`][agents.exceptions.UserError]: This exception is raised when you (the person writing code using the SDK) make an error while using the SDK. This typically results from incorrect code implementation, invalid configuration, or misuse of the SDK's API.
-   [`InputGuardrailTripwireTriggered`][agents.exceptions.InputGuardrailTripwireTriggered], [`OutputGuardrailTripwireTriggered`][agents.exceptions.OutputGuardrailTripwireTriggered]: `InputGuardrailTripwireTriggered` is raised when an input guardrail's conditions are met, and `OutputGuardrailTripwireTriggered` is raised when an output guardrail's conditions are met. Input guardrails check incoming messages before processing, while output guardrails check the agent's final response before delivery.

---

## sandbox_agents

- 官方原文：https://github.com/openai/openai-agents-python/blob/main/docs/sandbox_agents.md
- 存档：`01-Raw/VibeCoding/openai/openai-agents-sdk-docs-sandbox-agents-md.md`

# Quickstart

!!! warning "Beta feature"

    Sandbox agents are in beta. Expect details of the API, defaults, and supported capabilities to change before general availability, and expect more advanced features over time.

Modern agents work best when they can operate on real files in a filesystem. **Sandbox Agents** in the Agents SDK give the model a persistent workspace where it can search large document sets, edit files, run commands, generate artifacts, and pick work back up from saved sandbox state.

The SDK gives you that execution harness without making you wire together file staging, filesystem tools, shell access, sandbox lifecycle, snapshots, and provider-specific glue yourself. You keep the normal `Agent` and `Runner` flow, then add a `Manifest` for the workspace, capabilities for sandbox-native tools, and `SandboxRunConfig` for where the work runs.

## Prerequisites

- Python 3.10 or higher
- Basic familiarity with the OpenAI Agents SDK
- A sandbox client. For trusted local development, start with `UnixLocalSandboxClient`.

## Installation

If you have not already installed the SDK:

```bash
pip install openai-agents
```

For Docker-backed sandboxes:

```bash
pip install "openai-agents[docker]"
```

## Create a local sandbox agent

This example stages a local repo under `repo/`, loads local skills lazily, and has the runner create a Unix-local sandbox session for the run.

!!! warning "Local commands use host permissions"

    On Linux, `UnixLocalSandboxClient` adds no OS-level confinement to commands. On macOS, it applies filesystem restrictions through `sandbox-exec`, but does not provide network isolation. Use this example for trusted local development or within an externally isolated environment. For untrusted commands, including commands influenced by untrusted inputs, choose an appropriately configured Docker or hosted sandbox, or provide external isolation. See [Unix-local execution limits](sandbox/clients.md#decision-guide).

```python
import asyncio
from pathlib import Path

from agents import Runner
from agents.run import RunConfig
from agents.sandbox import Manifest, SandboxAgent, SandboxRunConfig
from agents.sandbox.capabilities import Capabilities, LocalDirLazySkillSource, Skills
from agents.sandbox.entries import LocalDir
from agents.sandbox.sandboxes.unix_local import UnixLocalSandboxClient

EXAMPLE_DIR = Path(__file__).resolve().parent
HOST_REPO_DIR = EXAMPLE_DIR / "repo"
HOST_SKILLS_DIR = EXAMPLE_DIR / "skills"

def build_agent(model: str) -> SandboxAgent[None]:
    return SandboxAgent(
        name="Sandbox engineer",
        model=model,
        instructions=(
            "Read `repo/task.md` before editing files. Stay grounded in the repository, preserve "
            "existing behavior, and mention the exact verification command you ran. "
            "If you edit files with apply_patch, paths are relative to the sandbox workspace root."
        ),
        default_manifest=Manifest(
            entries={
                "repo": LocalDir(src=HOST_REPO_DIR),
            }
        ),
        capabilities=Capabilities.default() + [
            Skills(
                lazy_from=LocalDirLazySkillSource(
                    # This is a host path read by the SDK process.
                    # Requested skills are copied into `skills_path` in the sandbox.
                    source=LocalDir(src=HOST_SKILLS_DIR),
                )
            ),
        ],
    )

async def main() -> None:
    result = await Runner.run(
        build_agent("gpt-5.6-sol"),
        "Open `repo/task.md`, fix the issue, run the targeted test, and summarize the change.",
        run_config=RunConfig(
            sandbox=SandboxRunConfig(client=UnixLocalSandboxClient()),
            workflow_name="Sandbox coding example",
        ),
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

See [examples/sandbox/docs/coding_task.py](https://github.com/openai/openai-agents-python/blob/main/examples/sandbox/docs/coding_task.py). It uses a tiny shell-based repo so the example can be verified deterministically across Unix-local runs.

## Key choices

Once the basic run works, the choices most people reach for next are:

- `default_manifest`: the files, repos, directories, and mounts for fresh sandbox sessions
- `instructions`: short workflow rules that should apply across prompts
- `base_instructions`: an advanced escape hatch for replacing the SDK sandbox prompt
- `capabilities`: sandbox-native tools such as filesystem editing/image inspection, shell, skills, memory, and the SDK's compaction mechanism
- `run_as`: the sandbox user account under which model-facing tools execute
- `SandboxRunConfig.client`: the sandbox backend
- `SandboxRunConfig.session`, `session_state`, or `snapshot`: how later runs reconnect to prior work

## Where to go next

- [Concepts](sandbox/guide.md): understand manifests, capabilities, permissions, snapshots, run config, and composition patterns.
- [Sandbox clients](sandbox/clients.md): choose Unix-local, Docker, hosted providers, and mount strategies.
- [Agent memory](sandbox/memory.md): preserve and reuse lessons from previous sandbox runs.

If shell access is just one tool that you use occasionally, start with hosted shell in the [tools guide](tools.md). Reach for sandbox agents when workspace isolation, sandbox client choice, or sandbox-session resume behavior are part of the design.
