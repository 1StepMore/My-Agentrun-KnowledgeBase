---
title: XpertAI 多平台多模态内容自动化系统 - 搭建教程
keywords:
- XpertAI
- AI-Agent
- documentation
state:
  phase: raw
  time_raw: '2026-05-08T00:00:00'
  time_draft: '2026-09-23T00:53:35'
  time_wiki: '2026-09-23T00:50:32'
source_url: AI生成
source_type: article
source_platform: xpertai
author: XpertAI
fetch_date: '2026-05-08'
priority: 3
language: zh
notes: XpertAI官方文档
author_id: ''
publish_date: ''
---
# XpertAI 多平台多模态内容自动化系统 - 搭建教程

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

---
AIGC:
    ContentProducer: Minimax Agent AI
    ContentPropagator: Minimax Agent AI
    Label: AIGC
    ProduceID: 33902d3bf57a0262c3f2dc0d5d8e9780
    PropagateID: 33902d3bf57a0262c3f2dc0d5d8e9780
    ReservedCode1: 3046022100c7e5181ab039109d8df417bea27414f9ece08508035bd6eaddc45f2422bc938c022100e44522161e4cc4744b3d4a19f09d1a1252e953089c2f8220b103873f0ad91942
    ReservedCode2: 304502210080ef66e63736b20b49539f564e804449fcadcb930e1f406a2362d018f733f6f0022059ab8085112666c52250c77443fa9a88d3a9c244c5e0f2cc26769ac80b48f3df
---

# XpertAI 多平台多模态内容自动化系统 - 搭建教程

> 本教程基于《XpertAI 多平台多模态内容自动化工作流架构设计方案》，提供详细的分步搭建指导。

## 目录

