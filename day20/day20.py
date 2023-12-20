import collections
import math


def part1():
    graph = {}
    state = {}
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            line = line.split(" -> ")
            module = line[0].strip()
            type = None
            if module != "broadcaster":
                type = module[0]
                module = module[1:]
            dests = line[1].split(", ")
            graph[module] = dests
            state[module] = {
                "type": type,
                "state": 0,
                "input": {}
            }

    for item in graph.items():
        for dest in item[1]:
            if dest not in state:
                state[dest] = {
                    "type": type,
                    "state": 0,
                    "input": {}
                }
            if state[dest]["type"] == '&':
                state[dest]["input"][item[0]] = 0

    h_p = 0
    l_p = 0
    for _ in range(1000):
        q = collections.deque([("broadcaster", 0, "button")])
        while q:
            module, signal, prev_module = q.popleft()
            if signal == 1:
                h_p += 1
            else:
                l_p += 1
            if module == "broadcaster":
                dests = graph[module]
                for dest in dests:
                    q.append((dest, signal, module))
            elif state[module]["type"] == '%':
                if signal == 0:
                    if state[module]["state"] == 0:
                        state[module]["state"] = 1
                    elif state[module]["state"] == 1:
                        state[module]["state"] = 0
                    for dest in graph[module]:
                        q.append((dest, state[module]["state"], module))
            elif state[module]["type"] == '&':
                input = state[module]["input"]
                input[prev_module]= signal
                all_high_signal = False
                if all(x == 1 for x in input.values()):
                    all_high_signal = True
                if module in graph:
                    for dest in graph[module]:
                        if all_high_signal:
                            q.append((dest, 0, module))
                        else:
                            q.append((dest, 1, module))
            else:
                raise Exception("Unknown type")

    return h_p * l_p


def part2():
    graph = {}
    state = {}
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            line = line.split(" -> ")
            module = line[0].strip()
            type = None
            if module != "broadcaster":
                type = module[0]
                module = module[1:]
            dests = line[1].split(", ")
            graph[module] = dests
            state[module] = {
                "type": type,
                "state": 0,
                "input": {}
            }

    for item in graph.items():
        for dest in item[1]:
            if dest not in state:
                state[dest] = {
                    "type": type,
                    "state": 0,
                    "input": {}
                }
            if state[dest]["type"] == '&':
                state[dest]["input"][item[0]] = 0
    i = 0
    res = {}
    while True:
        if len(res) == 4:
            break
        i += 1
        q = collections.deque([("broadcaster", 0, "button")])
        while q:
            module, signal, prev_module = q.popleft()
            if module == "broadcaster":
                dests = graph[module]
                for dest in dests:
                    q.append((dest, signal, module))
            elif state[module]["type"] == '%':
                if signal == 0:
                    if state[module]["state"] == 0:
                        state[module]["state"] = 1
                    elif state[module]["state"] == 1:
                        state[module]["state"] = 0
                    for dest in graph[module]:
                        q.append((dest, state[module]["state"], module))
            elif state[module]["type"] == '&':
                input = state[module]["input"]
                input[prev_module] = signal
                all_high_signal = False
                if module == "kh":
                    if any(x == 1 for x in input.values()):
                        for k, v in input.items():
                            if v == 1:
                                if k not in res:
                                    res[k] = i
                if all(x == 1 for x in input.values()):
                    all_high_signal = True
                if module in graph:
                    for dest in graph[module]:
                        if all_high_signal:
                            q.append((dest, 0, module))
                        else:
                            q.append((dest, 1, module))
            else:
                raise Exception("Unknown type")

    return math.lcm(*res.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
