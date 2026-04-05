# 7.
def is_prime(number):
    checker = int(number ** 0.5)
    for i in range(2, checker+1):
        if number % i == 0:
            print(f"{number}, is not a prime")
            return
    print(f"{number}, is a prime")
is_prime(20)
is_prime(57)
is_prime(73)
is_prime(17)

# 8.
def primes(number):
    primes_list = [].sort()
    for i in range(2, number + 1):
        checker = int(i ** 0.5)
        for j in range(2, checker + 1):
            if i % j == 0:
                break
        else:
            primes_list.append(i)
    print(primes_list)
primes(100)