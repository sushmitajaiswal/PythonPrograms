n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("elements by row wise:")
for r in n:
 print(r)
print("elements by matrix style:")
for i in range(len(n)):
 for j in range(len(n[i])):
  print(n[i][j],end=' ')
 print()