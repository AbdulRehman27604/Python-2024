def print_my_info():
    """
    The program prints the name, favourite number, age, and a calculation.
    >>> print_my_info()
    My name is Abdul Rehman 
    My favourite number is 7 
    I am 19 years old 
    Here is some math: 7 / 19 is 0.3684210526315789
    """
    name = "Abdul Rehman"
    favoraite_number = 7
    age = 19
    result = 7/19
    print("My name is", name,"\nMy favourite number is",favoraite_number,"\nI am",age,"years old","\nHere is some math:",favoraite_number,"/",age,"is",result)
print_my_info()

def print_sum():
    """
    The program adds two values
    >>> print_sum()
    105.60000000000001
    """
    number1 = 23.2
    number2 = 82.4
    sum = number1 + number2
    print(sum)
print_sum()