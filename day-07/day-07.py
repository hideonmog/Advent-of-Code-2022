from collections import defaultdict

with open ("input.txt", "r") as f:
    lines = f.read().strip().splitlines()

size = defaultdict(int)
path = []

for line in lines:
    words = line.strip().split()
    if words[0] == "$":
        if words[1] == "cd":
            if words[2] == "..":
                path.pop()
            else:
                path.append(words[2])
        if words[1] == "ls":
            continue
    elif words[0] == "dir":
        continue
    else:
        filesize = int(words[0])
        for i in range(1, len(path) + 1):
            size["/".join(path[:i])] += filesize

total_disk_space = 70000000
space_needed_for_update = 30000000
space_used = size["/"]
free_space_needed = space_used - (total_disk_space - space_needed_for_update)

part1 = sum([v for k, v in size.items() if v <= 100000])
part2 = min([v for k, v in size.items() if v >= free_space_needed])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")