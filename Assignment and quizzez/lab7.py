import doctest
Flight_Info = tuple[str,str,float] 


#Q1
def swap(cad: list[int],pos_1: int, pos_2: int) -> None:
    """
    empties the first variable to temperory variable and then put the value of 
    second variable in to the first variable and finally empties the temp value 
    to the second varible.
    >>> line = [2,3,4,5]
    >>> swap(line,1,3)
    [2,5,4,3]
    """
    if cad != []:
        temp = cad[pos_1]
        cad[pos_1] = cad[pos_2]
        cad[pos_2] = temp

#Q2    
def index_of_smallest(Array: list) -> int:
    """
    >>> index_of_smallest([])
    -1
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'a'])
    0
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'A'])
    4
    >>> index_of_smallest([90, 87, 34, 45, 50, 34])
    2
    """
    pos = 0
    lenght = len(Array)
    if Array != []:
        value = min(Array)
        while pos < lenght and Array[pos] != value:
            pos += 1
        return pos
    return -1
    
#Q4      
hour = 2    
def total_duration(Array: list[tuple]) -> float:
    """
    >>> total_duration([])
    0
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    """
    total_hours = 0
    if Array != []:
        for cur_tuple in Array:
            total_hours += cur_tuple[hour]
    return total_hours

#Q5
from_city = 0
to_city = 1
def get_destinations_from(line: list[tuple], depature_city: str) -> list:
    """
    >>> get_destinations_from([],'Karachi')
    []
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)],'Victoria')
    ['Vancouver', 'Calgary']
    """
    new_list = []
    found = False
    if line != []:
        for city in line:
            if city[from_city] == depature_city:
                for appended_cities in new_list:
                    if appended_cities == city[to_city]:
                        found = True
                if found == False:
                    new_list.append(city[to_city])
    return new_list
                     

        
            
    