- [第一步：环境准备](#第一步环境准备)
- [第二步：项目初始化](#第二步项目初始化)
- [第三步：数据结构配置](#第三步数据结构配置)
- [第四步：创建数字专家](#第四步创建数字专家)
- [第五步：配置知识库](#第五步配置知识库)
- [第六步：搭建主工作流](#第六步搭建主工作流)
- [第七步：配置定时任务](#第七步配置定时任务)
- [第八步：外部平台集成](#第八步外部平台集成)
- [第九步：测试与部署](#第九步测试与部署)
- [附录：常见问题](#附录常见问题)

---

## 第一步：环境准备

### 1.1 系统要求

在开始搭建之前，确保您的环境满足以下要求：

| 组件 | 最低要求 | 推荐配置 |
|------|---------|----------|
| 操作系统 | Windows 10 / macOS 10.15 / Ubuntu 20.04 | Windows 11 / macOS 12+ |
| 内存 | 8GB RAM | 16GB RAM |
| 磁盘空间 | 50GB 可用空间 | 100GB SSD |
| 网络 | 稳定宽带连接 | 企业级网络 |
| XpertAI | 开源版 v1.0+ | 最新稳定版 |

### 1.2 安装 XpertAI

#### Windows 系统

1. 访问 XpertAI 官网下载 Windows 安装包
2. 运行安装程序，按照向导完成安装
3. 启动 XpertAI Desktop 应用程序
4. 首次启动时注册账号并登录

#### macOS 系统

1. 下载 macOS 版本的 DMG 安装包
2. 双击挂载磁盘镜像
3. 将 XpertAI 应用拖拽到 Applications 文件夹
4. 启动应用并登录账号

#### Linux 系统（命令行安装）

```bash
# 下载安装包
wget https://xpertai.example.com/downloads/xpertai-linux-latest.tar.gz

# 解压安装
tar -xzf xpertai-linux-latest.tar.gz
cd xpertai-installer
chmod +x install.sh
./install.sh

# 启动服务
xpertai start
```

### 1.3 创建工作目录

在本地创建项目所需的数据存储目录结构：

```bash
# 创建主数据目录
mkdir -p /data/xpertai-content
cd /data/xpertai-content

# 创建子目录结构
mkdir -p topics_pool           # 选题池
mkdir -p contents              # 内容制品
mkdir -p assets               # 素材文件
mkdir -p assets/{date}/{platform}  # 按日期和平台分子目录
mkdir -p drafts               # 草稿文件
mkdir -p drafts/wechat
mkdir -p drafts/zhihu
mkdir -p drafts/xiaohongshu
mkdir -p drafts/douyin
mkdir -p drafts/bilibili
mkdir -p logs                 # 日志文件
mkdir -p backups              # 备份文件
mkdir -p configs             # 配置文件

# 设置目录权限（Linux/macOS）
chmod -R 755 /data/xpertai-content
```

### 1.4 获取 API 凭证

在开始配置之前，您需要准备以下 API 凭证：

| 平台 | 凭证类型 | 获取方式 |
|------|---------|----------|
| XpertAI/Minimax | API Key | XpertAI 控制台 -> API 管理 |
| 微信公众号 | AppID + AppSecret | 微信公众平台 -> 开发 -> 基本配置 |
| 企业微信 | Webhook URL | 企业微信管理后台 -> 应用管理 |
| 知乎 | 创作者账号 | 知乎创作者中心 |

---

## 第二步：项目初始化

### 2.1 创建 XpertAI 项目

1. 登录 XpertAI 控制台
2. 点击「新建项目」按钮
3. 填写项目信息：
   - 项目名称：`MultiPlatform Content Automation`
   - 项目描述：多平台多模态内容自动化工作流
   - 协作模式：规划模式（推荐）

### 2.2 配置项目基础设置

在项目设置页面，配置以下参数：

```
项目配置：
├── 默认模型：Minimax
├── Temperature 设置：
│   ├── 选题生成：0.85
│   ├── 内容创作：0.75
│   └── 合规检查：0.2
├── 超时设置：
│   ├── LLM 调用：60 秒
│   ├── 图片生成：120 秒
│   ├── 视频生成：300 秒
│   └── HTTP 请求：30 秒
└── 并发控制：最多 2 个工作流实例
```

### 2.3 初始化配置文件

创建项目配置文件 `configs/project_config.json`：

```json
{
  "project": {
    "name": "MultiPlatform Content Automation",
    "version": "1.0.0",
    "created_at": "2026-05-01"
  },
  "resource_limits": {
    "max_concurrent_workflows": 2,
    "max_topic_pool_size": 50,
    "cooldown_days": 7
  },
  "scheduling": {
    "topic_generation": "0 7 * * *",
    "content_creation": "0 8 * * *",
    "publishing": "0 10 * * *",
    "effect_collection": "0 12 * * *"
  },
  "platforms": {
    "wechat": {
      "enabled": true,
      "modality": ["article"],
      "publish_mode": "automatic"
    },
    "xiaohongshu": {
      "enabled": true,
      "modality": ["image"],
      "publish_mode": "semiautomatic"
    },
    "zhihu": {
      "enabled": true,
      "modality": ["article"],
      "publish_mode": "semiautomatic"
    },
    "douyin": {
      "enabled": false,
      "modality": ["video"],
      "publish_mode": "semiautomatic"
    },
    "bilibili": {
      "enabled": false,
      "modality": ["video"],
      "publish_mode": "semiautomatic"
    }
  }
}
```

---

## 第三步：数据结构配置

### 3.1 选题池配置

创建选题池初始化文件 `topics_pool.json`：

```json
{
  "version": "1.0",
  "last_updated": "2026-05-01T00:00:00Z",
  "topics": [],
  "stats": {
    "total_count": 0,
    "pending_count": 0,
    "processing_count": 0,
    "published_count": 0,
    "eliminated_count": 0
  }
}
```

### 3.2 评分权重配置

创建评分配置文件 `configs/scoring_weights.json`：

```json
{
  "traffic_topic": {
    "weights": {
      "heat_score": 0.35,
      "timeliness_score": 0.25,
      "platform_fit": 0.15,
      "service_tag_cover": 0.05,
      "case_fit": 0.05,
      "audience_match": 0.05,
      "history_effect": 0.10
    }
  },
  "service_topic": {
    "weights": {
      "heat_score": 0.10,
      "timeliness_score": 0.10,
      "platform_fit": 0.10,
      "service_tag_cover": 0.35,
      "case_fit": 0.20,
      "audience_match": 0.15,
      "history_effect": 0.00
    }
  }
}
```

### 3.3 平台输出规格配置

创建平台配置 `configs/platform_specs.json`：

```json
{
  "wechat": {
    "content_type": "article",
    "title_length": [15, 30],
    "body_length": [1500, 3000],
    "cover_size": [900, 383],
    "image_count": [2, 3],
    "output_format": "html"
  },
  "xiaohongshu": {
    "content_type": "image",
    "title_length": [20, 50],
    "body_length": [200, 300],
    "cover_size": [1242, 1660],
    "image_count": [4, 6],
    "tag_count": [5, 10],
    "output_format": "markdown"
  },
  "zhihu": {
    "content_type": "article",
    "title_length": [15, 40],
    "body_length": [2000, 4000],
    "image_count": [1, 3],
    "output_format": "markdown"
  },
  "douyin": {
    "content_type": "video",
    "title_length": [15, 30],
    "description_length": [50, 100],
    "script_chapters": [3, 8],
    "video_duration": [30, 180],
    "output_format": "json"
  },
  "bilibili": {
    "content_type": "video",
    "title_length": [15, 30],
    "description_length": [50, 100],
    "script_chapters": [3, 8],
    "video_duration": [60, 600],
    "output_format": "json"
  }
}
```

---

## 第四步：创建数字专家

### 4.1 Supervisor Agent（总调度器）

1. 在 XpertAI 控制台，点击「智能体」->「新建智能体」
2. 配置基本信息：
   - 名称：`Supervisor Agent`
   - 角色：总调度器
   - 描述：负责协调所有子智能体，管理任务分发和结果汇总
3. 配置系统提示词：

```
你是 XpertAI 多平台内容自动化系统的总调度器（Supervisor Agent）。
你的职责是协调多个数字专家完成从选题到发布的全流程。

核心职责：
1. 分析当前任务状态，制定执行计划
2. 判断是否需要生成新选题
3. 决定当日创作的选题（基于评分排序）
4. 协调多平台内容并行生成
5. 监控执行状态，处理异常情况

调度流程：
1. 检查选题池状态（待处理选题数量 < 5 时触发选题生成）
2. 触发选题评分与排序
3. 选取 Top-N 选题进行创作
4. 分发任务给平台策略专家
5. 汇总生成结果，进入合规检查
6. 执行发布或生成操作清单

当遇到异常时，采用降级策略：
- 某平台生成失败：继续其他平台，标记失败项
- 评分计算失败：使用默认权重
- 合规检查失败：进入人工审核队列
```

4. 配置所需工具：
   - 定时任务工具集
   - 逻辑分支
   - 列表操作器
   - 代码执行

### 4.2 热点监控与选题生成专家

1. 新建智能体，名称：`热点监控与选题生成专家`
2. 配置系统提示词：

```
你是热点监控与选题生成专家，负责每日抓取热点并生成候选选题。

工作流程：
1. 通过 Web 搜索工具抓取热榜数据：
   - 微博热搜 TOP 20
   - 百度热榜 TOP 20
   - 知乎热榜 TOP 20
   - 抖音热点 TOP 20
2. 结合企业服务标签进行创意关联
3. 生成 5-10 个候选选题

选题类型：
- 引流题材：热点切入，自然带出企业介绍
- 服务介绍题材：服务关联，强调转化价值

每个选题需包含：
- title: 选题标题（20字以内）
- description: 选题描述（100-200字）
- topic_type: traffic 或 service
- heat_score: 预估热度（0-100）
- timeliness_score: 时效性评分（0-100）
- service_tags: 关联服务标签
- target_platforms: 目标平台列表

生成后进行去重处理，避免与历史选题重复。
```

3. 配置所需工具：
   - Web 搜索工具
   - 知识库检索
   - Minimax LLM
   - 代码执行

### 4.3 平台策略专家

#### 微信公众号策略专家

1. 新建智能体，名称：`微信公众号策略专家`
2. 系统提示词：

```
你是微信公众号内容策略专家，负责生成适配微信公众号的图文内容。

输出规格：
- 封面图：900x383 px
- 配图：2-3 张，宽度 900px
- 标题：15-30 字，含关键词
- 摘要：50-80 字
- 正文：1500-3000 字

内容结构：
引言（吸引注意）-> 热点分析（切入话题）->
观点阐述（展现专业）-> 企业服务介绍（自然过渡）-> CTA（引导转化）

风格要求：
- 专业、权威
- 图文并茂
- 自然植入品牌信息

输出格式：HTML/Markdown
```

3. 配置工具：
   - Minimax LLM
   - 知识库检索
   - 图片生成 Skill

#### 小红书策略专家

1. 新建智能体，名称：`小红书策略专家`
2. 系统提示词：

```
你是小红书内容策略专家，负责生成适配小红书平台的多图笔记。

输出规格：
- 封面图：1242x1660 px（竖版）
- 配图：4-6 张，1080x1080 px（方图）
- 短文案：300 字以内
- 话题标签：5-10 个

内容风格：
- 要点化、清单化
- 视觉化呈现
- 避免大段文字
- 结尾含互动引导

内容结构：
吸引眼球的标题 + 3-5 个要点 + 互动引导（提问/收藏引导）

话题标签：
- 平台热门标签
- 企业服务相关标签
- 热点相关标签
```

3. 配置工具：
   - Minimax LLM
   - 图片生成 Skill

#### 知乎策略专家

1. 新建智能体，名称：`知乎策略专家`
2. 系统提示词：

```
你是知乎内容策略专家，负责生成适配知乎平台的深度图文。

输出规格：
- 标题：15-40 字，含疑问句或数据
- 正文：2000-4000 字
- 配图：1-3 张
- 引用/数据：需标注权威来源

内容结构：
问题引入（引发思考）-> 背景分析（提供上下文）->
深度解读（展现专业）-> 数据/引用支撑（增强可信度）-> 总结观点（给出结论）

风格要求：
- 专业、有深度
- 逻辑清晰
- 适当引用数据和案例
- Markdown 格式输出
```

3. 配置工具：
   - Minimax LLM
   - 知识库检索

### 4.4 合规与风控审查专家

1. 新建智能体，名称：`合规与风控审查专家`
2. 系统提示词：

```
你是合规与风控审查专家，负责对生成的内容进行四维度合规检查。

检查维度：

1. 法律与监管合规
   - 广告法合规：无绝对化用语、无虚假承诺
   - 未成年人保护：无不当信息披露
   - 敏感领域：无金融投资建议、无医疗健康建议
   - 政治与社会：无敏感话题

2. 版权与素材来源
   - 图片版权：AI生成或已授权
   - 文字原创性：无高度相似内容
   - 数据引用：标注权威来源

3. 品牌一致性
   - 品牌调性一致
   - 服务承诺在范围内
   - 联系方式准确

4. 事实准确性
   - 事实陈述准确
   - 数据来源权威
   - 时效性验证通过

检查结果格式：
{
  "legal_compliance": "pass/reject/pending_manual",
  "copyright": "pass/reject/pending_manual",
  "brand_consistency": "pass/reject/pending_manual",
  "fact_accuracy": "pass/reject/pending_manual",
  "overall": "pass/reject/pending_manual",
  "issues": ["具体问题描述"],
  "suggestions": ["修改建议"]
}

设计原则：宁可误拦、不可漏放
```

3. 配置工具：
   - Minimax LLM
   - 知识库检索
   - 代码执行

### 4.5 发布与集成执行专家

1. 新建智能体，名称：`发布与集成执行专家`
2. 系统提示词：

```
你是发布与集成执行专家，负责将内容发布到各平台。

发布策略：

微信公众号（全自动）：
1. 获取 access_token
2. 上传封面图和配图
3. 创建草稿
4. 群发

其他平台（半自动）：
1. 生成草稿文件（Markdown/JSON）
2. 生成发布操作清单
3. 通过通知渠道发送给运营人员

发布结果记录：
{
  "content_id": "内容ID",
  "platform": "平台名称",
  "published_at": "发布时间",
  "result": "success/failed",
  "error_message": "错误信息（如有）",
  "external_id": "平台返回的内容ID"
}

异常处理：
- 失败后自动重试 2 次（间隔 60 秒）
- 重试仍失败时进入人工处理队列
```

3. 配置工具：
   - HTTP 请求
   - 代码执行
   - 逻辑分支

---

## 第五步：配置知识库

### 5.1 创建知识库分类

在 XpertAI 控制台的知识库模块中，创建以下分类：

```
知识库结构
├── 品牌信息库
│   ├── 品牌故事
│   ├── 品牌调性指南
│   └── VI 规范
├── 服务介绍库
│   ├── 产品服务列表
│   ├── 服务定价
│   └── 业务流程
├── 案例库
│   ├── 成功案例
│   ├── 客户证言
│   └── 行业解决方案
├── 合规规则库
│   ├── 广告法禁用词
│   ├── 敏感领域清单
│   └── 发布规范
└── 模板库
    ├── 微信文章模板
    ├── 小红书笔记模板
    ├── 知乎问答模板
    └── 视频脚本模板
```

### 5.2 上传品牌信息

1. 准备品牌文档（支持 PDF、Word、Markdown、TXT 格式）
2. 上传到「品牌信息库」
3. 配置分块策略：
   - 块大小：500 字符
   - 块重叠：50 字符
4. 执行嵌入生成

### 5.3 上传服务介绍

1. 整理产品服务文档
2. 上传到「服务介绍库」
3. 标注关键信息（服务名称、价格、适用场景）
4. 生成嵌入向量

### 5.4 整理历史案例

1. 收集成功案例材料
2. 按行业/场景分类上传
3. 添加案例效果数据（阅读量、转化率等）
4. 建立案例标签体系

### 5.5 配置合规规则

1. 创建广告法禁用词列表 `compliance/ forbidden_words.txt`：

```
最、第一、国家级、独家、顶级、极品
无效退款、100%有效、永久治愈
立即购买、限时特价、错过等一年
```

2. 创建敏感领域清单 `compliance/sensitive_topics.txt`：

```
金融投资建议类
医疗健康建议类
法律咨询类
政治敏感类
```

3. 上传至「合规规则库」

---

## 第六步：搭建主工作流

### 6.1 创建主工作流

1. 在 XpertAI 控制台，点击「工作流」->「新建工作流」
2. 命名为：`主内容生产工作流`
3. 设置触发方式：定时触发

### 6.2 节点配置

按以下顺序添加和配置节点：

#### 节点 1：定时触发器

```
节点类型：触发器
配置：
├── Cron 表达式：0 7 * * *
├── 触发时间：每天 7:00
└── 失败通知：企业微信 Webhook
```

#### 节点 2：热点监控与选题生成

```
节点类型：Agent
配置：
├── 智能体：热点监控与选题生成专家
├── 输入：
│   ├── 企业服务标签
│   ├── 历史选题数据
│   └── 当日日期
├── 输出：
│   └── candidate_topics（候选选题列表）
└── 失败策略：重试 2 次，降级为模板生成
```

#### 节点 3：选题评分与排序

```
节点类型：Workflow
配置：
├── 节点功能：评分公式计算
├── 评分公式：total_score = Σ(factor_score[i] × weight[i])
├── 评分因子：
│   ├── 热度评分
│   ├── 时效性评分
│   ├── 平台偏好匹配
│   ├── 服务标签覆盖
│   ├── 案例适配度
│   ├── 目标客群匹配
│   └── 历史效果
├── 输出：
│   ├── scored_topics（排序后的选题列表）
│   └── updated topics_pool.json
└── 失败策略：使用默认权重重算
```

#### 节点 4：选题选取

```
节点类型：Workflow
配置：
├── 节点功能：Top-N 选取
├── 选取策略：
│   ├── 每日选取数量：1-3 个
│   ├── 题材比例：引流 7 : 服务介绍 3
│   └── 状态更新：pending -> processing
├── 输出：
│   ├── selected_topics
│   └── updated topics_pool.json
└── 失败策略：选题池为空时跳过并通知
```

#### 节点 5：多平台内容生成

```
节点类型：Agent + Workflow 混合
配置：
├── 分发逻辑：根据 target_platforms 路由
├── 并行策略：伪并行（快速串行切换）
├── 平台配置：
│   ├── wechat -> 微信公众号策略专家
│   ├── xiaohongshu -> 小红书策略专家
│   └── zhihu -> 知乎策略专家
├── 输出：
│   └── generated_contents（各平台内容制品）
└── 失败策略：单平台失败不影响其他平台
```

#### 节点 6：合规与风控检查

```
节点类型：Workflow
配置：
├── 检查维度：
│   ├── 法律与监管合规
│   ├── 版权与素材来源
│   ├── 品牌一致性
│   └── 事实准确性
├── 检查方式：并行四维度检查
├── 输出：
│   ├── compliance_results
│   └── 各制品标注：pass/reject/pending_manual
└── 失败策略：检查节点失败则全部进入人工队列
```

#### 节点 7：发布执行

```
节点类型：Workflow
配置：
├── 路由逻辑：根据平台类型分发
├── 微信公众号：全自动 API 发布
├── 其他平台：生成草稿 + 操作清单
├── 输出：
│   ├── publish_results
│   ├── PublishLog
│   └── Content 状态更新
└── 失败策略：重试 2 次后进入人工队列
```

#### 节点 8：效果数据回采（延迟执行）

```
节点类型：Workflow
配置：
├── 触发时间：发布后 24 小时
├── 回采数据：
│   ├── 阅读量
│   ├── 点赞数
│   ├── 评论数
│   └── 转发数
├── 输出：
│   ├── effect_data.jsonl
│   └── 评分权重调整建议
└── 失败策略：非关键，跳过并记录日志
```

### 6.3 工作流连接配置

在可视化编辑器中，按以下拓扑连接各节点：

```
[定时触发] -> [热点监控与选题生成] -> [选题评分与排序]
    -> [选题选取] -> [多平台内容生成] -> [合规与风控检查]
    -> [发布执行] -> [效果数据回采]
```

### 6.4 全局错误处理配置

```
错误处理策略：
├── 节点执行失败：自动重试 2 次（间隔 30 秒）
├── 重试仍失败：暂停工作流并发送告警
├── 非关键节点：配置"跳过并继续"
└── 数据持久化：每次操作后写回 JSON 文件
```

---

## 第七步：配置定时任务

### 7.1 定时任务列表

| 任务名称 | Cron 表达式 | 执行时间 | 执行智能体 |
|---------|-----------|---------|-----------|
| 选题生成 | `0 7 * * *` | 每天 7:00 | 热点监控专家 |
| 内容创作 | `0 8 * * *` | 每天 8:00 | Supervisor Agent |
| 发布执行 | `0 10 * * *` | 每天 10:00 | 发布执行专家 |
| 效果回采 | `0 12 * * *` | 每天 12:00 | 数据分析专家 |

### 7.2 配置定时任务

1. 在 XpertAI 控制台，点击「定时任务」->「新建定时任务」
2. 逐个创建上述四个任务
3. 配置每个任务的通知接收人
4. 设置超时告警阈值

### 7.3 备份任务配置

创建每日凌晨的自动备份任务：

```
任务名称：每日数据备份
Cron 表达式：0 3 * * *
执行内容：
1. 打包 /data/xpertai-content/ 目录
2. 存储到 /backup/xpertai-content/
3. 保留最近 7 天备份
4. 清理过期备份（超过 7 天）
```

---

## 第八步：外部平台集成

### 8.1 微信公众号集成

#### 8.1.1 创建自定义工具

在 XpertAI 中创建微信公众号 API 封装工具：

```python
# 工具名称：wechat_publish
# 工具类型：代码执行

import requests
import json
import time
from datetime import datetime

class WeChatPublisher:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        self.token_expires_at = 0

    def get_access_token(self):
        """获取 access_token（带缓存）"""
        if self.access_token and time.time() < self.token_expires_at:
            return self.access_token

        url = f"https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.app_id,
            "secret": self.app_secret
        }
        response = requests.get(url, params=params)
        data = response.json()

        self.access_token = data.get("access_token")
        expires_in = data.get("expires_in", 7200)
        self.token_expires_at = time.time() + expires_in - 300

        return self.access_token

    def upload_permanent_material(self, file_path, material_type="image"):
        """上传永久素材"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/material/add_material"
        files = {"media": open(file_path, "rb")}
        data = {"type": material_type}
        params = {"access_token": token}

        response = requests.post(url, files=files, data=data, params=params)
        result = response.json()

        return result

    def create_draft(self, articles):
        """创建草稿"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/draft/add"
        payload = {"articles": articles}
        params = {"access_token": token}

        response = requests.post(url, json=payload, params=params)
        result = response.json()

        return result

    def publish_draft(self, media_id):
        """发布草稿（群发）"""
        token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/media/publish"
        payload = {"media_id": media_id}
        params = {"access_token": token}

        response = requests.post(url, json=payload, params=params)
        result = response.json()

        return result

# 使用示例
def publish_wechat_content(title, author, digest, content_html, cover_path, image_paths):
    """发布微信公众号内容的完整流程"""
    # 初始化（需要替换为实际凭证）
    publisher = WeChatPublisher(
        app_id="YOUR_APP_ID",
        app_secret="YOUR_APP_SECRET"
    )

    # 上传封面图
    cover_result = publisher.upload_permanent_material(cover_path, "image")
    thumb_media_id = cover_result.get("media_id")

    # 上传配图
    image_media_ids = []
    for path in image_paths:
        result = publisher.upload_permanent_material(path, "image")
        image_media_ids.append(result.get("media_id"))

    # 创建文章结构
    article = {
        "title": title,
        "author": author,
        "digest": digest,
        "content": content_html,
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }

    # 创建草稿
    draft_result = publisher.create_draft([article])
    media_id = draft_result.get("media_id")

    return {
        "success": True,
        "media_id": media_id,
        "draft_url": f"https://mp.weixin.qq.com/"
    }

# 测试函数
if __name__ == "__main__":
    result = publish_wechat_content(
        title="测试文章标题",
        author="XpertAI Bot",
        digest="这是文章摘要",
        content_html="<p>文章正文内容</p>",
        cover_path="/data/xpertai-content/assets/test_cover.jpg",
        image_paths=["/data/xpertai-content/assets/test_image1.jpg"]
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
```

#### 8.1.2 注册为自定义 Skill

1. 在 XpertAI 控制台，点击「Skills」->「新建 Skill」
2. 填写 Skill 信息：
   - 名称：`wechat_publish`
   - 描述：微信公众号内容发布工具
   - 类型：代码执行
3. 粘贴上述代码
4. 配置输入参数映射

### 8.2 知乎半自动方案

#### 8.2.1 生成草稿文件

```python
# 工具名称：zhihu_draft_generator
# 工具类型：代码执行

import json
import os
from datetime import datetime

def generate_zhihu_draft(content_data, output_dir="/data/xpertai-content/drafts/zhihu"):
    """生成知乎草稿文件"""
    os.makedirs(output_dir, exist_ok=True)

    topic_id = content_data.get("topic_id", "unknown")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 生成 Markdown 文件
    md_content = f"""---
title: {content_data.get('title', '未命名')}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {', '.join(content_data.get('tags', []))}
---

# {content_data.get('title', '未命名')}

{content_data.get('body', '')}

---
*本文由 XpertAI 自动生成，仅供人工审核发布*
"""

    md_filename = f"zhihu_draft_{topic_id}_{timestamp}.md"
    md_path = os.path.join(output_dir, md_filename)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    # 生成发布操作清单
    checklist = f"""
================================================================================
                          知乎发布操作清单
================================================================================
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
选题ID：{topic_id}

【一、推荐标题】
{content_data.get('title', '未命名')}

【二、SEO 优化建议】
- 关键词：{', '.join(content_data.get('tags', [])[:5])}
- 建议话题：{', '.join(content_data.get('recommended_topics', []))}

【三、正文内容】
详见附件 Markdown 文件：{md_filename}

【四、配图说明】
"""

    for i, img in enumerate(content_data.get('images', []), 1):
        checklist += f"- 配图{i}：{img}\n"

    checklist += f"""
【五、建议发布时间】
- 工作日：上午 9:00-11:00 或 下午 14:00-16:00
- 周末：上午 10:00-12:00

【六、注意事项】
1. 发布前请审核内容准确性
2. 检查配图是否有水印
3. 确认话题标签选择合适
4. 设置开放评论

【七、发布后操作】
发布成功后，请在系统中回录发布状态：
- 登录 XpertAI 控制台
- 找到内容 ID：{content_data.get('content_id', '')}
- 更新状态为：published

================================================================================
"""

    checklist_filename = f"publish_checklist_{topic_id}_{timestamp}.txt"
    checklist_path = os.path.join(output_dir, checklist_filename)

    with open(checklist_path, "w", encoding="utf-8") as f:
        f.write(checklist)

    return {
        "success": True,
        "md_file": md_path,
        "checklist_file": checklist_path
    }
```

### 8.3 小红书半自动方案

#### 8.3.1 生成素材包

```python
# 工具名称：xiaohongshu_package_generator
# 工具类型：代码执行

import zipfile
import os
import json
from datetime import datetime

def generate_xiaohongshu_package(content_data, output_dir="/data/xpertai-content/drafts/xiaohongshu"):
    """生成小红书素材包"""
    os.makedirs(output_dir, exist_ok=True)

    topic_id = content_data.get("topic_id", "unknown")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 创建 ZIP 包
    zip_filename = f"xiaohongshu_package_{topic_id}_{timestamp}.zip"
    zip_path = os.path.join(output_dir, zip_filename)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 添加封面图
        if content_data.get('cover_image'):
            zipf.write(content_data['cover_image'], 'cover.jpg')

        # 添加配图
        for i, img in enumerate(content_data.get('images', []), 1):
            if os.path.exists(img):
                zipf.write(img, f'image_{i}.jpg')

        # 添加文案文件
        caption_content = f"""# {content_data.get('title', '未命名')}

{content_data.get('body', '')}

---
话题标签：
{', '.join(content_data.get('tags', []))}
"""
        zipf.writestr('caption.txt', caption_content)

    # 生成操作清单
    checklist = f"""
================================================================================
                         小红书发布操作清单
================================================================================
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
选题ID：{topic_id}

【一、素材包】
文件：{zip_filename}
内容：
- 封面图：cover.jpg（尺寸：1242x1660 竖版）
- 配图：{len(content_data.get('images', []))} 张
- 文案：caption.txt

【二、发布步骤】
1. 下载并解压素材包
2. 打开小红书 APP 或创作者中心
3. 按以下顺序上传图片：
   第一张：cover.jpg（封面图）
   第二张及后续：image_1.jpg, image_2.jpg...

4. 复制 caption.txt 中的文案内容
5. 添加话题标签：
   {', '.join(content_data.get('tags', [])[:10])}

【三、图片尺寸要求】
- 封面图：1242x1660（竖版）或 1080x1440
- 配图：建议 1080x1080（方图）

【四、文案要点】
{content_data.get('body', '')[:500]}...

【五、建议发布时间】
- 工作日：19:00-22:00
- 周末：全天均可

【六、注意事项】
1. 封面图是吸引点击的关键，请确保清晰美观
2. 图片避免水印和版权问题
3. 话题标签选择要精准

================================================================================
"""

    checklist_filename = f"publish_checklist_{topic_id}_{timestamp}.txt"
    checklist_path = os.path.join(output_dir, checklist_filename)

    with open(checklist_path, "w", encoding="utf-8") as f:
        f.write(checklist)

    return {
        "success": True,
        "package_file": zip_path,
        "checklist_file": checklist_path
    }
```

---

## 第九步：测试与部署

### 9.1 功能测试

#### 9.1.1 选题生成测试

```
测试步骤：
1. 手动触发热点监控与选题生成专家
2. 检查生成选题数量（预期：5-10 个）
3. 验证选题格式是否正确
4. 检查去重逻辑是否生效
5. 验证写入 topics_pool.json
```

#### 9.1.2 评分排序测试

```
测试步骤：
1. 在选题池中准备 10 条测试选题
2. 运行评分排序工作流
3. 验证评分计算是否正确
4. 检查排序结果是否符合预期
5. 验证末位淘汰逻辑
```

#### 9.1.3 内容生成测试

```
测试步骤：
1. 选取一个选题进行内容生成
2. 分别测试各平台内容生成
3. 验证输出格式是否符合平台规格
4. 检查素材文件是否正确生成
```

#### 9.1.4 合规检查测试

```
测试步骤：
1. 准备正常内容样本
2. 准备包含违规内容样本
3. 运行合规检查流程
4. 验证检查结果准确性
5. 验证人工审核队列机制
```

#### 9.1.5 发布测试

```
测试步骤（微信公众号）：
1. 准备测试内容
2. 运行发布工作流
3. 检查草稿是否成功创建
4. 验证草稿内容正确性

测试步骤（半自动平台）：
1. 运行发布工作流
2. 检查草稿文件是否生成
3. 检查操作清单是否完整
```

### 9.2 集成测试

#### 9.2.1 端到端流程测试

```
测试步骤：
1. 执行完整主工作流
2. 监控各节点执行状态
3. 检查数据流转正确性
4. 验证最终输出结果
5. 测量总执行时间
```

#### 9.2.2 定时任务测试

```
测试步骤：
1. 创建测试定时任务（每分钟触发）
2. 验证触发时间准确性
3. 验证通知机制
4. 完成后删除测试任务
```

### 9.3 性能优化

#### 9.3.1 超时配置调整

根据测试结果调整各节点超时时间：

```json
{
  "timeout_settings": {
    "llm_call": 60,
    "image_generation": 120,
    "video_generation": 300,
    "http_request": 30,
    "code_execution": 30,
    "workflow_total": 1800
  }
}
```

#### 9.3.2 并发控制

配置工作流并发限制：

```json
{
  "concurrency": {
    "max_workflow_instances": 2,
    "max_parallel_agents": 2,
    "api_rate_limit": {
      "minimax": "60 requests/minute",
      "wechat_api": "10 requests/minute"
    }
  }
}
```

### 9.4 上线部署

#### 9.4.1 最终检查清单

```
上线前检查：
□ 所有定时任务已配置
□ 企业微信通知已测试
□ 备份策略已配置
□ 监控告警已设置
□ 知识库已更新
□ 配置文件已验证
□ 应急预案已准备
```

#### 9.4.2 启动生产运行

1. 确认所有测试通过
2. 将系统切换到生产模式
3. 启用完整监控
4. 通知相关人员
5. 开始第一天的生产运行

#### 9.4.3 监控与维护

```
日常监控：
- 工作流执行日志
- API 调用成功率
- 素材存储空间
- 错误告警通知

定期维护（每周）：
- 检查日志文件大小
- 清理过期素材
- 审核知识库内容
- 评估系统性能

定期维护（每月）：
- 更新热点监控关键词
- 优化评分权重
- 更新合规规则
- 备份检查
```

---

## 附录：常见问题

### Q1：选题生成数量过少怎么办？

**原因**：热点数据不足或企业服务标签匹配度低

**解决方案**：
1. 增加热榜数据源（添加更多热搜平台）
2. 扩展企业服务标签范围
3. 降低选题生成阈值
4. 检查去重逻辑是否过于严格

### Q2：内容生成超时怎么处理？

**原因**：LLM 响应慢或 API 限流

**解决方案**：
1. 增加超时时间配置
2. 启用降级策略（简化生成流程）
3. 错峰执行（避免高峰期）
4. 优化提示词，减少生成内容长度

### Q3：微信公众号 API 调用失败？

**常见错误**：
- `40001`：access_token 无效 → 重新获取
- `40013`：appid 不匹配 → 检查配置
- `40125`：appsecret 无效 → 重新配置

**排查步骤**：
1. 检查 AppID 和 AppSecret 是否正确
2. 验证 IP 白名单配置
3. 确认接口权限已开通
4. 检查调用频率限制

### Q4：合规检查误报率过高？

**原因**：规则过于严格或缺少业务理解

**解决方案**：
1. 优化合规规则库
2. 调整检查阈值
3. 增加人工审核豁免条件
4. 定期分析误报案例并优化

### Q5：如何备份和恢复数据？

**备份操作**：
```bash
# 创建备份
tar -czf backup_$(date +%Y%m%d).tar.gz /data/xpertai-content/

# 备份到外部存储
cp backup_*.tar.gz /external_storage/backup/
```

**恢复操作**：
```bash
# 停止工作流
xpertai stop

# 恢复数据
tar -xzf backup_YYYYMMDD.tar.gz -C /

# 重启工作流
xpertai start
```

---

## 版本信息

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| 1.0.0 | 2026-05-01 | 初始版本，基于架构设计文档 |

---

*本文档由 XpertAI 多平台内容自动化系统生成，仅供内部使用*


## 核心摘录

（在这里记录你阅读时的重点摘录）

## 个人解读

（在这里写下你的理解和思考）

## 待验证点

（记录文章中需要查证的信息）

## 关联问题

- 这个概念和其他知识有什么联系？
- 这个观点和我的已有认知是否冲突？

---

## 抓取备注

- 抓取时间：2026-05-08
- 抓取工具：手动导入
- 质量评分：
