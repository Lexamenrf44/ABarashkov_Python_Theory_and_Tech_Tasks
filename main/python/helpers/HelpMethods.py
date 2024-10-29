from typing import List

class HelpMethods:

    @staticmethod
    # Function for fizz buzz with hardcoded elements within
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
    # Function for fizz buzz with parametrized elements
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
    # Function to find
    def find_two_sum_indices_hash_map(nums, target):

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
    def find_two_sum_indices_brute_force(nums: List[int], target: int) -> List[int]:

        n = len(nums)

        # Loop through each pair of indices in the list
        for i in range(n):
            for j in range(i + 1, n):  # Start j from i + 1 to avoid using the same element twice
                if nums[i] + nums[j] == target:  # Check if the current pair sums to the target
                    return [i, j]  # Return the indices of the two numbers

        # Return None if no solution is found
        return []

    @staticmethod
    def find_two_sum_two_pointer_approach(numbers: List[int], target: int) -> List[int]:

        # `l` starts at the beginning of the list (left pointer)
        l = 0

        # `n` stores the length of the numbers list for easy reference
        n = len(numbers)

        # `r` starts at the end of the list (right pointer)
        r = n - 1

        # Continue the loop as long as the left pointer is less than the right pointer
        while l < r:
            # Calculate the sum of the elements at the two pointers
            summ = numbers[l] + numbers[r]

            # Check if the sum is equal to the target
            if summ == target:
                # If so, return the indices of the two numbers (1-based index)
                return [l + 1, r + 1]

            # If the sum is less than the target, move the left pointer to the right to increase the sum
            elif summ < target:
                l += 1

            # If the sum is greater than the target, move the right pointer to the left to decrease the sum
            else:
                r -= 1

        # If no pair is found that sums to the target, return an empty list
        return []


    @staticmethod
    # Function to find the maximum value in the array
    def find_max_brute_force(array):
        max_value = array[0]  # Assume the first element is the largest for now

        # Loop through the rest of the array
        for i in range(1, len(array)):
            # Check if the current element is greater than the current max
            if array[i] > max_value:
                max_value = array[i]  # Update max if we found a bigger number

        return max_value  # Return the largest number found

    @staticmethod
    # Function to find the difference between maximum and minimum elements in the array
    def calculate_array_difference(array):
        # Initialize the indices of minimum and maximum elements
        index_of_minimum = 0
        index_of_maximum = 0

        # Traverse the array to find indices of the minimum and maximum values
        for i in range(1, len(array)):
            # Check if the current element is smaller than the current minimum
            if array[i] < array[index_of_minimum]:
                index_of_minimum = i

            # Check if the current element is greater than the current maximum
            if array[i] > array[index_of_maximum]:
                index_of_maximum = i

        # Return the difference between the maximum and minimum values
        return array[index_of_maximum] - array[index_of_minimum]