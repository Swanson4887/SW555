class Triangle():
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c


	def isTriangle(self):
		#determines whether or not something is triangle
		if((self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b) or (self.a <= 0 or self.b <= 0 or self.c <= 0)):
			return False
		else:
			return True

	def isEquilateral(self):
		#determines whether or not a triangle is equilateral
		if((self.a == self.b and self.b == self.c and self.a == self.c) and (self.isTriangle() == True)):
			return True
		else:
			return False

	def isIsosceles(self):
		#determines whether or not a triangle is isosceles
		if((self.a == self.b or self.a == self.c or self.b == self.c) and (self.isTriangle() == True)):
			return True
		else:
			return False

	def isScalene(self):
		#determines whether or not a triangle is scalene
		if((self.a != self.b or self.b != self.c or self.a != self.c) and (self.isTriangle() == True)):
			return True
		else:
			return False
		



