---
title: Roles
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
- Xpertai/XpertAI工作流教程-MD版/ai/ai-assistant/roles.md
---
# Roles

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Roles

The **Copilot Business Role** function provides virtual business assistant roles when Copilot performs tasks. These roles help AI better understand the actual business scenarios and meanings of tasks. Through the business role, the system can use few-shot learning to provide relevant prompt examples, enabling AI to generate and execute corresponding operations based on the business context accurately. This not only improves the accuracy of task execution but also ensures the rationality and consistency of business logic, adapting to various business needs.

## Role Usage

1. **Custom Roles**:
   Users can customize business roles according to their current analysis needs. These roles are pre-set with different analysis themes and examples, suitable for different business scenarios such as market analysis, financial reporting, operations management, and more.

2. **Example Fewshot**:
   Each business role corresponds to different examples. When a user selects or customizes a business role, Copilot automatically selects examples most relevant to the role and sends them to the large language model (LLM) for processing. This ensures that the generated analysis results are more aligned with actual business needs.

3. **Role Switching**:
   Users can switch business roles at any time during the analysis process to suit different analytical tasks and business needs. This flexibility allows users to handle multiple types of data analysis tasks on the same platform.
