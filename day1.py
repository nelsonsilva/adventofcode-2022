"""https://adventofcode.com/2022/day/1"""

txt = open('day1.txt', encoding='utf-8').read()

# part 1
cals = list(map(lambda p: [int(c) for c in p.split('\n')], txt.split('\n\n')))
res = max(map(sum, cals))
print(res)

# part 2
res = sum(sorted(map(sum, cals))[-3:])
print(res)
