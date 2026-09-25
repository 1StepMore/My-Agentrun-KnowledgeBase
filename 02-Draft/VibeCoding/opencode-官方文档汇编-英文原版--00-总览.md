---
title: opencode 官方文档汇编（英文原版） · 00-总览
source: opencode 官方文档（官方一手，逐篇原始地址见正文）
sources:
- VibeCoding/opencode/opencode-.md
- VibeCoding/opencode/opencode-zh-tw.md
evidence: E1
domain: VibeCoding
keywords:
- opencode
- vibe-coding
- AI编程
- claude-code
state:
  phase: draft
  time_raw: 2026-09-23 02:44:23+08:00
  time_draft: 2026-09-23 03:14:06+08:00
  time_wiki: null
wiki_target: false
wiki_note: 双语冗余：中文版已消化并入库
---

> **汇编性质**：opencode 官方文档 官方原文 2 页，按官方结构合并，逐节保留原始 URL。本汇编**不做改写**（一手来源改写会引入二手误差），可逐节回溯官方原文。
> 证据等级：E1（官方一手）。汇编时间：2026-09-23T03:14:06+08:00

---

## Intro

- 官方原文：https://opencode.ai/docs/
- 存档：`01-Raw/VibeCoding/opencode/opencode-.md`

# Intro

Get started with OpenCode. 

OpenCode is an open source AI coding agent. It’s available as a terminal-based interface, desktop app, or IDE extension.

Let’s get started.
 

#### Prerequisites

To use OpenCode in your terminal, you’ll need:
 

- A modern terminal emulator like:

WezTerm, cross-platform

- Alacritty, cross-platform

- Ghostty, Linux and macOS

- Kitty, Linux and macOS
 
 

- API keys for the LLM providers you want to use.
 
 

## Install

The easiest way to install OpenCode is through the install script.
 
- Terminal windowcurl -fsSL https://opencode.ai/install | bash
You can also install it with the following commands:

Using Node.js
 npm
- Bun
- pnpm
- Yarn Terminal window 

npm install -g opencode-ai Terminal windowbun install -g opencode-ai Terminal windowpnpm install -g opencode-ai Terminal windowyarn global add opencode-ai 

- Using Homebrew on macOS and Linux
Terminal windowbrew install anomalyco/tap/opencode

We recommend using the OpenCode tap for the most up to date releases. The official brew install opencode formula is maintained by the Homebrew team and is updated less frequently.

- Installing on Arch Linux
Terminal windowsudo pacman -S opencode # Arch Linux (Stable)paru -S opencode-bin # Arch Linux (Latest from AUR)

#### Windows

 Recommended: Use WSL 

For the best experience on Windows, we recommend using Windows Subsystem for Linux (WSL). It provides better performance and full compatibility with OpenCode’s features. 
 

- Using Chocolatey
Terminal windowchoco install opencode

- Using Scoop
Terminal windowscoop install opencode

- Using NPM
Terminal windownpm install -g opencode-ai

- Using Mise
Terminal windowmise use -g github:anomalyco/opencode

- Using Docker
Terminal windowdocker run -it --rm ghcr.io/anomalyco/opencode
 

Support for installing OpenCode on Windows using Bun is currently in progress.

You can also grab the binary from the Releases.
 

## Configure

With OpenCode you can use any LLM provider by configuring their API keys.

If you are new to using LLM providers, we recommend using OpenCode Zen.
It’s a curated list of models that have been tested and verified by the OpenCode
team.
 

- Run the /connect command in the TUI, select opencode, and head to opencode.ai/auth.
/connect

- Sign in, add your billing details, and copy your API key.

- Paste your API key.
┌ API key││└ enter
 

Alternatively, you can select one of the other providers. Learn more.
 

## Initialize

Now that you’ve configured a provider, you can navigate to a project that
you want to work on.
 Terminal window 

cd /path/to/project
And run OpenCode.
 Terminal window 

