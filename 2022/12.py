import collections
import functools
import itertools
import sys

start_pos = None
end_pos = None

def elevation(char):
    if char == 'S':
        return 0
    if char == 'E':
        return 25
    return ord(char) - ord('a')

def load_row(y, row):
    global start_pos, end_pos
    start = row.find("S")
    end = row.find("E")
    if start != -1:
        start_pos = (start, y)
    if end != -1:
        end_pos = (end, y)
    return list(map(elevation, row))

grid = list(itertools.starmap(
    load_row,
    enumerate(sys.stdin.read().split())
))

WIDTH = len(grid[0])
HEIGHT = len(grid)

def bfs(begin, add_check, end_check):
    visited = [[False]*WIDTH for _ in range(HEIGHT)]
    q = collections.deque()

    visited[begin[1]][begin[0]] = True
    q.append((begin, 0))

    def add(check, fromSteps, x, y):
        if check(x, y):
            visited[y][x] = True
            q.append(((x, y), fromSteps + 1))

    while len(q) > 0:
        cur, steps = q.popleft()
        x, y = cur
        if end_check(cur):
            return steps

        check_step = functools.partial(add_check, visited, grid[y][x])
        add_step = functools.partial(add, check_step, steps)
        add_step(x+1, y)
        add_step(x-1, y)
        add_step(x, y+1)
        add_step(x, y-1)

# part a (bfs from `S` to `E`)

def check_A(visited, fromHeight, x, y):
    return (
        0 <= x < WIDTH
        and 0 <= y < HEIGHT
        and grid[y][x] <= fromHeight + 1
        and not visited[y][x]
    )

print("A:", bfs(start_pos, check_A, lambda pos: pos == end_pos))

# part b (bfs from `E` to any `a`)
# (could have solved part A backwards too)

def check_B(visited, fromHeight, x, y):
    return (
        0 <= x < WIDTH
        and 0 <= y < HEIGHT
        and fromHeight <= grid[y][x] + 1
        and not visited[y][x]
    )

print("B:", bfs(end_pos, check_B, lambda pos: grid[pos[1]][pos[0]] == 0))
