---
title: "Anthropic 开发者文档 · </CardGroup> · Cloud sandbox reference"
source: Anthropic 开发者文档（官方一手，英文）
source_url: https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference
description: ": Pre-installed packages, databases, and utilities available in cloud sandboxes."
evidence: E1
domain: VibeCoding
lang: en
keywords: ["Anthropic", "AI-Agent", "prompt-engineering", "vibe-coding"]
state:
  phase: raw
  time_raw: 2026-09-23T03:00:00+08:00
  time_draft: 2026-09-23T02:51:20+08:00
  time_wiki: null
related:
---

> 溯源：Anthropic 官方文档全文（llms-full.txt 官方机器可读版，证据等级 E1）。抓取 2026-09-23T03:00:00+08:00。
> 原始地址：https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference

Cloud sandboxes run as isolated Linux containers on Anthropic-managed infrastructure. They come pre-installed with a comprehensive set of programming languages, databases, and utilities. The agent can use these immediately without any installation steps.

These specifications apply to `cloud` environments. Self-hosted sandboxes run on your infrastructure with whatever your worker provides.

## Programming languages

| Language | Version                     | Package manager      |
| -------- | --------------------------- | -------------------- |
| Python   | 3.10, 3.11, 3.12, and 3.13  | pip, uv, poetry      |
| Node.js  | 20, 21, and 22 (default)    | npm, yarn, pnpm, bun |
| Go       | 1.24 (default) and 1.25     | go modules           |
| Rust     | Stable toolchain (rustup)   | cargo                |
| Java     | OpenJDK 21                  | maven, gradle        |
| Ruby     | 3.1, 3.2, and 3.3 (default) | bundler, gem         |
| PHP      | 8.3                         | composer             |
| C/C++    | GCC 13 and Clang            | make, cmake, ninja   |

Common Python data and document libraries, including NumPy, pandas, Matplotlib, openpyxl, python-docx, python-pptx, and pypdf, are installed for the `python3` interpreter.

## Databases

| Database      | Description                                                                   |
| ------------- | ----------------------------------------------------------------------------- |
| PostgreSQL 16 | Server and `psql` client are installed. The server is not running by default. |
| Redis 7       | Server and `redis-cli` are installed. The server is not running by default.   |
| SQLite        | Available through language bindings, such as Python's `sqlite3` module.       |

## Utilities

### System tools

* `git` - Version control
* `curl`, `wget` - HTTP clients
* `jq`, `yq` - JSON and YAML processing
* `tar`, `zip`, `unzip` - Archive tools
* `tmux` - Terminal multiplexer

### Development tools

* `make`, `cmake` - Build systems
* `docker` - Container management (limited availability)
* `ripgrep` (`rg`) - Fast file search

### Text processing

* `sed`, `awk`, `grep` - Stream editors
* `vim`, `nano` - Text editors
* `diff`, `patch` - File comparison

### Document and media processing

* `ffmpeg` - Audio and video processing
* ImageMagick (`convert`, `identify`) - Image manipulation
* `pandoc` - Document conversion
* LibreOffice (headless) - Office document conversion
* Poppler utilities (`pdftotext`, `pdftoppm`) and `qpdf` - PDF processing
* `tesseract` - Optical character recognition (English language data)
* TeX Live (`pdflatex`, `xelatex`, `latexmk`) - Typesetting

### Browser automation

* Playwright (Python and Node.js) - Browser automation library
* Chromium (`/opt/pw-browsers/chromium`) - Browser used by Playwright, not on `PATH`

The sandbox sets `PLAYWRIGHT_BROWSERS_PATH` to `/opt/pw-browsers`, so the pre-installed Playwright packages find Chromium there without configuration. The Python package is installed for the `python3` interpreter. Use the pre-installed packages rather than installing another Playwright version, which would look for a browser build that is not present. Firefox and WebKit are not installed.

## Sandbox specifications

| Property         | Value                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operating system | Ubuntu 24.04 LTS                                                                                                                                                                                              |
| Architecture     | x86\_64 (amd64)                                                                                                                                                                                               |
| Memory           | Up to 8 GB                                                                                                                                                                                                    |
| Disk space       | Up to 10 GB                                                                                                                                                                                                   |
| Network          | API-created environments default to [`unrestricted` networking](https://platform.claude.com/docs/en/managed-agents/environments#networking); sandboxes provisioned through Claude Studio default to `limited` |


### Configure agent environment > Self-hosted sandboxes
