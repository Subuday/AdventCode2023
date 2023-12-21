import collections


def part1():
    grid = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            grid.append([])
            for c in line:
                grid[-1].append(c)

    s = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                s = (x, y)
                break

    res = set()
    seen = set()
    q = collections.deque([(s[0], s[1], 64)])
    while q:
        r, c, s = q.popleft()

        if s % 2 == 0:
            res.add((r, c))

        if s == 0:
            continue

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nr, nc = r + dx, c + dy
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[nr]):
                continue
            if grid[nr][nc] == "#":
                continue
            if (nr,nc) in seen:
                continue
            seen.add((nr,nc))
            q.append((nr, nc, s - 1))


    return len(res)


def part2():
    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
