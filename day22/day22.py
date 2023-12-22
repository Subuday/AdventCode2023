import collections


def overlaps(b1, b2):
    return max(b1[0], b2[0]) <= min(b1[3], b2[3]) and max(b1[1], b2[1]) <= min(b1[4], b2[4])


def part1():
    bricks = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            bricks.append(list(map(int, line.replace("~", ",").split(","))))
            bricks.sort(key=lambda b: b[2])

    for i, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:i]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] += (max_z - brick[2])
        brick[2] = max_z

    bricks.sort(key=lambda brick: brick[5])

    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supported_k = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supported_k[j].add(i)

    res = 0
    for i in range(len(bricks)):
        if all(len(v_supported_k[j]) >= 2 for j in k_supports_v[i]):
            res += 1

    return res


def part2():
    bricks = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            bricks.append(list(map(int, line.replace("~", ",").split(","))))
            bricks.sort(key=lambda b: b[2])

    for i, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:i]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] += (max_z - brick[2])
        brick[2] = max_z

    bricks.sort(key=lambda brick: brick[5])

    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supported_k = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supported_k[j].add(i)

    res = 0
    for i in range(len(bricks)):
        q = collections.deque(j for j in k_supports_v[i] if len(v_supported_k[j]) == 1)
        falling = set(q)
        falling.add(i)

        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
                if v_supported_k[k] <= falling:
                    q.append(k)
                    falling.add(k)

        res += len(falling) - 1


    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
