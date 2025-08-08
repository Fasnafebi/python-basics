# Check and Add Key Using .get()

items = {'pen': 10, 'pencil': 5}
print("Before check:", items)

if items.get('eraser') is None:
    items['eraser'] = 7

print("After adding eraser:", items)


# Increment Value Using .get()

# stock = {'milk': 5, 'eggs': 12}
# Use .get() to increment 'milk' by 3. If it doesn’t exist, treat as 0.


stock = {'milk': 5, 'eggs': 12}
print("Before update:", stock)

stock['milk'] = stock.get('milk', 0) + 3

print("After update:", stock)



