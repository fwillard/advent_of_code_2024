import regex as re


def check_equation(operands, total):
    product = operands[0] * operands[1]
    sum = operands[0] + operands[1]

    if len(operands) == 2:
        if product == total or sum == total:
            return True
        else:
            return False

    prod_list = operands[:]
    del prod_list[0]
    prod_list[0] = product

    sum_list = operands[:]
    del sum_list[0]
    sum_list[0] = sum

    return check_equation(prod_list, total) | check_equation(sum_list, total)


file = open("input.txt")

contents = file.read()


matches = re.findall(r"(\d+): ([\d\s][^\n]+)", contents)

sum = 0

for match in matches:
    total = int(match[0])
    operands = [int(x) for x in match[1].split(" ")]

    if check_equation(operands, total):
        sum += total

print(f"part 1: {sum}")
