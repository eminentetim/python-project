class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(self.name, self.age)

class Student(Person):
	def __init__(self, name, age):
		self.sName = name
		self.sAge = age

	super().__init__("Emem", age)

	def showInfo(self):
		print(self.sName, self.sAge)


ok = student("Nancy", 26)
ok.show()
ok.showInfo()

