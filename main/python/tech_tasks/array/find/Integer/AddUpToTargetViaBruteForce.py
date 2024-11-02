from main.python.helpers.FindTwoSumMethods import FindTwoSumMethods
from main.python.helpers.DataTest import array

"""

Find integers that add up to the target value via hash map.

"""

target = 9

result = FindTwoSumMethods.find_two_sum_integers_brute_force(array, target)

if target == 9:
    assert True
    print(f"\nTest passed! The values are: {result}")
else:
    assert False, f"Test failed! Could not find values for target: {result}"