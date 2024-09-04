#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 3

import json

def FileDictionaryWriteProgram(fileName, userdict):
    try:
        with open(fileName, 'w') as fileObj:
            fileObj.write(str(userdict))
        
        print("file contents now: ")

        with open(fileName, 'r') as fileObj2:
            content = fileObj2.read()
        print(content)

    except FileNotFoundError:
        print("the file does not exist/not found.")
    except IOError:
        print("an error occured during reading the file")
    except Exception as e:
        print(f"unexpected error occured: {e}")

filename = 'task3text.txt'

print("enter comma separated values for 2 lists with same number of elements (e.g: 4,6,9,10): ")
userlist1 = input("userlist1: ").split(',')
userlist2 = input("userlist2: ").split(',')

userdict = dict(zip(userlist1, userlist2)) 

FileDictionaryWriteProgram(filename, userdict)
