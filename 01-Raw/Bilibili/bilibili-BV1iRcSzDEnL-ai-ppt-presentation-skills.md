---
title: 最优秀的1%，已经在这样做PPT了
keywords:
- ppt-replacement
- prompt-engineering
- productivity-tools
- generative-ai
state:
  phase: raw
  time_raw: '2026-09-13T00:00:00'
  time_draft: 2026-09-13 23:13:26
  time_wiki: '2026-09-23T00:53:35'
source_url: https://www.bilibili.com/video/BV1iRcSzDEnL
source_type: video
source_platform: bilibili
author: JeffSu杰夫
author_id: '602010761'
publish_date: '2026-03-22'
fetch_date: '2026-09-13'
priority: 2
language: en
notes: 最优秀的1%，已经在这样做PPT了
---
# 最优秀的1%，已经在这样做PPT了

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文基本信息

| 项目 | 内容 |
|------|------|
| **标题** | 最优秀的1%，已经在这样做PPT了 |
| **UP主** | JeffSu杰夫 |
| **发布时间** | 2026-03-22 |
| **视频时长** | 12:53 |
| **播放量** | 9808 |
| **点赞** | 309 |
| **视频链接** | https://www.bilibili.com/video/BV1iRcSzDEnL |
| **语言** | 英文原声（中文字幕） |

## 视频简介

📃 PPT大纲 - https://www.jeffsu.org/your-ai-presentations-look-great-but-say-nothing 
🦾 AI 系统课程 - https://systemsacademy.ai/?utm_source=youtube&utm_medium=video&utm_campaign=200 
📧 订阅我的邮件 - https://www.jeffsu.org/newsletter/?utm_source=youtube&utm_medium=video&utm_campaign=description

## 英文转写全文

Here is your typical AI presentation. It looks absolutely incredible, but pause on any single slide and you'll realize, just like some congressional hearings, it's a bit thin on substance. The Dow is over 50,000 right now. Here's an easy way to think about it. On one side, we have models like ChatGPT, Gemini, and Claude that can produce sharp arguments in text format, but they can't make pretty slides. On the other side, we have AI presentation tools like Gamma and Beautiful AI that produce gorgeous visuals, but with generic content. What you actually want is up here: slides that are analytically sharp and visually polished. So today I'll walk you through a real workflow that gets you there. Let's get started.

In the interest of time, I've already prepared a flawed presentation outline for you to copy and follow along, linked down below, where we pitch the CEO of Google on partnering with Apple. Now, I'm not saying I was the brains behind this partnership, but when I was at Google, Sundar and I were like this. Now, most videos focus on generating presentations, but in real life, we know the initial draft is never the hard part. It's the multiple rounds of iterations, implementing the feedback from your manager, that takes up 80% of our time. So today we're only gonna spend a minute generating that first draft in Gamma, since that's the easy part, and spend most of the time making changes to that first draft based on realistic stakeholder feedback. And you'll see how I use the right AI features to cut the process down dramatically.

By the way, for transparency, I reached out to Gamma about sponsoring this video since I was gonna make it anyway, and they agreed.

Jumping into Gamma, I'm gonna select Paste in Text, select Presentation, choose the traditional 16 by 9 dimensions. And if we go back to the Google Docs, you'll notice there are two versions of the outline: the original and Gamma optimized, with the difference being the Gamma optimized version uses the three dashes, as you can see, to separate each slide. And this is something Gamma recommends we do. So this is gonna be the version we're pasting in. We're gonna select all of this, Command and Control C, and Command and Control V to paste right here. And I'm gonna scroll to the bottom, select preserve this exact text, which takes us to the prompt editor. We chose the preserve option specifically because I wrote strong titles in this outline, and this option lets us keep those titles unchanged, and we can always trim the body text using the Gamma agent later.

