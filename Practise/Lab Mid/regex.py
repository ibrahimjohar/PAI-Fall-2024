import re

#findall(pattern, string) - returns a list containing all matches
txt = "the rain in spain"
print("original text: ", txt)
foundtxt = re.findall("ai", txt)
print(foundtxt)
print("found {} matches".format(len(foundtxt)))

print("\n")

foundtxt = re.findall("portugal", txt)
print(foundtxt)
print("found {} matches".format(len(foundtxt)))

print("\n")

#search(pattern, string) - returns a match object if there is a match anywhere in the string
foundtxt = re.search("rain", txt)
print("text found: ", foundtxt)
print("starting: ", foundtxt.start())
print("ending: ", foundtxt.end())

print("\n")

#split(pattern, string) - returns a list where the string has been split at each match
foundtxt = re.split(" ", txt)
print(foundtxt)

print("\n")

#sub(pattern, replace, string) - replaces one or many matches with a string
foundtxt = re.sub("i", "I", txt)
print(foundtxt)

print("\n")

#finditer(pattern, string) - returns an iterator that yields Match objects for all non-overlapping matches found anywhere in the string
txt2 = "the quick brown fox jumps over the lazy dog"
foundtxt = re.finditer(" ", txt2)

for match in foundtxt:
    print(match)

print("\n")

#span() - returns the start & end positions of the match
text3 = "hello mistor world"
pattern = "world"
match = re.search(pattern, text3)
print("span: ", match.span())

#string() - returns the string passed into the search function
print("string found: ", match.string)

#group() - returns the part of the string where there was a match
print("group(): ", match.group())

