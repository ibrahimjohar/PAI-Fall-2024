#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 5

import json

dictionary = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}

filename = 'task5file.json'

try:
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

    with open(filename, 'r') as file:
        content = json.load(file)

    print("loaded content:", content)

    maxAge = None
    maxName = None

    for name, age in content.items():
        if maxAge is None or age > maxAge:
            maxAge = age
            maxName = name

    age_count = {}
    for age in content.values():
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1

    sameAge = {}
    for name, age in content.items():
        if age_count[age] > 1:
            sameAge[name] = age

    print("max age: ", maxAge, " Name: ", maxName)
    print("people with the same age:", sameAge)
except FileNotFoundError:
    print('file does not exist')
except IOError:
    print('could not read/write file')
except:
    print('unexpected error')