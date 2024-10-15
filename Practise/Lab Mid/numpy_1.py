import numpy as np

#1d array
arr = np.array([1,2,3])
print("1d array: ",arr)
print("\n")

#2d array
arr = np.array([[1,2,3], [4,5,6]])
print("2d array:\n", arr)
print("dimensions: ", arr.ndim)
print("\n")

#converting a list to numpy array
list1 = [12,14,32,100,24]
print("original list: ", list1)
arr = np.array(list1)
print("1d numpy array: ", arr)
print("\n")

#append values to numpy array
x = [10, 20, 30]
arr1 = np.array(x)
print("array x: ", arr1)
arr1 = np.append(arr1, [[40,50,60], [70, 80, 90]])
print("after appending new vals: ", arr1)
print("\n")

#finding common vals between two arrays
array1 = np.array([0, 10, 20, 40, 60])
print("array1: ", array1)
array2 = np.array([10, 30, 40])
print("array2: ", array2)

print("common values between two arrays: ")
print(np.intersect1d(array1, array2))
print("\n")

#create numpy arrays with zeros and ones
a = np.zeros([2,2], dtype = int)
print(a)
print('\n')
b = np.ones([2,2], dtype = int)
print(b)
print('\n')

#create an identity matrix
c = np.eye(3, dtype=int)
print(c)
print('\n')
c = np.eye(3,4, dtype=int)
print(c)
print('\n')

#matrix with elements on its diagnol
d = np.diag([1,2,3,4,5])
print(d)
print('\n')

#checking for null values
e = np.array([1, 0, np.nan, 3])
print("original arr: ", e)
print("test element-wise for NaN: ")
print(np.isnan(e))
print('\n')

#create numpy arrays using 'arange' function
#arange(starting, ending, step)
print("arrange function:")
print("0->2: ", np.arange(3))
print("3->7: ", np.arange(3, 8))
print("0->20: ", np.arange(0, 20, 2))
print("\n")

#reshape() - creating a multi-dimensional array using arange and reshape
print("original: ", np.arange(10,22))
f = np.arange(10,22).reshape((3,4))
print("reshaped arr:\n",f)
print("\n")

#array slicing
arr = np.array([1,2,3,4,5,6,7,8,9])
print("original: ", arr)
print("arr[1:5] = ",arr[1:5])
print("arr[4:] = ",arr[4:])
print("arr[1:7:2] = ", arr[1:7:2])
#checking shape of array
print("shape of arr: ", arr.shape)
#reshaping
arr = arr.reshape(3,3)
print("reshaped arr:\n", arr)
print("\n")

#iterating numpy arrays
y = np.arange(0,5)
print(y)
print("iterating 1d array:")
for var in y:
    print(var)

print("iterating a 2d array:")
for var in arr:
    print(var)

print("iterating a 2d array using nested loops(2):")
for x in arr:
    for y in x:
        print(y)

print('\n')
#using nditer()
for x in np.nditer(arr):
    print(x)

print('\n')
#numpy array join using np.concatenate()
arr1 = np.arange(1,4)
arr2 = np.arange(4,7)

arr = np.concatenate((arr1,arr2))
print("concatenated arr: ", arr)
#joining with axis=0 and axis=1
arr = np.concatenate((arr1,arr2), axis=0)
print("concatenated arr on axis=1:\n", arr)
print("\n")

#stacking along rows using hstack & vstack along cols
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print("arr1: ", arr1, " arr2: ", arr2)
arr = np.hstack((arr1, arr2))
print("after hstack: ",arr)
arr = np.vstack((arr1, arr2))
print("after vstack:\n", arr)
print("\n")

#array_split() for splitting arrays
arr1 = np.array([1,2,3,4,5,6])
new_arr = np.array_split(arr, 3)
print(new_arr)

#array searching using where() function, returns arr of instances where value was found
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print("index pos where 4 was found in 'arr': ", x)

arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2 == 0)
print("index pos where even numbers was found in 'arr': ", x)

#np.searchsorted() to find where an element should be inserted inside a sorted list, uses binary search in the array

print("\n")

#array sorting
arr = np.array([3,2,0,1])
print("unsorted: ", arr)
print("sorted: ", np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print("unsorted: ", arr)
print("sorted: ", np.sort(arr))

arr = np.array([[3,2,4], [5,0,1]])
print("unsorted:\n", arr)
print("sorted:\n", np.sort(arr))





