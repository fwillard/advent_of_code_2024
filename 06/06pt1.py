from enum import Enum

# def print_map(L, direction):
#     for r in L:
#         for c in r:
#             if c == 0:
#                 print(".", end="")
#             if c == -1:
#                 print("#", end="")
#             if c == 1:
#                 match direction:
#                     case Direction.UP:
#                         print("^", end="")
#                     case Direction.DOWN:
#                         print("v", end="")
#                     case Direction.LEFT:
#                         print("<", end="")
#                     case Direction.RIGHT:
#                         print(">", end="")
#         print()


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def rotate(self):
        return Direction((self.value % 4) + 1)


def encode(c):
    if c == "#":
        return -1
    elif c == "^":
        return 1
    else:
        return 0


def index_2d(L, v):
    for i, x in enumerate(L):
        if v in x:
            return (i, x.index(v))


def valid_index(L, x, y):
    r = True
    if not 0 <= y < len(L):
        r = False
    if not 0 <= x < len(L[0]):
        r = False
    return r


def step_index(x, y, direction):
    match direction:
        case Direction.UP:
            return (x, y - 1)
        case Direction.DOWN:
            return (x, y + 1)
        case Direction.LEFT:
            return (x - 1, y)
        case Direction.RIGHT:
            return (x + 1, y)


file = open("input.txt")

contents = file.read()

# location of the guard
x = 0
y = 0
direction = Direction.UP

# -1 represents an obstacle. 0 for values not visited
puzzle_map = []
for line in contents.splitlines():
    puzzle_map.append(list(map(encode, list(line))))

(y, x) = index_2d(puzzle_map, 1)

in_bounds = True

visited = {}

while in_bounds:
    # step in the direciton, increment location and rotate as needed
    (new_x, new_y) = step_index(x, y, direction)

    # check if still in bounds
    in_bounds = valid_index(puzzle_map, new_x, new_y)
    if not in_bounds:
        break

    # check for colision
    if puzzle_map[new_y][new_x] == -1:
        direction = direction.rotate()
    else:
        (x, y) = (new_x, new_y)
        visited[(x, y)] = direction

total = len(visited)
print(f"part 1: {total}")
