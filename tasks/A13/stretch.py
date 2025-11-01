class Student:
    def __init__(self, name, marks, roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no
        self.status = "Passed" if marks >= 40 else "Failed"

    def info(self):
        print(f"Name: {self.name}\nMarks: {self.marks}\nRoll No: {self.roll_no}\nStatus: {self.status}")


s1 = Student("Alice", 85, 21)
print("student info:")
s1.info()
