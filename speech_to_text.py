import os #load .env file
from dotenv import load_dotenv #load .env file
import azure.cognitiveservices.speech as speechsdk # Azure Cognitive Services Speech SDK

# Load environment variables
load_dotenv()
api_key = os.getenv('Azure_api_key')
region = os.getenv('region')
microphone_device_id = os.getenv('microphone_device_id')

# Check if API key and region are loaded
if not api_key or not region:
    print("[Error] Can't load the api_key or region, please check .env!")
    exit(1)

def speak_to_microphone(api_key, region):
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language = "zh-HK"  # Set the recognition language to Cantonese
    #audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)  # Use the default microphone
    audio_config = speechsdk.audio.AudioConfig(device_name=microphone_device_id)  # Link to the microphone device
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Set timeout duration
    # Maximum wait time for initial silence before speech starts (in ms)
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "5000")  # 5 seconds
    # Maximum wait time for end silence after speech ends (in ms)
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "5000")  # 5 seconds

    print("Please start speaking and end with '發送指令'. ")
    while True:
        # Debug
        #user_input = input("Type 'exit' to stop the program or press Enter to continue: ").strip().lower()
        #if user_input == 'exit':
        #    print("Exiting...")
        #    break

        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"Recognized: {speech_recognition_result.text}")
            if "發送指令" in speech_recognition_result.text: # The ending words you want to use to stop the command
                print("End of command detected. Exiting...")
                break
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print(f"No speech could be recognized: {speech_recognition_result.no_match_details}")
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print(f"Speech Recognition canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
                print("Please check the .env file and ensure the setting of api_key, region and microphone_device_id is correct.")

speak_to_microphone(api_key, region)