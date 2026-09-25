---
title: OpenAI 官方文档汇编 · 02-Cookbook 官方文章
source: OpenAI 官方仓库（openai-agents-python / openai-cookbook）（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/openai/openai-cookbook-articles-chatgpt-agents-sales-meeting-prep-md.md
- VibeCoding/openai/openai-cookbook-articles-codex-exec-plans-md.md
- VibeCoding/openai/openai-cookbook-articles-how-to-work-with-large-language-models-md.md
- VibeCoding/openai/openai-cookbook-articles-techniques-to-improve-reliability-md.md
- VibeCoding/openai/openai-cookbook-articles-what-makes-documentation-good-md.md
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

> **汇编性质**：OpenAI 官方仓库（openai-agents-python / openai-cookbook） 官方原文 5 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:37:43+08:00

---

## chatgpt-agents-sales-meeting-prep

- 官方原文：https://github.com/openai/openai-cookbook/blob/main/articles/chatgpt-agents-sales-meeting-prep.md
- 存档：`01-Raw/VibeCoding/openai/openai-cookbook-articles-chatgpt-agents-sales-meeting-prep-md.md`

# Building workspace agents in ChatGPT to complete repeatable, end-to-end work

This cookbook shows how to build a ChatGPT workspace agent. Currently available in research preview for ChatGPT Business, Enterprise, and Edu customers, workspace agents are evolutions of GPTs that can work across tools to complete high-value tasks, helping your team move faster.

In this cookbook, we'll create a workspace agent through the conversational builder, give it access to our team's calendars and knowledge bases, and add a brief-writing skill to help craft the agent's output. Then we'll test our team agent, schedule it to run on a recurring schedule, and share it with teammates.

## Introduction

ChatGPT workspace agents are shared agents that can run repeatable workflows across ChatGPT and independently complete end-to-end tasks. They can use connected apps, follow skills, run on a schedule, and they can be shared with your colleagues in your workspace.

In this cookbook, we'll build a workspace agent that supports a sales team. Sales teams often spend time manually pulling account notes, recent customer feedback, product usage metrics, and company news to prepare for upcoming customer meetings.

We'll build a workspace agent that helps our sales team more efficiently prepare for their sales meetings by automatically generating meeting briefs ahead of upcoming customer calls, backed by up-to-date customer data. Specifically, our agent will run each day to check tomorrow's customer meetings, gather recent account context from SharePoint, and search the web for recent company news and background information on each attendee. Our agent will generate a meeting brief, save it down as a SharePoint doc, and send us an executive summary.

Once our agent is deployed, it will run automatically each day, and we can also invoke it on-demand in ChatGPT.

## Prerequisites and setup

For this cookbook, you will need a ChatGPT Business, Enterprise, or Edu workspace with access to workspace agents, and a set of apps (connectors) that enable your agent to access your calendar and account information. We'll use Google Calendar and Microsoft SharePoint to show a workflow that uses both Google Workspace and Microsoft 365 apps, but you can switch out any supported apps. Our agent will send notifications in Slack, but you can also use email or another notification surface.

Before you build, ask your workspace admin to confirm four settings:

1. **Agents are enabled for your workspace.** Workspace owners can enable agents for the workspace and assign access to specific roles with RBAC.
2. **You have permission to build and share agents.** An admin will need to enable you (or the appropriate RBAC group) to create agents. If you plan to share the agent, an admin may also need to enable publishing.
3. **The apps you need are enabled.** For this cookbook, an admin would need to enable Google Calendar, Gmail, and SharePoint in workspace app settings.
4. **[optional] Slack is approved for the workspace.** Only required if you want to interact with your agent through Slack. Enterprise admins need to enable the "workspace agents for Slack" app and grant access to users or groups with RBAC. Your Slack workspace must also allow the ChatGPT Agents app for Slack.

## Building your agent

The conversational agent builder is the fastest way to start. It can draft the agent profile, choose apps, generate a skill, write instructions, and prepare a draft agent that you can test in Preview. We'll use that flow here, then review each piece step by step so you can refine the agent later.

Note that if you want inspiration on work to automate, you can start from pre-built agent templates including a Chief of Staff, Data Analysis, and Customer Support agents.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img0.png" alt="Build a new agent" width="80%" />
</p>

### 1. Describe your workflow

We'll enter the following text into the agent builder:

```text
Create an agent to help with sales meeting prep. The agent should check my Google Calendar for tomorrow's customer meetings. Exclude internal-only meetings and skip events with no external attendees.

For each customer meeting, pull recent notes and feedback from SharePoint, then search the web for any relevant company news from the last 30 days. Then write a 2-3 page meeting brief. Save the meeting brief as a SharePoint doc.

Then, send me an email with a daily summary of my upcoming meetings, with a link to the full brief.
```

You'll see the assistant create a plan for building the agent, then starting to build each component step-by-step. The first draft should give you a working agent with a name, description, instructions, and a set of connected apps.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img1-v2.png" alt="Agent builder in progress" width="80%" />
</p>

If you don't have the required apps already configured, the agent builder will walk you through the configuration steps. If an app is unavailable, you can adjust scope - for example if you don't have Slack enabled, you can instruct your agent to send you an email with your sales meeting doc instead.

### 2. Review and configure your apps

Now we'll review the configurations of our apps. Because our agent can access external tools, it's important to understand the permissions it has to take actions on these tools, and how those permissions change as we share our agent for other teammates to use.

Note that connector actions can be enforced at the workspace level by admins. For example, an admin can enforce that workspace agents can only take read actions, but not write actions, for the SharePoint connector.

We can click into each connector to view and change its permissions.

For the **Google Calendar** connection, we'll use *End-user account*. What this means is that each person who is using the agent will need to authenticate with their own google calendar, and the agent will access their individual meetings.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img2.png" alt="End-user auth for Google Calendar" width="60%" />
</p>

For Google Calendar, we just need to view upcoming meetings and attendees, so we'll only enable read actions. We can also enforce permissions more granularly, by selecting individual actions to enable or disable.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img3.png" alt="Read access for Google Calendar" width="60%" />
</p>

We'll also use the same *End-user account* configuration for the **Gmail** connector, since each agent user will get their own email briefing for their upcoming meetings.

For the **Microsoft SharePoint** connection, we'll use an *Agent-owned account* linked to a service account associated with a sales team. What this means is that regardless of who is using the agent, the agent will have access to the full set of SharePoint folders, files, and sites that are accessible to the team service account.

In this case, we want to be able to search through SharePoint for any documents relevant to a customer account, then create a new meeting prep document. So we'll scope the SharePoint connector permissions accordingly, to allow a broad set of read actions but prevent bulk write actions and prevent deletes.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img4.png" alt="Scoped permissions for SharePoint" width="60%" />
</p>

Aside from the connectors we've already enabled, the agent has access to **Web search** that it will use to enrich the meeting briefs with recent public company news from the last 30 days.

### 3. Enabling skills and memories for consistent, customized outputs

One of the benefits of using workspace agents is how easy it is to ensure **high-quality and consistent** outputs, and skills are an ideal way to help our agent follow the same workflow each time it generates a meeting prep document.

