#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 05

def factorial_func(n):
    if n < 0:
        print("factorial function does not deal with negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_func(n-1)

userinput = int(input("Enter a number 'n': "))
print(f"Factorial of {userinput}: {factorial_func(userinput)}")
