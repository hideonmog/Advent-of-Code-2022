with open("input.txt", "r") as f:
    rucksacks = f.read().splitlines()

def item_priority_score(item: str) -> int:
    return ord(item) - 96 if item.islower() else ord(item) - 38

score = 0
for rucksack in rucksacks:
    compartment1, compartment2 = set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])
    same = list(compartment1.intersection(compartment2))
    score += sum([item_priority_score(i) for i in same])

print(f"Part 1: {score}")

score2 = 0
for i in range(0, len(rucksacks), 3):
    first, second, third = set(rucksacks[i]), set(rucksacks[i + 1]), set(rucksacks[i + 2])
    same = list(first.intersection(second.intersection(third)))
    score2 += sum([item_priority_score(i) for i in same])

print(f"Part 2: {score2}")