class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def work(self):
        print(f"{self.name} is working.")

        
    def increase_salary(self):
        salary_increase = int(input("Enter the amount to increase salary: "))
        self.salary += salary_increase

        print(f"Salary increased by {salary_increase}. \n New salary is: {self.salary}")

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

emp1 = Employee("Karan", 101, 50000)

emp1.display_info()
emp1.increase_salary()
emp1.display_info()
emp1.work()