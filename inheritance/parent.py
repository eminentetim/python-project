class Person(object):

	def __init__(self, name , id):
		self.name = name
		self.id = id

	def show(self):
		print(self.salary)
		print(self.name)
		print(self.id)
		print(self.point)
class Dev(Person):

	def __init__(self, name, id, salary, point):
		self.salary = salary
		self.point = point

		Person.__init__(self, name, id)

let = Dev('Emem', 5000, 100000, 'Software')

let.show()
