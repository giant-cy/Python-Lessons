# # 7.
# def is_prime(number):
#     checker = int(number ** 0.5)
#     for i in range(2, checker+1):
#         if number % i == 0:
#             print(f"{number}, is not a prime")
#             return
#     print(f"{number}, is a prime")
# is_prime(20)
# is_prime(57)
# is_prime(73)
# is_prime(17)
#
# # 8.
# def primes(number):
#     primes_list = [].sort()
#     for i in range(2, number + 1):
#         checker = int(i ** 0.5)
#         for j in range(2, checker + 1):
#             if i % j == 0:
#                 break
#         else:
#             primes_list.append(i)
#     print(primes_list)
# primes(100)


# 9
def is_perfect(num):
    if num <= 1:
        return False

    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i

    return divisors_sum == num

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(10))


# 10
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == num

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))