def f(n):
 if n==0:
  r=1
 else:
  r=n*f(n-1)
 return r
print("factorial of 4 is:",f(4))
print("factorial of 5 is:",f(5))