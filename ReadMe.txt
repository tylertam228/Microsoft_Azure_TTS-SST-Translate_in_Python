# Azure Speech and Translation Services

## Overview
This project demonstrates the use of Microsoft Azure's Speech Services for text-to-speech (TTS) and speech-to-text (STT) functionalities, along with Azure Translator for converting text between languages, with a focus on translating Simplified Chinese to Traditional Chinese. The project is implemented in Python and defaults to using Cantonese (zh-HK) for speech-related features.

## Prerequisites
- **Python**: Version 3.8 or higher.
- **Microsoft Azure Account**: Required for accessing Speech and Translator services.
- **Operating System**: Compatible with Windows, macOS, or Linux.
- **FFmpeg**: Required for audio playback support (install via your system's package manager or [FFmpeg official site](https://ffmpeg.org/download.html)).
- **Text Editor or IDE**: For editing configuration files and running scripts.

## Setup Instructions
1. **Create Azure Resources**:
   - Log in to the [Microsoft Azure Portal](https://portal.azure.com).
   - Create a Resource Group in a suitable region (e.g., East US).
   - Add a **Speech Service** resource (Pricing Tier: F0 for free or S0 for standard).
   - Add a **Translator** resource (Pricing Tier: F0 for free or S0 for standard).

2. **Obtain API Credentials**:
   - Navigate to your Speech Service resource in the Azure Portal.
   - Retrieve the **Subscription Key** and **Region** (e.g., `eastus`).
   - For the Translator resource, retrieve the **Subscription Key**, **Region**, and **Endpoint** (default: `https://api.cognitive.microsofttranslator.com/`).
   - Store these credentials securely for use in the configuration file.

3. **Configure the Environment File**:
   - Create a `.env` file in the project root directory with the following structure:
     ```
     AZURE_SPEECH_KEY=your_speech_service_key
     AZURE_SPEECH_REGION=your_speech_service_region
     AZURE_SPEECH_ENDPOINT=your_speech_service_endpoint
     AZURE_TRANSLATOR_KEY=your_translator_key
     AZURE_TRANSLATOR_REGION=your_translator_region
     AZURE_TRANSLATOR_ENDPOINT=your_translator_endpoint
     MICROPHONE_DEVICE_ID=your_microphone_device_id
     SPEAKER_DEVICE_ID=your_speaker_device_id
     ```
   - Replace placeholder values with your actual credentials and device IDs.
   - Ensure variable names are consistent (e.g., use `AZURE_SPEECH_KEY` instead of `AZURE_API_KEY`).

4. **Install Dependencies**:
   - Install required Python packages by running:
     ```bash
     pip install azure-cognitiveservices-speech pydub python-dotenv requests
     ```
   - Install `FFmpeg` for audio processing:
     - **Windows**: Download from [FFmpeg official site](https://ffmpeg.org/download.html) or use a package manager like Chocolatey (`choco install ffmpeg`).
     - **macOS**: Use Homebrew (`brew install ffmpeg`).
     - **Linux**: Use your package manager (e.g., `sudo apt install ffmpeg` for Ubuntu).

5. **Find Supported Language Codes**:
   - For Speech Services, refer to [Azure Speech Service Language Support](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts).
   - For Translator, refer to [Azure Translator Language Support](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support).

6. **Obtain Device IDs for Microphone and Speaker**:
   - **Windows**:
     - Open **Sound** settings, select your microphone or speaker, and note the device name or ID (e.g., `{0.0.1.00000000}.{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}`).
     - Alternatively, use Python's `sounddevice` library to list devices: `pip install sounddevice` and run `python -m sounddevice`.
   - **macOS**:
     - Run in Terminal:
       ```bash
       system_profiler SPAudioDataType
       ```
     - Identify the device name or ID for your microphone or speaker.
   - **Linux**:
     - Run `aplay -l` for playback devices or `arecord -l` for recording devices to find device IDs.

## Usage
- **Speech-to-Text**:
  - Run `speech_to_text.py` to convert spoken Cantonese (zh-HK) or other supported languages to text.
  - The script uses the microphone to capture speech and prints the recognized text.
  - Say the trigger phrase (default: "發送指令" for Cantonese) to end the session.

- **Text-to-Speech**:
  - Run `text_to_speech.py` to synthesize text into speech.
  - Specify the language (default: zh-HK) and voice gender, then input the text to convert.
  - The synthesized audio is played and saved as a `.wav` file.

- **Translator**:
  - Run `translator.py` to translate text, with a default configuration for Simplified Chinese (zh-Hans) to Traditional Chinese (zh-Hant).
  - Modify the source and target language codes in the script for other translations (refer to the Azure Translator documentation for codes).

## Troubleshooting
- **API Key or Region Errors**: Verify that the `.env` file contains correct values with no typos or trailing spaces.
- **Microphone/Speaker Issues**: Confirm that device IDs match your system's configuration. Test devices using system tools or the `sounddevice` library.
- **FFmpeg Errors**: Ensure FFmpeg is installed and added to your system's PATH.
- **Language Support**: Check the Azure documentation for supported languages and voice options if unexpected results occur.
- **Further Assistance**: Refer to the [Azure Speech Service Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) or [Azure Translator Documentation](https://learn.microsoft.com/en-us/azure/ai-services/translator/).

## Notes
- This project defaults to Cantonese (zh-HK) for speech functionalities but can be adapted for other languages by modifying language codes.
- Ensure credentials in the `.env` file are kept secure and not exposed in version control systems.
- For production use, implement robust error handling and logging beyond what is provided in this educational example.

## Credits
This project was developed by Tiger228 during a summer internship to demonstrate the application of Azure Speech and Translator services.

## License
This project is open-source and available under the MIT License.
