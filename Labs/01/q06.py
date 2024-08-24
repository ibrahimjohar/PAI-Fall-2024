#name: ibrahim johar farooqi
#date: 21 august 2024
#lab: 01
#task: 06

marks = {}

marks["Physics"] = int(input("Enter physics marks: "))
marks["Chemistry"] = int(input("Enter chemistry marks: "))
marks["Maths"] = int(input("Enter maths marks: "))

avg_marks = 0.0
sum = 0
highest_marks = ''
max = -1

for x in marks:
    val = marks[x]
    if val > max:
        max = val
        highest_marks = x
    sum += val

avg_marks = sum / len(marks)

print("Average Marks: ", avg_marks)
print("Highest Marks in: ", highest_marks)
