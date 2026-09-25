---
title: Palantir 官方文档 · 入门 · 认证
source: Palantir 官方文档（中文机翻版）
url: https://palantir.com/docs/zh/foundry/getting-started/authentication/
lang: zh
keywords:
- Palantir
- Foundry
state:
  phase: raw
  time_raw: 2026-09-23 02:19:56+08:00
  time_draft: 2026-09-23T02:23:28+08:00
  time_wiki: null
---


> 溯源注：本文为 Palantir 官方文档原文抓取（一手来源）。⚠️ 官方标注该中文页为**未经人工验证的机器翻译**，权威表述以英文原版为准。
> 抓取时间：2026-09-23T02:19:56+08:00

:::callout{theme="warning"}
注意：以下翻译的准确性尚未经过验证。这是使用 [AIP ↗](https://www.palantir.com/platforms/aip/) 从原始英文文本进行的机器翻译。
:::

# 认证

本页面提供有关如何登录 Palantir 平台的信息。在大多数情况下，您的注册管理员会将您组织现有的身份提供者与 Palantir 平台集成，以便您可以使用您在其他内部系统中使用的相同凭据登录。

或者，自 2024 年夏季起，Palantir 的自助服务无密码身份提供者可用于配置 AIP Now 和 AIP Bootcamps 的新注册。

## 您自己的身份提供者

Palantir 平台可以与您现有的身份提供者无缝集成，通过现有系统进行完整的端到端访问管理。有关如何配置身份提供者以用于 Palantir 平台的详细说明，请参阅[管理文档](/docs/foundry/authentication/overview/)。

## Palantir 自助服务用户目录

在某些情况下，您的注册可能会自动配置为内置的身份提供者。Palantir 的自助服务用户目录是**无密码**的，利用 FIDO2 密钥提供无与伦比的安全性和无缝的用户体验。

如果您使用 Palantir 自助服务用户目录注册了一个新账户，您将在注册后不久收到一封主题为“设置您的 Palantir 账户”的电子邮件。完成以下说明以设置您的账户后，您可以通过导航到 **认证 > Palantir 自助服务用户目录** 在控制面板中邀请其他用户加入您的注册。然后，选择 **管理用户**。

### 什么是密钥？

FIDO2（快速身份在线）密钥是一种旨在增强安全性和便利性的现代认证形式。密钥是一种无需使用密码即可登录账户的安全方式，消除了记住复杂密码的需要，这些密码可能很难记住且令人沮丧。使用密钥，您可以通过指纹、面部扫描、硬件词元或密码管理器登录。

### 密钥如何工作？

FIDO2 密钥是一种物理安全密钥或平台认证器，如生物识别设备或智能手机，可用于无密码认证。设备为每个服务或应用程序生成一对唯一的公钥和私钥。公钥注册在服务中，而私钥则安全地存储在设备上。

当您使用 FIDO2 密钥进行认证时，服务会向您的设备发送一个挑战。设备将使用私钥对挑战进行签名，并将签名的响应发送回服务。然后，服务使用公钥验证响应以确认您的身份。

密钥提供了几个好处：

* **强大的安全性**：公钥加密提供了高水平的安全性，由于私钥从未离开设备，它更不易受到攻击。
* **无密码认证**：FIDO2 密钥消除了密码的需要，使认证更方便，并减少钓鱼和其他与密码相关的攻击风险。
* **隐私**：每个服务生成的唯一密钥对确保您的认证信息不能用于跟踪您在不同服务中的活动。
* **易用性**：密钥提供了一个简单、用户友好的认证体验，只需要一个简单的操作，如插入安全密钥或使用生物识别设备如指纹或面部扫描。

### 设置和配置密钥

以下是如何使用 Palantir 内置无密码认证的说明。

要继续，您必须已经收到 Palantir 发送的标题为“设置您的 Palantir 账户”的电子邮件。然后，按照以下说明操作：

1. 在来自 Palantir 的电子邮件中选择 **注册** 选项以开始设置您的 Palantir 账户。

    <img alt="设置您的 Palantir 账户" src="../../foundry-docs/getting-started/media/setup-email.png" width="400">
2. 输入您的电子邮件地址和临时密码，然后选择 **下一步**。

    <img alt="注册步骤" src="../../foundry-docs/getting-started/media/sign-up-step.png" width="400">
3. 在 SMS 或电话验证之间进行选择以验证您的账户。

    <img alt="创建账户步骤" src="../../foundry-docs/getting-started/media/create-account-step.png" width="400">
4. 使用 6 位数的认证码验证您的电话号码。

    <img alt="验证电话号码步骤" src="../../foundry-docs/getting-started/media/verify-phone-step.png" width="400">
5. 如果您被邀请加入现有的注册，请同意条款和条件以继续。否则，跳至步骤 6。

    <img alt="同意条款步骤" src="../../foundry-docs/getting-started/media/tos-step.png" width="400">
6. 选择 **添加密钥**。
7. 选择一个保存密钥的目的地，然后按照屏幕上的说明操作。

   * 对于硬件词元，您可能需要选择 **使用其他设备**。
     * 然后，您需要插入您的硬件词元，输入其 PIN 和/或触摸词元上的指纹传感器。
   * 对于移动设备词元，您可能需要选择 **使用其他设备**，然后使用您的移动设备扫描二维码。
   * 为避免问题，请确保您正在使用[支持的浏览器](/docs/foundry/getting-started/supported-browsers/)。

    <img alt="创建密钥对话框" src="../../foundry-docs/getting-started/media/create-passkey-step.png" width="400">
8. 一旦您的密钥成功添加，您将看到以下屏幕：

    <img alt="成功步骤" src="../../foundry-docs/getting-started/media/success-step.png" width="400">

#### 使用密钥登录

1. 在 Palantir 登录页面，输入您的电子邮件地址并选择 **下一步**。
2. 选择 **使用密钥** 选项以使用您的密钥登录账户。
3. 按照屏幕上的密钥说明解锁您的设备并选择您的密钥。

#### 添加额外的密钥

我们建议您为您的账户添加多个密钥作为备份。每个账户最多可以添加四个密钥。

要向您的账户添加额外的密钥，请导航到 **设置 > 账户**。然后，找到 **认证**。您也可以直接访问 `<your-enrollment-URL>/workspace/settings/authentication`。

<img alt="认证设置" src="../../foundry-docs/getting-started/media/passkey-mgmt.png" width="700">

* 选择 **添加密钥** 选项。
  * 在添加额外的密钥之前，您可能会被要求重新认证。
* 选择一个保存密钥的目的地，然后按照屏幕上的说明操作。
  * 对于硬件词元，您可能需要选择 **使用其他设备**。然后，您需要插入您的硬件词元，输入其 PIN 和/或触摸词元上的指纹传感器。

#### 删除密钥

* 要删除已注册的密钥，请导航到 **设置 > 账户**。然后，找到 **认证** 或访问 `<your-enrollment-URL>/workspace/settings/authentication`。
* 使用要删除的密钥旁边的操作下拉菜单。
* 选择 **删除** 并 **确认** 您要删除密钥。一旦删除，您将无法再使用该密钥登录。

#### 重置账户

如果您无法访问任何密钥，请联系您的注册管理员以重置您的账户。为避免这种情况，我们建议您注册至少两个密钥，以防无法访问某一个密钥时高枕无忧。

### 密钥类型和最佳实践

#### 最佳实践

我们建议您为您的账户至少保留两个不同的密钥。例如，您可以将一个密钥存储在手机上，一个存储在 Chrome 配置文件中。此外，您还应配置多个[注册管理员](/docs/foundry/administration/enrollments-and-organizations-permissions/)以协助账户恢复作为备份。

#### 推荐的密钥类型

在 **Windows** 计算机上，我们推荐以下方法管理密钥：

* [在手机或 YubiKey 上创建并存储密钥 ↗](https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/?tabs=windows#create-a-passkey)
* [直接在 Google Chrome 中创建并存储密钥 ↗](https://blog.chromium.org/2022/12/introducing-passkeys-in-chrome.html)

在 **macOS** 设备上，您可以创建并存储同步到您的设备上的密钥，使用 iCloud。在 macOS 上，您可以：

* [确保您的 iCloud 密钥已启用并使用 iCloud 密钥 ↗](https://support.apple.com/en-us/109016)
* [直接在 iOS 上创建密钥 ↗](https://support.apple.com/guide/iphone/use-passkeys-to-sign-in-to-apps-and-websites-iphf538ea8d0/ios)
* [管理密钥 ↗](https://it-training.apple.com/tutorials/support/sup540)
