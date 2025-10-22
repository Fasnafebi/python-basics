print("Safe Calculator")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 == 0:
            print("Error: Cannot divide by zero!\n")
            continue
        result = num1 / num2
        print(f"Result: {result}\n")
        break
    except ValueError:
        print("Error: Please enter valid numbers!\n")
