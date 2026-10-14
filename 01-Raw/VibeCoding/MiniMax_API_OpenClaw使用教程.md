---
title: MiniMax API 使用教程（OpenClaw 智能体版）
keywords:
- AI平台
- API
- MiniMax
- OpenClaw
- 多模态
state:
  phase: raw
  time_raw: '2026-05-09T00:00:00'
  time_draft: '2026-09-23T00:50:32'
  time_wiki: '2026-09-23T00:53:35'
source_type: document
source_platform: other
author: MiniMax
fetch_date: '2026-05-09'
priority: 3
language: zh
source_url: ''
author_id: ''
publish_date: ''
notes: ''
---

# MiniMax API 使用教程（OpenClaw 智能体版）

## 1. 概述
MiniMax 是覆盖文本、语音、视频、图像、音乐全模态的AI平台，提供多种高性能模型，支持智能体开发。本教程专为OpenClaw智能体设计，帮助快速上手调用MiniMax API。

## 2. 准备工作
### 2.1 开通 Token Plan
1. 访问 [Token Plan 订阅页面](https://platform.minimaxi.com/subscribe/token-plan)，选择适合的套餐（标准版/极速版）。
2. 订阅成功后，前往 [账户管理/Token Plan](https://platform.minimaxi.com/user-center/payment/token-plan) 获取 **Token Plan API Key** 和 **Group ID**。

⚠️ 重要注意：
- 此 API Key 为 Token Plan 专属，与按量计费的 API Key 不可互换
- 仅在订阅有效期内可用，请妥善保管防止泄露
- Group ID 需在多模态接口URL中携带，格式为 `?GroupId=${group_id}`

### 2.2 环境配置
根据所在地区设置API端点：
- 国内用户：`https://api.minimaxi.com/v1`
- 国际用户：`https://api.minimax.io/v1`

## 3. 可用模型列表
### 3.1 文本模型
| 模型名称 | 核心特点 |
|---------|----------|
| MiniMax-M2.7 | 旗舰模型，支持自我迭代，复杂任务能力强 |
| MiniMax-M2.7-highspeed | 与M2.7效果一致，推理速度大幅提升 |
| MiniMax-M2.5 | 顶尖性能与极致性价比平衡 |
| M2-her | 专为角色扮演、长轮次多轮对话场景优化 |

### 3.2 语音模型
| 模型名称 | 核心特点 |
|---------|----------|
| speech-2.8-hd | 高音质，支持自然语气词和情绪渲染 |
| speech-2.8-turbo | 极致生成速度，音质优异 |
| speech-02-hd | 通用场景高性价比选择 |

### 3.3 视频模型
| 模型名称 | 核心特点 |
|---------|----------|
| MiniMax-Hailuo-2.3 | 1080P原生输出，高指令遵循度，支持运镜控制 |
| MiniMax-Hailuo-2.3-Fast | 图生视频优化，生成速度提升50% |

### 3.4 图像模型
| 模型名称 | 核心特点 |
|---------|----------|
| image-01 | 文生图/图生图支持，画面表现细腻，支持人物主体参考 |
| image-01-live | 支持画风控制（漫画/元气/中世纪/水彩等） |

### 3.5 音乐模型
| 模型名称 | 核心特点 |
|---------|----------|
| music-2.6 | 支持文本生成音乐、旋律结构控制、中低频优化 |
| music-cover | 保留旋律骨架，支持风格迁移翻唱重编曲 |

## 4. 文本API调用方式
MiniMax 文本API原生兼容 OpenAI SDK 和 Anthropic SDK，无需额外学习成本即可快速接入。

### 4.1 使用 OpenAI SDK 调用（推荐）
#### 安装依赖
```bash
pip install openai
```

#### 环境变量配置
```bash
export OPENAI_BASE_URL=https://api.minimaxi.com/v1
export OPENAI_API_KEY=${你的Token Plan API Key}
```

#### 调用示例
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="MiniMax-M2.7",
    messages=[
        {"role": "system", "content": "你是一个专业的AI助手，回答简洁准确。"},
        {"role": "user", "content": "介绍一下MiniMax的核心优势"},
    ],
    # 开启思考内容分离（可选）
    extra_body={"reasoning_split": True},
)

# 结果处理
print(f"回复内容: {response.choices[0].message.content}")
print(f"总Token消耗: {response.usage.total_tokens}")

# 查看缓存命中情况
if hasattr(response.usage, 'prompt_tokens_details'):
    print(f"缓存命中Token: {response.usage.prompt_tokens_details.cached_tokens}")
```

### 4.2 使用 Anthropic SDK 调用
#### 安装依赖
```bash
pip install anthropic
```

#### 环境变量配置
```bash
export ANTHROPIC_BASE_URL=https://api.minimaxi.com/anthropic
export ANTHROPIC_API_KEY=${你的Token Plan API Key}
```

#### 调用示例
```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="MiniMax-M2.7",
    system="你是一个专业的AI助手，回答简洁准确。",
    messages=[
        {
            "role": "user",
            "content": "介绍一下MiniMax的核心优势"
        }
    ],
    max_tokens=1024,
)

