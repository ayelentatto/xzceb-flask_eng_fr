import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Crea una instancia de IAMAuthenticator con tu clave API
authenticator = IAMAuthenticator(apikey)

# Crea una instancia de LanguageTranslatorV3
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator=authenticator
)

# Establece la URL del servicio
language_translator.set_service_url(url)

def englishToFrench(englishText):
    # Traduce el texto de entrada en inglés a francés
    translation = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()

    # Extrae el texto francés de la respuesta de traducción
    frenchText = translation['translations'][0]['translation']

    return frenchText

print(englishToFrench("¡Hola, cómo estás?"))

def  frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()

    frenchText = translation['translations'][0]['translation']
    return frenchText
