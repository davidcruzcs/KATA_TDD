from unittest import TestCase

from Main import Main

class MainTest(TestCase):
    def test_contarElementos(self):
        self.assertEqual(Main().contarElementos([""]),["0"], "Cadena Vacia")

    def test_contarElementos_UnElemento(self):
        self.assertEqual(Main().contarElementos(["1"]), ["1"], "Un Numero")

    def test_contarElementos_DosElementos(self):
        self.assertEqual(Main().contarElementos(["1","1"]), ["2"], "Dos Numeros")

    def test_contarElementos_NNumeros(self):
        self.assertEqual(Main().contarElementos(["1","2","3","4","5"]), ["5"], "N Numeros")
