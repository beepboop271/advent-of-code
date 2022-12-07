import collections
import sys

def find_distinct_run(it, length):
    buf = collections.deque()
    present = collections.defaultdict(int)

    def add(c):
        buf.append(c)
        present[c] += 1

    def remove():
        c = buf.popleft()
        present[c] -= 1
        if present[c] == 0:
            del present[c]

    for _ in range(length):
        add(next(it))

    if len(present) == length:
        return length

    for i, c in enumerate(it, length+1):
        add(c)
        remove()
        if len(present) == length:
            return i

inp = sys.stdin.read()
print("A:", find_distinct_run(iter(inp), 4))
print("B:", find_distinct_run(iter(inp), 14))
