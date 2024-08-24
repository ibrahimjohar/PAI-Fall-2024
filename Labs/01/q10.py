
userList=[] 

print("Enter a list of numbers:")

for x in range(0,5):
    num = int(input("Enter Number: "))
    userList.append(num)

maxNum = userList[0]

for x in userList:
    if x > maxNum:
        maxNum = x

print("The largest number is: ", maxNum)