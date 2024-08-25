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

	def test_fibonacci_recursivo(self):
		self.assertEqual(algebra.fibonacci_recursivo(0), 0)
		self.assertEqual(algebra.fibonacci_recursivo(1), 1)
		self.assertEqual(algebra.fibonacci_recursivo(6), 8)
		self.assertEqual(algebra.fibonacci_recursivo(7), 13)
		self.assertEqual(algebra.fibonacci_recursivo(8), 21)

	def test_fibonacci_iterativo(self):
		self.assertEqual(algebra.fibonacci_iterativo(0), 0)
		self.assertEqual(algebra.fibonacci_iterativo(1), 1)
		self.assertEqual(algebra.fibonacci_iterativo(6), 8)
		self.assertEqual(algebra.fibonacci_iterativo(7), 13)
		self.assertEqual(algebra.fibonacci_iterativo(8), 21)