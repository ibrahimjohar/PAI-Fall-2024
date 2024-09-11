#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 3

class Student:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print_biodata(self):
        print(f"student name: {self.name}")
        print(f"student age: {self.age}")

student1 = Student("ali",21)
student1.Print_biodata()