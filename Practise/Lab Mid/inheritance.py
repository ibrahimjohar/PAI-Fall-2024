class child():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isStudent(self):
        return False;

class student(child):
    def isStudent(self):
        return True


#object of child
std = child("salman")
print(std.getName(), std.isStudent())

#object of student
std = student("muneeb")
print(std.getName(), std.isStudent())



##SINGLE INHERITANCE
#base class
class parent:
    def func1(self):
        print('this function is in parent class')

#derived class
class child(parent):
    def func2(self):
        print("this function is in child class")


obj = child()
obj.func1()
obj.func2()

##MULTIPLE INHERITANCE
#base class
class mother:
    mothername=""
    def __init__(self):
        pass


# base class
class father:
    fathername = ""
    def __init__(self):
        pass

class son(mother, father):
    def parents(self):
        print("father: ", self.fathername)
        print("mother: ", self.mothername)

s1 = son()
s1.fathername = "jon carter"
s1.mothername = "alice carter"
s1.parents()

#super() - call a method from a parent class within a child class

class parents:
    def show(self):
        print("this is the parents class")

class child(parents):
    def show(self):
        super().show() #calls the show method of the parent class
        print("this is the child class")

child_1 = child()
child_1.show()
