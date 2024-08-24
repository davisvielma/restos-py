import unittest
from herramientas import algebra

class TestAlgebra(unittest.TestCase):
	def test_es_par(self):
		self.assertTrue(algebra.es_par(12))
		self.assertFalse(algebra.es_par(13))
		self.assertTrue(algebra.es_par(54))
		self.assertTrue(algebra.es_par(-14))