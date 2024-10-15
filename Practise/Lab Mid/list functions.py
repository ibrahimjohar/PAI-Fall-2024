list = [2, 12, 22, 32, 42, 52]
print("original list: ", list)

list.append(62)                     #Adds an item to the end of the list
print("append(x): ", list)

list.extend([72, 82, 92])           #Extends the list by appending elements from an iterable
print("extend(new_list): ", list)

list.insert(0, -12)          #inserts an item at a given position
print("insert(i, x): ", list)

list.remove(-12)                    #removes the first item from the list whose value is equal to x
print("remove(x): ", list)

list.pop(0)                         #removes and returns the item at the given position in the list
print("pop(i): ", list)

print("returns index of x in list -> index(x): ", list.index(32))

print("num of 2 in list -> count(x): ", list.count(12)) #Returns the number of times x appears in the list

list2 = [21, 13, 17, 9]
list2.sort(reverse=True) #descending order (True)
print(list2)
list2.sort(reverse=False) #ascending order (False)
print(list2)

list3 = ["apple", "banana", "cherry", "kiwi"]
list3.sort(key = len)
print("list3 sorted by length of words: ", list3)
list3.sort(key = len, reverse = True)
print("list3 sorted by length of words & descending order: ", list3)

print("original list: ", list)
list.reverse()                  #Reverses the elements of the list in place
print("reverse(): ", list)

#reversing a list without modifying the original list
reversed_list = list[::-1]  #with slicing
print("reversed_list = list[::-1] : ", reversed_list)

