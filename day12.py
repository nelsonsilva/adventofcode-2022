"""https://adventofcode.com/2022/day/12"""

INPUT = open("day12.txt", encoding="utf-8").read()

TEST_INPUT = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

DIR = ((0, -1), (0, 1), (1, 0), (-1, 0))


def parse(input):
    grid = []
    for y, r in enumerate(input.split("\n")):
        row = []
        for x, h in enumerate(r):
            if h == "S":
                start = (x, y)
                h = "a"
            if h == "E":
                end = (x, y)
                h = "z"
            row.append(ord(h) - ord("a"))
        grid.append(row)
    return grid, start, end


def options(grid, path):
    rows, cols = len(grid), len(grid[0])
    x, y = path[-1]
    for dx, dy in DIR:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and (grid[ny][nx] - grid[y][x]) <= 1:
            yield nx, ny


def solve(grid, start, end, to_visit=None):
    if to_visit == None:
        to_visit = [[start]]
    seen = set()
    while to_visit:
        path = to_visit.pop()
        if path[-1] == end:
            return path
        for n in options(grid, path):
            if not n in seen:
                seen.add(n)
                to_visit.insert(0, path + [n])


def steps(path):
    return len(path) - 1


def test_solve():
    assert steps(solve(*parse(TEST_INPUT))) == 31


print(steps(solve(*parse(INPUT))))

# Part 2


def low_starts(grid):
    rows, cols = len(grid), len(grid[0])
    return [[(x, y)] for x in range(cols) for y in range(rows) if grid[y][x] == 0]


def test_any():
    grid, _, end = parse(TEST_INPUT)
    assert steps(solve(grid, None, end, low_starts(grid))) == 29


grid, _, end = parse(INPUT)
print(steps(solve(grid, None, end, low_starts(grid))))
