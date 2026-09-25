---
title: WeCom Integration
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
- Xpertai/XpertAI工作流教程-MD版/ai/tutorial/wechat-work-integration.md
---
# WeCom Integration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xpertai.cn/llms.txt
> Use this file to discover all available pages before exploring further.

# WeCom Integration

The **Xpert AI Multi-Agent Platform** now supports integration with **WeCom (WeChat Work)**. Through this integration, enterprise users can directly access intelligent dialogue capabilities of digital experts within WeCom, including data analysis using the **ChatBI toolset**, with analysis results returned as screenshots.

This tutorial will guide you step-by-step through the WeCom integration setup.

***

## Step 1: Create a WeCom Application and Obtain Required Information

1. Log in to the [WeCom Admin Console](https://work.weixin.qq.com/) and go to **“App Management”**.

2. Click “Custom App” to create a new application, and fill in the name, logo, description, etc.

3. Once created, take note of the following information:
   * **AgentId**
   * **Secret**

4. On the app’s settings page, enable and activate the **Receive Messages** feature, and configure the Token and EncodingAESKey. The platform will return the following:
   * **Token**
   * **EncodingAESKey**

5. Finally, go to the **“My Company”** page to get the unique company identifier:
   * **CorpID**

✅ By this point, you should have the following five key pieces of information:

* CorpID
* AgentId
* Secret
* Token
* EncodingAESKey

***

## Step 2: Configure Digital Expert Integration with WeCom

1. Log into the Xpert AI platform, go to the **Digital Experts** module, and create a new digital expert agent.

2. When configuring the toolset, if this agent is used for data analysis, **select “WeCom Chat BI” as the toolset type** to enable ChatBI analysis capabilities.

3. After configuring the agent, click “Publish Version”, and in the **Third-Party Publishing** step, add “WeCom” as the distribution channel.

4. Enter the five pieces of information you obtained from the WeCom admin console:

   * CorpID
   * AgentId
   * Secret
   * Token
   * EncodingAESKey

5. After saving the configuration, the system will generate a **Callback URL**.

***

## Step 3: Enter the Callback URL in WeCom to Complete Verification

1. Go back to the WeCom Admin Console and open the app's “Receive Messages” settings.
2. Enter the Xpert AI-provided **Callback URL** into the **“Message Server Address”** field.
3. Click save. WeCom will automatically send a verification request.
4. If everything is correct, you’ll see a success message.

🎉 Congratulations! Your digital expert agent has been successfully connected to WeCom!

***

## Step 4: Chat with the Digital Expert in WeCom

Now, WeCom users can:

* Chat directly with the Xpert AI agent
* Use ChatBI for BI data analysis
* Receive analytical charts and insights as screenshot images

***

## FAQ

You may encounter some common issues when integrating the Xpert AI digital expert with WeCom. Below are common problems and suggested solutions:

### 1. No response when sending messages to the WeCom app

**Possible Causes & Solutions:**

* Message receiving not enabled\
  👉 Ensure the “Receive Messages” feature is enabled in the WeCom Admin Console.

* Incorrect Callback URL or failed verification\
  👉 Double-check the Callback URL and make sure verification succeeded.

* Incorrect AgentId or Secret\
  👉 Confirm that the AgentId and Secret entered in Xpert AI match those in WeCom.

* Enterprise trusted IP of enterprise WeChat application
  👉 Check whether the enterprise trusted IP is configured with the server export IP (the IP of XpertAI online system can be obtained by contacting our technicians)

***

### 2. ChatBI analysis request fails or no screenshot returned

**Possible Causes & Solutions:**

* “WeCom Chat BI” toolset not enabled for the agent\
  👉 Make sure the correct toolset is selected for the agent.

* Analysis result generation failed or screenshot service error\
  👉 Contact the platform administrator and check logs for any anomalies.

***

### 3. WeCom shows “URL Verification Failed”

**Possible Causes & Solutions:**

* Incorrect Token or EncodingAESKey\
  👉 Ensure they match exactly with what’s configured in WeCom.

* Callback URL not publicly accessible\
  👉 Make sure the server is publicly accessible and the port is open.

* WeCom request blocked by firewall or proxy\
  👉 Check if any security group, WAF, or firewall is blocking the request.

***

### 4. WeCom app users cannot see the app or its entry point

**Possible Causes & Solutions:**

* App visibility scope not set\
  👉 Go to the WeCom app settings and add users or departments to grant access.

***

For more information on ChatBI features or enterprise customization needs, feel free to contact our product support team!
