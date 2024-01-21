import doctest
from math import pi

class Circle:
    
    def __init__(self, radius):
        self.__radius = radius
        
    def calculate_area(self):
        area = round(pi * self.__radius ** 2,2)
        return area
    
    def perimeter(self):
        peri = f'{(2 * pi * self.__radius):.2f}'
        return peri

ob1 = Circle(5)
print(ob1.calculate_area())
print(ob1.perimeter())