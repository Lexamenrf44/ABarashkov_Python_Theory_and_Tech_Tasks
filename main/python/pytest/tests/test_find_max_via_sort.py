import pytest

from main.python.helpers.DataTest import array

"""

Find maximum value in array using sort

"""

def test_find_max_via_sort():

    # Sort the array in ascending order
    array.sort()

    max_value = array[-1]

    # Assert results and print if passed/failed
    assert max_value == 9, f"Test failed! The maximum number is: {max_value}"

    print(f"\n\nTest passed! The maximum number is: {max_value}")