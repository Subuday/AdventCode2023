def part1():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    seeds = list(map(lambda s: int(s.strip()), lines[0].split(" ")[1:]))

    def mapper(x, ranges):
        for r in ranges:
            d, s, l = r
            if s <= x <= s + l:
                return d + x - s
        return x

    maps = []

    lines = lines[2:]
    for i in range(len(lines)):
        group = []
        if len(lines[i]) == 0 or i == len(lines) - 1:
            j = i
            if len(lines[i]) == 0:
                j -= 1
            while j >= 0 and lines[j] != "":
                group.insert(0, lines[j])
                j -= 1
        if group:
            group = group[1:]
            ranges = []
            for item in group:
                dest, source, length = item.split(" ")
                dest = int(dest)
                source = int(source)
                length = int(length)
                ranges.append((dest, source, length))
            maps.append(ranges)

    res = float('inf')
    for seed in seeds:
        for ranges in maps:
            seed = mapper(seed, ranges)
        res = min(res, seed)
    return res


def mapper(lo, hi, m):
    ans = []
    for dst, src, R in m:
        end = src + R - 1
        D = dst - src  # How much is this range shifted

        if not (end < lo or src > hi):
            ans.append((max(src, lo), min(end, hi), D))

    res = []

    if len(ans) == 0:
        res.append((lo, hi))
        return res

    for i, interval in enumerate(ans):
        l, r, D = interval
        res.append((l + D, r + D))

        if i < len(ans) - 1 and ans[i + 1][0] > r + 1:
            res.append((r + 1, ans[i + 1][0] - 1))

    if ans[0][0] != lo:
        res.append((lo, ans[0][0] - 1))
    if ans[-1][1] != hi:
        res.append((ans[-1][1] + 1, hi))

    return res

def part2():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    seeds = list(map(lambda s: int(s.strip()), lines[0].split(" ")[1:]))

    maps = []

    lines = lines[2:]
    for i in range(len(lines)):
        group = []
        if len(lines[i]) == 0 or i == len(lines) - 1:
            j = i
            if len(lines[i]) == 0:
                j -= 1
            while j >= 0 and lines[j] != "":
                group.insert(0, lines[j])
                j -= 1
        if group:
            group = group[1:]
            ranges = []
            for item in group:
                dest, source, length = item.split(" ")
                dest = int(dest)
                source = int(source)
                length = int(length)
                ranges.append((dest, source, length))
            ranges.sort(key=lambda x: x[1])
            maps.append(ranges)

    for m in maps:
        for i in range(len(m) - 1):
            if not m[i][1] + m[i][2] <= m[i + 1][1]:
                print(m[i], m[i + 1])

    res = float('inf')
    i = 1
    while i < len(seeds):
        seed = seeds[i - 1]
        count = seeds[i]
        cur_intervals = [(seed, seed + count - 1)]
        new_intervals = []

        for ranges in maps:
            for l, r in cur_intervals:
                for interv in mapper(l, r, ranges):
                    new_intervals.append(interv)
            cur_intervals, new_intervals = new_intervals, []

        for l, r in cur_intervals:
            res = min(res, l)
        i += 2
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
