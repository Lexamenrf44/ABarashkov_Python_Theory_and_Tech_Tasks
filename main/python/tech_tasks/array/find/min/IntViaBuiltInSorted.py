from main.python.helpers.DataTest import array

"""

Find maximum value in array via built in sorted()

"""

print(f"Max value: {sorted(array)[0]}")

min_value = sorted(array)[0]

if min_value == -40:
    assert True
    print(f"Test passed! The maximum number is: {min_value}")
else:
    assert False, f"Test failed! The maximum number is: {min_value}"
