class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        pass

class Developer(employee):
    def work(self):
        return "Writing code..."
    
class Manager(employee):
    def work(self):
        return "Managing project..."


employees = [
    Developer("Ravi", 50000),
    Manager("Priya", 70000)
]

for emp in employees:
    print(f"employee: {emp.name}")
    print(f"Role: {emp.__class__.__name__}")
    print(f"Task: {emp.work()}\n")