opencode
Next, initialize OpenCode for the project by running the following command.
 

/init
This will get OpenCode to analyze your project and create an AGENTS.md file in
the project root.
 

Tip 

You should commit your project’s AGENTS.md file to Git. 

This helps OpenCode understand the project structure and the coding patterns
used.
 

## Usage

You are now ready to use OpenCode to work on your project. Feel free to ask it
anything!

If you are new to using an AI coding agent, here are some examples that might
help.
 

### Ask questions

You can ask OpenCode to explain the codebase to you.
 

Tip 

Use the @ key to fuzzy search for files in the project. 
 

How is authentication handled in @packages/functions/src/api/index.ts
This is helpful if there’s a part of the codebase that you didn’t work on.
 

### Add features

You can ask OpenCode to add new features to your project. Though we first recommend asking it to create a plan.
 

- Create a plan
OpenCode has a Plan mode that disables its ability to make changes and
instead suggest how it’ll implement the feature.
Switch to it using the Tab key. You’ll see an indicator for this in the lower right corner.
&#x3C;TAB>">
Now let’s describe what we want it to do.
When a user deletes a note, we'd like to flag it as deleted in the database.Then create a screen that shows all the recently deleted notes.From this screen, the user can undelete a note or permanently delete it.
You want to give OpenCode enough details to understand what you want. It helps
to talk to it like you are talking to a junior developer on your team.
 TipGive OpenCode plenty of context and examples to help it understand what you
want.

