import unittest
from herramientas import cadenas

class TestCadenas(unittest.TestCase):
	def test_invertir(self):
		self.assertEqual(cadenas.invertir('Ana'), 'anA')
		self.assertEqual(cadenas.invertir('casa de papel'), 'lepap ed asac')
		self.assertEqual(cadenas.invertir(' Prueba de espacios    '), 'soicapse ed abeurP')
		self.assertNotEqual(cadenas.invertir('hola'), 'aloH')

	def test_contador_de_palabras(self):
		self.assertEqual(cadenas.contador_de_palabras('Me tome un cafe americano'), 5)
		self.assertEqual(cadenas.contador_de_palabras(' Probando la funcion strip  '), 4)
		self.assertEqual(cadenas.contador_de_palabras('Prueba de correcta'), 3)

	def test_acronimos(self):
		self.assertEqual(cadenas.acronimos('Asociacion de meseros'), 'ADM')
		self.assertEqual(cadenas.acronimos('casona de ganaderos llaneros'), 'CDGL')

	def test_palindromo(self):
		self.assertTrue(cadenas.palindromo('  oSO '))
		self.assertTrue(cadenas.palindromo('Anita lava la tina'))
		self.assertFalse(cadenas.palindromo('papel'))