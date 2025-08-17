customers = [
    {"name": "Alice", "orders": [1200, 1500, 1300]},
    {"name": "Bob", "orders": [500, 700, 600]},
    {"name": "Charlie", "orders": [2500, 2600, 2400]}
]
from pprint import pprint
def customer_types(customers):
    final_output = {}
    for cust in customers:
        avg_order = sum(cust["orders"]) / len(cust["orders"])
        status = "VIP" if avg_order >= 2000 else "Regular"
        final_output[cust["name"]] = {
            "average_spending": round(avg_order),
            "status": status
        }
    return final_output

pprint(customer_types(customers))
