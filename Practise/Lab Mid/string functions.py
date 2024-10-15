text = "heres my demo string"
print("original: ", text)
print("capitalize(): ", text.capitalize())  #converts the 1st character to upper case
print("casefold(): ", text.casefold())      #converts string to lower case
print("center(): ", text.center(20))        #returns a centered string with padding
print("count(): ", text.count('e'))         #returns the number of times a specified value occurs in the string
print("endwith(): ", text.endswith('g'))    #returns true if string ends with specified value
print("find(): ", text.find('m'))           #searches the string for a specified value and returns the position of where it was found.
print("lower(): ", text.lower())
print("upper(): ", text.upper())
print("replace(): ", text.replace('demo', 'new'))
text = "heres my demo string"
print("rfrind(): ", text.rfind('e'))        #searches the string for a specified value and returns the last position of where it was found.
print("split(): ", text.split(' '))         #splits the string at the specified separator, and returns a list.
print("title(): ", text.title())            #converts the first character of each word to upper case.

#Joins the elements of an iterable to the end of the string.
words = ['hello', 'world', 'python']
sentence = " ".join(words)
print(sentence)
text = "ABCDE"
joined_text = "-".join(text)
print("'ABCDE' after join() function with spacing defined '-': ", joined_text)  # Output: "A-B-C-D-E"
