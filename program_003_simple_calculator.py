# Simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else: 
        return x / y
    
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Devide")

while True: 
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "x", num2, "=", multiply(num1, num2))
        elif choice == '4': 
            print(num1, "/", num2, "=", divide(num1, num2))

# ask user if they want to preform anothe computation.

        next_calculation = input("Would you like to do another computation? yes or no?")
        if next_calculation.lower() != 'yes':
            break
    
else:
    print("Invalid Input")