Quick pro tip: you know your slide titles are good when someone can read through every title in sequence without the body text and still understand the full storyline without context. Back in Gamma, I'm gonna select my own custom theme, minimal blue accent, but I also really like the Commons theme, so under their standard, search for Commons, this one. So feel free to start with that. For image source, in a real corporate setting, I would
Honestly, choose image placeholders, so I can add my own internal visuals later. But for the purposes of this video, let's go with AI images. And since I'm on the Plus plan, I'm just gonna select the Flux Pro, the latest Flux Pro model. But if you're actually on a higher tier, I recommend the Nano Banana Pro model, since that performs the best for now. And for image style, I'm just gonna go with illustration for now. Scrolling back up, we're gonna leave the additional instructions field blank because, in my experience, adding instructions here tends to conflict with Gamma's underlying system prompts. So we're gonna leave this blank and we're gonna go ahead and click Generate.

While those slides are generating, if you wanna boost your Google Workspace productivity by 1% every week, including Gemini tips, you can sign up for my weekly newsletter. Every issue is a bite-size tip you can read and apply in under 60 seconds, link down below.

All right, it's done. And what I like to do after generating the first draft of our presentation is to do a quick content cleanup. Because we selected the preserve option earlier, right? So for every single one of these slides, the body text is way too dense, so we need to trim the fat. And what I'm gonna do is open up the agent, or Gamma agent, and paste this prompt to trim the body text on all these slides, and you can find this exact prompt in the Google Doc as well. And we're just gonna fast forward a little bit.

Two things. After every single change the agent makes, we can choose to keep the modified version or revert back to the original. So this original with more text, this is after the trim, right? And if this is still too dense, you can follow up again and say, "Hey, make the slides even more concise without losing intent and message." But for now, this is good enough for me.

Next, I usually remove images that don't complement the text on a slide. Like, what the hell is this image? There's no heads. This is why I don't use AI images for actual presentations. But for the sake of time, we're gonna skip this step and jump into the most important part of the video, which is making changes based on stakeholder feedback.

Diving into scenario one, the general counsel of Google looks at this deck and says the risk mitigation slide needs to be moved right after the executive summary, because if we can't overcome the regulatory hurdles, the rest of the presentation is useless, which is a fair point. So on this slide that basically says, "Hey, don't worry, we're not going to get in trouble with the law, wink, wink," we're going to open up the agent and tell it to move this to right after the executive summary slide. And you're going to find all these prompts, by the way, in the Google Doc. And after literally a second, this gets moved up. Now, it may come as a surprise that moving slides around is something we can do manually and in much less time. So moving onto something a bit more complex, scenario number two, the SVP of plat
Forms and ecosystems says the new slide four claims the distribution war is wide open, but never actually shows where each player stands. So we need to add a new slide with the latest market share breakdown for the frontier AI models. Back in the Gamma agent, I'm going to tell it to search the web for the latest data, present it as a table, and add it as a new slide after this current slide four. After a few seconds — let's fast forward here — it searches the web, pulls the breakdown, and adds it as a brand new slide.

From here, I can also access the Gamma agent from within this new slide and ask it to add yet another slide that visualizes this data as a chart. We're going to wait a few seconds and again fast forward a little bit, and boom, we get a nice visual chart.

In area three, the CFO flags that the 400 million monthly active user statistic isn't sourced. So before Sundar can quote this in a board meeting, we're going to need to verify it. Here, notice that after I select the text on the slide and open up the Gamma agent, it automatically appears as context in the agent window, so the agent knows exactly what I'm referring to. I'm just going to run the prompt, tell it to search online for OpenAI's latest officially reported user count. And we're going to need to replace the number on the slide, right? After a few seconds, let's start over again. The number has been updated to weekly active users, since that's what OpenAI has officially reported, and we've added a source as a footnote.

Scenario four, the chief business officer says this distribution impact slide is way too text heavy and we should show the numbers in a more effective way, and so this needs to be visualized as a chart. Pulling up the Gamma agent, I am going to tell it to convert the slide content into a waterfall chart showing how, if we add up the number of Android devices and iPhone devices, we get a total of roughly 3.25 billion smartphones with Gemini built-in if we proceed with this partnership.

Funnily enough, the agent got this right the first time, but it usually doesn't, because it still struggles with turning text into visuals. So let me walk you through how to fix it if it messes up. All you have to do is double click into the chart and imagine it messed up, right? It added, let's say, MacBook as well — MacBook devices, and let's say it's 1.1 billion right here, so that the chart is incorrect. Instead of 4.53, it should say 3.25. All you gotta do in this example is to right click on the extra row that it added, which I found to be the case a lot of times, and delete the row. And now the number is correct, 3.25. Android smartphones with Gemini, iPhones with Gemini equals 3.25 billion smartphone devices using Gemini if we proceed with this partnership.

Moving on to scenario five, the VP of corporate development says the "Apple can't build this alone" slide has three columns — one, two, three — with equal visual weight, right? But the argument has a clear hierarchy.
Column one and column two are context, and column three competitors eliminated is the punchline. So the visual needs to make that obvious. Back in the Gamma agent, I am going to tell it to make column three visually dominant using color, size, or emphasis, so the audience immediately sees that we, Google, are the last credible option.

The agent restructures the layout and column three now pops compared to the other two, but I still don't actually like how this looks. I'm gonna make a few manual edits. I'm gonna remove the number here, and the text here is still too small. Therefore, I'm gonna make this large text, and this looks much better.

In scenario six, the chief of staff to the CEO looks at slides 11 and 12 and says they're both trying to do the same thing, which is getting the audience to act now. So we need to combine these two slides into one. Now, I wanna show you something. If I just use this first prompt, "combine slides 11 and 12," with no additional context, let's see what happens. Okay, as expected, the result is a mess because the agent just cramped everything together into one slide without applying any sort of critical thinking, sort of like what a dumb intern would do in the Justice Department. So let's revert back to the original, and this time, using the same prompt, we're just going to add "stick with three talking points maximum." And then we'll see what happens.

The agent combines the two slides into one and it's better, but the image is still getting in the way. So let's follow up with "the combined slide is still too dense, remove the image and optimize spacing." And let's fast forward a little bit here. Okay. This is much, much better. And this is a good example of the Gamma agent being designed for speed, not reasoning. So the more precise our instructions, the better the output.

Last scenario, the head of Google Grid China, my old big boss, needs a simplified Chinese version of the deck for the leadership pre-read next Thursday. It doesn't need to be super accurate, just clean enough for internal use. Here, I can just click the dropdown at the top next to the agent, select translate, and find simplified Chinese, which is somewhere down here, if I remember correctly. Here we go. Click translate, and after a minute or two, I am left with a fully translated deck. And as someone who speaks Mandarin Chinese, I would say this is 70, 75% there, which is good enough.

Quick note, if you do need to translate your Gamma presentation, I recommend clicking three dots and duplicating your Gamma presentation and then translating that duplicated version. Because if you just translate right off the bat, Gamma sort of replaces your current original English version with the translated version. Also, after translating, download both the original English and the translated versions as PDFs, upload them onto Gemini, and tell it to act as an expert bilingual translator, and recommend changes to the translated version so it sounds more natur
Logical and coherent. By the way, this type of multi-tool workflow systems thinking is exactly what I teach in the AI Systems Academy, so I'll leave a link to the waitlist below.

Alright, moving on to Pro Tip number one. While Gamma is mainly used for presentations, I actually use Gamma a lot for asynchronous sharing like pre-reads and debriefs because of the scroll format. For example, before a meeting, I'd paste talking points into Gamma, generate a quote-unquote presentation, and send the link to my colleagues as a pre-read.

Pro Tip number two, although it's out of scope for this video, after downloading your Gamma presentation as a PowerPoint, you should use Claude Cowork to visually refine the deck using your own brand guidelines saved locally through the skills feature. Let me know in the comments if you'd like a video on that.

While AI presentation tools, including Gamma, are nowhere close to perfect, I can definitely see a future where low-value tasks like aligning text boxes disappear. But what won't disappear is human-specific skills like critical thinking, soliciting high-quality feedback, and weaving all of that into a coherent narrative. Those skills are only going to become even more important.

On that note, you might want to check out this video where I talk about the four skills AI can never replace. See you there and in the meantime, have a great one.
