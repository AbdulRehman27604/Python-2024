import doctest

'''
Q1. Design a function that takes an integer n and prints
print the squares of numbers from 0 to n separated by commas.
Your function should assume n is not negative.
'''
list = []
def square_of_n(n):
    """
    >>> square_of_n(10)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    >>> square_of_n(0)
    [0]
    """
    for i in range(n + 1):
        list.append(i**2)
    return list

def print_square_n(n):
    for i in range(n + 1):
        sq = i ** 2
        print(sq, end='')
        if i < n:
            print(', ',end='')


'''
Q2. Design a function that takes an integer n and returns
the sum of the squares of numbers from 0 to n.
Your function should assume n is not negative.
'''

def sum_of_squares(n2: int):
    total = 0
    new_list = square_of_n(n2)
    for i in range(len(new_list)):
        total += new_list[i]
    return total


def return_square(n: int)-> int:
    """
    >>> return_square(0)
    0
    >>> return_square(10)
    385
    >>> return_square(5)
    55
    """
    total = 0
    for x in range(n + 1):
        total += x ** 2
    return total

'''
Q3. Design a function that takes an integer n and returns
a string with the squares of all the numbers from 0 to limit inclusive,
where numbers are separated by commas.
'''
def convert_str(number: int) -> str:
    result = ''
    for y in range(number + 1):
        sq = y ** 2
        result += str(sq)
        if y < number:
            result += ','
    return result


'''
Q4. Design a function that takes an integer n and prints
prints the number n down to 1 followed by 'BLASTOFF!'
Your function should assume n is greater than 0.
'''
def print_negative_step(n) -> str:
    for i in range(n ,-1,-1):
        print(i)
    print("BLASTOFF!")
print_negative_step(10)

'''Q5. Design a function that takes an integer n and a string and
prints that string n times with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''
'''def multiply_string(n: int,string_1: str) -> str:
    result = ''
    for i in range(n+1):
        result += string_1
    print(string)
multiply_string(2,'hi')''' 


'''
Q6. Design a function that takes an integer n and a string and
returns a new string that has the given string repeated n times
with no additional spaces or newlines.
Your function should assume n is not negative
You cannot use the * operator.
'''
"""import doctest
DAYS_PER_EARTH_YEAR = 365
DAYS_PER_MARS_YEAR = 687
def print_planet_age(number_of_days: int)->None:
    earth_year = int(number_of_days /  DAYS_PER_EARTH_YEAR)
    mars_year = int(number_of_days / DAYS_PER_MARS_YEAR)
    if earth_year != 1 and mars_year != 1:  
        print("Earth age:",earth_year,"years")
        print("Mars age:",mars_year,"years")
    elif earth_year == 1 and mars_year != 1:
        print("Earth age:",earth_year,"year")
        print("Mars age:",mars_year,"years")  
    elif earth_year != 1 and mars_year == 1:
        print("Earth age:",earth_year,"years")
        print("Mars age:",mars_year,"year")  
    else:
        print("Earth age:",earth_year,"year")
        print("Mars age:",mars_year,"year")         
print_planet_age()"""


s = 'love hello elephant'
print(s[-18:16])