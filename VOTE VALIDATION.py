age=int(input("enter your age:"))
if(age<=18):
    print("not eligible to vote")
    print("you are eligible after" ,int(18-age),"years")
else:
    print("you are eligible to vote")
