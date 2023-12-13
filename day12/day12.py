def dfs(springs, groups, cache):
    if (springs, tuple(groups)) in cache:
        return cache[(springs, tuple(groups))]

    res = 0
    if len(springs) == 0:
        # "" (,) -> True
        # "" -> (1,) -> False
        if len(groups) == 0:
            res = 1
        else:
            res = 0
    elif springs.startswith("."):
        # ".###?" -> "###?"
        res = dfs(springs[1:], groups, cache)
    elif springs.startswith("?"):
        # "?###?" -> ".###?"
        # "?###?" -> "####?"
        res = dfs(springs.replace("?", ".", 1), groups, cache) + dfs(springs.replace("?", "#", 1), groups, cache)
    elif springs.startswith("#"):
        if len(groups) == 0:
            # "##" ()
            res = 0
        elif len(springs) < groups[0]:
            # "##" (3)
            res = 0
        elif any(c == "." for c in springs[0:groups[0]]):
            # "##.???" (3,1)
            res = 0
        elif len(groups) > 1:
            if len(springs) < (groups[0] + 1) or springs[groups[0]] == "#":
                res = 0
            else:
                # "##.???" (2,1) -> "???" (1,)
                res = dfs(springs[(groups[0] + 1):], groups[1:], cache)
        else:
            # "##.???" (2,) -> ".???" (,)
            res = dfs(springs[groups[0]:], groups[1:], cache)
    else:
        raise Exception("No other branches possible")

    cache[(springs, tuple(groups))] = res
    return res


def part1():
    res = 0
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            springs, groups = line.split(' ')
            groups = [int(x) for x in groups.split(",")]
            res += dfs(springs, groups, {})
    return res


def part2():
    res = 0
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            springs, groups = line.split(' ')
            springs = "?".join([springs] * 5)
            groups = [int(x) for x in groups.split(",")] * 5
            res += dfs(springs, groups, {})
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
