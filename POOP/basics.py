# insert in car.py
class Car:
    
   wheels = 4 #class variable

    def __init__(self,make,model,year,color):
        self.make = make #instance variable 
        self.model = model #instance variable 
        self.year = year #instance variable 
        self.color = color #instance variable 


    def drive(self):
        print("This car is driving...")

    def stop(self):
        print("This car has stopped")

  # insert in any other file.py
from car import Car

car_1 = Car("Chevy", "Corvette", "2021", "Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_1.wheels)
print(Car.wheels)

car_1.drive()
car_1.stop()
