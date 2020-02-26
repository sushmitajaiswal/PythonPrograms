class Student:
	def setName(self,name):
		self.name=name

	def getName(self):
		return self.name

	def setMarks(self,marks):
		self.marks=marks

	def getMarks(self):
		return self.marks

n=int(input('enter no. of students:'))
for i in range(n):
	s=Student()
	name=input('enter name:')
	s.setName(name)
	marks=int(input('enter marks:'))
	s.setMarks(marks)

	print('hi',s.getName())
	print('your marks is:',s.getMarks())
	print()
