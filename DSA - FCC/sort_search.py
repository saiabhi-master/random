# bogo sort is the worst sorting operation - random sorts until correct
import random

numbers = [8, 4, 5, 3, 9, 5, 3, 7, 0]

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index -1]:
            return False
    return True
#---------------------------------
#randomly shuffles until sorted
def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    print(attempts)
    return values
#---------------------------------
def selection_sort(values):
    """
    technical run time is O(1/2 n^2)
    but large data sets ==> take out constants
    """
    sorted_list = []

    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
#---------------------------------
# recursive function
def sum(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + remaining_sum
#---------------------------------
def quicksort(values):
    """
    best case: O(n log n ) &
    worst case: O(n^2) - reversed ordered list as input
    """

    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
#---------------------------------
# Tells you number of times an operation is performed
# Doesn't describe duration of operation
# A useful tool for quickly describing how the run time of an algorithm increases
# as the data set its get big
#---------------------------------




