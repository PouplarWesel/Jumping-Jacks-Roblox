from ast import Num


repeat = 0
try:
    import pyautogui
    import pydirectinput
    import time
    import ahk
    from ahk import AHK
    import keyboard
    import sys
    
except:
    print("Read README.txt and follow the directions")
    repeat = 1
filew = open("setup.txt" , "w")
while repeat == 0:
    print("What would you like to use as the single key to start the next number. (Press the key on your keyboard)")
    a = keyboard.read_key()
    b = input("\nIs \"" + a + "\" going to be the key you use when you would like to start the next jumping jack. (This means that when every you would like to do a jumping jack you have to hit this button to start the next one) \nType Y for yes, N for no: ")
    if b == "Y":
        a = a + "\n"
        repeat = 1
        filew.write(a)
    elif len(b) == 2:
        check = b[1]
        if check == "Y":
            a = a + "\n"
            repeat = 1
            filew.write(a)
    else:
        time.sleep(2)
        print("\n")
repeat = 0
time.sleep(2)
while repeat == 0:
    print("\n\nWhat would you like to use as the single key edit the number. (Press the key on your keyboard)")
    a = keyboard.read_key()
    b = input("\nIs \"" + a + "\" going to be the key you use when you would like to edit number. (This means when you have to change the number, hit the button and open the pannel and type in the new number.) \nType Y for yes, N for no: ")
    if b == "Y":
        a = a + "\n"
        repeat = 1
        filew.write(a)
    elif len(b) == 2:
        check = b[1]
        if check == "Y":
            a = a + "\n"
            repeat = 1
            filew.write(a)
    else:
        time.sleep(2)
        print("\n")

repeat = 0
time.sleep(2)
while repeat == 0:
    print("\n\nWhat would you like to use as the single key to exit or stop the program: ")
    a = keyboard.read_key()
    b = input("\nIs \"" + a + "\" going to be the key you use when you would exit or stop the program. (This means when your number has been reached, press this button and it would quit the program for you.) \nType Y for yes, N for no: ")
    if b == "Y":
        a = a + "\n"
        repeat = 1
        filew.write(a)
    elif len(b) == 2:
        check = b[1]
        if check == "Y":
            a = a + "\n"
            repeat = 1
            filew.write(a)
    else:
        time.sleep(2)
        print("\n")
repeat = 0
while repeat == 0:
    a = input("\n\nWould you like to remove the questions asking to double check? (Like ,\"Are you sure. Y = Yes, N = No\"): ")
    if a == "Y":
        a = "0" "\n"
        repeat = 1
        filew.write(a)
    elif a == "N":
        a = "1" + "\n"
        repeat = 1
        filew.write(a)
    else:
        time.sleep(0.5)
        print("\n")
        
repeat = 0
while repeat == 0:
    a = input("\n\nWould you like hell jacks to be at the speed of roblox chat or as fast as it can be? (1 = Fast, 2 = Slow): ")
    if a == "1":
        a = "0.2" "\n"
        repeat = 1
        filew.write(a)
        filew.close()
    elif a == "2":
        a = "0.5" + "\n"
        repeat = 1
        filew.write(a)
        filew.close()
    else:
        time.sleep(0.5)
        print("\n")
print("You can close this now")
a = input()

        
