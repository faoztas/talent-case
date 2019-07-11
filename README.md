# Talent Program Case

## Problem

Calculating the best moves in backgammon game.

### Example Input
```
checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}

def find_moves(checkers, dice1, dice2):
    ...
    ...
    ...

print(find_moves(checkers, 6, 1))
```
### Example Output
```
[((1, 7), (6, 7), 3), ((1, 7), (12, 13), 2), ((6, 12), (1, 2), 2), ((6, 12), (6, 7), 2), ((6, 12), (12, 13), 3), ((6, 12), (13, 14), 3), ((12, 18), (12, 13), 2)]
```
### Rules

* Important doors: 5, 6, 7, 8, 17, 18, 19, 20
* Close a door +1 point, if it is important door +2
* Opening a door is -1 points, if it is important door -2
* Unleash a stone -1 points.
* Redeem a stone +1 point.

## Requirements

Python 3.6.8

## How to run

python3 bestmoves.py
