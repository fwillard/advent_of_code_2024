from collections import defaultdict

import regex as re

file = open("input.txt")

contents = file.read().split("\n\n")
rules = defaultdict(list)

for rule in re.findall(r"(\d+)\|(\d+)", contents[0]):
    rules[int(rule[0])].append(int(rule[1]))

updates = [
    [int(num) for num in update.split(",")] for update in contents[1].splitlines()
]

total = 0
for update in updates:
    valid = True
    seen = []
    for num in update:
        for s in seen:
            if s in rules[num]:
                valid = False
        seen.append(num)
    if valid:
        middleIdx = int((len(update) - 1) / 2)
        total += update[middleIdx]

print(f"part 1: {total}")
