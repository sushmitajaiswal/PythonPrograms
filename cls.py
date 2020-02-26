class Person:
	def _init_(self):
		self.name='sush'
		self.dob=self.DOB()
    def display(self):
		print('name: ',self.name)

	class DOB:
		def _init_(self):
			self.dd=15
			self.mm=8
			self.yyyy=1995
 		def display(self):
			print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
p=Person()
p.display()
x=p.dob
x.display()