import doctest
from race_time import RaceTime
from race_result import RaceResult

# represents a racer as (name, country)
# where name and country != ''
RacerNameCountry = tuple[str, str]

# columns of values in input file row and positions in RacerNameCountry
NULL = 0
FIRST_ELEMENT = 0
CONVERT_BY_THOUSAND = 1000
CONVERT_BY_SIXTY = 60
NAME = 0
COUNTRY = 1
TIME_MS = 2


def read_file(filename: str) -> list[RaceResult]:
    """ returns a list of RaceResults populated with data from filename
    Precondition: the file exists, is not empty, has the following
      information on each row separated by commas:
      racer's name, racer's country, race time in milliseconds>=0
      and contains a header row with the column titles.
      The header row is ignored.

    >>> read_file('0lines_data.csv')
    []
    >>> read_file('9lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Evan Jager', 'United States', RaceTime(450, 0, 8)), \
     RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7)), \
     RaceResult('Saif Saaeed Shaheen', 'Qatar', RaceTime(630, 53, 7)), \
     RaceResult('Wander Moura', 'Brazil', RaceTime(410, 14, 8)), \
     RaceResult('Mahiedine Mekhissi-Benabbad', 'France', RaceTime(90, 0, 8)), \
     RaceResult('Peter Renner', 'New Zealand', RaceTime(50, 14, 8))]
    """
    # TODO: complete this function
    result_list = []
    file_handle = open(filename, 'r')
    file_handle.readline()
    
    for line in file_handle:
        line = line.strip()
        name, country, seconds = line.split(',')
        seconds = int(seconds)
        
        milliseconds = seconds % CONVERT_BY_THOUSAND
        seconds = seconds // CONVERT_BY_THOUSAND
        remaining_minutes = seconds // CONVERT_BY_SIXTY
        remaining_seconds = seconds % CONVERT_BY_SIXTY        
    
        time_of_race = RaceTime(milliseconds,remaining_seconds, remaining_minutes)
        result_of_race = RaceResult(name, country, time_of_race)
        result_list.append(result_of_race)
        
    file_handle.close()
    return result_list


def find_athlete(loresults: list[RaceResult], name: str) -> int:
    """ returns the position of RaceResult with given athlete name in loresults
    Returns -1 if name not found
    Returns the position of the first if there >1 RaceResult with given name
    Precondition: case sensitive (ie. 'Brad' != 'brad')

    >>> find_athlete([], 'Brimin Kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))],\
        'brimin kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Brimin Kipruto')
    1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Peter Renner')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Usain Bolt', 'Canada', RaceTime(1, 2, 2019))], \
        'Usain Bolt')
    0
    """
    # TODO: complete this function
    position = -1
    count = 0
    index = 0
    
    for race_object in loresults:
        search_name = race_object.get_name()
        if search_name == name:
            count += 1
    if count > NULL:
        while (loresults[index]).get_name() != name:
            index += 1
        position = index  
    return position
        

def get_all_from_country(loresults: list[RaceResult], country: str
                         ) -> list[RaceResult]:
    """ returns a list of all results of the given country
    Precondition: case sensitive (ie. 'Canada' != 'canada')

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 12)), \
     RaceResult('Perrier', 'France', RaceTime(1, 23, 18)), \
     RaceResult('Perrieruels', 'Canada', RaceTime(3, 29, 0)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country([], 'Jamaica')
    []

    >>> get_all_from_country(results, 'jamaica')
    []

    >>> get_all_from_country(results, 'Jamaica') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country(results, 'Japan')
    []
    """
    # TODO: complete this function
    result_list = []
    for race_object in loresults:
        country_name = race_object.get_country()
        if country_name == country:
            result_list.append(race_object)
    return result_list
            

