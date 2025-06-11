import os
import requests
from dotenv import load_dotenv

# Set the key and region directly here
load_dotenv()  # Load environment variables from .env file
AZURE_TRANSLATOR_KEY = os.getenv('Azure_Translator_Key')
AZURE_TRANSLATOR_REGION = os.getenv('Azure_Translator_Region')
AZURE_TRANSLATOR_ENDPOINT = os.getenv('Azure_Translator_Endpoint')


def translate_zhcn_to_zhtw(text):
    """
    Use Azure Text Translation to convert Simplified Chinese (zh-CN) to Traditional Chinese (zh-TW)
    :param text: Text to be translated
    :return: Translated text (Traditional Chinese)
    """
    path = '/translate?api-version=3.0'
    # You can modify the language codes as needed, for example, to translate from Simplified Chinese (zh-Hans) to English (en):
    # params = f'&from=zh-Hans&to=en'
    params = f'&from=zh-Hans&to=zh-Hant'  # <-- Change source/target language codes here
    # (You can find language IDs in the official docs: https://learn.microsoft.com/azure/ai-services/translator/language-support)
    constructed_url = AZURE_TRANSLATOR_ENDPOINT.rstrip('/') + path + params
    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_TRANSLATOR_KEY,
        'Ocp-Apim-Subscription-Region': AZURE_TRANSLATOR_REGION,
        'Content-type': 'application/json',
    }
    body = [{ 'text': text }]
    response = requests.post(constructed_url, headers=headers, json=body)
    response.raise_for_status()
    result = response.json()
    return result[0]['translations'][0]['text'] if result and 'translations' in result[0] else ''

# Example call
text = input("Enter text in Simplified Chinese (zh-CN) to translate to Traditional Chinese (zh-TW): ")
print(translate_zhcn_to_zhtw(text))
