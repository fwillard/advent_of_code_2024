import regex as re

file = open("input.txt")

contents = file.read()

width = len(contents.splitlines()[0])

count = 0

count += len(re.findall(r"XMAS", contents, overlapped=True))  # left
count += len(re.findall(r"SAMX", contents, overlapped=True))  # right
count += len(
    re.findall(
        rf"X[\s\S]{{{width}}}M[\s\S]{{{width}}}A[\s\S]{{{width}}}S",
        contents,
        overlapped=True,
    )
)  # down
count += len(
    re.findall(
        rf"S[\s\S]{{{width}}}A[\s\S]{{{width}}}M[\s\S]{{{width}}}X",
        contents,
        overlapped=True,
    )
)  # up
count += len(
    re.findall(
        rf"X[\s\S]{{{width + 1}}}M[\s\S]{{{width + 1}}}A[\s\S]{{{width + 1}}}S",
        contents,
        overlapped=True,
    )
)  # down right
count += len(
    re.findall(
        rf"X[\s\S]{{{width - 1}}}M[\s\S]{{{width - 1}}}A[\s\S]{{{width - 1}}}S",
        contents,
        overlapped=True,
    )
)  # down left
count += len(
    re.findall(
        rf"S[\s\S]{{{width + 1}}}A[\s\S]{{{width + 1}}}M[\s\S]{{{width + 1}}}X",
        contents,
        overlapped=True,
    )
)  # down left
count += len(
    re.findall(
        rf"S[\s\S]{{{width - 1}}}A[\s\S]{{{width - 1}}}M[\s\S]{{{width - 1}}}X",
        contents,
        overlapped=True,
    )
)  # down left

print(f"part 1: {count}")

count = 0

count += len(
    re.findall(
        rf"M.S[\s\S]{{{width - 1}}}A[\s\S]{{{width - 1}}}M.S",
        contents,
        overlapped=True,
    )
)
count += len(
    re.findall(
        rf"S.M[\s\S]{{{width - 1}}}A[\s\S]{{{width - 1}}}S.M",
        contents,
        overlapped=True,
    )
)
count += len(
    re.findall(
        rf"M.M[\s\S]{{{width - 1}}}A[\s\S]{{{width - 1}}}S.S",
        contents,
        overlapped=True,
    )
)
count += len(
    re.findall(
        rf"S.S[\s\S]{{{width - 1}}}A[\s\S]{{{width - 1}}}M.M",
        contents,
        overlapped=True,
    )
)


print(f"part 2: {count}")
