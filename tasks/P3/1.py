employees = [
    {"name": "John", "salary": [2500, 2600, 2550]},
    {"name": "Emma", "salary": [3000, 3100, 3050]},
    {"name": "Noah", "salary": [2000, 1900, 2100]},
    {"name": "Sophia", "salary": [2800, 2850, 2900]}
]
from pprint import pprint
def average(employees): 
    final_output = {}
    for employee in employees:
        avgsalary = sum(employee["salary"]) / len(employee["salary"])
        status = "high" if avgsalary >= 2800 else "low"

        final_output[employee["name"]] = {
            "average": avgsalary,
            "status": status
        }
    return final_output

pprint(average(employees))
