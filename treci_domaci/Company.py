class Company:
    def __init__(self, name, area, balance, max_num_of_employees):
        self.name = name
        self.area = area
        self.employees = []
        self.balance = self.validate_balance(balance)
        self.max_num_of_employees = max_num_of_employees

    def validate_balance(self, value):
        if value < 0:
            return 0
        else:
            return value

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = self.validate_balance(balance)

    def get_max_num_of_employees(self):
        return self.max_num_of_employees

    def set_max_num_of_employees(self, max_num_of_employees):
        if max_num_of_employees >= 0:
            self.max_num_of_employees = max_num_of_employees

    def add_employee(self, employee):
        if len(self.employees) < self.max_num_of_employees:
            self.employees.append(employee)
        else:
            print("Maximum number of employees reached.")

    def remove_employee(self, employee_name, employee_surname):
        for employee in self.employees:
            if employee["name"] == employee_name and employee["surname"] == employee_surname:
                self.employees.remove(employee)
                print(f"Employee {employee_name} {employee_surname} removed.")
                return
        print("Employee not found.")

    def __str__(self):
        return f"\"name\": \"{self.name}\", \"area\": \"{self.area}\", \"balance\": \"{self.balance}\""

    def can_pay_employees(self):
        total_salary = sum(employee["salary"] for employee in self.employees)
        return total_salary <= self.balance

    def __gt__(self, other):
        return len(self.employees) > len(other.employees)

company1 = Company("ABC Corp", "Technology", 10000, 20)
company2 = Company("XYZ Ltd", "Finance", 20000, 30)

print(company1)
print(company2)

company1.add_employee({"name": "John", "surname": "Doe", "salary": 3000})
company1.add_employee({"name": "Alice", "surname": "Smith", "salary": 4000})

company2.add_employee({"name": "Bob", "surname": "Jones", "salary": 3500})

company1.remove_employee("John", "Doe")

print(company1.can_pay_employees())
print(company2.can_pay_employees())

print(company1 > company2)
