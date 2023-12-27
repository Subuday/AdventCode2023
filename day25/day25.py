import collections


def part1():
    graph = collections.defaultdict(list)
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            left, right = line.split(":")
            for node in right.strip().split():
                graph[left].append(node)
                graph[node].append(left)

    edges = collections.defaultdict(lambda: 0)
    for start in graph:
        q = collections.deque([start])
        seen = {start}
        prev = {}

        while q:
            node = q.popleft()
            for nx in graph[node]:
                if nx not in seen:
                    seen.add(nx)
                    q.append(nx)
                    prev[nx] = node

        for node in graph:
            while node != start:
                nx = prev[node]
                edges[(min(nx, node), max(nx, node))] += 1
                node = nx

    edges_by_uses = sorted(edges, key=edges.get)

    for a,b in edges_by_uses[-3:]:
        graph[a].remove(b)
        graph[b].remove(a)

    start = list(graph)[0]
    q = collections.deque([start])
    seen = {start}
    while q:
        node = q.popleft()
        for nx in graph[node]:
            if nx not in seen:
                seen.add(nx)
                q.append(nx)

    return (len(graph) - len(seen)) * len(seen)



def part2():
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
