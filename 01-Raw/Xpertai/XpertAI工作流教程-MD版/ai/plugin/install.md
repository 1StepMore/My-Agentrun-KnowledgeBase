---
title: Publish & Use
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
# Publish & Use

> 此文档为原始素材，请勿直接修改。编译后的知识请移步 `02-Draft/` 目录。

## 原文内容

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish & Use

After developing your plugin, the final step is to publish it to npm and enable it in the host system (Xpert AI).

## Publish Plugin

Run the following commands in the monorepo root directory:

```bash theme={null}
# Build the plugin
npx nx build my-plugin

# Use the monorepo's release workflow
npx nx release

# Or manually publish to npm
npx nx run @xpert-ai/my-plugin:nx-release-publish --access public --otp=<one-time-password-if-needed>
```

Once published, you'll get an installable package on npm, for example:

```
@xpert-ai/my-plugin
```

## Use Plugin

In the Xpert AI host system, declare the list of enabled plugins using the `PLUGINS` environment variable. Separate multiple plugins with commas:

```bash theme={null}
PLUGINS=@xpert-ai/my-plugin1,@xpert-ai/my-plugin2
```

When the host starts, it will automatically parse the `PLUGINS` environment variable and load these plugins in order.

**Notes**:

* The host project should install the plugin packages via npm/yarn/pnpm (`npm install @xpert-ai/my-plugin`) and configure the plugin list in the environment variable.
* The plugin's `meta.name` must match the npm package name.
* If a plugin fails to load correctly, check the logs for `register` or `onPluginBootstrap` output.
* After starting the Xpert AI system, you can view the loaded plugins on the system settings [Plugins page](https://app.xpertai.cn/settings/plugins).


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
