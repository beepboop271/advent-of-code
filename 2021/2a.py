def f(x):
    v = {}
    s = iter(x.split())
    for d, n in zip(s, s):
        v[d] = v.get(d, 0)+int(n)
    return v["forward"]*(v["down"]-v["up"])
