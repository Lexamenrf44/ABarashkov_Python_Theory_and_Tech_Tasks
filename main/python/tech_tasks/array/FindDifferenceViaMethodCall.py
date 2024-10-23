from main.python.helpers.HelpMethods import HelpMethods
from main.python.helpers.DataTest import array

"""

Find the difference between its maximum and minimum elements in array calling a method

"""

# Call the function method to find max int value
difference = HelpMethods.calculate_array_difference(array)

# Assert results and print if passed / failed
if difference == 8:
    assert True
    print(f"Test passed! The difference between the max and min is: {difference}")
else:
    assert False, f"Test failed! The maximum number is: {difference}"