# 结果处理
for block in response.content:
    if block.type == "text":
        print(f"输出内容: {block.text}")

print(f"输入Token: {response.usage.input_tokens}")
print(f"输出Token: {response.usage.output_tokens}")
print(f"缓存命中Token: {response.usage.cache_read_input_tokens}")
```

## 5. Prompt 缓存功能
MiniMax 提供自动 Prompt 缓存功能，可大幅降低成本和延迟，无需修改调用方式即可自动生效。

### 5.1 适用场景
- 系统提示词在多轮对话中保持不变的场景
- 固定工具定义重复使用的场景
- 长上下文多轮对话历史复用

### 5.2 生效条件
- 输入 Token ≥ 512 个才会触发缓存机制
- 缓存采用前缀匹配，将静态内容放在对话前面可大幅提高命中率

### 5.3 计费优势
缓存命中的Token仅按标准价格的10%左右计费，最高可节省75%成本。

### 5.4 缓存使用最佳实践
1. 静态内容前置：系统提示词、工具定义放在消息最前面
2. 动态内容后置：用户输入、变量内容放在对话最后
3. 定期监控：通过返回的usage字段查看缓存命中率，持续优化提示词结构

### 5.5 缓存信息返回示例
```json
{
  "usage": {
    "prompt_tokens": 1200,
    "completion_tokens": 300,
    "total_tokens": 1500,
    "prompt_tokens_details": {
      "cached_tokens": 800
    }
  }
}
```

## 6. 多模态API调用
MiniMax 全模态API覆盖语音、图像、视频、音乐四大场景，所有接口统一使用Bearer Token鉴权，多模态接口需在URL中携带`GroupId`参数。

### 6.1 语音生成API（T2A）
支持40+语种，提供同步、流式、异步三种调用方式，满足不同场景需求。

#### 6.1.1 同步HTTP调用（短文本场景，<3000字符）
适合3000字符以内的短文本合成，调用后直接返回音频文件。

**Python示例：**
```python
import requests
import os

api_key = os.environ.get("MINIMAX_API_KEY")
group_id = os.environ.get("MINIMAX_GROUP_ID")
url = f"https://api.minimaxi.com/v1/t2a_v2?GroupId={group_id}"

payload = json.dumps({
    "model": "speech-2.8-hd",  # 可选 speech-2.8-turbo/speech-02-hd
    "text": "真正的危险不是计算机开始像人一样思考，而是人开始像计算机一样思考。",
    "stream": False,
    "voice_setting": {
        "voice_id": "male-qn-qingse",  # 可选100+系统音色
        "speed": 1,  # 0.5-2.0
        "vol": 1,  # 0.1-10.0
        "pitch": 0,  # -12到12
        "emotion": "happy"  # 可选happy/sad/angry/neutral等
    },
    "audio_setting": {
        "sample_rate": 32000,  # 8000/16000/24000/32000
        "bitrate": 128000,  # 32000-320000
        "format": "mp3",  # mp3/wav/opus
        "channel": 1  # 1单声道/2立体声
    },
    "output_format": "url"  # url/base64
})

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
result = response.json()

# 获取音频文件
if result["base_resp"]["status_code"] == 0:
    audio_url = result["data"]["audio"]
    print(f"音频生成成功：{audio_url}")
else:
    print(f"生成失败：{result['base_resp']['status_msg']}")
```

#### 6.1.2 WebSocket流式调用（实时播放场景）
适合需要实时播放音频的场景，支持边生成边播放，延迟更低。

**Python示例：**
```python
import asyncio
import websockets
import json
import ssl

