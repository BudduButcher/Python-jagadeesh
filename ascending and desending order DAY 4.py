B =[]
s= int(input("Enter the number of elements you want to print : "))
l= str(input("Order (A/D): "))
for i in range(s):
    e= str(input(" "))
    B.append(e)
B.sort()
if (l == 'A'):
    for sel in B:
        print(sel)
else:
    B.sort(reverse=True)
    for sel in B:
        print(sel)
