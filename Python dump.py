

'''          inputs stuff
name = input("What's your name: ")

print("Nice to have you here, "+name)

age = int(input("How old are you: "))

print("You are "+str(age)+" years old!")

height = float(input("How tall are you: "))

print("Not tall enough, you are gay..")



         slice, index stuff
website = "https://roblox.com"

slice = slice(8,-4)

print(website[slice].capitalize())



         if statements stuff
age = int(input("How old are you?: "))
if age >= 18:
    print("You are an adult!")
else:
     print("You are not an adult!")
     int(input("How old are you?: "))


       while loops
name = ""

while len(name) == 0:
    name = input("What's your name?: ")
    
print("Hello "+name)'''



'''import time 

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
        print("Nice to meet you! " + name)'''


#import time

#pname = input("Product name: ")
#ptype = input("Product type: ")
#pprice = float(input("Product price: "))

#discount = pprice*0.1
#discount1 = pprice*0.3
#discount2 = pprice*0.2


#time.sleep(0.6)
#print("Product name: "+pname)
#time.sleep(0.5)
#print("Product type: "+ptype)
#time.sleep(0.7)
#print("Product price: "+str(pprice))


#if pprice > 150:
#    tprice = pprice - discount1

#elif pprice < 150:
 #   tprice = pprice - discount2
#else:
#    tprice = pprice - discount

#time.sleep(0.9)
#print("Total price: "+str(tprice))



'''rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()'''

'''while True:
    name = input("ur name is what: ")
    if name != "":
        break'''

'''jawal = "1-2-3-4-5-6-2-2"

for i in jawal:
    if i == "-":
        continue
    print(i, end="")'''

# idek what this is

'''food = ["shawarma","pizza","ms7b"]

food.remove(food[1])

for x in food:
    print(food, end="")
    break

def print_numbers():
    print(1)
    print(2)
    print(3)

print_numbers()'''

# a project from satr

'''number_holder = {
    'Amal': '1111111111',
    'Mohammed': '2222222222',
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}

name_or_number = input("Enter the name or the number: ")


if name_or_number.isdigit():
    for name, number in number_holder.items():
        if number == name_or_number:  
            print(f"The name belonging to the number {name_or_number} is {name}.")
            break  
    else:
        print(f"Sorry, the number {name_or_number} is not found in the phone book.")
else:
    if name_or_number in number_holder:
        print(f"The phone number is: {number_holder[name_or_number]}")
    else:
        print(f"Sorry, the name {name_or_number} is not found in the phone book.")'''

# failed birthday project

'''import datetime

name = input("Enter your name: ")
date.str = input("Enter your birthday: ")



def birthday(name, date):
    print(name+" is "+  +date)

birthday(name, date)'''

#     a little project
"""import time
pizza = ['pizza', 22]
shawarma = ['shawarma', 12]
burger = ['burger', 15]

menu = [pizza[0], shawarma[0], burger[0]]
menu_price = [pizza[1], shawarma [1], burger[1]]

menu_search = input(f"What would you like to order?: ({', '.join(menu)} ) ")

if menu_search == 'pizza':
    print("Great choice!")
    time.sleep(1)
    print(f"Your order would be: {pizza[1]}$")
    time.sleep(1)
    confirmation = input("Type: (Confirm) if you would like to confirm your order")
    backtomenu = input("Type: (Back) if you would like to go back to the menu")

    if confirmation == "Confirm":
        print("Your order has been confirmed!")
        print("Your order will be delivered in 30 minutes!")
    elif backtomenu == "Back":
        print("Going back to the menu...")
        time.sleep(1)
        menu_search = input(f"What would you like to order?: ({', '.join(menu)} ) ")
        if menu_search == 'shawarma':
            print("Great choice!")
            time.sleep(1)
            print(f"Your order would be: {shawarma[1]}$")
            time.sleep(1)
            confirmation = input("Type: (Confirm) if you would like to confirm your order")
            backtomenu = input("Type: (Back) if you would like to go back to the menu")
            if confirmation == "Confirm":
                print("Your order has been confirmed!")
                print("Your order will be delivered in 30 minutes!")
            elif backtomenu == "Back":
                print("Going back to the menu...")
                time.sleep(1)
                menu_search = input(f"What would you like to order?: ({', '.join(menu)}) ")
                if menu_search == 'burger':
                    print("Great choice!")
                    time.sleep(1)
                    print(f"Your order would be: {burger[1]}$")
                    time.sleep(1)
                    confirmation = input("Type: (Confirm) if you would like to confirm your order")
                    backtomenu = input("Type: (Back) if you would like to go back to the menu")
                    if confirmation == "Confirm":
                        print("Your order has been confirmed!")
                        print("Your order will be delivered in 30 minutes!")
                    elif backtomenu == "Back":
                        print("Going back to the menu...")
                        time.sleep(1)
                        menu_search = input(f"What would you like to order?: ({', '.join(menu)} ) ")"""
                        
#  upgraded version of the little project
    
# import time

# menu = {
#     'pizza': 22,
#     'shawarma': 12,
#     'burger': 15
# }

# while True:
#     menu_search = input(f"What would you like to order?: ").strip().lower()

#     if menu_search not in menu:
#         print(f"{menu_search} is an invalid order... try again")
#         continue

#     print(f"Your order will be {menu_search} ${menu[menu_search]} ")
#     confirmation = input("Type (Confirm) to confirm or (Back) to go back to the menu: ").strip().lower()

#     if confirmation == "confirm":
#         print("Your order will be delivered in 21 minutes!")
#         break

#     elif confirmation == "back":
#         print("Going back to the menu...")
#         continue
    
