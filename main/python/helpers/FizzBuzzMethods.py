from itertools import count, islice


class FizzBuzzMethods:
    @staticmethod
    def fizz_buzz_iteration_conditional_loop_approach_hardcoded():
        for num in range(51):                  # Loop through numbers from 0 to 50 (inclusive)
            if num % 3 == 0 and num % 5 == 0:  # Check if the number is a multiple of both 3 and 5
                print("FizzBuzz")              # If true, print "FizzBuzz" for multiples of both 3 and 5
            elif num % 3 == 0:                 # Check if the number is a multiple of 3 only
                print("Fizz")                  # If true, print "Fizz" for multiples of 3
            elif num % 5 == 0:                 # Check if the number is a multiple of 5 only
                print("Buzz")                  # If true, print "Buzz" for multiples of 5
            else:
                print(num)                     # If none of the conditions are met, print the number itself


    @staticmethod
    def fizz_buzz_iteration_conditional_loop_approach_parametrized(start, end):
        for num in range(start, end + 1):      # Loop through numbers from start to end (inclusive)
            if num % 3 == 0 and num % 5 == 0:  # Check if the number is a multiple of both 3 and 5
                print("FizzBuzz")              # If true, print "FizzBuzz"
            elif num % 3 == 0:                 # Check if the number is a multiple of 3 only
                print("Fizz")                  # If true, print "Fizz"
            elif num % 5 == 0:                 # Check if the number is a multiple of 5 only
                print("Buzz")                  # If true, print "Buzz"
            else:
                print(num)                     # If none of the conditions are met, print the number itself

    @staticmethod
    def fizz_buzz_functional_programming_hardcoded():
        results = [                          # Use a list comprehension to generate results
            "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
            "Fizz" if num % 3 == 0 else
            "Buzz" if num % 5 == 0 else
            str(num)
            for num in islice(count(0), 51)  # Generate numbers from 0 to 50
        ]

        print("\n".join(results))            # Print all results joined by newlines