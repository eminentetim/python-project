
class Person(object):
 
    # Constructor
	def __init__(self, name, id):
        	self.name = name
		self.id = id
 
    # To get name
	def getName(self):
		return self.name

    #get id
	def getId(self):
		return self.id
 
    # To check if this person is an employee
	def isEmployee(self):
		return False
 
 
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
 
    # Here we return: true
	def isEmployee(self):
		return True
 
 
# Driver code
emp = Person("Geek1", 100)  # An Object of Person
print(emp.getName(), emp.getId(), emp.isEmployee())
 
emp = Employee("Geek2", 40)  # An Object of Employee
print(emp.getName(), emp.getId(), emp.isEmployee())
