# fruits = {'apple': 5, 'banana': 3}
# 1.	Add 'orange': 8 only if it doesn’t already exist
# 	2.	Increase 'apple' value by 5
# 	3.	Use .get() in both steps
# 	4.	Print the dictionary after each step



fruits = {'apple': 5, 'banana': 3}
print("Original dictionary:", fruits)

if fruits.get('orange') is None:
    fruits['orange'] = 8
print("After adding orange:", fruits)

fruits['apple'] = fruits.get('apple', 0) + 5
print("After updating apple:", fruits)