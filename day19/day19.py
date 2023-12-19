def part1():
    tfms = {}
    parts = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        first_part = True
        for line in lines:
            if len(line) == 0:
                first_part = False
                continue
            if first_part:
                name, stms = line.split("{")
                stms = stms[:-1].split(",")
                tfm = []
                for i in range(len(stms)):
                    stms[i] = stms[i].strip()
                    if '>' in stms[i] or '<' in stms[i]:
                        op = 1
                        if stms[i][1] == '<':
                            op = -1
                        stm = {
                            'el': stms[i].split(':')[0].strip()[:1],
                            'op': op,
                            'val': int(stms[i].split(':')[0].strip()[2:]),
                            'dest': stms[i].split(':')[1].strip(),
                        }
                        tfm.append(stm)
                    else:
                        tfm.append(stms[i])
                tfms[name] = tfm
            else:
                line = line[1:-1].split(",")
                part = {}
                for e in line:
                    part[e.split("=")[0]] = int(e.split("=")[1])
                parts.append(part)

    res = []
    for part in parts:
        wrkf = 'in'
        while wrkf:
            if wrkf == 'R':
                break
            if wrkf == 'A':
                res.append(part)
                break
            tfm = tfms[wrkf]

            for check in tfm:
                if type(check) == dict:
                    if (check['op'] == 1 and part[check['el']] > check['val'] or
                            check['op'] == -1 and part[check['el']] < check['val']):
                        wrkf = check['dest']
                        break
                else:
                    wrkf = check

    sum = 0
    for part in res:
        for val in part.values():
            sum += val

    return sum


def merge(r1, r2):
    start = max(r1[0], r2[0])
    end = min(r1[1], r2[1])
    if start < end:
        return start, end
    else:
        return 0, 0


def part2():
    tfms = {}
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        first_part = True
        for line in lines:
            if len(line) == 0:
                first_part = False
                continue
            if first_part:
                name, stms = line.split("{")
                stms = stms[:-1].split(",")
                tfm = []
                for i in range(len(stms)):
                    stms[i] = stms[i].strip()
                    if '>' in stms[i] or '<' in stms[i]:
                        op = 1
                        if stms[i][1] == '<':
                            op = -1
                        stm = {
                            'el': stms[i].split(':')[0].strip()[:1],
                            'op': op,
                            'val': int(stms[i].split(':')[0].strip()[2:]),
                            'dest': stms[i].split(':')[1].strip(),
                        }
                        tfm.append(stm)
                    else:
                        tfm.append(stms[i])
                tfms[name] = tfm
            else:
                break

    def backtracking(wrkf, ranges):
        if wrkf == 'R':
            return 0
        elif wrkf == 'A':
            product = 1
            for r in ranges.values():
                product *= (r[1] - r[0] + 1)
            return product
        else:
            sum = 0
            new_ranges = ranges.copy()
            tfm = tfms[wrkf]
            for check in tfm:
                if type(check) == dict:
                    if check['op'] == 1:
                        new_range = (check['val'] + 1, 4000)
                        new_range = merge(new_ranges[check['el']], new_range)

                        new_range_reversed = (1, check['val'])
                        new_range_reversed = merge(new_ranges[check['el']], new_range_reversed)

                        new_ranges[check['el']] = new_range
                        sum += backtracking(check['dest'], new_ranges)
                        new_ranges[check['el']] = new_range_reversed
                    else:
                        new_range = (1, check['val'] - 1)
                        new_range = merge(new_ranges[check['el']], new_range)

                        new_range_reversed = (check['val'], 4000)
                        new_range_reversed = merge(new_ranges[check['el']], new_range_reversed)

                        new_ranges[check['el']] = new_range
                        sum += backtracking(check['dest'], new_ranges)
                        new_ranges[check['el']] = new_range_reversed
                else:
                    sum += backtracking(check, new_ranges)
            return sum

    return backtracking('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})


if __name__ == "__main__":
    print(part1())
    print(part2())
