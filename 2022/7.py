import sys

class Dir:
    def __init__(self, name):
        self.name: str = name
        self.size: int = 0
        self._children: dict[str, Dir] = {}
    def __getitem__(self, key):
        return self._children[key]
    def __setitem__(self, key, item):
        self._children[key] = item
    def __iter__(self):
        return iter(self._children.values())
    def __repr__(self):
        return f"Dir({self.name}, {self.size})"

sys.stdin.readline()
root = Dir("")
wd = [root]

# assume `ls` is only run on each dir once
# assume `cd` is only run after `ls` has
# been run in the current dir
for line in sys.stdin:
    match line.split():
        case ["$", "cd", ".."]:
            wd.pop()
        case ["$", "cd", d]:
            wd.append(wd[-1][d])
        case ["dir", d]:
            wd[-1][d] = Dir(d)
        case [size, filename] if size.isdigit():
            size = int(size)
            for d in wd:
                d.size += size

def search_small(d: Dir):
    return (
        sum(search_small(child) for child in d)
        + (d.size if d.size <= 100000 else 0)
    )

print("A:", search_small(root))

min_delete_size = root.size - 40000000

def search_min(d: Dir, best: int):
    if d.size < min_delete_size:
        return best
    if d.size < best:
        best = d.size
    for child in d:
        best = search_min(child, best)
    return best

print("B:", search_min(root, root.size))
