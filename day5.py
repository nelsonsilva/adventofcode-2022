"""https://adventofcode.com/2022/day/5"""

import re

INPUT = open("day5.txt", encoding="utf-8").read()

TEST_INPUT = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2\
"""


def parse(input):
    (stacks, moves) = input.split("\n\n")
    stacks = [stack[1::4] for stack in stacks.split("\n")][:-1]
    stacks = list(zip(*stacks))
    stacks = list(map(lambda stack: [i for i in stack if i != " "][::-1], stacks))
    moves = [tuple(map(int, re.search("move (\d+) from (\d+) to (\d+)", move).groups())) for move in moves.split("\n")]
    return (stacks, moves)


def do_move(stacks, move):
    (n, src, dst) = move
    while n > 0:
        stacks[dst - 1].append(stacks[src - 1].pop())
        n -= 1


def top(stacks):
    return "".join(map(lambda l: l[-1], stacks))


def test_moves():
    [stacks, moves] = parse(TEST_INPUT)
    for move in moves:
        do_move(stacks, move)
    assert top(stacks) == "CMZ"


[stacks, moves] = parse(INPUT)
for move in moves:
    do_move(stacks, move)

print(top(stacks))

# Part 2


def do_new_move(stacks, move):
    (n, src, dst) = move
    lst = []
    while n > 0:
        lst.append(stacks[src - 1].pop())
        n -= 1
    stacks[dst - 1].extend(lst[::-1])


def test_new_moves():
    [stacks, moves] = parse(TEST_INPUT)
    for move in moves:
        do_new_move(stacks, move)
    assert top(stacks) == "MCD"


[stacks, moves] = parse(INPUT)
for move in moves:
    do_new_move(stacks, move)

print(top(stacks))
