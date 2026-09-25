---
title: Hermes-Agent接入飞书-企业自建应用与长连接配置
source: Bilibili 视频转写（1 篇）；本页为我们的提炼
keywords:
- Hermes-Agent
- 飞书
- IM工具
- integration-tutorial
- setup
state:
  phase: draft
  time_raw: '2026-05-07T00:00:00'
  time_draft: '2026-09-23T01:05:00'
sources:
- Bilibili/bilibili-BV1DMDnBNEXj-hermes-agent-feishu-integration-tutorial.md
related:
- '[[hermes-agent-15-技巧-5-心法]]'
wiki_target: false
wiki_note: 参考层：工具/视频类实操经验（用户已掌握，部分内容过时）→ 不进 Wiki
---

# Hermes Agent 接入飞书：企业自建应用 + 长连接配置

> **核实状态（2026-09-23）**：本页配置项已对照**官方文档** `website/docs/user-guide/messaging/feishu.md`（本机 hermes-agent 仓库，v0.21.0）逐条核对。原视频（2026-04-09）当时的官方文档**确实没有**飞书权限清单，作者借用了 OpenAI 的清单；**现在官方文档已给出完整清单**，本页以官方为准。

## 结论

接入后**脱离终端**：无论电脑还是手机，发一条消息 AI 就开始干活，定时任务的结果也会直接推送到聊天窗口。**现在最省事的路径是「扫码自动建应用」**——`hermes gateway setup` 选 Feishu/Lark 后扫二维码，Hermes 会自动创建带正确权限的机器人应用并保存凭证；手工配置仍可用。核心配置只有三件事：**权限清单**、**事件订阅（长连接）**、**应用发版**。

## 一、为什么接：Gateway 的角色

Hermes 内置一个 **Gateway** 进程，专门负责接入聊天平台，支持 Telegram、飞书、Discord、Slack、钉钉、企业微信、WhatsApp 等约 20 个平台，**全部跑在同一个网关**（一个进程管所有平台）。

接入后的实际收益：
- 不用开终端，手机上就能驱动 agent；
- 定时任务的结果直接推送到聊天窗口；
- **记忆连续性**：在 TUI 里做过的事，换到飞书应用里照样能通过会话搜索回忆起来，甚至能找到上次自动沉淀的技能。

## 二、飞书侧配置

### 2.1 建应用（两条路，优先第一条）

| 路径 | 做法 |
|:---|:---|
| **① 扫码自动创建（推荐）** | 运行 `hermes gateway setup` → 选 **Feishu / Lark** → 用飞书手机端扫码。Hermes 自动创建机器人应用、配好正确权限、保存凭证 |
| ② 手工创建 | 飞书开放平台（国内 `open.feishu.cn`／国际 `open.larksuite.com`）→ 创建应用 → 在**凭证与基础信息**取 **App ID / App Secret** → 启用**机器人**能力 → 再跑 `hermes gateway setup` 选 Feishu/Lark 填入凭证 |

> ⚠️ **App Secret 必须保密**（持有者可冒充你的应用）。

### 2.2 权限清单（官方口径，支持批量导入）

在开放平台**权限管理**页添加以下 scope：

**必需权限**

| Scope | 用途 |
|:---|:---|
| `im:message` | 接收与读取消息 |
| `im:message:send_as_bot` | 以机器人身份发消息 |
| `im:resource` | 访问用户发来的图片/文件/音频 |
| `im:chat` | 访问会话/群元数据 |
| `im:chat:readonly` | 读取会话列表与成员 |

**推荐权限（完整功能）**

| Scope | 用途 |
|:---|:---|
| `im:message.reactions:readonly` | 接收表情回应事件 |
| `admin:app.info:readonly` | 自动识别机器人身份，用于 @提及 门控 |
| `contact:user.id:readonly` | 解析用户 ID，用于白名单匹配 |

> 历史说明：2026-04 的视频里作者因官方未给清单而**参考了 OpenAI 的飞书权限段**。现已不需要——直接用上表，并遵循最小权限原则（身份类权限开通前自行核对）。

### 2.3 事件订阅

在**事件与回调**里：
1. 连接方式选 **长连接（WebSocket）**（推荐；也支持配置 webhook URL）；
2. 事件配置订阅 **`im.message.receive_v1`**（接收消息必需，仅此一个）。

### 2.4 发布应用（权限生效的前提）

配置完权限与事件后，去**版本管理发布新版本**。**权限在发版并通过审核后才生效**；企业自建应用可能还需管理员审批。

## 三、Hermes 侧配置

**交互式（推荐）**：`hermes gateway setup` → 选 Feishu / Lark → 按提示填凭证。

**手工（写入 `~/.hermes/.env`）**：

```bash
FEISHU_APP_ID=cli_xxx
FEISHU_APP_SECRET=secret_xxx
FEISHU_DOMAIN=feishu              # 国际版填 lark
FEISHU_CONNECTION_MODE=websocket  # 或 webhook
```

- **连接模式**：`websocket`（默认，无需公网，SDK 负责心跳与自动重连；需装 `websockets` 包）／`webhook`（需公网可达，Hermes 起 HTTP 服务，默认端点 `/feishu/webhook`，需装 `aiohttp`）。
- **白名单**：`FEISHU_ALLOWED_USERS` —— 只有被允许的用户能与机器人对话。**安全关键项，必设。**
- webhook 模式下可另设 `FEISHU_WEBHOOK_HOST/PORT/PATH`、`FEISHU_VERIFICATION_TOKEN`（校验回调来源）。

配置后**重启网关**生效。

## 四、配对与验证

1. 在飞书里给应用发消息 → 应用回 **OK** 标记（表示已接收）；
2. 应用返回**配对命令** → 复制到终端执行完成配对；
3. 再发消息 → 收到 Hermes Agent 回复，端到端接通。

## 五、安全（必做）

- **必须设白名单**（`FEISHU_ALLOWED_USERS`）；
- **App Secret / Token 保密**，泄露立刻在平台重新生成并更新配置；
- 权限按最小必要开通，身份类权限事前核对；
- **发版是权限生效的前提**——只配不发布 = 配置全部不生效。

## 六、可迁移要点

这套流程对任何「**企业自建应用 + 长连接**」型 IM 平台都成立：造应用（或扫码自动建）→ 授权限 → 定事件订阅方式（长连接免公网）→ **发版** → 取凭证 → 网关配置 → 配对验证 → 白名单兜底 → 重启网关。换平台时变的只是权限清单、事件名与环境变量名。

## 关联与核实记录

- 与 `[[hermes-agent-15-技巧-5-心法]]` 互补：那篇讲使用技巧，这篇讲接入配置。
- **已核实**：权限清单、扫码建应用、事件名 `im.message.receive_v1`、连接模式环境变量、发版要求、白名单变量名 —— 均来自官方文档 `website/docs/user-guide/messaging/feishu.md`（v0.21.0 本机仓库）。
- **本页相对原视频的修正**：① 官方现已提供权限清单（原视频没有，借用 OpenAI）；② 新增扫码自动建应用路径；③ 补齐 `FEISHU_*` 环境变量与白名单变量名。
- **仍待核**：配对命令的具体形式随版本变化，以实际输出为准。
