"""https://adventofcode.com/2022/day/13"""

from functools import cmp_to_key, reduce

INPUT = open("day13.txt", encoding="utf-8").read()

TEST_INPUT = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parse(input):
    return [[eval(l) for l in p.split()] for p in input.split("\n\n")]


def is_sorted(pair):
    l, r = pair
    if isinstance(l, int) and isinstance(r, int):
        return None if l == r else l < r
    if isinstance(l, int):
        return is_sorted([[l], r])
    if isinstance(r, int):
        return is_sorted([l, [r]])
    for pair in zip(l, r):
        if (s := is_sorted(pair)) != None:
            return s
    return None if len(l) == len(r) else len(l) < len(r)


def test_packets():
    pairs = parse(TEST_INPUT)
    assert is_sorted(pairs[0])
    assert is_sorted(pairs[1])
    assert not is_sorted(pairs[2])
    assert not is_sorted(pairs[4])
    assert list(map(is_sorted, pairs)) == [True, True, False, True, False, True, False, False]
    assert sum([idx + 1 for idx, pair in enumerate(pairs) if is_sorted(pair)]) == 13


print(sum([idx + 1 for idx, pair in enumerate(parse(INPUT)) if is_sorted(pair)]))

# Part 2
DIVIDERS = [[[2]], [[6]]]


def parse_all(input):
    return [eval(l) for l in input.split() if l]


def cmp_packages(a, b):
    return -1 if is_sorted([a, b]) else 1


def mul(lst):
    return reduce(lambda x, y: x * y, lst)


def test_sorted():
    packets = parse_all(TEST_INPUT) + DIVIDERS
    res = sorted(packets, key=cmp_to_key(cmp_packages))
    assert mul([idx + 1 for idx, pair in enumerate(res) if pair in DIVIDERS]) == 140


print(
    mul(
        [
            idx + 1
            for idx, pair in enumerate(sorted(parse_all(INPUT) + DIVIDERS, key=cmp_to_key(cmp_packages)))
            if pair in DIVIDERS
        ]
    )
)
