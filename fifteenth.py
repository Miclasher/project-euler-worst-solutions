def calculate(size):
    from math import factorial
    num = factorial(size*2)/factorial(size)**2
    return int(num)
print(calculate(20))
