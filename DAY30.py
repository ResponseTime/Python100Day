def sum_of_digits(digit):
    if digit == 0:
        return 0
    else:
        return digit % 10 + sum_of_digits(digit // 10)


print(sum_of_digits(1234))


def factorial(m):
    if m == 0 or m == 1:
        return 1
    return m * factorial(m-1)


print(factorial(5))


def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


for i in range(0, 10):
    print(fib(i))
