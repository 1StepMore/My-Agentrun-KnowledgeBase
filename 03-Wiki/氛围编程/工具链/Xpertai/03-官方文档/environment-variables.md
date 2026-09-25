---
title: Environment Variables
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
- Xpertai/XpertAI工作流教程-MD版/ai/digital-expert/environment-variables.md
---
# Environment Variables

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Variables

To further enhance the platform's flexibility and maintainability, the Xpert AI Multi-Agent Platform officially launches the **Env Environment Management Function**. With this feature, users can define multiple runtime environments within a workspace and configure environment variables for use in agents, workflows, and toolsets. It supports critical capabilities such as sensitive information isolation, configuration reuse, and environment separation.

***

## 🧩 Feature Highlights

### ✅ Multi-Environment Definition and Switching

Each agent workspace supports creating multiple named environments (e.g., `dev`, `test`, `prod`), enabling independent configuration management for different business stages or runtime needs.

### ✅ Unified Environment Variable Management

Each environment can define multiple key-value pair variables, accessible across the platform using the unified syntax `{{env.variable_name}}`. These can be applied to agent model parameters, tool configurations, API calls, and more.

### ✅ Global Injection Mechanism

Environment variables can be dynamically resolved and injected into:

* Agent configurations (e.g., prompts)
* Workflow node parameters (e.g., HTTP params)
* Toolset connection configurations (e.g., API Key)

### ✅ Environment Binding for Digital Expert Publishing

When publishing a digital expert, you can **bind a specific environment**, which will automatically take effect during end-user interactions. This ensures digital experts use different prompts, APIs, or tool resources at various stages for consistent and controlled behavior.

### ✅ Runtime Environment Selection

When running or testing agents or workflow tasks, you can manually select an environment, and the platform will automatically load the corresponding variable set, improving testing efficiency and scenario flexibility.

***

## 🛠 How to Use

### 1. Create an Environment

Go to the workspace → Click the “Env” tab → Create an environment → Define the variable set:

For example:

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/envs.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=06c2b2559a9c4d31aa318cd90ad66ff2" alt="Environment Management" width="2320" height="772" data-path="public/img/ai/xpert/envs.png" />

### 2. Reference Variables

Use the `{{env.variable_name}}` syntax in agent, workflow, or tool configurations. For example:

<img src="https://mintcdn.com/xpertai/ZGpPZkKu2RpKGlB0/public/img/ai/xpert/use-env-in-agent.png?fit=max&auto=format&n=ZGpPZkKu2RpKGlB0&q=85&s=474991ea9038c38aa8b9487692cd28a8" alt="Prompt Referencing Environment Variables" width="1708" height="1474" data-path="public/img/ai/xpert/use-env-in-agent.png" />

### 3. Bind Default Environment for Digital Expert

In the “Digital Expert” publishing interface, select the default environment to bind. Once bound, all end-user conversation requests will run with that environment’s variables, ensuring response consistency and security.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/publish-with-env.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=c4478b8ad6b62bfa1f87a11832d52132" alt="Publish with Bound Environment" width="1096" height="1160" data-path="public/img/ai/xpert/publish-with-env.png" />

### 4. Manually Switch Environments for Testing

During development or debugging, flexibly select environments to simulate behavior differences across scenarios.

<img src="https://mintcdn.com/xpertai/KjFE_c3zPYs4Z9GJ/public/img/ai/xpert/env-variables.png?fit=max&auto=format&n=KjFE_c3zPYs4Z9GJ&q=85&s=ad36a6951ef052076ec44be9dcda7d5d" alt="Manage Environment Variables" width="1710" height="1126" data-path="public/img/ai/xpert/env-variables.png" />

***

The **release of the Env feature** marks a significant step forward for the XpertAI platform in configuration management, security control, and enterprise-grade multi-scenario deployment capabilities. Try it now and build your exclusive AI system with greater professionalism!
