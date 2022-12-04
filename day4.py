"""https://adventofcode.com/2022/day/4"""


def parseRange(s):
    start, end = map(int, s.split("-"))
    return range(start, end + 1)


def parseAssignment(s):
    return list(map(parseRange, s.split(",")))


assignments = [parseAssignment(assignment) for assignment in open("day4.txt", encoding="utf-8")]

TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def contains(r1, r2):
    """Checks if range r1 contains r2"""
    return r2[-1] in r1 and r2[0] in r1


def either_contains(ranges):
    """checks if either range contains the other"""
    return contains(ranges[0], ranges[1]) or contains(ranges[1], ranges[0])


def test_contained():
    assignments = map(parseAssignment, TEST_INPUT.split("\n"))
    contained = list(filter(either_contains, assignments))
    assert len(contained) == 2


print(len(list(filter(either_contains, assignments))))

# Part 2


def overlap(ranges):
    """Checks if the ranges overlap"""
    return len(set(ranges[0]) & set(ranges[1])) != 0


def test_overlaps():
    assignments = map(parseAssignment, TEST_INPUT.split("\n"))
    overlapped = list(filter(overlap, assignments))
    assert len(overlapped) == 4


print(len(list(filter(overlap, assignments))))
