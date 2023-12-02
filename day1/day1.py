def part1():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    res = 0
    for line in lines:
        num = ""
        for c in line:
            if c.isdigit():
                num += c
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                num += line[i]
                break

        num = int(num)
        res += num

    return res


def part2():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    digits = {"one": 1, "two": 2, "three": 3, "four" : 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    res = 0
    for line in lines:
        num = ""
        for i in range(0, len(line)):
            if line[i].isdigit():
                num += line[i]
                break
            else:
                for d in digits.keys():
                    if i + len(d) <= len(line) and line[i:i+len(d)] == d:
                        num += str(digits[d])
                        break

                if len(num) == 1:
                    break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                num += line[i]
                break
            else:
                for d in digits.keys():
                    if i + len(d) <= len(line) and line[i:i+len(d)] == d:
                        num += str(digits[d])
                        break

                if len(num) == 2:
                    break

        num = int(num)
        res += num

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
