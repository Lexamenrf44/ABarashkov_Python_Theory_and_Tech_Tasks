from main.python.helpers.HelpMethods import HelpMethods

input_string = "Hello World"

repeated_characters = HelpMethods.find_repeated_characters_collections_counter(input_string)

if repeated_characters:
    print("Repeated characters and their counts:", repeated_characters)
else:
    print("No repeated characters found.")