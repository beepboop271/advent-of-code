import re
import sys


def part1_first_digit(line: str) -> str:
    return next(filter(str.isdigit, line))

def part1_last_digit(line: str) -> str:
    return next(filter(str.isdigit, reversed(line)))


# regex "lazy" modifier on star *?
forward = re.compile(r"^.*?(one|two|three|four|five|six|seven|eight|nine|\d)")
reverse = re.compile(r"^.*?(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)")

digit_map = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
}

def normalize_digit(digit: str) -> str:
    return digit if digit.isdigit() else digit_map[digit]

def part2_first_digit(line: str) -> str:
    return normalize_digit(forward.match(line).group(1))

def part2_last_digit(line: str) -> str:
    return normalize_digit(reverse.match(line[::-1]).group(1)[::-1])


def solve(lines):
    def get_numbers(find_first_digit, find_last_digit):
        for line in lines:
            first = find_first_digit(line)
            last = find_last_digit(line)
            yield int(first+last)

    print(sum(get_numbers(part1_first_digit, part1_last_digit)))
    print(sum(get_numbers(part2_first_digit, part2_last_digit)))


solve(sys.stdin.read().splitlines())
