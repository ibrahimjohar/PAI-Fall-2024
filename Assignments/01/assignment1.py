#ibrahim johar farooqi
#23k-0074
#bai-3a - programming for ai - assignment 1

#base class
class animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.available = True

    #marking as available
    def mark_as_available(self):
        self.available = True

    #marking as quarantine
    def mark_as_quarantine(self):
        self.available = False

    #polymorphism showcased here
    def display(self):
        print(f"animal name: {self.name}")
        print(f"animal age: {self.age}")
        print(f"animal habitat: {self.habitat}")
        status = "yes" if self.available else "in quarantine"
        print(f"is {self.name} available to be viewed?: {status}")

#derived class
class mammal(animal):
    def __init__(self, name, age, habitat, furLength, dietType):
        super().__init__(name, age, habitat)
        self.furLength = furLength
        self.dietType = dietType

    def display(self):
        super().display()
        print(f"fur length: {self.furLength}")
        print(f"diet type: {self.dietType}")

#derived class
class bird(animal):
    def __init__(self, name, age, habitat, wingspan, flightAltitude):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flightAltitude = flightAltitude

    #polymorphism showcased here
    def display(self):
        super().display()
        print(f"wing span: {self.wingspan}")
        print(f"flight altitude: {self.flightAltitude}")


#derived class
class reptile(animal):
    def __init__(self, name, age, habitat, scalePattern, venomous_stat):
        super().__init__(name, age, habitat)
        self.scalePattern = scalePattern
        self.venomous_stat = venomous_stat

    #polymorphism showcased here
    def display(self):
        super().display()
        print(f"scale pattern: {self.scalePattern}")
        print(f"venomous status: {self.venomous_stat}")

reptile1 = reptile("anaconda", 4, "rainforest", "striped", "venomous")
mammal1 = mammal("rhino", 12, "savannah", 2.3, "herbivore")
bird1 = bird("sparrow", 5, "mountain", 2.2, 4500)

print("before availability status is changed:\n")
mammal1.display()
print("\n")
bird1.display()
print("\n")
reptile1.display()

print("\nafter availability status is changed:")
bird1.mark_as_quarantine()
mammal1.mark_as_available()
reptile1.mark_as_quarantine()

mammal1.display()
print("\n")
bird1.display()
print("\n")
reptile1.display()
