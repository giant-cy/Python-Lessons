# {"":""} = DICT
# {} = SET - unique items
# () = TUPLE
# [] = LIST


import addition


# addition("123","456")
# print(addition.__name__)




# TEST_CASES = [
#     # basic
#     ([2, 7, 11, 15], 9, (2, 7)),
#     # unordered input
#     ([3, 2, 4], 6, (2, 4)),
#     # negatives
#     ([-3, 4, 3, 90], 0, (-3, 3)),
#     # duplicates
#     ([3, 3], 6, (3, 3)),
#     # zero values
#     ([0, 4, 3, 0], 0, (0, 0)),
#     # larger numbers
#     ([1000000, 500000, -500000], 500000, (1000000, -500000)),
#     # single element (no solution)
#     ([5], 5, None),
#     # empty list
#     ([], 10, None),
#     # no match
#     ([1, 2, 3, 4], 100, None),
# ]
#
#
# def find_number(list_of_integers, sum_number):
#     for index,item in enumerate(list_of_integers):
#         for index2,item2 in enumerate(list_of_integers):
#             if index != index2:
#                 if item + item2 == sum_number:
#                     return item, item2
#     return None
#
#
# def test_logic(test_list, test_sum, expected_numbers):
#     output = find_number(test_list, test_sum)
#     print(test_list, output, expected_numbers)
#     assert output == expected_numbers
#     print("DONE")
#
#
# for item in TEST_CASES:
#     test_logic(*item)


# if __name__ == "__main__":
#     pass


# import sys
# x = 42
# print(sys.getsizeof(x))
#
#
#
# test = "asasa".capitalize()


var_int = ""
print(bool(var_int))


var_int = "12"
print(int(var_int))