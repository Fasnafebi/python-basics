sales = [
    {"name": "Amit", "sales": [50, 60, 55]},
    {"name": "Ravi", "sales": [30, 25, 28]},
    {"name": "Neha", "sales": [70, 75, 72]}
]
from pprint import pprint
def sales_report(sales):
    final_output = {}
    for person in sales:
        avg_sales = sum(person["sales"]) / len(person["sales"])
        status = "Top Performer" if avg_sales >= 60 else "Needs Improvement"
        final_output[person["name"]] = {
            "average_sales": round(avg_sales, 1),
            "status": status
        }
    return final_output

pprint(sales_report(sales))
