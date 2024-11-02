from main.python.helpers.HelpMethods import HelpMethods
from main.python.helpers.DataTest import array

"""

Find minimum value in array via brute force

"""

def find_min_int_brute_force_with_pass(array):

    min_value = array[0]

    for num in array:
        if num < min_value:
            min_value = num

    print("Minimum value:", {min_value})

    pass

find_min_int_brute_force_with_pass(array)
