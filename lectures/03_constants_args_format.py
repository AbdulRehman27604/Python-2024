
'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.
How can we make this function easier for some reading it to quickly
comprehend what the function does?
'''



'''
Q1b. The acres_to_sqr_meters function is not very versatile -
it will only calculate the square meters for 5.7 acres!
Edit the function so that it will calculate the square meters
for ANY non-negative number of acres.
'''


'''
Q2. Design a function that will take the name of the best team and
print out a cheer for that team.
'''
def cheer_team(team) -> None:
    print(team, 'You are the best')
cheer_team('KALA')


''' Q3. Design a function called print_bill that takes the
price of a clothing item. The function should print the bill
which should include the following items:
the price, the PST amount, the GST amount, and the total bill including taxes
NOTE: PST is provincial sales tax at 7%
GST is goods and services tax at 5% '''
print("   ","\nCode 3")

PST = 0.07
GST = 0.05
def print_bill(cloth_price: int) -> None:
    """
    >>> print_bill(50)
    the pst amount is: $3.5 ,the gst price is: $2.5 and the total price is: $56.0
    """
    pst_price = cloth_price * PST
    gst_price = cloth_price * GST
    total_price = cloth_price + pst_price + gst_price
    print('the pst amount is: ' + '$' + f'{pst_price:.1f}',',the gst price is: ' + '$' + f'{gst_price:.1f}','and the total price is: ' + '$'+ f'{total_price:.1f}')



'''
Q4. Design a function that will take a person's name and age and will
print a personalized message for that person.
For example, if we call the function as: welcome('Amy', 21)
the function should print:  Welcome Amy! Amy's 21 years old.
'''
print("   ","\nCode 4")

def personalized_message(name: str, age: int) -> None:
    """
    >>> personalized_message('Amy', 21)
    Welcome Amy! Amy's 21 years old
    """
    print('Welcome',name + '!', name + '\'s', str(age), 'years old')
personalized_message('Amy', 21)