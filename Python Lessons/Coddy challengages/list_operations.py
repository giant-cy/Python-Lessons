import math

# def reverse_list(list_input):
#     for i in range(math.floor(len(list_input)/2)):
#         list_input[i], list_input[-1-i] = list_input[-1-i], list_input[i]
#     print(list_input)
#
# reverse_list([1,2,3,4,5,6,7,8,9])







# def find(provided_list, find_value):
#     # counter = 0
#     # for i in provided_list:
#     #     if i == find_value:
#     #         return counter
#     #     counter += 1
#     # return -1
#     for i in range(len(provided_list)):
#         if provided_list[i] == find_value:
#             return i
#     return -1
#
#
#
#
# print(find([1,2,3,4,5,6],5))






# Intuition (simple mental model)
#
# Imagine numbers as bubbles:
#
# Bigger numbers are “heavier bubbles”
# Each pass pushes the biggest one to the end
# After each pass, one more element is in the correct place
# Step-by-step example
#
# Start with:
#
# [5, 2, 9, 1]
#
# Pass 1:
#
# Compare 5 and 2 → swap → [2, 5, 9, 1]
# Compare 5 and 9 → ok
# Compare 9 and 1 → swap → [2, 5, 1, 9]
# 👉 Now 9 is in the correct final position
#
# Pass 2:
#
# Compare 2 and 5 → ok
# Compare 5 and 1 → swap → [2, 1, 5, 9]
# 👉 Now 5 is in the correct position
#
# Pass 3:
#
# Compare 2 and 1 → swap → [1, 2, 5, 9]
# 👉 Sorted
# Key points to emphasize
# We only compare adjacent elements
# We swap if they are in the wrong order
# Each pass guarantees:
# the largest remaining element moves to the end
# We stop early if no swaps happen


# def is_palidrome_list(list_input):
#     for i in range(math.floor(len(list_input)/2)):
#         if list_input[i] != list_input[-1-i]:
#             return "not palidrome"
#     return "palidrome"
# print(is_palidrome_list([1,2,3,2,1]))

# # # find the
# def bubble_sort_list(provided_list):
#
#     for i in range(len(provided_list)):
#         swapped = False
#         for j in range(0, len(provided_list) - i - 1):
#             if provided_list[j] > provided_list[j+1]:
#                 provided_list[j], provided_list[j+1] = provided_list[j+1], provided_list[j]
#                 swapped=True
#             print(i , j)
#         if not swapped:
#             break
#     return provided_list

#42, 7, 19, 102, 33, 8, 54
#7, 42, 19, 102, 33, 8, 54
#7, 19, 42, 102, 33, 8, 54

# print(sort_list([42, 7, 19, 102, 33, 8, 54]))
# print(sort_list([3,1,5,2]))
# print(sort_list([9, 3, 1, 4, 1, 5, 9, 2, 6, 5]))
# print(sort_list([1002, 543, 21, 99, 8, 765]))
# print(sort_list([0, -15, 22, -3, 40, -100, 5]))
# print(sort_list([12, 12, 11, 13, 5, 6, 7]))
# print(sort_list([88, 24, 65, 13, 91, 47, 2, 36]))
# print(sort_list([10, 20, 30, 40, 50]))
# print(sort_list([5, 4, 3, 2, 1]))
# print(sort_list([999, 111, 444, 222, 888, 333]))
# print(sort_list([7, 14, 21, 28, 35, 42, 49]))



# def find_min(provided_list):
#     min_number = provided_list[0]
#     for i in range(len(provided_list)):
#         if provided_list[i] < min_number:
#             min_number = provided_list[i]
#     return min_number
#
# print(find_min([42, 7, 19, 102, 33, 8, 54]))
# print(find_min([3,1,5,2]))
# print(find_min([9, 3, 1, 4, 1, 5, 9, 2, 6, 5]))
# print(find_min([1002, 543, 21, 99, 8, 765]))
# print(find_min([0, -15, 22, -3, 40, -100, 5]))
# print(find_min([12, 12, 11, 13, 5, 6, 7]))
# print(find_min([88, 24, 65, 13, 91, 47, 2, 36]))
# print(find_min([10, 20, 30, 40, 50]))
# print(find_min([5, 4, 3, 2, 1]))
# print(find_min([999, 111, 444, 222, 888, 333]))
# print(find_min([7, 14, 21, 28, 35, 42, 49]))

