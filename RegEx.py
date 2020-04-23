#Yanira Manzano
#4/23/2020
#Assignment 12

import re

#Identifiers
#'''If there's a 'q', 'the' '*' a digit, period, 2 consecutive vowels,
# space, repetative letters, 'Hello', or contains an email address.'''

str = input("Type the string that you want to insert\n>>>")

#Main menu with chooses for the string
menu = 0
while menu != 11:
    menu = int(input("Choose the test\n"
                 "1. Seeing if the string has a 'q'\n"
                 "2. Seeing if the string has a 'the'\n"
                 "3. Seeing if the string has a '*' in it\n"
                 "4. Seeing if the string have a digit\n"
                 "5. Seeing if the string have a period\n"
                 "6. Seeing if the string has at least 2 consecutive vowels\n"
                 "7. Seeing if the string contains space\n"
                 "8. Seeing if the string has any letters that repeat three times in a single word\n"
                 "9. Seeing if the string starts with 'Hello'\n"
                 "10. Seeing if the string contains an email address\n"
                 "11. Quit\n"))

# Find 'q'
    if menu == 1:
        match = re.search("[q]", str)
        if match:
            print(f'There is "{match.group()}" here.')
        else:
            print("There is NO letter of 'q'")

# Find 'the' word
    elif menu == 2:
        match = re.search("the", str)
        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no 'the' in your string")

# Find * symbol
    elif menu == 3:
        match = re.search('\*', str)
        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no '*' in your string")

# Find any digits
    elif menu == 4:
        match = re.search('\d', str)
        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no digit in your string")

# Find period
    elif menu == 5:
        match = re.search('\.', str)
        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no '.' in your string")

# Find consecutive vowels "aeiou"
    elif menu == 6:
        match = re.search('[aeiou]+[aeiou]', str)
        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no two consecutive vowels in your string")

#Find any space
    elif menu == 7:
        match = re.search('\s', str)
        if match:
            print(f'There is space in your string')
        else:
            print("There is no space in your string")

#Find repetitive words
    elif menu == 8:
        match = re.search(r"\b\w*(\w)\1{2}\w*\b", str)

        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no three repetitive letters in your string")

#Find 'Hello'
    elif menu == 9:
        match = re.search("^Hello", str)
        if match:
            print(f'Yeah your string starts with "{match.group()}"')
        else:
            print("There is no 'Hello' letters in your string")

#Find email address
    elif menu == 10:
        match = re.search('\S+@\S+\.\S', str)
        if match:
            print(f'There is "{match.group()}" in your string')
        else:
            print("There is no email in your string")

#Quit Option
    elif menu == 11:
        print("Bye")
        break
#Other numbers out of the range 1-11 won't be valid in this programming
    else:
        print("Sorry but that's not valid.")
