# Zwróc n-ty element ciągu fibonacciego zaczynając od n1

def rec_fib(n):
    if n <= 2:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)


def mem_fib(n):
    Array = [1 for _ in range(n)]
    for i in range(2, n):
        Array[i] = Array[i-1] + Array[i-2]
    return Array[n-1]


def ite_fib(n):
    if n <= 2:
        return 1
    a = b = 1
    c = 0
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


n = 6
result = ite_fib(n)
print(result)
