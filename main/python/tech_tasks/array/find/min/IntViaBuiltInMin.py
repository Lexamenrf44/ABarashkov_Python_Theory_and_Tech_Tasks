from main.python.helpers.DataTest import array

def IntViaBuiltInMin(array):

    return min(array)

print(f"Min value: {IntViaBuiltInMin(array)}")

min_value = IntViaBuiltInMin(array)

if min_value == -1:
    assert True
    print(f"Test passed! The minimum number is: {min_value}")
else:
    assert False, f"Test failed! The minimum number is: {min_value}"