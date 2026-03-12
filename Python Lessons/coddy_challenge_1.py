# operators_list = ['+', '-', '/', '*']
#
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# op = input("Enter the operator (+, -, /, *): ")
# result = 0
#
# while op not in operators_list:
#     op = input("Enter the operator (+, -, /, *): ")
#
# if op == '+':
#     result = n1 + n2
# elif op == '-':
#     result = n1 - n2
# elif op == '/':
#     resu':
#     result = nlt = n1 / n2
# # elif op == '*1 * n2
#
# print(f"result = {result}")

# print(bool("0"))
#
# variable_1 = False
# name_1 = "MIME"
# name_2 = "YIOTIS"
#
# names = name_1.lower() == "mime" and name_2 != "YIOTISS"
# print(names)

# import addition
# print(addition.__name__)
# print(addition.__file__)
# print(addition.__doc__)
#
# print(__name__)



integer = 19
div = 3
# print the integer division of int by div
# print(int / div) # for decimal divitions -> 6.3
# print(int // div) # for integer division -> 6
# print(int % div) # for integer division -> 1

import math
result = integer / div
print(result.__ceil__())
print(math.ceil(result))


number = 81
print(math.sqrt(number))
for i in range(1, number):
    if i * i == number:
        print(i)