#     else:
#         print(f"{confirmation} is not a valid input")




# conditional expressions:

# user_role = "admin"
# access_level = "Full access" if user_role == "admin" else "Limited Access"

# print(access_level)


# loops

# name = input("What's your name?: ")

# while name == "":
#     print("Invalid.")
#     name = input("What's your name?: ")

# zesty = True
# print(f"Is the person zesty?: {zesty}")
# while zesty:
#     print("NO!")
#     zesty = False

# print(f"Is the person zesty?: {zesty}")

# food = ["spaghetti", "shawarma", "burger"]
# for i in food:
#     print("-".join(i))

# sets 

# p1blngs = {"phone", "car", "pen", "perfume", "glasses"}
# p2blngs = {"house", "car", "phone", "personal computer", "bed"}


# print("Person 2 doesn't have:", ", ".join(p1blngs.difference(p2blngs)))


# phone number book by name mini project

# phone_dict = {
#     "Amal":1111111111,
#     "Mohammed":2222222222,
#     "Khadijah":3333333333,
#     "Abdullah":4444444444,
#     "Rawan":5555555555,
#     "Faisal":6666666666,
#     "Layla":7777777777
# }

# search = ""

# while len(search) != 10 or not search.isdigit():
#     search = input("Enter the number/name: ")
    
#     if search in phone_dict:
#         print(phone_dict[search])
#         break
#     else:
#         print("The number/name is invalid.")
#         continue

# keyword arguments

# def info(fname, lname, age):
#     print(f"Hello {fname} {lname}")
#     print(f"You are {age} years old!")

# info(fname="Meow", age=19, lname="Cater")

# import random 

# x = random.randint(1,6)
# y = random.random()

# my_list = ['rock','paper','scissors']
# z = random.choice(my_list)

# cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

# random.shuffle(cards)
# print(cards)

# Exceptions
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: ")) # divide by zero to get the error
#     result = numerator / denominator
    
# except ZeroDivisionError:
#     print("You can't divide by zero baka!")
# except ValueError as e:
#     print(e)
#     print("Use numbers only please")
# except Exception:
#     print("Something went wrong.")
# else:
#     print(result)
# finally:
#     print("I always get executed :<")

# File detection

# import os

# path = "C:\\Users\\ahmed\\Desktop\\text.txt"
# path2 = "C:\\Users\\ahmed\\Desktop\\Shimiji"
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")

# try:
#     with open("C:\\Users\\ahmed\\Desktop\\text.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found.")


# text = "yooo\nthis is some text yall been waiting for\nhave a good day chat"
# text = "This text have been overridden\nidk if i wrote that right"
# with open('test1.txt', 'w') as file: #to write
#     file.write(text)

# text = "\nand also me i am being written!"
# with open('test1.txt', 'a') as file: #to append
#     file.write(text)

# import shutil 

# copyfile() = copies the contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modifiation time)

#                                                            #original file here                                    #copied file here
# shutil.copyfile("C:\\Users\\ahmed\\Documents\\.Study\\.Python\\test1.txt","C:\\Users\\ahmed\\Documents\\.Study\\.Python\\copy.txt") #src, dst

# shutil.copy("C:\\Users\\ahmed\\Documents\\.Study\\.Python\\test1.txt","C:\\Users\\ahmed\\Documents\\.Study\\.Python\\copy2.txt") #src, dst
# shutil.copy2("C:\\Users\\ahmed\\Documents\\.Study\\.Python\\test1.txt","C:\\Users\\ahmed\\Documents\\.Study\\.Python\\copy3.txt") #src, dst


# import os

# source = "C:\\Users\\ahmed\\Desktop\\text1.txt" 
# destination = "C:\\Users\\ahmed\\Documents\\.Study\\.Python\\test1.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there!")
#     else:
#         os.replace(source, destination)
#         print(f"{source} was moved")

# except FileNotFoundError:
#     print(f"{source} was not found.")


# import os
# import shutil

# path = "copy.txt"
# path2 = "emptyfolder"
# try:
#     #os.remove(path)
#     #os.rmdir(path2) #rmdir = remove directory
#     shutil.rmtree(path2) #dangerous, can delete a folder with its contents
# except FileNotFoundError:
#     print("This file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print("You cannot delete this folder using this function")
# else:
#     print(f"{path2} was deleted")


# import new_message # calling a module(a python file containing blocks of code such as functions)

# new_message.hello()
# new_message.bye()

# import new_message as msg # alias to a module
# from new_message import hello,bye # calling specific functions from a module instead of the whole module

# msg.hello()
# msg.bye()

# hello()
# bye()

# help("modules")

# OOP

# from car import Car

# car_1 = Car("Chevy", "Corvette", "2021", "Blue")

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_1.drive()
# car_1.stop()

# Inheritance

# class Animal:

#     alive = True

#     def eat(self):
#         print("This animal is eating...")

#     def sleep(self):
#         print("This animal is asleep zzz")
    
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running...")
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming...")
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying...")

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

# rabbit.run()
# fish.swim()
# hawk.fly()


# multilevel inheritance

# class Organism:

#     alive = True

# class Animal(Organism): # inherits Organism's attributes and methods

#     def eat(self):
#         print("This animal is eating")

# class Dog(Animal): # inherits Animal's attributes and methods
    
#     def bark(self):
#         print("This dog is barking")

# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()


# multiple inheritance = when a child class is derived from more than one parent

# class Prey:
#     def flee(self):
#         print("This animal flees")

# class Predator:
#     def hunt(self):
#         print("This animal hunts")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()
