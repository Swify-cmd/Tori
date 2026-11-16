# Break and Continue
while True:
    name = input("ur name is what: ")
    if name != "":
        break

jawal = "1-2-3-4-5-6-2-2"

for i in jawal:
    if i == "-":
        continue
    print(i, end="")
