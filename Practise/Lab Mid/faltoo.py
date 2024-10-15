
for var in range(0,51):
    if(var % 3 == 0 and var % 5 == 0):
        print("Fizzbuzz")
    elif(var % 3 == 0):
        print("Fizz")
    elif(var % 5 == 0):
        print("Buzz")
    else:
        print(var)

