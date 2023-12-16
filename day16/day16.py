import collections
import enum


class Dir(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def bfs(graph, start, start_dir):
    q = collections.deque([(start, start_dir)])
    visited = dict()
    while q:
        for _ in range(len(q)):
            coord, d = q.popleft()
            if coord[0] < 0 or coord[1] < 0 or coord[0] >= len(graph) or coord[1] >= len(graph[0]):
                continue
            if coord in visited and d in visited[coord]:
                continue
            if coord not in visited:
                visited[coord] = []
            visited[coord].append(d)
            if graph[coord[0]][coord[1]] == '.':
                if d == Dir.DOWN:
                    q.append(((coord[0] - 1, coord[1]), Dir.DOWN))
                elif d == Dir.UP:
                    q.append(((coord[0] + 1, coord[1]), Dir.UP))
                elif d == Dir.RIGHT:
                    q.append(((coord[0], coord[1] + 1), Dir.RIGHT))
                elif d == Dir.LEFT:
                    q.append(((coord[0], coord[1] - 1), Dir.LEFT))
            elif graph[coord[0]][coord[1]] == '\\':
                if d == Dir.DOWN:
                    q.append(((coord[0], coord[1] - 1), Dir.LEFT))
                elif d == Dir.UP:
                    q.append(((coord[0], coord[1] + 1), Dir.RIGHT))
                elif d == Dir.RIGHT:
                    q.append(((coord[0] + 1, coord[1]), Dir.UP))
                elif d == Dir.LEFT:
                    q.append(((coord[0] - 1, coord[1]), Dir.DOWN))
            elif graph[coord[0]][coord[1]] == '/':
                if d == Dir.DOWN:
                    q.append(((coord[0], coord[1] + 1), Dir.RIGHT))
                elif d == Dir.UP:
                    q.append(((coord[0], coord[1] - 1), Dir.LEFT))
                if d == Dir.RIGHT:
                    q.append(((coord[0] - 1, coord[1]), Dir.DOWN))
                elif d == Dir.LEFT:
                    q.append(((coord[0] + 1, coord[1]), Dir.UP))
            elif graph[coord[0]][coord[1]] == '|':
                if d == Dir.DOWN:
                    q.append(((coord[0] - 1, coord[1]), Dir.DOWN))
                elif d == Dir.UP:
                    q.append(((coord[0] + 1, coord[1]), Dir.UP))
                else:
                    q.append(((coord[0] - 1, coord[1]), Dir.DOWN))
                    q.append(((coord[0] + 1, coord[1]), Dir.UP))
            elif graph[coord[0]][coord[1]] == '-':
                if d == Dir.RIGHT:
                    q.append(((coord[0], coord[1] + 1), Dir.RIGHT))
                elif d == Dir.LEFT:
                    q.append(((coord[0], coord[1] - 1), Dir.LEFT))
                else:
                    q.append(((coord[0], coord[1] + 1), Dir.RIGHT))
                    q.append(((coord[0], coord[1] - 1), Dir.LEFT))


    # for i in range(len(graph)):
    #     line = ""
    #     for j in range(len(graph[0])):
    #         if (i, j) in visited:
    #             line += '#'
    #         else:
    #             line += '.'
    #     print(line)

    return len(visited)


def part1():
    graph = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            graph.append([c for c in line])

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == ' ':
                graph[i][j] = '#'
    return bfs(graph, (0, 0), Dir.RIGHT)


def part2():
    graph = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            graph.append([c for c in line])


    res = 0
    for i in range(len(graph)):
        res = max(res, bfs(graph, (i, 0), Dir.RIGHT))
        res = max(res, bfs(graph, (i, len(graph[0]) - 1), Dir.LEFT))

    for i in range(len(graph[0])):
        res = max(res, bfs(graph, (0, i), Dir.UP))
        res = max(res, bfs(graph, (len(graph) - 1, i), Dir.DOWN))

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
