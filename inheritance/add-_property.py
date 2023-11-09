class Person():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(self.name, self.age)

class List(Person):
	def __init__(self, name, dob):
		self.sName = name
		self.sAge = age
		self.dob = dob

		super().__init__("Etim", age)

	def showInfo(self):
		print(self.sName, self.sAge, self.dob)
obj = List("Emem", 26, "1996")
obj.show()
obj.showInfo()
	
