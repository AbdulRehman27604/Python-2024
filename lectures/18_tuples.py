import doctest

'''
Q1. Design a function that takes a list of tuples and prints
the first element of every tuple.
'''
def print_first(line: list[tuple]) -> None:
    """
    >>> print_first([])
    
    >>> print_first([(1,4),(54,3),(5,90))])
    1 54 5
    """
    for cur_tuple in line:
        if len(cur_tuple) > 0:
            print(cur_tuple[0], end='')


'''
Q2. Design a function that takes a list of tuples where each tuple contains
the name and age of a person.  The function should print the information on
for each person represented in the list.
'''
name = 0
age = 1
def print_each(array: list[tuple]) -> None:
    """
    >>> print_each([])
    >>> print_each([('Adam',22),('Rehman',19)])
    Adam 22
    Rehman 19
    """
    for cur_tuple in array:
        if len(array) > 0:
            print(cur_tuple[name],cur_tuple[age])

'''
Q3. Design a function that takes a list of tuples and an additional tuple as
arguments. Each tuple contains the name and age of a person.
The function should return a list of only those tuples in the list who are
younger than the age of the person represented in the additional argument.
If they are the same age, tie should be broken by
lexicographical order of names (Python's string ordering).
'''
def compare_tuple(tuple_1: list[tuple], tuple_2: list[tuple]) -> list:
    """
    >>> compare_tuple([],('mina',50))
    >>> lop = [('Adam',22),('jose',45),('Adel',32),('Geogria',32)]
    
    >>> compare_tuple(lop,('celina',50))
    """
    list_1 = []
    compare = tuple_2[age]
    if len(tuple_1) > 0:
        for cur_tuple in tuple_1:
            if cur_tuple[age] < compare:
                list_1.append(cur_tuple)
    return list_1


'''
Q4. Design a function that takes a list of person tuples in increasing age
order (if age is equal, by name lexicographically)
and an addtional argument that is also a person tuple.
The function should create and return a new list with all the persons in the
orginal list + the additional argument.
The new list should be increasing age order too.
If there are 2 people of the same age, order by name lexicographically.
'''

def form_ordered_list(list_1: list[tuple], list_2: list[tuple]) -> list:
    if list_1 != []:
        