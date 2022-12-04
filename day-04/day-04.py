with open ("input.txt", "r") as f:
    pairs = [line.split(",") for line in f.read().splitlines()]

full_overlap = 0
partial_overlap = 0

for pair in pairs:
    sections1, sections2 = [[int(ids) for ids in sections.split("-")] for sections in pair]
    set1 = set(range(sections1[0], sections1[1] + 1))
    set2 = set(range(sections2[0], sections2[1] + 1))

    if set1 >= set2 or set2 >= set1:
        full_overlap += 1

    if len(set1.intersection(set2)) > 0:
        partial_overlap += 1 
    
print(f"Part 1: {full_overlap}")
print(f"Part 2: {partial_overlap}")