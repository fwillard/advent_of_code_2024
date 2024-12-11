import itertools
from collections import defaultdict


# compute the antinodes for two points a and b
def compute_antinodes(a, b, max_x, max_y, multiple=False):
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    c1_valid = True
    c2_valid = True
    weight = 1
    candidates = []
    for point in [a, b]:
        if multiple:
            while c1_valid or c2_valid:
                candidate_1 = tuple(
                    [sum(x) for x in zip(point, (weight * dx, weight * dy))]
                )
                candidate_2 = tuple(
                    [sum(x) for x in zip(point, (-weight * dx, -weight * dy))]
                )

                if in_bounds(candidate_1, max_x, max_y):
                    candidates.append(candidate_1)
                else:
                    c1_valid = False
                if in_bounds(candidate_2, max_x, max_y):
                    candidates.append(candidate_2)
                else:
                    c2_valid = False

                weight += 1
        else:
            candidate_1 = tuple([sum(x) for x in zip(point, (dx, dy))])
            candidate_2 = tuple([sum(x) for x in zip(point, (-dx, -dy))])

            if candidate_1 != a and candidate_1 != b:
                if in_bounds(candidate_1, max_x, max_y):
                    candidates.append(candidate_1)

            if candidate_2 != a and candidate_2 != b:
                if in_bounds(candidate_2, max_x, max_y):
                    candidates.append(candidate_2)

    return candidates


def in_bounds(p, max_x, max_y):
    if not (0 <= p[0] < max_x):
        return False
    if not (0 <= p[1] < max_y):
        return False
    return True


file = open("input.txt")

contents = file.readlines()

grid = []

for line in contents:
    row = list(line.strip("\n"))
    grid.append(row)

antennas = defaultdict(list)

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != ".":
            antennas[cell].append((x, y))


print(antennas)
rows = len(grid)
cols = len(grid[0])

pt1_nodes = set()
pt2_nodes = set()
for antenna_type in antennas.keys():
    for a in itertools.product(antennas[antenna_type], antennas[antenna_type]):
        if a[0] == a[1]:
            continue
        temp = compute_antinodes(a[0], a[1], cols, rows)
        for node in temp:
            pt1_nodes.add(node)

        temp = compute_antinodes(a[0], a[1], cols, rows, multiple=True)
        for node in temp:
            pt2_nodes.add(node)

print(f"part 1: {len(pt1_nodes)}")
print(f"part 2: {len(pt2_nodes)}")