async def establish_connection(api_key):
    url = "wss://api.minimaxi.com/ws/v1/t2a_v2"
    headers = {"Authorization": f"Bearer {api_key}"}
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    try:
        ws = await websockets.connect(url, additional_headers=headers, ssl=ssl_context)
        connected = json.loads(await ws.recv())
        if connected.get("event") == "connected_success":
            print("连接成功")
            return ws
        return None
    except Exception as e:
        print(f"连接失败: {e}")
        return None

async def start_task(websocket, text):
    start_msg = {
        "event": "task_start",
        "model": "speech-2.8-hd",
        "voice_setting": {
            "voice_id": "male-qn-qingse",
            "speed": 1,
            "vol": 1,
            "pitch": 0
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": "mp3",
            "channel": 1
        }
    }
    await websocket.send(json.dumps(start_msg))
    response = json.loads(await websocket.recv())
    return response.get("event") == "task_started"

async def continue_task(websocket, text):
    continue_msg = {"event": "task_continue", "text": text}
    await websocket.send(json.dumps(continue_msg))

async def close_connection(websocket):
    if websocket:
        try:
            await websocket.send(json.dumps({"event": "task_finish"}))
            await websocket.close()
        except Exception:
            pass

async def main():
    api_key = os.environ.get("MINIMAX_API_KEY")
    ws = await establish_connection(api_key)
    if ws:
        await start_task(ws, "你好，欢迎使用MiniMax语音合成服务。")
        await close_connection(ws)

if __name__ == "__main__":
    asyncio.run(main())
```

#### 6.1.3 异步长文本调用（>3000字符场景）
适合长文本合成，支持10万字符以内的文本，支持批量处理。

**Python示例：**
```python
import requests
import time

def create_async_tts_task(api_key, group_id, text, voice_id="audiobook_male_1"):
    """创建异步语音合成任务"""
    url = f"https://api.minimaxi.com/v1/t2a_async_v2?GroupId={group_id}"
    payload = json.dumps({
        "model": "speech-2.8-hd",
        "text": text,
        "voice_setting": {
            "voice_id": voice_id,
            "speed": 1,
            "vol": 10,
            "pitch": 1
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": "mp3",
            "channel": 2
        }
    })
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

def query_async_tts_status(api_key, group_id, task_id):
    """查询异步任务状态"""
    url = f"https://api.minimaxi.com/v1/query/t2a_async_query_v2?task_id={task_id}&GroupId={group_id}"
    response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
    return response.json()

# 使用示例
api_key = os.environ.get("MINIMAX_API_KEY")
group_id = os.environ.get("MINIMAX_GROUP_ID")
long_text = "这里是超过3000字符的长文本内容..."

# 创建任务
task_result = create_async_tts_task(api_key, group_id, long_text)
task_id = task_result["task_id"]
print(f"任务已创建，ID：{task_id}")

# 轮询任务状态
while True:
    status_result = query_async_tts_status(api_key, group_id, task_id)
    status = status_result["data"]["task_status"]
    if status == "finished":
        audio_file_id = status_result["data"]["file_id"]
        print(f"任务完成，音频文件ID：{audio_file_id}")
        break
    elif status == "failed":
        print(f"任务失败：{status_result['base_resp']['status_msg']}")
        break
    else:
        print(f"任务进行中：{status}")
        time.sleep(5)
```

#### 6.1.4 语音生成最佳实践
1. **长文本分段**：超过3000字符的文本建议使用异步接口，或手动分段使用同步接口
2. **停顿控制**：在文本中添加`<#1.5#>`标记实现1.5秒的自定义停顿
3. **语种识别**：`language_boost`参数设置为`auto`可自动识别文本语种
4. **音色选择**：有声书场景推荐`audiobook_male_1/audiobook_female_1`，对话场景推荐`conversation_male_1`

### 6.2 图像生成API（image-01）
支持文生图、图生图、人物主体参考，画面细腻，支持多种比例和分辨率。

