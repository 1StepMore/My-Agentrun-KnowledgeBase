---
title: 如何打造AI记忆系统，让AI完美记住你的指令
keywords:
- memory
- context-engineering
- knowledge-base
- disk-persistence
state:
  phase: raw
  time_raw: '2026-09-13T00:00:00'
  time_draft: 2026-09-13 23:13:26
  time_wiki: '2026-09-23T00:53:35'
source_url: https://www.bilibili.com/video/BV1KHYX6yECa
source_type: video
source_platform: bilibili
author: JeffSu杰夫
author_id: '602010761'
publish_date: '2026-09-13'
fetch_date: '2026-09-13'
priority: 2
language: en
notes: 如何打造AI记忆系统，让AI完美记住你的指令
---
# 如何打造AI记忆系统，让AI完美记住你的指令

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文基本信息

| 项目 | 内容 |
|------|------|
| **标题** | 如何打造AI记忆系统，让AI完美记住你的指令 |
| **UP主** | JeffSu杰夫 |
| **发布时间** | 2026-09-13 |
| **视频时长** | 13:40 |
| **播放量** | 540 |
| **点赞** | 15 |
| **视频链接** | https://www.bilibili.com/video/BV1KHYX6yECa |
| **语言** | 英文原声（中文字幕） |

## 视频简介

AI能记住你的写作风格，却会遗忘你昨天做出的项目决策，这背后是有原因的。
在本视频中，我将剖析AI记忆的三个层级：全局记忆、项目记忆以及自定义记忆系统。你将了解ChatGPT、Claude和Gemini之类的AI工具调取信息的方式，已保存的事实为何会残缺不全或者过时，还有Claude Cowork如何维护由你掌控的可见文件。
看完视频后，你会清楚哪一种方案适配你的工作，以及什么时候值得搭建属于你自己的AI记忆系统。

## 英文转写全文

If you're watching this, then you've probably enabled the memory feature in your go-to AI chatbot, expecting it to remember all the important things about you, only to find out that's a big fat lie. Which is weird, because AI companies are known for never over-promising. So in this video, we'll cover why that auto-generated memory is bad on purpose, no matter which chatbot you're using. Then I'll break down the three levels of AI memory, from the basic version you already know to an automated memory system you control, so you can decide how far up you want to go. Let's get started.

Picking things off with Level 1, Global Memory. Put simply, these are the account-level facts and preferences your AI chatbot auto-generates after you enable the memory feature. And the key thing to know is that these notes apply across every chat you have. Diving into an example, let's say you're preparing for a big presentation and you spend a few hours working on it with ChatGPT. The ideal scenario would be for the AI to remember something like, "The user is working on a high-stakes presentation pitching Satya Nadella and Tim Cook on a Microsoft PowerPoint. Slides V1 are confirmed, visual polish is next." Then ideally, when you come back in an hour, a day, or even a month later, you can pick up exactly where you left off without trying to remember everything that happened last session.

But obviously, that's not what happens. When I asked ChatGPT in a brand new chat the next day about the presentation, the AI has no idea what I'm talking about, much less any of the context, feedback, and learnings from the day before. And you can confirm this yourself by opening up your AI's auto-generated memory. In ChatGPT, for example, this lives under personalization, the memory section, manage, where you'll probably notice that it saved very little, if anything, about a specific project or workstream. But it does know high-level details like your role and writing preferences.

So why did it remember those things, but not the presentation? It turns out this is actually by design, because anything saved at the account level, what I call global memory, gets dragged into every future chat. So the AI deliberately keeps it thin, which makes sense, because if something wrong lands there, it poisons everything. Just think about how many hats you wear. You might be a manager at work, a parent to adorable kids, a responsible son or daughter—or irresponsible, I don't judge. You might be a spouse, you might be a sibling, maybe you run a part-time business, and maybe, maybe you play golf on the weekends. Information that's useful in one of those contexts can be completely irrelevant in another. So if AI tried to save all of it at the global level, every new chat would be carrying around a bunch of unrelated contexts, and that can very easily make the output worse. So in plain English, global memory stays high-level because it has to work across every part of your life. And since AI gets t
To decide which details to keep, it errs on the side of remembering less. That being said, at level one, you do have two workarounds. First, in the middle of a conversation, you can explicitly tell AI, "Update your memory. I have a high-stakes presentation on October 6th," and it works. I can literally watch the memory page update. The problem is, I have to remember to ask every single time, and that new entry lands inside the same thin global profile the AI curates. So it follows me into unrelated chats that have nothing to do with this presentation.

