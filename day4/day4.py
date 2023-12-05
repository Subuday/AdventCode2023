def part1():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    cards = []

    for line in lines:
        card_id, nums = line.split(":")
        winning_nums_str, elf_nums_str = nums.strip().split("|")
        winning_nums_str = list(filter(lambda x: x.strip(), winning_nums_str.split(" ")))
        elf_nums_str = list(filter(lambda x: x.strip(), elf_nums_str.split(" ")))

        winning_nums = list(map(lambda s: int(s.strip()), winning_nums_str))
        elf_nums = list(map(lambda s: int(s.strip()), elf_nums_str))
        cards.append((winning_nums, elf_nums))

    res = 0
    for card in cards:
        winning_nums, elf_nums = card
        winning_nums = set(winning_nums)
        i = 0
        for elf_num in elf_nums:
            if elf_num in winning_nums:
                i += 1
        if i != 0:
            res += pow(2, i - 1)
    return res


def part2():
    lines = []
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    cards = []

    for line in lines:
        card_id, nums = line.split(":")
        winning_nums_str, elf_nums_str = nums.strip().split("|")
        winning_nums_str = list(filter(lambda x: x.strip(), winning_nums_str.split(" ")))
        elf_nums_str = list(filter(lambda x: x.strip(), elf_nums_str.split(" ")))

        winning_nums = list(map(lambda s: int(s.strip()), winning_nums_str))
        elf_nums = list(map(lambda s: int(s.strip()), elf_nums_str))
        cards.append((winning_nums, elf_nums))

    cache = {}
    res = 0
    for i in range(len(cards) - 1, -1, -1):
        queue = [i]
        j = 0
        while queue:
            card_id = queue.pop(0)
            card = cards[card_id]
            winning_nums, elf_nums = card
            winning_nums = set(winning_nums)
            k = 1
            for elf_num in elf_nums:
                if elf_num in winning_nums:
                    if card_id + k in cache:
                        j += cache[card_id + k]
                    else:
                        queue.append(card_id + k)
                    k += 1
            j += 1

        cache[i] = j
        res += j

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
