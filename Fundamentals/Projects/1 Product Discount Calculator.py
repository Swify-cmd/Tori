import time

pname = input("Product name: ")
ptype = input("Product type: ")
pprice = float(input("Product price: "))

discount = pprice*0.1
discount1 = pprice*0.3
discount2 = pprice*0.2


time.sleep(0.6)
print("Product name: "+pname)
time.sleep(0.5)
print("Product type: "+ptype)
time.sleep(0.7)
print("Product price: "+str(pprice))


if pprice > 150:
   tprice = pprice - discount1

elif pprice < 150:
   tprice = pprice - discount2
else:
   tprice = pprice - discount

time.sleep(0.9)
print("Total price: "+str(tprice))
