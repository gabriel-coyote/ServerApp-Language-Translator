import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# ---------------------------------
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# language_translator.set_disable_ssl_verification(True)
# ---------------------------------


def englishToFrench(englishText):
    """Function return french text from english"""
    if englishText is None:
        return None

    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()

    text = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
    t_list = text["translations"]
    frenchText = t_list[0]["translation"]

    return frenchText

# ---------------------------------


def frenchToEnglish(frenchText):
    """Function returning engglish text from french"""
    if frenchText is None:
        return None

    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()

    text = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
    t_list = text["translations"]
    englishText = t_list[0]["translation"]

    return englishText
