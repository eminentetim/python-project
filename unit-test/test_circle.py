import unittest
from circle import circle
from math import pi

class TestCircleArea(unittest.Testcase):
	def test_area(self):
	# test areas when radius >= 0
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)