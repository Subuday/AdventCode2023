import functools

strengths = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

strengths2 = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
}


def hand_type(h):
    dict = {}
    cards = h[0]
    for c in cards:
        dict[c] = dict.get(c, 0) + 1

    if len(dict) == 1:
        return 7  # five of a kind
    elif len(dict) == 2:
        if 4 in dict.values():
            return 6  # four of a kind
        else:
            return 5  # full house
    elif len(dict) == 3:
        if 3 in dict.values():
            return 4  # three of a kind
        else:
            return 3  # two pairs
    elif len(dict) == 4:
        return 2  # one pair
    else:
        return 1  # high card


def items_sort(x1, x2):
    if x1[1] > x2[1]:
        return 1
    elif x1[1] < x2[1]:
        return -1

    if strengths2[x1[0]] > strengths2[x2[0]]:
        return 1
    elif strengths2[x1[0]] < strengths2[x2[0]]:
        return -1

    return 0


def hand_type2(h):
    dict = {}
    cards = h[0]
    for c in cards:
        dict[c] = dict.get(c, 0) + 1

    if 'J' in dict.keys():
        new_cards = str(cards)
        del dict['J']
        items = list(dict.items())
        if not items:
            items.append(('A', 5))
        items.sort(key=functools.cmp_to_key(items_sort))
        new_letter = items[-1][0]
        new_cards = new_cards.replace('J', new_letter)
        return hand_type((new_cards, h[1]))
    else:
        return hand_type(h)


def hands_sort(h1, h2):
    t1 = hand_type(h1)
    t2 = hand_type(h2)

    if t1 > t2:
        return 1
    elif t1 < t2:
        return -1

    for c1, c2 in zip(h1[0], h2[0]):
        if strengths[c1] > strengths[c2]:
            return 1
        elif strengths[c1] < strengths[c2]:
            return -1

    return 0


hands_types = {}


def hands_sort2(h1, h2):
    t1 = hand_type2(h1)
    t2 = hand_type2(h2)

    hands_types[h1[0]] = t1
    hands_types[h2[0]] = t2

    if t1 > t2:
        return 1
    elif t1 < t2:
        return -1

    for c1, c2 in zip(h1[0], h2[0]):
        if strengths2[c1] > strengths2[c2]:
            return 1
        elif strengths2[c1] < strengths2[c2]:
            return -1

    return 0


def part1():
    hands = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            cards = line.split(" ")[0]
            bid = line.split(" ")[1]
            hands.append((cards, int(bid)))

    hands.sort(key=functools.cmp_to_key(hands_sort))

    res = 0
    for i, (_, bid) in enumerate(hands):
        res += ((i + 1) * bid)
    return res


def part2():
    hands = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            cards = line.split(" ")[0]
            bid = line.split(" ")[1]
            hands.append((cards, int(bid)))

    hands.sort(key=functools.cmp_to_key(hands_sort2))

    res = 0
    for i, (_, bid) in enumerate(hands):
        res += ((i + 1) * bid)
    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
