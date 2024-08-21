#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 03

a1=[]
even_count=0

for x in range(0,5):
    user_input = int (input("Enter Number: "))
    a1.append(user_input)
    if user_input % 2 == 0:
        even_count += 1


print ("Even Count: ", even_count)
