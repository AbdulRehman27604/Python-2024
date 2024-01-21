import doctest

def sum_even_values(line: list[int]) -> int:
    """
    >>> sum_even_values([])
    0
    >>> sum_even_values([2,4,3,9,0])
    6
    >>> sum_even_values([1,3,5,7])
    0
    """
    total = 0
    if line != 0:
        for value in line:
            if value % 2 == 0:
                total += value
    return total

def count_above(array: list, threshold_value: int) -> int:
    """
    >>> count_above([],10)
    0
    >>> count_above([2,3,8,4],3)
    3
    >>> count_above([23,34,12,78,45],50)
    1
    """
    count = 0
    if array != 0:
        for value in array:
            if value > threshold_value:
                count += 1
    return count

def add1(lon: list) -> list:
    """
    >>> add1([])
    []
    >>> add1([2,5,7,9])
    [3, 6, 8, 10]
    """
    new_list = []
    if lon != 0:
        for number in lon:
            number += 1
            new_list.append(number)
    return new_list

def are_all_even(array: list) -> bool:
    """
    >>> are_all_even([])
    True
    >>> are_all_even([2,6,12])
    True
    >>> are_all_even([2,4,5])
    False
    
    """
    count = 0
    is_even = True
    lenght = len(array)
    if array != 0:
        while count < lenght:
            if array[count] % 2 != 0:
                is_even = False
            count += 1
    return is_even

