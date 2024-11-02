from itertools import count, islice


class FizzBuzzMethods:

    @staticmethod
    def fizz_buzz_iteration_conditional_loop_approach_hardcoded():
        for num in range(51):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)


    @staticmethod
    def fizz_buzz_iteration_conditional_loop_approach_parametrized(start, end):
        for num in range(start, end + 1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)


    @staticmethod
    def fizz_buzz_functional_programming_hardcoded():
        results = [
            "FizzBuzz" if num % 3 == 0 and num % 5 == 0 else
            "Fizz" if num % 3 == 0 else
            "Buzz" if num % 5 == 0 else
            str(num)
            for num in islice(count(0), 51)
        ]

        print("\n".join(results))