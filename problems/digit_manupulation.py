# 17
def remove_digit(num, digit):
    output = 0
    base_multiplier = 1
    while num != 0:
        suffix = num % 10 # get the last digit of the number
        num = num // 10 # remove the last digit from the number

        if suffix != digit:
            output = output + suffix * base_multiplier # add the digit in its correct decimal position
            base_multiplier = base_multiplier * 10 # move to the next decimal place
    return output

print(remove_digit(67384613, 6))  #  => 738413