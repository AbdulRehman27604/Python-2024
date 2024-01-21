from math import pi
class Circle:
    def __init__(self,radius):
        self.Radius = radius

    def area(self):
        return pi * self.Radius**2

    def perimeter(self):
        2 * pi * self.Radius

from datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.__Name = name
        self.__Country = country
        self.__DOB = dob

    def GetAge(self):
        today = date.today()
        age = today.year - self.__DOB
        print(age)

    def GetName(self):
        return self.__Name

class Calculator:
    def __init__(self,num1,num2):
        self.__Num1 = num1
        self.__Num2 = num2

    def Plus(self):
        T = self.__Num1 + self.__Num2
        return T

    def minus(self):
        M = self.__Num1 - self.__Num2
        return M

    def multiply(self):
        x = self.__Num1 * self.__Num2
        return x

    def divide(self):
        y = self.__Num1 / self.__Num2
        return y

from math import pi
class Circle:
    def __init__(self,radius):
        self.__Radius = radius

    def Area_Of_Circle(self):
        A = pi * self.__Radius**2
        return A

    def perimeter(self):
        p = 2 * pi * self.__Radius
        return p

class triangle():
    def __init__(self,lenght,width,side1,side2,side3):
        self.__Lenght = lenght
        self.__Width = width
        self.__Side1 = side1
        self.__Side2 = side2
        self.__Side3 = side3

    def Area(self):
        A = self.__Width * 0.5 * self.__Lenght
        return A

    def primeterT(self):
        t = self.__Side1 + self.__Side2 + self.__Side3
        return t

class Square:
    def __init__(self,lenght,width):
        self.__Lenght = lenght
        self.__Width = width

    def areaS(self):
        A = self.__Width * self.__Lenght
        return A

    def perS(self):
        pp = 2(self.__Lenght * self.__Width)
        return pp

class Stack():
    def __init__(self):
        self.__TopOfStack = 0
        self.__List = [0,0,0,0,0,0,0,0,0,0]

    def push(self,val):
        if self.__TopOfStack < len(self.__List):
            self.__List[self.__TopOfStack] = val
            self.__TopOfStack += 1
            print(self.__List)
        else:
            print("Stack is full")

    def pop(self):
        if self.__TopOfStack >= 0:
            self.__TopOfStack -= 1
            self.__List[self.__TopOfStack] = 0
            print(self.__List)
        else:
            print("Stack is empty")

print("Hello tati")








