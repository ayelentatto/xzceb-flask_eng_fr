import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    # Prueba para englishToFrench
    def test_english_to_rench(self):
        # Prueba de traducción de texto inglés a francés
        self.assertEqual(english_to_french("Hello"), "Bonjour")

        self.assertEqual(english_to_french("My name is John."), "Je m'appelle John.")
        # Prueba de manejo de entrada nula
        with self.assertRaises(TypeError):
            english_to_french(None)
        # Prueba de manejo de entrada de cadena vacía
        self.assertEqual(english_to_french(""), "")

    # Prueba para frenchToEnglish
    def test_french_to_english(self):
        # Prueba de traducción de texto francés a inglés
        self.assertEqual(french_to_english("Bonjour"), "Hello")

        self.assertEqual(french_to_english("Je m'appelle Marie."), "My name is Marie.")
        # Prueba de manejo de entrada nula
        with self.assertRaises(TypeError):
            french_to_english(None)
        # Prueba de manejo de entrada de cadena vacía
        self.assertEqual(french_to_english(""), "")

    # Pruebas adicionales
    def test_additional(self):
        # Prueba de traducción de otras palabras y frases
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")

        self.assertEqual(english_to_french("I love you"), "Je t'aime")

        self.assertEqual(french_to_english("Je suis français"), "I am French")
        
        self.assertEqual(french_to_english("Je ne comprends pas"), "I don't understand")
