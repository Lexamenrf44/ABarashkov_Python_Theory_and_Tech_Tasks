from typing import List, Optional, Tuple


class FindTwoSumMethods:

    @staticmethod
    def find_two_sum_indices_brute_force(nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:], start=i + 1):
                if num1 + num2 == target:
                    return [i, j]
        return []


    @staticmethod
    def find_two_sum_integers_brute_force(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:], start=i + 1):
                if num1 + num2 == target:
                    return (num1, num2)
        return None


    @staticmethod
    def find_two_sum_indices_hash_map(nums, target):

        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        return None


    @staticmethod
    def find_two_sum_integers_hash_map(nums: List[int], target: int) -> Optional[Tuple[int, int]]:

        num_map = {}

        for num in nums:
            complement = target - num
            if complement in num_map:
                return complement, num
            num_map[num] = True
        return None


    @staticmethod
    def find_two_sum_two_pointer_approach(nums: List[int], target: int) -> List[int]:

        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []