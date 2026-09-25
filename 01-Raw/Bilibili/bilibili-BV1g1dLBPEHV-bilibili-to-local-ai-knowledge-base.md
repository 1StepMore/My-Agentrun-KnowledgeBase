---
title: 把B站视频转成本地AI知识库！新手也能3分钟上手
keywords:
- Obsidian
- knowledge-base
- productivity-tools
- beginner-tutorial
- Karpathy
- AI
- bilibili
- 本地知识库
- Bilibili-Obsidian-Clipper
state:
  phase: raw
  time_raw: '2026-05-07T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:50:32'
source_url: https://www.bilibili.com/video/BV1g1dLBPEHV/
source_type: video
source_platform: bilibili
author: MIP耀
author_id: '6112497'
publish_date: '2026-04-18'
fetch_date: '2026-05-07'
priority: 3
language: zh
notes: 视频无原生字幕（用户未上传）。使用 Whisper (openai-whisper small, CPU) 自动转写生成字幕，转写结果由 MiniMax 大模型进行后处理（断句、加标点、修正术语）。
duration_seconds: 273
duration_formatted: 04:33
---
# 把B站视频转成本地AI知识库！新手也能3分钟上手

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 视频信息

| 字段 | 内容 |
|------|------|
| 标题 | 把B站视频转成本地AI知识库！新手也能3分钟上手 |
| 作者 | MIP耀（一名正在转型AI的前端工程师） |
| 发布时间 | 2026-04-18 |
| 播放量 | 9653 |
| 点赞数 | 521 |
| 投硬币 | 189 |
| 收藏人数 | 1830 |
| 转发人数 | 279 |
| 弹幕数 | 2 |
| 视频时长 | 04:33 |
| BV号 | BV1g1dLBPEHV |
| 标签 | #Obsidian #知识库 #效率工具 #新手教程 #Karpathy |

## 关联链接

- 原知识库仓库：https://github.com/jason-effi-lab/karpathy-llm-wiki-vault
- B站视频插件仓库：https://github.com/haixiong1997/Bilibili-Obsidian-Clipper
- 作者主页：https://space.bilibili.com/6112497/

## 视频简介

「把B站视频转成本地AI知识库！新手也能3分钟上手」

初投稿，感谢 @杰森的效率工坊 与 @小陈同学c_z 的分享。

原知识库仓库Github地址：https://github.com/jason-effi-lab/karpathy-llm-wiki-vault
B站视频插件仓库地址：https://github.com/haixiong1997/Bilibili-Obsidian-Clipper

## 字幕（Whisper AI 转写）

> ⚠️ 视频无原生字幕（用户未上传）。以下为 Whisper small 模型自动转写结果，CPU 推理。

把B站视频整理至本地LLM Wiki，从视频收藏到AI可理解的知识库。油管能，B站也能。

这一页介绍Carpenter提出的LLM Wiki核心理念。它提出利用WebClipper作为本地知识库，通过WebClipper抓取视频，生成可被LLM理解的Markdown笔记，实现知识互联。核心思路是这样的：视频通过WebClipper抓取，转化为Markdown格式存入本地Obsidian Vault，让LLM能够理解，最终实现知识生长。

B站UP主节森的效率工坊开源了一个Obsidian知识库模板，叫Carpenter LLM Wiki Vault。它基于Carpenter的理念构建，支持YouTube视频自动抓取。但是有一个问题：YouTube视频可以用原生Obsidian WebClipper正常抓取，而B站视频不行，插件无法解析B站页面结构，需要专用解决方案。

B站用户面临三个主要困境。第一，平台差异。B站采用不同的播放器与页面结构，Obsidian WebClipper无法正确解析。第二，字幕格式。B站字幕格式与YouTube不同，需专门解析才能提取。第三，特有数据。B站特有的数据需单独处理。本来B站聚集了大量优质学习资源，却无法像油管一样收入本地知识库。

为了解决这个问题，B站UP主小陈师傅CZ开发了Bilibili WebClipper浏览器扩展，这是专为B站定制的工具，可以一键将视频转化为结构化笔记。目前支持Chromium内核浏览器，如Chrome和Edge，Firefox版本也由UP主提供适配。

