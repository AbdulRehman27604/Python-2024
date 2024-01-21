list = [1,2,3,4,5,6,7,8,9]
def shift():
    global list
    for i in range(1,len(list)):
        if i % 3 == 0:
            list[i-1] = 0
    print(list)

from random import randint
def digi3():
    inti = ""
    for i in range(3):
        num = randint(0,9)
        inti = inti + str(num)
    print(inti)

import random
def shuffle():
    word = ["a","e","i","o","u"]
    random.shuffle(word)
    print(''.join(word))

def 


