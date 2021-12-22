def transpose(s):
    return [list(map(next, s)) for _ in range(2)]
def f(s):
    ps, fs = map(lambda x: x.split("\n"), s.split("\n\n"))
    x, y = transpose(list(map(lambda x: map(int, x.split(",")), ps)))
    fs = map(lambda x: x.rsplit(maxsplit=1)[1], fs)
    p1 = False
    for f in fs:
        c = int(f[2:])
        l = x if f[0] == "x" else y
        for i, p in enumerate(l):
            if p > c:
                l[i] = 2*c-p
        if not p1:
            print(len({(x[i], y[i]) for i in range(len(x))}))
            p1 = True
    pf = {(x[i], y[i]) for i in range(len(x))}
    g = [[" "]*(max(x)+1) for _ in range(max(y)+1)]
    for xi, yi in pf:
        g[yi][xi] = "*"
    print("\n".join("".join(row) for row in g))
