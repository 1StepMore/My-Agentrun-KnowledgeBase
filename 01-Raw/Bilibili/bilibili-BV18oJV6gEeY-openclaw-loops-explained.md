---
title: 龙虾之父说的 loops 到底能干嘛？
keywords:
- agentic-loop
- Agent
- Claude
- ai-coding
- AI自主编码
- Loop模式
state:
  phase: raw
  time_raw: '2026-06-13T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.bilibili.com/video/BV18oJV6gEeY/
source_type: video
source_platform: bilibili
author: 63号炼金工坊
publish_date: '2026-06-12'
fetch_date: '2026-06-13'
priority: 3
language: zh
notes: 使用 Whisper (openai-whisper small, WSL GPU, fp16=False) 转写 + DeepSeek V4 Flash 后处理。视频单P，时长12:15。
duration_seconds: 735
duration_formatted: '12:15'
author_id: ''
---
# 龙虾之父说的 loops 到底能干嘛？

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 龙虾之父说的 loops 到底能干嘛？ |
| 作者 | 63号炼金工坊 |
| 发布时间 | 2026-06-12 |
| 总时长 | 12:15 |
| BV号 | BV18oJV6gEeY |
| 播放量 | 471 |

## 原文内容

（以下为整理后的字幕，已清除非中英文字符和明显乱码，并尝试保留原意，但部分内容因语音识别错误而难以完全还原。）

還有新消息他身受追急中心的加持研究就是 busy 與局培方面在處理同時李永獨和北京斯丁節之旅我無法助攜我原來有脫爛器筋我必須按照下次電視 scale 聽味道是我 Ai 信用你视踪他們可能想說向你到結 CHANNEL No. 長使類型先簡單這次的《一起來三圓的工作》從而將用作同學 迴尾的職業對於迴尾警啦第一個是鏡頭 第二是鏡頭你的所有星巴之間 會一 want to build doctors worldwide 改用服務室字數作大家很良司簡單定位打砸到完成,所以才和切換但是你會在那一段時間在註據收認到 YouTube、Twitter 來訪呀但是無論 GRG 在你的官方 GRG 我嘗試了自然註定證明也滑斷了現在有何不正確意 streets 只要用來談論你可選一研究分不合理但是你要分 mouths 密合信任公理首先,你要捉利格格的預祝友情物數把他送出再 Kita 去或者校围了剩下的增数

So that's where we get to loops. The most basic flow of this being you have a log of all of your issues stored on whatever taskboard you prefer. You have an agent come along and triage those issues, perhaps on an automation, so that it's a manageable amount of work coming down the pipe. Then an agent kicks on to take down that issue, work on the issue, verify it's work using an automated test suite, or using Here or even computer use, and then PR changes for you to look at. Before you were involved in every step of this process, remembering to spin up some work trees to go through GitHub issues, spinning up agents to act on those issues, having an agent review its code and open the PR, and then finally merging it into the code base. But with this new setup, you're slowly removing bottlenecks at each step in the chain, where it's all automated right up until you get to the code review step to let things into the code base. And if you're brave enough, 要不然就让总统拾取所有的线索每个项目的项目以及所有的 QA，你可以把整个人的饮料完全拆除让这个东西跑到墓地。但我还以为我们还没有用模式的能力让总统拾取自己的工作进行一个货币，所以我们仍要把最后的饮料拾取到最后的工作来确保货币好才能拾取。但最后我们要拾取很多饮料的进行让你只要花时间第一是寄信息，第二是寄信息。

所以你如何設定最簡單的信息寄信息然後寄信息？首先寄信息你需要好信息寄信息，這是我的基本步驟寄信息寄信息。我經常開始用 Docs 技術，那是一個計劃模式的計劃模式。我們會問你很多問題，可以想像的如何使用這個方式。所以在最後一節你會走開有一個很清楚的計劃。這是一個很長的討論，我曾經有很多的問題在一個很大的模式中。我曾經在最後一節我和阿俊一起計劃了幾個問題用一個問題計劃，你可以看到阿俊把這個長的討論 img。你還有什麼改選冇法印法印 walking 那個激昁作强還有坎伯農場情的人要備社街市新加坡組織出現林igning 文偉藍線技能 基本上聯想制 as well as Codesino 需要哪個艇進行如何使用令方法究竟 Jar 字也無需免費誰傅再來瑛博防機應付他的技能看這裡的觸動然後它都使用進行自動力制能接近收牆需要場上出現的絕對理論下一權蓄力需要技能

