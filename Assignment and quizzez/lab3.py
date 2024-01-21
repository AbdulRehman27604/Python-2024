import doctest
GST = 0.05 
PST = 0.10

def get_longer(string_1: str, string_2: str)-> str:
    """
    >>> get_longer('horse', 'cow')
    horse
    >>> get_longer('car', 'cap')
    car
    >>> get_longer('lion', 'zebra')
    zebra
    """
    lenght_of_string_1 = len(string_1)
    lenght_of_string_2 = len(string_2)
    if lenght_of_string_1 == lenght_of_string_2:
        return string_1
    elif lenght_of_string_1 > lenght_of_string_2:
        return string_1
    else:
        return string_2

        
def get_tax(money_on_food: float, money_on_alcohal: float) -> float:
    """
    >>> get_tax(100.4, 24.34)
    8.67
    >>> get_tax(0, 0)
    0
    >>> get_tax(29.3, 2.43)
    1.83
    >>> get_tax(10, 23)
    3.95
    """
    tax_on_food = money_on_food * (GST)
    tax_on_alcohal = (money_on_alcohal * (GST)) + (money_on_alcohal * (PST/100))
    total_tax = tax_on_food + tax_on_alcohal 
    
    return (total_tax)
    
def get_bill_share (food_amount: float, alcohal_amount: float, number_of_people: int) -> float:
    """
    get_bill_share (12,89,4)
    28.7375
    get_bill_share (0,23,2)
    13.225
    get_bill_share (67,0,4)
    17.5875
    get_bill_share (6.34,98.43,1)
    119.85150000000002
    """
    taxes = get_tax(food_amount, alcohal_amount)
    total_amount = food_amount + alcohal_amount + taxes
    amount_per_person = (total_amount / number_of_people)
    return amount_per_person


