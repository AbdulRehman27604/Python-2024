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
    new_list = []
    file_handle = open(filename, 'r')
    file_handle.readline()
    
    for line in file_handle:
        
        line = line.strip()
        name, country, race_time1 = line.split(',')
        race_time1 = int(race_time1)
        
        milliseconds = race_time1 % CONVERT_BY_THOUSAND
        race_time1 = race_time1 // CONVERT_BY_THOUSAND
        remaining_minutes = race_time1 // CONVERT_BY_SIXTY
        remaining_seconds = race_time1 % CONVERT_BY_SIXTY 
        
        time_object = RaceTime(milliseconds, remaining_seconds, remaining_minutes)
        new_instance = RaceResult(name, country, time_object)
        new_list.append(new_instance)
    
    file_handle.close()
    return new_list
        
        


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
    index = 0
    length = len(loresults)
    if loresults != []:
        while index < length and (loresults[index].get_name()) != name:
            index += 1
        if index == length:
            index = -1
    else:
        index = -1

    return index 
            

def get_all_from_country(loresults: list[RaceResult], country: str) -> list[RaceResult]:
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
    if loresults != []:
        for instance in loresults:
            if instance.get_country() == country:
                result_list.append(instance)
                
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
    fastest = RaceTime(0, 0, 0)
    for instance in loresults:
        race_time = instance.get_finish_time()
        if fastest.is_faster(race_time):
            fastest = race_time
            
    return fastest
     
 
def get_with_fastest_time(loresults: list[RaceResult]) -> list[RacerNameCountry]:
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
    # TODO: complete this function'''
    
    new_list = []
    fastest_time = get_fastest_time(loresults)
    
    for objects in loresults:
        song_length = objects.get_finish_time()
        
        if song_length == fastest_time:
            name = objects.get_name()
            country = objects.get_country()
            new_tuple = (name, country)
            new_list.append(new_tuple)
            
    return new_list