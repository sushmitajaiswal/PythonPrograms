vowels=['a','e','i','o','u']
word=input("enter the words to search for vowels:")
found=[]
for letter in word:
 if letter in vowels:
  if letter not in found:
   found.append(letter)
print(found)
print("the no. of different vowels present in",word,"is",len(found))