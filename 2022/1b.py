import sys

print(sum(
    sorted(
        sum(map(int, elf.split()))
        for elf in
        sys.stdin.read().split("\n\n")
    )[-3:]
))
