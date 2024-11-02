from main.python.helpers.DataTest import array

"""

Find maximum value in array via built in max()

"""

def IntViaBuiltInMax(array):

    return max(array)

print(f"Max value: {IntViaBuiltInMax(array)}")

max_value = IntViaBuiltInMax(array)

if max_value == 9:
    assert True
    print(f"Test passed! The maximum number is: {max_value}")
else:
    assert False, f"Test failed! The maximum number is: {max_value}"