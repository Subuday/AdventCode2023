import heapq
from math import inf


def part1():
    grid = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            grid.append([c for c in line])

    graph = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            graph[x, y] = int(grid[y][x])

    q = [(0, 0, 0, None, 0)]
    visited = {}
    while q:
        cost, x, y, dir, dist = heapq.heappop(q)
        if (x, y) == (len(grid[0]) - 1, len(grid) - 1):
            return cost
        if visited.get((x, y, dir, dist), inf) <= cost:
            continue
        visited[(x, y, dir, dist)] = cost
        for i, (dx, dy) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
                continue
            if (i + 2) % 4 == dir:
                continue  # can't turn back
            new_dist = dist
            if i != dir:
                new_dist = 1
            else:
                new_dist = dist + 1
                if new_dist >= 4:
                    continue
            heapq.heappush(q, (cost + graph[new_x, new_y], new_x, new_y, i, new_dist))


def part2():
    grid = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            grid.append([c for c in line])

    graph = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            graph[x, y] = int(grid[y][x])

    q = [(0, 0, 0, None, 0)]
    visited = {}
    while q:
        cost, x, y, dir, dist = heapq.heappop(q)
        if (x, y) == (len(grid[0]) - 1, len(grid) - 1):
            if dist < 4:
                continue
            return cost
        if visited.get((x, y, dir, dist), inf) <= cost:
            continue
        visited[(x, y, dir, dist)] = cost
        for i, (dx, dy) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or new_x >= len(grid[0]) or new_y >= len(grid):
                continue
            if (i + 2) % 4 == dir:
                continue  # can't turn back
            new_dist = dist
            if i != dir:
                if dir is not None and dist < 4:
                    continue
                new_dist = 1
            else:
                new_dist = dist + 1
                if new_dist >= 11:
                    continue
            heapq.heappush(q, (cost + graph[new_x, new_y], new_x, new_y, i, new_dist))


if __name__ == "__main__":
    print(part1())
    print(part2())
