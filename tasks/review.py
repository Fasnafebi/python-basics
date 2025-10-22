items = {
   "apple": 30,
   "banana": 20,
   "milk": 50,
   "bread": 25,
   "eggs": 5
}
cart = ["apple", "banana", "milk", "banana", "eggs", "eggs", "bread"]

total = sum(items[item] for item in cart)
print("Total cost:", total)
