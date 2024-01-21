list = []
def multiples():
    x = 1500
    while x != 2700:
        if x % 7 == 0 and x % 5 == 0:
            list.append(x)
        x = x + 1
    print(list)

def conversion():
    temp = input("PLease choose what to convert in: ")
    if temp == "c":
        far = int(input("Enter the celcius value: "))
        val = 5*(far - (32/9))
        print("celcius = ",val)

from random import randint
def guess():
    guss = False
    while guss != True:
        num = randint(0,9)
        value = int(input("PLease enter your guess number: "))
        if num == value:
            print("Well done")
            guss = True
        else:
            print("you failed, the guess number was: ",num)

def pattern():
    star = ""
    for i in range(5):
        for j in range(i):
            print('* ', end="")
        print('')
    newstar = ""
    for i in range(5,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

def reverse():
    val = ""
    word = input("PLease enter a word to reverse: ")
    for i in range(len(word)):
        val = val + word[-i]
    print(val)

def count():
    even = 0
    odd = 0
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    print("There are",even, "Even numbers.")
    print("There are", odd, "Odd numbers.")

def type1():
    list = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
    for i in range(len(list)):
        print("The type of",list[i],"is",type(list[i]))

def racist():
    for i in range(6):
        if i == 3 or i == 6:
            continue
        else:
            print(i, end='')

def fabonacci():
    x, y = 0, 1

    while y < 50:
        print(y)
        x, y = y, x + y
def fizzbuzz():
    for i in range(51):
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)

'''rows = 3
columns = 4
two_dimensional_array = [[0 for y in range(columns)] for x in range(rows)]
for row in two_dimensional_array:
    print(row)'''

def blank():
    line = input("PLease enter a line to print: ")
    while line != "":
        newline = line.lower()
        print(newline)
        line = input("PLease enter a line to print: ")

def diff(string):
    num = 0
    alpha = 0
    for i in range(len(string)):
        if string[i].lower() >= "a" and string[i].lower() <= "z":
            alpha += 1
        elif string[i] >= "0" and string[i] <= "9":
            num += 1
    print("Number of alphabets are",alpha)
    print("Number of digits are",num)
x = "Python 3.2"

def PassCheck():
    up = False
    low = False
    special = False
    Password = input("PLease Enter A Password: ")
    if len(Password) <= 6 and len(Password) >= 16:
        return print("wrong password")
    for i in range(len(Password)):
        if Password[i] >= "A" and Password[i] <= "Z":
            up = True
        elif Password[i] >= "a" and Password[i]<= "z":
            low = True
        elif Password == "&" or Password == "@" or Password == "#":
            special = True
    if up == True and low == True and special == True:
        return print("Correct Password")
    else:
        return print("wrong Password")

'''result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);'''

def dogYear():
    year = int(input("Please enter the dog age: "))
    if year <= 2:
        print("dog age is 10.5")
    else:
        newage = year - 2
        n = newage * 4
        total = 10.5 + n
        print("dog age is",total)
def vowel():
    list = ["a","e","i","o","u"]
    letter = input("Please enter a letter: ")
    for i in list:
        if i == letter:
            return print("The letter is a vowel")
    return print("The letter is a consonant")

def month():
    list31 = ["january","march","may","july","august","october","december"]
    list30 = ["april","june","september","november"]
    m = input("PLease enter a month: ")
    for i in list31:
        if m == i:
            return print("This month has 31 days")
    for x in list30:
        if m == x:
            return print("This month has 30 days")
    return print("this month has 28/29 days")

def sum(n1, n2):
    total = n1 + n2
    if total >= 15 and total <= 20:
        return print("20")
    else:
        return print(total)

def sting():
    line = input("Please enter a value: ")
    if len(line) < 1:
        return print("invalid string")
    for i in range(len(line)):
        if line[i] in "0123456789":
            ok = True
        else:
            ok = False
            break
    if ok == True:
        return print("line is an integer")
    else:
        return print("line is a string")

def Tri():
    x = int(input("PLease enter the lenght of side: "))
    y = int(input("PLease enter the lenght of side: "))
    z = int(input("PLease enter the lenght of side: "))
    if x == y == z:
        return print("The triangle is an equilateral triangle")
    if x == y or x == z or y == z:
        return print("it is an isosceles triangle")
    else:
        return print("it is a scalene triangle")

def ChangeDate():
    year = int(input("Please Enter The Year: "))
    month = int(input("PLease Enter The Month: "))
    day = int(input("Please Enter The Day: "))
    day = day + 1
    if day > 31:
        day = 1
        month = month + 1
        if month > 12:
            month = 1
            year = year + 1
    print(str(day),"-",str(month),"-",str(year))

def sum():
    ine = int(input("PLease Enter a number: "))
    count = 0
    total = 0
    while ine != 0:
        count += 1
        total = total + ine
        ine = int(input("PLease Enter a number: "))
    print(total)
    avg = total/count
    print(avg)

def table6():
    for i in range(11):
        val = i * 6
        print("6","x",str(i),"=",str(val))

def nest():
    for i in range(10):
        print(str(i) * i)


vowel()







