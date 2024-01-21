def lenS():
    string = input("PLease enter a string to get its lenght: ")
    print(len(string))


# Q2 Skip

def collide():
    sting = input("PLease enter a string : ")
    if len(sting) < 2:
        return print("Empty String")
    else:
        i = sting[0:2] + sting[-2:]
        return print(i)

def change():
    string = input("PLease enter a string: ")
    first = string[0]
    string1 = ""
    for i in range(len(string)):
        if i == 0:
            string1 = string1 + string[i]
        elif string[i] == first:
            string1 = string1 + "$"
        else:
            string1 = string1 + string[i]
    print(string1)

def shift(n1,n2):
    new1 = len(n1)
    new2 = len(n2)
    val1 = n1[0:2]
    val2 = n2[0:2]
    x = n1[2:new1]
    y = n2[2:new2]
    print(val2 + x +","+ val1 + y)

def word(string):
    if len(string) >= 3:
        if string[-3:] == "ing":
            lenght = len(string) - 3
            newstr = string[0:lenght]
            str1 = newstr + "ly"
            print(string)
    else:
        print(string)

def max1():
    new = []
    list = ["hello","mind","abdulRehman","asdwfdqec"]
    for i in range(len(list)):
        x = len(list[i])
        new.append(x)
    high = max(new)
    for y in range(len(new)):
        if new[y] == high:
            val = y
    print("longest string",list[y],"with lenght",len(list[y]))

def remove_char(str,n):
    first_part = str[0:n]
    last_part = str[n+1:]
    final_part = first_part + last_part
    print(final_part)

def exchange():
    str = input("PLease enter a string: ")
    print(str[len(str) - 1] + str[1:len(str) - 1] + str[0])

def oddstr():
    str = input("PLease Enter A String: ")
    newstr = ""
    for i in range(len(str)):
        if i % 2 == 0:
            newstr = newstr + str[i]
        else:
            continue
    print(newstr)

list = ["zebra","yellow","xylophone","anaconda"]
def bubbleSort():
    global list
    swap = False
    boundry = len(list) - 1
    while not swap:
        swap = True
        for i in range(boundry):
            x = list[i]
            y = list[i + 1]
            if x[0] > y[0]:
                temp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = temp
                swap = False
        boundry -= 1

def Html(tag,inner):
    print("<"+tag+">"+inner+"</"+tag+">")

def middle(mid,string):
    cal = int(len(mid) / 2)
    print(str(mid[:cal + 1]) + string + str(mid[cal:len(mid)]))

def copies():
    str = input("PLease Enter A Value: ")
    if len(str) < 2:
        return "not possible"
    print(str[-2:] * 4)

def initials():
    str = input("PLease Enter A Value: ")
    if len(str) < 3:
       return print(str)
    return print(str[0:3])

def four_manu():
    str1 = input("PLease Enter A Value: ")
    if len(str1) % 4 == 0:
        return print(''.join(reversed(str1)))

def convert():
    str1 = input("PLease Enter A Value: ")
    up = 0
    for i in range(4):
        if str1[i] >= "A" and str1[i] <= "Z":
            up = up + 1
    if up >= 2:
        new = str1.upper()
        print(new)
    else:
        print(str1)

def start_with():
    str = input("PLease Enter a Value: ")
    print(str.startswith("w3r"))

def Caesar_cipher():
    list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    word = input("Please Enter a word to cipher: ")
    total = ""
    for i in range(len(word)):
        x = word[i]
        for index in range(len(list)):
            if list[index] == x:
                newindex = index
        total = total + list[newindex + 2]
    print(total)

def decimal():
    calc = input("Please Enter A Value: ")
    for i in range(len(calc)):
        if calc[i] == ".":
            x = i
    first = calc[:x]
    y = len(calc) - x
    if y > 2:
        if int(calc[x+3]) >= 5:
            new = int(calc[x + 2]) + 1
            print(str(calc[:x]),new)
        else:
            print()

def padding():
    str1 = input("PLease Enter A Value: ")
    y = ""
    x = len(str1)
    for i in range(x):
        y = y + "0"
    print(y+str1)

def paddingStar():
    str1 = input("PLease Enter A Value: ")
    y = ""
    x = len(str1)
    for i in range(x):
        y = y + "*"
    print(str1 + y)

def percentage():
    val = input("Please enter a decimal value: ")
    x = val * 100
    print("X as a percentage is:",x,"%")

def align():
    val = input("Please enter a value: ")
    print("left allign:"+"  ")

def reverse(str1):
    return ''.join(reversed(str1))

def split(str):
    for i in range(str):
        











