#method overloading example
def product(a, b):
    p = a*b
    print(p)
def product(a, b, c):
    p = a*b*c
    print(p)
product(4,5, 1)

#polymorphism with inheritance
class animal:
    def types(self):
        print("various types of animals")

    def age(self):
        print("age of the animal")

class rabbit(animal):
    def age(self):
        print("age of rabbit")

class horse(animal):
    def age(self):
        print("age of horse")


objAnimal = animal()
objRabbit = rabbit()
objHorse = horse()

objAnimal.types()
objAnimal.age()

objRabbit.types()
objRabbit.age()

objHorse.types()
objHorse.age()
