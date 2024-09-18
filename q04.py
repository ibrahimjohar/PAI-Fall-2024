class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_student_info(self):
        print("Student ID:", self.id)
        print("Student Name:", self.name)


class Marks(Student):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print("Marks in Algorithm:", self.marks_algo)
        print("Marks in Data Science:", self.marks_dataScience)
        print("Marks in Calculus:", self.marks_calculus)


class Result(Marks):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print("Total Marks:", total_marks)
        print("Average Marks:", average_marks)


def main():
    result = Result(1, "John Doe", 80, 90, 70)
    result.display_student_info()
    result.display_marks()
    result.calculate_result()


if __name__ == "__main__":
    main()