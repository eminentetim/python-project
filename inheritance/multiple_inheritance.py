class Dev1(object):
	def __init__(self):
		self.case1 = "ALX"
		print("Do hard thing")

class Dev2(object):
	def __init__(self):
		self.case2 = "software"
		print("I just want to be the best")

class combine(Dev1, Dev2):
	def __init__(self):

		Dev1.__init__(self)
		Dev2.__init__(self)
		print("Among the best")

	def printStrs(self):
		print(self.case1, self.case2)

ok = combine()
ok.printStrs()

	
