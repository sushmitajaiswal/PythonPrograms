from sys import argv
print("the number of command line arguments:", len(argv))
print("the list of command line arguments:", argv)
print("command line arguments one by one:")
for x in argv:
    print(x)