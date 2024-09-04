#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 2

def FileReadReplaceProgram(fileName, searchText, replaceText):
    try:
        with open(fileName, 'r') as fileObj:
            content = fileObj.read()

        updated_content = content.replace(searchText, replaceText)

        with open(fileName, 'w') as fileObj2:
            fileObj2.write(updated_content)

        print("replacement done successfully. and the file has been updated")  

    except FileNotFoundError:
        print("the file does not exist/not found.")
    except IOError:
        print("an error occured during reading the file")
    except Exception as e:
        print(f"unexpected error occured: {e}")

filename = 'task2text.txt'

searchtext = str(input("enter text to search in file: "))

replacetext = str(input("enter text to replace in place of 'searchtext': "))

FileReadReplaceProgram(filename, searchtext, replacetext)
