import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y==0 :
        print("\nERROR!! Cannot divide by ZERO.")
    return x / y

print("----------BASIC CALCULATOR----------")

print("\nSelect operation.")
print("\n\t1.Add")
print("\n\t2.Subtract")
print("\n\t3.Multiply")
print("\n\t4.Divide")
print("\n\t5.Exit")


while True:
    choice = input("Enter choice from above: ")

    if choice in ('1', '2', '3', '4','5'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(a, "+", b, "=", add(a, b))

        elif choice == '2':
            print(a, "-", b, "=", subtract(a, b))

        elif choice == '3':
            print(a, "*", b, "=", multiply(a, b))

        elif choice == '4':
            print(a, "/", b, "=", divide(a, b))

        elif choice == '5':
            sys.exit("System Exiting.....")

        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")