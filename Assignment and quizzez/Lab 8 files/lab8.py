'''import doctest
NAME = 0
AGE = 1
name_age_tuple = [(str, int)]

def file_to_person_list(output_file: str) -> list[name_age_tuple]:
    """
    file_name = 'lab8-name-age.txt'
    >>> file_to_person_list(file_name)
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
    """

    new_list = []
    handle_file = open(output_file,'r')
    value = handle_file.readline()
    while value != '':
        item_list = value.split(' ')
        new_tuple = (item_list[NAME],int(item_list[AGE]))
        new_list.append(new_tuple)
        value = handle_file.readline()
    handle_file.close()
    return new_list

def get_average_age(info_list: list[name_age_tuple]) -> int:
    """
    >>> get_average_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)])
    31
    """
    count = 0
    total_age = 0
    avg_age = 0
    if info_list != []:
        for information in info_list:
            total_age += information[AGE]
            count += 1
        avg_age = int(total_age / count)
    return avg_age

def get_above_age(info_list: list[name_age_tuple], threshold_age: int) -> list[name_age_tuple]:
    """
    >>> get_above_age([],76)
    []
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 18)
    [('Tian', 27), ('Jose', 53), ('Rajan', 65)]
    """
    new_list = []
    for info in info_list:
        if info[AGE] > threshold_age:
            new_list.append(info)
    return new_list

def to_file(info_list: list[name_age_tuple], file:str) -> None:
    """
    >>> lst = [('claire',21)]
    >>> output_file = 'lab8-name-age.txt'
    >>> to_file(lst,output_file)
    """
    name = ''
    age = 0
    string = ''
    opened_file = open(file,'w')
    for value in info_list:
        name = value[NAME]
        age = value[AGE]
        string += name
        string += ','
        string += str(age)
        opened_file.write(string)
        opened_file.write("\n")
        string = ''
    opened_file.close()


def write_names_above_avg_age(input_file: str, output_file: str) -> None:
    """
    >>> input_file_1 = 'lab8-name-age.txt'
    >>> output_file_1 = 'values.txt'
    >>> write_names_above_avg_age(input_file_1, output_file_1)
    """
    result_list = file_to_person_list(input_file)
    average_age = get_average_age(result_list)
    another_list = get_above_age(result_list, average_age)
    to_file(another_list, output_file)


    
new_list = []
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

file_handle = open(filename,'r')
line = file_handle.readline().strip()
line = file_handle.readline().strip()
while line != '':
    lst = line.split(',')
    movie_type = lst[1]
    movie_title = lst[2]
    director_list = lst[3].split(':')
    cast_list = lst[4].split(':')
    
    day,month,year = lst[6].split('-')
    year = 2000 + int(year)
    for index in range(len(month_names)):
        if month_names[index] == month:
            final_month = index
    date_tuple = (year,final_month,int(day))
    
    new_tuple = (movie_type, movie_title, director_list, cast_list,date_tuple)
    new_list.append(new_tuple)
file_handle.close()
return new_list
    
# take a tuple from the list then open the cast list in the tuple and take 
#one cast name from the 

[('TV Show', 'The Lion King', ['Connie Budai', 'Mwayi Lee', 'Wayan Nielsen', 'Uchenna Garfield','Jianping Martinek', 'Jose Garfield', 'Jose Martinek'],['Chidiebere Stroman'], (2019, 4, 10)),('Movie', 'Eternal Sunshine of the Spotless 'Dada Gereben', 'Kanta Nielsen', 'Wambli Martinek', 'Xia Lee',
  'Wambli Budai', 'Jose Blum', 'Jing Lee'],
 ['Xia Stroman', 'Badr MacAoidh', 'Neo MacAoidh', 'Wayan Stroman',
  'Kanta Scriven', 'Bob Bryan'], (2001, 5, 2)),
 ('Movie', 'The Walking Dead', ['Jie MacAoidh'], 
 ['Badr Blum', 'Jose Gereben', 'Xia Budai', 'Shandiin Scriven'], (2007, 11, 17)),
 ('TV Show', 'The Dark Knight', 
 ['Wayan Budai', 'Xia Kennedy', 'Mwayi Garfield', 'Connie Smith'],
 ['Badr Nielsen', 'Mwayi Blum', 'Chidiebere Berardi', 'Nur Koenig',
  'Chidiebere Blum'], (2017, 4, 19)),
 ('TV Show', 'Inception', ['Dada Stroman', 'Mwayi Alserda'], 
 ['Bob Scriven', 'Jing Alserda', 'Wayan Stroman', 'Connie Martinek',
  'Jianping Stroman', 'Michele Budai', 'Jianping Nielsen'], (2022, 7, 5))]'''


list1 = [2,0,2,3,2]
list1 += [90]
print(list1)

