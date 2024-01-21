import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

'''
Q0. Design a function that will take two numbers and
returns the sum of those numbers
'''
def sum_of_two(num1:float, num2:float) -> float:
    """
    >>> sum_of_two(10.1, 34.4)
    44
    >>> sum_of_two(45 + 20)
    65.5
    """
    total = num1 + num2
    return total
    

'''
Q0b. Design a function that will take two numbers and prints the average
of those numbers.
In your function body, call the funtion desiged in Q1a
to practice calling a function from another function.
'''
def Average_of_two(number1:float, number2:float) -> None:
    """
    >>> Average_of_two(2,4)
    3
    >>> Average_of_two(10,15)
    12.5
    """
    tatal = sum_of_two(number1,number2)
    avg = total/2
    print(avg)

'''
Q0c. If the function you designed in Q0a printed the sum instead of
returning it, would you average function still behave as expected?

No it will work not work as expected because average is dependent to sum function and calls the sum function to store value in total if total is empty then the average fuction will return None.
'''

'''
Q1. Below is the print_fare function we wrote in a past lecture.
Continuing in this problem domain, design a separate function that takes
the number of children, number of adults and number of seniors
and returns the total fare for those riders.
You function should take into acount a group discount of 10%
for groups of 10 or more.
You can assume the function will not be passed negative values.

NOTICE: print_fare does not return a value, so calling it will not be useful
BUT, there are CONSTANTS defined that might be useful!
'''


def print_fare(age: int) -> None:
    """ determines the bus fare for a rider of the given age and prints it
    Precondition: age > 0
    >>> print_fare(0)
    The fare is: $1.50
    >>> print_fare(ADULT-1)
    The fare is: $1.50
    >>> print_fare(ADULT)
    The fare is: $2.50
    >>> print_fare(ADULT+1)
    The fare is: $2.50
    >>> print_fare(SENIOR-1)
    The fare is: $2.50
    >>> print_fare(SENIOR)
    The fare is: $2.00
    >>> print_fare(SENIOR+1)
    The fare is: $2.00
    """
    fare = 0
    if age < ADULT:
        fare = CHILD_RATE
    elif age >= SENIOR:
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE

    print(f'The fare is: ${fare:.2f}')

def discount_fare(number_adult: int, number_senior: int, number_child: int) -> float:
    
    """
    >>> discount_fare(0,0,0)
    0.0
    >>> discount_fare(2,1,2)
    10.0
    >>> discount_fare(2,2,2)
    12.0
    >>> discount_fare(4,2,4)
    18.0
    >>> discount_fare(4,3,4)
    19.8
    """
    child_fare = number_child * CHILD_RATE
    adult_fare = number_adult * ADULT_RATE
    senior_fare = number_senior * SENIOR_RATE
    
    total = number_adult + number_senior + number_child
    total_fare = child_fare + adult_fare + senior_fare
    
    if total >= 10:
        discount = total_fare * 0.1
        total_fare -= discount
        
    return total_fare

'''
Q2. design a function that takes the amount of money in a bank account and
the number of children, number of adults and number of seniors.
You can assume the function will not be passed negative values for
number of people, but the account balance can be negative.

The function should print the total fare for all of these people and
the balance left in the bank account after the fare is paid.
The function should return the balance left in the bank account
after the fare is paid.
'''

def account_balance(amount: float, child_1: int, adult_1: int, senior_1: int) -> float:
    """
    >>> account_balance(0,0,0,0)
    0.0
    >>> account_balance(46.23,2,1,2)
    36.23
    >>> account_balance(56.89,2,2,2)
    44.89
    >>> account_balance(89.40,4,2,4)
    71.4
    >>> account_balance(100,4,3,4)
    80.2
    """
    fare = discount_fare(child_1,adult_1,senior_1)
    print("The fare is:",fare)
    balance = amount - fare
    return balance
    






''' Q3. Recall we designed the following function in a past lecture.
Update this function so it does not print the roman numeral,
but instead returns it.'''


def print_roman_numeral(num: int) -> None:
    """ determines and prints the corresponding roman numeral for the given num
    Precondition: 1 <= num <=10
    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
    >>> print_roman_numeral(5)
    V
    >>> print_roman_numeral(6)
    VI
    >>> print_roman_numeral(7)
    VII
    >>> print_roman_numeral(8)
    VIII
    >>> print_roman_numeral(9)
    IX
    >>> print_roman_numeral(10)
    X
    """
    roman_numeral = ''

    if num == 1:
        roman_numeral = 'I'
    elif num == 2:
        roman_numeral = 'II'
    elif num == 3:
        roman_numeral = 'III'
    elif num == 4:
        roman_numeral = 'IV'
    elif num == 5:
        roman_numeral = 'V'
    elif num == 6:
        roman_numeral = 'VI'
    elif num == 7:
        roman_numeral = 'VII'
    elif num == 8:
        roman_numeral = 'VIII'
    elif num == 9:
        roman_numeral = 'IX'
    else:
        roman_numeral = 'X'

    print(roman_numeral)
