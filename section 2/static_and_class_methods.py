# @staticmethod nd @classmethod in python

class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = [10]

	def addMarks(self,mark):
		self.marks.append(mark)

	@classmethod
	def addFriend(*args):
		if len(args)==3:
			return args[0](args[2],args[1].school)
		elif len(args)==4:
			return args[0](args[2],args[1].school,args[3])

class WorkingSudent(Student):
	def __init__(self,name,school,salary):
		super().__init__(name,school)
		self.salary = salary

anna = WorkingSudent("Anna","MIT",234)
anna.addMarks(50)
print('{} studies in {} school. Her salary is ${}. Her marks are {}'.format(anna.name,anna.school,anna.salary,anna.marks))

greg = WorkingSudent.addFriend(anna,"Greg",325)
greg.addMarks(80)
print('{} studies in {} school. His salary is ${}. His marks are {}'.format(greg.name,greg.school,greg.salary,greg.marks))

rachel = Student('Rachel','Stanford')
rachel.addMarks(60)
print('{} studies in {} school. Her marks are {}'.format(rachel.name,rachel.school,rachel.marks))

sam = Student.addFriend(rachel,'Sam')
sam.addMarks(85)
print('{} studies in {} school. His marks are {}'.format(sam.name,sam.school,sam.marks))