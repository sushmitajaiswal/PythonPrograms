
import sys
class Customer:
	'''Customer class with bank operations..'''
	bankname='SUSHBANK'
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance
	def deposit(self,amt):
		self.balance=self.balance+amt
		print('Balance after deposit:',self.balance)
	def withdraw(self,amt):
		if amt>self.balance:
			print('insufficient funds..cannot perform this operation')
			sys.exit()
		self.balance=self.balance-amt
		print('Balance after withdraw:',self.balance)
print('Welcome to',Customer.bankname)
name=input('Enter your name:')
c=Customer(name)
while True:
	print('d-Deposit\nw=withdraw\ne-exit')
	option=input('choose your option:')
	if option=='d' or option=='D':
		amt=float(input('enter amount:'))
		c.deposit(amt)
	elif option=='w' or option=='W':
		amt=float(input('enter amount:'))
		c.withdraw(amt)
	elif option=='e' or option=='E':
		print('Thanks for banking')
		sys.exit()
	else:
		print('invalid option..plz choose valid option')