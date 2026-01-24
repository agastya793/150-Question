''' Create a program to demonstrate Inheritance where:

A parent class contains common features

A child class inherits and uses them'''

class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()    # Inherited method
d.bark()   # Own method
