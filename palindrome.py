input_integer = input("Enter an integer to convert to binary: ")
remaining = int(input_integer)
output = 0

while remaining != 0:
    suffix = remaining % 10
    remaining = remaining // 10
    output = output*10 + suffix

print(output)
print(input_integer == output)