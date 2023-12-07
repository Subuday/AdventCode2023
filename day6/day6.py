def bs_l(lo, hi, r):
    t = hi
    while lo < hi:
        h = lo + (hi - lo) // 2
        d = (t - h) * h
        if d > r:
            hi = h
        else:
            lo = h + 1

    return lo


def bs_h(lo, hi, r):
    t = hi
    while lo < hi:
        h = lo + (hi - lo) // 2
        d = (t - h) * h
        if d > r:
            lo = h + 1
        else:
            hi = h

    return lo - 1


def part1():
    races = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        times = list(filter(lambda x: x.strip(), lines[0].split(" ")))[1:]
        dists = list(filter(lambda x: x.strip(), lines[1].split(" ")))[1:]
        for time, dist in zip(times, dists):
            races.append((int(time), int(dist)))

    res = 1
    for (time, dist) in races:
        lo = bs_l(0, time, dist)
        hi = bs_h(0, time, dist)
        res *= (hi - lo + 1)

    return res


def part2():
    # Just fulfill another input
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
