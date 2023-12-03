def part1():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    res = 0
    for r, l in enumerate(lines):
        i = 0
        while i < len(l):
            if l[i].isdigit():
                j = i + 1
                while j < len(l) and l[j].isdigit():
                    j += 1
                num = int(l[i:j])

                is_ok = False
                for c in range(i - 1, j + 1):
                    if r - 1 >= 0 and 0 <= c < len(lines[r - 1]) and not (lines[r - 1][c]).isdigit() and lines[r - 1][c] != '.':
                        is_ok = True
                        break

                    if r + 1 < len(lines) and 0 <= c < len(lines[r + 1]) and not (lines[r + 1][c]).isdigit() and \
                            lines[r + 1][c] != ".":
                        is_ok = True
                        break

                for c in range(r - 1, r + 1):
                    if 0 <= c < len(lines) and i - 1 >= 0 and not (lines[c][i - 1]).isdigit() and lines[c][i - 1] != ".":
                        is_ok = True
                        break

                    if 0 <= c < len(lines) and j < len(lines[c]) and not (lines[c][j]).isdigit() and lines[c][j] != ".":
                        is_ok = True
                        break

                if is_ok:
                    res += num

                i = j
            else:
                i += 1

    return res


def part2():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    def num(r, c, seen):
        num = [lines[r][c]]
        i = c - 1

        while i >= 0 and lines[r][i].isdigit():
            num.insert(0, lines[r][i])
            seen.add((r, i))
            i -= 1

        i = c + 1
        while i < len(lines[r]) and lines[r][i].isdigit():
            num.append(lines[r][i])
            seen.add((r, i))
            i += 1

        return int("".join(num))

    res = 0
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if lines[r][c] == "*":
                nums = []
                coords = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1), (r - 1, c - 1), (r - 1, c + 1),
                          (r + 1, c + 1), (r + 1, c - 1)]

                seen = set()
                for (cr, cc) in coords:
                    if 0 <= cr < len(lines) and 0 <= cc < len(lines[cr]) and (lines[cr][cc]).isdigit() and (cr, cc) not in seen:
                        nums.append(num(cr, cc, seen))
                if len(nums) == 2:
                    res += (nums[0] * nums[1])

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
