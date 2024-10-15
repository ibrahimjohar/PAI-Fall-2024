fruits = ["apple", "banana", "cherry", "date"]

for index, fruit in enumerate(fruits):
    print(f"index {index}: {fruit}")

print("\n")

languages = ['python', 'java', 'javascript']
enumerate_prime = enumerate(languages)
print(list(enumerate_prime))

print("\n")

languages = ['python', 'java', 'javascript']
enumerate_prime = enumerate(languages,10)
print(list(enumerate_prime))

print("\n")

grocery = ['bread', 'milk', 'butter']
enumerate_grocery = enumerate(grocery)

for i, j in enumerate(grocery, 20):  #second parameter sets the base starting value
    print(i, j)