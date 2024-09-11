#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 4

class Employee:
    name = ""
    monthly_salary = 0.0
    percentage_tax = 0.0

    def __init__(self):
        self.name = ""
        self.monthly_salary = 0.0
        self.percentage_tax = 2

    def get_data(self, e_name, e_sal, e_tax):
        self.name = e_name
        self.monthly_salary = e_sal
        self.percentage_tax = e_tax

    def salary_after_tax(self):
        self.monthly_salary = self.monthly_salary * ((100 - self.percentage_tax) / 100)
        return self.monthly_salary
    
    def update_tax_percentage(self, new_tax):
        self.percentage_tax = new_tax
        self.salary_after_tax()
        return self.monthly_salary

    def employee_details(self):
        print(f"employee name: {self.name}")
        print(f"employee monthly salary without tax cut: {self.monthly_salary}")
        print(f"employee percentage tax: {self.percentage_tax}%")
        print(f"employee monthly salary with tax cut: {self.salary_after_tax()}")
        self.monthly_salary = 1000
        print(f"employee monthly salary with new 3% tax cut: {self.update_tax_percentage(3)}")
        print(f"employee percentage tax: {self.percentage_tax}%")


emp1 = Employee()
emp1.get_data("ibrahim", 1000, 2)
emp1.employee_details()


