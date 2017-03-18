from unittest import TestCase

from Main import Main

class MainTest(TestCase):
    def test_contarElementos(self):
        self.assertEqual(Main().contarElementos(""),0, "Cadena Vacia")

    def test_contarElementos_UnElemento(self):
        self.assertEqual(Main().contarElementos("1"), 1, "Un Numero")
