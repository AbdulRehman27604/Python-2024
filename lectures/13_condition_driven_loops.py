'''
Q1. Design a function called get_number that asks a
user to enter a whole number int >= 0 returns
the number as an integer.
TIP: remember the int function
'''
'''def get_number():
    """
    get_number()
    50
    get_number()
    0
    """
    value = int(input("Please Enter a whole number: ")
    return value'''

'''
Q2. update the get_number so that if the user enters
an invalid int (non-integer or number<0)
it repeatedly prompts the user.
When a valid entry is finally made, the function
returns the number as an integer
TIP: remember the isdigit function
'''
def get_number(value):
    """
    """
    while (value < 0):
        value = int(input("Please Enter a whole number: "))
    return value


'''
Q3. Design a function that will compute and return the sum of a series
of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''
def sum_series():
    total = 0
    num = int(input("PLease enter value to sum: "))
    while num != 0:
        num = get_number(num)
        total += num
        num = int(input("PLease enter value to sum: "))
    return total

        

'''
Q4. Design a function that will determine and return the largest of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
'''
def largest_with_loop()-> int:
    """
    largest_with_loop()
    99
    """
    large = 0
    num = int(input("PLease enter value to find largest: "))
    while num != 0:
        if num > large:
            large = num
        num = int(input("PLease enter value to find largest: "))
    return large

    
'''
Q5. Design a function that will calculate and return the average of a
series of positive numbers entered by a user.  The user enters the values,
one at a time, and enters 0 to indicate there are no more values to enter.
If the user enters an invalid entry (non-integer or number<0),
they are repeatedly prompted until they enter valid data.
If the first number entered by the user is 0, the message
"Error: no data" is printed and the function returns -1.
'''
def average_series()-> float:
    total = 0
    count = 0
    number = int(input("Please enter the value to calculate avarage: "))
    while number != 0:
        number = get_number(number)
        total += number
        count += 1
        number = int(input("Please enter the value to calculate avarage: "))
    avg = total / count
    return avg

print(average_series())