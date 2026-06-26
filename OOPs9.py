class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee name:{self.name} \nsalary {self.salary}")

class Developer(Employee):
    def __init__(self, name, salary, langauge):
        super().__init__(name, salary)
        self.langauge = langauge

    def work(self):
        print(f"{self.name} is working in {self.langauge}")

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)

        self.tool = tool

    def work(self):
        print(f"{self.name} is desinging with {self.tool}")

dev = Developer("Karan", 50000, "Python")
des = Designer("Rahul", 45000, "Figma")

employees = [dev , des]

for employees in employees:
    employees.display()
    employees.work()
    print("----------------")
        