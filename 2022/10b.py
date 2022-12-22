import sys

class CRT:
    WIDTH = 40
    HEIGHT = 6
    def __init__(self):
        self.screen = [['.']*CRT.WIDTH for _ in range(CRT.HEIGHT)]
        self.x = 0
        self.y = 0
    def tick(self, cpuX):
        if abs(cpuX - self.x) <= 1:
            self.screen[self.y][self.x] = '#'
        self.x += 1
        if self.x == CRT.WIDTH:
            self.x = 0
            self.y += 1
            if self.y == CRT.HEIGHT:
                self.y = 0

crt = CRT()
reg = 1

for l in sys.stdin:
    match l.strip().split():
        case ["noop"]:
            crt.tick(reg)
        case ["addx", inc]:
            crt.tick(reg)
            crt.tick(reg)
            reg += int(inc)

print("\n".join("".join(row) for row in crt.screen))
