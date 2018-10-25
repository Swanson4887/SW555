import unittest
import Triangle

class TestTriangleMethods(unittest.TestCase):
	a = Triangle.Triangle(3,4,5)
	b = Triangle.Triangle(0,0,0)
	c = Triangle.Triangle(3,4,17)
	d = Triangle.Triangle(3,4,3)
	e = Triangle.Triangle(3,3,3)
	f = Triangle.Triangle(3,4,6)

	def test_isTriangle(self):
		self.assertEqual(self.a.isTriangle(), True)
		self.assertEqual(self.b.isTriangle(), False)
		self.assertEqual(self.c.isTriangle(), False)
		self.assertEqual(self.d.isTriangle(), True)

	def test_isEquilateral(self):
		self.assertEqual(self.a.isEquilateral(), False)
		self.assertEqual(self.e.isEquilateral(), True)
		self.assertEqual(self.b.isEquilateral(), False)

	def test_isIsosceles(self):
		self.assertEqual(self.d.isIsosceles(), True)
		self.assertEqual(self.f.isIsosceles(), False)
		self.assertEqual(self.e.isIsosceles(), True)

	def test_isScalene(self):
		self.assertEqual(self.f.isScalene(), True)
		self.assertEqual(self.c.isScalene(), False)
		self.assertEqual(self.a.isScalene(), True)

if __name__ == '__main__':
    unittest.main()

