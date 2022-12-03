import sys

def priority(char):
    if char.isupper():
        return ord(char) - ord("A") + 27
    else:
        return ord(char) - ord("a") + 1

print(sum(
    priority((
        set(sack[:len(sack)//2])
        & set(sack[len(sack)//2:])
    ).pop())
    for sack in
    sys.stdin.read().split()
))
