#name: ibrahim johar farooqi
#date: 28 august 2024
#lab: 02
#task: 02

def last_letter_check(input):
    last_character = input[-1].lower()

    vowel_list = 'aeiou'

    if last_character in vowel_list:
        return "The last letter is a vowel."
    else:
        return "the last letter is a consonant."
    
userinput = str(input("enter string: "))

print(last_letter_check(userinput))
