# students = [
#    {"name": "Alice", "Math": 95, "Science": 85, "English": 78},
#    {"name": "Bob", "Math": 65, "Science": 70, "English": 60},
#    {"name": "Charlie", "Math": 50, "Science": 55, "English": 45}
# ]
# final_output={}
# for student in students:
#     student["marks"]=students.get(marks)
#     average_score=sum(student["marks"])/len(student["marks"])
#     total_score=sum(student["marks"])
# if average_score>=90:
#     grade= "A"
# elif 75>=average_score<=89:
#     grade="B"
# elif 60>=average_score<=74:
#     grade="c"
# elif average_score<60:
#     grade="D"
# else:
#     grade="F"
# final_output[student["name"]]={
#     "average":average_score,
#     "total":total_score,
#     "grade":grade
# }
# print(final_output)
students = [
    {"name": "Alice", "Math": 95, "Science": 85, "English": 78},
    {"name": "Bob", "Math": 65, "Science": 70, "English": 60},
    {"name": "Charlie", "Math": 50, "Science": 55, "English": 45}
]

final_output = {}

for student in students:
    # Get marks from the student dictionary (excluding the name)
    marks = [score for subject, score in student.items() if subject != "name"]
    
    average_score = sum(marks) / len(marks)
    total_score = sum(marks)

    # Assign grade based on average
    if average_score >= 90:
        grade = "A"
    elif 75 <= average_score <= 89:
        grade = "B"
    elif 60 <= average_score <= 74:
        grade = "C"
    elif average_score < 60:
        grade = "D"
    else:
        grade = "F"

    # Store results
    final_output[student["name"]] = {
        "average": average_score,
        "total": total_score,
        "grade": grade
    }

print(final_output)
