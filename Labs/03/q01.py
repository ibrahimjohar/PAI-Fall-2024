try:
    with open('task1text.txt', 'r') as fileObj:
        content = fileObj.read()

    char_count = len(content)
    print(f"character count: {char_count}")

    word_count = len(content.split())
    print(f"word count: {word_count}")

except FileNotFoundError:
    print("the file does not exist/not found.")
except IOError:
    print("an error occured during reading the file")
except Exception as e:
    print(f"unexpected error occured: {e}")
