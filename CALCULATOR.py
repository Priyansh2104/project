# CODE TO RUN A SIMPLE CALCULATOR IN PYTHON
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

while True:
    
    choice = input("Enter choice(a/b/c/d): ")

  
    if choice in ('a', 'b', 'c', 'd'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'a':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'b':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'c':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'd':
            print(num1, "/", num2, "=", divide(num1, num2))
        
       
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
