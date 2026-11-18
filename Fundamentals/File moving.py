import os

source = "C:\\Users\\ahmed\\Desktop\\text1.txt" 
destination = "C:\\Users\\ahmed\\Documents\\.Study\\.Python\\test1.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")

except FileNotFoundError:
    print(f"{source} was not found.")
