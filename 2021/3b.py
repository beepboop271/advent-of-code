from collections import Counter
from itertools import starmap

def f(inp):
    v = []
    for i in range(2):
        s = list(map(lambda x: (iter(x), x, x), inp.split()))
        while len(s) > 1:
            c = Counter(map(lambda x: next(x[0]), s)).most_common()
            b = c[i][0] if len(c) < 2 or c[0][1] != c[1][1] else str(1-i)
            s = list(starmap(lambda x,y,z:(x, y[1:], z), filter(lambda x: x[1][0] == b, s)))
        v.append(int(s[0][2], 2))
    return v[0]*v[1]