# def selection_sort_list(provided_list):
#     n = len(provided_list)
#     for i in range(n):
#         min_value = provided_list[i]
#         for j in range(n):
#             if min_value < provided_list[j]:
#                 provided_list.pop(i)
#                 provided_list.insert(j, min_value)
#                 break
#         print(provided_list)
#     return provided_list



# def selection_sort_list(provided_list):
#     n = len(provided_list)
#     for i in range(n-1):
#         min_value = provided_list[i]
#         min_value_index = i
#         for j in range(i+1, n):
#             if min_value > provided_list[j]:
#                 min_value = provided_list[j]
#                 min_value_index = j
#         provided_list.pop(min_value_index)
#         provided_list.insert(i, min_value)
#     return provided_list
#
# print(selection_sort_list([42, 7, 19, 102, 33, 8, 54]))
# print(selection_sort_list([3,1,5,2]))
# print(selection_sort_list([9, 3, 1, 4, 1, 5, 9, 2, 6, 5]))
# print(selection_sort_list([1002, 543, 21, 99, 8, 765]))
# print(selection_sort_list([0, -15, 22, -3, 40, -100, 5]))
# print(selection_sort_list([12, 12, 11, 13, 5, 6, 7]))
# print(selection_sort_list([88, 24, 65, 13, 91, 47, 2, 36]))
# print(selection_sort_list([10, 20, 30, 40, 50]))
# print(selection_sort_list([5, 4, 3, 2, 1]))
# print(selection_sort_list([999, 111, 444, 222, 888, 333]))
# print(selection_sort_list([7, 14, 21, 28, 35, 42, 49]))



# def find_indices(numbers, sum):
#     n = len(numbers)
#     for i in range(n):
#         for j in range(i+1, n):
#             print(i, j)
#             if numbers[i]+numbers[j] == sum:
#                 return i,j
#     return "NO NUMBERS"
#
#
# # print(find_indices([2, 9, 11, 15], 24))
# print(find_indices([12, 5, 7], 17))
# # → [0, 1])
#
#
# def max_sliding_window(numbers, window):
#     result = []
#     for i in range(len(numbers) - window + 1):
#         result.append(numbers[i])
#     return result
#
# # Given a list of integers and a window size k, return a list of the maximum value in each sliding window.
# print(max_sliding_window([1], 1))     # → [1]
# print(max_sliding_window([9,8,7,6,8,4,6], 3))  # → [9,8,7,6,8]
# print(max_sliding_window([1,1,1,1], 2))  # → [1,1,1]

#
# def binary_search(number:list, item: int):
#     low = 0
#     high = len(number) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if number[mid] == item:
#             return mid
#         elif number[mid] < item:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
#
# print(binary_search([1,2,3,4,5], 1))   # 0 (first element)
# print(binary_search([1,2,3,4,5], 5))   # 4 (last element)
# print(binary_search([1,2,3,4,5], 10))  # -1 (not found)
# print(binary_search([10,20,30,40,50,60,70], 40))  # 3 (middle)
# print(binary_search([7], 7))           # 0 (single element)
# print(binary_search([], 3))            # -1 (empty list)

# Initialize:
# low = 0
# high = len(A) - 1
# While low <= high:
# Compute middle index:
# mid = low + (high - low) // 2
# (avoids overflow vs (low + high) // 2)
# Compare:
# If A[mid] == target → return mid
# If A[mid] < target → search right half:
# low = mid + 1
# Else → search left half:
# high = mid - 1
# If loop ends → target not found → return -1




def reverse(lst):
    n = len(lst)
    for i in range(n//2):
        lst[i],lst[-1-i] = lst[-1-i], lst[i]
    print(lst)
    # print(lst[::-1])

reverse([1, 2, 3, 4])