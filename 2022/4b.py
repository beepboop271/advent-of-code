import re
import sys

def overlap(left, right):
    return left[0] <= right[1] and left[1] >= right[0]

dash_or_comma = re.compile(r"-|,")

print(sum(
    1
    for e1s, e1e, e2s, e2e in (
        map(int, dash_or_comma.split(line))
        for line in
        sys.stdin.read().split()
    )
    if overlap((e1s, e1e), (e2s, e2e))
        or overlap((e2s, e2e), (e1s, e1e))
))
