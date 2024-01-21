
def print_bird():
  print('  @_____@','\n  (\' v \')','\n//(_____)\\\\','\n    " "  ')

def print_alienBird():
  print('           ___________','\n\"\"\_______(\'0       0\')_______/"\"','\n            \___V___/','\n          __/       \__')

def print_logo():
  spacer = "/~~~~~~~~\\"
  print(spacer)
  print_bird()
  print(spacer)
  print_alienBird()
  print(spacer)
  print_bird()
  print(spacer)
  print_alienBird()
  print(spacer)
print_logo()


from math import pi
# calling the function pi from the math module

def calculate_surface_area(height:float, diameter:float):
  #Taking height and diameter as parameters
  
  circumference = pi * diameter
  #calculate the circumference
  
  area_of_top = pi * (diameter/2) ** 2
  #used the formulae IIr^2 to calculate the area of top of cylinder
  
  area_of_walls = circumference * height
  #calculate the area of walls by multipying the cicumference and the height if the cylinder
  
  total_surface_area = 2 * area_of_top + area_of_walls
  #multipying area_of_top with two as a cylinder consist of two circles and adding it with area_of_walls to calculate the total surface area.
  
  print('cylinder area:',round(total_surface_area,1))
  #Using the round function to get 1 decimal place answer and print
calculate_surface_area(1.2, 3.5)
  

  
  