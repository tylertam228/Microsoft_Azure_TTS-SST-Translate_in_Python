Azure Text-to-Speech & Speech-to-Text & Translator - EN
========================================================

This project demonstrates how to use Microsoft Azure's Speech Services for both speech-to-text and text-to-speech in Python. It also includes a translator utility for converting Simplified Chinese to Traditional Chinese using Azure Translator.

> **Note:** All examples in this project default to using Cantonese (zh-HK) as the primary language.


Setup Instructions
------------------

1. **Create Azure Resources**
   - Log in to the Microsoft Azure Portal.
   - Create a Resource Group.
   - Add a 'Speech Service' resource (suggested region: East US; Pricing Tier: F0:Free or S0:Standard).
   - Add a 'Translation' resource (suggested region: East US; Pricing Tier: F0:Free or S0:Standard).

2. **Get API Credentials**
   - Go to your Speech Service resource in Azure.
   - Find your Subscription Key and Region.
   - Copy these values for use in your `.env` file.

3. **Configure the `.env` File**
   - Create a `.env` file in the project root with the following keys:
     ```
     Azure_api_key=YOUR_AZURE_SPEECH_KEY
     region=YOUR_AZURE_REGION
     endpoint=YOUR_AZURE_ENDPOINT
     Azure_Translator_Key=YOUR_TRANSLATOR_KEY
     Azure_Translator_Region=YOUR_TRANSLATOR_REGION
     Azure_Translator_Endpoint=YOUR_TRANSLATOR_ENDPOINT (or https://api.cognitive.microsofttranslator.com/)
     microphone_device_id=YOUR_MICROPHONE_DEVICE_ID
     speaker_device_id=YOUR_SPEAKER_DEVICE_ID
     ```
   - Replace the values with your actual credentials and device IDs.

4. **Install Dependencies**
   - Open a terminal and run:
     ```
     pip install azure-cognitiveservices-speech pydub python-dotenv requests
     ```
   - You may also need to install `ffmpeg` for audio playback support. Please refer to the official ffmpeg documentation or your operating system's package manager for installation instructions.

