import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    translation_copy=translation
    translation_list=(translation_copy.get('translations'))
    translation_dict=translation_list[0]
    french_text=(translation_dict.get('translation'))
    return french_text

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    translation_copy=translation
    translation_list=(translation_copy.get('translations'))
    translation_dict=translation_list[0]
    english_text=(translation_dict.get('translation'))
    return english_text
