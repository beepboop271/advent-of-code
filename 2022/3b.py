import sys

def by_three(it):
    try:
        while True:
            yield (next(it), next(it), next(it))
    except StopIteration:
        pass

def priority(char):
    if char.isupper():
        return ord(char) - ord("A") + 27
    else:
        return ord(char) - ord("a") + 1

print(sum(
    priority((set(elf1) & set(elf2) & set(elf3)).pop())
    for elf1, elf2, elf3 in
    by_three(iter(sys.stdin.read().split()))
))
