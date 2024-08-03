recursive_lambda = (lambda func: lambda *args: func(func, *args))
print(recursive_lambda(lambda a, b: b*a(a, b-1) if b > 0 else 1)(5))