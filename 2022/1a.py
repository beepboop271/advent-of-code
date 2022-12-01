import sys

print(max(
    sum(map(int, elf.split()))
    for elf in
    sys.stdin.read().split("\n\n")
))
