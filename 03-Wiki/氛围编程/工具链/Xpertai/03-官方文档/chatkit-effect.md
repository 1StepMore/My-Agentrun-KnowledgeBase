---
title: Client Effects
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/chatkit/chatkit-effect.md
---
# Client Effects

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Client Effects

<Info>
  Learn how to define tools that let the agent trigger client-side effects.
</Info>

Client effects **push model-generated “side-effect events” to the frontend for execution** **without interrupting model reasoning**, and they return a server-configured default value to the model. Use them for UI updates, focus, highlighting, animations, and state sync—situations that only affect the frontend and do not depend on a returned value.

<img src="https://mintcdn.com/xpertai/s0VVkPNi8D_ZpOIf/public/img/ai/chatkit/client-effect-middleware.png?fit=max&auto=format&n=s0VVkPNi8D_ZpOIf&q=85&s=d830ac1b8222a34da45c321610ef5318" alt="Client effect middleware" width="1764" height="1534" data-path="public/img/ai/chatkit/client-effect-middleware.png" />

## Core capabilities

* **No interruption**: does not wait for the frontend to respond
* **One-way notification**: model → frontend UI
* **Automatic return value**: uses the middleware-configured Result
* **Strong UI control**: the model can “drive UI changes”

***

## Workflow

1. **Configure the Client Effect middleware on the server**

* Define `Tool Name / Description / Arguments Schema`
* Configure a fixed `Result`

2. **Model triggers the effect**

* The LLM calls the effect tool (for example, `show_station`)

3. **Frontend receives and executes**

* ChatKit sends the event via `onEffect`
* The frontend performs the UI side effect (state update, focus, etc.)

4. **Model continues reasoning**

* It does not wait for frontend completion

***

## Server configuration essentials

**Tool Name**

```text theme={null}
show_station
```

**Arguments Schema (example)**

The schema must follow the [JSON Schema spec](https://json-schema.org/learn/getting-started-step-by-step):

```json theme={null}
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Station name"
    }
  }
}
```

**Result**

```text theme={null}
It has already been shown to users
```

***

## Frontend (React) integration

Register `onEffect` in `useChatKit`:

```ts theme={null}
const handleClientEffect = useCallback(
  ({ name, data }) => {
    if (name === 'update_mindmap' && data?.mindmap) {
      setMindmap(convertMindmapFromSnake(data.mindmap));
    }

    if (name === 'focus_node' && data?.nodeId) {
      focusNode(data.nodeId);
    }
  },
  []
);
```

```ts theme={null}
useChatKit({
  ...
  onEffect: handleClientEffect,
});
```

***

## Client Tool vs. Client Effect

| Item                      | Client Tool                     | Client Effect                |
| ------------------------- | ------------------------------- | ---------------------------- |
| Interrupts reasoning      | ✅ Yes                           | ❌ No                         |
| Waits for frontend result | ✅ Yes                           | ❌ No                         |
| Dynamic result            | ✅ Yes                           | ❌ No (fixed Result)          |
| Best for                  | State reads / user confirmation | UI updates / display / focus |

***

## Best practices

* Effects handle **UI side effects only**; keep business decisions elsewhere
* `name` must exactly match the server tool name
* `data` should include only the minimal fields needed by the frontend
* Avoid long-running or blocking tasks inside effects

***

Client effects let the model **declaratively drive UI behavior**, which is key for building **visual, highly interactive agent experiences**.