接下来演示完整工作流程，共四步。第一步，安装插件。通过浏览器扩展商店或GitHub下载并安装Bilibili WebClipper。第二步，打开任意B站视频页面，点击浏览器右上角的扩展图标。第三步，插件会自动提取标题、UP主字幕和简介，一键生成标准Markdown文件。第四步，文件自动存入LLM Wiki Vault，配合模板的Scales功能自动完成双项链接与图谱构建。

完整工具链包含四个核心组件。第一，Obsidian作为本地知识库核心，支持双链笔记与图谱可视化。第二，Local REST API插件，它为外部工具提供读写笔记库的接口。第三，Carpenter LLM Wiki Vault模板提供标准化的知识管理结构。第四，Bilibili WebClipper负责抓取B站视频原数据与字幕，打通最后一环。

理论就绪，接下来进入实战演示。我会一步步操作，展示如何用Bilibili WebClipper把B站视频无缝整理进LLM Wiki Vault。插件我们打开GitHub Carpenter LLM Wiki Vault仓库，首先看项目结构。核心目录是Root目录下的03 Transcripts，这里专门存放视频转录文本和会议记录，我们稍后将把视频抓取到这个目录。Skills目录下的In-context Query，是我们编译与维护用到的技能。你需要克隆这个仓库到本地作为知识库。根目录在Obsidian中打开，我本地已经有一个克隆好的项目了，让我们进入下一步。

在Obsidian中打开仓库，点击设置，在第三方插件社区插件市场里安装Local REST API。打开插件选项，复制这个API key，稍后我们会把它填入Bilibili WebClipper的配置中。开启这个HTTP服务器选项，配置完成。我们切换到浏览器，打开任意B站学习视频，点击浏览器右上角的插件图标。首次使用需要配置一下，点击设置按钮，粘贴刚才复制的API key，笔记目录改为Rolls/03 Transcripts，点击测试连接，确保配置正确并保存设置。

回到视频页面，点击保存至Obsidian，找到刚刚保存的笔记文件。我已经安装了Claude插件，当然你也可以使用终端或者其他Agent来调用Skill。我们调用In-context Query技能，由于BPI小英较慢，我们直接看编译后的结果。看原文件已经被自动归档到03文件夹，同时Wiki Map目录下生成了对应的概念实体和摘要。后续我们可以通过Query命令向知识库提问，也可以定期运行Link命令修复Wiki Map中的错误。

这样B站视频就被转化成了AI可理解的知识库。从视频收藏到知识生长，油管能，B站也能。如果你觉得这个工作流有帮助，欢迎点赞收藏，我们下期见。

## 相关推荐视频

- [保姆级教程 搭建出karpathy同款AI知识库！知识复利积累](https://www.bilibili.com/video/BV1p4DeB8ECi/)（BV1p4DeB8ECi）
- [视频内容一键保存到 Obsidian：打通本地知识库](https://www.bilibili.com/video/BV15qQwB4EZ9/)（BV15qQwB4EZ9）
- [（1）v5.0详细图文笔记](https://www.bilibili.com/video/BV1GLfcBMEvQ/)（BV1GLfcBMEvQ）
- [【超简单】本地化AI视频总结](https://www.bilibili.com/video/BV1yC97BsE5x/)（BV1yC97BsE5x）
- [Obsidian入门保姆级教程](https://www.bilibili.com/video/BV1Xi4y1h76C/)（BV1Xi4y1h76C）
- [Hermes+Obsidian+LLM wkii，构建AI知识库](https://www.bilibili.com/video/BV16hZFB5ERM/)（BV16hZFB5ERM）
- [跟Karpathy学搭建AI知识库](https://www.bilibili.com/video/BV1mgQPBXEZp/)（BV1mgQPBXEZp）

---

> 抓取时间：2026-05-07
> 抓取工具：Firecrawl（metadata + markdown）+ yt-dlp（音频）+ Whisper small（字幕转写，CPU 推理）
> Whisper 模型：openai-whisper 20250625，small，CUDA/PyTorch 2.11
