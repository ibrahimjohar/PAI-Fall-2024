#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 6

def WriteSentenceToFile(filename, sentence):
    try:
        flag = False
        for i in sentence:
            if i == '?':
                flag = True
                break
        
        with open(filename, 'w') as file:
            if (flag):
                file.write(sentence)
                print("sentence written to file successfully")
            else:
                print("no question found in sentence, to write to file")
                
    except FileNotFoundError:
        print("the file does not exist/not found.")
    except IOError:
        print("an error occured during reading the file")
    except Exception as e:
        print(f"unexpected error occured: {e}")
            
filename = 'questions.txt'
user_sentence = (str(input("enter sentence to write to file: ")))
WriteSentenceToFile(filename, user_sentence)
            
