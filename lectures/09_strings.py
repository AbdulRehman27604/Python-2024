import doctest
import math
'''
Q0.These functions appear to have similar behaviours but are very different.
'''

# Q0a. What is the difference between the expected output in the
# tests for these 2 functions?


def string_return() -> str:
    """ demonstrate returning a string
    >>> string_return()
    'error'
    """
    value = 'error'
    return value


def string_print() -> None:
    """ demonstrate printing a string
    >>> string_print()
    error
    """
    value = 'error'
    print(value)

# The differences become much more clear when you call them....

# Q0b. if I execute the following code what is printed:

# returned_value = string_return()
# print(returned_value)

# Q0c. given your answer above, can I do this:
# sliced_str = returned_value[0:4]
# print(sliced_str)


# Q0d. if I execute the following code what is printed:
# returned_value = string_print()
# print(returned_value)

# Q0e. given your answer above, can I do this:
# sliced_str = returned_value[0:4]
# print(sliced_str)


'''
Q1. Design a function that will take a word and determine whether
it is plural or not (ends with the letter s)
Assume any word that ends with s is plural (ie. pass is considered plural)
'''
def is_plural(given_word) -> bool:
    last_letter = given_word[-1]
    if last_letter == 's':
        return True
    return False  


'''
Q2. Design a function that pluralizes a word if it is not already plural
The function should return a pluralized word (s added to the end).
We are going to assume anything with an s at the end is already pluralized.
'''
def pluralizes_a_word(word: str) -> str:
    """
    >>> pluralizes_a_word(" ")
    's'
    
    >>> pluralizes_a_word("play")
    'plays'
    >>> pluralizes_a_word("plays")
    'Already pluralized'
    """
    if is_plural(word) == False:
        word += 's'
        return word 
    return 'Already pluralized'
        
pluralizes_a_word("play")

'''
Q3. Design a function that takes a string and determines whether it
is composed of exactly 2 repeating strings ie. 'abcabc' is a repeating string.
'''
def word_1(word: str) -> bool:
    """
    >>> word_1("abcabc")
    True
    >>> word_1("carca")
    False
    """
    lenght = int(len(word) / 2)
    initial = word[0:lenght]
    final = word[0:-lenght]
    if initial == final:
        return print("True")
    return print("False")
word_1("abcabe")
'''
Q4. Design a function that takes the amount of time an
object takes to fall after being dropped in seconds.
The function calculates and returns the distance the object fell in meters,
where the formula for distance is:
        d = 1/2 gt^2
        where t is the time in seconds and
        g is gravitational acceleration constant at 9.8 m/s^2
        d is in meters
If the function is passed a negative value for time it should
return the value -1 to indicate an error.
'''
gravity = 9.8
def distance_relative_to_time(time: int) -> float:
    """
    >>> distance_relative_to_time(100)
    49000.0
    >>> distance_relative_to_time(-23)
    -1
    """
    if time < 0:
        return -1
    
    distance = 1/2 * gravity * (time ** 2)
    return distance


'''
Q5. Design another function that takes the distance in meters from a point
to the ground and a time in seconds.  The function should determine whether
the object will hit the ground in the given time.
The function should assume that both time and distance are not negative.
Make use of the previous function!
'''

def reach_ground(distance_to_cover: int, time_passed: int) -> bool:
    """
    >>> reach_ground(12250.0,50)
    True
    >>> reach_ground(100,20)
    False
    """
    distance_covered = distance_relative_to_time(time_passed)
    if distance_covered == distance_to_cover:
        return True
    return False
    
