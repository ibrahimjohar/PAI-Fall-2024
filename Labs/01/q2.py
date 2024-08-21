#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 02

num1 = float(input("Enter Num 1: "))
num2 = float(input("Enter Num 2: "))

operator = str(input("Select operation between (+, -, *, /): "))

if operator == "+":
    result = num1 - (-num2)
    print ("Result: ", result)
elif operator == "-":
    result = num1 - num2
    print ("Result: ", result)
elif operator == "*":
    result = num1 * num2
    print ("Result: ", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print ("Result: ", result)
    else:
        print ("Num2 is 0, cannot divide Num1 with 0.")
else:
    print("Invalid Operator choosen.")
