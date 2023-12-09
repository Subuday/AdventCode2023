def is_all_zeroes(nums):
    for num in nums:
        if num != 0:
            return False
    return True


def part1():
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    ans = []
    for line in lines:
        nums = list(map(int, line.split(" ")))
        seqs = [nums]
        while not is_all_zeroes(seqs[-1]):
            prev_seq = seqs[-1]
            new_seq = []
            for i in range(1, len(prev_seq)):
                new_seq.append(prev_seq[i] - prev_seq[i - 1])
            seqs.append(new_seq)

        next = 0
        for i in range(len(seqs) - 1, -1, -1):
            next += seqs[i][-1]
        ans.append(next)

    res = 0
    for num in ans:
        res += num

    return res


def part2():
    with open("input.txt", "r") as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))

    ans = []
    for line in lines:
        nums = list(map(int, line.split(" ")))
        seqs = [nums]
        while not is_all_zeroes(seqs[-1]):
            prev_seq = seqs[-1]
            new_seq = []
            for i in range(len(prev_seq) - 1, 0, -1):
                new_seq.insert(0, prev_seq[i] - prev_seq[i - 1])
            seqs.append(new_seq)
        dp = [0 for _ in range(len(seqs))]
        for i in range(len(seqs) - 2, -1, -1):
            dp[i] = seqs[i][0] - dp[i + 1]
        ans.append(dp[0])

    res = 0
    for num in ans:
        res += num

    return res


if __name__ == "__main__":
    print(part1())
    print(part2())
