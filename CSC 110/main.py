'''import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)

import datetime
print("current time")
print(datetime.date)'''

from math import pi
def area():
    radius = float(input("please enter the radius of circle: "))
    Area = float(pi * radius * radius)
    print("The area of circle with radius " + str(radius) + " is " + str(Area))

def ReverseName():
    first = input("please enter the first name: ")
    last = input("please enter the last name: ")
    print("Full name: " + (last + " " + first))

'''list = []
value = input("Enter some comma seperated numbers: ")
list = value.split(",")
tuple = tuple(list)
print(list)
print(tuple)'''

def extension():
    file = input("PLease enter a file name: ")
    for i in range(len(file)):
        if file[i] == ".":
            found = i
    ex = file[found + 1:len(file)]
    print(ex)

'''color_list = ["Red","Green","White" ,"Black"]
print("First color is "+ color_list[0]+ " and Last color is " + color_list[len(color_list) - 1])

exam_st_date = (11, 12, 2014)
print("the exam will be held at %i / %i / %i"%exam_st_date)'''

'''def operation():
    n1 = (input("please enter a value: "))
    n2 = str(n1 + n1)
    n3 = str(n1+n1+n1)
    val = int(n1) + int(n2) + int(n3)
    print(val)

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))'''


'''from datetime import date
initial = date(2014,7,2)
final = date(2014,7,11)
delta = final - initial
print(delta.days)'''

from math import pi
def volume():
    radius = float(input("please enter the redius to calculate volume of sphere: "))
    volume1 = float(4/3 * pi * radius*radius*radius)
    print(volume1)

def diffrence():
    value = int(input("please enter a value: "))
    new = value - 17
    if new > 17:
        return print(2 * new)
    else:
        return print(new)

def sum():
    n1 = int(input("PLease enter value 1: "))
    n2 = int(input("PLease enter value 2: "))
    n3 = int(input("PLease enter value 3: "))
    total = n1 + n2 + n3
    if n1 == n2 == n3:
        return print(total * 3)
    else:
        return print(total)

def change():
    value = input("please enter a string to change: ")
    if value[0:2] == "Is":
        return print(value)
    else:
        return print("Is" + value)

def copies(num, word):
    text = ""
    for i in range(num):
        text = text + " " + " "+ word
    print(text)

def EvenODD():
    value = int(input("please enter a value: "))
    if value%2 == 0:
        return print("The given value is Even")
    else:
        return print("The value is Odd")

list = [1,3,4,23,54,4,78,12,4,4,4,90,4]
def count4():
    count = 0
    global list
    for i in range(len(list)):
        if list[i] == 4:
            count = count + 1
    return print(count)

def fun(n , word):
    if len(word) < 2:
        for i in range(n):
            print(word)
    else:
        for x in range(n):
            print(word[0:2])

def vowel(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("The passed letter is a vowel")
    else:
        print("It is not a vowel")

def check(n):
    list = [1,5,8,3]
    if n in list:
        return print(True)
    else:
        return print(False)

histrogram = [3,5,9,10]

def histro():
    global histrogram
    output = ""
    for i in range(len(histrogram)):
        val = histrogram[i]
        for x in range(val):
            output += "*"
        print(output)


def concat():
    total = ""
    list = ["do","re","m","on"]
    for i in range(len(list)):
        item = list[i]
        total = total + item
    print(total)

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,958,743, 527]
def search():
    global numbers
    for i in range(len(numbers)):
        if numbers[i] == 237:
            return
        if numbers[i]%2 == 0:
            print(numbers[i])

def Triangle():
    height = float(input("please enter the height: "))
    base = float(input("please enter the base: "))
    area = 0.5 * height * base
    print("Area = " + area)

def sum(n1,n2,n3):
    sum = 0
    if n1 == n2 or n1 == n3 or n2 == n3:
        print(sum)
    else:
        sum = n1 + n2 + n3
        print(sum)

def stuck(x,y):
    z = x + y
    if z >= 15 and z <= 20:
        return print(20)

def bool(x,y):
    sum = x + y
    diff = x - y
    if sum == 5 or diff ==  5 or x == y:
        return print("True")

def calculate():
    x = int(input("please enter a value: "))
    y = int(input("please enter a value: "))
    z = x + y
    total = z * z
    print(total)

def interest():
    year = 7
    amt = 10000
    rate = 3.5
    int = (year * amt * rate) / 100
    print(int)

def sumN():
    n = int(input("Please enter a value: "))
    son = int((n*(2+(n-1)))/2)
    print(son)

def sumdigi():
    sum = 0
    val = input("PLease enter a number: ")
    for i in range(len(val)):
        sum = sum + int(val[i])
    print(sum)







