import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    # Prueba para englishToFrench
    def test_englishToFrench(self):
        # Prueba de traducción de texto inglés a francés
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

        self.assertEqual(englishToFrench("My name is John."), "Je m'appelle John.")
        # Prueba de manejo de entrada nula
        with self.assertRaises(TypeError):
            englishToFrench(None)
        # Prueba de manejo de entrada de cadena vacía
        self.assertEqual(englishToFrench(""), "")

    # Prueba para frenchToEnglish
    def test_frenchToEnglish(self):
        # Prueba de traducción de texto francés a inglés
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

        self.assertEqual(frenchToEnglish("Je m'appelle Marie."), "My name is Marie.")
        # Prueba de manejo de entrada nula
        with self.assertRaises(TypeError):
            frenchToEnglish(None)
        # Prueba de manejo de entrada de cadena vacía
        self.assertEqual(frenchToEnglish(""), "")

    # Pruebas adicionales
    def test_additional(self):
        # Prueba de traducción de otras palabras y frases
        self.assertEqual(englishToFrench("Goodbye"), "Au revoir")

        self.assertEqual(englishToFrench("I love you"), "Je t'aime")

        self.assertEqual(frenchToEnglish("Je suis français"), "I am French")
        
        self.assertEqual(frenchToEnglish("Je ne comprends pas"), "I don't understand")
