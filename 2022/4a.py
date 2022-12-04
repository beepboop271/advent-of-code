import re
import sys

def contains(super, sub):
    return super[0] <= sub[0] and sub[1] <= super[1]

dash_or_comma = re.compile(r"-|,")

print(sum(
    1
    for e1s, e1e, e2s, e2e in (
        map(int, dash_or_comma.split(line))
        for line in
        sys.stdin.read().split()
    )
    if contains((e1s, e1e), (e2s, e2e))
        or contains((e2s, e2e), (e1s, e1e))
))
