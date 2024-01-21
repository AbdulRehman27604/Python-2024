import doctest

'''
Q1.  Complete this function according to the documentation
'''
def find(lon: list[int], n: int) -> int:
    """ returns first index of n in lon, -1 if not found
    >>> find([], 2)
    -1
    >>> find([3, 6, 9, -1], 3)
    0
    >>> find([2, 3, 6, -12, 6], 6)
    2
    >>> find([3, 61, 9, -1], -1)
    3
    >>> find([3, 61, 9, -1], -18)
    -1
    """
    count = 0
    value = lon[count]
    while count < len(lon) and  n != value:
        value = lon[count]
        count += 1
    if count > len(lon):
        count = -1
    return count

'''
Q1. Design a function that will take a list of integers and
changes the first element in the given list to its negated value.
ie. if the first value is 8, change it to -8,
if the first value is -2 change it to 2.
'''
def change_first(list):
    """
    >>> change_first([23,45])
    [-23,45]
    >>> change_first([-56,90])
    [56,90]
    """
    if len(list) > 0:
        list[0] = -list[0]
    print(list)

        

'''
Q2. Design a function that will take a list of integers and
adds one to every element in the given list.
'''
def add_1(list):
    """
    >>> add_1([24,45])
    [25, 46]
    """
    if list != []:
        for i in range(len(list)):
            list[i] += 1
    print(list)

'''
Q3a. Design a function that will take a list of integers and change
every value in that list to its absolute value
DO not use the built in abs function.

Q3b. Design a second version of this function that does use the built-in abs function
'''
def absolute_list_1(list):
    """
    >>> absolute_list_1([])
    []
    >>> absolute_list([-23,45,-54])
    [23, 45, 54]
    """
    if list != []:
        for i in range(len(list)):
            list[i] = -list[i]
    print(list)
    
def absolute_list_2(list):
    """
    >>> absolute_list([])
    []
    >>> absolute_list([-23,45,-54])
    [23, 45, 54]

    """
    if list != []:
        for i in range(len(list)):
            list[i] = abs(list[i])
    print(list)

'''
Q4. Design a function that takes a list of integers and an
additional integer.  The function should determine whether the
additional number is contained in the list.
Do not use the builtin in operator.
'''
def search_list(list, number: int):
    """
    >>> search_list([],10)
    False
    >>> search_list([2,36,7,34],7)
    True
    >>> search_list([2,36,7,34],10)
    False
    """
    found = False
    for index in range(len(list)):
        if list[index] == number:
            found = True
    print(found)


'''
Q5. Design a function that takes a list of integers and an additional integer as second argument.
The function subtracts the integer from every value in the list.
If the subtraction results in a value below 0,
the element at that position should be set to 0.
'''
def change_number(list,num:int):
    """
    >>> change_number([5,2,45,90],5)
    [0, 0, 40, 85]
    >>> change_number([-33,-10,67,9],7)
    [0, 0, 60, 2]
    >>> change_number([56,21,69,89],4)
    [52, 17, 65, 85]
    """
    for index in range(len(list)):
        list[index] = list[index] - num
        if list[index] < 0:
            list[index] = 0
    print(list)
