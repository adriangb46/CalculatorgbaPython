import unittest
from calculadora import multiplicar

class TestCalculadora(unittest.TestCase):

    def test_multiplicar_enteros(self):
        self.assertEqual(multiplicar(3, 5), 15)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-2, 4), -8)

    def test_multiplicar_flotantes(self):
        self.assertAlmostEqual(multiplicar(0.1, 10), 1.0)

    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(500, 0), 0)

if __name__ == "__main__":
    unittest.main()