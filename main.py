from string import ascii_lowercase as abc
from random import randint, choice
digits = "0123456789"
symbols = "!$%^&*()-_=+"
letters = abc + abc.upper()
validchars = letters + digits + symbols

def seq(string):
    for i in range(len(string)-2):
        yield string[i:i+3]
    return

def keyboardCheck(password):
    penalty = 0
    lines = ["qwertyuiop",
             "asdfghjkl",
             "zxcvbnm"]
    for line in lines:
        for s in seq(line):
            if s in password.lower():
                penalty += 5
    return penalty

def valid_password(password):
    if len(password) >= 8 and len(password) <= 24:
        for c in password:
            if not c in validchars:
                return False
        return True
    return False

def contains(characters, string):
    for c in characters:
        if c in string:
            return True
    return False

def points(password):
    p = 0
    #check for uppercase and lowercase letters
    if password.lower() != password: p += 5
    if password.upper() != password: p += 5
    #check if a number or digit is in the password
    if contains(digits, password): p += 5
    if contains(symbols, password): p += 5
    # if a number, letter, and symbol is in the password add an extra 10 points
    if p == 20:
        p += 10
    elif p == 5:
        # must just be one type due to amount of poitns
        p -= 5
    elif p == 10:
        # could just be letters
        if not (contains(symbols, password) or contains(digits, password)): # if only letters
            p -= 5
    # now check qwerty keyboard layout
    penalty = keyboardCheck(password)
    p -= penalty
    return p + len(password)

def checkPassword():
    password = input("Please enter a password: ")
    if valid_password(password):
        p = points(password)
        if p > 20:
            strength = "STRONG"
        elif p <= 0:
            strength = "WEAK"
        else:
            strength = "MEDIUM"
        print("Password strength: {} ({})".format(strength, p))
    else:
        print("Invalid password!")
    return

def generatePassword():
    password = ""
    p = 0
    while p <= 20:
        length = randint(8, 12)
        for i in range(length):
            password += choice(validchars)
        p = points(password)
    print("Generated password: "+password)
    print("Password strength: STRONG ({})".format(p))
    return

# custom exception
class InIdle(Exception):
    def __init__(self):
        super().__init__()

#ascii art
asciiart = """\
  ___                              _    ___                       _           
 | _ \__ _ _______ __ _____ _ _ __| |  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_| \__,_/__/__/\_/\_/\___/_| \__,_|  \___\___|_||_\___|_| \__,_|\__\___/_|  
                                
"""


#clear text output
try:
    from sys import modules
    if 'idlelib.run' in modules: raise InIdle
    from os import system
    def clear():
        system("cls")
        print(asciiart)
except (ImportError, InIdle):
    #failed import of system. security measure?
    clear = lambda : None

options = """\
What do you want to do?
 1) Check Password
 2) Generate Password
 3) Quit\
"""
leave = False
print(asciiart)
while not leave:
    print(options)
    option = input("#")
    if option == "1":
        clear()
        checkPassword()
    elif option == "2":
        clear()
        generatePassword()
    elif option == "3":
        print("Exiting")
        leave = True
    else:
        clear()
        print("Invalid choice. Please select again.\n")
