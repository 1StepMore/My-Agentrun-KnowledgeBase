---
title: Loop Engineering! AI 编程的下一个范式?
keywords:
- agentic-loop
- ai-programming
- paradigm-shift
- prompt-engineering
- ai-coding
state:
  phase: raw
  time_raw: '2026-06-13T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.bilibili.com/video/BV1S6EY6fEUc/
source_type: video
source_platform: bilibili
author: 硅基考古队
publish_date: '2026-06-11'
fetch_date: '2026-06-13'
priority: 3
language: zh
notes: 使用 Whisper (openai-whisper small, WSL GPU, fp16=False) 转写 + DeepSeek V4 Flash 后处理。视频总时长约4分22秒。
duration_seconds: 262
duration_formatted: '4:22'
author_id: ''
---
# Loop Engineering! AI 编程的下一个范式?

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | Loop Engineering! AI 编程的下一个范式? |
| 作者 | 硅基考古队 |
| 发布时间 | 2026-06-11 |
| 总时长 | 4:22 |
| BV号 | BV1S6EY6fEUc |

## 原文内容

你还在一行一行地给AI写Prompt吗？Anthropic的Cloud Code负责人Boris Churny说了句话，我觉得挺炸的。他说：“我已经不亲自Prompt Cloud了。我写了一堆循环，让循环去Prompt Cloud，决定下一步该干嘛。”

Google的Eddie Osmani最近写了篇文章专门讲这个事，他管它叫Loop Engineering，循环工程。什么意思呢？就是设计一个系统，让这个系统取代你自己去Prompt的Coding Agent。你定义目标，AI自己迭代，直到完成。

以前你用Coding Agent，就是你写Prompt，看结果，再写下一个Prompt。你一直握着方向盘，一来一回的。现在变了，你不再是那个打字的人。你设计一个系统，这个系统自己去找活、派活、检查、记录、进度，决定下一步。你从司机变成了造高速公路的人。Osmani说，Loop Engineering在Harness之上一层。Harness是单个Agent的运行环境，Loop是那个环境上面跑的定时系统。自己生子任务，自己为自己……关键观察：一年前搭循环还得自己写Bash脚本，现在Codex和Cloud Code已经内置了所有零件。你别再争论用哪个工具了，直接设计循环就行。

一个循环有五样东西加一样组成：自动化、定时触发，不用你手动敲——比如每天早上自动扫一遍CI失败和新Issue跟踪数；两个Agent并行干活，不会互相踩文件——每个Agent在自己的分支上改，互不干扰；技能，把你的项目规矩写下来，Agent每次不用从头猜你的规范、构建步骤那些因为出过事故才有的规矩；插件和连接器，让Agent能读你的Jira Tracker、Slack消息、调API。这就是Agent说“修完了”和Agent自己开PR的区别。本质上，写代码的和审代码的分开，自己审自己永远太松。一个探索，一个实现，一个验证。

还有第六样——状态。一个Markdown文件或者一个看板，记录哪些做了，哪些过了，哪些还挂着。模型每次跑完就忘，但仓库不会忘。

给你举个完整的例子。每天早上，一个自动化任务跑起来。它读昨天的CI失败、新Issue、最近的提交，写一份清单。清单里值得修的问题，每个开一个独立的工作室，派一个子Agent去写修复。写完以后，另一个子Agent来审。对照项目的技能文件和现有测试。审过了，连接器自动开PR，更新工单，通知频道。搞不定的丢进收件箱等人来看。整个循环的核心是一份状态文件，它记得昨天试了啥、过了啥、还剩啥。今天的循环接上昨天的进度继续跑。你设计了一次，你没有手动Prompt任何一步。同一个循环在Codex和Cloud Code里都能跑，因为底层零件一模一样。但别高兴太早。

循环跑得越快，有三个问题反而会变严重。

第一，验证。你不在的时候，循环也在犯错。写代码的和审代码的分开确实有帮助，但“做完了”仍然是个声明，不是证明。

第二，理解债务。循环替你写的代码越多，你对这些代码的理解就越少。代码存在和你懂它是两回事。

第三，认知投降。循环自己跑，你很容易就停了思考。它给什么你就接受什么。循环分不出来，但人分得出来。两个人可以搭出一模一样的循环，但结果完全相反。一个人用循环加速自己深度理解的工作，另一个人用循环逃避理解工作。

循环工程比Prompt工程更难，不是更简单。门槛低了，但你还是那个得握着方向盘的人。造循环吧。但要像一个打算继续当工程师的人那样去造，而不是像一个只管按按钮的人。

## 核心摘录

## 个人解读

## 待验证点

## 关联问题

## 抓取备注
