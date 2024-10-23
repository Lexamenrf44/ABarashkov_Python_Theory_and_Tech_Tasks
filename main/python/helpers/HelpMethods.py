class HelpMethods:

    @staticmethod

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

    @staticmethod
    # Define a function named find_two_sum
    # This will contain the logic for find_two_sum
    def find_two_sum_by_index(nums, target):
        """

        Find two indices of numbers in nums that add up to the target.
        :param nums: List[int] - List of integers
        :param target: int - Target sum
        :return: List[int] - Indices of the two numbers that add up to target

        """
        # Create a dictionary to store the number and its index
        num_map = {}  # Dictionary to store number and its index

        # Loop through the array
        for i in range(len(nums)):  # Loop through each index in nums
            complement = target - nums[i]  # Calculate the complement (target - current number)

            # Check if the complement exists in the map
            if complement in num_map:  # If the complement is found in the dictionary
                # If complement exists, return its index and the current index
                return [num_map[complement], i]  # Return the indices of the two numbers

            # If complement does not exist, store the current number and its index in the map
            num_map[nums[i]] = i  # Store the current number and its index

        # Return an empty list if no solution is found (shouldn't happen given problem constraints)
        return None

    @staticmethod
    def find_max_brute_force(array):
        max_value = array[0]  # Assume the first element is the largest for now

        # Loop through the rest of the array
        for i in range(1, len(array)):
            # Check if the current element is greater than the current max
            if array[i] > max_value:
                max_value = array[i]  # Update max if we found a bigger number

        return max_value  # Return the largest number found