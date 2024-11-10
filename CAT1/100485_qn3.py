class Employee:
    def __init__(self, employee_id: int, name: str, salary: float):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return self.display_details()

    def display_details(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary:.2f}")

    def update_salary(self, new_salary: float):
        self.salary = new_salary
        print(f"Salary updated for {self.name}. New Salary: {self.salary:.2f}")

class Department:
    def __init__(self, department_name: str):
        self.department_name = department_name
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: {total_salary:.2f}")
        return total_salary

    def display_all_employees(self):
        if not self.employees:
            print(f"No employees in {self.department_name} department.")
        else:
            print(f"Employees in {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()

# Interactive Function
def main():
    departments = {}
    
    while True:
        print("\nCompany Management System")
        print("1. Create a department")
        print("2. Add an employee to a department")
        print("3. Display employees in a department")
        print("4. Display total salary expenditure of a department")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            department_name = input("Enter the department name: ")
            if department_name in departments:
                print(f"Department {department_name} already exists.")
            else:
                departments[department_name] = Department(department_name)
                print(f"Department {department_name} created.")

        elif choice == "2":
            department_name = input("Enter the department name: ")
            department = departments.get(department_name)
            if not department:
                print(f"Department {department_name} does not exist.")
            else:
                try:
                    employee_id = int(input("Enter employee ID: "))
                    name = input("Enter employee name: ")
                    salary = float(input("Enter employee salary: "))
                    employee = Employee(name, employee_id, salary)
                    department.add_employee(employee)
                except ValueError:
                    print("Invalid input. Please enter numeric values for ID and salary.")

        elif choice == "3":
            department_name = input("Enter the department name: ")
            department = departments.get(department_name)
            if not department:
                print(f"Department {department_name} does not exist.")
            else:
                department.display_all_employees()

        elif choice == "4":
            department_name = input("Enter the department name: ")
            department = departments.get(department_name)
            if not department:
                print(f"Department {department_name} does not exist.")
            else:
                department.calculate_total_salary_expenditure()

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
