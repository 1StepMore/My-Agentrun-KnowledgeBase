---
title: Publish & Use
source: XpertAI 官方文档
related: []
keywords:
- XpertAI
state:
  phase: wiki
  time_raw: '2026-07-01T12:42:25'
  time_draft: '2026-07-01T12:42:25'
  time_wiki: '2026-07-01T12:42:25'
sources:
- Xpertai/XpertAI工作流教程-MD版/ai/plugin/install.md
---
# Publish & Use

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