#### 6.2.1 文生图调用
**Python示例：**
```python
import requests
import os

api_key = os.environ.get("MINIMAX_API_KEY")
group_id = os.environ.get("MINIMAX_GROUP_ID")
url = f"https://api.minimaxi.com/v1/image_generation?GroupId={group_id}"

payload = json.dumps({
    "model": "image-01",  # 可选 image-01/image-01-live
    "prompt": "90年代时尚摄影，一名穿着白色T恤的男性全身正面站立，背景是威尼斯海滩，胶片质感，真实感强",
    "aspect_ratio": "16:9",  # 可选 1:1/16:9/4:3/3:2/2:3/3:4/9:16/21:9
    "width": 1280,  # 512-2048，需为8的倍数
    "height": 720,  # 512-2048，需为8的倍数
    "response_format": "url",  # url/base64，url有效期24小时
    "n": 3,  # 1-9，单次生成数量
    "prompt_optimizer": True,  # 自动优化提示词
    "aigc_watermark": False  # 是否添加水印
})

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
result = response.json()

if result["base_resp"]["status_code"] == 0:
    image_urls = result["data"]["image_urls"]
    for i, url in enumerate(image_urls):
        print(f"生成图片{i+1}：{url}")
    print(f"成功生成{result['metadata']['success_count']}张图片")
else:
    print(f"生成失败：{result['base_resp']['status_msg']}")
```

#### 6.2.2 人物主体参考图生图
保持指定人物的面部特征，生成不同场景、姿势的图片。

**Python示例：**
```python
payload = json.dumps({
    "model": "image-01",
    "prompt": "穿着红色连衣裙的女性站在巴黎埃菲尔铁塔前，日落时分，电影质感",
    "subject_reference": [
        {
            "type": "character",
            "image_file": "https://example.com/portrait.jpg"  # 支持URL或Base64
        }
    ],
    "aspect_ratio": "3:4",
    "response_format": "url",
    "n": 2
})
```

#### 6.2.3 图像生成最佳实践
1. **提示词结构**：主体描述 + 场景 + 风格 + 画质关键词（如“8K、RAW、胶片质感”）
2. **人物一致性**：使用`subject_reference`参数上传清晰的正面单人照，可保持人物特征稳定
3. **分辨率控制**：建议整体分辨率不超过200万像素（如1280×720=92万像素），避免生成失败
4. **画风控制**：使用`image-01-live`模型可设置`style`参数，支持漫画、元气、中世纪、水彩等画风

### 6.3 视频生成API（Hailuo 2.3）
支持文生视频、图生视频，1080P原生输出，支持15种运镜指令，画面流畅自然。

#### 6.3.1 文生视频调用
**Python示例：**
```python
import requests
import time

api_key = os.environ.get("MINIMAX_API_KEY")
group_id = os.environ.get("MINIMAX_GROUP_ID")
create_url = f"https://api.minimaxi.com/v1/video_generation?GroupId={group_id}"
query_url = f"https://api.minimaxi.com/v1/query/video_generation_query?GroupId={group_id}"

# 1. 创建视频生成任务
payload = json.dumps({
    "model": "MiniMax-Hailuo-2.3",  # 可选 MiniMax-Hailuo-2.3-Fast（更快）
    "prompt": "一只橘猫在阳光明媚的草地上奔跑，蝴蝶在周围飞舞，[推进]镜头跟随猫咪移动",
    "duration": 6,  # 6/10秒，1080P仅支持6秒
    "resolution": "768P",  # 768P/1080P，10秒仅支持768P
    "prompt_optimizer": True,  # 自动优化提示词
    "fast_pretreatment": False,  # 开启可缩短预处理时间
    "aigc_watermark": False
})

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

create_response = requests.post(create_url, headers=headers, data=payload)
create_result = create_response.json()

if create_result["base_resp"]["status_code"] == 0:
    task_id = create_result["task_id"]
    print(f"视频任务已创建，ID：{task_id}")
else:
    print(f"任务创建失败：{create_result['base_resp']['status_msg']}")
    exit()

# 2. 轮询任务状态（视频生成通常需要1-3分钟）
while True:
    query_params = {"task_id": task_id}
    query_response = requests.get(query_url, headers=headers, params=query_params)
    query_result = query_response.json()
    
    status = query_result["data"]["task_status"]
    if status == "finished":
        video_url = query_result["data"]["video_url"]
        print(f"视频生成成功：{video_url}")
        break
    elif status == "failed":
        print(f"生成失败：{query_result['base_resp']['status_msg']}")
        break
    else:
        print(f"生成进度：{query_result['data']['progress']}%")
        time.sleep(10)
```

#### 6.3.2 图生视频调用
指定首帧图片生成视频，保持图片内容的连贯性。

**Python示例：**
```python
payload = json.dumps({
    "model": "MiniMax-Hailuo-2.3",
    "prompt": "海浪轻轻拍打着沙滩，海鸥在天空飞过，[左摇]镜头缓慢移动",
    "first_frame_image": "https://example.com/beach.jpg",  # 支持URL或Base64
    "duration": 6,
    "resolution": "1080P",
    "prompt_optimizer": True
})
```

