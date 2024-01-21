import doctest

# Part 1
def get_biggest(number_1: int, number_2: int, number_3: int):
    """
    >>> get_biggest(2,4,3)
    4
    >>> get_biggest(10,5,9)
    10
    >>> get_biggest(23,100,999)
    999
    >>> get_biggest(0,0,0)
    0
    >>> get_biggest(23,23,23)
    23
    """
    if (number_1 > number_2) and (number_1 > number_3):
        return number_1
    elif (number_2 > number_1) and (number_2 > number_3):
        return number_2
    else:
        return number_3

def get_smallest(number_1: int, number_2: int, number_3: int):
    """
    >>> get_smallest(2,4,3)
    2
    >>> get_smallest(10,5,9)
    5
    >>> get_smallest(999,100,87)
    87
    >>> get_smallest(0,0,0)
    0
    >>> get_smallest(23,23,23)
    23
    """
    if (number_1 < number_2) and (number_1 < number_3):
        return number_1
    elif (number_2 < number_1) and (number_2 < number_3):
        return number_2
    else:
        return number_3

def is_multiple_of(n1: int, n2: int):

    """
    >>> is_multiple_of(4, 4)
    True
    >>> is_multiple_of(13, 13)
    True
    >>> is_multiple_of(5, 30)
    False
    >>> is_multiple_of(90, 15)
    True
    >>> is_multiple_of(8, 33)
    False
    >>> is_multiple_of(25, 4)
    False
    >>> is_multiple_of(10, 0)
    False
    >>> is_multiple_of(0, 9)
    True
    >>> is_multiple_of(-5, -3)
    False
    """
    if n2 != 0:
        if n1 % n2 == 0:
            return True
        else:
            return False
    elif n1 == 0 and n2 == 0:
        return True
    else:
        return False
        
def is_biggest_multiple_of_smallest(value_1, value_2, value_3):
    """
    >>> is_biggest_multiple_of_smallest(5, 50, 9)
    True
    >>> is_biggest_multiple_of_smallest(-10, -30, -3)
    False
    >>> is_biggest_multiple_of_smallest(14, 7, 99)
    False
    """
    biggest_value = get_biggest(value_1, value_2, value_3)
    smallest_value = get_smallest(value_1, value_2, value_3)
    return is_multiple_of(biggest_value, smallest_value)

#part 2
code_first_purchase = 10
code_frequent_buyer = 2
code_no_discount = 0

def get_discount(discount_code: str, is_member: bool):
    """
    >>> get_discount('FIRST_PURCHASE', True)
    10
    >>> get_discount('FIRST_PURCHASE', False)
    10
    >>> get_discount('FREQUENT_BUYER', True)
    2
    >>> get_discount('FREQUENT_BUYER', False)
    0
    >>> get_discount('NO_DISCOUNT', True)
    0
    >>> get_discount('NO_DISCOUNT', False)
    0
    """
    if discount_code == 'FIRST_PURCHASE':
        return code_first_purchase
    elif discount_code == 'FREQUENT_BUYER' and is_member:
        return code_frequent_buyer
    else:
        return code_no_discount


def get_discounted_price(code_for_discount: str, item_price: float, membership: bool):
    """
    >>> get_discounted_price('FIRST_PURCHASE',12.43,True)
    2.4299999999999997
    >>> get_discounted_price('FIRST_PURCHASE',10.53,False)
    0.5299999999999994
    >>> get_discounted_price('FIRST_PURCHASE',2.34,True)
    0
    >>> get_discounted_price('FIRST_PURCHASE',1.90,False)
    0
    >>> get_discounted_price('FREQUENT_BUYER',9.67,True)
    7.67
    >>> get_discounted_price('FREQUENT_BUYER',54,False)
    54
    >>> get_discounted_price('NO_DISCOUNT',12.34,True)
    12.34
    >>> get_discounted_price('NO_DISCOUNT',88.3,False)
    88.3
    """
    discount_to_apply = get_discount(code_for_discount, membership)
    discounted_price = item_price - discount_to_apply
    if discounted_price < 0:
        return 0
    return discounted_price

