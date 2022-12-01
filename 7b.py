def f(x):
    s = sorted(map(int, x.split(",")))
    ts = [0]*(s[-1]+1)

    dt, last_dt, dcrabs, crabs, j = 0, 0, 0, 0, 0
    for i in range(s[-1]+1):
        while j < len(s) and s[j] == i:
            j += 1
            dcrabs += 1
        last_dt += dt
        ts[i] += last_dt
        dt += crabs+dcrabs
        crabs += dcrabs
        dcrabs = 0
    dt, last_dt, crabs = 0, 0, 0
    j = len(s)-1
    for i in range(s[-1], -1, -1):
        while j > -1 and s[j] == i:
            j -= 1
            dcrabs += 1
        last_dt += dt
        ts[i] += last_dt
        dt += crabs+dcrabs
        crabs += dcrabs
        dcrabs = 0
    # print(ts)
    return min(ts)
