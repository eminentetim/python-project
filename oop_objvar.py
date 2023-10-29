class Robot:

	population = 0
	
	def __init__(self, name):
		self.name = name
		print("(Initializing {})".format(self.name))
		Robot.population += 1

	def die(self):
		print("{} is being destroyed".format(self.namw))
		Robot.population -= 1

	if Robot.population == 0:
		print("{} was the last one.".format(self.name))
	else:
		print("There ars still {:d} robot working.".format(Robot.population))

	def say_hi(sellf):
		print("Greetings, my master call me {}.".format(self.name))

def how_many(cls):
	print("We have {:d} robots.".format(cls.population))

droid1 = Robet("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robet("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. so let's destory them.")
droid1.die()
droid2.die()
Robot.how_man()
