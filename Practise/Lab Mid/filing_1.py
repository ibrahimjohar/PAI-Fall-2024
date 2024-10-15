#reading from a text file
print('using read():')
with open(r'text.txt') as file:
    content = file.read()
print(content)

print('\n')

print('using readlines():')
with open(r'text.txt') as file2:
    filecontents = file2.readlines()
print(filecontents)

#writing to a text file
with open("text2.txt", 'w') as file3:
    file3.write("i am writing text to a file.\n")

#appending to a text file
with open("text2.txt", 'a') as file4:
    file4.write("im appending text to a file now.\n")

#reading from text2 file
with open("text2.txt", 'r') as file5:
    content = file5.readlines()
print("\nafter writing and appending text2.txt file:\n", content)
print("\n")

#reading and writing
with open('text3.txt', 'r+') as file6:
    file6.write("i love programing(not).\ni love video editing\n")

    file6.seek(0)
    content = file6.readlines()
    print("file 3 content:\n",content)

#for importing/loading dictionaries from files
import json

stu={}
filename = "text.txt"
with open(filename) as file:
    stu = json.load(file)