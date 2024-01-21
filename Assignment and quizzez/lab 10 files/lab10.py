import doctest
from student import Student

def get_students(filename: str) -> list[str]:
    """ Reads a file and makes an object which is then added to the list
    >>> get_students('empty.txt')
    []
    >>> get_students('student_data.csv')
    [Student('V00123456', '89'), Student('V00123457', '99'), Student('V00123458', '30'), Student('V00123459', '78')]
    """
    result_list = []
    file_handle = open(filename, 'r')
    for line in file_handle:
        line = line.strip()
        std_id, grade = line.split(',')
        std_obj = Student(std_id, grade)
        result_list.append(std_obj)
    file_handle.close()
    return result_list

def get_classlist(student_lst: list[Student]) -> list[str]:
    """
    >>> empty_list = []
    >>> new_list = [Student('V00123456', '89'), Student('V00123457', '99'), Student('V00123458', '30'), Student('V00123459', '78')]
    >>> get_classlist(empty_list)
    []
    >>> get_classlist(new_list)
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']
    """
    new_list = []
    for std_object in student_lst:
        student_id = std_object.get_sid()
        new_list.append(student_id)
    return new_list

def count_above(student_lst: list[Student], threshold_grade: int) -> int:
    """
    >>> empty_list = []
    >>> new_list = [Student('V00123456', '89'), Student('V00123457', '99'), Student('V00123458', '30'), Student('V00123459', '78')]
    >>> count_above(empty_list, 50)
    0
    >>> count_above(new_list, 82)
    2
    """
    count = 0
    for std_object in student_lst:
        student_grade = std_object.get_grade()
        if int(student_grade) > threshold_grade:
            count += 1
    return count

def get_average_grade(student_lst: list[Student]) -> float:
    """
    >>> empty_list = []
    >>> new_list = [Student('V00123456', '89'), Student('V00123457', '99'), Student('V00123458', '30'), Student('V00123459', '78')]
    >>> get_average_grade(empty_list)
    0
    >>> get_average_grade(new_list)
    74.0
    """
    total = 0
    count = 0
    for student_instance in student_lst:
        student_grade = student_instance.get_grade()
        total += int(student_grade)
        count += 1
    average = (total / count)
    return average