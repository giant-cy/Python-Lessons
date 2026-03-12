# Find the smallest power of 2 that is greater than a given number.
#
# To solve it we will use a while loop that will repeatedly multiply
# the current power of 2 by 2 until it becomes greater than the given number:


# # 1,2,4,8,16
# input_number = int(input("Give number:"))
# result = 1
#
# for i in range(input_number+1):
#     print(result)
#     result = 2*result

input_number = int(input("Give number:"))
inter = 0
result = 1
while input_number >= result:
    result = 2*result
    inter += 1
print(f"2**{inter}=", result)
