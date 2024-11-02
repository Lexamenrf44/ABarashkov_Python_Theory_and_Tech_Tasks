"""

Write username input algorithm

"""

user_input = input('Enter username: ')

if user_input:
    name = user_input
else:
    name = 'N/A'

print(f"Your username is {name}")