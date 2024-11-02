from main.python.helpers.DataTest import array

print(f"This is what unsorted array looks like: {array}")

array.sort()

print(f"This is what sorted array looks like: {array}")

max_value = array[-1]

if max_value == 9:
    assert True
    print(f"Test passed! Maximum value is: {max_value}")
else:
    assert False, f"Test failed! The maximum number is: {max_value}"