from typing import List


class FindTwoSumMethods:

    @staticmethod
    def find_two_sum_indices_brute_force(nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:], start=i + 1):
                if num1 + num2 == target:
                    return [i, j]
        return []


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
    def find_two_sum_two_pointer_approach(nums: List[int], target: int) -> List[int]:

        l = 0
        n = len(nums)
        r = n - 1

        while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
                return [l + 1, r + 1]
            elif summ < target:
                l += 1
            else:
                r -= 1
        return []