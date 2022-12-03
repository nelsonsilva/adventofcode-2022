"""https://adventofcode.com/2022/day/3"""

from functools import reduce

INPUT = [line.rstrip() for line in open("day3.txt", encoding="utf-8")]

TEST_INPUT = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]

# Part 1
def compartments(items):
    middle = len(items) // 2
    return [items[:middle], items[middle:]]


def priority(item):
    if item.islower():
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27


def common(lists):
    """Returns first common item in the lists"""
    return list(reduce(lambda a, b: set(a) & set(b), lists))[0]


def test_priority():
    commons = list(map(lambda r: common(compartments(r))[0], TEST_INPUT))
    assert commons == ["p", "L", "P", "v", "t", "s"]
    priorities = list(map(priority, commons))
    assert priorities == [16, 38, 42, 22, 20, 19]


print(sum(map(priority, map(common, map(compartments, INPUT)))))

# Part 2


def split(l, n):
    return [l[i : i + n] for i in range(0, len(l), n)]


def test_groups():
    commons = list(map(common, split(TEST_INPUT, 3)))
    assert commons == ["r", "Z"]
    assert sum(map(priority, commons)) == 70


print(sum(map(priority, map(common, split(INPUT, 3)))))
