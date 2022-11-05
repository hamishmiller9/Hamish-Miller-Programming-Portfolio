#Line 2 will import the random function to be used for the random generation of passwords.
import random

#Lines 6 to 19 will ask the user how many passwords are needed, whilst checking if the input is valid.
Continue = False
while Continue == False:
    NumofPasswords = input("Please enter the amount of passwords required: ")
    try:
        NumofPasswords = int(NumofPasswords)
    except:
        print("Please enter an integer")
        continue
    if NumofPasswords > 24:
        print("Please enter a value between 1-24")
    elif NumofPasswords < 1:
        print("Please enter a value between 1-24")
    else:
        print("You will recieve", NumofPasswords, "Passwords...")
        Continue = True

#lines 22 to 31 will generate a random password and display to the user
x = int(0)
CONSTANTS = ['Cheese', 'Orange', 'Peugeot', 'Yaddle', 'Chicken', 'Pound', 'Coffee', 'Intel']
while NumofPasswords > 0:
    CONSTANT1 = random.choice(CONSTANTS)
    CONSTANT2 = random.choice(CONSTANTS)
    CONSTANT3 = random.choice(CONSTANTS)
    Userpasswordlist = [(CONSTANT1 + CONSTANT2 + CONSTANT3)]
    x = x + 1
    print(x, "-->", *Userpasswordlist)
    NumofPasswords = NumofPasswords - 1