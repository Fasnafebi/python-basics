# 1.	Add 'John': 92 if 'John' doesn’t exist
# 	2.	Increase 'Ali'’s mark by 5 using .get()
# 	3.	Print after each change


marks = {'Ali': 70, 'Sara': 88}
print("Original dictionary:", marks)

if marks.get('John') is None:
    marks['John'] = 92
print("After adding John:", marks)

marks['Ali'] = marks.get('Ali', 0) + 5
print("After updating Ali:", marks)