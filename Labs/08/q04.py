import numpy as np

datatype = [('name', 'S15'), ('class', int), ('height', float)]
student_det = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

#creating a structured array
students = np.array(student_det, dtype = datatype)
print('original array: ', students)

#sort by class and then height
sorted_students = np.sort(students, order=['class', 'height'])
print(sorted_students)