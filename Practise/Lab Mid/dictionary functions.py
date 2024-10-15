dict = {'name': 'ibrahim', 'age': 23, 'city': 'wollongong'}


#get() - returns the value for a specified key
print("get(key)")
name = dict.get('name')
print("get(name): ", name)
age = dict.get('age')
print("get(age): ", age)
print("get(city): ", dict.get('city'))

#items() - returns a view object with key-value pairs
my_items = dict.items()
print("items in dictionary: ", list(my_items))

#keys() - returns a view object with all the keys
my_keys = dict.keys()
print("keys in dictionary: ", list(my_keys))

#values() - returns a view object with all the values
my_values = dict.values()
print("values in dictionary: ", list(my_values))

print("before pop operation: ", dict)
new_age = dict.pop('age')
print("after pop operation: ", dict)
print("popped age: ", age)


