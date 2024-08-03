def fib(n):
    temp = 1
    if n > 2:
        temp = fib(n-2)+fib(n-1)
    return temp


print(fib(28))