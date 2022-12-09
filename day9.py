"""https://adventofcode.com/2022/day/9"""

from utils import reduce

TEST_INPUT = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

DIR = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}


def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def adjacent(t1, t2):
    return abs(t2[0] - t1[0]) <= 1 and abs(t2[1] - t1[1]) <= 1


def keep_up(l, t):
    h = l[-1]
    if not adjacent(h, t):
        kx = 0 if h[0] == t[0] else -1 if h[0] < t[0] else 1
        ky = 0 if h[1] == t[1] else -1 if h[1] < t[1] else 1
        t = add(t, (kx, ky))
    return [*l, t]


def move(k, m):
    visited = set()
    dir, times = DIR[m[0]], int(m[1])
    while times > 0:
        k = reduce(keep_up, k[1:], [add(k[0], dir)])
        visited.add(k[-1])
        times = times - 1
    return k, visited


def count_visited(moves, n=2):
    k = [(0, 0) for n in range(n)]
    visited = set()
    for m in moves:
        k, v = move(k, m)
        visited.update(v)
    return len(visited)


def test_moves():
    assert count_visited([l.split() for l in TEST_INPUT.split("\n")]) == 13


moves = [l.split() for l in open("day9.txt", encoding="utf-8")]

print(count_visited(moves))

# Part 2


def test_mutiple():
    assert count_visited([l.split() for l in TEST_INPUT.split("\n")], 10) == 1


print(count_visited(moves, 10))
