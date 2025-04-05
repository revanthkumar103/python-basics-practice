print("Welcome to the Simple Calculator 🔢")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose an operation: +  -  *  /")
op = input("Enter operation: ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero not allowed!")
else:
    print("Invalid operation")
