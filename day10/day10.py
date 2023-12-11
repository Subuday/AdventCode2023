import collections


def dirs(graph, point):
    if graph[point[0]][point[1]] == "S":
        res = []
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = point[0] + di, point[1] + dj
            if 0 <= ni < len(graph) and 0 <= nj < len(graph[ni]):
                if point in list(neighbors(graph, (ni, nj))):
                    res.append((di, dj))
        return res
    else:
        nav_map = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            ".": [],
        }
        return nav_map[graph[point[0]][point[1]]]


def neighbors(graph, point):
    res = []
    for di, dj in dirs(graph, point):
        ni, nj = point[0] + di, point[1] + dj
        if 0 <= ni < len(graph) and 0 <= nj < len(graph[ni]):
            res.append((ni, nj))
    return res


def part1():
    graph = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            graph.append([c for c in line])

    s = None
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'S':
                s = (i, j)
                break

    visited = set()
    dists = {}
    q = collections.deque([(s, 0)])
    while q:
        point, dist = q.popleft()
        visited.add(point)
        dists[point] = dist

        for n in neighbors(graph, point):
            if n in visited:
                continue
            q.append((n, dist + 1))

    return max(dists.values())


def intersections(graph, visited, point):
    res = 0
    for k in range(point[1]):
        if (point[0], k) in visited:
            line = graph[point[0]]
            if line[k] in {"F", "7", "|"}:
                res += 1
    return res


def part2():
    graph = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            graph.append([c for c in line])

    s = None
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'S':
                s = (i, j)
                break

    graph[s[0]][s[1]] = "J"

    visited = set()
    dists = {}
    q = collections.deque([(s, 0)])
    while q:
        point, dist = q.popleft()
        visited.add(point)
        dists[point] = dist

        for n in neighbors(graph, point):
            if n in visited:
                continue
            q.append((n, dist + 1))

    res = 0
    for i, line in enumerate(graph):
        for j in range(len(line)):
            if not (i, j) in visited:
                intrs = intersections(graph, visited, (i, j))
                if intrs % 2 == 1:
                    res += 1

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