5. **Find Supported Language Codes**
   - For Speech Service: [Azure Speech Language Support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts)
   - For Translator: [Azure Translator Language Support](https://learn.microsoft.com/azure/ai-services/translator/language-support)

6. **Get Device IDs (Microphone/Speaker)**
   - **Windows:**
     - Open Device Manager > Audio inputs and outputs.
     - Right-click your microphone or speaker > Properties > Details tab.
     - Select 'Device instance path' and copy the value (format: `{xxxx}.{xxxx}`).
   - **Mac:**
     - Open Terminal and run:
       ```
       system_profiler SPAudioDataType
       ```
     - Find the device path for your audio device.

Usage
-----

- **Speech to Text:**
  - Run `speech_to_text.py` to convert spoken Cantonese (or other supported languages) to text using your microphone.
  - The script will listen for speech and print the recognised text. Say the trigger phrase (default: '發送指令') to end the session.

- **Text to Speech:**
  - Run `text_to_speech.py` to convert text to speech.
  - Select the language and gender for the voice, then enter the text you want to synthesise.
  - The script will play the audio and save it as a `.wav` file.

- **Translator:**
  - Use `translator.py` to translate Simplified Chinese to Traditional Chinese (or modify the language codes for other translations).
  - See comments in the code for how to change source/target languages and where to find language codes.

Troubleshooting
---------------
- If you see errors about missing API keys or region, check your `.env` file for typos or missing values.
- If your microphone or speaker is not working, double-check the device ID and ensure it matches your system's device path.
- For more help, refer to the official Azure documentation linked above.

---

This project was created by Tiger228 during a summer internship, with the aim of sharing the knowledge and experience gained throughout that period.

This project is intended for educational and demonstration purposes only. For production use, please ensure your credentials are kept secure and follow best practices for error handling and logging.

Azure Text-to-Speech & Speech-to-Text & Translator - ZH
========================================================

本專案展示如何在 Python 中使用 Microsoft Azure 的語音服務進行語音轉文字（Speech-to-Text）與文字轉語音（Text-to-Speech），並包含利用 Azure 翻譯器將簡體中文轉換為繁體中文的工具。

設定說明
--------

1. **建立 Azure 資源**
   - 登入 Microsoft Azure 入口網站。
   - 建立資源群組（Resource Group）。
   - 新增「語音服務」（Speech Service）資源（建議區域：East US；價格方案：F0:免費 或 S0:標準）。
   - 新增「翻譯」（Translation）資源（建議區域：East US；價格方案：F0:免費 或 S0:標準）。

2. **取得 API 憑證**
   - 前往 Azure 入口網站中的語音服務資源。
   - 找到您的訂閱金鑰（Subscription Key）與區域（Region）。
   - 複製這些資訊，稍後填入 `.env` 檔案。

3. **設定 `.env` 檔案**
   - 在專案根目錄建立 `.env` 檔案，內容如下：
     ```
     Azure_api_key=YOUR_AZURE_SPEECH_KEY
     region=YOUR_AZURE_REGION
     endpoint=YOUR_AZURE_ENDPOINT
     Azure_Translator_Key=YOUR_TRANSLATOR_KEY
     Azure_Translator_Region=YOUR_TRANSLATOR_REGION
     Azure_Translator_Endpoint=YOUR_TRANSLATOR_ENDPOINT (或 https://api.cognitive.microsofttranslator.com/)
     microphone_device_id=YOUR_MICROPHONE_DEVICE_ID
     speaker_device_id=YOUR_SPEAKER_DEVICE_ID
     ```
   - 請將上述內容替換為您實際的金鑰與裝置 ID。

4. **安裝相依套件**
   - 開啟終端機並執行：
     ```
     pip install azure-cognitiveservices-speech pydub python-dotenv requests
     ```
   - 您可能還需要安裝 `ffmpeg` 以支援音訊播放。請參考官方 ffmpeg 文件或您的作業系統套件管理工具進行安裝。

5. **查詢支援語言代碼**
   - 語音服務：[Azure 語音服務語言支援](https://learn.microsoft.com/zh-tw/azure/ai-services/speech-service/language-support?tabs=tts)
   - 翻譯服務：[Azure 翻譯語言支援](https://learn.microsoft.com/zh-tw/azure/ai-services/translator/language-support)

6. **取得裝置 ID（麥克風/喇叭）**
   - **Windows：**
     - 開啟裝置管理員 > 音訊輸入與輸出。
     - 右鍵點選您的麥克風或喇叭 > 內容 > 詳細資料。
     - 選擇「裝置實例路徑」，複製其值（格式如 `{xxxx}.{xxxx}`）。
   - **Mac：**
     - 開啟終端機並執行：
       ```
       system_profiler SPAudioDataType
       ```
     - 找到您的音訊裝置路徑。

使用方式
--------

- **語音轉文字（Speech to Text）：**
  - 執行 `speech_to_text.py`，可將粵語（或其他支援語言）的語音轉換為文字。
  - 程式會監聽麥克風並顯示辨識結果。說出結束語（預設為「發送指令」）即可結束。

- **文字轉語音（Text to Speech）：**
  - 執行 `text_to_speech.py`，可將文字轉換為語音。
  - 選擇語言與聲音性別，輸入要合成的文字。
  - 程式會播放語音並儲存為 `.wav` 檔案。

- **翻譯工具（Translator）：**
  - 執行 `translator.py`，可將簡體中文翻譯為繁體中文（或依需求修改語言代碼進行其他語言轉換）。
  - 請參考程式碼中的註解，了解如何修改來源/目標語言及查詢語言代碼。

疑難排解
--------
- 若出現找不到 API 金鑰或區域的錯誤，請檢查 `.env` 檔案是否有拼寫錯誤或遺漏。
- 若麥克風或喇叭無法正常運作，請再次確認裝置 ID 是否正確，並確保與系統裝置路徑相符。
- 更多協助請參考上方的官方 Azure 文件連結。

---

本專案由 Tiger228 於暑期實習期間製作，旨在分享其學習經驗與知識。

本專案僅供教學與示範用途。若用於正式環境，請妥善保管您的金鑰，並遵循最佳實踐進行錯誤處理與日誌記錄。

