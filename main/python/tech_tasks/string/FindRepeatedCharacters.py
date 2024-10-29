from main.python.helpers.HelpMethods import HelpMethods

input_string = "Hello World"

# Call the method to find repeated characters
repeated_characters = HelpMethods.find_repeated_characters(input_string)

# Print the results
if repeated_characters:
    print("Repeated characters and their counts:", repeated_characters)
else:
    print("No repeated characters found.")