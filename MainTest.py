from unittest import TestCase

import Main

class MainTest(TestCase):
    def test_contarElementos(self):
        self.assertEqual(Main().contarElementos(""),0, "Cadena Vacia")
