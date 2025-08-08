num1 = float(input("Enter number 1: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter number 2: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operation"

print(result)
