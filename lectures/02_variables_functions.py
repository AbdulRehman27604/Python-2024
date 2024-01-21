import math
'''
Q0. The following code attempts to print the total price
of a group of items I would like to buy followed by
the amount of money I will have left in my wallet.
My wallet started with 200 dollars.
There are a few things wrong with this program.
What do you think is wrong and how would you fix it?
'''

wallet = 200
purchase = 3+4+6+14
print('total of item prices:','$' + str(purchase))
print('wallet balance:','$' + str(wallet - purchase))



'''
Q1a. Recall from your math classes that the equation for
the lengths of the sides in a right triangle is:
  a^2 + b^2 = c^2
- using the ^ to indicate "raise to the power of" in the description
- how is "raise to the power of" represented in Python?

Write the code that will print the length of side c of
a right triangle with side a length as 3 and side length b as 4.
'''

'''lenght_a = 3
lenght_b = 4
lenght_c = ((lenght_a ** 2) + (lenght_b ** 2)) ** 0.5
print(lenght_c)'''

'''width = 3
breath = 4
hypotheus = (width ** 2 + breath ** 2) ** 0.5
print(hypotheus)'''


 
'''
Q1b. Update the program you just wrote so
it is contained within a function.
Test the function by calling it from the shell.
'''

"""def lenght_Triangle():
    lenght_a = 3
    lenght_b = 4
    lenght_c = math.sqrt((lenght_a ** 2) + (lenght_b ** 2))
    return lenght_c""" 

def hypotenus_of_triangle(width: int, breath: int) -> float:
    hypotheus = (width ** 2 + breath ** 2) ** 0.5
    return hypotheus    
    
'''
Q1c. complete the function below so it prints the lengths
of all sides of the right triangle.
Try to avoid re-writing code you have already written!

Test the function by calling it from the shell.
Your output should look something like this...

Dimensions of this right triangle:
the short sides are length: 3 and 4
the hypotenuse is length:  5.0
'''
def print_triangle_sides() -> None:
    lenght_a = int(input("Please enter the side of the triangle: "))
    lenght_b = int(input("PLease enter the other side of the triangle: "))
    new_side = hypotenus_of_triangle(lenght_a, lenght_b)
    print('the short sides are', lenght_a, '&', lenght_b, ', the hypothus is', f' {new_side:.2f}')
print_triangle_sides()

'''def print_right_triangle_dimensions():
    a = 3
    b = 4
    c = lenght_Triangle()
    print("The short sides are:",a ,"and", b,"while the hypotonuos is:",c)'''


'''
Q2. What does the following code print when uncommented?
Rewrite this code so that it is contained in a function
and both the code and the output makes it more clear
what the program is doing.
Test your function by calling it from the shell
'''

    
'''
Q3. Design a function that prints the area of
a 5.7 acre plot of land in square metres
Assume that 1 acre is 4046.85642 square metres
'''
conversion_rate = 4046.85642
def conversion() -> None:
    area_in_acres = 5.7
    area_in_square_metres = f' {(area_in_acres * conversion_rate):.2f}'
    print(area_in_acres, 'acres', 'in square metres is:',area_in_square_metres)
conversion()