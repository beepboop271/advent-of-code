import sys

class CPU:
    def __init__(self):
        self.clock = 0
        self.x = 1
        self.total = 0
    def tick(self):
        self.clock += 1
        if self.clock in range(20, 221, 40):
            self.total += self.clock*self.x

cpu = CPU()

for l in sys.stdin:
    match l.strip().split():
        case ["noop"]:
            cpu.tick()
        case ["addx", inc]:
            cpu.tick()
            cpu.tick()
            cpu.x += int(inc)

print(cpu.total)
