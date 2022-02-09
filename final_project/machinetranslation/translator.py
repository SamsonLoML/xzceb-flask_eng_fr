import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('CZFC96BIqS7vgRgVAcMYsaHtk7r9m0M2m0Q1idKeaJXS')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/73b60b1d-1888-4e26-a415-f1acc857c9bc')

def english_to_french(english_text):
    """Translate from English to French"""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """Translate from French to English"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
