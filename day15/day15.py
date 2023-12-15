from collections import OrderedDict


def hash(step):
    res = 0
    for c in step:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def part1():
    steps = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        steps = lines[0].split(",")

    res = 0
    for step in steps:
        res += hash(step)
    return res


def part2():
    steps = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        steps = lines[0].split(",")

    boxes = [OrderedDict() for _ in range(256)]

    for step in steps:
        if '-' in step:
            label = step.split('-')[0]
            if label in boxes[hash(label)]:
                del boxes[hash(label)][label]
        else:
            label = step.split('=')[0]
            focal = int(step.split('=')[1])
            boxes[hash(label)][label] = focal

    res = 0
    for i, box in enumerate(boxes):
        if len(box) == 0:
            continue
        for j, label in enumerate(box):
            res += (i + 1) * (j + 1) * box[label]
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
