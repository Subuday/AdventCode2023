def part1():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    res = 0
    for l in lines:
        id, game = l.split(":")
        id = int(id.split(' ')[1].strip())
        subsets = game.split(";")

        is_valid = True

        for s in subsets:
            cubes = s.split(",")

            g = 0
            r = 0
            b = 0

            for c in cubes:
                num, color = c.strip().split(" ")
                num = int(num)
                color = color.strip()

                if color == "green":
                    g += num
                elif color == "red":
                    r += num
                elif color == "blue":
                    b += num

            if r <= 12 and g <= 13 and b <= 14:
                continue
            else:
                is_valid = False
                break

        if is_valid:
            res += id

    return res


def part2():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    res = 0
    for l in lines:
        id, game = l.split(":")
        id = int(id.split(' ')[1].strip())
        subsets = game.split(";")

        is_valid = True

        min_g = 0
        min_r = 0
        min_b = 0

        for s in subsets:
            cubes = s.split(",")

            g = 0
            r = 0
            b = 0

            for c in cubes:
                num, color = c.strip().split(" ")
                num = int(num)
                color = color.strip()

                if color == "green":
                    g += num
                elif color == "red":
                    r += num
                elif color == "blue":
                    b += num

            min_g = max(min_g, g)
            min_r = max(min_r, r)
            min_b = max(min_b, b)

        res += (min_g * min_r * min_b)

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
