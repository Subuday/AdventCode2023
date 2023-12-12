from collections import defaultdict

from math import inf


def dist(p1, p2, empty_rows, empty_cols, exp):
    res = 0
    for r in range(min(p1[0], p2[0]), max(p1[0], p2[0])):
        if r in empty_rows:
            res += exp
        else:
            res += 1

    for c in range(min(p1[1], p2[1]), max(p1[1], p2[1])):
        if c in empty_cols:
            res += exp
        else:
            res += 1
    return res


def floyd_warshall(graph, empty_rows, empty_cols, exp):
    glxs = []
    for r in range(len(graph)):
        for c in range(len(graph[r])):
            if graph[r][c] == "#":
                glxs.append((r, c))

    dists = [[inf for _ in range(len(glxs))] for _ in range(len(glxs))]
    for i in range(len(glxs)):
        for j in range(len(glxs)):
            if i == j:
                dists[i][j] = 0
            else:
                dists[i][j] = dist(glxs[i], glxs[j], empty_rows, empty_cols, exp)

    for k in range(len(glxs)):
        for i in range(len(glxs)):
            for j in range(len(glxs)):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]

    return dists


def part1(exp=2):
    graph = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            graph.append([c for c in line])

    empty_rows = []
    for i in range(len(graph)):
        if all(c == "." for c in graph[i]):
            empty_rows.append(i)

    empty_cols = []
    for j in range(len(graph[0])):
        if all(graph[i][j] == "." for i in range(len(graph))):
            empty_cols.append(j)

    dists = floyd_warshall(graph, empty_rows, empty_cols, exp)

    res = 0
    for i in range(len(dists)):
        for j in range(i, len(dists[i])):
            res += dists[i][j]

    return res


def part2():
    return part1(exp=1_000_000)


if __name__ == "__main__":
    print(part1())
    print(part2())
