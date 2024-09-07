#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 8

try:
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    print(f"num1 / num2: {num1 / num2}")
    
except ZeroDivisionError:
    print("math error")
except ValueError:
    print("invalid string input")