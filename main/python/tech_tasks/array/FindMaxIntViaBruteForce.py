from main.python.helpers.HelpMethods import HelpMethods
from main.python.helpers.DataTest import array

"""

Find maximum value in array via brute force

"""

max_value = HelpMethods.find_max_brute_force(array)

if max_value == 9:
    assert True
    print(f"\nTest passed! The maximum number is: {max_value}")
else:
    assert False, f"Test failed! The maximum number is: {max_value}"
