---
title: "opencode 官方文档 · HTTPS proxy (recommended)"
source: opencode 官方文档（官方一手文档）
source_url: https://opencode.ai/docs/network
evidence: E1
domain: VibeCoding
lang: en
keywords: ["opencode", "vibe-coding", "AI编程", "claude-code"]
state:
  phase: raw
  time_raw: 2026-09-23T02:44:23+08:00
  time_draft: 2026-09-23T02:45:52+08:00
  time_wiki: null
related:
---

> 溯源：opencode 官方文档 官方原文（证据等级 E1 = 官方一手）。抓取时间 2026-09-23T02:44:23+08:00。
> 原始地址：https://opencode.ai/docs/network

OpenCode supports standard proxy environment variables and custom certificates for enterprise network environments.

---

## Proxy

OpenCode respects standard proxy environment variables.

```bash
# HTTPS proxy (recommended)
export HTTPS_PROXY=https://proxy.example.com:8080

# HTTP proxy (if HTTPS not available)
export HTTP_PROXY=http://proxy.example.com:8080

# Bypass proxy for local server (required)
export NO_PROXY=localhost,127.0.0.1
```

:::caution
The TUI communicates with a local HTTP server. You must bypass the proxy for this connection to prevent routing loops.
:::

You can configure the server's port and hostname using [CLI flags](/docs/cli#run).

---

### Authenticate

If your proxy requires basic authentication, include credentials in the URL.

```bash
export HTTPS_PROXY=http://username:password@proxy.example.com:8080
```

:::caution
Avoid hardcoding passwords. Use environment variables or secure credential storage.
:::

For proxies requiring advanced authentication like NTLM or Kerberos, consider using an LLM Gateway that supports your authentication method.

---

## Custom certificates

If your enterprise uses custom CAs for HTTPS connections, configure OpenCode to trust them.

```bash
export NODE_EXTRA_CA_CERTS=/path/to/ca-cert.pem
```

This works for both proxy connections and direct API access.
