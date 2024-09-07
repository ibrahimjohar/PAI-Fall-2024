#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 7

def ReplaceLetterInFile(searchWord, replaceWord):
    try:        
        with open ("replacement_needed.txt", 'r+') as file:
            content = file.read()
            
            stringlist = content.split()
            
            for i in range(0, len(stringlist)):
                if stringlist[i] == searchWord:
                    stringlist[i] = replaceWord
                    
            file.write("\n")
            file.write(' '.join(stringlist))
            
            print("letter successfully updated in required word in the file.")
    except FileNotFoundError:
        print("File not found")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")


ReplaceLetterInFile("needad", "needed")