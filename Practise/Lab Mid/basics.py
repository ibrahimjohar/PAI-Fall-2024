#types of data types

list_data = [11,12,13,14,15, 'orange']

tuple_data = (12,15,17, 'kiran')

set_data = {'ali', 'hasan', 'ayesha', 12, 18.6}

range_data = range(1,11)

print('list data: ', list_data)
print('tuple data: ', tuple_data)
print('set data: ', set_data)
print('range data: ', range_data)

#playing with different operations on a list

list_data.append('apple')
print('updated list: ', list_data)

print('custom element viewing list_data[2]: ',list_data[2])

del list_data[2]
print('updated after deleting 02 index element in list: ', list_data)

print('\n')
#playing with different tuple operations

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tiny_tuple = (123, 'john')

#tuples' size cannot be changed, can be thought as read-only lists

print(tuple)    #print complete tuple
print(tuple[0]) #print first element of tuple
print(tuple[1:3]) #prints elements from 2nd till 3rd
print(tuple[2:])  #prints elements starting from the 3rd element

print(tiny_tuple * 2) #prints tuple two times, prints concatenated tuple

print('\n')

#playing with different operations with dictionaries
dict = {}

dict['col1'] = "this is column number one"

dict[2] = "this is column number two"

print('===  created dictionary  === ', dict)

print(dict['col1']) #prints value for 'one key

print(dict[2]) #prints value for 2 keys

print('\n')

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(tinydict) #prints complete dictionary

print("tinydict keys: ", tinydict.keys()) #prints all the keys

print("tinydict values: ", tinydict.values()) #prints all the values