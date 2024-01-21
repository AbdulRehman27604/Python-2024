import doctest

#LAB 1 practice
'''def print_my_info() -> None:
    favourite_number = 7
    name = 'ARZ'
    age = 19
    result = favourite_number / age
    print('My name is', name)
    print('My favourite number is',favourite_number) 
    print('I am',str(age),'years old')
    print('Here is some math:',str(favourite_number) + '/' + str(age), 'is',f'{result:.2f}')
print_my_info()

NUM_1 = 23.2
NUM_2 = 82.4
def print_sum() -> None:
    result = NUM_1 + NUM_2 
    print(result)'''


# ASSIGNMENT 2

def check_funds(balance_of_person: float, purchase_amount: float) -> None:
    """
    >>> check_funds(100.0, 50.2)
    you will have $49.8 left after this purchase
    >>> check_funds(10, 12)
    you have a negative balance
    you are short $2
    """
    if balance_of_person >= purchase_amount:
        balance_of_person -= purchase_amount
        print('you will have $' + str(balance_of_person),'left after this purchase')
    else:
        short_amount = purchase_amount - balance_of_person
        print('you have a negative balance')
        print('you are short','$'+str(short_amount))

def print_biggest(num1: float, num2: float, num3: float) -> None:
    """
    >>> print_biggest(0.0,0.0,0.0)
    0.0
    >>> print_biggest(1.0, 4.5, 5.7)
    5.7
    """
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

def is_multiple_of(n1: int, n2: int) -> None:
    """
    >>> is_multiple_of(8, 2)
    8 is a multiple of 2
    >>> is_multiple_of(9, 2)
    9 is not a multiple of 2
    """
    if n1 % n2 == 0:
        print(n1,'is a multiple of',n2)
    else:
        print(n1,'is not a multiple of',n2)
        
CODE_1 = 'FIRST_PURCHASE'
CODE_2 = 'FREQUENT_BUYER'
DIS_CODE_1 = 10
DIS_CODE_2 = 2
FREE = 0
SHIPPING_RATE = 0.1
NULL = 0
'''def display_charges(purchase_price: float, tax_rate: int, site_membership: bool, discount_code: str, country_name: str) -> None:
        """
        >>> display_charges(10.5, 15, True, 'NO_DISCOUNT', 'Pakistan')
         price: $ 10.50
         tax: $ 1.57
         shipping: $ 0.00
         total charge: $ 12.07
         
        >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
        price: $ 12.00
        tax: $ 0.96
        shipping: $ 2.20
        total charge: $ 15.16
        """
        if site_membership or country_name == 'Canada':
            shipping_fee = FREE
        else:
            shipping_fee = purchase_price * SHIPPING_RATE
        if purchase_price >= NULL:
            if discount_code == CODE_1:
                purchase_price -= DIS_CODE_1 
            elif discount_code == CODE_2:
                purchase_price -= DIS_CODE_2
            else:
                purchase_price -= NULL
        tax_amount = purchase_price * (tax_rate / 100)
        total_amount = purchase_price + shipping_fee + tax_amount
        print(f'price: $ {purchase_price:.2f}')
        print(f'tax: $ {tax_amount:.2f}')
        print(f'shipping: $ {shipping_fee:.2f}')
        print(f'total charge: $ {total_amount:.2f}')'''
        
#LAB 2

def print_longer(str_1: str, str_2: str) -> None:
    """
    >>> print_longer('hi','hello')
    hello
    >>> print_longer('car','jar')
    car
    """
    str_length_1 = len(str_1)
    str_length_2 = len(str_2)
    if str_length_1 == str_length_2:
        print(str_1)
    elif str_length_1 > str_length_2:
        print(str_1)
    else:
        print(str_2)
        
#Lab 3

def get_longer(string_1: str, string_2: str) -> str:
    """
    """
    len_str_1 = len(string_1)
    len_str_2 = len(string_2)
    
    if len_str_1 == len_str_2:
        print(string_1)
    elif len_str_1 > len_str_2:
        print(string_1)
    else:
        print(string_2)

GST = 0.05
PST = 0.1
def get_tax(money_on_food: float, money_on_alcohal: float) -> float:
    """
    """
    tax_on_food = money_on_food * GST
    tax_on_alcohal = (money_on_alcohal * GST) + (money_on_alcohal * PST)
    total_tax = tax_on_food + tax_on_alcohal
    return total_tax


# Assignment 3

def get_biggest(num1: int, num2: int, num3: int) -> int:
    """
    >>> get_biggest(23, 56, 12)
    56
    >>> get_biggest(0, 0, 0)
    0
    """
    if num1 > num2 and num1 > num3:
        value_to_return = num1
    elif num2 > num1 and num2 > num3:
        value_to_return = num2
    else:
        value_to_return = num3
    return value_to_return

