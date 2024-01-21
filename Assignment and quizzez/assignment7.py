import doctest
date = tuple[int, int, int]
netflix_show = tuple[str, str, list[str], list[str], date]

def raise_to_power(array:list[int], power_list: list[int]) -> None:
    """
    update the orginal list with the second list element as power applied on the
    same index on the first list.

    >>> raise_to_power([],[3,8,7])
    []
    >>> raise_to_power([3,9,1],[1,4,2])
    [3, 6561, 1]
    >>> raise_to_power([-2,6,-4],[2,4,3])
    [4, 1296, -64]
    """

    count = 0
    lenght = len(array)
    power_lenght = len(power_list)
    for index in range(lenght):
        if count < power_lenght:
            new_value = array[index] ** power_list[index]
            count += 1
            array[index] = new_value

def create_date(date_year: str) -> date:
    """
    change date format
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    """
    final_month = 0
    this_tuple = ()
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    char_list = date_year.split('-')
    year = char_list[2]
    day = char_list[0]
    month = char_list[1]
    for index in range(len(month_names)):
        if month_names[index] == month:
            final_month = index
    new_year = '20' + year
    this_tuple = (int(new_year),final_month + 1,int(day))

    return this_tuple
    

def create_show(show_type: str, show_title: str, director_name: str, actor_name: str, date_str: str) -> netflix_show:
    """
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23)) 
    
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
    (2019, 7, 1))
    """
    if director_name != '':
        directors = director_name.split(':')
    else:
        directors = []
    if actor_name != '':
        actors = actor_name.split(':')
    else:
        actors = []
        
    day, month, year = date_str.split('-')
    movie_date =  create_date(date_str)
    cur_tuple = (show_type, show_title, directors, actors, movie_date) 
    return cur_tuple   

def get_titles(netflix_show_list: list[netflix_show]) -> list[str]:
    """
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    """
    
    titles = []
    for shows in netflix_show_list:
        titles.append(shows[1])
    return titles

def is_actor_in_show(net_show: netflix_show, actor_name: str ) -> bool:
    """
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True
    
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    """
    actors = net_show[3]
    actor_name_lower = actor_name.lower()
    found = False
    for actor in actors:
        if actor.lower() == actor_name_lower:
            found = True
    return found  
            
def count_shows_before_date(netflix_list: list[netflix_show], date_tuple: date) -> int:
    """
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2017, 4, 18))]
    
    >>> count_shows_before_date(loshows, (2015, 1, 1))
    0
    
    >>> count_shows_before_date(loshows, (2018, 10, 20))
    3
    """
    count = 0
    
    for cur_tuple in netflix_list:
        new_date = cur_tuple[4]
        if new_date < date_tuple:
            count += 1
            
    return count

def get_shows_with_actor(list_for_netflix: list[netflix_show], name_of_actor: str) -> list:
    """
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
    ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
    'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
    'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
    (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
    'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]
    
    >>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
    'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
    ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
    'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
    'Jemima Kirke'], \
    (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'Justin Bieber')
    []
    """
    found = False
    new_list = []
    for new_tuple in list_for_netflix:
        actor_in_list = new_tuple[3]
        for name in actor_in_list:
            if name.lower() == name_of_actor.lower():
                for patch in new_list:
                    if patch == new_tuple:
                        found = True
                if not found:
                    new_list.append(new_tuple)
            found = False
    return new_list           
        
