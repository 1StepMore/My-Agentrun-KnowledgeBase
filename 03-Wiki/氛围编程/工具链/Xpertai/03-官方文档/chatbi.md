---
title: ChatBI Toolset
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
- Xpertai/XpertAI工作流教程-MD版/ai/toolset/chatbi-toolset/chatbi.md
---
# ChatBI Toolset

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# ChatBI Toolset

**ChatBI (Data Analysis) Toolset** Seamlessly integrates with Xpert Data Analysis Platform for business intelligence tools.

### Configuring ChatBI Toolset

See [BI Toolset](/docs/ai/tool/bi/).

### Session Variables

* `chatbi_models`: List of available Cubes, accessible via `get_available_cubes` tool.
* `chatbi_cubes`: List of available Cubes.
* `chatbi_cubes_context`: Contextual info for available Cubes.
* `tool_chatbi_prompts_default`: Default prompts for ChatBI tools, usable in main agent prompts.

### Prompt Example

```text theme={null}
You are a sales analysis expert. Use tools to answer user queries.  
{{tool_chatbi_prompts_default}}  

Common times:  
{{sys.common_times}}  

Available Cubes:  
<cubes>  
{{chatbi_models}}  
</cubes>  
```

### Tools

#### 1. get\_available\_cubes

Fetches list of accessible Cubes. Use `{{chatbi_models}}` in prompts to reduce tool calls.

```text theme={null}
Available Cubes:  
<cubes>  
{{chatbi_models}}  
</cubes>  
```

#### 2. get\_cube\_context

Retrieves Cube context (dimensions, measures, metrics). Helps agents understand Cube data structure for accurate responses.\
When using [Session Summary](/docs/ai/xpert/long-term-memory), context may be summarized. Use `{{chatbi_cubes_context}}` in prompts for detailed Cube info:

```text theme={null}
Cube context:  
<cubes>  
{{chatbi_cubes_context}}  
</cubes>  
```

#### 3. dimension\_member\_retriever

Fetches dimension member details (dimension, hierarchy, level, key, caption) for building reports or filters.\
Solves inefficient manual searches by using semantic queries and embeddings to return matching members.

**Features:**

* Natural language query support.
* Handles multi-level dimension structures.
* Controls TopK results.
* Supports re-embedding for accurate matches.
* Links with model ID and Cube for consistent results.

**Use Cases:**

* Confirming “East China” for sales analysis.
* Retrieving members like “Gold Card” for filters.

**Parameters:**

| Parameter      | Type               | Description                        |
| -------------- | ------------------ | ---------------------------------- |
| `modelId`      | string             | Data model ID.                     |
| `cube`         | string             | Cube name.                         |
| `query`        | string             | Keyword for fuzzy search.          |
| `dimension`    | string (optional)  | Dimension name.                    |
| `hierarchy`    | string (optional)  | Hierarchy name.                    |
| `level`        | string (optional)  | Dimension level.                   |
| `topK`         | number (optional)  | Max results returned.              |
| `re_embedding` | boolean (optional) | Re-embed members (default: false). |

**Indexing Dimension Members:**\
Vectorize dimension members for faster retrieval. See [Dimension Member Retrieval](/docs/models/member-retriever).

#### 4. answer\_question

Answers user queries using Cube context, returning data visuals or metrics.

**Temporary Calculated Members:**\
For queries requiring temporary calculations, agents pass `calculated_members` to the tool:

```json theme={null}
{  
  "calculated_members": [  
    {  
      "name": "Calculated Member Name",  
      "caption": "Display Name",  
      "description": "Description",  
      "formula": "Expression",  
      "formatting": {  
        "unit": "Unit",  
        "decimal": "Decimals"  
      }  
    }  
  ]  
}  
```

**Example:** *Analyze monthly sales growth rate for value-added resellers over the past two years.*

1. Fetch Cube context.
2. Retrieve dimension member details.
3. Build visual answer with *monthly growth rate* calculated member.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/xpertai/en/ai/toolset/chatbi-toolset/calculated-members.png" alt="Using Calculated Members" />

Open the chart execution interpreter to view detailed parameters:

<img src="https://mintcdn.com/xpertai/IL25qkwj-czMDTNd/public/img/chatbi/calculated-members-explain.png?fit=max&auto=format&n=IL25qkwj-czMDTNd&q=85&s=aebf58fd69467e601e2ab49a27600bfc" alt="Explanation of calculated member parameters" width="2436" height="1562" data-path="public/img/chatbi/calculated-members-explain.png" />

**Parameter Control:**\
For models with [parameters](/docs/models/cube-designer/parameter/), agents select appropriate values.\
Example: “Top 5 high-value customer sales” uses:

```json theme={null}
{  
  "parameters": [  
    {  
      "name": "TopN",  
      "value": 5  
    }  
  ],  
  "measures": [  
    {  
      "name": "High-Value Customer Sales"  
    }  
  ]  
}  
```

#### 5. show\_indicators

Displays metrics as a list when users explicitly request specific indicators.

### Feishu-Adapted ChatBI

```text theme={null}
You are a data analysis expert. Use tools to answer user queries.  

If no specific query, use `welcome` tool to suggest 3 questions for Top 3 models based on context.  

If Cube dimensions/measures are missing, use `get_cube_context` first.  

Use `answer_question` for analysis results:  
- Use `slicers` for explicit time.  
- Use `timeSlicers` for relative time:  
  <input>last year</input>  
  <output>lookBack: 1, lookAhead: -1</output>  
  <input>this year</input>  
  <output>lookBack: 0, lookAhead: 0</output>  
  <input>next year</input>  
  <output>lookBack: -1, lookAhead: 1</output>  
  <input>last year to this year</input>  
  <output>lookBack: 1, lookAhead: 0</output>  

Current date: {{sys.date}}  
Common times: {{sys.common_times}}  

If Cube lacks required measures/indicators, create one using `create_indicator` before answering.  
MDX query restrictions:  
1. Same dimension cannot appear in multiple axes (columns, rows, slicers). Use functions like `descendants` for restrictions.  

No image generation needed; visuals are shown via tools.  

Available models:  
<cubes>  
{{chatbi_models}}  
</cubes>  
```

**Note:** `show_indicators` is not supported for Feishu.

#### welcome

When no specific query is provided, suggests questions for users based on available models.\
Set as a [terminal tool](/docs/ai/xpert/terminal/); no further response needed after execution.

### Publishing to Feishu Bot

Publish ChatBI toolkit as a Feishu bot app via [one-click publishing](/docs/ai/xpert/publish). Displays results as interactive card messages.

See [ChatBI Feishu Bot](/docs/chatbi/feishu/bot) for details.

### Version Control & Changelog

* **v3.4**:
  * Removed `create_indicator` tool; replaced with `calculated_members` parameter.
  * Added `parameters` and `calculated_members` to `answer_question` tool.
