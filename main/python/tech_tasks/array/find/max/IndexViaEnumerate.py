from main.python.helpers.DataTest import array

"""

Find index of maximum value in array via enumerate()

"""

def IndexViaEnumerate(array):

    return max(enumerate(array), key=lambda x: x[1])[0]

print(f"Index of max value: {IndexViaEnumerate(array)}")

max_index = IndexViaEnumerate(array)

if max_index == 6:
    assert True
    print(f"Test passed! The index of maximum value is: {max_index}")
else:
    assert False, f"Test failed! The index of maximum value is: {max_index}"