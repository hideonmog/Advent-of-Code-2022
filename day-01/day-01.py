with open ("input.txt", "r") as f:
    elves = f.read().split("\n\n")

elf_calories = sorted([sum(map(int, elf.split("\n"))) for elf in elves], reverse = True)

part1 = elf_calories[0]
part2 = sum(i for i in elf_calories[0:3])

print(part1)
print(part2)