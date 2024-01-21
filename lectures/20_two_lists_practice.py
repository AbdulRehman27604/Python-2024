import doctest


'''
Q0. Complete the function below from last lecture.
'''

def zip_longer(list1: list[int], list2: list[int], fill_val: int
               ) -> list[tuple[int, int]]:
    """ creates and returns a list of tuples for pairs across list1 and list2,
    fills missing values with fill_val
    >>> zip_longer([], [], 2)
    []
    >>> zip_longer([2, 3, 4], [], 1000)
    [(2, 1000), (3, 1000), (4, 1000)]
    >>> zip_longer([], [5, 6, 7], 1)
    [(1, 5), (1, 6), (1, 7)]
    >>> zip_longer([8, 9, 10], [5, 6, 7], 1)
    [(8, 5), (9, 6), (10, 7)]
    >>> zip_longer([8, 9, 10], [5, 6], 2)
    [(8, 5), (9, 6), (10, 2)]
    >>> zip_longer([8, 9], [5, 6, 7], 2)
    [(8, 5), (9, 6), (2, 7)]
    """
    new_list = []
    len1 = len(list1)
    len2 = len(list2)
    repetation = max(len1,len2)
    for index in range(repetation):
        if index <= len1:
            first = list1[index]
        else:
            first = fill_val
        if index <= len2:
            second = list1[index]
        else:
            second = fill_val
        pair = (first, second)
        new_list.append(pair)
    return new_list



'''
Q1. Design a function that will take two lists of integers
that are in increasing order. The function should
create and return a list of all the values from list1 and list2
in sorted order
ie. if the function is called with [2, 10], [5, 6, 11]
the function should return [2, 5, 6, 10, 11]
'''
def sort_lists(list1: list[int], list2: list[int]) -> list:
    """
    returns sorted list of elements from list1 and list2 
    precondition: list1 and list2 are sorted
    >>> sort_lists([],[])
    []
    >>> sort_lists([2, 10],[])
    [2, 10]
    >>> sort_lists([],[5,6,11])
    [5, 6, 11]
    >>> sort_lists([2,10],[5,6,11])
    [2, 5, 6, 10, 11]
    """
    result_list = []
    index1 = 0
    index2 = 0
    len1 = len(list1)
    len2 = len(list2)
    
    while index1 < len1 and index2 < len2:
        if list1[index1] > list2[index2]:
            result_list.append(list2[index2])
            index2 += 1
        else:
            result_list.append(list1[index1])
            index1 += 1
    if index1 != len1:
        for i in range(index1,len1):
            result_list.append(list1[i])
    elif index2 != len2:
        for x in range(index2,len2):
            result_list.append(list2[x])
        
    return result_list


    
'''
Q2. Design a function that will sort a given list of integers.
The function should use a selection sort algorithm:
for each position in the given list,
-finds the position of the smallest value between 
the current position and the end of the list
-swaps the values at the current position and
the position of the smallest value
NOTE: this function will mutate the list
TIP: use the functions you wrote in lab as helper functions
'''



'''
Q3. Design a function that takes 2 lists of integers and determines whether the
first list is strictly contained in the second list.
You should not need a nested loop to solve this problem.
For example,
[1, 4, 3] is contained in [1, 1, 4, 3]
[1, 4, 3] is not contained in [1, 1, 4, 4, 3]
'''

def bubble_sort(Array: list[int]) -> list:
    swap = False
    boundry = len(Array) - 1
    while not swap:
        swap = True
        for count in range(boundry):
            if Array[count] > Array[count + 1]:
                temp = Array[count]
                Array[count] = Array[count + 1]
                Array[count + 1] = temp
            swap = False
        boundry -= 1
    return Array
print(bubble_sort([34,776,12,2,90,4,3]))