# 1.
def check(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
check(2)
check(5)

# 2.
def sum_nums(*args):
    result = 0
    for i in range(len(args)):
        result = result + args[i]
    print(result)
sum_nums(1,2,3,10)

# 3.
def factorial(number):
    result = 1
    for i in range(1,number+1):
        result = result * i
    print(result)
factorial(5)

# 4.
def power(x, y):
    result = 1
    for i in range(y):
        result = result * x
    print(result)
power(2,3)

# 5.
def average_nums(*args):
    result = 0
    for i in range(len(args)):
        result = result + args[i]
    print(result / len(args))
average_nums(1,2,3,10)

# 6.
def swap(a, b):
    print(f"before: a={a}")
    print(f"before: b={b}")
    a, b = b, a
    print(f"after: a={a}")
    print(f"after: b={b}")
swap(1, 5)