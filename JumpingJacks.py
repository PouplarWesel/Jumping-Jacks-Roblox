from cgitb import reset


try:
    import pyautogui
    import pydirectinput
    import time
    import ahk
    from ahk import AHK
    import keyboard
    import sys
except:
    print("Read README.txt and follow the directions given")
    a = input()
    sys.exit()

try:
    fileR = open("setup.txt", "r")
    content = fileR.readlines()
    content1 = []
    for i in content:
        j = i.strip("\n")
        j.lower()
        content1.append(j)
    keys = content1
    key1 = keys[0]
    key2 = keys[2]
    key3 = keys[1]
    key4 = keys[3]
    key5 = keys[4]

except:
    print("Run setup.py and follow the directions given")
    a = input()
    sys.exit()

ahk = AHK()
nextProgram = False
exitProgram = False
jumptime = float(key5)

fileW = open("One-Nineteen.txt", "r")
content = fileW.readlines()
content1 = []
for i in content:
    j = i.strip("\n")
    content1.append(j)
OneNineteen = content1

fileW = open("Twenty-NinetyPart1.txt", "r")
content = fileW.readlines()
content1 = []
for i in content:
    j = i.strip("\n")
    content1.append(j)
TwentyNinetyPart1 = content1

fileW = open("Twenty-NinetyPart2.txt", "r")
content = fileW.readlines()
content1 = []
for i in content:
    j = i.strip("\n")
    content1.append(j)
TwentyNinetyPart2 = content1

def quit():
    global exitProgram
    exitProgram=True

def next():
    global nextProgram
    nextProgram=True
    joebiden = False

def reset():
    joebiden = True
    while joebiden == True:
        global number
        global kind
        repeat = 0
        while repeat == 0:
            try:
                while repeat == 0:
                    kind = int(input("\nType the one you would like to use:\n[1] - Jumping Jacks (ONE!, TWO!, THREE!) \n[2] - Grammer Jacks (One., Two., Three.)\n[3] - Hell Jacks(O,N,E,ONE!): "))
                    if kind == 1 or kind == 2 or kind == 3:
                        repeat = 1
            except:
                print("You typed a non-numerical number")
        repeat = 0
        while repeat == 0: 
            try:
                number = int(input("\nWhat number would you like to switch to?: "))
                if number < 20:
                    word = (OneNineteen[number])
                elif number >= 20 and number < 100:
                    num = str(number)
                    first = int(num[0])
                    second = int(num[1])
                    word = TwentyNinetyPart1[int(first)] + TwentyNinetyPart2[int(second)]
                if number != 0 and number < 100:
                    print("\n" +word + " is the new number")
                    print("\n\nWhen you are ready hit \"" +  key1 + "\" to start.\nTo edit the number press \"" + key3 + "\" and type in the next number into the pannel.\nWhen you are finished hit \"" + key2 + "\" when you are done.")  
                    joebiden = False
                    repeat = 1
            except:
                print("You typed a non-numerical number. Type in like \"1\" or \"24\".")

keyboard.add_hotkey(key2, lambda: quit())
keyboard.add_hotkey(key1, lambda: next())
keyboard.add_hotkey(key3, lambda: reset())

def write(a, b):
    ahk.key_press("/")
    ahk.key_press("Backspace")
    time.sleep(b)
    pyautogui.write(a)
    time.sleep(b)
    ahk.key_press("Enter")
    time.sleep(b)
    
def jump():
    ahk.key_press("Space")
    
def jumpingjacks(a):
    if kind == 1:
        word = a.upper()
        word = word + "!"
        write(word,0.25)
        jump()
    elif kind == 2:
        word = a + "."
        write(word, 0.25)
        jump()
    elif kind == 3:
        for x in range(len(a)):
            word = a[x]
            word = word.upper()
            write(word, jumptime)
            jump()
        word = a.upper()
        word = word + "!"
        write(word, jumptime)
        jump()

    
repeat = 0
while repeat == 0:
    try:
            kind = int(input("Type the one you would like to use:\n[1] - Jumping Jacks (ONE!, TWO!, THREE!) \n[2] - Grammer Jacks (One., Two., Three.)\n[3] - Hell Jacks(O,N,E,ONE!): "))
            if kind == 1 and key4 == "1":
                awd = input("Is Jumping Jacks (ONE!, TWO!, THREE!) correct (Y = yes, N = no): ")
                if awd == "Y":
                    repeat = 1
            if kind == 2 and key4 == "1":
                awd = input("Is Grammer Jacks (One., Two., Three.) correct (Y = yes, N = no): ")
                if awd == "Y":
                    repeat = 1
            if kind == 3 and key4 == "1":
                awd = input("Is Hell Jacks (O,N,E,ONE!) correct (Y = yes, N = no): ")
                if awd == "Y" and key4 != "0":
                    repeat = 1
            elif key4 == "0":
                if kind == 1 or kind == 2 or kind == 3:
                    repeat = 1

    except:
            print("You typed a non-numerical number")
            
repeat = 0

while repeat == 0:    
    try:
        number = int(input("\nWhat number should it start at: "))

        if number < 20:
            word = (OneNineteen[number])
        elif number >= 20 and number < 100:
            num = str(number)
            first = int(num[0])
            second = int(num[1])
            word = TwentyNinetyPart1[int(first)] + TwentyNinetyPart2[int(second)]
        if key4 == "1":
            if number != 0 and number <= 100:
                randomstuff = input("Is \"" + word + "\" the correct number (Type Y for yes, N for no): ")
                if randomstuff == "Y":
                    repeat = 1
                    print("\n\nWhen you are ready hit \"" +  key1 + "\" to start.\nTo edit the number press \"" + key3 + "\" and type in the next number into the pannel.\nWhen you are finished hit \"" + key2 + "\" when you are done.")
        elif key4 == "0" and number != 0 and number < 100:
            repeat = 1
            print ("The number chosen is \"" + word + "\"")
            print("\n\nWhen you are ready hit \"" +  key1 + "\" to start.\nTo edit the number press \"" + key3 + "\" and type in the next number into the pannel.\nWhen you are finished hit \"" + key2 + "\" when you are done.")
            
    except:
        print("You typed a non-numerical number. Type in like \"1\" or \"24\".")
        
while not exitProgram:
    if nextProgram == True:
        if number < 20:
            jumpingjacks(OneNineteen[number])
            number += 1
            nextProgram = False
        elif number >= 20 and number < 100:
            num = str(number)
            first = int(num[0])
            second = int(num[1])
            firstword = TwentyNinetyPart1[int(first)]
            secondword = TwentyNinetyPart2[int(second)]
            secondword = secondword.lower()
            word = firstword + secondword
            jumpingjacks(word)
            number += 1
            nextProgram = False
        else:
            print("Number not aviable")
            print("Press \"" + key2 + "\" on your keyboard to exit")
sys.exit()

