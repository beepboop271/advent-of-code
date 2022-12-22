import sys

line = sys.stdin.readline()
num_stacks = (len(line)+1)//4
stacks = [[] for _ in range(num_stacks)]

while line[1].isupper() or line[1] == " ":
    read = 1
    for i in range(len(stacks)):
        if line[read].isupper():
            stacks[i].append(line[read])
        read += 4
    line = sys.stdin.readline()
line = sys.stdin.readline()

for stack in stacks:
    stack.reverse()

for line in sys.stdin:
    _, amount, _, src, _, dest = line.split()
    for _ in range(int(amount)):
        stacks[int(dest)-1].append(stacks[int(src)-1].pop())

print("".join(stack[-1] for stack in stacks))
