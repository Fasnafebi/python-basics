attendance = [
    {"name": "John", "days": [20, 22, 18]},
    {"name": "Emma", "days": [25, 26, 27]},
    {"name": "Noah", "days": [15, 18, 20]}
]
from pprint import pprint
def attendance_report(attendance):
    final_output = {}
    for emp in attendance:
        avg_days = sum(emp["days"]) / len(emp["days"])
        status = "Good" if avg_days >= 22 else "Poor"
        final_output[emp["name"]] = {
            "average_days": round(avg_days, 1),
            "status": status
        }
    return final_output

pprint(attendance_report(attendance))
