from collections import Counter


class HelpMethods:

    @staticmethod
    def find_max_int_brute_force(array):
        max_value = array[0]
        for num in array:
            if num > max_value:
                max_value = num
        return max_value


    @staticmethod
    def calculate_array_difference(array):
        index_of_minimum = min(array)
        index_of_maximum = max(array)

        return index_of_maximum - index_of_minimum

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