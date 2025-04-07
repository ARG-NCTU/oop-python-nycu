class Matrix2:
	def __init__(self, a=0, b=0, c=0, d=0):
		"""
		Create a 2x2 matrix \\
		`[a b]`\\
		`[c d]`
		"""
		self.a = a
		self.b = b
		self.c = c
		self.d = d
	
	def __str__(self):
		return f"[{self.a} {self.b}]\n[{self.c} {self.d}]"
	
	def add(self, mat):
		return Matrix2(
			self.a + mat.a,
			self.b + mat.b,
			self.c + mat.c,
			self.d + mat.d
		)
	
	def minus(self, mat):
		return Matrix2(
			self.a - mat.a,
			self.b - mat.b,
			self.c - mat.c,
			self.d - mat.d
		)
	
	def multiply(self, x):
		return Matrix2(
			self.a * x,
			self.b * x,
			self.c * x,
			self.d * x
		)
	
	def multiply_matrix(self, mat):
		return Matrix2(
			self.a * mat.a + self.b * mat.c,
			self.a * mat.b + self.b * mat.d,
			self.c * mat.a + self.d * mat.c,
			self.c * mat.b + self.d * mat.d
		)
	
	def det(self):
		return self.a * self.d - self.b * self.c
	
	def trace(self):
		return self.a + self.d