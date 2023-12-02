import collections
import functools
import operator
import re
import sys

line_pattern = re.compile(r"Game (\d+): (.*)$")

def parse_lines(lines):
    for line in lines:
        game_id, draws = line_pattern.match(line).groups()
        yield int(game_id), draws

def parse_draws(draws):
    for draw in draws.split(";"):
        count = collections.Counter()
        for colour in draw.split(","):
            amount, name = colour.strip().split(" ", maxsplit=1)
            count[name] = int(amount)
        yield count


def part1(lines):
    bag = collections.Counter(red=12, green=13, blue=14)

    def valid_game_ids():
        for game_id, draws in parse_lines(lines):
            if all(draw <= bag for draw in parse_draws(draws)):
                yield game_id

    return sum(valid_game_ids())


def part2(lines):
    def min_game_bags():
        for _, draws in parse_lines(lines):
            # union of all bags
            yield functools.reduce(operator.or_, parse_draws(draws))

    def power(bag):
        return bag["red"]*bag["green"]*bag["blue"]

    return sum(map(power, min_game_bags()))


def solve(lines):
    print(part1(lines))
    print(part2(lines))


solve(sys.stdin.read().splitlines())
