"""https://adventofcode.com/2022/day/2"""

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

strategy = [game.split() for game in open('day2.txt', encoding='utf-8')]

# Part 1
def score(game):
  o, p = game 
  score = {'X': 1, 'Y': 2, 'Z':3}[p]
  # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
  if (p == 'X' and o == 'C') or (p == 'Z' and o == 'B') or (p == 'Y' and o == 'A'):
    score += 6
  elif (p == 'X' and o == 'A') or (p == 'Y' and o == 'B') or (p == 'Z' and o == 'C'):
    score += 3
  return score

def test_strategy():
  input = [['A', 'Y'],['B', 'X'],['C', 'Z']]
  assert list(map(score, input)) == [8, 1, 6]

print(sum((map(score, strategy))))

# Part 2
def choose(game):
  """Translates the strategy into a play. We still use X, Y and Z for the play to reuse the scoring"""
  opponent, outcome = game
  # X : lose, Y : draw, and Z : win.
  if outcome == 'Y':
    play = {'A': 'X', 'B': 'Y', 'C': 'Z'}[opponent]
  elif outcome == 'Z':
    play = 'Y' if opponent == 'A' else 'Z' if opponent == 'B' else 'X'
  elif outcome == 'X':
    play = 'Z' if opponent == 'A' else 'X' if opponent == 'B' else 'Y'
  return [opponent, play]
    

def test_choices():
  input = [['A', 'Y'],['B', 'X'],['C', 'Z']]
  choices = list(map(choose, input))
  assert list(map(score, choices)) == [4, 1, 7]

print(sum(map(score, map(choose, strategy))))