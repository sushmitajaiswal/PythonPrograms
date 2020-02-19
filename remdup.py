s=input("enter some string:")
l=[]
for x in s:
 if x not in l:
  l.append(x)
o=''.join(l)
print(o)