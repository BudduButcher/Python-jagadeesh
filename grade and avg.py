sub1 = int(input("Enter marks obtained in subject 1: "))
sub2 = int(input("Enter marks obtained in subject 2: "))
sub3 = int(input("Enter marks obtained in subject 3: "))

avg_marks =(sub1+sub2+sub3)/3
print("Average mark:",avg_marks)

if avg_marks>=90:
    print("Grade is A")
elif avg_marks>=80:
    print("Grade is B")
elif avg_marks>=70:
    print("Grade is C")
elif avg_marks>=60:
    print("Grade is D")
else:
    print("Grade is F")
