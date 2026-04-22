# 1. user inputs a number
# 2. the number is stored in a variable
# 3. the algorith takes this number/variable and convers it to binary
# 4. print the binary form of the number


# 1. get the number from the user
# 2. check that the input is an integer, if not print an error message and exit
# 3. apply the conversion from the given integer to binary
# 4. 7=111, 7/2 3 mod 1  2_1
# 3. print the result


# STEPS:
# 7/2 = 3 mod 1 -> 2_0 OUTPUT: 1
# 3/2 = 1 mod 1 -> 2_1 OUTPUT: 11
# 1/2 = 0 mod 1 -> 2_2 OUTPUT: 111
#
#
# 5/2 = 2 mod 1 -> 2_0 OUTPUT: 1
# 2/2 = 1 mod 0 -> 2_1 OUTPUT: 01
# 1/2 = 0 mod 1 -> 2_2 OUTPUT: 101
#
# input = 5
# remaining = input 5
# binary = ""
#
# while remaining != 0:			5	2   1
# 	remaining % 2 = suffix      1   0   1
# 	remaining / 2 = remaining   2   1   0
# 	output = suffix + output    1   01  101



input = input("Enter an integer to convert to binary: ")
remaining = int(input)
output = ""

while remaining != 0:
    suffix = remaining % 2
    remaining = remaining // 2
    output = str(suffix) + output

print(output)