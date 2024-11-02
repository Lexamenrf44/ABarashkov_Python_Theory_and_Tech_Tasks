from main.python.helpers.HelpMethods import HelpMethods
from main.python.helpers.DataTest import array

"""

Find the count that met to target from array

"""

target = 4

count = HelpMethods.find_count_with_condition(array, target)

if target == 4:
    assert True
    print(f"\nTest passed! The number of integers met to target: {count}")
else:
    assert False, f"Test failed! The number of integers met to target: {count}"
