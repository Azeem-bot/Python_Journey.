import math

class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def showArea(self):
        print("The area of the", self.name, "is", self.area, "units")


class Circle(Shape):
    def __init__(self, radius):
        self.area = 0
        self.name = "Circle"
        self.radius = radius

    def calcArea(self):
        self.area = math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.area = 0
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth

    def calcArea(self):
        self.area = self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.area = 0
        self.name = "Triangle"
        self.base = base
        self.height = height

    def calcArea(self):
        self.area = self.base * self.height / 2

r = float(input("Enter radius of circle: "))
c1 = Circle(r)
c1.calcArea()
c1.showArea()
l, b = map(float, input("Enter length and breadth of rectangle (separated by space): ").split())
r1 = Rectangle(l, b)
r1.calcArea()
r1.showArea()
b, h = map(float, input("Enter base and height of rectangle (separated by space): ").split())
t1 = Triangle(b, h)
t1.calcArea()
t1.showArea()