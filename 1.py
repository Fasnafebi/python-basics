# Increment Value Using .get()

# stock = {'milk': 5, 'eggs': 12}
# Use .get() to increment 'milk' by 3. If it doesn’t exist, treat as 0.


stock = {'milk': 5, 'eggs': 12}
print("Before update:", stock)

stock['milk'] = stock.get('milk', 0) + 3

print("After update:", stock)


