s='a4b3c2'
o=''
for ch in s:
 if ch.isalpha():
  x=ch
 else:
  d=int(ch)
  o=o+x*d
print(o)