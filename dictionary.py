# Check and Add Key Using .get()

items = {'pen': 10, 'pencil': 5}
print("Before check:", items)

if items.get('eraser') is None:
    items['eraser'] = 7

print("After adding eraser:", items)