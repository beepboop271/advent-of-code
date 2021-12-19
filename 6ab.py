import functools
@functools.cache
def count(days):
    return 1+sum(count(days-i) for i in range(9, days, 7))
def bruh2(x, n):
    return count(n+9-x)
def f(x, days):
    lut = [bruh2(i, days) for i in range(7)]
    return sum(lut[i] for i in map(int, x.split(",")))