#### 6.3.3 运镜指令说明
Hailuo 2.3支持15种精确运镜指令，在prompt中使用`[指令名]`格式添加：
| 类别 | 指令 | 效果 |
|------|------|------|
| 左右移 | [左移]/[右移] | 镜头水平左右移动 |
| 左右摇 | [左摇]/[右摇] | 镜头水平左右转动 |
| 推拉 | [推进]/[拉远] | 镜头向前推进或向后拉远 |
| 升降 | [上升]/[下降] | 镜头垂直上下移动 |
| 上下摇 | [上摇]/[下摇] | 镜头垂直上下转动 |
| 变焦 | [变焦推近]/[变焦拉远] | 镜头焦距变化，不改变位置 |
| 其他 | [晃动]/[跟随]/[固定] | 手持晃动效果/跟随主体移动/固定镜头 |

**使用规则：**
- 组合运镜：同一`[]`内可添加多个指令，如`[左摇,上升]`
- 顺序运镜：prompt中前后的指令依次生效，如`[推进]然后[拉远]`
- 自然语言：也可直接用自然语言描述运镜，但标准指令效果更精准

#### 6.3.4 视频生成最佳实践
1. **运镜搭配**：复杂场景建议组合2-3种运镜，避免过多指令导致画面混乱
2. **时长选择**：768P支持10秒时长适合长镜头叙事，1080P 6秒适合短视频场景
3. **提示词优化**：建议包含主体、动作、场景、光影、运镜五个要素，如“一只金毛犬在森林里叼着飞盘奔跑，阳光透过树叶洒下，[跟随]镜头”
4. **首帧质量**：图生视频建议上传高清、构图清晰的首帧图片，可大幅提升最终视频质量

### 6.4 音乐生成API（Music 2.6）
支持文本生成音乐、Cover翻唱重编曲，支持BPM、调性、情绪控制，音乐风格丰富。

#### 6.4.1 文生音乐调用
**Python示例：**
```python
import requests
import os

api_key = os.environ.get("MINIMAX_API_KEY")
group_id = os.environ.get("MINIMAX_GROUP_ID")
url = f"https://api.minimaxi.com/v1/music_generation?GroupId={group_id}"

payload = json.dumps({
    "model": "music-2.6",
    "prompt": "轻快的城市流行音乐，120BPM，钢琴和吉他伴奏，适合vlog背景音乐，时长30秒",
    "duration": 30,  # 10-300秒
    "bpm": 120,  # 可选，60-200
    "key": "C major",  # 可选，调性设置
    "output_format": "url",
    "n": 1  # 1-2
})

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
result = response.json()

if result["base_resp"]["status_code"] == 0:
    music_url = result["data"]["audio_urls"][0]
    print(f"音乐生成成功：{music_url}")
else:
    print(f"生成失败：{result['base_resp']['status_msg']}")
```

#### 6.4.2 Cover翻唱重编曲
上传现有歌曲，提取旋律骨架，重新编曲和换风格。

**Python示例：**
```python
# 1. 预处理参考音频（免费，提取旋律骨架）
preprocess_url = f"https://api.minimaxi.com/v1/music_cover_preprocess?GroupId={group_id}"
preprocess_payload = json.dumps({
    "model": "music-cover",
    "audio_url": "https://example.com/original_song.mp3"
})
preprocess_response = requests.post(preprocess_url, headers=headers, data=preprocess_payload)
preprocess_result = preprocess_response.json()
cover_feature_id = preprocess_result["data"]["cover_feature_id"]

# 2. 生成翻唱版本
cover_url = f"https://api.minimaxi.com/v1/music_cover_generation?GroupId={group_id}"
cover_payload = json.dumps({
    "model": "music-cover",
    "cover_feature_id": cover_feature_id,
    "prompt": "重金属摇滚风格，电吉他solo，强劲鼓点",
    "keep_vocal": False,  # 是否保留原有人声
    "duration": 180,
    "output_format": "url"
})
cover_response = requests.post(cover_url, headers=headers, data=cover_payload)
cover_result = cover_response.json()
```

