with open ("input.txt", "r") as f:
    input = f.read().split("\n")

games = [i.split() for i in input]

scoring = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6}
}

scores = [scoring[game[0]][game[1]] for game in games]

print(f"Part 1: {sum(scores)}")

scoring2 = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7}
}

scores2 = [scoring2[game[0]][game[1]] for game in games]

print(f"Part 2: {sum(scores2)}")