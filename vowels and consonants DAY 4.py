n=input("enter the character:")
print("\n vowels are:")
for i in n:
   if i in "aeiouAEIOU":
      print(i,end=',')
print("\n consonant are:")
for i in n:
   if i not in "aeiouAEIOU":
      print(i,end=',')
