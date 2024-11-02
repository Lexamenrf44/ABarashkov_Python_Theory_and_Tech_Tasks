from collections import Counter
from itertools import count
from typing import List


class HelpMethods:

    @staticmethod
    def find_count_with_condition(array: List[int], target: int) -> int:

        return sum(1 for num in array if num >= target)

    @staticmethod
    def find_min_max_integer_range(array):
        min_value = min(array)
        max_value = max(array)

        return max_value - min_value

    @staticmethod
    def find_repeated_characters_hash_map(s: str) -> dict:

        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        repeated_chars = {char: count for char, count in char_count.items() if count > 1}

        return repeated_chars


    @staticmethod
    def find_repeated_characters_collections_counter(s: str) -> dict:

        return {char: count for char, count in Counter(s).items() if count > 1}