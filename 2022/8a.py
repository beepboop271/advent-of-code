import sys

grid = [
    list(map(int, row.strip()))
    for row in sys.stdin
]

WIDTH = len(grid[0])
HEIGHT = len(grid)

visible = [[False]*WIDTH for _ in range(HEIGHT)]

def scan(x, y, dx, dy):
    highest = -1
    while 0 <= x < WIDTH and 0 <= y < HEIGHT:
        if grid[y][x] > highest:
            highest = grid[y][x]
            if not visible[y][x]:
                visible[y][x] = True
        x += dx
        y += dy

for x in range(WIDTH):
    scan(x, 0, 0, 1)
    scan(x, HEIGHT-1, 0, -1)
for y in range(HEIGHT):
    scan(0, y, 1, 0)
    scan(WIDTH-1, y, -1, 0)

print(sum(map(sum, visible)))
