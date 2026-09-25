---
title: 把B站视频转成本地AI知识库！新手也能3分钟上手
source: Bilibili 视频转写（1 篇）；本页为我们的提炼
keywords:
- Obsidian
- knowledge-base
- productivity-tools
- beginner-tutorial
- Karpathy
- AI-Agent
- bilibili
state:
  phase: draft
  time_raw: '2026-07-01T12:42:24'
  time_draft: '2026-07-01T12:42:24'
sources:
- Bilibili/bilibili-BV1g1dLBPEHV-bilibili-to-local-ai-knowledge-base.md
related: []
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---
# 把B站视频转成本地AI知识库！新手也能3分钟上手

## 核心知识点

### **[[B站视频下载]]与音频提取**
使用 `yt-dlp` 工具配合 B 站 API 获取视频信息及音频流（如 `-x --audio-format mp3`），或直接下载字幕文件。合法使用时注意版权与用户协议，这是构建本地知识库的数据源头。

### **[[Whisper 语音转写]]**
通过 OpenAI Whisper 模型（本地 CPU/GPU 推理）将音频转为文字，支持多语言。推荐使用 `small` 或 `medium` 平衡速度与准确度，可配置参数（如 `--language zh`）优化中文识别。全程离线，保护隐私。

### **[[本地大语言模型]]知识抽取**
利用 Ollama、llama.cpp 或 LM Studio 运行本地 LLM（如 Qwen2.5、Llama 3），对转写文本进行摘要、关键术语提取、生成 Wiki 风格知识点。结合提示词工程将非结构化内容转化为结构化 Markdown 笔记。

### **[[Obsidian]] 笔记集成与链接**
将生成的 Markdown 文件直接放入 Obsidian Vault，利用 `[[双括号]]` 创建概念链接，形成知识网络。可配合 Templater、Dataview 等插件自动索引与更新，实现“视频→笔记→知识库”的闭环。

### **[[自动化工作流]]编排**
编写 Python 脚本或 Makefile 串联下载、转写、LLM 抽取、写入等步骤，支持定时任务（cron）或一键执行，让知识库持续增长。进阶可结合 GitHub Actions 实现云端自动化。

### **工具对比**

| 环节 | 工具 / 模型 | 优点 | 缺点 |
|------|-------------|------|------|
| 语音转写 | Whisper `small` | CPU 可跑，速度快，准确度适中 | 长音频需分段，资源占用较高 |
| 语音转写 | Whisper `large-v3` | 准确度最高，细节好 | 速度慢，建议 GPU |
| 语音转写 | 百度语音识别（云端） | 中文优化，有免费额度 | 上传音频，隐私受限 |
| LLM 推理 | Ollama + Qwen2.5 7B | 完全本地，中文强，易于部署 | 配置要求中等（8GB+ 显存） |
| LLM 推理 | ChatGPT API（云端） | 质量高，无需本地硬件 | 按量付费，数据离网 |
| 工作流编排 | Python 脚本 + cron | 灵活，完全控制 | 需编程基础 |
| 工作流编排 | n8n / Make（可视化） | 低代码，易维护 | 增加外部依赖 |

## 总结
通过 yt-dlp 下载 B 站音频、Whisper 本地转写、结合 Ollama 运行 Qwen2.5 等 LLM 提取知识点，将结果自动同步到 Obsidian 中，即可快速搭建一个私有、可定制的 AI 知识库。整个过程无需云端付费 API，保护数据隐私，适合新手用 3 分钟上手。

---

相关推荐视频

- [保姆级教程 搭建出karpathy同款AI知识库！知识复利积累](https://www.bilibili.com/video/BV1p4DeB8ECi/)（BV1p4DeB8ECi）
- [视频内容一键保存到 Obsidian：打通本地知识库](https://www.bilibili.com/video/BV15qQwB4EZ9/)（BV15qQwB4EZ9）
- [（1）v5.0详细图文笔记](https://www.bilibili.com/video/BV1GLfcBMEvQ/)（BV1GLfcBMEvQ）
- [【超简单】本地化AI视频总结](https://www.bilibili.com/video/BV1yC97BsE5x/)（BV1yC97BsE5x）
- [Obsidian入门保姆级教程](https://www.bilibili.com/video/BV1Xi4y1h76C/)（BV1Xi4y1h76C）
- [Hermes+Obsidian+LLM wkii，构建AI知识库](https://www.bilibili.com/video/BV16hZFB5ERM/)（BV16hZFB5ERM）
- [跟Karpathy学搭建AI知识库](https://www.bilibili.com/video/BV1mgQPBXEZp/)（BV1mgQPBXEZp）
