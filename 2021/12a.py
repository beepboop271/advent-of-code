def small(x):
    return x[0].islower()
def dfs(n, d, m, v):
    return 1 if n == "end" else sum(
        dfs(e, d, m, v|m.get(e, 0)) if not (small(e) and (v&m[e])) else 0
        for e in d[n]
    )
def f(x):
    d = {}
    s = map(lambda x: x.split("-"), x.split())
    for n1, n2 in s:
        d.setdefault(n1, []).append(n2)
        d.setdefault(n2, []).append(n1)
    m = {k: 1<<i for i, k in enumerate(filter(small, d.keys()))}
    return dfs("start", d, m, m["start"])
