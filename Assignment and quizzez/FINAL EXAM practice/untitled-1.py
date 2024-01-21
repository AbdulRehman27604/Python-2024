import doctest

# ASSIGNMENT 5:
# part 1:

'''def get_sequence(starting_value: int, increment: int, max_value: int) -> str:
    """ the function return a tring of the artimatic series
    >>> get_sequence(0, 0, 0)
    0
    >>> get_sequence(2, 5, 32)
    2,7,12,17,22,27,32
    >>> get_sequence(2, 5, 31)
    2,7,12,17,22,27
    """
    string = str(starting_value)
    multiply = 1
    value = 0
    value = starting_value + (multiply * increment)
    while value <= max_value:
        string += ','
        string += str(value)
        multiply += 1
        value = starting_value + (multiply * increment)
    return string'''

ten = 10
def digit_sum(number: int) -> int:
    """
    >>> digit_sum(0)
    0
    >>> digit_sum(432)
    9
    """
    total = 0
    number = abs(number)
    while number != 0:
        value = number % ten
        total += value
        number //= ten
    return total

def sum_factors(number: int) -> int:
    """
    """
    total = 0
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1
    return total

#LAB 6
def sum_even_values(loint: list[int]) -> int:
    """
    >>> lst = []
    >>> sum_even_values(lst)
    0
    >>> lon = [2,4,5,9,1,10]
    >>> sum_even_values(lon)
    16
    """
    total = 0
    if loint != []:
        for num in loint:
            if num % 2 == 0:
                total += num
    return total

def count_above(lon: list[int], threshold: int) -> int:
    """
    >>> lst = []
    >>> count_above(lst, 6)
    0
    >>> lon = [2,6,8,4,1,9]
    >>> count_above(lon, 4)
    4
    """
    count = 0
    if lon != []:
        for num in lon:
            if num >= threshold:
                count += 1
    return count

def add1(lon: list[int]) -> list[int]:
    """
    >>> empty_list = []
    >>> add1(empty_list)
    []
    >>> lon = [1, 2, 3, 4]
    >>> add1(lon)
    [2, 3, 4, 5]
    """
    new_list = []
    if lon != []:
        for num in lon:
            new_list.append(num + 1)
    return new_list

def are_all_even(loint: list[int]) -> bool:
    """
    >>> empty_list = []
    >>> are_all_even(empty_list)
    True
    >>> lon = [2,5,6,8,9]
    >>> are_all_even(lon)
    False
    >>> even_lon = [2,6,8,10]
    >>> are_all_even(even_lon)
    True
    """
    if loint == []:
        return True
    else:
        index = 0
        length = len(loint)
        while index < length and loint[index] % 2 == 0:
            index += 1
    return index  == length
                
# Assignment 6

def get_powers(lon: list[int], power: int) -> list[int]:
    """ This function creates a new list with the elements raised to the power of the power parameter
    >>> empty_list = []
    >>> loint = [2, 5, 6, 8]
    >>> get_powers(empty_list, 4)
    []
    >>> get_powers(loint, 2)
    [4, 25, 36, 64]
    """
    new_list = []
    if lon != []:
        for num in lon:
            num **= power
            new_list.append(num)
    return new_list

def concatenate(lo_str: list[str]) -> str:
    """
    >>> empty_list = []
    >>> str_list = ['hello', 'my', 'name', 'is', 'ARZ']
    >>> concatenate(empty_list)
    ''
    >>> concatenate(str_list)
    'hello my name is ARZ'
    """
    string = ''
    if lo_str != []:
        length = len(lo_str)
        for index in range(length):
            if index == length - 1:
                string += lo_str[index]
            else:
                string += lo_str[index]
                string += ' '
    return string

def contains_multiple(lo_int: list[int], additional_int: int) -> bool:
    """
    >>> empty_list = []
    >>> loint = [2, 5, 7, 3, 9]
    >>> list_2 = [4,8,10,14,16]
    >>> contains_multiple(empty_list, 9)
    True
    >>> contains_multiple(loint, 9)
    True
    >>> contains_multiple(list_2, 3)
    False
    """
    index = 0
    length = len(lo_int)
    if lo_int != []:
        while index < length and lo_int[index] % additional_int != 0:
            index += 1
        return index != length
    else:
        return True
    
# LAB 7:
'''def swap(list1: list, pos_1:int, pos_2: int) -> None:
    """
    >>> empty_list = []
    >>> full_list = [2,3,7,1,9]
    >>> swap(empty_list, 3,5)
    >>> swap(full_list, 0, 3)
    [1,3,7,2,9]
    """
    if list1 != []:
        temp = list1[pos_1]
        list1[pos_1] = list1[pos_2]
        list[pos_2] = temp'''

# all these done in the practice:

# Q3, Q4, and Q5

HOUR = 2
Flight_info = (str, str, int)
def total_duration(lo_flights: Flight_info) -> float:
    """
    >>> empty_list = []
    >>> flight_list = [('Mexico', 'America',5), ('Karachi', 'Pakistan',4)]
    >>> total_duration(empty_list)
    0
    >>> total_duration(flight_list)
    9
    """
    hour = 0
    if lo_flights != []:
        for cur_tuple in lo_flights:
            hour += cur_tuple[HOUR]
    return hour


DE_CITY = 0
AR_CITY = 1

def get_destinations_from(lo_flights: Flight_info, departure_city: str) -> list[str]:
    """
    >>> empty_list = []
    >>> flights = [('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)]
    >>> get_destinations_from(empty_list, 'Karachi')
    []
    >>> get_destinations_from(flights, 'Victoria')
    ['Vancouver', 'Calgary']
    """
    new_list = []
    if lo_flights != []:
        for cur_tuple in lo_flights:
            if cur_tuple[DE_CITY].lower() == departure_city.lower():
                if cur_tuple[AR_CITY] not in new_list:
                    new_list.append(cur_tuple[AR_CITY])
    return new_list

#Assignment 7:


Date = (int, int, int)
Netflix = (str, str, list[str], list[str], Date)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
START_YEAR = 2000

def create_date(given_date: str) -> Date:
    """
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    """
    day, month, year = given_date.split('-')
    for position in range(len(months)):
        if month == months[position]:
            index = position + 1
    new_year = int(year) + START_YEAR
    date_tuple = (new_year, index, int(day))
    return date_tuple

constant = ':'
def create_show(movie: str, show_title: str, director: str, actors: str, date: str) -> Netflix:
    """
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [''], (2016, 9, 23))   
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1))   
    """
    director_list = director.split(constant)
    actor_list = actors.split(constant)
    new_date = create_date(date)
    new_tuple = (movie, show_title, director_list, actor_list, new_date)
    return new_tuple

TITLE = 1
def get_titles(netflix_list: Netflix) -> list[str]:
    """
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    """
    new_list = []
    for cur_tuple in netflix_list:
        netflix_title = cur_tuple[TITLE]
        new_list.append(netflix_title)
    return new_list

ACTOR = 4
def is_actor_in_show(netflix_tuple: Netflix, actor_name: str) -> bool:
    """
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    """
    found = False
    actor_names = netflix_tuple[ACTOR]
    length = len(actor_names)
    index = 0 
    new_name = actor_names[index]
    while index < length and new_name.lower() != actor_name.lower():
        index += 1
        new_name = actor_names[index]
    return index != length

for x in range(3):
    for y in range(2):
        print(y, end=' ')
print(x)

for outer in range(3):
    for inner in range(outer):
        print(outer, inner, sep=':', end=' ')
        
x = 0
for outer in range(5):
    for inner in range(outer):
        x += 1
print(x)