- Iterate on the plan
Once it gives you a plan, you can give it feedback or add more details.
We'd like to design this new screen using a design I've used before.[Image #1] Take a look at this image and use it as a reference.
 TipDrag and drop images into the terminal to add them to the prompt.
OpenCode can scan any images you give it and add them to the prompt. You can
do this by dragging and dropping an image into the terminal.

- Build the feature
Once you feel comfortable with the plan, switch back to Build mode by
hitting the Tab key again.
&#x3C;TAB>">
And asking it to make the changes.
Sounds good! Go ahead and make the changes.
 
 

### Make changes

For more straightforward changes, you can ask OpenCode to directly build it
without having to review the plan first.
 

We need to add authentication to the /settings route. Take a look at how this ishandled in the /notes route in @packages/functions/src/notes.ts and implementthe same logic in @packages/functions/src/settings.ts
You want to make sure you provide a good amount of detail so OpenCode makes the right
changes.
 

### Undo changes

Let’s say you ask OpenCode to make some changes.
 

Can you refactor the function in @packages/functions/src/api/index.ts?
But you realize that it is not what you wanted. You can undo the changes
using the /undo command.
 

/undo
OpenCode will now revert the changes you made and show your original message
again.
 

Can you refactor the function in @packages/functions/src/api/index.ts?
From here you can tweak the prompt and ask OpenCode to try again.
 

Tip 

You can run /undo multiple times to undo multiple changes. 

Or you can redo the changes using the /redo command.
 

/redo

## Share

The conversations that you have with OpenCode can be shared with your
team.
 

/share
This will create a link to the current conversation and copy it to your clipboard.
 

Note 

Conversations are not shared by default. 

Here’s an example conversation with OpenCode.
 

## Customize

And that’s it! You are now a pro at using OpenCode.

To make it your own, we recommend picking a theme, customizing the keybinds, configuring code formatters, creating custom commands, or playing around with the OpenCode config.

---

## zh-tw

- 官方原文：https://opencode.ai/docs/zh-tw/
- 存档：`01-Raw/VibeCoding/opencode/opencode-zh-tw.md`

export const console = config.console

[**OpenCode**](/) 是一個開源的 AI 編碼代理。它提供終端機介面、桌面應用程式和 IDE 擴充功能等多種使用方式。

讓我們開始吧。

---

#### 前提條件

要在終端機中使用 OpenCode，您需要：

1. 一款現代終端機模擬器，例如：
   - [WezTerm](https://wezterm.org)，跨平台
   - [Alacritty](https://alacritty.org)，跨平台
   - [Ghostty](https://ghostty.org)，Linux 和 macOS
   - [Kitty](https://sw.kovidgoyal.net/kitty/)，Linux 和 macOS

2. 您想使用的 LLM 供應商的 API 金鑰。

---

## 安裝

安裝 OpenCode 最簡單的方法是透過安裝指令碼。

```bash
curl -fsSL https://opencode.ai/install | bash
```

您也可以使用以下方式安裝：

- **使用 Node.js**

      ```bash
      npm install -g opencode-ai
      ```

        ```bash
        bun install -g opencode-ai
        ```

        ```bash
        pnpm install -g opencode-ai
        ```

        ```bash
        yarn global add opencode-ai
        ```

- **在 macOS 和 Linux 上使用 Homebrew**

  ```bash
  brew install anomalyco/tap/opencode
  ```

  > 我們推薦使用 OpenCode tap 以取得最新版本。官方的 `brew install opencode` formula 由 Homebrew 團隊維護，更新頻率較低。

- **在 Arch Linux 上安裝**

  ```bash
  sudo pacman -S opencode           # Arch Linux (Stable)
  paru -S opencode-bin              # Arch Linux (Latest from AUR)
  ```

#### Windows

:::tip[推薦：使用 WSL]
為了在 Windows 上獲得最佳體驗，我們推薦使用 [Windows Subsystem for Linux (WSL)](/docs/windows-wsl)。它提供更好的效能，並完全相容 OpenCode 的所有功能。

- **使用 Chocolatey**

  ```bash
  choco install opencode
  ```

- **使用 Scoop**

  ```bash
  scoop install opencode
  ```

- **使用 NPM**

  ```bash
  npm install -g opencode-ai
  ```

- **使用 Mise**

  ```bash
  mise use -g github:anomalyco/opencode
  ```

- **使用 Docker**

  ```bash
  docker run -it --rm ghcr.io/anomalyco/opencode
  ```

在 Windows 上透過 Bun 安裝 OpenCode 的支援目前正在開發中。

您也可以從 [Releases](https://github.com/anomalyco/opencode/releases) 頁面直接下載二進位檔案。

---

## 設定

透過 OpenCode，您可以設定 API 金鑰來使用任意 LLM 供應商。

如果您剛開始接觸 LLM 供應商，我們推薦使用 [OpenCode Zen](/docs/zen)。這是一組經過 OpenCode 團隊測試和驗證的精選模型。

1. 在 TUI 中執行 `/connect` 指令，選擇 opencode，然後前往 [opencode.ai/auth](https://opencode.ai/auth)。

   ```txt
   /connect
   ```

2. 登入並新增帳單資訊，然後複製您的 API 金鑰。

3. 貼上您的 API 金鑰。

   ```txt
   ┌ API key
   │
   │
   └ enter
   ```

您也可以選擇其他供應商。[了解更多](/docs/providers#directory)。

---

## 初始化

設定好供應商後，導覽到您想要處理的專案目錄。

```bash
cd /path/to/project
```

然後執行 OpenCode。

```bash
opencode
```

接下來，執行以下指令為專案初始化 OpenCode。

```bash frame="none"
/init
```

OpenCode 會分析您的專案並在專案根目錄建立一個 `AGENTS.md` 檔案。

:::tip
您應該將專案的 `AGENTS.md` 檔案提交到 Git。

這有助於 OpenCode 理解專案結構和編碼規範。

---

## 使用

現在您已經準備好使用 OpenCode 來處理專案了，儘管提問吧！

如果您是第一次使用 AI 編碼代理，以下範例可能會對您有所幫助。

---

### 提問

您可以讓 OpenCode 為您講解程式碼庫。

:::tip
使用 `@` 鍵可以模糊搜尋專案中的檔案。

```txt frame="none" "@packages/functions/src/api/index.ts"
How is authentication handled in @packages/functions/src/api/index.ts
```

當您遇到不熟悉的程式碼時，這個功能非常有用。

---

### 新增功能

您可以讓 OpenCode 為專案新增新功能。不過我們建議先讓它制定一個計畫。

1. **制定計畫**

   OpenCode 有一個*計畫模式*，該模式下它不會進行任何修改，而是建議*如何*實作該功能。

   使用 **Tab** 鍵切換到計畫模式。您會在右下角看到模式指示器。

   ```bash frame="none" title="Switch to Plan mode"
   <TAB>
   ```

   接下來描述您希望它做什麼。

   ```txt frame="none"
   When a user deletes a note, we'd like to flag it as deleted in the database.
   Then create a screen that shows all the recently deleted notes.
   From this screen, the user can undelete a note or permanently delete it.
   ```

   您需要提供足夠的細節，讓 OpenCode 理解您的需求。可以把它當作團隊中的一名初級開發者來溝通。

   :::tip
   為 OpenCode 提供充足的上下文和範例，幫助它理解您的需求。

2. **迭代計畫**

   當它給出計畫後，您可以提供回饋或補充更多細節。

   ```txt frame="none"
   We'd like to design this new screen using a design I've used before.
   [Image #1] Take a look at this image and use it as a reference.
   ```

   :::tip
   將圖片拖放到終端機中即可將其新增到提示詞中。

   OpenCode 可以掃描您提供的圖片並將其新增到提示詞中。只需將圖片拖放到終端機視窗即可。

3. **建置功能**

   當您對計畫滿意後，再次按 **Tab** 鍵切換回*建置模式*。

   ```bash frame="none"
   <TAB>
   ```

   然後讓它開始實施。

   ```bash frame="none"
   Sounds good! Go ahead and make the changes.
   ```

---

### 直接修改

對於比較簡單的修改，您可以直接讓 OpenCode 實施，無需先審查計畫。

```txt frame="none" "@packages/functions/src/settings.ts" "@packages/functions/src/notes.ts"
We need to add authentication to the /settings route. Take a look at how this is
handled in the /notes route in @packages/functions/src/notes.ts and implement
the same logic in @packages/functions/src/settings.ts
```

請確保提供足夠的細節，以便 OpenCode 做出正確的修改。

---

### 復原修改

假設您讓 OpenCode 做了一些修改。

```txt frame="none" "@packages/functions/src/api/index.ts"
Can you refactor the function in @packages/functions/src/api/index.ts?
```

但您發現結果不是您想要的。您**可以使用** `/undo` 指令來復原修改。

```bash frame="none"
/undo
```

OpenCode 會還原所做的修改，並重新顯示您之前的訊息。

```txt frame="none" "@packages/functions/src/api/index.ts"
Can you refactor the function in @packages/functions/src/api/index.ts?
```

您可以調整提示詞，讓 OpenCode 重新嘗試。

:::tip
您可以多次執行 `/undo` 來復原多次修改。

您也**可以使用** `/redo` 指令來重做修改。

```bash frame="none"
/redo
```

---

## 分享

您與 OpenCode 的對話可以[與團隊分享](/docs/share)。

```bash frame="none"
/share
```

這會生成當前對話的連結並複製到剪貼簿。

:::note
對話預設不會被分享。

這是一個與 OpenCode 的[範例對話](https://opencode.ai/s/4XP1fce5)。

---

## 個人化

以上就是全部內容！您現在已經是 OpenCode 的使用高手了。

要讓它更符合您的習慣，我們推薦[選擇一個主題](/docs/themes)、[自訂快捷鍵](/docs/keybinds)、[設定程式碼格式化器](/docs/formatters)、[建立自訂指令](/docs/commands)，或者探索 [OpenCode 設定](/docs/config)。
