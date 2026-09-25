---
title: 🏭 Project
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
- Xpertai/XpertAI工作流教程-MD版/ai/conversation/projects.md
---
# 🏭 Project

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# 🏭 Project

**Xpert Projects** is a new collaborative AI project feature on the XpertAI platform, enabling users to efficiently complete complex tasks by flexibly combining digital expert agents, toolsets, and file resources. It offers a one-stop solution for dynamic planning, intelligent execution, and resource integration for individual multi-step projects or team collaboration.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/project/xpert-project.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=5714bd15059251949b514f9cda1ae8b0" alt="Xpert Project" width="2688" height="1714" data-path="public/img/ai/project/xpert-project.png" />

## Core Features

### 1. Project Creation & Management

Create projects directly in the digital expert interface, customize project names and avatars. Manage all resources (agents, tools, files, session records) centrally, with editing and archiving support.

**Steps**

1. Click “New Project” in the agent interface.
2. Save and access the project management panel.
3. Edit project name and avatar.

### 2. Multi-Agent Collaboration

Import published digital expert agents into projects. Agents share file storage and collaborate to generate precise solutions.

**Use Cases**

* **Market Analysis**: Combine “Data Analyst,” “Trend Forecaster,” and “Copywriting Assistant” for reports.
* **Tech Development**: Use “Code Generator,” “Test Engineer,” and “Documentation Assistant” for tasks.

### 3. Toolset Integration (MCP Tool Compatible)

Add toolsets (e.g., MCP tools) from bound agent workspaces to extend project agent capabilities. Tool results sync to project context in real-time.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/project/project-tools.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=0b96acee29a092f0014ccd1e6e7830f8" alt="Project tools" width="2688" height="1714" data-path="public/img/ai/project/project-tools.png" />

**Supported Tools**

* Data processing (e.g., Excel parsing, API calls)
* Development (e.g., code debugging, version control)
* Industry-specific (e.g., data modeling, design rendering)
* Compatible with all MCP marketplace tools.

### 4. File Upload & Context Sharing

Upload text files (e.g., PDF, TXT, DOCX) as a global knowledge base. All agents can access file content for responses or tasks.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/project/project-files.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=eaa72e3a0ddb186365b3b84ddcb45a5a" alt="Project files" width="2688" height="1714" data-path="public/img/ai/project/project-files.png" />

**Benefits**

* Persistent file storage across sessions
* Automatic file content extraction for enhanced context.

### 5. Intelligent Execution Mode Switching

Project agents support two modes:

1. **Exploration Mode**: AI autonomously breaks down tasks and optimizes paths, ideal for rapid prototyping.
2. **Planning Mode**: AI creates detailed step-by-step plans, suited for structured workflows.

<img src="https://mintcdn.com/xpertai/CUk-Ab9Rv7YWeJmd/public/img/ai/project/project-plan.png?fit=max&auto=format&n=CUk-Ab9Rv7YWeJmd&q=85&s=f63f410ccd0ec722d8184e2cfc8805d6" alt="Project plan" width="3024" height="1714" data-path="public/img/ai/project/project-plan.png" />

### 6. Team Collaboration & Permission Management

* **Member Invitation**: Add colleagues to co-manage projects.
* **Session Management**: Retain full conversation and execution history.
* **System Instructions**: Define project-level rules (e.g., format standards, terminology) for unified agent behavior.

## Prompt Examples

* Core functionality and workflow management prompt:

```markdown theme={null}
# CORE IDENTITY & CAPABILITIES
You are a full-spectrum autonomous agent capable of executing complex tasks across domains including information gathering, content creation, software development, data analysis, and problem-solving. You have access to a Linux environment with internet connectivity, file system operations, terminal commands, web browsing, and programming runtimes.

# WORKFLOW MANAGEMENT

## AUTONOMOUS WORKFLOW SYSTEM
You operate through a self-maintained tasks that serves as your central source of truth and execution roadmap:

1. Upon receiving a task, immediately create a lean, focused plan with essential sections covering the task lifecycle
2. Each section contains specific, actionable subtasks based on complexity - use only as many as needed, no more
3. Each task should be specific, actionable, and have clear completion criteria
4. MUST actively work through these tasks one by one, checking them off as completed
5. Adapt the plan as needed while maintaining its integrity as your execution compass
```

* [Sandbox Tool Prompts](/docs/ai/tool/sandbox/#prompt-guidelines)

## Typical Use Cases

1. **Cross-Domain Research**: Combine industry experts, data tools, and literature for in-depth analysis.
2. **Product Development**: Automate from requirements parsing to code generation and testing.
3. **Team Knowledge Base**: Build Q\&A systems from uploaded files with real-time agent support.

Start using Xpert Project to unlock a new era of intelligent collaboration!
