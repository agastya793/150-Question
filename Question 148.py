'''Create a program to demonstrate Abstraction using:

Abstract class

Abstract method

Child class implementation'''

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        return 10 * 5
class Circle(Shape):
    def area(self):
        return 3.14 * 7 * 7
r = Rectangle()
c = Circle()

print("Rectangle Area:", r.area())
print("Circle Area:", c.area())
