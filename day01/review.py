# num = int(input("enter a number:"))
# for i in range(0,num+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)



# factorial
num =int(input("enter a number:"))
fact = 1
for i in range(1,num+1):
    fact *=i
print("factorial is :",fact)