from main.python.helpers.FindMaxMethods import FindMaxMethods
from main.python.helpers.DataTest import array

"""

Find maximum value in array via brute force

"""

max_value = FindMaxMethods.find_max_int_brute_force(array)

if max_value == 9:
    assert True
    print(f"\nTest passed! The maximum number is: {max_value}")
else:
    assert False, f"Test failed! The maximum number is: {max_value}"
