# Time Module and Conditional Statements

import time 

name = input("What's your name?: ")

if name == "Ahmed":
    print("?!")
    time.sleep(1)
    print("OMG I LOVE YOUR NAME")
    time.sleep(0.5)
    print("CAN WE BE FRIENDS?")
    time.sleep(0.3)
    answer = input("Yes! | No!: ").lower()  # Convert input to lowercase
    if answer == "Yes!" or answer == "yes" or answer == "Yes" or answer == "yes!" or answer == "YES!" or answer == "YES":
        print("YAY!")
    elif answer == "No!" or answer == "no" or answer == "No" or answer == "no!" or answer == "NO!" or answer == "NO":
        print("You're done lil bro...")

elif name == "":
    print("...")
    time.sleep(1)
    print("Bro? what's your name??")
    time.sleep(1)
    name = input("What's your name?: ")
    if name == "Ahmed":
        print("?!")
        time.sleep(1)
        print("OMG I LOVE YOUR NAME")
        time.sleep(0.5)
        print("CAN WE BE FRIENDS?")
        time.sleep(0.3)
        answer = input("Yes! | No!: ").lower()  # Convert input to lowercase
        if answer == "Yes!" or answer == "yes" or answer == "Yes" or answer == "yes!" or answer == "YES!" or answer == "YES":
            print("YAY!")
        elif answer == "No!" or answer == "no" or answer == "No" or answer == "no!" or answer == "NO!" or answer == "NO":
            print("You're done lil bro...")
    else:
        print("Nice to meet you! " + name)
