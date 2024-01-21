'''import doctest
months_list = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_SID        = 0
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10


def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]],
                                 dict[str, str]):
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names] <--- check repetation
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {}, {})
    
    >>> read_file('11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})
    """
    month_pos = 0
    show_date_dict = {}
    show_actors_dict = {}
    show_cat_id = {}
    show_id_title = {}
   
    result_tuple = ()
   
    file_handle = open(filename, 'r')
   
    for line in file_handle:
        line = line.strip()
        lst_items = line.split(',')
   
        show_id = lst_items[INPUT_SID]
        show_title = lst_items[INPUT_TITLE]
        show_casts_list = lst_items[INPUT_CAST].split(':')
        show_date = lst_items[INPUT_DATE]
        show_cat_list = lst_items[INPUT_CATEGORIES].split(':')
        
        date_list = show_date.split('-')
        date_day = int(date_list[DAY])
        date_month = date_list[MONTH]
        
        date_year = int(date_list[YEAR]) + START_YEAR
        length_month_list = len(months_list)
   
        month_pos = 0  # Initialize month_pos before the loop
   
        for index in range(length_month_list):  # Use range instead of len for iteration
            if months_list[index] == date_month:
                month_pos = index + 1
                break  # Exit the loop once the month is found
   
        date_tuple = (date_year, month_pos, date_day)
   
        show_date_dict[show_id] = date_tuple
   
        if show_id not in show_actors_dict:
            show_actors_dict[show_id] = []  # Initialize the list for the show_id
   
        for cast_name in show_casts_list:
            if cast_name not in show_actors_dict[show_id]:
                show_actors_dict[show_id].append(cast_name)
   
        for category in show_cat_list:
            if category not in show_cat_id:
                show_cat_id[category] = []  # Initialize the list for the category
            show_cat_id[category].append(show_id)
   
        show_id_title[show_id] = show_title
   
        result_tuple = (show_date_dict, show_actors_dict, show_cat_id, show_id_title)
   
    return result_tuple    


dict_cast = {}
name = ['zia','kamran','abdul']
id_show = 10
dict_cast[id_show] = name
x = dict_cast[id_show]
print(x)

name1 = ['zia','kamran','kala']
name2 = ['adhi','manav','zia']
if name1 in name2:
    print('1')
else:
    print('0')
    
    
    
    result_list = []
    found = False
    generate_tuple = read_file(filename)
    
    id_cat_dict = generate_tuple[CAT_ID]
    id_date_dict = generate_tuple[ID_DATE]
    id_cast_dict = generate_tuple[ID_CAST]
    id_title_dict = generate_tuple[ID_TITLE]
    
    list_of_ids = id_cat_dict[category]
    
    for ids in list_of_ids:
        if actors != []:
            list_cast = id_cast_dict[ids]
            for name_of_cast in list_cast:
                if name_of_cast in actors:
                    found = True
            if found == True:
                if id_date_dict[ids] < date:
                    title_name = id_title_dict[ids]
                    result_list = (title_name,ids)
     
        elif id_date_dict[ids] < date:
            new_title_name = id_title_dict[ids]
            result_list = (new_title_name,ids) 
            
    return result_list'''

x = 
print(x)