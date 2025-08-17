students = [
    {"name": "Ali", "marks": [78, 85, 90]},
    {"name": "Sara", "marks": [92, 88, 95]},
    {"name": "Omar", "marks": [60, 65, 58]}
]
from pprint import pprint
def student_results(students):
    final_output = {}
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        status = "Pass" if avg >= 70 else "Fail"
        final_output[student["name"]] = {
            "average": round(avg, 1),
            "status": status
        }
    return final_output

pprint(student_results(students))
