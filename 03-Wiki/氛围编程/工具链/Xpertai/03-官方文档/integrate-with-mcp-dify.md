---
title: Integrating Dify via MCP
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
- Xpertai/XpertAI工作流教程-MD版/ai/tutorial/integrate-with-mcp-dify.md
---
# Integrating Dify via MCP

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating Dify via MCP

To further unlock the potential of enterprise digital resources, the **Xpert AI Multi-Agent Platform** now supports deep integration with the **Dify platform** via **MCP**, covering key capabilities such as **Knowledge Base**, **Workflow**, and **Chatflow**.

Through this tutorial, you will learn how to configure MCP tools in the Xpert AI platform, integrate Dify’s core resources, and empower AI agents to use these tools to achieve smarter and more professional business automation processes.

***

## 🧩 Step 1: Prepare Dify Platform Resources

Before integration, you need to prepare the resources you want to connect to on the [Dify Platform](https://cloud.dify.ai/), such as:

* **Knowledge Base**: e.g., FAQ documents, product introductions, etc.;
* **Workflow**: e.g., an automated process for exception handling or approvals;
* **Chatflow**: Custom LLM-based dialogue processes.

### ✅ Required Information

Prepare the following information for use during tool configuration:

* Dify **API Key** (it’s recommended to use a key with the appropriate resource permissions);
* The unique identifiers of the resources (such as Workflow ID, Chatflow ID);
* Other required access parameters (e.g., Base URL, Agent ID, etc.).

***

## 🛠️ Step 2: Install Dify Tool Template from MCP Marketplace

1. Go to the **[MCP Tool Marketplace](/docs/ai/tool/mcp/#mcp-tools-marketplace)** in the Xpert AI platform;
2. Search for the keyword **“Dify”**, and you will find several official Dify integration templates:
   * Dify Chatflow Invocation Template
   * Dify Workflow Invocation Template
   * Dify Knowledge Base Q\&A Template
3. Select the template that fits your needs and click **“Install”**;
4. On the installation page, fill in:
   * The **API Key** of the Dify platform
   * The target resource ID (e.g., Chatflow ID, Workflow ID)
   * Optional: default parameters, environment variable configurations, etc.
5. After installation, the MCP tool will be automatically generated and appear in your tool list.

***

## 🧬 Step 3: Customize MCP Tool Code for Parameters and Logic

Go to the “Code” tab to fine-tune the tool’s logic. Here's an example:

```python title=main.py theme={null}
import os
import requests

...

@mcp.tool()
def run_chatflow(input: str) -> Optional[str]:
   """
   Calls a Chatflow process on the Dify platform, useful for exception handling and similar scenarios.
   :param input: User's description of the issue, used as main context for the Dify Chatflow.
   :return: Core response content returned by Dify
   """

   API_KEY = os.getenv("DIFY_API_KEY")
   CHATFLOW_ID = os.getenv("DIFY_CHATFLOW_ID")

   headers = {"Authorization": f"Bearer {API_KEY}"}
   payload = {
      "inputs": {"input": input},
      "response_mode": "blocking"
   }

   resp = requests.post(
      f"https://api.dify.ai/v1/chat-flows/{CHATFLOW_ID}/invoke",
      json=payload,
      headers=headers,
      timeout=20
   )

   if resp.status_code == 200:
      return resp.json().get("answer")  # Adjust based on Dify’s response format
   return None
```

### 💡 Tips

* The `input` parameter can be extended with more fields (e.g., user role, business type);
* The function's docstring is **critical for guiding the model in tool invocation**—describe purpose, input expectations, and typical use cases clearly;
* For structured outputs (e.g., JSON), add parsing logic to extract key fields;
* Use environment variables to manage sensitive data securely.

Once done, click save to generate your MCP tool.

***

## 🧠 Step 4: Integrate MCP Tool into an Agent

1. Open the agent orchestration page for the agent that needs to access Dify resources;
2. Click "Add Toolkit", and select the Dify MCP tool you just created;
3. The configuration will auto-save;
4. Now your agent can invoke Dify Chatflow, Workflows, or Knowledge Base content based on user input in conversations.

***

## ✅ Example Use Cases

* **Customer Support Copilot**: Automatically answer user questions by invoking Dify Chatflow;
* **Process Collaboration Agent**: Connect to Dify workflows for sales approvals, exception handling, etc.;
* **Knowledge Search Assistant**: Integrate Dify Knowledge Base for real-time business knowledge retrieval.

***

## ❓ Frequently Asked Questions (FAQ)

Here are some common issues and solutions when integrating and using Dify tools on the Xpert AI platform:

***

### 1. 🧠 The model didn’t invoke the tool?

**Possible reasons & solutions**:

* Check if the model supports **tool calling**;
* Ensure the MCP tool’s `Docstring` is clear and descriptive;
* Check if the agent’s prompt guides the model to recognize tool use;
* Make sure the tool is properly bound to the agent.

**Tip**: Add intent hints in the description, like: “When the user asks XXX, please invoke this tool.”

***

### 2. 🧾 Missing parameters when calling the MCP tool?

**Check the following**:

* Are parameters set as optional instead of required?
* Is the parameter usage described clearly in the docstring?
* Use required parameters (no default value) to force input;
* Provide structured prompts to guide input correctly.

***

### 3. 🔐 “Unauthorized” or “401” error?

**Possible reasons**:

* Incorrect or expired API Key;
* API Key not correctly passed via environment variables;
* Key lacks permission to access the target resource.

***

### 4. 🆔 “Resource Not Found” or “Invalid ID”?

**Check**:

* If the Chatflow/Workflow ID is correct;
* Whether the resource is private and accessible to the API Key user;
* Avoid spaces or hidden characters when copying the ID.

***

### 5. 🌐 Dify call fails or has no response?

**Tips**:

* Increase `timeout` (e.g., `timeout=30`) if request times out;
* Ensure network can access `https://api.dify.ai`;
* Add error handling and logging in the MCP tool.

***

### 6. 🧪 Incomplete or malformed return from the tool?

**Check**:

* Understand Dify’s response format (typically JSON);
* Log the full response to debug;
* If the response is in markdown or HTML, add cleanup logic.

***

### 7. 🤖 Agent hit rate limits or errors when calling tools?

**Solutions**:

* Check Dify's rate limit policy;
* Use higher-permission API Key or upgrade plan;
* Add cooldowns or retry logic in MCP tool.

***

### 8. 📦 MCP tool fails to connect?

**Check**:

* Are required Python packages (e.g., `requests`, `httpx`) missing?
* Add them to `requirements.txt`;
* Re-deploy after updating dependencies;
* Check logs for `ModuleNotFoundError`.

**Tip**: Fully test locally before deploying.

***

### 9. 🛠️ How to debug if the tool was called successfully?

**Try**:

* Print `response.status_code` and `response.json()` in the MCP tool;
* Use Postman or curl to test Dify API manually;
* Use Xpert AI’s MCP tool test console to simulate input and inspect logs.

***

### 10. 🔄 How to update or upgrade Dify integration tools?

**Steps**:

* Edit the code in the MCP tool backend;
* If a new version of the template is available, reinstall or merge changes;
* Save the toolkit after updating to apply changes.

***

If you have more questions, feel free to join our developer community or contact technical support for assistance.