codexapp user there's this tab called automations that you can go to and you can create new automations just by asking the codexapp what automation you want to do and then it will create a new one inside of here I have a couple that I've already set up one of them for writing specifications for big features and another one to work

Here is a cleaned-up and reorganized version of the original transcript, focusing on the coherent English narration and removing garbled or unrelated sections. The text has been lightly edited for readability while preserving the speaker's intended message.

---

…on issues that already have that acceptance criteria that I showed you. If we click into this, you'll see it's a very basic automation. We just have it go to that repo, anything labeled "ready for agent" (or do nothing if there aren't any issues open), pick up an unclaimed issue, and the one bit of instruction that I added was to always use computer use for UI changes — which is a feature that Codex has to let the agent click around the app that it built. Otherwise, I just deferred to the acceptance criteria in the issue to guide the agent to a working solution.

This is a sample run that kicked off recently. You can see it picked up the first issue that it found that was well scoped. It opened a pull request. And I can browse the page list in a new page. I can see the repo, the issues, the labels. I can use condition grammars, but after that I compared them.

You can also try multiple forms — for example, use a plan to do something, or from an issue evidence to a written plan. Then you can plan to a plan, or in a comment plan to do something. So it will have a second plan. You can go to plan, but in the plan, here is a plan I've planned from a plan to a plan. So here is a plan.

Before I sent the second point, you can see here it's writing several comments or techniques on comments. It says how to write a good comment. So here there is a comment to write this character. I want it to think about whether it can write a comment on our question and whether it can write in techniques. It can see what plan is on this issue. Now this will be very critical — it will follow your plan. You can see my comments include effects app, and because this is a monorepo, I want to see what apps are happening. Various frameworks are all using the same style and coverage.

What do we want to do? In order to let the integration check get inspection, meanwhile the information is very impressive. If you hear that our codebase is happy, I love using paper style to upload — just like uploading paper inward. Then you can expect spec 2 ready for agent. So that way the other automation can pick up this plan as acceptance criteria and implement it for me. So now I have two acts to my laziness factor: agents handle all the planning for me, and agents handle the initial implementation.

Now if you're curious about those spec documents I showed you and you want to invent your own skills to teach agents how to write specs, I would suggest pulling down the open source specs that Warp already has. That is the open source terminal that you are seeing right here.

We have a common sense building. We have written our feature documents and product documents. This is my own building. I just ask Codex to look at those product documents and then adapt to my own building. You can see the details of my building are very high level in the whole model part. I like this way and I like this way. So I just want to give you… but I like this building. Let one person take a very hard building and give it to a larger building, then another building takes this building.

Now we need to put these devices. We have already put devices for the company's responsibility. You see it puts many issues. We used a very similar approach to what I just gave you — like a ready approach. When a company can enter, then open a device. We also have more devices at each step of the process. For example, when a device has a device, we have a device. If it is a device, like weapon concerns, the key is to customize. We aim to… model's research… then… the whole model recall. For example, some people might say no, it is using a little speed… out tamet… false write… also pointed to this… etc. legislation, of course.

---

*Note: The last part of the original transcript contained heavy interference; only fragments could be retained. The above represents the most coherent interpretation of the speaker's presentation.*

## 核心摘录

（待补充）

## 个人解读

（待补充）

## 待验证点

（待补充）

## 关联问题

（待补充）

## 抓取备注

- 来源：B站
- 转写方式：Whisper small (GPU) + DeepSeek V4 Flash 后处理
- 话题相关：Agentic Loops
