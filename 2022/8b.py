import sys

grid = [
    list(map(int, row.strip()))
    for row in sys.stdin
]

WIDTH = len(grid[0])
HEIGHT = len(grid)

def score_single(x, y, dx, dy):
    cur_height = grid[y][x]
    x += dx
    y += dy
    score = 0
    while 0 <= x < WIDTH and 0 <= y < HEIGHT:
        score += 1
        if grid[y][x] < cur_height:
            x += dx
            y += dy
        else:
            return score
    return score

def score(x, y):
    return (
        score_single(x, y, 1, 0)
        * score_single(x, y, 0, 1)
        * score_single(x, y, -1, 0)
        * score_single(x, y, 0, -1)
    )

print(max(
    score(x, y)
    for y in range(HEIGHT)
    for x in range(WIDTH)
))
