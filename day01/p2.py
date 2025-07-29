num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

''' count vowels in a string'''

text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

'''maximum in a list'''
numbers = [10, 5, 23, 7, 31]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Maximum number is:", max_num)


'''fibonacci series'''
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

'''check armstrong number'''
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

'''remove duplicates from a list'''
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("Without duplicates:", unique)

