---
title: MiniMax_API_OpenClaw使用教程
source: 其他（1 篇）；本页为我们的提炼
keywords:
- MiniMax
- API
- OpenClaw
- AI平台
- 多模态
state:
  phase: draft
  time_raw: '2026-07-01T12:47:26'
  time_draft: '2026-07-01T12:47:26'
sources:
- MiniMax_API_OpenClaw使用教程.md
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---
# MiniMax API 使用教程（OpenClaw 智能体版）

## 核心知识点

1. **双端点配置**：国内 `api.minimaxi.com`，国际 `api.minimax.io`
2. **模型体系**：文本(M2.7/M2.5/M2-her)、语音(speech-2.8-hd/turbo)、图像(image-01)、视频(Hailuo-2.3)、音乐(music-2.6)
3. **SDK兼容**：原生支持 OpenAI SDK 和 Anthropic SDK，无需额外学习成本
4. **Prompt缓存**：输入≥512 Token自动触发，前缀匹配，命中仅按10%计费
5. **M2.7推理加速版**：MiniMax-M2.7-highspeed，与M2.7效果一致但速度大幅提升
6. **Token Plan vs 按量计费**：Key不可互换，M2.7配额5小时滚动窗口重置，其他模型每日0点重置
7. **多模态GroupId**：语音/图像/视频/音乐API需在URL中携带 `GroupId` 参数
8. **音乐Cover流程**：预处理(提取旋律骨架) → 生成翻唱版本，支持风格迁移
9. **视频运镜指令**：15种精确运镜，[推进]/[拉远]/[左移]等，prompt中 `[]` 格式使用
10. **用量重置**：M2.7系列5小时滚动窗口；其他模型每日0点自动重置

## API端点速查

| 类型 | 端点 |
|------|------|
| 文本-OpenAI兼容 | `https://api.minimaxi.com/v1` |
| 文本-Anthropic兼容 | `https://api.minimaxi.com/v1/anthropic` |
| 语音T2A | `https://api.minimaxi.com/v1/t2a_v2?GroupId={group_id}` |
| 图像生成 | `https://api.minimaxi.com/v1/image_generation?GroupId={group_id}` |
| 视频生成 | `https://api.minimaxi.com/v1/video_generation?GroupId={group_id}` |
| 音乐生成 | `https://api.minimaxi.com/v1/music_generation?GroupId={group_id}` |

## 可用模型一览

### 文本模型
- **MiniMax-M2.7**：旗舰模型，复杂任务能力强
- **MiniMax-M2.7-highspeed**：推理速度大幅提升，效果一致
- **MiniMax-M2.5**：性能与性价比平衡
- **M2-her**：角色扮演/长轮次对话优化

### 语音模型
- **speech-2.8-hd**：高音质，自然语气词和情绪渲染
- **speech-2.8-turbo**：极致生成速度
- **speech-02-hd**：通用高性价比

### 图像模型
- **image-01**：文生图/图生图，细腻表现
- **image-01-live**：支持画风控制（漫画/元气/中世纪/水彩）

### 视频模型
- **MiniMax-Hailuo-2.3**：1080P原生，15种运镜指令
- **MiniMax-Hailuo-2.3-Fast**：图生视频优化，速度+50%

### 音乐模型
- **music-2.6**：文本生成音乐，旋律结构控制
- **music-cover**：风格迁移翻唱重编曲


---

## 原文结构（供审核参考）

> 以下为原始文档的完整章节结构，知识点已提取上方

- **文档类型**：API使用教程 / OpenClaw智能体集成指南
- **适合场景**：快速接入MiniMax全模态API（文本/语音/图像/视频/音乐）
- **关键优势**：SDK兼容（OpenAI/Anthropic）、Prompt缓存降低成本、多模态统一鉴权

### 原始章节

1. 概述
2. 准备工作（Token Plan订阅、API Key获取、环境配置）
3. 可用模型列表（文本/语音/视频/图像/音乐）
4. 文本API调用方式（OpenAI SDK / Anthropic SDK）
5. Prompt缓存功能（512 Token触发、前缀匹配、10%计费）
6. 多模态API调用
   - 6.1 语音生成API（T2A）：同步/流式/异步三种方式
   - 6.2 图像生成API（image-01）：文生图/人物主体参考
   - 6.3 视频生成API（Hailuo 2.3）：文生视频/图生视频/运镜指令
   - 6.4 音乐生成API（Music 2.6）：文生音乐/Cover翻唱
7. Token Plan用量管理（套餐对比、用量重置规则、超限处理）
8. OpenClaw智能体最佳实践
9. 官方资源链接
