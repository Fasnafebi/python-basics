students = [
    {"name": "Ali", "marks": [78, 85, 90]},
    {"name": "Sara", "marks": [92, 88, 95]},
    {"name": "Omar", "marks": [60, 65, 58]},
    {"name": "Nina", "marks": [55, 48, 60]},   # Likely fail
    {"name": "Zaid", "marks": [80, 82, 85]},   # High scorer
    {"name": "Maya", "marks": [70, 75, 68]},   # Just above pass
    {"name": "Imran", "marks": [40, 50, 45]},  # Low scorer
    {"name": "Laila", "marks": [88, 92, 85]}   # Competitive high scorer
]
# {

#     "Ali": {"average": 84.3, "status": "Pass"},

#     "Sara": {"average": 91.6, "status": "Pass"},

#     "Omar": {"average": 61.0, "status": "Pass"}

# }
def calculate_average(marks):

 for _ in marks:

  print(_)


calculate_average(students)

 