#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 04

def employee(name, monthly_salary=10000):
    tax = monthly_salary*0.02
    salarywithtaxcut = monthly_salary - tax

    print(f"Employee: {name}, Salary after tax: {salarywithtaxcut}")

employee("ibrahim", 50000) #with monthly salary in function argument

employee("ali") #without monthly salary in function argument
