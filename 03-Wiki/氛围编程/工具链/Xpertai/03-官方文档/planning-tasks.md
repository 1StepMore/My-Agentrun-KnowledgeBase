---
title: Planning Tasks
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
- Xpertai/XpertAI工作流教程-MD版/ai/toolset/planning-tasks.md
---
# Planning Tasks

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Planning Tasks

## Toolkit Introduction

The planning toolkit provides AI agent teams with task planning and execution capabilities. By invoking the following four tool methods, agents can create, manage, update, and delete task plans, executing them step-by-step to achieve more efficient and intelligent automated workflows.

## 1. create\_plan

* **Function:** Create a new task plan.
* **Parameters:**
  * `title` (string): The title of the plan.
  * `steps` (list): A list of plan steps, each containing information such as step descriptions.
* **Return Value:** Returns the plan ID on success, or an error message on failure.

## 2. list\_plans

* **Function:** List all created task plans.
* **Parameters:** None
* **Return Value:** Returns a list of all plans, including plan ID, name, creation time, and other details.

## 3. update\_plan\_step

* **Function:** Update a specific step in a task plan.
* **Parameters:**
  * `step_index` (number): The index of the step to update.
  * `new_step_info` (dictionary): The new step information, such as step description.
* **Return Value:** Returns the updated step information on success, or an error message on failure.

## 4. delete\_plan\_step

* **Function:** Delete a specific step from a task plan.
* **Parameters:**
  * `step_index` (number): The index of the step to delete.
* **Return Value:** Returns the ID of the deleted step on success, or an error message on failure.

## Use Cases

* **Project Management:** Agents can create task plans based on project requirements, assign them to different agents for execution, and monitor project progress in real-time.
* **Process Automation:** Automate highly repetitive and rule-based workflows, such as data cleaning, report generation, etc.
* **Intelligent Decision-Making:** Combine with other AI tools, such as data analysis or predictive models, for smarter decision-making and planning.

## Summary

The planning toolkit enhances the Xpert AI platform with robust task planning and execution capabilities, empowering your AI agent team to achieve more efficient and intelligent automated workflows.
