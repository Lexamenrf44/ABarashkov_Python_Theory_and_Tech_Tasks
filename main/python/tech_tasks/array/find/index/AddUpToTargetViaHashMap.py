from main.python.helpers.FindTwoSumMethods import FindTwoSumMethods
from main.python.helpers.DataTest import array

"""

Find indices that add up to the target value via hash map.

"""

target = 9

result = FindTwoSumMethods.find_two_sum_indices_hash_map(array, target)

if result:
    print(f"\nTest passed! The indices are: {result}")
else:
    assert False, f"Test failed! Could not find indices for target: {target}"