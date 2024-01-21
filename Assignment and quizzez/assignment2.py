import doctest

def check_funds(balance: float, purchase_amount: float):
    """
    >>> check_funds(100,34.67)
    you will have $ 65.33 left after this purchase
    >>> check_funds(-23.45,34.67)
    you have a negative balance
    >>> check_funds(16.76,34.67)
    you are short $ 17.91
    """
    if balance >= purchase_amount:
        new_balance = balance - purchase_amount
        print("you will have $",f'{new_balance:.2f}',"left after this purchase")
    elif balance < 0:
        print("you have a negative balance")
    elif balance < purchase_amount:
        amount_short = purchase_amount - balance
        print("you are short $", f'{amount_short:.2f}')
     
def print_biggest(number_1: float, number_2: float, number_3: float):
    """
    >>> print_biggest(10.3,89.4,41.0)
    89.4
    >>> print_biggest(100,34.7,1.5)
    100
    >>> print_biggest(-23,-12,6)
    6
    >>> print_biggest(-39,-45,-99.9)
    -39
    """    
    if number_1 >= number_2 and number_1 >= number_3:
        print(number_1)
    elif number_2 >= number_1 and number_2 >= number_3:
        print(number_2)
    else:
        print(number_3) 

 
def convert_inches(inches):
    """
    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    
    >>> convert_inches(1223212213)
    19305 mi, 1317 yd, 0 ft, 1 in
    
    >>> convert_inches(31)
    0 mi, 0 yd, 2 ft, 7 in
    
    >>> convert_inches(-2123)
    -1 mi, 1701 yd, 0 ft, 1 in
    
    >>> convert_inches(2324234.894859)
    36.0 mi, 1202.0 yd, 0.0 ft, 2.894859000109136 in
    """
    inches_per_mile = 63360 
    inches_per_yard = 36 
    inches_per_feet = 12  
    
    miles = inches // inches_per_mile
    inches %= inches_per_mile
    
    yards = inches // inches_per_yard
    inches %= inches_per_yard
    
    feet = inches // inches_per_feet 
    inches  %= inches_per_feet
    
    print(miles,'mi'+',',yards,'yd'+',',feet,'ft'+',',inches,'in')


    
def is_multiple_of(n1: int, n2: int):

    """
    >>> is_multiple_of(15,3)
    15 is a multiple of 3
    >>> is_multiple_of(180,2)
    180 is a multiple of 2
    """
    if n2 != 0:
        if n1 % n2 == 0:
            print(n1,"is a multiple of",n2)
        else:
            print(n1,"is not a multiple of",n2)
    elif n1 == 0 and n2 == 0:
        print(n1,"is a multiple of",n2)
    else:
        print(n1,"is not a multiple of",n2)

first_buyer_discount = 10.00
frequent_buyer_discount = 2.00
shipping_rate = 10

def display_charges(purchase_price: float, tax_rate: int, is_a_member: bool, discount_code: str, country_to_ship: str):
    """
    >>> display_charges(4.39, 9, False, 'NO_DISCOUNT', 'Mozambique')
    price: $ 4.39
    tax: $ 0.40
    shipping: $ 0.44
    total charge: $ 5.22

    >>> display_charges(4.39, 9, True, 'NO_DISCOUNT', 'Mozambique')
    price: $ 4.39
    tax: $ 0.40
    shipping: $ 0.00
    total charge: $ 4.79

    >>> display_charges(4.39, 9, False, 'NO_DISCOUNT', 'Canada')
    price: $ 4.39
    tax: $ 0.40
    shipping: $ 0.00
    total charge: $ 4.79
    
    >>> display_charges(4.39, 9, True, 'NO_DISCOUNT', 'Canada')
    price: $ 4.39
    tax: $ 0.40
    shipping: $ 0.00
    total charge: $ 4.79

    >>> display_charges(4.39, 9, False, 'FIRST_PURCHASE', 'Mozambique')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.44
    total charge: $ 0.44
    
    >>> display_charges(4.39, 9, True, 'FIRST_PURCHASE', 'Mozambique')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    
    >>> display_charges(4.39, 9, False, 'FIRST_PURCHASE', 'Canada')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    
    >>> display_charges(4.39, 9, True, 'FIRST_PURCHASE', 'Canada')
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    
    >>> display_charges(4.39, 9, False, 'FREQUENT_BUYER', 'Mozambique')
    price: $ 2.39
    tax: $ 0.22
    shipping: $ 0.44
    total charge: $ 3.04
  """    
    if country_to_ship.lower() == 'canada' or is_a_member:
        shipping_cost = 0
    else:
        shipping_cost = (shipping_rate / 100) * purchase_price

    if discount_code.upper() == 'FIRST_PURCHASE':
        purchase_price -= first_buyer_discount
    elif discount_code.upper() == 'FREQUENT_BUYER':
        purchase_price -= frequent_buyer_discount
    else:
        purchase_price -= 0

    if purchase_price < 0:
        purchase_price = 0

    item_tax = (tax_rate / 100) * purchase_price
    total_price = purchase_price + shipping_cost + item_tax

    print('price: $', f'{purchase_price:.2f}')
    print('tax: $', f'{item_tax:.2f}')
    print('shipping: $', f'{shipping_cost:.2f}')
    print('total charge: $', f'{total_price:.2f}')
