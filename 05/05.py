from collections import defaultdict

import regex as re


def bubble_sort(L, rules):
    swapped = True
    n = len(L)
    while swapped:
        swapped = False
        for i in range(1, n):
            if L[i - 1] in rules[L[i]]:
                L[i - 1], L[i] = L[i], L[i - 1]
                swapped = True
    return L


file = open("input.txt")

contents = file.read().split("\n\n")
rules = defaultdict(list)

for rule in re.findall(r"(\d+)\|(\d+)", contents[0]):
    rules[int(rule[0])].append(int(rule[1]))

updates = [
    [int(num) for num in update.split(",")] for update in contents[1].splitlines()
]


valid_lists = []
reordered_lists = []
for update in updates:
    valid = True
    seen = []
    for num in update:
        for s in seen:
            if s in rules[num]:
                valid = False
        seen.append(num)
    if valid:
        valid_lists.append(update)
    else:
        reordered_lists.append(update)

total = 0
for update in valid_lists:
    middleIdx = int((len(update) - 1) / 2)
    total += update[middleIdx]
print(f"part 1: {total}")

total = 0
for update in reordered_lists:
    bubble_sort(update, rules)
    middleIdx = int((len(update) - 1) / 2)
    total += update[middleIdx]
print(f"part 2: {total}")
