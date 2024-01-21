import doctest
'''
Q1. Design a function that will take a whole number and
prints the number and prints whether it is odd or not
'''
print("----------Code 1---------")
def even_or_odd(number: int):
    """
    >>> even_or_odd(10)
    The number entered is an even number.
    >>> even_or_odd(5)
    The number entered is an odd number.
    """
    print("The value entered is: ",number)
    remainder = number % 2
    if remainder == 0:
        print("The number entered is an even number.")
    else:
        print("The number entered is an odd number.")
even_or_odd(5)
        
    

'''
Q2. Design a function that takes two numbers and prints
the smallest value.  Do not use the builtin min function.
'''
print("----------Code 2----------")
def smallest_value(number1, number2):
    """
    >>> smallest_value(10,5)
    5
    >>> smallest_value(21,52)
    21
    """
    small = min(number1,number2)
    print(small)
smallest_value(23,-23.5)

'''
Q3. Design a function that takes one argument: a person's age
and determines and prints the cost of
riding the bus based on that given age.
Your function should assume age is not negative.

If age is less than 18, the cost is $1.50.
If age is 65 or more, the cost is $2.00.
For all other values of age, the cost is $2.50.
'''
print("----------Code 3----------")
adult = 18
senior = 65
def age_for_riding(age):
    """
    >>> age_for_riding(70)
    $2.00
    >>> age_for_riding(45)
    $2.50
     >>> age_for_riding(8)
    $1.50
    """
    cost = 0
    if age < adult:
        cost = 1.50
    elif age >= senior:
        cost = 2.00
    else:
        cost = 2.50
    print("According to your age the cost is:","$" + str(cost))
age_for_riding(70)


'''
Q4. Design a function that takes a number within the range of 1 through 10.
The function should assume it will only be called with numbers 1 to 10.
The function should display the Roman numeral version of that number.
The following list shows the Roman numerals for the numbers 1 through 10:

Number:	Roman Numeral
1	I
2	II
3	III
4	IV
5	V
6	VI
7	VII
8	VIII
9	IX
10	X
'''
print("----------Code 4----------")

list = ["I","II","III","IV","V","VI","VII","VIII","IX","X"]
def Roman(number):
    """
    >>> Roman(2)
    II
    >>> Roman(5)
    V
    """
    print(list[number - 1])
Roman(2)

def Roman2(number):
    """
    >>> Roman2(2)
    II
    >>> Roman2(5)
    V
    """
    if number == 1:
        print("I")
    elif number == 2:
        print("II")  
    elif number == 3:
        print("III") 
    elif number == 4:
        print("IV") 
    elif number == 5:
        print("V") 
    elif number == 6:
        print("VI") 
    elif number == 7:
        print("VII") 
    elif number == 8:
        print("VIII") 
    elif number == 9:
        print("IX") 
    elif number == 10:
        print("X")     