def get_smallest(num1: int, num2: int, num3: int) -> int:
    """
    >>> get_smallest(23, 56, 12)
    12
    >>> get_biggest(0, 0, 0)
    0
    """
    if num1 < num2 and num1 < num3:
        value_to_return = num1
    elif num2 < num1 and num2 < num3:
        value_to_return = num2
    else:
        value_to_return = num3
    return value_to_return

def is_multiple_of(num1: int, num2: int) -> bool:
    """
    >>> is_multiple_of(8, 2)
    True
    >>> is_multiple_of(2,3)
    False
    """
    is_multiple = False
    if num1 % num2 == 0:
        is_multiple = True
    return is_multiple

def is_biggest_multiple_of_smallest(n1: int, n2: int, n3: int) -> bool:
    """
    >>> is_biggest_multiple_of_smallest(23,45,1)
    True
    >>> is_biggest_multiple_of_smallest(8,5,3)
    False
    """
    biggest = get_biggest(n1,n2,n3)
    smallest = get_smallest(n1,n2,n3)
    truth_value = is_multiple_of(biggest, smallest)
    return truth_value

FIRST_PURCHASE = 10
FREQUENT_BUYER = 2
NO_DISCOUNT = 0

def get_discount(dis_code: str, site_membership: bool):
    """
    """
    dis_amount = 0
    if dis_code == 'FIRST_PURCHASE':
        dis_amount = FIRST_PURCHASE
    elif dis_code == 'FREQUENT_BUYER' and site_membership:
        dis_amount = FREQUENT_BUYER
    else:
        dis_amount = 0
    return dis_amount

def get_discounted_price(discount_code: str, price: float, site_membership: bool) -> float:
    """
    """
    discount_value = get_discount(discount_code, site_membership)
    new_price = price - discount
    return new_price

def print_right_triangle(n: int) -> None:
    """
    """
    for index in range(1,n + 1):
        print(index * '*')
        
def print_isosceles_triangle(n):
    num = n + 1
    string = ''
    for index in range(n + 1):
        print(' ' * num, end='')
        print('*' * index)
        num -= 1


# Lab 4

def compute_harmonic_series(n):
    total = 0
    for index in range(1,n):
        total += 1/index
    return total


#LAB 5
YOUNG = 18
ADULT = 64
def print_name_age_v1() -> None:
    """
    """
    name = input("Please enter your name: ")
    age = int(input("please enter your age: "))   
    if age < YOUNG:
        print('Hello!',name,'child')
    elif age >= YOUNG and age <= ADULT:
        print('Hello!',name,'adult')
    else:
        print('Hello!',name,'senior')

def print_name_age_v2():
    name = input("Please enter your name: ")
    age = input("please enter your age: ")
    if not age.isdigit():
        print('you are lying about your age')
    elif int(age) < YOUNG:
        print('Hello!',name,'child')
    elif int(age) >= YOUNG and int(age) <= ADULT:
        print('Hello!',name,'adult')
    else:
        print('Hello!',name,'senior')    

def get_num(number: int, prompt: str) -> int:
    """
    """
    value = input(prompt)
    while not (value.isdigit() and int(value) > number):
        value = input(prompt)
    return value
number = 10
prompt = 'Please enter a number: '


def print_name_age_v3():
    """
    """
    name = input('Please Enter Your Name: ')
    sentence = 'PLease enter your age: '
    valid_number = 0
    age = get_num(valid_number, sentence)
    age = int(age)
    if age < YOUNG:
        print('Hello!',name,'child')
    elif age >= YOUNG and age <= ADULT:
        print('Hello!',name,'adult')
    else:
        print('Hello!',name,'senior')    

# ASSIGNMENT 5:
# part 1:

def get_sequence(starting_value: int, increment: int, max_value: int) -> str:
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
    return string

def digit_sum(number: int) -> int:
    """
    >>> digit_sum(0)
    0
    >>> digit_sum(432)
    9
    """
    total = 0
    abs_number = abs(number)
    mod_value = number // 10
    div_value = number % 10
    total += div_value
    while mod_value != 0:
        div_value = number % 10
        total += div_value
    return total
    
    
def raise_to_power(array:list[int], power_list: list[int]) -> None:
    """
    update the orginal list with the second list element as power applied on the
    same index on the first list.

    >>> raise_to_power([],[3,8,7])
    []
    >>> raise_to_power([3,9,1],[1,4,2])
    [3, 6561, 1]
    >>> raise_to_power([-2,6,-4],[2,4,3])
    [4, 1296, -64]
    """

    count = 0
    lenght = len(array)
    power_lenght = len(power_list)
    while count < power_lenght:
        array[index] = array[index] ** power_list[index]
        count += 1
    print(array)
    
x = 0
for outer in range(5):
    for inner in range(outer):
        x += 1
print(x)

s = 'EgGs'
s.lower()
print(s)