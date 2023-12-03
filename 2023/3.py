import sys
from itertools import chain, islice, takewhile

flatten = chain.from_iterable
all_dirs = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))

class Lines:
    def __init__(self, lines):
        self.lines = lines
        self.rows = len(lines)
        self.cols = len(lines[0])

    def coords_where(self, condition):
        for row, line in enumerate(self.lines):
            for col, char in enumerate(line):
                if condition(char):
                    yield row, col

    def _get_full_number(self, row, col):
        def digits(it):
            return sum(1 for _ in takewhile(str.isdigit, it))

        line = self.lines[row]
        right = col+digits(islice(line, col, None))
        left = col-digits(islice(reversed(line), self.cols-col, None))
        return row, left, right

    def number_coords_adjacent_to(self, coord):
        for row_offset, col_offset in all_dirs:
            new_row = coord[0]+row_offset
            new_col = coord[1]+col_offset
            if (
                0 <= new_row < self.rows
                and 0 <= new_col < self.cols
                and self.lines[new_row][new_col].isdigit()
            ):
                yield self._get_full_number(new_row, new_col)

    def unique_ints(self, number_coords):
        seen = set()
        for row, left, right in number_coords:
            if (row, left) not in seen:
                seen.add((row, left))
                yield int(self.lines[row][left:right])


def part1(lines: Lines):
    symbols = lines.coords_where(lambda c: c != "." and not c.isdigit())
    part_nums = flatten(map(lines.number_coords_adjacent_to, symbols))
    return sum(lines.unique_ints(part_nums))


def part2(lines: Lines):
    def gears():
        stars = lines.coords_where(lambda c: c == "*")
        for star in map(lines.number_coords_adjacent_to, stars):
            part_numbers = list(islice(lines.unique_ints(star), 3))
            if len(part_numbers) == 2:
                yield part_numbers[0]*part_numbers[1]

    return sum(gears())


def solve(lines):
    l = Lines(lines)
    print(part1(l))
    print(part2(l))


solve(sys.stdin.read().splitlines())
