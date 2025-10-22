products = [
    {"name": "Laptop", "prices": [50000, 52000, 51000]},
    {"name": "Phone", "prices": [20000, 19500, 20500]},
    {"name": "Tablet", "prices": [30000, 31000, 29000]}
]
from pprint import pprint
final_output={}
 def average_price(products):
    for price in products:
     avg=sum(products["price"])/len(products["prices"])
     label="expensive" if average>=30000 else "affordable"
final_output[products["price"]]= {
   "average" :avg ,
   "Label": label
}

return final_output
pprint(average_price(products))
