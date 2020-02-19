s=input("enter some string:")
o=''
for x in s:
 if x.isalpha():
  o=o+x
  previous=x
 else:
  o=o+chr(ord(previous)+int(x))
print(o)