from main.python.helpers.HelpMethods import HelpMethods
from main.python.helpers.DataTest import array

"""

Find maximum value in array calling a method

"""

# Call the function method to find max int value
max_value = HelpMethods.find_max_brute_force(array)

# Assert results and print if passed / failed
if max_value == 9:
    assert True
    print(f"Test passed! The maximum number is: {max_value}")
else:
    assert False, f"Test failed! The maximum number is: {max_value}"
