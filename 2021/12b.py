def small(x):
    return x[0].islower()
def dfs(n, d, m, v, p, u):
    return (1 if u and v&m[p] else 0) if n == "end" else sum(
        dfs(e, d, m, v, p, True) if not u and e == p else
        dfs(e, d, m, v|m.get(e, 0), p, u) if not (small(e) and (v&m[e])) else
        0
        for e in d[n]
    )
def f(x):
    d = {}
    s = map(lambda x: x.split("-"), x.split())
    for n1, n2 in s:
        d.setdefault(n1, []).append(n2) if n2 != "start" else 0
        d.setdefault(n2, []).append(n1) if n1 != "start" else 0
    m = {k: 1<<i for i, k in enumerate(filter(small, d.keys()))}
    return dfs("start", d, m, 0, "end", True)+sum(
        dfs("start", d, m, 0, small, False)
        if small != "end" else 0
        for small in m
    )
