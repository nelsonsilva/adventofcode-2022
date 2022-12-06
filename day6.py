"""https://adventofcode.com/2022/day/6"""

INPUT = open("day6.txt", encoding="utf-8").read()


def marker(stream, n=4):
    for i in range(len(stream)):
        if len(set(stream[i : i + n])) == n:
            return i + n


def test_marker():
    assert marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert marker("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


print(marker(INPUT))

# PART 2


def test_message():
    assert marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26


print(marker(INPUT, 14))
