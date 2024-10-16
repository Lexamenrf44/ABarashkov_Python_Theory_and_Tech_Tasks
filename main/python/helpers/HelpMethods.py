class HelpMethods:

    @staticmethod
    # Define a function named fizz_buzz_hardcoded
    # This will contain the logic for FizzBuzz with given parameters
    def fizz_buzz_hardcoded():

        # Loop through numbers from 0 to 50 (inclusive)
        for num in range(51):  # range(51) generates numbers from 0 to 50
            # Check if the number is a multiple of both 3 and 5
            if num % 3 == 0 and num % 5 == 0:  # Use modulus operator to check divisibility
                print("FizzBuzz")  # If true, print "FizzBuzz" for multiples of both 3 and 5
            # Check if the number is a multiple of 3 only
            elif num % 3 == 0:  # If not a multiple of both, check for multiple of 3
                print("Fizz")  # If true, print "Fizz" for multiples of 3
            # Check if the number is a multiple of 5 only
            elif num % 5 == 0:  # If not a multiple of both or 3, check for multiple of 5
                print("Buzz")  # If true, print "Buzz" for multiples of 5
            else:
                print(num)  # If none of the conditions are met, print the number itself

    @staticmethod
    # Define a function named fizz_buzz_parametrized
    # This will contain the logic for FizzBuzz with dynamic parameters
    def fizz_buzz_parametrized(start, end):

        # Loop through numbers from start to end (inclusive)
        for num in range(start, end + 1):  # Use the provided start and end values
            # Check if the number is a multiple of both 3 and 5
            if num % 3 == 0 and num % 5 == 0:  # Use modulus operator to check divisibility
                print("FizzBuzz")  # If true, print "FizzBuzz"
            # Check if the number is a multiple of 3 only
            elif num % 3 == 0:  # If not a multiple of both, check for multiple of 3
                print("Fizz")  # If true, print "Fizz"
            # Check if the number is a multiple of 5 only
            elif num % 5 == 0:  # If not a multiple of both or 3, check for multiple of 5
                print("Buzz")  # If true, print "Buzz"
            else:
                print(num)  # If none of the conditions are met, print the number itself