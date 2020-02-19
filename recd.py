n=int(input("enter no. of students:"))
d={}
for i in range(n):
 name=input("enter student name:")
 marks=input("enter student marks:")
 d[name]=marks
while True:
 name=input("enter student name to get marks:")
 marks=d.get(name,-1)
 if marks==-1:
  print("studeent not found")
 else:
  print("the marks of",name,"is",marks)
 option=input("do you want to find another student marks[yes|no]")
 if option=="no":
  break
print("thanks for using our application")