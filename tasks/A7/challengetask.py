def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("\t1\tAdd")
    print("\t2\tSubtract")
    print("\t3\tMultiply")
    print("\t4\tDivide")
    
    choice = input("Choose operation: ")

    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            result = add(a, b)
        elif choice == '2':
            result = subtract(a, b)
        elif choice == '3':
            result = multiply(a, b)
        elif choice == '4':
            result = divide(a, b)

        print(f"Result: {result}")
    else:
        print("Invalid choice.")

calculator()