#### 6.4.3 OpenClaw 音乐Skill集成
MiniMax 官方提供三个开源Music Skill，可直接集成到OpenClaw智能体：
1. **minimax-music-gen**：核心音乐生成引擎，支持文生音乐、纯音乐、Cover三种模式
2. **buddy-sings**：读取智能体角色性格，匹配音色和风格，生成角色专属歌曲
3. **minimax-music-playlist**：分析用户听歌偏好，构建品味画像，自动生成整份原创歌单

**OpenClaw集成示例：**
```yaml
# OpenClaw Skill配置
skills:
  - name: minimax-music-gen
    source: https://github.com/MiniMax-AI/skills/tree/main/music-gen
    parameters:
      api_key: ${MINIMAX_API_KEY}
      group_id: ${MINIMAX_GROUP_ID}
```

#### 6.4.4 音乐生成最佳实践
1. **风格描述**：prompt中明确说明音乐风格（如“lo-fi嘻哈”、“国风古风”）、使用场景（如“vlog背景音乐”、“游戏Boss战”）
2. **结构控制**：可在prompt中描述段落结构，如“前奏轻快→主歌舒缓→副歌高潮→ outro渐弱”
3. **BPM设置**：电子音乐建议120-140BPM，抒情歌曲建议60-90BPM，节奏类建议90-120BPM
4. **Cover优化**：上传人声清晰的原歌曲，可获得更准确的旋律提取，建议使用无和声的干声版本

## 7. Token Plan 用量管理
### 7.1 套餐用量速查表
#### 标准版套餐
| 模型类型 | Starter | Plus | Max |
|----------|---------|------|-----|
| M2.7文本 | 600次/5小时 | 1500次/5小时 | 4500次/5小时 |
| Speech 2.8语音 | - | 4000字符/日 | 11000字符/日 |
| image-01图像 | - | 50张/日 | 120张/日 |
| Hailuo 2.3视频 | - | - | 2个/日 |
| Music-2.6音乐 | 100首/天（限免） | 100首/天（限免） | 100首/天（限免） |

#### 极速版套餐
| 模型类型 | Plus-极速版 | Max-极速版 | Ultra-极速版 |
|----------|-------------|------------|--------------|
| M2.7-highspeed | 1500次/5小时 | 4500次/5小时 | 30000次/5小时 |
| Speech 2.8语音 | 9000字符/日 | 19000字符/日 | 50000字符/日 |
| image-01图像 | 100张/日 | 200张/日 | 800张/日 |
| Hailuo 2.3视频 | - | 3个/日 | 5个/日 |
| Music-2.6音乐 | 100首/天（限免） | 100首/天（限免） | 100首/天（限免） |

### 7.2 用量重置规则
- **M2.7系列**：采用5小时滚动窗口重置，不是整点固定重置
- **其他模型**：按自然日每日0点自动重置配额

### 7.3 超限处理方案
#### 文本模型（M2.7）达到上限
1. **切换按量计费**：替换为按量计费API Key，按实际Token消耗从账户余额扣费
2. **等待额度恢复**：暂停使用，5小时滚动窗口会自动逐步释放额度

#### 非文本模型达到每日配额
1. **切换按量计费**：使用按量计费API Key继续调用对应模型
2. **等待次日重置**：每日0点自动恢复所有非文本模型配额

## 8. OpenClaw 智能体最佳实践
1. **缓存优先策略**：智能体系统提示词、工具定义等长静态内容尽量前置，最大化利用缓存降低成本
2. **模型动态选型**：普通对话和工具调用使用highspeed模型提高响应速度，复杂推理任务使用标准模型保证质量
3. **密钥分级管理**：分别存储Token Plan和按量计费API Key，在Token Plan超限时自动无缝切换
4. **用量监控**：定期检查API返回的usage信息，及时调整调用策略避免超限
5. **多模态能力组合**：结合文本+语音+视频能力，实现智能体语音交互、视频内容生成等复杂场景
6. **错误处理机制**：添加请求重试机制，遇到配额超限错误时自动切换模型或等待恢复，遇到参数错误时自动修正重试

## 9. 官方资源链接
- [完整文档索引](https://platform.minimaxi.com/docs/llms.txt)
- [Token Plan 订阅页面](https://platform.minimaxi.com/subscribe/token-plan)
- [API 参考文档总览](https://platform.minimaxi.com/docs/api-reference)
- [AI编程工具配置指南](https://platform.minimaxi.com/docs/guides/text-ai-coding-tools)
- [OpenClaw Skill开源仓库](https://github.com/MiniMax-AI/skills)