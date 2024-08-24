#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 11

marks_dict = {
    "Subject 1": int(input("Enter Subject 1 marks out of 50: ")),
    "Subject 2": int(input("Enter Subject 2 marks out of 50: ")),
    "Subject 3": int(input("Enter Subject 3 marks out of 50: "))
}

print("\n")

totalMarks = marks_dict["Subject 1"] + marks_dict["Subject 2"] + marks_dict["Subject 3"]

avgMarks = totalMarks / 3

for sub, marks in marks_dict.items():
    percentage = (marks / 50) * 100
    print(f"{sub}: {marks} Marks, {percentage}%")


print("\nSubject w/ Marks Dictionary: ", marks_dict)
print(f"Average Marks: {avgMarks}")
