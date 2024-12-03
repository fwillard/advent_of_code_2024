import re

data = open("input.txt").read()
matches = re.findall(r"mul\((\d+),(\d+)\)", data)

total = 0

for m in matches:
    total += int(m[0]) * int(m[1])

print(f"part 1: {total}")
