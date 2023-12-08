import collections
import math


def part1():
    nav = ""
    net = {}
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        net_i = 0
        for i, line in enumerate(lines):
            if not line:
                net_i = i + 1
                break
            nav += line
        for line in lines[net_i:]:
            line = line.split("=")
            net[line[0].strip()] = list(map(lambda s: s.strip(), line[1].strip()[1:-1].split(",")))

        if 'AAA' not in net.keys():
            return -1

        q = ["AAA"]
        i = 0
        while q:
            cur = q.pop()
            if cur == 'ZZZ':
                break
            paths = net[cur]
            dir = nav[i % len(nav)]
            if dir == 'L':
                q.append(paths[0])
            elif dir == 'R':
                q.append(paths[1])
            i += 1

        return i


def part2():
    nav = ""
    net = {}
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        net_i = 0
        for i, line in enumerate(lines):
            if not line:
                net_i = i + 1
                break
            nav += line
        for line in lines[net_i:]:
            line = line.split("=")
            net[line[0].strip()] = list(map(lambda s: s.strip(), line[1].strip()[1:-1].split(",")))

        nums = []
        for point in net.keys():
            if point.endswith('A'):
                q = [point]
                i = 0
                while q:
                    cur = q.pop()
                    if cur.endswith('Z'):
                        break
                    paths = net[cur]
                    dir = nav[i % len(nav)]
                    if dir == 'L':
                        q.append(paths[0])
                    elif dir == 'R':
                        q.append(paths[1])
                    i += 1
                nums.append(i)

        return math.lcm(*nums)


if __name__ == "__main__":
    print(part1())
    print(part2())
