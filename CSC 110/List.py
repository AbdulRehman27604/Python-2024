list1 = [2,5,3,9,10,4,5,1,6,1]
uniArray = ['abc', 'xyz', 'aba', '1221','22']
buniArray = ['akc', 'xy', 'abd', '1221','2','@km']
seti = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l1 = []
l2 = []

def sum():
    global list1
    total = 0
    for i in range(len(list1)):
        total = total + list1[i]
    print(total)

def multiply():
    global list1
    total = 1
    for i in range(len(list1)):
        total = total * list1[i]
    print(total)

def highest():
    x = max(list1)
    print(x)

def lowest():
    x = min(list1)
    print(x)

def unique():
    global uniArray
    count = 0
    for i in range(len(uniArray)):
        x = uniArray[i]
        if len(x) >= 2:
            if x[0] == x[len(x)-1]:
                count += 1
    print(count)

def last(n): return n[-1]
def sorting(tuple):
    print(sorted(tuple,key=last))

def dubi():
    for i in list1:
        if i not in l1:
            l1.append(i)
            l2.append(i)
    print(l2)

def mty():
    global list1
    if len(list1) == 0:
        print("list is empty")
    else:
        print("List is not empty")

def clone():
    global list1
    for i in list1:
        l1.append(i)
    print(l1)

def word(n):
    global uniArray
    for i in uniArray:
        if len(i) > n:
            l1.append(i)
    print(l1)

def comman():
    global uniArray, buniArray
    for i in uniArray:
        if i in buniArray:
            return True
    return False

def specified():
    global buniArray
    for i in range(len(buniArray)):
        if i in (0,4, 5):
            continue
        else:
            l1.append(buniArray[i])
    print(l1)

def remove_even():
    global list1
    for i in range(len(list1)):
        if i % 2 == 0:
            continue
        else:
            print(list1[i],end=',')

from random import shuffle
def shufflee():
    global uniArray
    shuffle(uniArray)
    print(uniArray)

def prime(n):
    ok = False
    for i in n:
        if i % i == 0 and i % 1 == 0:
            ok = True
        else:
            return False
    return True

from itertools import permutations
def perm():
    print(list(permutations([1,2,3])))

list11 = [1, 3, 5, 7, 9]
list22=[1, 2, 4, 6, 7, 8]
def diff():
    list10 = []
    for i in list11:
        if i not in list22:
            list10.append(i)
    for x in list22:
        if x not in list11:
            list10.append(x)
    print(list10)

def read():
    global list1
    for i in range(len(list1)):
        print(i,list1[i])

def join():
    global list1
    join1 = ""
    for i in range(len(list1)):
        join1 = join1 + str(list1[i])
    print(join1)

def merge():
    global list1 ,uniArray
    for i in range(len(list1)):
        uniArray.append(list1[i])
    print(uniArray)

from random import choice
def choice1():
    global list1
    print(choice(list1))

def second_large():
    new_list = []
    new_list = sorted(list1)
    print(new_list[len(new_list)-2])

def second_small():
    new_list = []
    new_list = sorted(list1)
    print(new_list[0])

def unigue():
    my_list = [10, 20, 30, 40, 20, 50, 60, 40]
    x = []
    for i in my_list:
        if i not in x:
            x.append(i)

import collections
def frequency():
    my_list = [10, 10, 20, 20, 30, 40, 60, 20, 50, 60, 40]
    x = collections.Counter(my_list)
    print(x)


def conside(a,b):
    global list1
    for i in range(len(list1)):
        if list1[i] == a:
            if list1[i+1] == b:
                return True
            else:
                return False

def concatint():
    total = ""
    list = [11,33,50]
    for i in list:
        total = total + str(i)
    print(total)

def odd_items():
    global list1
    for i in range(len(list1)):
        if i % 2 == 0:
            continue
        else:
            print(list1[i])

def sep():
    colors = [['Red'], ['Green'], ['Black']]
    for i in colors:
        print(i)
def diffn():
    l1 = ["red", "orange", "green", "blue", "white"]
    l2 = ["black", "yellow", "green", "blue"]
    for i in l1:
        if i not in l2:
            print([i],end='')
    print(" ")
    for x in l2:
        if x not in l1:
            print([x], end='')

def list_of_list():
    high = 0
    total = 0
    num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    for i in num:
        for x in i:
            total = total + x
        if total > high:
            high = total
            index = i
    print(num[index])
list_of_list()








