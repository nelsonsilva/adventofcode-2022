"""https://adventofcode.com/2022/day/11"""

import math, re
from utils import reduce

INPUT = open("day11.txt", encoding="utf-8").read()

TEST_INPUT = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


class Monkey:
    def __init__(self, items, op, test, if_t, if_f):
        self.items = items
        self.op = op.split("=")[1].strip()
        self.divisor = int(re.match("divisible by (\d+)", test)[1])
        self.if_t = int(re.match("throw to monkey (\d+)", if_t)[1])
        self.if_f = int(re.match("throw to monkey (\d+)", if_f)[1])
        self.count = 0

    def inspect(self, item, relief):
        self.count = self.count + 1
        worry = relief(eval(self.op, {"old": item}))
        test = worry % self.divisor == 0
        return [worry, self.if_t if test else self.if_f]

    def turn(self, relief):
        items, self.items = self.items, []
        return [self.inspect(i, relief) for i in items]


def parse(input):
    monkeys = []
    for str in input.split("\n\n"):
        items, op, test, if_t, if_f = re.search(
            "Starting items: ([^\n]+).*Operation: ([^\n]+).*Test: ([^\n]+).*If true: ([^\n]+).*If false: ([^\n]+)",
            str,
            re.MULTILINE | re.DOTALL,
        ).groups()
        monkeys.append(Monkey([int(s.strip()) for s in items.split(",")], op, test, if_t, if_f))
    return monkeys


def do_rounds(monkeys, n=1, relief=lambda w: math.floor(w / 3)):
    for _ in range(n):
        for m in monkeys:
            for item, throw in m.turn(relief):
                monkeys[throw].items.append(item)
    return monkeys


def monkey_business_level(monkeys):
    return reduce(lambda x, y: x * y, sorted([m.count for m in monkeys])[-2:])


def test_monkeys():
    monkeys = parse(TEST_INPUT)
    do_rounds(monkeys)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []
    do_rounds(monkeys, 19)
    assert monkey_business_level(monkeys) == 10605


print(monkey_business_level(do_rounds(parse(INPUT), 20)))

# Part 2
def test_relief():
    monkeys = parse(TEST_INPUT)
    max = math.lcm(*[m.divisor for m in monkeys])
    relief = lambda w: w % max
    do_rounds(monkeys, 1, relief)
    assert [m.count for m in monkeys] == [2, 4, 3, 6]
    do_rounds(monkeys, 19, relief)
    assert [m.count for m in monkeys] == [99, 97, 8, 103]
    do_rounds(monkeys, 980, relief)
    assert [m.count for m in monkeys] == [5204, 4792, 199, 5192]
    do_rounds(monkeys, 9000, relief)
    assert [m.count for m in monkeys] == [52166, 47830, 1938, 52013]
    assert monkey_business_level(monkeys) == 2713310158


monkeys = parse(INPUT)
# LCM (Least Common Multiple)
max = math.lcm(*[m.divisor for m in monkeys])
print(monkey_business_level(do_rounds(monkeys, 10000, lambda w: w % max)))
