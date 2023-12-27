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


def cycle(grid):
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple(
            "#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)
    return grid


def part2():
    grid = tuple(open("input.txt").read().splitlines())

    seen = {grid}
    array = [grid]

    iter = 0

    while True:
        iter += 1
        grid = cycle(grid)
        if grid in seen:
            break
        seen.add(grid)
        array.append(grid)

    first = array.index(grid)

    grid = array[(1000000000 - first) % (iter - first) + first]

    print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))


if __name__ == "__main__":
    print(part1())
    print(part2())
