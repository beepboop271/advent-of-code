import sys

score = { "X": 1, "Y": 2, "Z": 3 }
tie = { "X": "A", "Y": "B", "Z": "C" }
win = { "X": "C", "Y": "A", "Z": "B" }

print(sum(
    score[this] + (
        3 if tie[this] == other else
        6 if win[this] == other else
        0
    )
    for other, this in (
        strategy.split()
        for strategy in
        sys.stdin.read().split("\n")
    )
))
