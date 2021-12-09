from itertools import chain

def f(inp):
    a = inp.split("\n\n")
    calls = a[0].split(",")
    boards = [[row.split() for row in board.split("\n")] for board in a[1:]]
    transposed = map(transpose, boards)
    rows = [(set(row), i) for i, board in enumerate(boards) for row in board]
    cols = [(set(col), i) for i, board in enumerate(transposed) for col in board]
    lol = rows+cols

    done = -1
    for call in calls:
        for bruh in lol:
            bruh[0].discard(call)
            if len(bruh[0]) == 0:
                done = bruh[1]
        if done >= 0:
            break

    return int(call)*sum(chain.from_iterable(
        map(lambda x: map(int, x[0]), filter(lambda x: x[1] == done, rows))
    ))


def transpose(l):
    w = len(l[0])
    s = list(map(iter, l))
    return [list(map(next, s)) for _ in range(w)]

