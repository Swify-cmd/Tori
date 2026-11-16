# loops

name = input("What's your name?: ")

while name == "":
    print("Invalid.")
    name = input("What's your name?: ")

zesty = True
print(f"Is the person zesty?: {zesty}")
while zesty:
    print("NO!")
    zesty = False

print(f"Is the person zesty?: {zesty}")
