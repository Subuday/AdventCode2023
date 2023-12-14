def is_mirror(pattern, j, i, max_diff):
    diff = 0
    while j >= 0 and i < len(pattern):
        p1, p2 = pattern[j], pattern[i]
        for k in range(len(p1)):
            if p1[k] != p2[k]:
                diff += 1
                if diff > 1:
                    return False
        j -= 1
        i += 1
    return max_diff == diff


def mirror(pattern, max_diff=0):
    for i in range(1, len(pattern)):
        if is_mirror(pattern, i - 1, i, max_diff):
            return i - 1, i
    return None


def transpose(pattern):
    res = []
    for col in range(len(pattern[0])):
        line = []
        for row in range(len(pattern)):
            line.append(pattern[row][col])
        res.append(line)
    return res


def part1():
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        patterns = []
        pattern = []
        for i, line in enumerate(lines):
            if line != '':
                pattern.append(line)

            if line == '' or i == len(lines) - 1:
                patterns.append(pattern)
                pattern = []

    res = 0
    for i, p in enumerate(patterns):
        h = mirror(p)
        if h:
            res += (h[0] + 1) * 100
        else:
            v = mirror(transpose(p))
            res += (v[0] + 1)

    return res


def part2():
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        patterns = []
        pattern = []
        for i, line in enumerate(lines):
            if line != '':
                pattern.append(line)

            if line == '' or i == len(lines) - 1:
                patterns.append(pattern)
                pattern = []

    res = 0
    for i, p in enumerate(patterns):
        h = mirror(p, max_diff=1)
        if h:
            res += (h[0] + 1) * 100
        else:
            v = mirror(transpose(p), max_diff=1)
            res += (v[0] + 1)

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
