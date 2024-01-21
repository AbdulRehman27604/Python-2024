import doctest
child_age = 18
adult_age = 64


def print_name_age_v1()->None:
    """
    Take name and age from the user and prints hello with there name and age.
    """
    string = ''
    name = input("Please Enter your name: ")
    age = int(input("Please Enter your age: "))
    if age < child_age:
        string = 'child'
    elif (age >= child_age) and (age <= adult_age):
        string = 'adult'
    else:
        string = 'senior'
    print('hello',name,string)


def print_name_age_v2():
    """
    Take the input from the user about name and age. If age is not an integer, 
    it prints that the user is lying, else print who is he.
    """
    name = input("PLease enter your name: ")
    age = input("PLease enter you age: ")
    if not age.isdigit():
        print(name,"you are lying about your age.")
    elif int(age) < child_age:
        print('hello',name,'child')
    elif (int(age) >= child_age) and (int(age) <= adult_age):
        print('hello',name,'adult')
    else:
        print('hello',name,'senior') 


def get_num(number:int, prompt:str) -> int:
    """
    Takes the user input and compare it with the minimum number and also checks 
    if it is an integer. If all the checks are complete then it return the value.
    """
    invalid = True
    value = input(prompt)
    while invalid:
        if value.isdigit() and int(value) >= number:
            invalid = False
        else:
            value = input(prompt)
    return int(value)


minimum = 0
def print_name_age_v3():
    """
    Takes name and age from the user and checks the age of the user, if it is
    correct.
    """
    string = ''
    name = input("Please enter your name: ")
    new_age = get_num(minimum,'Input a value: ')
    if int(new_age) < child_age:
        string = 'child'
    elif (int(new_age) >= child_age) and (int(new_age) <= adult_age):
        string = 'adult'
    else:
        string = 'senior'    
    print('hello',name,string)

def play_round(name_1:str, name_2:str, round_num:int) -> str:
    """
    Take two person names and the round number, it alternate calls the above fuction
    and sets both current value. The loop terminates when any of the  person point 
    reaches 21 or above. The person with the most value win and output accordingly.
    """
    person_1_point = take_turn(name_1,0,round_num)
    person_2_point = take_turn(name_2,0,round_num)
    while person_1_point < 21 and person_2_point < 21:
        person_1_point += take_turn(name_1,person_1_point,round_num)
        person_2_point += take_turn(name_2,person_2_point,round_num)     
    if person_1_point > person_2_point:
        print("the winner of this round is:", name_1)
        print(name_1,"has",person_1_point,"points and",name_2,"has",person_2_point,"points")
        return name_1
    else:
        print("the winner of this round is:", name_2)
        print(name_1,"has",person_1_point,"points and",name_2,"has",person_2_point,"points")
        return name_2