import os #load .env file
import io #save the audio as binary data
from dotenv import load_dotenv #load .env file
from pydub import AudioSegment #play audio
from pydub.playback import play #play audio
import azure.cognitiveservices.speech as speechsdk

load_dotenv() #load .env file

#load the environment variables
api_key = os.getenv('Azure_api_key')
region = os.getenv('region')
endpoint = os.getenv('endpoint')
speaker_device_id = os.getenv('speaker_device_id')

#debug
if not api_key or not region:
    print("[Error] Can't load the api_key or region，please check .env！")
    exit(1)

speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
#audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True) # Use the default microphone
audio_config = speechsdk.audio.AudioOutputConfig(device_name=speaker_device_id) # Link to the speaker device

# Language selection
while True:
    print("Select a language: 1) Cantonese 2) English 3) Mandarin")
    language_choice = input("Enter 1, 2, or 3: ").strip()
    if language_choice in ('1', '2', '3'):
        break
    print("Invalid input, please try again.\n")

# Gender selection
while True:
    print("Select a voice gender: 1) Woman 2) Man")
    gender_choice = input("Enter 1 or 2: ").strip()
    if gender_choice in ('1', '2'):
        break
    print("Invalid input, please try again.\n")


# Map language and gender to Azure TTS voice name
voice_map = {
    ('1', '1'): 'zh-HK-HiuGaaiNeural',   # Cantonese Woman
    ('1', '2'): 'zh-HK-WanLungNeural',   # Cantonese Man
    #If input Chinese word when using English mode, it will skip the Chinese word
    ('2', '1'): 'en-US-JennyNeural',     # English Woman 
    ('2', '2'): 'en-US-GuyNeural',       # English Man
    ('3', '1'): 'zh-CN-XiaoxiaoNeural',  # Mandarin Woman
    ('3', '2'): 'zh-CN-YunxiNeural',     # Mandarin Man
}

# Select voice based on user input
voice_name = voice_map.get((language_choice, gender_choice))
speech_config.speech_synthesis_voice_name = voice_name
#speech_config.speech_synthesis_voice_name = 'zh-HK-HiuGaaiNeural' # Default to Cantonese

# Prompt user for text to speak
text = input("Enter the text you want to speak: ")

# Check the text if you want
while True:
    confirm_text = input(f"You entered: '{text}'.\n Is this correct? (yes/no): ").strip().lower()
    if confirm_text in ('yes', 'no'):
        if confirm_text == 'no':
            text = input("Please enter the text again: ")
        else:
            break
    else:
        print("Invalid input, please enter 'yes' or 'no'.\n")

# Debug
#print(f"You selected language: {language_choice} ({'Cantonese' if language_choice == '1' else 'English' if language_choice == '2' else 'Mandarin'})")
#print(f"You selected gender: {gender_choice} ({'Woman' if gender_choice == '1' else 'Man'})")

# Before synthesizing speech, delete previous output.wav if it exists
wav_file_path = "output.wav"
if os.path.exists(wav_file_path):
    os.remove(wav_file_path)
    print(f"Deleted previous {wav_file_path}")

# Synthesize speech
def speak_text(text):
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_synthesizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized successfully.")
    else:
        print(f"Speech synthesis failed: {result.reason}")

def text_to_wav(text, wav_path):
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=speechsdk.audio.AudioOutputConfig(filename=wav_path))
    result = speech_synthesizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesized and saved to {wav_path}")
    else:
        print(f"Speech synthesis failed: {result.reason}")

# Example usage
speak_text(text)
text_to_wav(text, wav_file_path)



