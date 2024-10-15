#keyword arguments
def details(name, age):
    print("name: ", name)
    print("age: ", age)

details('ali', 77)
print("\n")
details(77, 'ali') #positional arguments
print("\n")
details(age=77, name='ali') #keyword arguments
print("\n")

#positional variable length parameters
def details2(*name):
    print('names: ', name)

details2('ibrahim', 'johar', 'farooqi')
print("\n")

#keyword variable length parameters(*args)
def details(**name):
    print('names: ', name)

details(n1 = 'ibrahim', n2 = 'johar', n3 = 'farooqi')
print("\n")

#lamda function
add = lambda x, y, z: x + y + z
print(add(12, 13, 15))
print("\n")


