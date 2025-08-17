products = [
    {"name": "Laptop", "prices": [50000, 52000, 51000]},
    {"name": "Phone", "prices": [20000, 19500, 20500]},
    {"name": "Tablet", "prices": [30000, 31000, 29000]}
]
from pprint import pprint
def product_labels(products):
    final_output = {}
    for product in products:
        avg_price = sum(product["prices"]) / len(product["prices"])
        label = "Expensive" if avg_price >= 30000 else "Affordable"
        final_output[product["name"]] = {
            "average_price": round(avg_price),
            "label": label
        }
    return final_output

pprint(product_labels(products))
