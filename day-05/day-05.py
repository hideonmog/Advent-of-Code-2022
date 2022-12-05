from copy import deepcopy
import re
from itertools import zip_longest, repeat
from collections import deque

with open ("input.txt", "r") as f:
    stacks, moves = f.read().split("\n\n")

columns = list([i for i in zip_longest(*stacks.splitlines())])
stack = {int(column[-1]): deque([crate for crate in column if crate.isupper()]) for column in columns if column[-1].isdigit()}
stack2 = deepcopy(stack)

for move in moves.splitlines():
    number_of_crates, source_stack, target_stack = map(int, re.findall(r"(\d+)", move))

    for _ in repeat(None, number_of_crates):
        stack[target_stack].appendleft(stack[source_stack].popleft())

    crates = [stack2[source_stack].popleft() for _ in repeat(None, number_of_crates)]
    for crate in crates[::-1]:
        stack2[target_stack].appendleft(crate)

print(f"Part 1: {''.join([i[0] for i in stack.values()])}")
print(f"Part 2: {''.join([i[0] for i in stack2.values()])}")

