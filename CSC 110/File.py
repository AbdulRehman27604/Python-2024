def ReadFile():
    file = open("file1.txt","r")
    x = file.readline()
    while x != "":
        print(x , end='')
        x = file.readline()

def fileline(n):
    file = open("file1.txt","r")
    for i in range(n):
        print(file.readline(),end='')

def write():
    file = open("file1.txt", "a")
    str1 = input("PLease enter a value: ")
    file.write(str1)
    file = open("file1.txt", "r")
    x = file.readline()
    while x != "":
        print(x, end='')
        x = file.readline()

def square():
    for i in range(100):
        n = i ** 2
        print(n)
square()