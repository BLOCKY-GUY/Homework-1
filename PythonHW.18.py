def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("FUNCTION CALCULATOR")

try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    op = input("Operation (add, subtract, multiply, divide): ")

    if op == "add":
        print(f"Result: {add(num1, num2)}")
    elif op == "subtract":
        print(f"Result: {subtract(num1, num2)}")
    elif op == "multiply":
        print(f"Result: {multiply(num1, num2)}")
    elif op == "divide":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Unknown operation.")
except ValueError:
    print("Please type numbers only.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("Thanks for using the calculator!")