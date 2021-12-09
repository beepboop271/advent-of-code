from collections import Counter

def f(inp):
    s = list(map(iter, inp.split()))
    s = list(map(iter, ((x[0] for x in Counter(map(next, s)).most_common())
                        for _ in range(12))))
    s = [int("".join(map(next, s)), 2) for _ in range(2)]
    return s[0]*s[1]
