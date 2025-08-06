# stock = {'milk': 10, 'bread': 15}
# 1.	Add 'eggs': 12 if not already present
# 	2.	Increase 'milk' by 5
# 	3.	Print after each step


stock = {'milk': 10, 'bread': 15}
print("Original dictionary:", stock)


if stock.get('eggs') is None:
    stock['eggs'] = 12
print("After adding eggs:", stock)

stock['milk'] = stock.get('milk', 0) + 5
print("After updating milk:", stock)