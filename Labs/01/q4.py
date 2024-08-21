#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 04

array=[]
sum = 0

for x in range(0,5):
    user_input = int(input("Enter Number: "))
    array.append(user_input)
    sum += user_input
    

print("Sum of list: ", sum)
