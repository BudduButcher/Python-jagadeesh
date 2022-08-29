def add(x, n):
    return x + n

def subtract(x, n):
    return x - n

def multiply(x, n):
    return x * n

def divide(x, n):
    return x / n
def pow(x,n):
    return x**n


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.power")

while True:
    
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "**", num2, "=", pow(num1, num2))
        
        next_calculation = input("Another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
