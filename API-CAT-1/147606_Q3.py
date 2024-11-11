
class Employee:
    def Details(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def Details(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary_expenditure(self):
        return sum(employee.salary for employee in self.employees)

    def display_all_employees(self):
        for employee in self.employees:
            employee.display_details()



def main():
    department = Department("Engineering")
    emp1 = Employee("Alice", "E001", 50000)
    department.add_employee(emp1)
    department.display_all_employees()
    print("Total salary expenditure:", department.total_salary_expenditure())

if __name__ == "__main__":
    main()