def get_fastest_time(loresults: list[RaceResult]) -> RaceTime:
    """ returns the fastest RaceTime of all finish_times of 
    RaceResult instances in loresults
    Precondition: loresults is not empty

    >>> one_result = [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 9))]
    >>> results = \
    [RaceResult('Allen', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 16, 17)), \
     RaceResult('Barnes', 'Canada', RaceTime(3, 43, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 29, 9)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 48, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 17))]

    >>> get_fastest_time(one_result)
    RaceTime(12, 31, 9)
    >>> get_fastest_time(results)
    RaceTime(3, 29, 9)
    """
    # TODO: complete this function
    position = 0
    length = len(loresults)
    for index in range(length):
        race_object = loresults[index]
        time_object = race_object.get_finish_time()
        milliseconds = time_object.get_ms()
        seconds = time_object.get_sec()
        minutes = time_object.get_mins()
        
        total_seconds = minutes * CONVERT_BY_SIXTY + seconds
        total_milliseconds = total_seconds * CONVERT_BY_THOUSAND
        total_milliseconds += milliseconds    
        
        if index == NULL:
            fastest = total_milliseconds
        else:
            if fastest > total_milliseconds:
                fastest = total_milliseconds
                position = index
                
    new_object = loresults[position]
    return new_object.get_finish_time()
        

def get_with_fastest_time(loresults: list[RaceResult]
                          ) -> list[RacerNameCountry]:
    """ returns a list tuples of fastest RaceResults in loresults

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 6)), \
     RaceResult('Barnes', 'Canada', RaceTime(1, 23, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 10, 7)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 15, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 6))]
     
    >>> get_with_fastest_time([])
    []
    >>> get_with_fastest_time(results)
    [('Zhou', 'China'), ('Davis', 'Jamaica')]
    """
    # TODO: complete this function
    if not loresults:
        return []

    first_racer_time = loresults[FIRST_ELEMENT].get_finish_time()
    winners = [(loresults[FIRST_ELEMENT].get_name(), loresults[FIRST_ELEMENT].get_country())]

    for result in loresults[1:]:
        if result.get_finish_time().is_faster(first_racer_time):
            first_racer_time = result.get_finish_time()
            winners = [(result.get_name(), result.get_country())]
        elif result.get_finish_time() == first_racer_time:
            winners.append((result.get_name(), result.get_country()))

    return winners    


def are_isomorphic(string_1: str, string_2: str) -> bool:
    """compares two string if they are equal
    >>> are_isomorphic('AABCCA', 'XXQZZX')
    True
    >>> are_isomorphic('UYSFN','QQSVR')
    False
    """
    str_1_dict = {}
    str_2_dict = {}
    position = 0
    length_1 = len(string_1)
    length_2 = len(string_2)
    
    if length_1 == length_2:
        
        for index in range(length_1):
            letter = string_1[index]
            if letter not in str_1_dict:
                str_1_dict[letter] = 1
            else:
                str_1_dict[letter] += 1
                
        for index_2 in range(length_2):
            letter_2 = string_2[index_2]
            if letter_2 not in str_2_dict:
                str_2_dict[letter_2] = 1
            else:
                str_2_dict[letter_2] += 1  
        
        while position < length_1 and str_1_dict[string_1[position]] == str_2_dict[string_2[position]]:
            position += 1
            
    return position == length_2

def gcd(num_1: int, num_2: int) -> int:
    """
    >>> gcd(0,0)
    0
    >>> gcd(2,3)
    1
    """
    a = num_1
    b = num_2
    remainder = a - b*int((a/b))
    
    while remainder != 0:
        a = b
        b = remainder
        remainder = a - b*int((a/b))
    return print(b)

def print_range(num_1: float, num_2: float) -> None:
    """
    >>> print_range(2.3,7.2)
    range: 2.3 to 7.2
    >>> print_range(10.9, 3.7)
    range: 3.7 to 10.9
    """
    if num_1 > num_2:
        print('range:',num_2,'to',num_1)
    else:
        print('range:',num_1,'to',num_2)