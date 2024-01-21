import doctest

# we designed this function in a past lecture:


def get_number() -> int:
    """ repeatedly prompts user for a number >=0
    and returns it as an int
    """
    prompt = 'enter a whole number >=0: '
    num_as_str = input(prompt)
    while not num_as_str.isdigit():
        num_as_str = input(prompt)

    return int(num_as_str)


'''
Q1. Design a function called print list that takes a list of numbers and
prints all the numbers in the list separated by a comma and space and
enclosed in square brackets.

Use a loop to do this, don't just use print(list_of_numbers)
'''
list = [2,5,3,8,9,3,1,0,4]
def print_list(input_list):
    """
    >>> print_list([2,5,3,8,9,3,1,0,4])
    [2,5,3,8,9,3,1,0,4]
    >>> print__list([0])
    [0]
    """
    string = '['
    for i in range(len(input_list)):
        if i == len(input_list) - 1:
            string += str(input_list[i])
        else:
            string += str(input_list[i])
            string += ' ,'
    string += ']'
    print(string)


'''
Q2. Design a function that will repeatedly prompt the user to enter
positive whole numbers and 0 to stop.
The function should create and return a list that holds all of the positive
integers entered by the user.
The function should ignore invalid input (ie. floats, words, negative values)
'''
def insert_list():
    """
    return a list of whole numbers populated with the user input
    """
    new_list = []
    value = get_number()
    while value != 0 and value > 0:
        new_list.append(value)
        value = get_number()
    return new_list
print(insert_list())
    
    

'''
Q3. Design a function that takes a list of numbers and returns the sum
of the numbers in the list.
Do not use the builtin sum function.
'''
def sum_of_list(sting):
    """
    >>> sum_of_list([0])
    0
    >>> sum_of_list([2,5,3,8,9,3,1,0,4])
    35
    """
    total = 0
    for i in range(len(sting)):
        total += sting[i]
    return total

        

'''
Q4. Design a function that takes a list of integers and returns a new list
with the numbers from the given list with all odd numbers removed.

Example: if called as: keep_even([3, 61, 4, 3, 2, 5])
it should return the list [4, 2]
'''
def is_even(array):
    """
    >>> is_even([3, 61, 4, 3, 2, 5])
    [4, 2]
    >>> is_even([0])
    [0]
    >>> is_even([2,4,76,23,12,45,34,88,98])
    [2, 4, 76, 12, 34, 88, 98]
    """
    new_list = []
    for i in array:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
    

'''
Q5. Design a function that takes a list of integers and
an additional integer value.
The function should return the index of the first occurrence of
the additional integer within the list.
If the value is not found in the list, the function should
return -1.
Do not use the builtin list index function
'''
def search_list(list,n: int):
    """
    >>> search_list([13,76,23,98,23,89],23)
    3
    """
    for i in range(len(list)):
        if list[i] == n:
            return i + 1

            