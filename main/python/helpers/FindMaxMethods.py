class FindMaxMethods:

    @staticmethod
    def find_max_int_brute_force(array):
        max_value = array[0]
        for num in array:
            if num > max_value:
                max_value = num
        return max_value