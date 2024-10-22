#name: ibrahim johar farooqi
#date: 10 october 2024
#lab: 07
#task: 04

import numpy as np

datatype = [('name', 'S15'), ('class', int), ('height', float)]
student_det = [('ibrahim', 5, 48.5), ('haris', 6, 52.5), ('joshua', 5, 42.10), ('patel', 5, 40.11)]

#creating a structured array
students = np.array(student_det, dtype = datatype)
print('original array: ', students)

#sort by class and then height
sorted_students = np.sort(students, order=['class', 'height'])
print(sorted_students)
