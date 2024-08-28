#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 03

userURL = str(input("Enter URL starting with 'http://www.': "))

if userURL.startswith("http://www."):
    newURL = userURL[11:]
    if not newURL.endswith(".com"):
        newURL += ".com"
        print("Converted User URL: ", newURL)
else:
    print("URL did not start with 'http://www.'")
