import doctest


'''
Q1. Design a function that takes a string and 2 numbers
representing height and width.
The function should print a rectangular pattern using the given string
that is of dimension width by height.
You can assume that height and width are not negative and the string is not empty
Example. if the string is '*#' and height is 4 and width is 3, it should print:
*#*#*#
*#*#*#
*#*#*#
*#*#*#
You must not use the * operator to repeat your string.
'''

def print_String(string: str, height: int, width: int) -> None:
     """
     >>> print_String('#',4,3)
     *#*#*#
     *#*#*#
     *#*#*#
     *#*#*#
     """
     char = ''
     for i in range(width):
          char += '*'
          char += string
     for x in range(height):
          print(char)
print_String('#',4,3)
print(' ')

'''
Q2. Design a function that will take a number representing height and it
should print a right angle triangle using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
Examples:
if ht is 2, prints:
*
**
if ht is 3, prints:
*
**
***
'''
def triangle(height: int)-> None:
     """
     >>> triangle(10)
     *
     **
     ***
     ****
     *****
     ******
     *******
     ********
     *********
     **********
     """
     initial = 1
     for i in range(height):
          string = '*' * initial
          initial += 1
          print(string)
     
triangle(10)
     

'''
Q3. Design a fucntion that takes a non-negative number that represents a size
and prints a number pattern according to the size.
You can assume that size is greater than or equal to 0
Examples:
if the size is 3 it prints...
3
32
321
if the size is 5 it prints...
5
54
543
5432
54321
'''
def down_size(number)-> None:
     """
     >>> down_size(5)
     5
     54
     543
     5432
     54321
     """
     string = ''
     for i in range(number,0,-1):
          string += str(i)
          print(string)
down_size(5)
          
          

'''
Q4. Design a function that will take a number representing height and it
should print an isosceles triangle using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
TIP: to get the stars to appear centered, think about how many space (' ')
characters to print on a row before you print the * characters.
Examples:
if ht is 2, prints:
 *
***
if ht is 3, prints:
  *
 ***
*****
'''
print(" ")
def isosceles(height: int)-> None:
     """
     >>> isosceles(5)
             *
            ***
           *****
          *******
         *********
     """
     lenght = height
     number = 1
     for i in range(height):
          string = ''
          lenght -= 1
          string += ' ' * (lenght)
          string += '*' * number
          number += 2
          print(string)
isosceles(5)
     

'''
Q5. Design a function that will take a number representing height and it
should print a diamond using '*'s that is of the given height.
You can assume that size is greater than or equal to 0
Examples:
if ht is 2, prints:
 *
***
 *
if ht is 3, prints:
  *
 ***
*****
 ***
  *
'''
def ajeeb_o_Ghareeb():
     lenght = height
     number = 1     
     for i in range(height):
          string = ''
          lenght -= 1
          string += ' ' * (lenght)
          string += '*' * number
          number += 2
          print(string)
          
          new_lenght = -1
          new_number = 
     for x in range(height - 1):
          string = ''
          new_lenght += 1
          string += ' ' * new_lenght
          string += '*' * number
          
          
                
          
          
     
