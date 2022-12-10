"""https://adventofcode.com/2022/day/10"""


class CPU:
    def __init__(self):
        self.x = 1
        self.xs = []

    def noop(self):
        pass

    def addx(self, n):
        self.tick()
        self.x = self.x + int(n)

    def tick(self):
        self.xs.append(self.x)

    def run(self, program):
        for l in program.split("\n"):
            self.tick()
            [cmd, *args] = l.split()
            getattr(self, cmd)(*args)


def test_small():
    cpu = CPU()
    cpu.run("noop\naddx 3\naddx -5")
    assert cpu.xs == [1, 1, 1, 4, 4]
    assert cpu.x == -1


def signal_strengths(cpu):
    return [(i + 1) * cpu.xs[i] for i in range(19, 220, 40)]


def test_larger():
    cpu = CPU()
    cpu.run(open("day10.test.txt", encoding="utf-8").read())
    assert cpu.xs[19::40] == [21, 19, 18, 21, 16, 18]
    assert sum(signal_strengths(cpu)) == 13140


cpu = CPU()
cpu.run(open("day10.txt", encoding="utf-8").read())
print(sum(signal_strengths(cpu)))

# Part 2
def render(positions):
    for r in range(6):
        print("".join(["#" if abs(positions[r * 40 + x] - x) <= 1 else "." for x in range(40)]))


render(cpu.xs)