shipping = 10
free_shipping = 0
def  get_shipping(site_membership: bool, country: str, purchase_price: float):
    """
    >>> get_shipping(True, 'Pakistan', 10.3)
    0
    >>> get_shipping(False, 'Pakistan', 23.0)
    2.3000000000000003
    >>> get_shipping(True, 'Canada', 9.8)
    0
    >>> get_shipping(False, 'Canada', 3.46)
    0
    """
    if site_membership or country == 'Canada':
        return free_shipping
    else:
        return purchase_price * (shipping / 100)
    
def display_charges(cost_of_item: float, tax_rate: int, membership_of_site: bool, discount_with_code: str, country_name: str):
    """
    >>> display_charges(12,8,True,'FIRST_PURCHASE','Canada')
    price: $ 2.00
    tax: $ 0.16
    shipping: $ 0.00
    total charge: $ 2.16
    >>> display_charges(23,4,False,'FIRST_PURCHASE','Canada')
    price: $ 13.00
    tax: $ 0.52
    shipping: $ 0.00
    total charge: $ 13.52
    >>> display_charges(2,1,True,'FIRST_PURCHASE','Pakistan') 
    price: $ 0.00
    tax: $ 0.00
    shipping: $ 0.00
    total charge: $ 0.00
    >>> display_charges(43.23,64,False,'FIRST_PURCHASE','Pakistan')
    price: $ 33.23
    tax: $ 21.27
    shipping: $ 4.32
    total charge: $ 58.82
    >>> display_charges(23,6,True,"FREQUENT_BUYER",'Canada')
    price: $ 21.00
    tax: $ 1.26
    shipping: $ 0.00
    total charge: $ 22.26
    >>> display_charges(89,7,False,"FREQUENT_BUYER",'Canada')
    price: $ 89.00
    tax: $ 6.23
    shipping: $ 0.00
    total charge: $ 95.23
    >>> display_charges(8.9,3,True,"FREQUENT_BUYER",'Pakistan')
    price: $ 6.90
    tax: $ 0.21
    shipping: $ 0.00
    total charge: $ 7.11
    >>> display_charges(54,3,False,"FREQUENT_BUYER",'Pakistan')
    price: $ 54.00
    tax: $ 1.62
    shipping: $ 5.40
    total charge: $ 61.02
    >>> display_charges(232.31,32,True,"NO_DISCOUNT",'Canada')
    price: $ 232.31
    tax: $ 74.34
    shipping: $ 0.00
    total charge: $ 306.65
    >>> display_charges(100.3,98,False,"NO_DISCOUNT",'Canada')
    price: $ 100.30
    tax: $ 98.29
    shipping: $ 0.00
    total charge: $ 198.59
    >>> display_charges(74,27,True,"NO_DISCOUNT",'Pakistan')
    price: $ 74.00
    tax: $ 19.98
    shipping: $ 0.00
    total charge: $ 93.98
    >>> display_charges(108,19,False,"NO_DISCOUNT",'Pakistan')
    price: $ 108.00
    tax: $ 20.52
    shipping: $ 10.80
    total charge: $ 139.32
    >>> display_charges(5.19, 6, False, 'NO_DISCOUNT', 'Dominican Republic')
    price: $ 5.19
    tax: $ 0.31
    shipping: $ 0.52
    total charge: $ 6.02
    """
    discounted_cost = get_discounted_price(discount_with_code, cost_of_item, membership_of_site)
    cost_for_shipping = get_shipping(membership_of_site, country_name,cost_of_item )
    
    taxes = (discounted_cost) * (tax_rate / 100)
    total_amount = discounted_cost + taxes + cost_for_shipping
    print('price: $',f'{discounted_cost:.2f}')
    print('tax: $',f'{taxes:.2f}')
    print('shipping: $',f'{cost_for_shipping:.2f}')
    print('total charge: $',f'{total_amount:.2f}')







