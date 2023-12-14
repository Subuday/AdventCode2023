def part1():
    table = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            table.append([c for c in line])

    for i in range(1, len(table)):
        line = table[i]
        for j in range(len(line)):
            if line[j] == "O":
                k = i
                while k > 0 and table[k - 1][j] == ".":
                    table[k][j] = "."
                    table[k - 1][j] = "O"
                    k -= 1

    res = 0
    for i, line in enumerate(table):
        for c in line:
            if c == "O":
                res += (len(table) - i)
    return res


def part2():
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
