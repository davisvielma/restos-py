import unittest
from herramientas import algebra

class TestAlgebra(unittest.TestCase):
	def test_es_par(self):
		self.assertTrue(algebra.es_par(12))
		self.assertFalse(algebra.es_par(13))
		self.assertTrue(algebra.es_par(54))
		self.assertTrue(algebra.es_par(-14))

	def test_factorial_recursivo(self):
		self.assertEqual(algebra.factorial_recursivo(0), 1)
		self.assertEqual(algebra.factorial_recursivo(1), 1)
		self.assertEqual(algebra.factorial_recursivo(5), 120)
		self.assertEqual(algebra.factorial_recursivo(7), 5040)

	def test_factorial_iterativo(self):
		self.assertEqual(algebra.factorial_iterativo(0), 1)
		self.assertEqual(algebra.factorial_iterativo(1), 1)
		self.assertEqual(algebra.factorial_iterativo(5), 120)
		self.assertEqual(algebra.factorial_iterativo(7), 5040)