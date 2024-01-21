import doctest
def compute_harmonic_series(number: int) -> float:
    """
    >>> compute_harmonic_series(0)
    0
    >>> compute_harmonic_series(2)
    1.5
    """
    total = 0
    for i in range(number):
        total += 1/(i+1)
    return total

def get_fibonacci_sequence(number: int) -> str:
    """
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'
    >>> get_fibonacci_sequence(9)
    '0,1,1,2,3,5,8,13,21'
    """
    string = ''
    previous_value = 0
    current_value = 1     
     
    if number == 0:
        return string
    elif number == 1:
        return str(previous_value)
    else:
        if number == 2:
            string += str(previous_value)
            string += ','
            string += str(current_value)
            return string
        
    string += str(previous_value)
    string += ','
    string += str(current_value)     
    string += ','
    
    for i in range(2,number):
        new_value = previous_value + current_value
        previous_value = current_value
        current_value = new_value
        if i == number - 1:
            string += str(new_value)
        else:           
            string += str(new_value)
            string += ','
    return string   


def print_pattern(height: int, width: int, string_1:str, string_2:str) -> str:
    """
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    >>> print_pattern(0,0, '!@', '$$$')
    
    >>> print_pattern(1,1, '!@', '$$$')
    !@$$$
    >>> print_pattern(3,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    """
    new_string_1 = ''
    new_string_2 = ''
    for i in range(height):
        if i % 2 != 0:
            for x in range(width):
                new_string_1 += (string_2 + string_1)
            print(new_string_1)
            new_string_1 = ''
        else:
            for y in range(width):
                new_string_2 += (string_1 + string_2)
            print(new_string_2)    
            new_string_2 = ''
print_pattern(1000,1000, '!@', '$$$')