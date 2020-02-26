import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("a new request came:")
try:
	x=int(input("enter first number: "))
	y=int(input("enter second number: "))
	print(x/y)
except ZeroDivisionError as msg:
	print("cannot divide with zero")
	logging.exception(msg)
except ValueError as msg:
	print("enter only int values")
	logging.exception(msg)
logging.info("request processing completed")