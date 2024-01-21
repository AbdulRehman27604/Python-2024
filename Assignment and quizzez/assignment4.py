import doctest

def get_factors(number: int) ->str:
    """
    >>> get_factors(100)
    '1,2,4,5,10,20,25,50,100'
    >>> get_factors(12)
    '1,2,3,4,6,12'
    """
    string = ''
    for count in range(1, number + 1):
        if number % count == 0:
            if count != number:
                string += str(count)
                string += ','
            else:
                string += str(count)
    return string


def get_range_of_factors(start, end):
    """
    >>> get_range_of_factors(10, 13)
    1,2,5,10
    1,11
    1,2,3,4,6,12
    >>> get_range_of_factors(2, 6)
    1,2
    1,3
    1,2,4
    1,5
    >>> et_range_of_factors(0,0)
    ''
    """
    result = ""
    for num in range(start, end):
        factors = [str(i) for i in range(1, num + 1) if num % i == 0]
        for i in range(len(factors)):
            result += factors[i]
            if i < len(factors) - 1:
                result += ","
        result += "\n"
    return result


def sum_fibonacci_sequence(number: int) -> int:
    """
    >>> sum_fibonacci_sequence(7)
    20
    >>> sum_fibonacci_sequence(0)
    0
    >>> sum_fibonacci_sequence(9)
    54
    """
    null = 0
    previous_value = 0
    current_value = 1 
    value = 0
     
    if number == 0 or number == 1:
        return null
    else:
        if number == 2:
            value += previous_value
            value += current_value
            return value
        
    value += previous_value
    value += current_value   
    for i in range(2,number):
        new_value = previous_value + current_value
        previous_value = current_value
        current_value = new_value
        value += new_value
    return value


def print_tail(rocket_size: int) -> str:  
    """
    will print the tail as long as user wants.
    """
    string = '//  '
    if rocket_size == 0:
        print('//  \\\\')
    else:
        for count in range(rocket_size):
            if count == rocket_size - 1:
                string += "/\\"
            else:
                string += "/\\" + ' ' + ' '
        string += '  \\\\'
        print(string)

dot = '.'
slashes = '/\\'
reverse_slashes = '\/'
def print_booster(body_size:int):
    string = ''
    count = 1
    dot_count = body_size
    
    if body_size != 0:
        for x in range(body_size):
            string += '|' + dot * dot_count
            string += slashes * count
            string += dot * dot_count
            count += 1  
            dot_count -= 1
            dublicate_string = string[-(len(string)-1) :]
            string += dublicate_string + '|'
            pure_lenght_of_string = len(string)
            print(string)   
            string_lenght = int(((len(string)/2)) - 1)
            string = ''
    
        print('|'+ slashes * string_lenght + '|')
        print('|'+ reverse_slashes * string_lenght + '|')
    
        string_2 = ''
        count_2 = body_size
        dot_count_2 = 1 
        for x in range(body_size):
            string_2 += '|' + dot * dot_count_2
            string_2 += reverse_slashes * count_2
            string_2 += dot * dot_count_2
            count_2 -= 1
            dot_count_2+= 1 
            dublicate_string_2 = string_2[-(len(string_2)-1) :]
            string_2 += dublicate_string_2 + '|'
            print(string_2) 
            string_lenght_2 = int(((len(string_2)/2)) - 1)
            string_2 = ''   
    
        last_string = '+'
        for lenght in range(pure_lenght_of_string - 2):
            if lenght % 2 == 0:
                last_string += '='
            else:
                last_string += '*'
        last_string += '+'
        print(last_string)
    else:
        print('|/\/\|')
        print('|\/\/|')
        print('+=*=*+')        
    
    
symbol = '~#'
def print_instrument_unit(lenght:int):
    number = 1
    count = 0
    string = ''
    if lenght  == 0:
        string += '||'+ symbol +'||'       
        for x in range(2):
            print(string)
    else:
        while count != (lenght):
            number += 2
            count += 1
        string += '||'+ symbol*(number) +'||'
        for y in range(2):
            print(string)
    
        
    
    last_string = '+'
    for Z in range(len(string) - 2):
        if Z % 2 == 0:
            last_string += '='
        else:
            last_string += '*'
    last_string += '+'
    print(last_string)    


        
symbol_2 = '%'
def print_lem_adapter(size_of_rocket:int):
    string_1 = ' //'
    string_2 = '//'
    if size_of_rocket == 0:
        print(' //' + '\\\\')
        print('//'+' %'+'\\\\')
        print('+=*=*+')
    else:
        for i in range(size_of_rocket*2):
            if i == (size_of_rocket*2) - 1:
                string_1 += ' %\\\\'
            else:
                string_1 += ' %'
        for j in range((size_of_rocket*2) + 1):
            if j == (size_of_rocket*2):
                string_2 += ' %\\\\'
            else:
                string_2 += ' %' 
        print(string_1)
        print(string_2)
            
 
        last_string = '+'
        for Z in range(len(string_2)-2):
            if Z % 2 == 0:
                last_string += '='
            else:
                last_string += '*'
        last_string += '+'
        print(last_string)       
            
slash = '/'
backslash = '\\'
symbol_1 = '++'
symbol_2 = '**'
space = ' ' 
def print_space_craft(rocket_size:int)->str:
    space_count = (rocket_size * 2) + 2
    reps = (rocket_size * 2)
    slash_count = 0
    string_lenght = 0
    string = ''
    for i in range(reps):
        string += space * space_count + slash * slash_count + symbol_2 + backslash * slash_count
        print(string)
        string_lenght = len(string)
        slash_count += 1
        space_count -= 1
        string = ''
    
    last_string = '  +'
    for Z in range(string_lenght-3):
        if Z % 2 == 0:
            last_string += '='
        else:
            last_string += '*'
    last_string += '+'
    print(last_string)    


def print_rocket_ship(rocket_size:int, boosters:int):    
    print_space_craft(rocket_size)
    print_lem_adapter(rocket_size)
    print_instrument_unit(rocket_size)
    for i in range(boosters):
        print_booster(rocket_size)
    print_tail(rocket_size)


'''x = int(input("PLease enter booster number: "))
while x != 0:
    y = int(input("Please enter the size of rocket: "))
    print_rocket_ship(y , x)
    x = int(input("PLease enter booster number: "))'''

print("Hello World", end='')
a = ' john'    
b = "Enter a Value: "
print(a,b)

my_string = 'Love of cotton candy'
print(my_string[-18:16])













