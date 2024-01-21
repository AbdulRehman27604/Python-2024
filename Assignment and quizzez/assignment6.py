import doctest

def get_powers(array: list[int], power:int) -> list:
    """
    The fuction take each element from the list and multiply itself power times and then add it in the new list.
    >>> get_powers([],2)
    []
    >>> get_powers([3,6,8,9],2)
    [9, 36, 64, 81]
    """
    lenght = len(array)
    new_list = []
    if array != []:
        for reps in range(lenght):
            new_value = array[reps] ** power
            new_list.append(new_value)
    return new_list


def concatenate(array: list[str]) -> str:
    """
    Takes a list and loops through it. it adds the elements in the list to the empty 
    string until every thing is added
    
    >>> concatenate([])
    ''
    >>> concatenate(['KHI','ISL','LOH','MUL','PEH'])
    'KHI ISL LOH MUL PEH'
    """
    string = ''
    lenght = len(array)
    if array != []:
        for count in range(lenght):
            if count == lenght - 1:
                string += array[count]
            else:
                string += array[count]
                string += ' '
    return string

def contains_multiple(line: list[int], number: int) -> bool:
    """
    >>> contains_multiple([],9)
    False
    >>> contains_multiple([4, 33, 16, 24, 35, 11, 18, 34, 36, 10, 7],0)
    False
    >>> contains_multiple([7,53,40,3],4)
    True
    >>> contains_multiple([4,8,56,34],3)
    False
    """
    found = False
    if line != []:
        for value in line:
            if number == 0:
                if value == 0:
                    found = True
            elif value % number == 0:
                found = True
                    
    return found

def get_long_enough(array: list[str],lenght: int) -> list:
    """
    Takes a list as parameter and compare each lenght of value to the threshold 
    value and if they are equal then it adds that value to a new list.
    
    >>> get_long_enough([],4)
    []
    >>> get_long_enough(['ab','fefef','efwew','re','gg'],2)
    ['ab', 'fefef', 'efwew', 're', 'gg']
    """
    new_list = []
    if array != []:
        for string in array:
            if len(string) >= lenght:
                new_list.append(string)
    return new_list

def all_multiples(array: list[int], number: int) -> bool:
    """
    checks if all the elements in the passed list are the multiple of number
    
    >>> all_multiples([],3)
    True
    >>> all_multiples([34,76,1,66,23],0)
    False
    >>> print(all_multiples([2,4,6,8],2))
    True
    >>> print(all_multiples([35,50,3,90],5))
    False
    """
    ok = False
    count = 0
    if array != []:
        if number == 0:
            for value in array:
                if value != 0:
                    return False
            return True
        else: 
            while (count < len(array)) and (array[count] % number == 0):
                count += 1
            if count == len(array):
                ok = True
    else:
        ok = True
    return ok
    

def getting_shorter(line: list[str]) -> bool:
    """
    checks if the list is in decending order of lenght of values.
    >>> getting_shorter([])
    True
    >>> getting_shorter(['biggest', 'bigger', 'ATE', 'at'])
    True
    >>> getting_shorter(['tiny', 'same', 'are', 'at'])
    False
    """
    is_ok = False
    count = 1
    if line != []:
        value = line[0]
        while count < len(line) and len(value) > len(line[count]):
            value = line[count]
            count += 1
        if count == len(line):
            is_ok = True
    else:
        is_ok = True
    return is_ok


