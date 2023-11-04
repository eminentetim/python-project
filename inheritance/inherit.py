class Person(object):

#constructor

	def __init__(self, name, id):
		self.name = name
		self.id = id

	def Display(self):
		print(self.name, self.id)

show = Person("Emem", 1456)
show.Display()

