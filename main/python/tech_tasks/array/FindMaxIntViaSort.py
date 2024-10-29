from main.python.helpers.DataTest import array

"""

Find maximum value in array via sort

"""

array.sort()

max_value = array[-1]

if max_value == 10:
    assert True
    print(f"Test passed! The maximum number is: {max_value}")
else:
    assert False, f"Test failed! The maximum number is: {max_value}"