from main.python.helpers.HelpMethods import HelpMethods
from main.python.helpers.DataTest import array

"""

Find the difference between its maximum and minimum elements in array

"""

difference = HelpMethods.find_min_max_integer_range(array)

print(f"{difference=}")

if difference == 49:
    assert True
    print(f"\nTest passed! The difference between the max and min is: {difference}")
else:
    assert False, f"Test failed! The maximum number is: {difference}"