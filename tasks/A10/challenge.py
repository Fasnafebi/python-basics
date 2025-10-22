print("Grade Calculator") 

def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

while True:
    try:
        n = int(input("How many grades to enter? "))
        if n <= 0:
            print("Error: Number of grades must be positive!")
            continue
        break
    except ValueError:
        print("Error: Please enter a valid number!")

grades = []
for i in range(1, n + 1):
    while True:
        try:
            grade = float(input(f"Enter grade {i} (0-100): "))
            if grade < 0 or grade > 100:
                print("Error: Grade must be between 0 and 100!")
                continue
            grades.append(grade)
            break
        except ValueError:
            print("Error: Please enter a valid number!")
average = sum(grades) / n
print(f"Average grade: {average}")
print(f"Letter grade: {letter_grade(average)}")
