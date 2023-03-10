import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Crea una instancia de IAMAuthenticator con tu clave API
authenticator = IAMAuthenticator(apikey)

# Crea una instancia de LanguageTranslatorV3
language_translator = LanguageTranslatorV3(
    version='2021-09-01',
    authenticator = authenticator
)

# Establece la URL del servicio
language_translator.set_service_url(url)

def english_to_french(english_text):
    # Traduce el texto de entrada en inglés a francés
    translation = language_translator.translate(
        text= english_text ,
        source='en',
        target='fr'
    ).get_result()

    # Extrae el texto francés de la respuesta de traducción
    french_text = translation['translations'] [0] ['translation']

    return french_text

print(english_to_french("¡Hola, cómo estás?"))

def  french_to_english(french_text):
    translation = language_translator.translate(
        text= french_text ,
        source='en',
        target='fr'
    ).get_result()

    english_text = translation['translations'] [0] ['translation']

    return english_text
