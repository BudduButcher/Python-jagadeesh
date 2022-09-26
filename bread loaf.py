a = int(input("enter the number of fresh loaves purchased:"))
b = int(input("enter the number of day old loaves purchased:"))
r=185*a
d=0.6*185*b
if a<0:
    print("INVALID INPUT!!!")
else:
    print("regular price for each : RS.185")
    print("amount of new loaves: " + str(r))
    print("amount of day old loaves: "+ str(d))
    print("Total Amount to be paid: " +str(r+d))
