#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 05

a1=[]

for x in range(0,5):
    user_input = int(input("Enter Number: "))
    a1.append(user_input)

num = int(input("Enter a number to remove all numbers lesser than it: "))

for x in a1[:]:
    if x < num:
        a1.remove(x)

print("List after removing numbers less than ", num)

print(a1)
