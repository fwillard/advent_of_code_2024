def check_safety(L, remove=None):
    safe = True

    if remove is not None:
        if remove < 0:
            return False
        temp = [x for x in L]
        del temp[remove]
        L = [x for x in temp]

    if L[0] < L[1]:
        increasing = True
    else:
        increasing = False

    for i, (x, y) in enumerate(zip(L, L[1:])):
        diff = abs(y - x)

        if not 1 <= diff <= 3:
            safe = False

        elif increasing and x > y:
            safe = False

        elif not increasing and x < y:
            safe = False

        if not safe:
            if remove is None:
                # print(i)
                # break
                return (
                    check_safety(L, i - 1)
                    or check_safety(L, i)
                    or check_safety(L, i + 1)
                )
            else:
                break
    return safe


with open("input.txt") as file:
    lines = file.readlines()

count = 0

for line in lines:
    data = [int(elem) for elem in line.split()]

    if check_safety(data):
        count += 1

print(f"Num Safe: {count}")
