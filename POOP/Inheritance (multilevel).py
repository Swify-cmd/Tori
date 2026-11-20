# multilevel inheritance

class Organism:

    alive = True

class Animal(Organism): # inherits Organism's attributes and methods

    def eat(self):
        print("This animal is eating")

class Dog(Animal): # inherits Animal's attributes and methods
    
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
