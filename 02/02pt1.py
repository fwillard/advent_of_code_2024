def strictly_increasing(L):
    return all(x < y for x, y in zip(L, L[1:]))


def strictly_decreasing(L):
    return all(x > y for x, y in zip(L, L[1:]))


def strictly_monotonic(L):
    return strictly_increasing(L) or strictly_decreasing(L)


def safe(L):
    for x, y in zip(L, L[1:]):
        if abs(x - y) > 3:
            return False
    return True


with open("input.txt") as file:
    lines = file.readlines()

count = 0

for line in lines:
    data = [int(elem) for elem in line.split()]

    if strictly_monotonic(data):
        if safe(data):
            count += 1

print(f"Num Safe: {count}")
