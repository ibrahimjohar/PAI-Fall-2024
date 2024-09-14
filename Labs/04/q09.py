#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 9

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print(f"student ID: {self.student_id}")
        print(f"student Name: {self.name}")

class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print(f"marks in algorithms: {self.marks_algo}")
        print(f"marks in data Science: {self.marks_dataScience}")
        print(f"marks in calculus: {self.marks_calculus}")

class Result(Marks):
    def calculate_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        avg_marks = total_marks / 3
        print(f"total marks: {total_marks}")
        print(f"average marks: {avg_marks:.2f}")


student1 = Result(101,"ali khan",85,90,80)
student1.display_info()
student1.display_marks()
student1.calculate_result()
