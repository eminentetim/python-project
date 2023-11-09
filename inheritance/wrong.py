class A:
	def __init__(self, n='Emem'):
		self.name = n

class B(A):
	def __init__(self, roll):
		self.roll = roll
		
		A.__init__(self, n='Emem')

object = B(32)
print(object.name)
		
