#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 08

for x in range(0,51):
    if (x % 3 == 0 and x % 5 ==0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        
