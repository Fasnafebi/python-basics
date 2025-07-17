number = int(input("Enter a number: "))

print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 20)  