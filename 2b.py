def f(inp):
    aim, x, y = 0, 0, 0
    s = iter(inp.split())
    for d, n in zip(s, map(int, s)):
        match d:
            case "down":
                aim += n
            case "up":
                aim -= n
            case _:
                x += n
                y += n*aim
    return x*y

def g(inp):
    aim, x, y = 0, 0, 0
    s = iter(inp.split())
    for d, n in zip(s, map(int, s)):
        if d == "forward":
            x += n
            y += n*aim
        else:
            aim += n + (-2*n*(d == "up"))
    return x*y

from functools import reduce

def h(inp):
    s = iter(inp.split())
    r = reduce(
        lambda b, c: (
            (b[0], b[1]+c[1], b[2]+c[1]*b[0])
            if c[0] == "forward"
            else (b[0] + c[1]+(-2*c[1]*(c[0] == "up")), *b[1:])
        ),
        zip(s, map(int, s)),
        (0, 0, 0)
    )
    return r[1]*r[2]