The second workaround is to connect tools like Google Drive, then tell the AI, "Pull the latest meeting transcript on the Nutella cookie deal and use it as context." And this can also give the AI information it needs. But this is also problematic because what if you didn't have a meeting about this presentation? And connectors also don't know what happened in a previous working session inside ChatGPT. And just to be clear, both Claude and Gemini have their own versions of global memory and they behave exactly the same way.

As a quick recap, level one is where the AI writes account-level memory about you that applies to every chat, which is useful for the high-level details that should follow you across all those different roles. But it's never gonna hold enough specific context for real work.

Now, longtime viewers know my workflow involves pulling meeting transcripts from Google Drive straight into AI, but that workflow has one critical gap: conversations that happen in person, like coffee chats.

Move on to level two, project memory. In plain English, the projects feature draws a boundary around one specific work stream or recurring task. And because every chat inside that project is about the same thing, the AI can generate much more specific memory entries about the actual work without dragging those details into everything else. To be clear, global memory still cascades in from level one, which means any chat inside a project gets both the account-level memory and the more specific project-level context.

For example, here I'm inside a Claude project. And although I can go in and view the project-level memory, I can't edit this directly, right? So Claude or the AI still gets to decide what gets written down and what gets left out. On one hand, this is great. The AI automatically remembers rules and contexts related to the specific work stream. So my presentation project, if I ask something like, "What are the next steps for this presentation?" Claude correctly tells me version one slides are done and visual polish is next. On the other hand, the AI doesn't know what matters as well as we do. So when I ask, "Remind me of all the confirmed attendees so I know everyone's name in the room," Claude gives me a partial list, even though I pasted a screenshot of the calendar invite into one of the chats a week ago. It read the screenshot just fine at the time, but decided those names weren't important enough to ke
The problem with level two is that the AI is still the author. It decides what makes a cut and what doesn't. And just imagine if Claude drafted an update for your manager with the wrong presentation date because it pulled from an outdated memory entry. That would not be good.

Similar to level one, the workaround for level two is to correct the AI manually. I can either tell Claude in the memory card directly, update project memory, or just explicitly say it in a project-level chat: "Update project memory. John Ternipp is now also confirmed to attend along with Tim Cook," and that fixes the attendee list. But the level one limitation still applies. The human has to notice a problem, remember the correction, and tell the AI what to fix, which isn't very sustainable and kind of defeats the purpose of AI memory.

As a quick recap of level two, projects give the AI a much tighter boundary so it can write more specific memory about one project, while every chat inside that project still inherits your account-level memory from level one. So, and this is the most important sentence in this entire video, everything you've seen so far has the same root issue. The AI is still in control. It decides what gets remembered, where it lives, and when it gets written.

Alright, level three: your own memory system. In a nutshell, this is where memory stops being a black box and becomes actual files you, the user, have full control over. At this level, your AI reads those files at the start of every session, and it automatically updates them as you work. And all three frontier AI labs now ship what I call AI systems. For example, Anthropic has Claude Cowork and Claude Code. OpenAI has ChatGPT Work and ChatGPT Codex. By the way, let me know if you want a video on ChatGPT Work. And Gemini has Gemini Spark. And it's through these tools that we can build and maintain our very own memory systems.

Here's how it works. At the start of every single task, the AI system loads one small file that's basically a routing table for your active projects. So when you say, "I want to continue working on the micro iPhone presentation," it checks that table and routes the request to the folder that owns the project. So even if you have 20-plus active projects, the AI still loads just that one. And within the project folder, the AI will read the latest project-specific memory updates and load all the relevant material, letting you pick up exactly where you left off an hour, a week, or a year from your last working session.

