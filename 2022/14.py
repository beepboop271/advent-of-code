import itertools
import sys

dims = [0, 1000, 0]

def update(x, y):
    x = int(x)
    y = int(y)
    if x > dims[0]:
        dims[0] = x
    if x < dims[1]:
        dims[1] = x
    if y > dims[2]:
        dims[2] = y
    return (x, y)

lines = [
    [
        update(*coord.split(","))
        for coord in line.split(" -> ")
    ]
    for line in sys.stdin.read().strip().split("\n")
]

MAX_Y = dims[2] + 2
MIN_Y = 0
MAX_X = max(dims[0], 500+MAX_Y)
MIN_X = min(dims[1], 500-MAX_Y)

WIDTH = MAX_X - MIN_X + 1
HEIGHT = MAX_Y - MIN_Y + 1

AIR = '.'
ROCK = '#'
SAND = 'o'

grid = [[AIR]*WIDTH for _ in range(HEIGHT-1)]
grid.append([ROCK]*WIDTH)

def write(x, y, c):
    grid[y-MIN_Y][x-MIN_X] = c

def read(x, y):
    if x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y:
        return AIR
    return grid[y-MIN_Y][x-MIN_X]

def settle():
    x = 500
    y = 0
    while True:
        while read(x, y+1) == AIR:
            y += 1
            if y > MAX_Y:
                return None
        if read(x-1, y+1) == AIR:
            x -= 1
            y += 1
            if x < 0 or y > MAX_Y:
                return None
        elif read(x+1, y+1) == AIR:
            x += 1
            y += 1
            if x > MAX_X or y > MAX_Y:
                return None
        else:
            return (x, y)

for sequence in lines:
    for (sx, sy), (ex, ey) in itertools.pairwise(sequence):
        for x in range(min(sx, ex), max(sx, ex)+1):
            for y in range(min(sy, ey), max(sy, ey)+1):
                write(x, y, ROCK)

sand_count = 0

while True:
    c = settle()
    if c[1] > MAX_Y-2:
        print("A:", sand_count)
        break

    write(c[0], c[1], SAND)
    sand_count += 1

while True:
    c = settle()
    write(c[0], c[1], SAND)
    sand_count += 1

    if c == (500, 0):
        print("B:", sand_count)
        break
