import sys

outcome_score = { "X": 0, "Y": 3, "Z": 6 }
play_score = { "A": 1, "B": 2, "C": 3 }
action = {
    "X": { "A": "C", "B": "A", "C": "B" },
    "Y": { "A": "A", "B": "B", "C": "C" },
    "Z": { "A": "B", "B": "C", "C": "A" },
}

print(sum(
    outcome_score[this] + play_score[action[this][other]]
    for other, this in (
        strategy.split()
        for strategy in
        sys.stdin.read().split("\n")
    )
))
