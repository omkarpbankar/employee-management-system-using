class Employee:
    def __init__(self, emp_id, name, department, salary, designation):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Designation: {self.designation}")
        print(f"Monthly Salary: ${self.salary:,.2f}")
        print("-" * 20)

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
            print(f"Salary updated to ${self.salary:,.2f} for {self.name}.")
        else:
            print("Invalid salary amount.")

    def calculate_annual_salary(self):
        return self.salary * 12


if __name__ == "__main__":
    # Creating 5 Employee objects
    emp1 = Employee(101, "Alice Smith", "Engineering", 7500, "Software Engineer")
    emp2 = Employee(102, "Bob Johnson", "HR", 5500, "HR Manager")
    emp3 = Employee(103, "Charlie Brown", "Sales", 6000, "Sales Executive")
    emp4 = Employee(104, "Diana Prince", "Marketing", 6500, "Marketing Specialist")
    emp5 = Employee(105, "Ethan Hunt", "Engineering", 9000, "Senior Software Engineer")

    employees = [emp1, emp2, emp3, emp4, emp5]

    print("--- Employee Information ---")
    for emp in employees:
        emp.display_info()
        print(f"Annual Salary: ${emp.calculate_annual_salary():,.2f}\n")

    print("--- Updating Salary ---")
    emp1.update_salary(8200)
    print(f"\nAfter update, {emp1.name}'s Annual Salary: ${emp1.calculate_annual_salary():,.2f}")
