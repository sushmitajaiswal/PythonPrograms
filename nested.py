#!/usr/bin/python2
def outer():
	print("outer function started")
	def inner():
		print("inner function execution")
	print("outer function calling inner function")
	inner()
outer()