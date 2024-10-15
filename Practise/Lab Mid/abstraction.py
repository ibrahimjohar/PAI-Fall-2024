from abc import ABC, abstractmethod

class polygon(ABC):
    @abstractmethod
    def nSides(self):
        pass

class triangle(polygon):
    #overriding abstract method
    def nSides(self):
        print("3 sides")

class pentagon(polygon):
    #overriding abstract method
    def nSides(self):
        print("5 sides")

class hexagon(polygon):
    #overriding abstract method
    def nSides(self):
        print("6 sides")

class quadrilateral(polygon):
    #overriding abstract method
    def nSides(self):
        print("4 sides")


t = triangle()
t.nSides()

q = quadrilateral()
q.nSides()

p = pentagon()
p.nSides()

h = hexagon()
h.nSides()