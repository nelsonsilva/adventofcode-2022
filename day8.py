"""https://adventofcode.com/2022/day/8"""

from itertools import product

INPUT = open("day8.txt", encoding="utf-8").read()

TEST_INPUT = """\
30373
25512
65332
33549
35390"""

grid = [list(map(int, row.rstrip())) for row in open("day8.txt", encoding="utf-8")]
rows = len(grid)
cols = len(grid[0])


def find_visible(grid):
    # could've assumed the patch is square to make it easier...
    rows = len(grid)
    cols = len(grid[0])

    visible = set()

    # horizontal
    for r in range(0, rows):
        ml = mr = -1
        for c in range(0, cols):
            # left to right
            if grid[r][c] > ml:
                visible.add((r, c))
                ml = grid[r][c]
            # right to left
            if grid[r][cols - c - 1] > mr:
                visible.add((r, cols - c - 1))
                mr = grid[r][cols - c - 1]

    # vertical
    for c in range(0, cols):
        mt = mb = -1
        for r in range(0, rows):
            # top to bottom
            if grid[r][c] > mt:
                visible.add((r, c))
                mt = grid[r][c]
            # bottom to top
            if grid[rows - r - 1][c] > mb:
                visible.add((rows - r - 1, c))
                mb = grid[rows - r - 1][c]

    return visible


def test_visibel():
    grid = list(map(lambda row: list(map(int, row)), TEST_INPUT.split("\n")))
    assert find_visible(grid) == 21


print(len(find_visible(grid)))

# Part 2


def scenic_score(grid, tree):
    (r, c) = tree
    rows = len(grid)
    cols = len(grid[0])
    h = grid[r][c]
    # left
    ld = 0
    i = c - 1
    while i >= 0:
        ld = ld + 1
        if grid[r][i] >= h:
            break
        i = i - 1
    # right
    rd = 0
    i = c + 1
    while i < cols:
        rd = rd + 1
        if grid[r][i] >= h:
            break
        i = i + 1
    # up
    ud = 0
    i = r - 1
    while i >= 0:
        ud = ud + 1
        if grid[i][c] >= h:
            break
        i = i - 1
    # down
    dd = 0
    i = r + 1
    while i < rows:
        dd = dd + 1
        if grid[i][c] >= h:
            break
        i = i + 1
    return ld * rd * ud * dd


def test_score():
    grid = list(map(lambda row: list(map(int, row)), TEST_INPUT.split("\n")))
    # middle 5 in the second row
    tree = (1, 2)
    assert scenic_score(grid, tree) == 4
    # tree of height 5 in the middle of the fourth row
    tree = (3, 2)
    assert scenic_score(grid, tree) == 8


print(max(map(lambda t: scenic_score(grid, t), product(range(0, rows), range(0, cols)))))
