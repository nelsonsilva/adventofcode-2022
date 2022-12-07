"""https://adventofcode.com/2022/day/7"""

INPUT = open("day7.txt", encoding="utf-8").read()

TEST_INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class File:
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    def size(self):
        return self.__size


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def size(self):
        return sum(map(lambda f: f.size(), self.children))


class System:
    def __init__(self):
        self.fs = [Directory("/")]
        self.pwd = self.fs[0]

    def cd(self, args, out):
        dir = args[0]
        if dir == "..":
            self.pwd = self.pwd.parent
        elif dir != "/":  # hacky af
            self.pwd = next(d for d in self.pwd.children if d.name == dir)

    def ls(self, args, out):
        if self.pwd.children:
            return
        for l in out:
            if not l:
                continue
            parts = l.split()
            if parts[0] == "dir":
                entry = Directory(parts[1], self.pwd)
            else:
                entry = File(parts[1], int(parts[0]))
            self.pwd.children.append(entry)

    def parse(self, input):
        for str in input.split("$ ")[1:]:
            out = str.split("\n")
            cmd, out = out[0].split(), out[1:]
            cmd, args = cmd[0], cmd[1:]
            getattr(self, cmd)(args, out)


def find_directories(fn, d: Directory, res=None):
    if res == None:
        res = []
    for c in d.children:
        if isinstance(c, Directory):
            if fn(c):
                res.append(c)
            find_directories(fn, c, res)
    return res


def test_system():
    system = System()
    system.parse(TEST_INPUT)
    assert system.fs[0].size() == 48381165
    dirs = find_directories(lambda f: f.size() < 100000, system.fs[0])
    assert sum(map(lambda d: d.size(), dirs)) == 95437


system = System()
system.parse(INPUT)

print(sum(map(Directory.size, find_directories(lambda f: f.size() < 100000, system.fs[0]))))

# Part 2

TOTAL = 70000000
NEEDED = 30000000


def test_free():
    s = System()
    s.parse(TEST_INPUT)
    to_free = NEEDED - (TOTAL - s.fs[0].size)
    dirs = find_directories(lambda d: d.size() >= to_free, s.fs[0])
    smallest = sorted(dirs, key=Directory.size)[0]
    assert smallest.name == "d"


used = system.fs[0].size()
to_free = NEEDED - (TOTAL - used)
dirs = find_directories(lambda f: f.size() >= to_free, system.fs[0])
print(sorted(dirs, key=Directory.size)[0].size())
