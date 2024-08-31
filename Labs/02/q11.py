#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 11

student_dict = { "ali": [98, 87, 75, 80, 82], "ahmed": [58, 84, 95, 88, 65], "arham": [89, 84, 84, 81, 82], "hamza": [79, 83, 78, 88, 91] }

def student_avg(name):
    if name in student_dict:
        grades = student_dict[name]
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{name}'s average grade: {avg:.3f}")
        else:
            print(f"{name}has no grades in dictionary.")
    else:
        print(f"{name} not found in dictionary.")
        
def add_grade(name, grade):
    if name in student_dict:
        student_dict[name].append(grade)
    else:
        print(f"{name} not found in dictionary.")

def add_student(name, grades=[]):
    student_dict[name] = grades
    print(f"{name} added to dictionary.")

def remove_student(name):
    if name in student_dict:
        student_dict.pop(name)
        print(f"{name} removed from dictionary.")
    else:
        print(f"{name} not found in dictionary.")
        
print("student dictionary:")
print(student_dict)

student_name = str(input("enter name of student to add a new grade to: "))
new_grade = int(input(f"enter new grade to add to {student_name}'s existing list of grades: "))

add_grade(student_name.lower(), new_grade)
print(f"\ndictionary after grade addition of {student_name}")
print(student_dict)

student_name = str(input("\nenter name of student to calculate grades' average: "))
student_avg(student_name.lower())

student_name = str(input("\nenter name of new student to add to dictionary: "))
add_student(student_name.lower())
print(f"\ndictionary after addition of {student_name}")
print(student_dict)

student_name = str(input("enter name of student to remove from dictionary: "))
remove_student(student_name.lower())
print(f"\ndictionary after {student_name} is removed:")
print(student_dict)