Skills package instructions, resources, and scripts to help our agent reliably complete its instructions. To equip our agent with a skill, we'll select "Add skill" in our agent view. We can upload a skill that we've already created (skills are built on the [open-source agent skills standard](https://agentskills.io/home) so you can use them across AI products), or we can use the built-in skill builder directly within ChatGPT workspace agents.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img5.png" alt="Creating a skill for our agent" width="336" />
</p>

Our assistant will read the meeting template and help us create a custom skill that matches the output format we want. To refine the skill, edit it directly in the agent builder or upload files it can use.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img6.png" alt="Editing a skill for our agent" width="60%" />
</p>

We'll also enable **Memory** for our agent. Memory enables the agent to maintain context across different agent sessions, by giving it access to a persistent folder where the agent can save notes, drafts, and outputs. In this case, we'll give the agent memory for previous runs of this agent so it knows per-user context.

Note that this memory is not shared across different end users of our agent. Users can view their memories from the agent page. For example, a user might give the agent guidance to ignore a certain meeting on its calendar that it doesn't need a meeting prep doc for, and the agent will be able to access that memory when following its instructions.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img7.png" alt="Giving our agent access to memory" width="60%" />
</p>

## Testing your agent

Before scheduling our agent to run on a periodic cadence, and before sharing it with other teammates, we can select **Preview** or **Try in ChatGPT** in the top-right corner of the agent builder to test our agent. We can also select **Create** to save our agent, and then invoke it by tagging it in our ChatGPT input box. Note that when you first create an agent, it is by default available only to you.

Note that our agent builder has automatically created some sample starter prompts that appear next to the agent in ChatGPT. To view and edit these prompts, we can select ChatGPT under "Channels" in the agent view.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img9.png" alt="Updating starter prompts" width="336" />
</p>

We'll ask our agent to prepare briefs for the meetings on our calendar for tomorrow, and we can view the traces of actions the agent is taking - accessing connectors, referencing skills and memories - as well as the agent's chain-of-thought reasoning as it completes its task.

When our agent completes, we see that it has generated polished SharePoint documents for each of our upcoming customer meetings and sent us an email summary.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img11.png" alt="Output email" width="80%" />
</p>

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img12.png" alt="Output meeting brief" width="80%" />
</p>

You can run additional tests with different input data - for example, you might ask the agent to prepare a brief for a meeting that you already had last week, to compare its output with a human-generated prep doc. You can also add that prep doc to the skill's files as an example. You can update agent instructions, provide it additional connectors and permissions, or update its skill to refine the output it produces.

## Deploying your agent

We'll first set our agent to run each day at 4pm, to give us a preview of the upcoming day. We'll select **Schedule** in the top-right of the agent screen and then **Add new schedule** to specify when the agent should run, and provide it any specific instructions.

For example, in addition to our daily weekday schedule, we might want to create a "weekly prep" schedule that runs each Sunday evening, and instruct our agent to prepare meeting briefs for each upcoming meeting this week.

<p align="center">
  <img src="https://cdn.openai.com/cookbook/chatgpt-agents-sales-meeting-prep/img10.png" alt="Creating a schedule" width="336" />
</p>

Now, we'll share our agent with our team. In the "Channels" section of the agent builder, we can select **ChatGPT** and then **Enable sharing**. (Note that your workspace admin will need to grant you permission to share agents you've created.)

We can turn on sharing to generate a shareable link for our agent, which lets anyone in your workspace either chat directly with your agent, or duplicate your agent to create their own forked version which they can edit individually. (You won't be able to access their duplicated agent, unless they choose to share it with you. Currently, multiple users cannot edit the same agent.)

Because we've selected *End-user account* for our Google Calendar and Gmail connectors, each person using our agent will need to log into these apps, and the agent will be able to access their specific meetings and email. However, because we've selected *Agent-owned account* for the SharePoint connector, **anyone we share the agent with will be able to access the SharePoint resources**.

In addition to providing our teammates with a link to our agent, we can also choose to list our agent in our company directory, allowing anyone in your workspace to view the agent. You can access your company directory of employee-built agents by selecting **Agents** from ChatGPT, and then selecting the agent directory tab.

---

## codex_exec_plans

- 官方原文：https://github.com/openai/openai-cookbook/blob/main/articles/codex_exec_plans.md
- 存档：`01-Raw/VibeCoding/openai/openai-cookbook-articles-codex-exec-plans-md.md`

# Using PLANS.md for multi-hour problem solving

Codex and the `gpt-5.2-codex` model (recommended) can be used to implement complex tasks that take significant time to research, design, and implement. The approach described here is one way to prompt the model to implement these tasks and to steer it towards successful completion of a project.

These plans are thorough design documents, and "living documents". As a user of Codex, you can use these documents to verify the approach that Codex will take before it begins a long implementation process. The particular `PLANS.md` included below is very similar to one that has enabled Codex to work for more than seven hours from a single prompt.

We enable Codex to use these documents by first updating `AGENTS.md` to describe when to use `PLANS.md`, and then of course, to add the `PLANS.md` file to our repository.

## `AGENTS.md`

[`AGENTS.md`](https://github.com/openai/agents.md) is a simple format for guiding coding agents such as Codex. We describe a term that users can use as a shorthand and a simple rule for when to use planning documents. Here, we call it an "ExecPlan". Note that this is an arbitrary term, Codex has not been trained on it. This shorthand can then be used when prompting Codex to direct it to a particular definition of a plan.

Here's an `AGENTS.md` section instructing an agent about when to use a plan:

```md
# ExecPlans

When writing complex features or significant refactors, use an ExecPlan (as described in .agent/PLANS.md) from design to implementation.
```

## `PLANS.md`

Below is the entire document. The prompting in this document was carefully chosen to provide significant amounts of feedback to users and to guide the model to implement precisely what a plan specifies. Users may find that they benefit from customizing the file to meet their needs, or to add or remove required sections.

~~~md
# Codex Execution Plans (ExecPlans):

This document describes the requirements for an execution plan ("ExecPlan"), a design document that a coding agent can follow to deliver a working feature or system change. Treat the reader as a complete beginner to this repository: they have only the current working tree and the single ExecPlan file you provide. There is no memory of prior plans and no external context.

## How to use ExecPlans and PLANS.md

When authoring an executable specification (ExecPlan), follow PLANS.md _to the letter_. If it is not in your context, refresh your memory by reading the entire PLANS.md file. Be thorough in reading (and re-reading) source material to produce an accurate specification. When creating a spec, start from the skeleton and flesh it out as you do your research.

When implementing an executable specification (ExecPlan), do not prompt the user for "next steps"; simply proceed to the next milestone. Keep all sections up to date, add or split entries in the list at every stopping point to affirmatively state the progress made and next steps. Resolve ambiguities autonomously, and commit frequently.

When discussing an executable specification (ExecPlan), record decisions in a log in the spec for posterity; it should be unambiguously clear why any change to the specification was made. ExecPlans are living documents, and it should always be possible to restart from _only_ the ExecPlan and no other work.

When researching a design with challenging requirements or significant unknowns, use milestones to implement proof of concepts, "toy implementations", etc., that allow validating whether the user's proposal is feasible. Read the source code of libraries by finding or acquiring them, research deeply, and include prototypes to guide a fuller implementation.

## Requirements

NON-NEGOTIABLE REQUIREMENTS:

* Every ExecPlan must be fully self-contained. Self-contained means that in its current form it contains all knowledge and instructions needed for a novice to succeed.
* Every ExecPlan is a living document. Contributors are required to revise it as progress is made, as discoveries occur, and as design decisions are finalized. Each revision must remain fully self-contained.
* Every ExecPlan must enable a complete novice to implement the feature end-to-end without prior knowledge of this repo.
* Every ExecPlan must produce a demonstrably working behavior, not merely code changes to "meet a definition".
* Every ExecPlan must define every term of art in plain language or do not use it.

Purpose and intent come first. Begin by explaining, in a few sentences, why the work matters from a user's perspective: what someone can do after this change that they could not do before, and how to see it working. Then guide the reader through the exact steps to achieve that outcome, including what to edit, what to run, and what they should observe.

The agent executing your plan can list files, read files, search, run the project, and run tests. It does not know any prior context and cannot infer what you meant from earlier milestones. Repeat any assumption you rely on. Do not point to external blogs or docs; if knowledge is required, embed it in the plan itself in your own words. If an ExecPlan builds upon a prior ExecPlan and that file is checked in, incorporate it by reference. If it is not, you must include all relevant context from that plan.

## Formatting

Format and envelope are simple and strict. Each ExecPlan must be one single fenced code block labeled as `md` that begins and ends with triple backticks. Do not nest additional triple-backtick code fences inside; when you need to show commands, transcripts, diffs, or code, present them as indented blocks within that single fence. Use indentation for clarity rather than code fences inside an ExecPlan to avoid prematurely closing the ExecPlan's code fence. Use two newlines after every heading, use # and ## and so on, and correct syntax for ordered and unordered lists.

When writing an ExecPlan to a Markdown (.md) file where the content of the file *is only* the single ExecPlan, you should omit the triple backticks.

Write in plain prose. Prefer sentences over lists. Avoid checklists, tables, and long enumerations unless brevity would obscure meaning. Checklists are permitted only in the `Progress` section, where they are mandatory. Narrative sections must remain prose-first.

## Guidelines

Self-containment and plain language are paramount. If you introduce a phrase that is not ordinary English ("daemon", "middleware", "RPC gateway", "filter graph"), define it immediately and remind the reader how it manifests in this repository (for example, by naming the files or commands where it appears). Do not say "as defined previously" or "according to the architecture doc." Include the needed explanation here, even if you repeat yourself.

Avoid common failure modes. Do not rely on undefined jargon. Do not describe "the letter of a feature" so narrowly that the resulting code compiles but does nothing meaningful. Do not outsource key decisions to the reader. When ambiguity exists, resolve it in the plan itself and explain why you chose that path. Err on the side of over-explaining user-visible effects and under-specifying incidental implementation details.

Anchor the plan with observable outcomes. State what the user can do after implementation, the commands to run, and the outputs they should see. Acceptance should be phrased as behavior a human can verify ("after starting the server, navigating to [http://localhost:8080/health](http://localhost:8080/health) returns HTTP 200 with body OK") rather than internal attributes ("added a HealthCheck struct"). If a change is internal, explain how its impact can still be demonstrated (for example, by running tests that fail before and pass after, and by showing a scenario that uses the new behavior).

Specify repository context explicitly. Name files with full repository-relative paths, name functions and modules precisely, and describe where new files should be created. If touching multiple areas, include a short orientation paragraph that explains how those parts fit together so a novice can navigate confidently. When running commands, show the working directory and exact command line. When outcomes depend on environment, state the assumptions and provide alternatives when reasonable.

Be idempotent and safe. Write the steps so they can be run multiple times without causing damage or drift. If a step can fail halfway, include how to retry or adapt. If a migration or destructive operation is necessary, spell out backups or safe fallbacks. Prefer additive, testable changes that can be validated as you go.

Validation is not optional. Include instructions to run tests, to start the system if applicable, and to observe it doing something useful. Describe comprehensive testing for any new features or capabilities. Include expected outputs and error messages so a novice can tell success from failure. Where possible, show how to prove that the change is effective beyond compilation (for example, through a small end-to-end scenario, a CLI invocation, or an HTTP request/response transcript). State the exact test commands appropriate to the project’s toolchain and how to interpret their results.

Capture evidence. When your steps produce terminal output, short diffs, or logs, include them inside the single fenced block as indented examples. Keep them concise and focused on what proves success. If you need to include a patch, prefer file-scoped diffs or small excerpts that a reader can recreate by following your instructions rather than pasting large blobs.

## Milestones

Milestones are narrative, not bureaucracy. If you break the work into milestones, introduce each with a brief paragraph that describes the scope, what will exist at the end of the milestone that did not exist before, the commands to run, and the acceptance you expect to observe. Keep it readable as a story: goal, work, result, proof. Progress and milestones are distinct: milestones tell the story, progress tracks granular work. Both must exist. Never abbreviate a milestone merely for the sake of brevity, do not leave out details that could be crucial to a future implementation.

Each milestone must be independently verifiable and incrementally implement the overall goal of the execution plan.

## Living plans and design decisions

* ExecPlans are living documents. As you make key design decisions, update the plan to record both the decision and the thinking behind it. Record all decisions in the `Decision Log` section.
* ExecPlans must contain and maintain a `Progress` section, a `Surprises & Discoveries` section, a `Decision Log`, and an `Outcomes & Retrospective` section. These are not optional.
* When you discover optimizer behavior, performance tradeoffs, unexpected bugs, or inverse/unapply semantics that shaped your approach, capture those observations in the `Surprises & Discoveries` section with short evidence snippets (test output is ideal).
* If you change course mid-implementation, document why in the `Decision Log` and reflect the implications in `Progress`. Plans are guides for the next contributor as much as checklists for you.
* At completion of a major task or the full plan, write an `Outcomes & Retrospective` entry summarizing what was achieved, what remains, and lessons learned.

# Prototyping milestones and parallel implementations

It is acceptable—-and often encouraged—-to include explicit prototyping milestones when they de-risk a larger change. Examples: adding a low-level operator to a dependency to validate feasibility, or exploring two composition orders while measuring optimizer effects. Keep prototypes additive and testable. Clearly label the scope as “prototyping”; describe how to run and observe results; and state the criteria for promoting or discarding the prototype.

Prefer additive code changes followed by subtractions that keep tests passing. Parallel implementations (e.g., keeping an adapter alongside an older path during migration) are fine when they reduce risk or enable tests to continue passing during a large migration. Describe how to validate both paths and how to retire one safely with tests. When working with multiple new libraries or feature areas, consider creating spikes that evaluate the feasibility of these features _independently_ of one another, proving that the external library performs as expected and implements the features we need in isolation.

## Skeleton of a Good ExecPlan

    # <Short, action-oriented description>

    This ExecPlan is a living document. The sections `Progress`, `Surprises & Discoveries`, `Decision Log`, and `Outcomes & Retrospective` must be kept up to date as work proceeds.

    If PLANS.md file is checked into the repo, reference the path to that file here from the repository root and note that this document must be maintained in accordance with PLANS.md.

    ## Purpose / Big Picture

    Explain in a few sentences what someone gains after this change and how they can see it working. State the user-visible behavior you will enable.

    ## Progress

    Use a list with checkboxes to summarize granular steps. Every stopping point must be documented here, even if it requires splitting a partially completed task into two (“done” vs. “remaining”). This section must always reflect the actual current state of the work.

    - [x] (2025-10-01 13:00Z) Example completed step.
    - [ ] Example incomplete step.
    - [ ] Example partially completed step (completed: X; remaining: Y).

    Use timestamps to measure rates of progress.

    ## Surprises & Discoveries

    Document unexpected behaviors, bugs, optimizations, or insights discovered during implementation. Provide concise evidence.

    - Observation: …
      Evidence: …

    ## Decision Log

    Record every decision made while working on the plan in the format:

    - Decision: …
      Rationale: …
      Date/Author: …

    ## Outcomes & Retrospective

    Summarize outcomes, gaps, and lessons learned at major milestones or at completion. Compare the result against the original purpose.

    ## Context and Orientation

    Describe the current state relevant to this task as if the reader knows nothing. Name the key files and modules by full path. Define any non-obvious term you will use. Do not refer to prior plans.

    ## Plan of Work

    Describe, in prose, the sequence of edits and additions. For each edit, name the file and location (function, module) and what to insert or change. Keep it concrete and minimal.

    ## Concrete Steps

    State the exact commands to run and where to run them (working directory). When a command generates output, show a short expected transcript so the reader can compare. This section must be updated as work proceeds.

    ## Validation and Acceptance

    Describe how to start or exercise the system and what to observe. Phrase acceptance as behavior, with specific inputs and outputs. If tests are involved, say "run <project’s test command> and expect <N> passed; the new test <name> fails before the change and passes after>".

    ## Idempotence and Recovery

    If steps can be repeated safely, say so. If a step is risky, provide a safe retry or rollback path. Keep the environment clean after completion.

    ## Artifacts and Notes

    Include the most important transcripts, diffs, or snippets as indented examples. Keep them concise and focused on what proves success.

    ## Interfaces and Dependencies

    Be prescriptive. Name the libraries, modules, and services to use and why. Specify the types, traits/interfaces, and function signatures that must exist at the end of the milestone. Prefer stable names and paths such as `crate::module::function` or `package.submodule.Interface`. E.g.:

    In crates/foo/planner.rs, define:

        pub trait Planner {
            fn plan(&self, observed: &Observed) -> Vec<Action>;
        }

If you follow the guidance above, a single, stateless agent -- or a human novice -- can read your ExecPlan from top to bottom and produce a working, observable result. That is the bar: SELF-CONTAINED, SELF-SUFFICIENT, NOVICE-GUIDING, OUTCOME-FOCUSED.

When you revise a plan, you must ensure your changes are comprehensively reflected across all sections, including the living document sections, and you must write a note at the bottom of the plan describing the change and the reason why. ExecPlans must describe not just the what but the why for almost everything.
~~~

---

## how_to_work_with_large_language_models

- 官方原文：https://github.com/openai/openai-cookbook/blob/main/articles/how_to_work_with_large_language_models.md
- 存档：`01-Raw/VibeCoding/openai/openai-cookbook-articles-how-to-work-with-large-language-models-md.md`

# How to work with large language models

## How large language models work

[Large language models][Large language models Blog Post] are functions that map text to text. Given an input string of text, a large language model predicts the text that should come next.

The magic of large language models is that by being trained to minimize this prediction error over vast quantities of text, the models end up learning concepts useful for these predictions. For example, they learn:

- how to spell
- how grammar works
- how to paraphrase
- how to answer questions
- how to hold a conversation
- how to write in many languages
- how to code
- etc.

They do this by “reading” a large amount of existing text and learning how words tend to appear in context with other words, and uses what it has learned to predict the next most likely word that might appear in response to a user request, and each subsequent word after that.

GPT-3 and GPT-4 power [many software products][OpenAI Customer Stories], including productivity apps, education apps, games, and more.

## How to control a large language model

Of all the inputs to a large language model, by far the most influential is the text prompt.

Large language models can be prompted to produce output in a few ways:

- **Instruction**: Tell the model what you want
- **Completion**: Induce the model to complete the beginning of what you want
- **Scenario**: Give the model a situation to play out
- **Demonstration**: Show the model what you want, with either:
  - A few examples in the prompt
  - Many hundreds or thousands of examples in a fine-tuning training dataset

An example of each is shown below.

### Instruction prompts

Write your instruction at the top of the prompt (or at the bottom, or both), and the model will do its best to follow the instruction and then stop. Instructions can be detailed, so don't be afraid to write a paragraph explicitly detailing the output you want, just stay aware of how many [tokens](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) the model can process.

Example instruction prompt:

```text
Extract the name of the author from the quotation below.

“Some humans theorize that intelligent species go extinct before they can expand into outer space. If they're correct, then the hush of the night sky is the silence of the graveyard.”
― Ted Chiang, Exhalation
```

Output:

```text
Ted Chiang
```

### Completion prompt example

Completion-style prompts take advantage of how large language models try to write text they think is most likely to come next. To steer the model, try beginning a pattern or sentence that will be completed by the output you want to see. Relative to direct instructions, this mode of steering large language models can take more care and experimentation. In addition, the models won't necessarily know where to stop, so you will often need stop sequences or post-processing to cut off text generated beyond the desired output.

Example completion prompt:

```text
“Some humans theorize that intelligent species go extinct before they can expand into outer space. If they're correct, then the hush of the night sky is the silence of the graveyard.”
― Ted Chiang, Exhalation

The author of this quote is
```

Output:

```text
 Ted Chiang
```

### Scenario prompt example

Giving the model a scenario to follow or role to play out can be helpful for complex queries or when seeking imaginative responses. When using a hypothetical prompt, you set up a situation, problem, or story, and then ask the model to respond as if it were a character in that scenario or an expert on the topic.

Example scenario prompt:

```text
Your role is to extract the name of the author from any given text

“Some humans theorize that intelligent species go extinct before they can expand into outer space. If they're correct, then the hush of the night sky is the silence of the graveyard.”
― Ted Chiang, Exhalation
```

Output:

```text
 Ted Chiang
```

### Demonstration prompt example (few-shot learning)

Similar to completion-style prompts, demonstrations can show the model what you want it to do. This approach is sometimes called few-shot learning, as the model learns from a few examples provided in the prompt.

Example demonstration prompt:

```text
Quote:
“When the reasoning mind is forced to confront the impossible again and again, it has no choice but to adapt.”
― N.K. Jemisin, The Fifth Season
Author: N.K. Jemisin

Quote:
“Some humans theorize that intelligent species go extinct before they can expand into outer space. If they're correct, then the hush of the night sky is the silence of the graveyard.”
― Ted Chiang, Exhalation
Author:
```

Output:

```text
 Ted Chiang
```

### Fine-tuned prompt example

With enough training examples, you can [fine-tune][Fine Tuning Docs] a custom model. In this case, instructions become unnecessary, as the model can learn the task from the training data provided. However, it can be helpful to include separator sequences (e.g., `->` or `###` or any string that doesn't commonly appear in your inputs) to tell the model when the prompt has ended and the output should begin. Without separator sequences, there is a risk that the model continues elaborating on the input text rather than starting on the answer you want to see.

Example fine-tuned prompt (for a model that has been custom trained on similar prompt-completion pairs):

```text
“Some humans theorize that intelligent species go extinct before they can expand into outer space. If they're correct, then the hush of the night sky is the silence of the graveyard.”
― Ted Chiang, Exhalation

###

```

Output:

```text
 Ted Chiang
```

## Code Capabilities

Large language models aren't only great at text - they can be great at code too. OpenAI's [GPT-4][GPT-4 and GPT-4 Turbo] model is a prime example.

GPT-4 powers [numerous innovative products][OpenAI Customer Stories], including:

- [GitHub Copilot] (autocompletes code in Visual Studio and other IDEs)
- [Replit](https://replit.com/) (can complete, explain, edit and generate code)
- [Cursor](https://cursor.sh/) (build software faster in an editor designed for pair-programming with AI)

GPT-4 is more advanced than previous models like `gpt-3.5-turbo-instruct`. But, to get the best out of GPT-4 for coding tasks, it's still important to give clear and specific instructions. As a result, designing good prompts can take more care.

### More prompt advice

For more prompt examples, visit [OpenAI Examples][OpenAI Examples].

In general, the input prompt is the best lever for improving model outputs. You can try tricks like:

- **Be more specific** E.g., if you want the output to be a comma separated list, ask it to return a comma separated list. If you want it to say "I don't know" when it doesn't know the answer, tell it 'Say "I don't know" if you do not know the answer.' The more specific your instructions, the better the model can respond.
- **Provide Context**: Help the model understand the bigger picture of your request. This could be background information, examples/demonstrations of what you want or explaining the purpose of your task.
- **Ask the model to answer as if it was an expert.** Explicitly asking the model to produce high quality output or output as if it was written by an expert can induce the model to give higher quality answers that it thinks an expert would write. Phrases like "Explain in detail" or "Describe step-by-step" can be effective.
- **Prompt the model to write down the series of steps explaining its reasoning.** If understanding the 'why' behind an answer is important, prompt the model to include its reasoning. This can be done by simply adding a line like "[Let's think step by step](https://arxiv.org/abs/2205.11916)" before each answer.

[Fine Tuning Docs]: https://platform.openai.com/docs/guides/fine-tuning
[OpenAI Customer Stories]: https://openai.com/customer-stories
[Large language models Blog Post]: https://openai.com/research/better-language-models
[GitHub Copilot]: https://github.com/features/copilot/
[GPT-4 and GPT-4 Turbo]: https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
[GPT3 Apps Blog Post]: https://openai.com/blog/gpt-3-apps/
[OpenAI Examples]: https://platform.openai.com/examples

---

## techniques_to_improve_reliability

- 官方原文：https://github.com/openai/openai-cookbook/blob/main/articles/techniques_to_improve_reliability.md
- 存档：`01-Raw/VibeCoding/openai/openai-cookbook-articles-techniques-to-improve-reliability-md.md`

# Techniques to improve reliability

When GPT-3 fails on a task, what should you do?

- Search for a better prompt that elicits more reliable answers?
- Invest in thousands of examples to fine-tune a custom model?
- Assume the model is incapable of the task, and move on?

There is no simple answer - it depends. However, if your task involves logical reasoning or complexity, consider trying the techniques in this article to build more reliable, high-performing prompts.

## Why GPT-3 fails on complex tasks

If you were asked to multiply 13 by 17, would the answer pop immediately into your mind? For most of us, probably not. Yet, that doesn't mean humans are incapable of two-digit multiplication. With a few seconds, and some pen and paper, it's not too taxing to work out that 13 x 17 = 130 + 70 + 21 = 221.

Similarly, if you give GPT-3 a task that's too complex to do in the time it takes to calculate its next token, it may confabulate an incorrect guess. Yet, akin to humans, that doesn't necessarily mean the model is incapable of the task. With some time and space to reason things out, the model still may be able to answer reliably.

As an example, if you ask `gpt-3.5-turbo-instruct` the following math problem about juggling balls, it answers incorrectly:

```gpt-3.5-turbo-instruct
Q: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?
A:
```

```gpt-3.5-turbo-instruct
There are 8 blue golf balls.
```

Does this mean that GPT-3 cannot do simple math problems? No; in fact, it turns out that by prompting the model with `Let's think step by step`, the model solves the problem reliably:

```gpt-3.5-turbo-instruct
Q: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?
A: Let's think step by step.
```

```gpt-3.5-turbo-instruct
There are 16 balls in total.
Half of the balls are golf balls.
That means that there are 8 golf balls.
Half of the golf balls are blue.
That means that there are 4 blue golf balls.
```

Of course, it's hard to tell from only a single example whether this `Let's think step by step` trick actually works in general or just got lucky on this particular problem. But it really does work. On a benchmark of word math problems, the `Let's think step by step` trick raised GPT-3's solve rate massively, from a worthless 18% to a decent 79%!

## Model capabilities depend on context

When learning to work with GPT-3, one common conceptual mistake is to believe that its capabilities are fixed across all contexts. E.g., if GPT-3 gets a simple logic question wrong, then it must be incapable of simple logic.

But as the `Let's think step by step` example illustrates, apparent failures of GPT-3 can sometimes be remedied with a better prompt that helps the model steer itself toward the correct output.

## How to improve reliability on complex tasks

The rest of this article shares techniques for improving reliability of large language models on complex tasks. Although some of the techniques are specific to certain types of problems, many of them are built upon general principles that can be applied to a wide range of tasks, e.g.:

- Give clearer instructions
- Split complex tasks into simpler subtasks
- Structure the instruction to keep the model on task
- Prompt the model to explain before answering
- Ask for justifications of many possible answers, and then synthesize
- Generate many outputs, and then use the model to pick the best one
- Fine-tune custom models to maximize performance

## Split complex tasks into simpler tasks

One way to give a model more time and space to think is to break tasks into simpler pieces.

As an example, consider a task where we ask the model a multiple-choice question about some text - in this case, a game of Clue. When asked directly, `gpt-3.5-turbo-instruct` isn't able to put clues 3 & 5 together, and answers incorrectly:

```gpt-3.5-turbo-instruct
Use the following clues to answer the following multiple-choice question.

Clues:
1. Miss Scarlett was the only person in the lounge.
2. The person with the pipe was in the kitchen.
3. Colonel Mustard was the only person in the observatory.
4. Professor Plum was not in the library nor the billiard room.
5. The person with the candlestick was in the observatory.

Question: Was Colonel Mustard in the observatory with the candlestick?
(a) Yes; Colonel Mustard was in the observatory with the candlestick
(b) No; Colonel Mustard was not in the observatory with the candlestick
(c) Unknown; there is not enough information to determine whether Colonel Mustard was in the observatory with the candlestick

Solution:
```

```gpt-3.5-turbo-instruct
(c) Unknown; there is not enough information to determine whether Colonel Mustard was in the observatory with the candlestick
```

Although clues 3 and 5 establish that Colonel Mustard was the only person in the observatory and that the person in the observatory had the candlestick, the model fails to combine them into a correct answer of (a) Yes.

However, instead of asking for the answer directly, we can split the task into three pieces:

- First, go through the clues one by one and consider whether the clue is potentially relevant
- Second, combine the relevant clues to reason out the answer to the question
- Third, write the final answer: either (a), (b), or (c)

```gpt-3.5-turbo-instruct
Use the following clues to answer the following multiple-choice question, using the following procedure:
(1) First, go through the clues one by one and consider whether the clue is potentially relevant
(2) Second, combine the relevant clues to reason out the answer to the question
(3) Third, map the answer to one of the multiple choice answers: either (a), (b), or (c)

Clues:
1. Miss Scarlett was the only person in the lounge.
2. The person with the pipe was in the kitchen.
3. Colonel Mustard was the only person in the observatory.
4. Professor Plum was not in the library nor the billiard room.
5. The person with the candlestick was in the observatory.

Question: Was Colonel Mustard in the observatory with the candlestick?
(a) Yes; Colonel Mustard was in the observatory with the candlestick
(b) No; Colonel Mustard was not in the observatory with the candlestick
(c) Unknown; there is not enough information to determine whether Colonel Mustard was in the observatory with the candlestick

Solution:
(1) First, go through the clues one by one and consider whether the clue is potentially relevant:
```

```gpt-3.5-turbo-instruct
Clue 1: Miss Scarlett was the only person in the lounge. This clue is not relevant.
Clue 2: The person with the pipe was in the kitchen. This clue is not relevant.
Clue 3: Colonel Mustard was the only person in the observatory. This clue is relevant.
Clue 4: Professor Plum was not in the library nor the billiard room. This clue is not relevant.
Clue 5: The person with the candlestick was in the observatory. This clue is relevant.

(2) Second, combine the relevant clues to reason out the answer to the question:
Clue 3 and Clue 5 both say that the person with the candlestick was in the observatory. Colonel Mustard was the only person in the observatory, so Colonel Mustard was the person with the candlestick.

(3) Third, write the final answer:
(a) Yes; Colonel Mustard was in the observatory with the candlestick
```

By giving the model more time and space to think, and guiding it along a reasoning plan, it's able to figure out the correct answer of (a) Yes.

Another benefit of splitting complex instructions into smaller subtasks is that it can help keep the model focused on each subtask.

For example, if we ask `gpt-3.5-turbo-instruct` to summarize a text in its original language, the model can lapse back into English:

```gpt-3.5-turbo-instruct
Summarize the text using the original language of the text. The summary should be one sentence long.

Text:
"""
La estadística (la forma femenina del término alemán Statistik, derivado a su vez del italiano statista, "hombre de Estado")​ es una ciencia que estudia la variabilidad, colección, organización, análisis, interpretación, y presentación de los datos, así como el proceso aleatorio que los genera siguiendo las leyes de la probabilidad.​ La estadística es una ciencia formal deductiva, con un conocimiento propio, dinámico y en continuo desarrollo obtenido a través del método científico formal. En ocasiones, las ciencias fácticas necesitan utilizar técnicas estadísticas durante su proceso de investigación factual, con el fin de obtener nuevos conocimientos basados en la experimentación y en la observación. En estos casos, la aplicación de la estadística permite el análisis de datos provenientes de una muestra representativa, que busca explicar las correlaciones y dependencias de un fenómeno físico o natural, de ocurrencia en forma aleatoria o condicional.
"""

Summary:
```

```gpt-3.5-turbo-instruct
The text explains that statistics is a science that studies the variability, collection, organization, analysis, interpretation, and presentation of data, as well as the random process that generates them following the laws of probability.
```

However, if we first ask the model to identify the language of the text, and then summarize the text, it becomes more reliable:

```gpt-3.5-turbo-instruct
First, identify the language of the text. Second, summarize the text using the original language of the text. The summary should be one sentence long.

Text:
"""
La estadística (la forma femenina del término alemán Statistik, derivado a su vez del italiano statista, "hombre de Estado")​ es una ciencia que estudia la variabilidad, colección, organización, análisis, interpretación, y presentación de los datos, así como el proceso aleatorio que los genera siguiendo las leyes de la probabilidad.​ La estadística es una ciencia formal deductiva, con un conocimiento propio, dinámico y en continuo desarrollo obtenido a través del método científico formal. En ocasiones, las ciencias fácticas necesitan utilizar técnicas estadísticas durante su proceso de investigación factual, con el fin de obtener nuevos conocimientos basados en la experimentación y en la observación. En estos casos, la aplicación de la estadística permite el análisis de datos provenientes de una muestra representativa, que busca explicar las correlaciones y dependencias de un fenómeno físico o natural, de ocurrencia en forma aleatoria o condicional.
"""

Language:
```

```gpt-3.5-turbo-instruct
Spanish

La estadística es una ciencia que estudia la variabilidad, colección, organización, análisis, interpretación, y presentación de los datos, así como el proceso aleatorio que los genera siguiendo las leyes de la probabilidad.
```

## Prompt the model to explain before answering

Another powerful technique for improving the reliability of answers is to prompt the model to gradually reason out the answer rather than jumping immediately to the final answer. By 'thinking aloud' the model can be far more likely to arrive at the correct answer.

### Zero-shot

#### Method

Published by [Takeshi Kojima et al. in 2022](https://arxiv.org/abs/2205.11916), the easiest way to prompt a model to reason out the answer is to simply prepend answers with `Let's think step by step.` Figure 2 illustrates an example:

[![zero-shot reasoning example](/images/zero-shot_reasoners_fig2.png)
<br>Source: _Large Language Models are Zero-Shot Reasoners_ by Takeshi Kojima et al. (2022).](https://arxiv.org/abs/2205.11916)

#### Results

Applying this simple trick to the MultiArith math dataset, the authors found `Let's think step by step` quadrupled the accuracy, from 18% to 79%!

[![zero-shot reasoning example](/images/zero-shot_reasoners_tab5.png)
<br>Source: _Large Language Models are Zero-Shot Reasoners_ by Takeshi Kojima et al. (2022).](https://arxiv.org/abs/2205.11916)

#### Implications

Although the `Let's think step by step` trick works well on math problems, it's not effective on all tasks. The authors found that it was most helpful for multi-step arithmetic problems, symbolic reasoning problems, strategy problems, and other reasoning problems. It didn't help with simple math problems or common sense questions, and presumably wouldn't help with many other non-reasoning tasks either.

[![zero-shot reasoning example](/images/zero-shot_reasoners_tab1.png)
<br>Source: _Large Language Models are Zero-Shot Reasoners_ by Takeshi Kojima et al. (2022).](https://arxiv.org/abs/2205.11916)

To learn more, read the [full paper](https://arxiv.org/abs/2205.11916).

If you apply this technique to your own tasks, don't be afraid to experiment with customizing the instruction. `Let's think step by step` is rather generic, so you may find better performance with instructions that hew to a stricter format customized to your use case. For example, you can try more structured variants like `First, think step by step about why X might be true. Second, think step by step about why Y might be true. Third, think step by step about whether X or Y makes more sense.`. And you can even give the model an example format to help keep it on track, e.g.:

```gpt-3.5-turbo-instruct
Using the IRS guidance below, answer the following questions using this format:
(1) For each criterion, determine whether it is met by the vehicle purchase
- {Criterion} Let's think step by step. {explanation} {yes or no, or if the question does not apply then N/A}.
(2) After considering each criterion in turn, phrase the final answer as "Because of {reasons}, the answer is likely {yes or no}."

IRS guidance:
"""
You may be eligible for a federal tax credit under Section 30D if you purchased a car or truck that meets the following criteria:
- Does the vehicle have at least four wheels?
- Does the vehicle weigh less than 14,000 pounds?
- Does the vehicle draw energy from a battery with at least 4 kilowatt hours that may be recharged from an external source?
- Was the vehicle purchased in a year before 2022?
  - If so, has the manufacturer sold less than 200,000 qualifying vehicles? (Tesla and GM have sold more than 200,000 qualifying vehicles.)
- Was the vehicle purchased in a year after 2022?
  - If so, is the vehicle present in the following list of North American-assembled vehicles? (The only electric vehicles assembled in North America are the Audi Q5, BMW 330e, BMW X5, Chevrolet Bolt EUV, Chevrolet Bolt EV, Chrysler Pacifica PHEV, Ford Escape PHEV, Ford F Series, Ford Mustang MACH E, Ford Transit Van, GMC Hummer Pickup, GMC Hummer SUV, Jeep Grand Cherokee PHEV, Jeep Wrangler PHEV, Lincoln Aviator PHEV, Lincoln Corsair Plug-in, Lucid Air, Nissan Leaf, Rivian EDV, Rivian R1S, Rivian R1T, Tesla Model 3, Tesla Model S, Tesla Model X, Tesla Model Y, Volvo S60, BMW 330e, Bolt EV, Cadillac Lyriq, Mercedes EQS SUV, and Nissan Leaf.)
"""

Question: Can I claim a federal tax credit for my Toyota Prius Prime bought in 2021?

Solution:

(1) For each criterion, determine whether it is met by the vehicle purchase
- Does the vehicle have at least four wheels? Let's think step by step.
```

```gpt-3.5-turbo-instruct
 The Toyota Prius Prime has four wheels, so the answer is yes.
- Does the vehicle weigh less than 14,000 pounds? Let's think step by step. The Toyota Prius Prime weighs less than 14,000 pounds, so the answer is yes.
- Does the vehicle draw energy from a battery with at least 4 kilowatt hours that may be recharged from an external source? Let's think step by step. The Toyota Prius Prime has a battery with at least 4 kilowatt hours that may be recharged from an external source, so the answer is yes.
- Was the vehicle purchased in a year before 2022? Let's think step by step. The Toyota Prius Prime was purchased in 2021, which is before 2022, so the answer is yes.
- Was the vehicle purchased in a year after 2022? N/A
- If so, is the vehicle present in the following list of North American-assembled vehicles? N/A

(2) After considering each criterion in turn, phrase the final answer as "Because of {reasons}, the answer is likely {yes or no}."

Because the Toyota Prius Prime meets all of the criteria for a federal tax credit, the answer is likely yes.
```

### Few-shot examples

#### Method

Prompting the model to reason out its answers can be done in many ways. One way is to demonstrate with a few examples ('few-shot'), as studied by [Jason Wei and Denny Zhou et al. from Google](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html). Here's an example few-shot chain-of-thought prompt:

[![chain of thought example](/images/chain_of_thought_fig1.png)
<br>Source: _Chain of Thought Prompting Elicits Reasoning in Large Language Models_ Jason Wei and Denny Zhou et al. (2022)](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

More demonstrations of reasoning chains written by human labelers:

[![chain of thought example](/images/chain_of_thought_fig3.png)
<br>Source: _Chain of Thought Prompting Elicits Reasoning in Large Language Models_ Jason Wei and Denny Zhou et al. (2022)](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

[(Note that it has been called into question whether pears actually float)](https://twitter.com/Meaningness/status/1561062170074370048?s=20&t=mpHt8f3RRboztXxdhLFnWQ)

#### Results

Testing on grade school math problems, the authors found that chain of thought prompting tripled the solve rate, from 18% to 57%.

[![chain of thought example](/images/chain_of_thought_fig5.png)
<br>Source: _Chain of Thought Prompting Elicits Reasoning in Large Language Models_ Jason Wei and Denny Zhou et al. (2022)](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

In addition to math problems, chain of thought prompting also lifted performance on questions related to sports understanding, coin flip tracking, and last letter concatenation. In most cases, not many examples were need to saturate the performance gains (less than 8 or so).

[![chain of thought example](/images/chain_of_thought_fig11.png)
<br>Source: _Chain of Thought Prompting Elicits Reasoning in Large Language Models_ Jason Wei and Denny Zhou et al. (2022)](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

To learn more, read the [full paper](https://arxiv.org/abs/2201.11903).

#### Implications

One advantage of the few-shot example-based approach relative to the `Let's think step by step` technique is that you can more easily specify the format, length, and style of reasoning that you want the model to perform before landing on its final answer. This can be particularly helpful in cases where the model isn't initially reasoning in the right way or depth.

### Fine-tuned

#### Method

In general, to eke out maximum performance on a task, you'll need to fine-tune a custom model. However, fine-tuning a model using explanations may take thousands of example explanations, which are costly to write.

In 2022, Eric Zelikman and Yuhuai Wu et al. published a clever procedure for using a few-shot prompt to generate a dataset of explanations that could be used to fine-tune a model. The idea is to use a few-shot prompt to generate candidate explanations, and only keep the explanations that produce the correct answer. Then, to get additional explanations for some of the incorrect answers, retry the few-shot prompt but with correct answers given as part of the question. The authors called their procedure STaR (Self-taught Reasoner):

[![STaR procedure](/images/star_fig1.png)
<br>Source: _STaR: Bootstrapping Reasoning With Reasoning_ by Eric Zelikman and Yujuai Wu et al. (2022)](https://arxiv.org/abs/2203.14465)

With this technique, you can combine the benefits of fine-tuning with the benefits of chain-of-thought prompting without needing to write thousands of example explanations.

#### Results

When the authors applied this technique to a Common Sense Q&A dataset, they found that STaR outperformed both chain-of-thought prompting alone (73% > 37%) and fine-tuning alone (73% > 60%):

[![STaR results](/images/star_tab1.png)
<br>Source: _STaR: Bootstrapping Reasoning With Reasoning_ by Eric Zelikman and Yujuai Wu et al. (2022)](https://arxiv.org/abs/2203.14465)

To learn more, read the [full paper](https://arxiv.org/abs/2203.14465).

#### Implications

Using a few-shot prompt to extend or modify a fine-tuning dataset is an idea that can be generalized beyond explanation writing. For example, if you have large quantities of unstructured text that you want to train on, you may find opportunities to use a prompt to extract a structured dataset from your unstructured text, and then fine-tune a custom model on that structured dataset.

## Extensions to chain-of-thought prompting

A number of extensions of chain-of-thought prompting have been published as well.

### Selection-inference prompting

#### Method

Published by Antonia Creswell et al., one extension of the chain-of-thought technique is to split the single prompt for generating explanations and answers into smaller parts. First, a prompt selects a relevant subset of facts from the text ('selection prompt'). Then, a second prompt infers a conclusion from the selected facts ('inference prompt'). These prompts are then alternated in a loop to generate multiple steps of reasoning and eventually land on a final answer. The authors illustrate the idea in the following figure:

[![Selection-inference prompting](/images/selection-inference_fig1.png)
<br>Source: _Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2205.09712)

#### Results

When applied to a 7B-parameter model, the authors found that selection-inference prompting substantially improved performance relative to chain-of-thought prompting on the bAbi and Proof Writer benchmark tasks (both of which require longer sequences of reasoning steps). The best performance they achieved combined both selection-inference prompting with fine-tuning.

[![Selection-inference prompting](/images/selection-inference_fig4.png)
<br>Source: _Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2205.09712)

#### Implications

Although the gains on these benchmarks were large, these benchmarks were specifically chosen because they required longer sequences of reasoning. On problems that don't require reasoning with many steps, the gains are likely smaller.

The results highlight a couple of general lessons for working with large language models. One, splitting up complex tasks into smaller tasks is a great way to improve reliability and performance; the more atomic the task, the less room there is for the model to err. Two, getting maximum performance often means combining fine-tuning with whatever approach you've chosen.

To learn more, read the [full paper](https://arxiv.org/abs/2205.09712).

### Faithful reasoning architecture

A few months after publishing the selection-inference prompting technique, the authors extended the technique in a follow-up paper, with ideas for:

- figuring out when the selection-inference cycle should stop or continue
- adding a value function to help search over multiple reasoning paths
- reducing hallucination of fake facts by fine-tuning a model to reason about sentence labels (e.g., sen1) rather than writing out the sentences themselves

#### Method

In the original selection-inference technique, specialized 'selection' and 'inference' prompts are alternated to select facts and make inferences from those facts, combining to generate a sequence of reasoning steps.

The authors extend this technique with two additional components.

First, the authors add a 'halter' model that, after each inference step, is asked whether the inferences thus far are sufficient to answer the question. If yes, then the model generates a final answer.

The halter models brings a couple of advantages:

- it can tell the selection-inference process to stop or keep going, as necessary.
- if the process never halts, you'll get no answer, which is often preferable to a hallucinated guess

[![Faithful reasoning](/images/faithful-reasoning_fig3.png)
<br>Source: _Faithful Reasoning Using Large Language Models_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2208.14271)

[![Faithful reasoning](/images/faithful-reasoning_fig5.png)
<br>Source: _Faithful Reasoning Using Large Language Models_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2208.14271)

Second, the authors add a value function, which is used to assess the quality of reasoning steps and search over multiple reasoning trajectories. This echoes a common theme for increasing reliability; instead of generating a single answer from the model, generate a set of answers and then use some type of value function / discriminator / verifier model to pick the best one.

[![Faithful reasoning](/images/faithful-reasoning_fig7.png)
<br>Source: _Faithful Reasoning Using Large Language Models_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2208.14271)

In addition to these two extensions, the authors also use a trick to reduce hallucination of fake facts. Rather than asking the model to write out factual sentences, they fine-tune a model to work with sentence labels (e.g., sen1) instead. This helps prevent the model from hallucinating fake facts not mentioned in the prompt context.

[![Faithful reasoning](/images/faithful-reasoning_fig4.png)
<br>Source: _Faithful Reasoning Using Large Language Models_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2208.14271)

#### Results

The authors evaluated their technique on two benchmarks: the ProofWriter task (not shown) and [EntailmentBankQA](https://allenai.org/data/entailmentbank) (shown). The technique increased accuracy substantially, especially on harder reasoning problems.

<br>Source: _Faithful Reasoning Using Large Language Models_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2208.14271)

In addition, their sentence label manipulation trick essentially eliminated hallucination!

<br>Source: _Faithful Reasoning Using Large Language Models_ by Antonia Creswell et al. (2022)](https://arxiv.org/abs/2208.14271)

#### Implications

This paper illustrates a number of helpful lessons for improving the reliability of large language models:

- Split complex tasks into smaller, more reliable subtasks
- Generate your answer in a step-by-step fashion, evaluating it along the way
- Generate many possible answers and use another model or function to pick the ones that look best
- Reduce hallucination by constraining what the model can say (e.g., by using sentence labels instead of sentences)
- Maximize performance of models by fine-tuning them on specialized tasks

To learn more, read the [full paper](https://arxiv.org/abs/2205.09712).

### Least-to-most prompting

In addition to doing poorly on long reasoning chains (where selection-inference shines), chain-of-thought prompting can especially struggle when the examples are short but the task is long.

#### Method

Least-to-most prompting is another technique that splits up reasoning tasks into smaller, more reliable subtasks. The idea is to elicit a subtask from the model by prompting it with something like `To solve {question}, we need to first solve: "`. Then, with that subtask in hand, the model can generate a solution. The solution is appended to the original question and the process is repeated until a final answer is produced.

[![Least-to-most prompting](/images/least-to-most_fig1.png)
<br>Source: _Least-to-most Prompting Enables Complex Reasoning in Large Language Models_ by Denny Zhou et al. (2022)](https://arxiv.org/abs/2205.10625)

#### Results

When applied to benchmarks involving long reasoning chains using `code-davinci-002` (which is optimized for code but can still understand text), the authors measured gains as large as 16% -> 99.7%!

[
<br>Source: _Least-to-most Prompting Enables Complex Reasoning in Large Language Models_ by Denny Zhou et al. (2022)](https://arxiv.org/abs/2205.10625)

#### Implications

Although the above gains from least-to-most prompting are impressive, they are measured on a very narrow set of tasks that require long reasoning chains.

Still, they illustrate a common theme: increase reliability by (a) breaking complex tasks into smaller subtasks and (b) giving the model more time and space to work out the answer.

To learn more, read the [full paper](https://arxiv.org/abs/2205.10625).

## Related ideas

### Maieutic prompting

#### Method

In contrast to the previous techniques, which try to maximize the likelihood of correct answers, another approach is to use GPT-3 to generate a tree of possible explanations (both correct _and incorrect_), and then analyze their relationships to guess at which set is correct. This technique was coined maieutic prompting by [Jaehun Jung et al. in May 2022](https://arxiv.org/abs/2205.11822) (maieutic means relating to the Socratic method of asking questions to elicit ideas).

The method is complicated, and works as follows:

- First, build a maieutic tree, where each node is a statement that could be true or false:
  - Start with a multiple-choice question or true/false statement (e.g. `War cannot have a tie`)
  - For each possible answer to the question, use the model to generate a corresponding explanation (with a prompt like `War cannot have a tie? True, because`)
  - Then, prompt the model with the question and the generated explanation, and ask it to produce the answer. If reversing the explanation (with a prefix like `It is wrong to say that {explanation}`) reverses the answer, then the explanation is considered 'logically integral.'
  - If an explanation is not logically integral, then repeat the above process recursively, with each explanation turned into a True or False question, and generate more explanations for each new question.
  - After all of the recursive explaining is done, you end up with a tree of explanations, where each leaf on the tree has the property that reversing the explanation reverses the model's answer.
- Second, convert the tree into a graph of relations:
  - For each node in the tree, calculate the model's relative belief in each node (inferred from the probability of getting an answer of `True` to given an explanation)
  - For each pair of nodes in the tree, use the model to identify whether they are entailed (implied) or contradicted
- Third, find the most consistent set of beliefs and take those to be true:
  - Specifically, using the strength of belief in each node and the logical relationships between them, formulate the problem as a weighted maximum satisfiability problem (MAX-SAT)
  - Use a solver to the find the most self-consistent set of beliefs, and take those as true

[
<br>Source: _Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations_ by Jaehun Jung et al. (2022)](https://arxiv.org/abs/2205.11822)

#### Results

[![Maieutic prompting results](/images/maieutic_tab1.png)
<br>Source: _Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations_ by Jaehun Jung et al. (2022)](https://arxiv.org/abs/2205.11822)

#### Implications

Beyond the complexity, one limitation of this method is that it appears to only apply to questions that can be posed as multiple-choice.

To learn more, read the [full paper](https://arxiv.org/abs/2205.11822).

## Extensions

### Self-consistency

#### Method

For tasks with a discrete set of answers, one simple way to improve reliability is to sample multiple explanations & answers from the model (using a positive temperature) and then pick the final answer that appears most often.

[![Self-consistency method](/images/self-consistency_fig1.png)
<br>Source: _Self-Consistency Improves Chain of Thought Reasoning in Language Models_ by Xuezhi Wang et al. (2022)](https://arxiv.org/abs/2203.11171)

#### Results

This technique lifted accuracies by anywhere from 1 to 24 percentage points on a suite of math and reasoning benchmarks. (Plotted below are results from Google's LaMDA model; using Google's larger PaLM model, the baselines were higher but the gains were a bit smaller.)

[![Self-consistency results](/images/self-consistency_fig3.png)
<br>Source: _Self-Consistency Improves Chain of Thought Reasoning in Language Models_ by Xuezhi Wang et al. (2022)](https://arxiv.org/abs/2203.11171)

#### Implications

Although this technique is simple to implement, it can be costly. Generating a set of 10 answers will increase your costs by 10x.

Also, as with many of these techniques, it applies only to tasks with a limited set of answers. For open-ended tasks where each answer is unique (such as writing a poem), it's not obvious what it would mean to pick the most common answer.

Lastly, this technique ought to be most beneficial when there are multiple paths or phrasings to reach an answer; if there's only one path, then the technique may not help at all. An extreme example: If the task was to generate a single token answer, then taking the most common token from 100 generations would be no different than taking the token with the highest logprobs (which you can get with a single generation at temperature=0).

### Verifiers

Another key technique for improving task performance is to train a verifier or discriminator model to evaluate the outputs of the main generative model. If the discriminator rejects the output, then you can resample the generative model until you get an acceptable output. In many cases, it's easier to judge an answer than it is to create an answer, which helps explain the power of this method.

#### Method

In 2021, OpenAI researchers applied this technique to grade school math problems, using the following procedure:

- First, they fine-tuned a model on questions and solutions
- For each problem in the training set, they generated 100 solutions
- Each of those 100 solutions was automatically labeled as either correct or incorrect, based on whether the final answer was correct
- Using those solutions, with some labeled correct and some labeled incorrect, they fine-tuned a verifier model to classify whether a question and candidate solution was correct or incorrect
- Finally, at test time, the generative model creates 100 solutions to each problem, and the one with the highest score according to the verifier model is picked as the final answer

[![Verifier method](/images/verifiers_fig3.png)
<br>Source: _Training Verifiers to Solve Math Word Problems_ by Karl Cobbe et al. (2021)](https://arxiv.org/abs/2110.14168)

#### Results

With a 175B GPT-3 model and 8,000 training examples, this technique substantially lifted grade school math accuracy from ~33% to ~55%.

[![Verifier results](/images/verifiers_fig5.png)
<br>Source: _Training Verifiers to Solve Math Word Problems_ by Karl Cobbe et al. (2021)](https://arxiv.org/abs/2110.14168)

#### Implications

Similar to the self-consistency technique, this method can get expensive, as generating, say, 100 solutions per task will increase your costs by roughly ~100x.

## Theories of reliability

Although the techniques above vary in their approach, they all share the goal of improving reliability on complex tasks. Mainly they do this by:

- decomposing unreliable operations into smaller, more reliable operations (e.g., selection-inference prompting)
- using multiple steps or multiple relationships to make the system's reliability greater than any individual component (e.g., maieutic prompting)

### Probabilistic graphical models

This paradigm of trying to build a reliable system out of less reliable components is reminiscent of probabilistic programming, and many of the analysis techniques of that field can be applied to this one.

In the paper _Language Model Cascades_, David Dohan et al. interpret the above techniques in the paradigm of probabilistic graphical models:

#### Chain of thought prompting

[![graphical model of chain of thought prompting](/images/lm_cascades_fig1.png)
<br>Source: _Language Model Cascades_ by David Dohan et al. (2022)](https://arxiv.org/abs/2207.10342)

#### Fine-tuned chain of thought prompting / Self-taught reasoner

[![graphical model of fine-tuned chain of thought prompting](/images/lm_cascades_fig3.png)
<br>Source: _Language Model Cascades_ by David Dohan et al. (2022)](https://arxiv.org/abs/2207.10342)

#### Selection-inference prompting

[![graphical model of selection-inference prompting](/images/lm_cascades_fig4.png)
<br>Source: _Language Model Cascades_ by David Dohan et al. (2022)](https://arxiv.org/abs/2207.10342)

#### Verifiers

[![graphical model of verifiers](/images/lm_cascades_fig5.png)
<br>Source: _Language Model Cascades_ by David Dohan et al. (2022)](https://arxiv.org/abs/2207.10342)

#### Implications

Although formulating these techniques as probabilistic graphical models may not be immediately useful for solving any particular problem, the framework may be helpful in selecting, combining, and discovering new techniques.

## Closing thoughts

Research into large language models is very active and evolving rapidly. Not only do researchers continue to improve the models, they also continue to improve our understanding of how to best employ the models. To underscore the pace of these developments, note that all of the papers shared above were published within the past 12 months (as I write in Sep 2022).

In the future, expect better models and better techniques to be published. Even if the specific techniques here are eclipsed by future best practices, the general principles behind them will likely remain a key part of any expert user's toolkit.

## Bibliography

| Lesson                                                                                                                         | Paper                                                                                                                                     | Date     |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Break complex tasks into simpler subtasks (and consider exposing the intermediate outputs to users)                            | [AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts](https://arxiv.org/abs/2110.01691) | 2021 Oct |
| You can improve output by generating many candidates, and then picking the one that looks best                                 | [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168)                                                        | 2021 Oct |
| On reasoning tasks, models do better when they reason step-by-step before answering                                            | [Chain of Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)                                 | 2022 Jan |
| You can improve step-by-step reasoning by generating many explanation-answer outputs, and picking the most popular answer      | [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)                               | 2022 Mar |
| If you want to fine-tune a step-by-step reasoner, you can do it with multiple-choice question & answer data alone              | [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)                                                          | 2022 Mar |
| The step-by-step reasoning method works great even with zero examples                                                          | [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)                                                         | 2022 May |
| You can do better than step-by-step reasoning by alternating a ‘selection’ prompt and an ‘inference’ prompt                    | [Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning](https://arxiv.org/abs/2205.09712)             | 2022 May |
| On long reasoning problems, you can improve step-by-step reasoning by splitting the problem into pieces to solve incrementally | [Least-to-most Prompting Enables Complex Reasoning in Large Language Models](https://arxiv.org/abs/2205.10625)                            | 2022 May |
| You can have the model analyze both good and bogus explanations to figure out which set of explanations are most consistent    | [Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations](https://arxiv.org/abs/2205.11822)                        | 2022 May |
| You can think about these techniques in terms of probabilistic programming, where systems comprise unreliable components       | [Language Model Cascades](https://arxiv.org/abs/2207.10342)                                                                               | 2022 Jul |
| You can eliminate hallucination with sentence label manipulation, and you can reduce wrong answers with a 'halter' prompt      | [Faithful Reasoning Using Large Language Models](https://arxiv.org/abs/2208.14271)                                                        | 2022 Aug |

---

## what_makes_documentation_good

- 官方原文：https://github.com/openai/openai-cookbook/blob/main/articles/what_makes_documentation_good.md
- 存档：`01-Raw/VibeCoding/openai/openai-cookbook-articles-what-makes-documentation-good-md.md`

# What makes documentation good

Documentation puts useful information inside other people’s heads. Follow these tips to write better documentation.

### Make docs easy to skim

Few readers read linearly from top to bottom. They’ll jump around, trying to assess which bit solves their problem, if any. To reduce their search time and increase their odds of success, make docs easy to skim.

**Split content into sections with titles.** Section titles act as signposts, telling readers whether to focus in or move on.

**Prefer titles with informative sentences over abstract nouns.** For example, if you use a title like “Results”, a reader will need to hop into the following text to learn what the results actually are. In contrast, if you use the title “Streaming reduced time to first token by 50%”, it gives the reader the information immediately, without the burden of an extra hop.

**Include a table of contents.** Tables of contents help readers find information faster, akin to how hash maps have faster lookups than linked lists. Tables of contents also have a second, oft overlooked benefit: they give readers clues about the doc, which helps them understand if it’s worth reading.

**Keep paragraphs short.** Shorter paragraphs are easier to skim. If you have an essential point, consider putting it in its own one-sentence paragraph to reduce the odds it’s missed. Long paragraphs can bury information.

**Begin paragraphs and sections with short topic sentences that give a standalone preview.** When people skim, they look disproportionately at the first word, first line, and first sentence of a section. Write these sentences in a way that don’t depend on prior text. For example, consider the first sentence “Building on top of this, let’s now talk about a faster way.” This sentence will be meaningless to someone who hasn’t read the prior paragraph. Instead, write it in a way that can understood standalone: e.g., “Vector databases can speed up embeddings search.”

**Put topic words at the beginning of topic sentences.** Readers skim most efficiently when they only need to read a word or two to know what a paragraph is about. Therefore, when writing topic sentences, prefer putting the topic at the beginning of the sentence rather than the end. For example, imagine you’re writing a paragraph on vector databases in the middle of a long article on embeddings search. Instead of writing “Embeddings search can be sped up by vector databases” prefer “Vector databases speed up embeddings search.” The second sentence is better for skimming, because it puts the paragraph topic at the beginning of the paragraph.

**Put the takeaways up front.** Put the most important information at the tops of documents and sections. Don’t write a Socratic big build up. Don’t introduce your procedure before your results.

**Use bullets and tables.** Bulleted lists and tables make docs easier to skim. Use them frequently.

**Bold important text.** Don’t be afraid to bold important text to help readers find it.

### Write well

Badly written text is taxing to read. Minimize the tax on readers by writing well.

**Keep sentences simple.** Split long sentences into two. Cut adverbs. Cut unnecessary words and phrases. Use the imperative mood, if applicable. Do what writing books tell you.

**Write sentences that can be parsed unambiguously.** For example, consider the sentence “Title sections with sentences.” When a reader reads the word “Title”, their brain doesn’t yet know whether “Title” is going to be a noun or verb or adjective. It takes a bit of brainpower to keep track as they parse the rest of the sentence, and can cause a hitch if their brain mispredicted the meaning. Prefer sentences that can be parsed more easily (e.g., “Write section titles as sentences”) even if longer. Similarly, avoid noun phrases like “Bicycle clearance exercise notice” which can take extra effort to parse.

**Avoid left-branching sentences.** Linguistic trees show how words relate to each other in sentences. Left-branching trees require readers to hold more things in memory than right-branching sentences, akin to breadth-first search vs depth-first search. An example of a left-branching sentence is “You need flour, eggs, milk, butter and a dash of salt to make pancakes.” In this sentence you don’t find out what ‘you need’ connects to until you reach the end of the sentence. An easier-to-read right-branching version is “To make pancakes, you need flour, eggs, milk, butter, and a dash of salt.” Watch out for sentences in which the reader must hold onto a word for a while, and see if you can rephrase them.

**Avoid demonstrative pronouns (e.g., “this”), especially across sentences.** For example, instead of saying “Building on our discussion of the previous topic, now let’s discuss function calling” try “Building on message formatting, now let’s discuss function calling.” The second sentence is easier to understand because it doesn’t burden the reader with recalling the previous topic. Look for opportunities to cut demonstrative pronouns altogether: e.g., “Now let’s discuss function calling.”

**Be consistent.** Human brains are amazing pattern matchers. Inconsistencies will annoy or distract readers. If we use Title Case everywhere, use Title Case. If we use terminal commas everywhere, use terminal commas. If all of the Cookbook notebooks are named with underscores and sentence case, use underscores and sentence case. Don’t do anything that will cause a reader to go ‘huh, that’s weird.’ Help them focus on the content, not its inconsistencies.

**Don’t tell readers what they think or what to do.** Avoid sentences like “Now you probably want to understand how to call a function” or “Next, you’ll need to learn to call a function.” Both examples presume a reader’s state of mind, which may annoy them or burn our credibility. Use phrases that avoid presuming the reader’s state. E.g., “To call a function, …”

### Be broadly helpful

People come to documentation with varying levels of knowledge, language proficiency, and patience. Even if we target experienced developers, we should try to write docs helpful to everyone.

**Write simply.** Explain things more simply than you think you need to. Many readers might not speak English as a first language. Many readers might be really confused about technical terminology and have little excess brainpower to spend on parsing English sentences. Write simply. (But don’t oversimplify.)

**Avoid abbreviations.** Write things out. The cost to experts is low and the benefit to beginners is high. Instead of IF, write instruction following. Instead of RAG, write retrieval-augmented generation (or my preferred term: the search-ask procedure).

**Offer solutions to potential problems.** Even if 95% of our readers know how to install a Python package or save environment variables, it can still be worth proactively explaining it. Including explanations is not costly to experts—they can skim right past them. But excluding explanations is costly to beginners—they might get stuck or even abandon us. Remember that even an expert JavaScript engineer or C++ engineer might be a beginner at Python. Err on explaining too much, rather than too little.

**Prefer terminology that is specific and accurate.** Jargon is bad. Optimize the docs for people new to the field, instead of ourselves. For example, instead of writing “prompt”, write “input.” Or instead of writing “context limit” write “max token limit.” The latter terms are more self-evident, and are probably better than the jargon developed in base model days.

**Keep code examples general and exportable.** In code demonstrations, try to minimize dependencies. Don’t make users install extra libraries. Don’t make them have to refer back and forth between different pages or sections. Try to make examples simple and self-contained.

**Prioritize topics by value.** Documentation that covers common problems—e.g., how to count tokens—is magnitudes more valuable than documentation that covers rare problems—e.g., how to optimize an emoji database. Prioritize accordingly.

**Don’t teach bad habits.** If API keys should not be stored in code, never share an example that stores an API key in code.

**Introduce topics with a broad opening.** For example, if explaining how to program a good recommender, consider opening by briefly mentioning that recommendations are widespread across the web, from YouTube videos to Amazon items to Wikipedia. Grounding a narrow topic with a broad opening can help people feel more secure before jumping into uncertain territory. And if the text is well-written, those who already know it may still enjoy it.

### Break these rules when you have a good reason

Ultimately, do what you think is best. Documentation is an exercise in empathy. Put yourself in the reader’s position, and do what you think will help them the most.
