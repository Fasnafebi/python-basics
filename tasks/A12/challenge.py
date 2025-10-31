def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    terms = int(input("Enter how many terms: "))
    if terms <= 0:
        print("Please enter a positive number!")
    else:
        print("Fibonacci sequence:")
        for i in range(terms):
            print(fibonacci(i), end=" ")
        print()
except ValueError:
    print("Error: Please enter a valid number!")
