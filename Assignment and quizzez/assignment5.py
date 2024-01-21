import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5

# PART 1
def get_sequence(starting_value: int, increment: int, max_value: int) -> str:
    """
    >>> get_sequence(0,0, 12)
    ''
    >>> get_sequence(6,10, 36)
    '6,16,26,36'
    >>> get_sequence(6,10, 34)
    '6,16,26'
    """
    string = str(starting_value)
    multiply = 1
    value = 0
    value = starting_value + (multiply * increment)
    while value <= max_value:
        string += ','
        string += str(value)
        multiply += 1
        value = starting_value + (multiply * increment)
    return string

ten = 10
def digit_sum(number: int) -> int:
    """
    >>> digit_sum(0)
    0
    >>> digit_sum(-571)
    13
    >>> digit_sum(432)
    9
    """
    total = 0
    number = abs(number)
    while number != 0:
        value = number % ten
        total += value
        number //= ten
    return total

def sum_factors(number: int) -> int:
    """
    >>> sum_factors(0)
    0
    >>> sum_factors(12)
    16
    >>> sum_factors(25)
    6
    >>> sum_factors(-67)
    0
    """
    count = 1
    total = 0
    while count < number:
        if number % count == 0:
            total += count
        count += 1
    return total

def is_perfect(num: int) -> bool:
    """
    >>> is_perfect(6)
    True
    >>> is_perfect(0)
    False
    >>> >>> is_perfect(50)
    False
    """
    value = sum_factors(num)
    if value == num:
        return True
    return False
        
def n_perfect_numbers(n) -> str:
    """
    >>> n_perfect_numbers(4)
    6,28,496,8128
    >>> n_perfect_numbers(3)
    6,28,496
    >>> n_perfect_numbers(2)
    6,28
    >>> n_perfect_numbers(1)
    6
    >>> n_perfect_numbers(0)
    ''
    """
    reps = 0
    count = 1
    string = ''
    while reps != n:
        value = sum_factors(count)
        if count == value:
            if reps != n - 1:
                string += str(count)
                string += ','
            else:
                string += str(count)
            reps += 1
        count += 1
    return string


# PART 2

def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    #this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    #die = int(input('enter a simulated dice roll\n'))

    return die

def take_turn(name:str,current_point:int,round_number:int) -> int:
    """
    The program takes the three parameters: name, current_point and round_number
    it calls the dies roll function thrice and compare there results to set the 
    roll_score value which is then added to current_point, the programs terminates
    when current value reaches 21 or above.
    
    """
    roll_score = 0
    num_1 = roll_one_die()
    num_2 = roll_one_die()
    num_3 = roll_one_die()
    if num_1 == num_2 == num_3 == round_number:
        roll_score = 21
    elif num_1 == num_2 == num_3:
        roll_score = 5
    elif (num_1 == num_2 == round_number) or (num_1 == num_3 == round_number) or (num_2 == num_3 == round_number):
        roll_score = 2
    elif (num_1 == round_number) or (num_2 == round_number) or (num_3 == round_number):
        roll_score = 1
    else:
        roll_score = 0
    current_point += roll_score
    print("Player",name, "is taking a turn in round",round_number)
    print("Three dice rolled:",str(num_1)+',',str(num_2)+',',str(num_3))
    print("scored:",roll_score,"points")
    print("Total points:", current_point)
    print(" ")
    
    while current_point < 21 and roll_score != 0:
   
        num_1 = roll_one_die()
        num_2 = roll_one_die()
        num_3 = roll_one_die()
        if num_1 == num_2 == num_3 == round_number:
            roll_score = 21
        elif num_1 == num_2 == num_3:
            roll_score = 5
        elif (num_1 == num_2 == round_number) or (num_1 == num_3 == round_number) or (num_2 == num_3 == round_number):
            roll_score = 2     
        elif (num_1 == round_number) or (num_2 == round_number) or (num_3 == round_number):
            roll_score = 1
        else: roll_score = 0
        current_point += roll_score

        print("Three dice rolled:",str(num_1)+',',str(num_2)+',',str(num_3))
        print("scored:",roll_score,"points")
        print("Total points:", current_point) 
        print(" ")
    return current_point

def play_round(player1_name, player2_name, round_number):
    """
    Take two person names and the round number, it alternate calls the above fuction
    and sets both current value. The loop terminates when any of the  person point 
    reaches 21 or above. The person with the most value win and output accordingly.
    """    
    player1_points = 0
    player2_points = 0
    current_player = player1_name
    
    while player1_points < 21 and player2_points < 21:
        if current_player == player1_name:
            player1_points = take_turn(player1_name, player1_points, round_number)
            current_player = player2_name
        else:
            player2_points = take_turn(player2_name, player2_points, round_number)
            current_player = player1_name
    
    print(f"the winner of this round is: {player1_name if player1_points >= 21 else player2_name}")
    print(f"{player1_name} has {player1_points} points and {player2_name} has {player2_points} points")
    
    return player1_name if player1_points >= 21 else player2_name

