def decor(func):
	def innner(name):
		if name=="Sunny":
			print("Hello Sunny Bad Morning")
		else:
			func(name)
	return innner

def wish(name):
	print("Hello",name,"Good Morning")

decorfunction=decor(wish)

wish("Durga")
wish("Sunny")

decorfunction("Durga")
decorfunction("Sunny")