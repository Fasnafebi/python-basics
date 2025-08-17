bills = [
    {"house": "A1", "units": [300, 320, 310]},
    {"house": "B2", "units": [150, 160, 155]},
    {"house": "C3", "units": [400, 420, 410]}
]
from pprint import pprint
def bill_report(bills):
    final_output = {}
    for house in bills:
        avg_units = sum(house["units"]) / len(house["units"])
        status = "High Usage" if avg_units >= 350 else "Normal Usage"
        final_output[house["house"]] = {
            "average_units": round(avg_units, 1),
            "status": status
        }
    return final_output

pprint(bill_report(bills))
