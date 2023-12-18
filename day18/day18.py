def shoelace_area(vertices):
    area = 0
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i][0], vertices[i][1]
        x2, y2 = vertices[(i + 1) % n][0], vertices[(i + 1) % n][1]
        area += x1 * y2 - y1 * x2
    return abs(area) // 2


def cubic_meters(cmds):
    border = 0
    for _, steps, _ in cmds:
        border += steps

    vertices = [(0, 0)]
    for cmd in cmds:
        dir, steps, _ = cmd
        if dir == 'L':
            p = vertices[-1]
            p = (p[0] - steps, p[1])
            vertices.append(p)
        elif dir == 'R':
            p = vertices[-1]
            p = (p[0] + steps, p[1])
            vertices.append(p)
        elif dir == 'U':
            p = vertices[-1]
            p = (p[0], p[1] - steps)
            vertices.append(p)
        elif dir == 'D':
            p = vertices[-1]
            p = (p[0], p[1] + steps)
            vertices.append(p)

    interior = shoelace_area(vertices) - (border // 2) + 1

    return interior + border


def part1():
    cmds = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            dir, steps, color = line.split(" ")
            dir = dir[0]
            steps = int(steps)
            color = color[1:-1]
            cmds.append((dir, steps, color))

    return cubic_meters(cmds)


def part2():
    cmds = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            dir, steps, color = line.split(" ")
            dir = color[-2:-1]
            if int(dir) == 0:
                dir = 'R'
            elif int(dir) == 1:
                dir = 'D'
            elif int(dir) == 2:
                dir = 'L'
            elif int(dir) == 3:
                dir = 'U'

            steps = int(color[2:-2], 16)
            color = color[1:-1]
            cmds.append((dir, steps, color))

    return cubic_meters(cmds)


if __name__ == "__main__":
    print(part1())
    print(part2())
