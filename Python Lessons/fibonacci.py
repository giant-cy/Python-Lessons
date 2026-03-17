# 0 1 1 2 3 5 8 13
# N = n-1 + n-2


# def fibonacci(n):
#     fib_list = [0,1]
#     for i in range(2,n):
#         fib_list.append(fib_list[i-1]+fib_list[i-2])
#     return fib_list
#
# print(fibonacci(10))


def fibonacci_2(n):
    a,b = 0,1
    # print(a,b,sep='\n')
    for i in range(n):
        print(a)
        current = a+b
        a = b
        b = current


fibonacci_2(10)
