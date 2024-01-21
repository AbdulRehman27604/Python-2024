import doctest


# represent a person's information as (name, age)
# where name!='' and age>=0
Person = tuple[str, int]
NAME = 0
AGE = 1

'''
Here is where we left off last lecture...
I have added documentation and tests.
We will start by completing the insert function.
'''


def print_people(lo_people: list[Person]) -> None:
    """ prints information for each Person in lo_people
    >>> print_people([])
    >>> print_people([('Adam', 22), ('Jose', 45), ('Lizzo', 32)])
    Adam: 22
    Jose: 45
    Lizzo: 32
    """
    for p in lo_people:
        print(p[NAME], ': ', p[AGE], sep='')


def is_before(p1: Person, p2: Person) -> bool:
    """ determines whether p1 is before p2 in age, or if age is equal
    if name of p1 is before name of p2. returns True if it is, False otherwise.
    >>> is_before(('Adam', 30), ('Lizzo', 32))
    True
    >>> is_before(('Zac', 30), ('Lizzo', 32))
    True
    >>> is_before(('Adam', 32), ('Lizzo', 32))
    True
    >>> is_before(('Zac', 32), ('Lizzo', 32))
    False
    >>> is_before(('Betty', 40), ('Lizzo', 32))
    False
    >>> is_before(('Zac', 40), ('Lizzo', 32))
    False
    >>> is_before(('Lizzo', 40), ('Lizzo', 40))
    False
    """
    return p1[AGE] < p2[AGE] or (p1[AGE] == p2[AGE] and p1[NAME] < p2[NAME])


age = 1
def insert_person(lo_people: list[Person], to_insert: Person) -> list[Person]:
    """ creates and returns a list with to_insert inserted into lo_people 
    in order of increasing age. If ages are equal, order by name alphabetically.
    Precondition: lo_people is in increasing age order, then alphabetical by name
    >>> people = [('Adam', 22), ('Jose', 25), ('Lizzo', 32)]

    >>> insert([], ('Tian', 19))
    [('Tian', 19)]

    >>> insert_person(people, ('Jill', 19))
    [('Jill', 19), ('Adam', 22), ('Jose', 25), ('Lizzo', 32)]

    >>> insert_person(people, ('Jill', 25))
    [('Adam', 22), ('Jill', 25), ('Jose', 25), ('Lizzo', 32)]

    >>> insert_person(people, ('Jill', 33))
    [('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)]
    """
    # TODO: complete
    result_list = []
    new_elements = len(lo_people)   
    index = 0
    while index < new_elements and is_before(lo_people[index],to_insert):
        result_list.append(lo_people[index])
        index += 1
    result_list.append(to_insert)

    for cur_person in lo_people[index:]:
        result_list.append(cur_tuple)
    return result_list


'''
Q1. Design a function that takes a list of Person tuples in no order.
The function should create and return a new list in increasing age order.
'''


def sort_people(lo_people: list[Person]) -> list[Person]:
    """ creates a new list with Persons in lo_people in increasing age order,
    and alphabetical by name if ages are equal

    >>> sort_people([])
    []

    >>> sort_people([('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)])
    [('Adam', 22), ('Jose', 25), ('Lizzo', 32), ('Jill', 33)]

    >>> sort_people([('Adam', 22), ('Jose', 12), ('Lizzo', 32), ('Jill', 32)])
    [('Jose', 12), ('Adam', 22), ('Jill', 32), ('Lizzo', 32)]

    >>> sort_people([('Adam', 22), ('Jose', 18), ('Betty', 18), ('Jill', 12)])
    [('Jill', 12), ('Betty', 18), ('Jose', 18), ('Adam', 22)]
    """
    # TODO: complete


'''
Q2. Design a function that takes a list of person tuples in no particular order.
The function should print the information for each person in order increasing age.
'''
'''def sort_list(array :list[tuple]) -> tuple:
    boundry = len(array) - 1
    swap = False
    while not swap:
        swap = True
        for count in range(boundry):
            cur_tuple_1 = array[count]
            cur_tuple_2 = array[count+1]
            if cur_tuple_1[1] > cur_tuple_2[1]:
                temp = cur_tuple_1
                cur_tuple_1[1] = cur_tuple_2[1]
                cur_tuple_2[1] = temp
       elif cur_tuple_1[1] == cur_tuple_2[1]:
                if array[count][0] > array[count + 1][0]:
                    temp = array[count][0]
                    array[count][0] = array[count + 1][0]
                    array[count + 1][0] = temp  
            swap = True
        boundry -= 1
    print(array)
sort_list([('Jill', 50), ('Betty', 1), ('Jose', 18), ('Adam', 22)])'''

def print_sorted_list(lo_people: list[Person]) -> None:
    """ prints lo_people in sorted order of age then by name
    >>> print_sorted_list([])
    >>> print_sorted_list([('Adam', 22), ('Jose', 12), ('Lizzo', 32), ('Jill', 32)])
    Jose: 12
    Adam: 22
    Jill: 32
    Lizzo: 32
    """
    # TODO: complete


'''
Q3. Design a function that will take two lists of integers and
creates and returns a list of tuples that are pairs across the lists.
ie. if the lists are [2, 3, 4] and [5, 6, 7]
the function should return [(2, 5), (3, 6), (4, 7)]

The function should assume the lists are the same length
'''
def across_list(Array_1: list[int], Array_2: list[int]) -> tuple:
    new_list = []
    cur_tuple = ()
    for index in range(len(Array_1)):
        cur_tuple = (Array_1[index],Array_2[index])
        new_list.append(cur_tuple)
    print(new_list)
across_list([2, 3, 4],[5, 6, 7])
                        

'''
Q4. Design a function that will take two lists of integers
and an additional integer argument.  The function should
create and return a list of tuples that are pairs across the lists.
If a list is shorter than the other, the tuple gets filled with the
additional argument.
ie. if the function is called with [2, 3, 4], [5, 6] and 1000
the function should return [(2, 5), (3, 6), (4, 1000)]
'''