And this is really what level three adds. The system can draw a different boundary for every task. Global context still cascades down, but now I decide where every memory write belongs, and the AI does the grunt work for me.

So let's see this in action. Here in Claude Cowork, I have my Jeff OS workspace folder mounted, and in a fresh session with no context, right? I can say, "I want to continue working on the micro iPhone presentation. Where are we right now and what do w
What do we do next? And we're just gonna fast forward this part. Here, we can see that Cowork first read my root memory.md file, which is that one small file I mentioned earlier, found the presentation listed as an active project, identified the project files live within my consulting folder, then it read the project files in full before giving me an update. The deck is content complete and waiting on a visual polish round, and the presentation date has moved from September 15th to October 6th, and because three more attendees are coming, we had to book a larger conference room. And it even knows what items are still open.

And here's a critical thing about level three. None of this came from an AI black box. They all came from folders and plain text files that I can open, read, and most importantly, edit, as you can see here, right? This is the plain text file that I just opened in Obsidian, and I can change the presentation date from October 6th to October 30th, right? And this gives me full visibility and control over my memory system.

I know this looks intimidating, but it's actually very easy to get started. My free Cowork toolkit includes all the templates you need to build your own Cowork workspace in one week. Link down below.

Back in the same Cowork session, let's continue working on the slide deck. Let's do the headline pass. Go through the deck and sharpen every slide headline so it states the insight. And we're just gonna fast forward a little bit here. All right, it comes back with rewrites for some of these slides, but I noticed a few of them still use acronyms like ASP, SKU, and GTM. Yeah, so I give it feedback using plain English. Don't use acronyms in slide headlines, spell them out. And skipping ahead a little bit here, after about a minute, it reruns the entire pass and confirms all slide titles are now acronym-free.

Now, watch this. When I'm done working, I just type, I'm done with the session, let's wrap up, and we'll send this off.

While that's processing, here's what's happening under the hood. Claude Cowork is scanning through the entire session for decisions, learnings, and progress worth keeping. And then, most importantly, it'll separate findings that need my approval from updates it can handle itself.

Here, under the input needed section, it proposes turning my one-off acronym correction into a permanent rule for all future working sessions. And under the approval exempt section, we see Cowork has already done two things. First, it recorded that the headlines were edited. And second, it also updated the small file it always loads first, root memory.md, because polish round next is no longer true. Meaning our next session starts where this one ended.

So just to be clear, whenever I wrap up a working session, the AI proposes improvements that future sessions should follow and automatically updates the memory files with the progress we made.

As a quick recap, level three is where we decide what gets saved and where it belongs, wh
While the AI is still responsible for the upkeep, AKA the grunt work. And most importantly, every single change lands in a plain text file that we can open and edit ourselves, so we have full visibility.

Now, I don't want to overwhelm you, but this next part is too cool not to share. Once you have an AI system set up correctly, that routing works across your entire workspace, not just inside one project. For example, if I say something like "draft an email updating my manager on the micro iPhone presentation," it routes to the folder holding my writing rules and the project folder with the actual details, so I get an accurate update that already sounds like me.

By the way, if you're at level two and you want the level three system without building the whole thing from scratch, you can get my complete AI command center system for Claude Co-Work in the Co-Work Academy, where you'll get a pre-built system I spent nearly a year refining, plus a step-by-step walkthrough to make it your own. Link down below.

All right, we covered a lot today, so here's a quick recap. Level one is global memory, where the memory writes happen automatically, and because they're account level, those memories apply across every single chat, which is useful for high-level details that should follow you across all the different roles in your life, but it also means they stay too broad for real work like ongoing projects.

Level two is project memory, where the writes still happen automatically, but now the AI has a much tighter boundary so it can keep more specific context about that work stream. The downside is the AI still picks what to keep, so answers can be confidently outdated.

And level three is your own memory system, where you write the rules for what gets saved and where, and the AI does the upkeep against those rules, meaning you get the best of both worlds: total control and minimal work. The downside is that the AI systems do take some real effort to set up, and they work differently than the chat window you might be used to.

If you wanna go deeper on level three, I have an entire video walking through my Claude Co-Work system. See you in the next video. In the meantime, have a great one.
