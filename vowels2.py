w=input("enter words to search for vowels:")
s=set(w)
v={'a','e','i','o','u'}
r=s.intersection(v)
print("the different vowels present in",w,"are",r)