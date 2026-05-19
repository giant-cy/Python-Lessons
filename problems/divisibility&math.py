# 18
def gcd(number_1, number_2):

    while number_2 != 0: # find the modulo of the 2 numbers, right before modulo becomes 0
        remainder = number_1 % number_2
        number_1, number_2 = number_2, remainder

    return number_1

print(gcd(48, 18))  # 6
